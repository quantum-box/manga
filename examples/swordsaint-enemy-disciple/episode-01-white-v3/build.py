#!/usr/bin/env python3
"""Typeset the episode; embed each original PNG once without editing its pixels."""
import base64
import hashlib
import html
import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parent


def esc(value):
    return html.escape(str(value), quote=True)


def space(pixels):
    return f"{pixels / 3.9:.4f}cqw"


def render(episode, assets, embedded):
    references = {}
    for name, asset in assets.items():
        reference = "art/" + name + ".png"
        if embedded:
            reference = "data:image/png;base64," + base64.b64encode(asset["bytes"]).decode("ascii")
        references[name] = reference
    content = []
    for block in episode["blocks"]:
        kind = block["type"]
        element_id = f' id="{esc(block["id"])}"' if block.get("id") else ""
        if kind == "art":
            asset = assets[block["asset"]]
            top = round(asset["height"] * block.get("start", 0) / 100)
            bottom = round(asset["height"] * block.get("end", 100) / 100)
            if not 0 <= top < bottom <= asset["height"]:
                raise ValueError("Invalid artwork window: " + str(block))
            width, height = asset["width"], bottom - top
            gap = space(block.get("gap", 0))
            offset = -100 * top / height
            content.append(f'<figure class="scene {esc(block.get("class", ""))}"{element_id} style="margin-top:{gap}" data-asset="{esc(block["asset"])}" data-window="{top}:{bottom}"><div class="art" style="aspect-ratio:{width}/{height}"><img data-source="{esc(block["asset"])}" width="{width}" height="{asset["height"]}" style="top:{offset:.6f}%" alt="{esc(block["alt"])}" decoding="async"></div></figure>')
        elif kind in ("thought", "speech", "narration", "sound", "final"):
            words = "<br>".join(esc(line) for line in block["text"].split("\n"))
            align = esc(block.get("align", "left"))
            gap = space(block.get("gap", 0))
            content.append(f'<div class="lettering {kind} {align}"{element_id} style="margin-top:{gap}"><p>{words}</p></div>')
        elif kind == "pause":
            content.append(f'<div class="pause"{element_id} style="height:{space(block["height"])}" aria-hidden="true"></div>')
        else:
            raise ValueError("Unknown block: " + kind)
    css = (ROOT / "reader.css").read_text(encoding="utf-8")
    sources = json.dumps(references, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return '<!doctype html>\n<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#ffffff"><title>' + esc(episode["title"]) + '｜第1話 知らない手</title><style>\n' + css + '\n</style></head><body><main class="episode"><header><p class="eyebrow">武侠転生譚 ／ 白嶺門</p><h1>剣聖、<br>仇の弟子に<br>転生する</h1><p class="subtitle">第1話　知らない手</p><p class="scroll-hint">下へスクロール ↓</p></header>\n' + '\n'.join(content) + '\n<footer><p>第1話　終</p><span>第2話「掴めない手」へ続く</span></footer></main><script type="application/json" id="artwork-sources">' + sources + '</script><script>const sources=JSON.parse(document.getElementById("artwork-sources").textContent);const urls={};for(const [key,source] of Object.entries(sources)){if(source.startsWith("data:image/png;base64,")){const raw=atob(source.slice(source.indexOf(",")+1));const bytes=new Uint8Array(raw.length);for(let i=0;i<raw.length;i++)bytes[i]=raw.charCodeAt(i);urls[key]=URL.createObjectURL(new Blob([bytes],{type:"image/png"}));}else{urls[key]=source;}}for(const img of document.querySelectorAll("img[data-source]")){img.src=urls[img.dataset.source];}</script></body></html>\n'


def main():
    episode = json.loads((ROOT / "episode.json").read_text(encoding="utf-8"))
    names = list(dict.fromkeys(block["asset"] for block in episode["blocks"] if block["type"] == "art"))
    assets = {}
    for name in names:
        data = (ROOT / "art" / (name + ".png")).read_bytes()
        if data[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError("Expected PNG: " + name)
        width, height = struct.unpack(">II", data[16:24])
        assets[name] = {"bytes": data, "width": width, "height": height}
    for embedded, filename in ((False, "index.html"), (True, "reader.html")):
        (ROOT / filename).write_text(render(episode, assets, embedded), encoding="utf-8")
    manifest = {"artwork": [{"file": "art/" + name + ".png", "width": a["width"], "height": a["height"], "sha256": hashlib.sha256(a["bytes"]).hexdigest()} for name, a in assets.items()], "artWindows": sum(b["type"] == "art" for b in episode["blocks"]), "readingTime": "4–6 minutes is a target; not measured"}
    (ROOT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built index.html and reader.html; {len(assets)} unchanged artwork originals, {manifest['artWindows']} reading windows")


if __name__ == "__main__":
    main()
