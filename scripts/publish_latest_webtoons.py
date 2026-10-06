#!/usr/bin/env python3
"""Publish all adopted chapters, verify bytes, then optionally retire old editions."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def load_manifest(folder):
    manifest = json.loads((folder / "manifest.json").read_text())
    if sha256((ROOT / "content/catalog.json").read_bytes()) != manifest["catalogSHA256"]:
        raise ValueError("Production catalog changed; regenerate the export")
    from export_latest_webtoons import adopted_chapters
    expected = adopted_chapters()
    if [(c["id"], c["sourceDigest"]) for c in manifest["chapters"]] != [
            (c["id"], c["sourceDigest"]) for c in expected]:
        raise ValueError("Export does not match every adopted chapter and its source assets")
    for chapter in manifest["chapters"]:
        episode_id = chapter["id"]
        if not re.fullmatch(r"[a-z0-9-]{1,80}", episode_id):
            raise ValueError("Invalid episode ID")
        payload = (folder / episode_id / "episode.json").read_bytes()
        episode = json.loads(payload)
        if (episode["title"], episode.get("subtitle")) != (chapter["title"], chapter["subtitle"]):
            raise ValueError(f"Publishing title differs: {episode_id}")
        names = {b["src"] for b in episode["blocks"] if b["type"] == "image"} | {episode["cover"]}
        if len(payload) > 256 * 1024 or not names or len(episode["blocks"]) > 500:
            raise ValueError(f"Invalid publishing payload: {episode_id}")
        if names != {a["name"] for a in chapter["assets"]}:
            raise ValueError(f"Asset manifest mismatch: {episode_id}")
        for asset in chapter["assets"]:
            if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}\.(png|jpg|webp)", asset["name"]):
                raise ValueError("Unsafe asset filename")
            data = (folder / episode_id / asset["name"]).read_bytes()
            if not data or len(data) > 16 * 1024 * 1024 or sha256(data) != asset["sha256"]:
                raise ValueError(f"Asset bytes differ: {episode_id}/{asset['name']}")
    return manifest


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *_args, **_kwargs):
        return None


class Client:
    def __init__(self, base, token):
        url = urllib.parse.urlsplit(base)
        if url.scheme != "https" or not url.hostname or url.username or url.password or url.path or url.query or url.fragment:
            raise ValueError("Use an HTTPS origin without credentials, path, query or fragment")
        self.base, self.token = base, token

    def request(self, path, method="GET", data=None, mime=None):
        headers = {"User-Agent": "manga-publisher/1.0", "Cache-Control": "no-cache"}
        if path.startswith("/admin/"):
            headers["Authorization"] = "Bearer " + self.token
        if data is not None:
            headers["Content-Type"] = mime or "application/json"
        for attempt in range(4):
            try:
                opener = urllib.request.build_opener(NoRedirect)
                request = urllib.request.Request(self.base + path, data=data, headers=headers, method=method)
                with opener.open(request, timeout=60) as response:
                    return response.read()
            except urllib.error.HTTPError as error:
                if error.code not in {429, 502, 503, 504} or attempt == 3:
                    raise
            except urllib.error.URLError:
                if attempt == 3:
                    raise
            time.sleep(2 ** attempt)

    def json(self, path):
        return json.loads(self.request(path))


def image_names(episode):
    return {b["src"] for b in episode["blocks"] if b["type"] == "image"} | ({episode["cover"]} if episode.get("cover") else set())


def owned_id(episode_id, series):
    return any(episode_id.startswith(s + "-") for s in series) or ("pochi" in series and episode_id == "pochis-handshake")


def backup_previous(client, folder, manifest):
    backup = folder / "backup"
    backup.mkdir(exist_ok=True)
    snapshot = backup / "previous-ids.json"
    new_ids = {c["id"] for c in manifest["chapters"]}
    series = {c["series"] for c in manifest["chapters"]}
    if snapshot.exists():
        old_ids = json.loads(snapshot.read_text())
    else:
        old_ids = [i for i in client.json("/api/episodes") if owned_id(i, series) and i not in new_ids]
        snapshot.write_text(json.dumps(old_ids, indent=2) + "\n")
    for episode_id in old_ids:
        target = backup / episode_id
        target.mkdir(exist_ok=True)
        payload = target / "episode.json"
        if not payload.exists():
            payload.write_bytes(client.request("/api/episodes/" + episode_id))
        episode = json.loads(payload.read_text())
        for name in image_names(episode):
            destination = target / name
            if not destination.exists():
                destination.write_bytes(client.request(f"/admin/images/{episode_id}/{name}"))
        print("Backed up previous edition " + episode_id, flush=True)
    return old_ids


def verify_chapter(client, folder, chapter):
    episode_id = chapter["id"]
    local = json.loads((folder / episode_id / "episode.json").read_text())
    if client.json("/api/episodes/" + episode_id) != local:
        raise ValueError("Published JSON differs: " + episode_id)
    def verify(asset):
        data = client.request(f"/images/{episode_id}/{asset['name']}")
        if sha256(data) != asset["sha256"]:
            raise ValueError(f"Published image differs: {episode_id}/{asset['name']}")
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(verify, chapter["assets"]))
    print("Verified adopted chapter " + episode_id, flush=True)
    return {"id": episode_id, "imagesMatched": len(chapter["assets"]), "payloadMatches": True}


def verify_catalog(client, manifest, retired=()):
    catalog = client.json("/api/v1/catalog?refresh=" + str(time.time_ns()))
    by_series = {s["id"]: s for s in catalog}
    for chapter in manifest["chapters"]:
        title = by_series["online-" + chapter["series"]]
        episode = next(e for e in title["episodes"] if e["id"] == chapter["id"])
        if (episode["number"], episode["title"], episode["edition"]) != (
                chapter["number"], chapter["subtitle"], chapter["edition"]):
            raise ValueError("Public catalog metadata differs: " + chapter["id"])
    catalog_ids = {e["id"] for s in catalog for e in s["episodes"]}
    if catalog_ids & set(retired):
        raise ValueError("Retired editions remain in the public catalog")
    return catalog


def retire_previous(client, folder, manifest, old_ids):
    new_ids = {c["id"] for c in manifest["chapters"]}
    series = {c["series"] for c in manifest["chapters"]}
    current = set(client.json("/api/episodes"))
    unexpected = {i for i in current if owned_id(i, series)} - new_ids - set(old_ids)
    if unexpected or not new_ids <= current:
        raise ValueError("Public editions changed concurrently; stop before cleanup")
    results = []
    for episode_id in old_ids:
        if episode_id in new_ids or not owned_id(episode_id, series):
            raise ValueError("Cleanup would remove an adopted or unrelated edition")
        payload = folder / "backup" / episode_id / "episode.json"
        episode = json.loads(payload.read_text())
        client.request("/admin/episodes/" + episode_id, "DELETE")
        deleted = 0
        for _ in range(20):
            result = json.loads(client.request("/admin/images/" + episode_id, "DELETE"))
            deleted += result["deleted"]
            if not result["remaining"]:
                break
        else:
            raise ValueError("Image purge did not complete: " + episode_id)
        for path in ["/api/episodes/" + episode_id] + [f"/admin/images/{episode_id}/{n}" for n in image_names(episode)]:
            try:
                client.request(path)
            except urllib.error.HTTPError as error:
                if error.code == 404:
                    continue
                raise
            raise ValueError("Retired object remains accessible: " + path)
        results.append({"id": episode_id, "deletedImages": deleted, "absenceVerified": True})
        print(f"Retired {episode_id}: purged {deleted} image objects", flush=True)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--retire-previous", action="store_true")
    args = parser.parse_args()
    folder = args.export.resolve()
    manifest = load_manifest(folder)
    print(f"Validated {len(manifest['chapters'])} adopted chapters and all exported bytes", flush=True)
    if args.dry_run:
        return
    token = os.environ.get("MANGA_ADMIN_TOKEN", "")
    if not args.verify_only and len(token) < 32:
        parser.error("Set MANGA_ADMIN_TOKEN to the production management secret")
    if args.verify_only and args.retire_previous:
        parser.error("Verification cannot retire editions")
    client = Client(manifest["baseURL"], token)
    old_ids = [] if args.verify_only else backup_previous(client, folder, manifest)
    checks = []
    for chapter in manifest["chapters"]:
        episode_id = chapter["id"]
        if not args.verify_only:
            for asset in chapter["assets"]:
                name = asset["name"]
                data = (folder / episode_id / name).read_bytes()
                mime = {"png": "image/png", "jpg": "image/jpeg", "webp": "image/webp"}[name.rsplit(".", 1)[1]]
                try:
                    client.request(f"/admin/images/{episode_id}/{name}", "PUT", data, mime)
                except urllib.error.HTTPError as error:
                    if error.code != 409 or client.request(f"/admin/images/{episode_id}/{name}") != data:
                        raise
            client.request("/admin/episodes/" + episode_id, "PUT", (folder / episode_id / "episode.json").read_bytes())
        checks.append(verify_chapter(client, folder, chapter))
    verify_catalog(client, manifest)
    retired = retire_previous(client, folder, manifest, old_ids) if args.retire_previous else []
    catalog = verify_catalog(client, manifest, [r["id"] for r in retired])
    report = {"baseURL": client.base, "chapters": checks, "retired": retired,
              "catalog": {s["id"]: len(s["episodes"]) for s in catalog}, "verifiedAt": time.time()}
    (folder / "published-checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"COMPLETE: verified {len(checks)} latest chapters; retired {len(retired)} previous editions", flush=True)


if __name__ == "__main__":
    main()
