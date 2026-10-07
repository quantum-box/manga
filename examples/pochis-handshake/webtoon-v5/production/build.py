#!/usr/bin/env python3
"""Package only fully drawn episodes; keep all dialogue in the artwork."""
from pathlib import Path
import hashlib
import html
import json
import subprocess
import sys
from PIL import Image

BASE = Path(__file__).resolve().parents[1]
STYLE = """*{box-sizing:border-box}
html,body{margin:0;background:#fffaf3;color:#372e26;font-family:system-ui,sans-serif}
main{width:100%;max-width:420px;margin:auto;container-type:inline-size}
header,footer{padding:26px 20px}
h1{font-size:23px;line-height:1.6;margin:8px 0}
a{color:#276c73}
nav{display:flex;flex-wrap:wrap;gap:14px;line-height:2}
figure{margin:0 0 var(--after,0)}
figure img{display:block;width:100%;height:auto}
.panel-window{position:relative;width:100%;overflow:hidden}
.panel-window img{position:absolute;left:0;top:var(--source-top);max-width:none}
.pause{height:var(--pause);background:#fffaf3}
small{font-size:13px;color:#6b6258}
.chapter-card{display:block;padding:18px 0;border-bottom:1px solid #d5cbbd;text-decoration:none}
.chapter-card strong{display:block;font-size:19px}
.chapter-card span{font-size:14px;color:#60584d}
"""
PLAN = json.loads((BASE / "production/plan.json").read_text())
RECORDS = json.loads((BASE / "production/generation-records.json").read_text())
LAYOUT = json.loads((BASE / "production/scroll-layout.json").read_text())
STYLE_LINK = "reader.css?v=" + hashlib.sha256(STYLE.encode()).hexdigest()[:12]


def write_page(path, document):
    # A returning reader must fetch the new spacing rules at the same episode URL.
    path.write_text(document.replace('href="reader.css"', f'href="{STYLE_LINK}"'), encoding="utf-8")


def scroll_length(px):
    """A narrative interval measured at 360px; track the actual artwork width."""
    return f'{px / LAYOUT["coordinateWidth"] * 100:.5f}cqw'


def render_scene(number, scene):
    """Keep one original; split its display at shared, visually reviewed gutters."""
    cuts = LAYOUT["cuts"].get(f'{number}/{int(scene["id"])}', [])
    width = LAYOUT["coordinateWidth"]
    height = scene["height"] * width / scene["width"]
    boundaries = [[[0, 0], [width, 0]], *(c.get("points", [[0, c["left"]], [width, c["right"]]]) for c in cuts), [[0, height], [width, height]]]
    panel_ends = [0, *(c["afterPanel"] for c in cuts), len(scene["panels"])]
    pieces, windows = [], []
    for index, (upper, lower) in enumerate(zip(boundaries, boundaries[1:])):
        start, end = min(y for x, y in upper), max(y for x, y in lower)
        span = end - start
        assert span > 0 and max(y for x, y in upper) < min(y for x, y in lower)
        first, last = panel_ends[index], panel_ends[index + 1]
        assert first < last
        spoken = "／".join(p["speaker"] + "：" + p["text"] for p in scene["panels"][first:last] if p["text"])
        alt = scene["label"] + "。" + (spoken or "無言の動作。")
        image = f'<img src="{scene["filename"]}" width="{scene["width"]}" height="{scene["height"]}" alt="{html.escape(alt, quote=True)}">'
        if not cuts:
            pieces.append(image)
        else:
            polygon = ",".join(f'{x/width*100:.5f}% {(y-start)/span*100:.5f}%' for x, y in upper + list(reversed(lower)))
            region = html.escape(json.dumps({"upper": upper, "lower": lower}, separators=(",", ":")), quote=True)
            pieces.append(f'<div class="panel-window" data-panels="{first+1}-{last}" data-source-region="{region}" style="aspect-ratio:{width}/{span:.5f};--source-top:{-start/span*100:.5f}%;clip-path:polygon({polygon})">{image}</div>')
        windows.append({"panels": [first+1, last], "upper": list(upper), "lower": list(lower), "source": scene["filename"]})
        if index < len(cuts):
            cut = cuts[index]
            pieces.append(f'<div class="pause" aria-hidden="true" data-purpose="{html.escape(cut["purpose"], quote=True)}" style="--pause:{scroll_length(cut["pause"])}"></div>')
    scene["scroll_windows"] = windows
    scene["internal_pauses"] = cuts
    return f'<figure id="scene-{scene["id"]}" data-artwork="{scene["filename"]}" style="--after:{scroll_length(scene["gap_after"])}">'+"".join(pieces)+"</figure>"


DRAWN = {e["number"] for e in PLAN if all((BASE / f'episode-{e["number"]:02}' / s["filename"]).is_file() for s in e["scenes"])}
completed = []
all_chapters = []
for episode in PLAN:
    number = episode["number"]
    folder = BASE / f"episode-{number:02}"
    if not all((folder / scene["filename"]).is_file() for scene in episode["scenes"]):
        continue
    previous = {s["id"]: s for s in json.loads((folder / "scenes.json").read_text())} if (folder / "scenes.json").is_file() else {}
    figures, storyboard, prompts = [], [], []
    for scene in episode["scenes"]:
        art = folder / scene["filename"]
        original = art
        source_digest = hashlib.sha256(original.read_bytes()).hexdigest()
        with Image.open(original) as picture:
            scene["width"], scene["height"] = picture.size
            art = original.with_suffix(".webp")
            if not art.is_file() or previous.get(scene["id"], {}).get("original_sha256") != source_digest:
                picture.convert("RGB").save(art, format="WEBP", quality=93, method=4)
        scene["raster_original"] = scene["filename"]
        scene["original_sha256"] = source_digest
        scene["filename"] = art.relative_to(folder).as_posix()
        scene["sha256"] = hashlib.sha256(art.read_bytes()).hexdigest()
        figures.append(render_scene(number, scene))
        storyboard.append(f'## {scene["id"]} {scene["label"]}\n\n採用画像: {scene["filename"]}\n\n場面の後: 360px幅で {scene["gap_after"]}px、本文幅に比例。{scene["pacing"]}\n\n')
        for cut in scene["internal_pauses"]:
            storyboard.append(f'コマ{cut["afterPanel"]}の後: 360px幅で {cut["pause"]}px。{cut["purpose"]}。原画の境界は左 {cut["left"]}px / 右 {cut["right"]}px。\n\n')
        for i, panel in enumerate(scene["panels"], 1):
            storyboard.append(f'{i}. {panel["visual"]}\n   発話: {panel["speaker"] or "なし"} / {panel["text"] or "無言"}\n   縦列（右→左）: {" / ".join(panel["columns"]) or "なし"}\n')
        initial = next(r for r in RECORDS if r["episode"] == number and r["scene"] == scene["id"] and not r.get("edit_source"))
        prompts.append(f'## {scene["id"]} {scene["label"]}\n\n採用: {scene["filename"]}\n\n{initial["prompt"]}\n\n')
    links = ['<a href="../chapters.html">話一覧</a>']
    if number - 1 in DRAWN:
        links.append(f'<a href="../episode-{number-1:02}/index.html">前の話</a>')
    if number + 1 in DRAWN:
        links.append(f'<a href="../episode-{number+1:02}/index.html">次の話</a>')
    title = f'第{number}話 {episode["title"]}'
    document = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'｜転生したら柴犬だった。</title><link rel="stylesheet" href="reader.css"></head><body><main><header><small>転生したら柴犬だった。</small><h1>'+title+'</h1></header>'+"\n".join(figures)+'<footer><nav>'+" ".join(links)+'</nav><p>第'+str(number)+'話 おわり</p></footer></main></body></html>'
    write_page(folder / "index.html", document)
    all_figures = [f.replace('src="art/', f'src="episode-{number:02}/art/').replace('id="scene-', f'id="episode-{number:02}-scene-') for f in figures]
    all_chapters.append(f'<section id="episode-{number:02}"><header><small>転生したら柴犬だった。</small><h1>{title}</h1></header>'+"\n".join(all_figures)+'</section>')
    (folder / "reader.css").write_text(STYLE, encoding="utf-8")
    (folder / "scenes.json").write_text(json.dumps(episode["scenes"], ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    (folder / "storyboard.md").write_text(f'# {title}\n\n目的: {episode["goal"]}\n\n開始: {episode["start"]}\n\n終了: {episode["end"]}\n\n'+ "".join(storyboard), encoding="utf-8")
    edits = [r for r in RECORDS if r["episode"] == number and r.get("edit_source")]
    prompts.extend(f'## 修正 {r["scene"]}\n\n編集元: {r["edit_source"]}\n採用: {r["adopted"]}\n\n{r["prompt"]}\n\n' for r in edits)
    (folder / "PROMPTS.md").write_text((f'# {title} 実際の生成指示\n\n'+"".join(prompts)).rstrip()+"\n", encoding="utf-8")
    package = BASE.parents[2]/"skills/webtoon/scripts/package_reader.py"
    subprocess.run([sys.executable, str(package), str(folder/"index.html"), "--output", str(folder/"reader.html"), "--force"], check=True, capture_output=True)
    completed.append(number)
(BASE/"reader.css").write_text(STYLE, encoding="utf-8")
cards = '<nav><a href="all.html">全話を続けて読む</a></nav>' + "".join(f'<a class="chapter-card" href="episode-{e["number"]:02}/index.html"><strong>第{e["number"]}話 {e["title"]}</strong><span>{html.escape(e["goal"])}</span></a>' for e in PLAN if e["number"] in completed)
write_page(BASE/"chapters.html", '<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>転生したら柴犬だった。 話一覧</title><link rel="stylesheet" href="reader.css"><main><header><h1>転生したら柴犬だった。</h1><p>言葉が通じなくても、できることはある。</p></header>'+cards+'</main></html>')
write_page(BASE/"all.html", '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>転生したら柴犬だった。 全話通読</title><link rel="stylesheet" href="reader.css"></head><body><main><header><nav><a href="chapters.html">話一覧</a></nav></header>'+"\n".join(all_chapters)+'<footer><a href="chapters.html">話一覧へ</a></footer></main></body></html>')
print(json.dumps({"packaged":completed,"planned":len(PLAN)}, ensure_ascii=False))
