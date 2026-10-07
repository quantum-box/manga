#!/usr/bin/env python3
"""Package the adopted Tower Forge PNGs and proportional white pauses for the server.

The original raster lettering and artwork bytes are copied unchanged. White pause
images scale with the reader width just like CSS cqw; no browser redraw is needed.
"""
import argparse
import io
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SERIES = ROOT / "examples/tower-forge"
sys.path.insert(0, str(ROOT / "scripts"))
from export_latest_webtoons import adopted_chapters, digest


def export(output, numbers):
    if (not isinstance(numbers, list) or len(numbers) != 1
            or type(numbers[0]) is not int or numbers[0] < 1):
        raise ValueError("Each release must export exactly one episode")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Use a new empty output directory for each release")
    chapters = adopted_chapters(series_ids=["tower-forge"], chapter_numbers=numbers)
    if len(chapters) != 1:
        raise ValueError("The selected scope must resolve to exactly one episode")
    from PIL import Image
    output.mkdir(parents=True, exist_ok=True)
    for chapter in chapters:
        folder = SERIES / f"episode-{chapter['number']:02d}"
        script = json.loads((folder / "episode.json").read_text())
        assets = json.loads((folder / "assets.json").read_text())
        if len(assets) != len(script["scenes"]):
            raise ValueError("Reader has not been rebuilt from the adopted script")
        target = output / chapter["id"]
        target.mkdir(exist_ok=True)
        blocks, manifest_assets = [], {}
        css_height = 0
        def save_asset(data, extension):
            sha = digest(data)
            name = f"native-{sha[:24]}.{extension}"
            (target / name).write_bytes(data)
            manifest_assets[name] = {"name": name, "sha256": sha, "bytes": len(data)}
            return name
        if script.get("opening_caption"):
            blocks.append({"type": "caption", "text": script["opening_caption"]})
        for scene, asset in zip(script["scenes"], assets):
            if scene.get("opening_caption"):
                blocks.append({"type": "caption", "text": scene["opening_caption"]})
            source = folder / asset["file"]
            data = source.read_bytes()
            if digest(data) != asset["sha256"]:
                raise ValueError("Adopted image changed after reader build")
            name = save_asset(data, "png")
            dialogue = " ".join(f"{p['speaker']}「{p['text']}」" for p in scene["panels"] if p["text"])
            blocks.append({"type": "image", "src": name, "alt": scene["name"] + "。" + dialogue})
            css_height += 390 * asset["height"] / asset["width"]
            if scene["gap"]:
                blank = io.BytesIO()
                Image.new("RGB", (390, scene["gap"]), "white").save(blank, "PNG")
                blocks.append({"type": "image", "src": save_asset(blank.getvalue(), "png"), "alt": ""})
                css_height += scene["gap"]
        image = Image.open(folder / assets[0]["file"]).convert("RGB")
        image = image.resize((390, round(image.height * 390 / image.width)), Image.Resampling.LANCZOS)
        thumb = io.BytesIO()
        image.save(thumb, "JPEG", quality=88)
        cover = save_asset(thumb.getvalue(), "jpg")
        blocks.append({"type": "ending", "text": "第" + str(chapter["number"]) + "話 おわり"})
        payload = {"title": chapter["title"], "subtitle": chapter["subtitle"], "cover": cover, "blocks": blocks}
        (target / "episode.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        chapter.update(assets=list(manifest_assets.values()), cssHeight=css_height,
                       rasterMethod="unchanged-native-PNG-and-proportional-white-pauses")
        print(f"Prepared {chapter['id']}: {len(script['scenes'])} original PNGs", flush=True)
    manifest = {"baseURL": "https://manga-server.txcloud.app", "seriesIds": ["tower-forge"],
                "chapterNumbers": numbers,
                "chapters": chapters, "catalogSHA256": digest((ROOT / "content/catalog.json").read_bytes())}
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--episode", type=int, action="append", required=True,
                        help="Package one adopted episode; repeated options are rejected")
    args = parser.parse_args()
    export(args.output.resolve(), args.episode)
