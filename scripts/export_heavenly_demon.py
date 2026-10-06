#!/usr/bin/env python3
"""Export the adopted readers as contiguous image strips for the publishing API."""

import argparse
import functools
import hashlib
import http.server
import json
import math
import os
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parents[1]
SERIES = REPO / "examples/heavenly-demon-ngplus"
DEFAULT_OUTPUT = SERIES / "server-export"
WIDTH = 390
DENSITY = 3
STRIP_HEIGHT = 1800
MAX_IMAGE = 16 * 1024 * 1024


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def save_image(folder, prefix, data, extension="png"):
    if not data or len(data) > MAX_IMAGE:
        raise ValueError(f"Invalid publishing image size: {prefix}")
    digest = hashlib.sha256(data).hexdigest()
    name = f"{prefix}-{digest[:20]}.{extension}"
    (folder / name).write_bytes(data)
    return name, digest, len(data)


def export(output, numbers=None):
    catalog = json.loads((REPO / "content/catalog.json").read_text())
    title = next(item for item in catalog if item["id"] == "heavenly-demon-ngplus")
    handler = functools.partial(QuietHandler, directory=str(REPO))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    output.mkdir(parents=True, exist_ok=True)
    old_manifest = output / "manifest.json"
    if numbers and not old_manifest.exists():
        raise ValueError("A scoped export requires an existing complete manifest")
    old_chapters = json.loads(old_manifest.read_text())["chapters"] if old_manifest.exists() else []
    manifest = {"title": title["title"], "baseURL": "https://manga-server.txcloud.app",
                "method": "Chromium screenshots of adopted HTML body; no extra spacing between strips",
                "cssWidth": WIDTH, "pixelWidth": WIDTH * DENSITY,
                "chapters": [c for c in old_chapters if numbers and c['number'] not in numbers]}
    try:
        with sync_playwright() as p:
            executable = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE") or (
                "/usr/bin/chromium" if Path("/usr/bin/chromium").exists() else None
            )
            browser = p.chromium.launch(executable_path=executable, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": WIDTH, "height": 844}, device_scale_factor=DENSITY)
            for chapter in title["episodes"]:
                number = chapter["number"]
                if numbers and number not in numbers:
                    continue
                episode_id = f"heavenly-demon-episode-{number:02d}"
                folder = output / episode_id
                folder.mkdir(exist_ok=True)
                page.goto(base + "/" + chapter["source"], wait_until="load")
                page.wait_for_function("Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)")
                page.evaluate("document.fonts.ready")
                bounds = page.evaluate("""() => {
                    const main = document.querySelector('main.episode');
                    const header = main.querySelector('header');
                    const footer = main.querySelector('footer');
                    return {top: header.getBoundingClientRect().bottom + scrollY,
                            bottom: footer.getBoundingClientRect().top + scrollY,
                            width: document.documentElement.scrollWidth,
                            ending: Array.from(footer.querySelectorAll('p')).map(e => e.textContent).join('　')};
                }""")
                if bounds["width"] != WIDTH or bounds["bottom"] <= bounds["top"]:
                    raise ValueError(f"Invalid source reader dimensions: {episode_id}")
                top, bottom = math.floor(bounds["top"]), math.ceil(bounds["bottom"])
                alts = page.locator("main.episode img").evaluate_all("els => els.map(e => e.alt)")
                scene = page.locator("main.episode .scene").first
                cover_bytes = scene.screenshot(type="jpeg", quality=88, scale="css")
                cover_name, digest, size = save_image(folder, "cover", cover_bytes, "jpg")
                assets = [{"name": cover_name, "sha256": digest, "bytes": size}]
                blocks = []
                spans = []
                for i, y in enumerate(range(top, bottom, STRIP_HEIGHT), 1):
                    height = min(STRIP_HEIGHT, bottom - y)
                    data = page.screenshot(type="png", full_page=True,
                                           clip={"x": 0, "y": y, "width": WIDTH, "height": height})
                    name, digest, size = save_image(folder, f"strip-{i:02d}", data)
                    assets.append({"name": name, "sha256": digest, "bytes": size})
                    blocks.append({"type": "image", "src": name,
                                   "alt": f"第{number}話「{chapter['title']}」本文 {i}。画像と日本語のセリフを原稿の順番・余白で収録。"})
                    spans.append({"y": y, "height": height, "file": name})
                blocks.append({"type": "ending", "text": bounds["ending"]})
                episode = {"title": title["title"], "subtitle": chapter["title"], "cover": cover_name, "blocks": blocks}
                payload = json.dumps(episode, ensure_ascii=False, indent=2) + "\n"
                if len(payload.encode()) > 256 * 1024 or len(blocks) > 500:
                    raise ValueError(f"Publishing payload too large: {episode_id}")
                (folder / "episode.json").write_text(payload)
                record = {"id": episode_id, "number": number, "title": chapter["title"],
                          "source": chapter["source"], "sourceSHA256": hashlib.sha256((REPO / chapter["source"]).read_bytes()).hexdigest(),
                          "bodyTop": top, "bodyBottom": bottom, "strips": spans,
                          "assets": assets, "sourceImageDescriptions": alts}
                manifest["chapters"].append(record)
                print(f"Exported chapter {number}: {len(spans)} strips, {sum(a['bytes'] for a in assets):,} bytes", flush=True)
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    manifest['chapters'].sort(key=lambda chapter: chapter['number'])
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    current_assets = {(c["id"], a["name"]) for c in manifest["chapters"] for a in c["assets"]}
    for chapter in old_chapters:
        for asset in chapter["assets"]:
            if (chapter["id"], asset["name"]) not in current_assets:
                (output / chapter["id"] / asset["name"]).unlink(missing_ok=True)
    print(f"Ready: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--episode", type=int, action="append", choices=range(1, 11))
    args = parser.parse_args()
    export(args.output.resolve(), args.episode)
