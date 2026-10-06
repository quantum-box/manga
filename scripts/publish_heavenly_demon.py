#!/usr/bin/env python3
"""Publish the ten prepared chapters and compare all public payloads and images."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = Path(__file__).resolve().parents[1]
DEFAULT_EXPORT = REPO / "examples/heavenly-demon-ngplus/server-export"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *_args, **_kwargs):
        return None


def read_manifest(folder):
    manifest = json.loads((folder / "manifest.json").read_text())
    chapters = manifest["chapters"]
    if [c["number"] for c in chapters] != list(range(1, 11)):
        raise ValueError("Export must contain chapters 1–10 in order")
    for chapter in chapters:
        episode_id = chapter["id"]
        if episode_id != f"heavenly-demon-episode-{chapter['number']:02d}":
            raise ValueError("Unexpected published chapter ID")
        root = folder / episode_id
        payload = (root / "episode.json").read_bytes()
        episode = json.loads(payload)
        if len(payload) > 256 * 1024 or not episode["blocks"]:
            raise ValueError(f"Invalid episode payload: {episode_id}")
        names = {b["src"] for b in episode["blocks"] if b["type"] == "image"} | {episode["cover"]}
        if names != {a["name"] for a in chapter["assets"]}:
            raise ValueError(f"Asset manifest mismatch: {episode_id}")
        for asset in chapter["assets"]:
            name = asset["name"]
            if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}\.(png|jpg)", name):
                raise ValueError(f"Invalid image filename: {name}")
            data = (root / name).read_bytes()
            signature = b"\x89PNG\r\n\x1a\n" if name.endswith(".png") else b"\xff\xd8\xff"
            if not data.startswith(signature) or len(data) > 16 * 1024 * 1024 or hashlib.sha256(data).hexdigest() != asset["sha256"]:
                raise ValueError(f"Invalid publishing image: {episode_id}/{name}")
        source = REPO / chapter["source"]
        if hashlib.sha256(source.read_bytes()).hexdigest() != chapter["sourceSHA256"]:
            raise ValueError(f"Source changed; regenerate export: {chapter['source']}")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", type=Path, default=DEFAULT_EXPORT)
    parser.add_argument("--base-url", default="https://manga-server.txcloud.app")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    folder = args.export.resolve()
    manifest = read_manifest(folder)
    count = sum(len(c["assets"]) for c in manifest["chapters"])
    print(f"Validated 10 chapters / {count} assets before publishing", flush=True)
    if args.dry_run:
        return
    base = args.base_url.rstrip("/")
    url = urllib.parse.urlsplit(base)
    if url.scheme != "https" or not url.hostname or url.username or url.password or url.query or url.fragment or url.path:
        parser.error("Use an HTTPS origin without user information, path, query, or fragment")
    opener = urllib.request.build_opener(NoRedirect)

    def get(path, token=None):
        headers = {"User-Agent": "manga-series-publisher/1.0"}
        if token is not None:
            headers["Authorization"] = "Bearer " + token
        with opener.open(urllib.request.Request(base + path, headers=headers), timeout=60) as response:
            return response.read()

    if not args.verify_only:
        token = os.environ.get("MANGA_ADMIN_TOKEN", "")
        if len(token) < 32:
            parser.error("Set the production MANGA_ADMIN_TOKEN secret (at least 32 characters)")
        # This read checks authentication without changing existing published content.
        first = manifest["chapters"][0]
        try:
            get(f"/admin/images/{first['id']}/{first['assets'][0]['name']}", token)
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise SystemExit(f"Publishing preflight failed: HTTP {error.code}") from None
        for chapter in manifest["chapters"]:
            subprocess.run([sys.executable, str(REPO / "scripts/publish_episode.py"), base,
                            chapter["id"], str(folder / chapter["id"] / "episode.json")], check=True)
    checks = []
    ids = json.loads(get("/api/episodes"))
    for chapter in manifest["chapters"]:
        episode_id = chapter["id"]
        if episode_id not in ids:
            raise ValueError(f"Published episode missing from list: {episode_id}")
        remote = json.loads(get("/api/episodes/" + episode_id))
        local = json.loads((folder / episode_id / "episode.json").read_text())
        if remote != local:
            raise ValueError(f"Published episode JSON differs: {episode_id}")
        for asset in chapter["assets"]:
            image = get(f"/images/{episode_id}/{asset['name']}")
            if hashlib.sha256(image).hexdigest() != asset["sha256"]:
                raise ValueError(f"Published image differs: {episode_id}/{asset['name']}")
        checks.append({"id": episode_id, "payloadMatches": True, "imagesMatched": len(chapter["assets"])})
        print(f"Verified public chapter {chapter['number']} and all its images", flush=True)
    catalog = json.loads(get("/api/v1/catalog"))
    series = next(s for s in catalog if s["id"] == "online-heavenly-demon")
    numbers = sorted({ep["number"] for ep in series["episodes"]})
    if not set(range(1, 11)).issubset(numbers):
        raise ValueError("Public catalog does not contain chapters 1–10")
    for chapter in manifest["chapters"]:
        ep = next(ep for ep in series["episodes"] if ep["id"] == chapter["id"])
        if ep["number"] != chapter["number"] or ep["title"] != chapter["title"]:
            raise ValueError(f"Public catalog chapter mismatch: {chapter['id']}")
    report = {"baseURL": base, "chapters": checks, "catalogContainsChapters1Through10": True}
    (folder / "published-checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print("Published and verified: " + base + "/?series=online-heavenly-demon")


if __name__ == "__main__":
    main()
