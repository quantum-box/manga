#!/usr/bin/env python3
"""Typeset chapters from unchanged image originals and editable scene scripts."""
import argparse
import base64
import hashlib
import html
import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parent


def esc(value):
    return html.escape(str(value), quote=True)


def cqw(pixels):
    return f"{pixels / 3.9:.4f}cqw"


def lettering(raw, **extra):
    speaker, words = raw.split("|", 1)
    kind = {"T": "thought", "N": "narration"}.get(speaker, "speech")
    return {"type": kind, "text": words, "speaker": speaker[1:] if speaker.startswith("S") else "", **extra}


def compile_blocks(chapter, crops):
    blocks = []
    gaps = [0, 680, 510, 600, 470, 760, 740]
    for number, scene in enumerate(chapter["scenes"], 1):
        scene_id = f"scene-{number}"
        if number > 1:
            blocks.append({"type": "pause", "height": gaps[number-1], "purpose": scene["purpose"]})
        raw = scene["lines"]
        if scene["mode"] != "panels":
            blocks.append(lettering(raw[0], id=scene_id+"-cue"))
            blocks.append({"type": "pause", "height": 950 if scene["mode"] == "hero" else 540, "purpose": scene["purpose"]})
            bounds = crops.get(f"{chapter['number']}-{number}", [0, 100])
            blocks.append({"type": "art", "asset": scene["asset"], "start": bounds[0], "end": bounds[-1], "id": scene_id+"-reveal", "alt": scene["name"], "class": scene["mode"]})
            for i, line in enumerate(raw[1:]):
                blocks.append(lettering(line, align="right" if i % 2 else "left"))
                blocks.append({"type": "pause", "height": [340, 510, 210][i % 3], "purpose": "返事と反応を受け止める"})
            continue
        bounds = crops.get(f"{chapter['number']}-{number}")
        if bounds is None:
            raise ValueError(f"Artwork windows need a visual review: chapter {chapter['number']} scene {number}")
        windows = bounds if isinstance(bounds[0], list) else list(zip(bounds, bounds[1:]))
        if not all(0 <= a < b <= 100 for a, b in windows) or not all(a[1] <= b[0] for a, b in zip(windows, windows[1:])):
            raise ValueError("Windows must be nonoverlapping and sequential")
        for i, (start, end) in enumerate(windows):
            blocks.append({"type": "art", "asset": scene["asset"], "start": start, "end": end, "id": f"{scene_id}-beat-{i+1}", "alt": scene["name"]+f"・動作{i+1}"})
            if i < len(raw):
                blocks.append(lettering(raw[i], align="right" if i % 2 else "left"))
            if i+1 < len(windows):
                blocks.append({"type": "pause", "height": [105, 185, 115, 380][i % 4], "purpose": "小さな動作と反応を分ける"})
        for i, line in enumerate(raw[len(windows):]):
            blocks.append({"type": "pause", "height": 310, "purpose": "動作のあとに残る言葉"})
            blocks.append(lettering(line))
        blocks.append({"type": "pause", "height": 440 if number in (1, 4, 7) else 230, "purpose": scene["purpose"]})
    return blocks


def render(chapter, blocks, assets, css, embedded=False):
    sources = {name: ("data:image/png;base64,"+base64.b64encode(a["bytes"]).decode("ascii") if embedded else "art/"+name+".png") for name,a in assets.items()}
    content = []
    for b in blocks:
        eid = f' id="{esc(b["id"])}"' if b.get("id") else ""
        if b["type"] == "pause":
            content.append(f'<div class="pause"{eid} style="height:{cqw(b["height"])}" aria-hidden="true" data-purpose="{esc(b["purpose"])}"></div>')
        elif b["type"] == "art":
            a=assets[b["asset"]]
            start=round(a["height"]*b["start"]/100);end=round(a["height"]*b["end"]/100)
            if not 0 <= start < end <= a["height"]:
                raise ValueError("Invalid art window")
            height=end-start; offset=-100*start/height
            content.append(f'<figure class="scene {esc(b.get("class",""))}"{eid} data-asset="{esc(b["asset"])}" data-window="{start}:{end}"><div class="art" style="aspect-ratio:{a["width"]}/{height}"><img data-source="{esc(b["asset"])}" width="{a["width"]}" height="{a["height"]}" style="top:{offset:.6f}%" alt="{esc(b["alt"])}" decoding="async"></div></figure>')
        else:
            words="<br>".join(esc(x) for x in b["text"].split("\n"))
            speaker=f'<span class="speaker">{esc(b["speaker"])}</span>' if b.get("speaker") else ""
            content.append(f'<div class="lettering {b["type"]} {esc(b.get("align","left"))}"{eid}><p>{speaker}{words}</p></div>')
    n=chapter["number"]; title=chapter["title"]
    next_note=f'第{n+1}話「{next(c["title"] for c in PLAN["chapters"] if c["number"]==n+1)}」へ続く' if n<10 else "第一の章　終 ／ 物語は続く"
    js='''const sources=JSON.parse(document.getElementById("artwork-sources").textContent);const urls={};for(const [key,source] of Object.entries(sources)){if(source.startsWith("data:image/png;base64,")){const raw=atob(source.slice(source.indexOf(",")+1));const bytes=new Uint8Array(raw.length);for(let i=0;i<raw.length;i++)bytes[i]=raw.charCodeAt(i);urls[key]=URL.createObjectURL(new Blob([bytes],{type:"image/png"}));}else{urls[key]=source;}}for(const img of document.querySelectorAll("img[data-source]")){img.src=urls[img.dataset.source];}const report=()=>{if(window.parent!==window)window.parent.postMessage({type:"webtoon-height",height:document.documentElement.scrollHeight},"*");};addEventListener("load",report);new ResizeObserver(report).observe(document.querySelector("main"));'''
    return '<!doctype html>\n<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#ffffff"><title>剣聖、仇の弟子に転生する｜第'+str(n)+'話 '+esc(title)+'</title><style>\n'+css+'\n</style></head><body><main class="episode"><header><p class="eyebrow">武侠転生譚 ／ 白嶺門</p><h1>剣聖、<br>仇の弟子に<br>転生する</h1><p class="subtitle">第'+str(n)+'話　'+esc(title)+'</p><p class="scroll-hint">下へスクロール ↓</p></header>\n'+'\n'.join(content)+'\n<footer><p>第'+str(n)+'話　終</p><span>'+esc(next_note)+'</span></footer></main><script type="application/json" id="artwork-sources">'+json.dumps(sources,ensure_ascii=False,separators=(",",":")).replace("<","\\u003c")+'</script><script>'+js+'</script></body></html>\n'


PLAN = json.loads((ROOT/"series-plan.json").read_text(encoding="utf-8"))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter",type=int,action="append")
    args=parser.parse_args()
    crops=json.loads((ROOT/"art-windows.json").read_text(encoding="utf-8"))
    css=(ROOT/"episode-01-white-v3/reader.css").read_text(encoding="utf-8")+"\n.speaker{display:block;font-family:-apple-system,BlinkMacSystemFont,sans-serif;font-size:12px;letter-spacing:.12em;color:#6d7b73;margin-bottom:5px}.lettering{padding-top:26px;padding-bottom:26px}\n"
    for planned in PLAN["chapters"]:
        n=planned["number"]
        if args.chapter and n not in args.chapter: continue
        directory=ROOT/f"episode-{n:02d}-white"
        chapter=json.loads((directory/"scene-script.json").read_text(encoding="utf-8"))
        blocks=compile_blocks(chapter,crops); assets={}
        for s in chapter["scenes"]:
            data=(directory/"art"/(s["asset"]+".png")).read_bytes()
            if data[:8]!=b"\x89PNG\r\n\x1a\n":raise ValueError("Expected original PNG")
            width,height=struct.unpack(">II",data[16:24]);assets[s["asset"]]={"bytes":data,"width":width,"height":height}
        (directory/"reader.css").write_text(css,encoding="utf-8")
        (directory/"episode.json").write_text(json.dumps({"title":"剣聖、仇の弟子に転生する","chapter":n,"subtitle":chapter["title"],"readingTargetMinutes":[4,6],"readingTimeMeasured":False,"blocks":blocks},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        for embedded,name in [(False,"index.html"),(True,"reader.html")]:
            (directory/name).write_text(render(chapter,blocks,assets,css,embedded),encoding="utf-8")
        manifest={"chapter":n,"artwork":[{"file":"art/"+name+".png","width":a["width"],"height":a["height"],"sha256":hashlib.sha256(a["bytes"]).hexdigest()} for name,a in assets.items()],"artWindows":sum(b["type"]=="art" for b in blocks),"readingTimeMeasured":False}
        (directory/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print(f"Built chapter {n}: {len(assets)} original illustrations, {manifest['artWindows']} reading windows")


if __name__=="__main__":main()
