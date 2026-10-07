#!/usr/bin/env python3
"""Export every adopted chapter at phone width, with revision IDs and provenance."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess

from sync_ios_webtoons import reader_files

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def adopted_chapters(root=ROOT, series_ids=None, chapter_numbers=None):
    root = root.resolve()
    catalog = json.loads((root / "content/catalog.json").read_text())
    if series_ids is not None:
        if not isinstance(series_ids, list) or not series_ids or any(not isinstance(s, str) for s in series_ids):
            raise ValueError("Series scope must be a nonempty list of series IDs")
        available = {"heavenly-demon" if t["id"] == "heavenly-demon-ngplus" else t["id"] for t in catalog}
        if len(set(series_ids)) != len(series_ids) or set(series_ids) - available:
            raise ValueError("Series scope contains a duplicate or unknown series ID")
    if chapter_numbers is not None:
        if (series_ids is None or len(series_ids) != 1 or not isinstance(chapter_numbers, list)
                or not chapter_numbers or any(type(n) is not int or n < 1 for n in chapter_numbers)
                or len(set(chapter_numbers)) != len(chapter_numbers)):
            raise ValueError("Chapter scope requires one series and distinct positive chapter numbers")
        numbers = {e["number"] for t in catalog
                   if ("heavenly-demon" if t["id"] == "heavenly-demon-ngplus" else t["id"]) == series_ids[0]
                   for e in t["episodes"]}
        if set(chapter_numbers) - numbers:
            raise ValueError("Chapter scope contains an unknown chapter")
    chapters = []
    for title in catalog:
        seen = set()
        series = "heavenly-demon" if title["id"] == "heavenly-demon-ngplus" else title["id"]
        if series_ids is not None and series not in series_ids:
            continue
        for episode in title["episodes"]:
            if chapter_numbers is not None and episode["number"] not in chapter_numbers:
                continue
            if episode["number"] in seen:
                continue
            seen.add(episode["number"])
            source = (root / episode["source"]).resolve()
            provenance = {str(path.relative_to(source.parent)): digest(path.read_bytes())
                          for path in sorted(reader_files(source))}
            source_digest = digest(json.dumps(provenance, sort_keys=True).encode())
            episode_id = f"{series}-episode-{episode['number']:02d}-r{source_digest[:12]}"
            if len(episode_id) > 80:
                raise ValueError("Episode ID exceeds server limit")
            chapters.append({"id": episode_id, "series": series, "number": episode["number"],
                             "title": title["title"], "subtitle": episode["title"],
                             "edition": "", "source": episode["source"],
                             "sourceDigest": source_digest, "provenance": provenance})
    return chapters


def export(output, node="node", chromium=None, series_ids=None):
    from PIL import Image
    output.mkdir(parents=True, exist_ok=True)
    chapters = adopted_chapters(series_ids=series_ids)
    sources = {c["id"]: dict(source=str(ROOT / c["source"]), subtitle=c["subtitle"],
                              sourceDigest=c["sourceDigest"], bodyOnly=True) for c in chapters}
    source_list = output / "sources.json"
    source_list.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n")
    raw = output / "raw"
    command = [node, str(ROOT / "scripts/render_retina_reader.cjs"), str(source_list), str(raw)]
    if chromium:
        command.append(chromium)
    subprocess.run(command, check=True)
    for chapter in chapters:
        source = raw / chapter["id"]
        metadata = json.loads((source / "render.json").read_text())
        if metadata["sourceDigest"] != chapter["sourceDigest"]:
            raise ValueError("Cached rendering does not match adopted source")
        folder = output / chapter["id"]
        folder.mkdir(exist_ok=True)
        blocks, assets = [], []
        for block in metadata["blocks"]:
            data = (source / block["src"]).read_bytes()
            image = Image.open(io.BytesIO(data))
            if image.width != 1170:
                raise ValueError("Rendered strip must be 1170 pixels wide")
            compressed = io.BytesIO()
            image.convert("RGB").save(compressed, format="WEBP", quality=93, method=4)
            extension = "png"
            if len(compressed.getvalue()) < len(data) * 0.8:
                data, extension = compressed.getvalue(), "webp"
            sha = digest(data)
            name = f"retina-{sha[:24]}.{extension}"
            (folder / name).write_bytes(data)
            blocks.append(dict(block, src=name))
            assets.append({"name": name, "sha256": sha, "bytes": len(data)})
        cover = metadata["cover"]
        cover_bytes = (source / cover).read_bytes()
        (folder / cover).write_bytes(cover_bytes)
        assets.append({"name": cover, "sha256": digest(cover_bytes), "bytes": len(cover_bytes)})
        ending = "\n".join(line.strip() for line in metadata["ending"].splitlines()
                           if line.strip() and line.strip() not in {"話一覧", "前の話", "次の話"})
        blocks.append({"type": "ending", "text": ending or "おわり"})
        episode = {"title": chapter["title"], "subtitle": chapter["subtitle"], "cover": cover, "blocks": blocks}
        (folder / "episode.json").write_text(json.dumps(episode, ensure_ascii=False, indent=2) + "\n")
        chapter.update(assets=assets, cssHeight=metadata["cssHeight"], pixelWidth=1170)
        print(f"Prepared {chapter['id']}: {len(blocks)-1} strips", flush=True)
    manifest = {"baseURL": "https://manga-server.txcloud.app", "chapters": chapters,
                "catalogSHA256": digest((ROOT / "content/catalog.json").read_bytes())}
    if series_ids is not None:
        manifest["seriesIds"] = series_ids
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Ready: {len(chapters)} adopted chapters in {output}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--node", default=os.environ.get("NODE_EXECUTABLE", "node"))
    parser.add_argument("--chromium")
    parser.add_argument("--series", action="append", help="Export only this series; repeat for multiple series")
    args = parser.parse_args()
    export(args.output.resolve(), args.node, args.chromium, args.series)
