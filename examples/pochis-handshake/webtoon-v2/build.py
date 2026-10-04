#!/usr/bin/env python3
"""Build the static, offline-friendly viewer from episode.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "episode.json"
OUTPUT = ROOT / "index.html"

HTML = r"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#18151d">
<title>__TITLE__</title>
<style>
:root{color-scheme:light;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif;background:#18151d;color:#241e27}
*{box-sizing:border-box}
html,body{margin:0;background:#18151d}
main{width:min(100%,680px);margin:0 auto;overflow:hidden;background:#fffaf3;box-shadow:0 0 64px #0007}
header{min-height:29svh;padding:3.5rem 1.25rem 2.4rem;display:grid;place-content:center;text-align:center;background:linear-gradient(180deg,#fffaf3,#eee1d4)}
h1{margin:0;font-size:clamp(1.9rem,8vw,3rem);line-height:1.38;letter-spacing:.03em}
.subtitle{margin:.7rem 0 0;color:#736671;font-size:clamp(.95rem,3.5vw,1.12rem);letter-spacing:.12em}
.scroll-hint{margin:1.7rem 0 0;color:#8b7d83;font-size:.78rem;letter-spacing:.18em}
.panel{position:relative;display:block;margin-inline:auto;line-height:0}
.panel img{display:block;width:100%;height:auto}
.panel.hero,.panel.wide{width:100%}
.panel.regular{width:92%}
.panel.close{width:76%;max-width:470px}
.panel.align-left{margin-left:0;margin-right:auto}
.panel.align-right{margin-left:auto;margin-right:0}
.balloon{position:absolute;z-index:2;display:block;width:var(--bubble-width,38%);left:var(--bubble-x,50%);top:var(--bubble-y,7%);padding:.78rem .9rem;transform:translateX(-50%);border:2px solid #302936;border-radius:46% / 34%;background:#fffefa;color:#211b24;box-shadow:0 5px 15px #14111c38;font-size:clamp(.95rem,4.3vw,1.35rem);font-weight:800;line-height:1.48;text-align:center}
.balloon:after{content:"";position:absolute;left:27%;bottom:-10px;width:15px;height:15px;border-right:2px solid #302936;border-bottom:2px solid #302936;background:#fffefa;transform:rotate(45deg)}
.speaker{display:block;margin-bottom:.2rem;color:#736671;font-size:.68em;font-weight:650;line-height:1.1}
.words{white-space:pre-line}
.balloon.thought{border-radius:1.2rem;font-size:clamp(.9rem,3.9vw,1.18rem)}
.balloon.thought:after{border-radius:50%;width:11px;height:11px}
.balloon.sfx{padding:.25rem .35rem;border:0;border-radius:0;background:transparent;color:#6d421b;box-shadow:none;font-size:clamp(1.25rem,6vw,1.8rem);font-weight:950;letter-spacing:.06em;transform:translateX(-50%) rotate(-9deg);-webkit-text-stroke:3px #fffaf3;paint-order:stroke fill}
.balloon.sfx:after{display:none}
.caption{display:grid;min-height:5.8rem;place-items:center;padding:1.5rem 1.15rem;text-align:center;font-size:clamp(1.15rem,4.8vw,1.62rem);font-weight:800;line-height:1.7}
.caption.quiet{background:#fffaf3;color:#493640}
.caption.storm{min-height:7rem;background:#1e1a2a;color:#f4eefa;letter-spacing:.08em}
.pause{width:100%;background:#fffaf3}
.pause.storm{background:linear-gradient(180deg,#1e1a2a 0%,#18151f 62%,#1e1a2a 100%)}
.pause.warm{background:linear-gradient(180deg,#fffaf3,#ffe7b9)}
.ending{min-height:34svh;display:grid;align-content:center;justify-items:center;gap:.7rem;padding:3.2rem 1.2rem 4rem;text-align:center;background:linear-gradient(180deg,#ffe9b8,#fffaf3);color:#4d3028}
.ending strong{font-size:clamp(1.55rem,6.5vw,2.35rem);line-height:1.5}
.ending span{font-size:clamp(.95rem,3.8vw,1.15rem);color:#80614f}
footer{padding:1.8rem 1rem 2.5rem;background:#fffaf3;color:#8b7d83;text-align:center;font-size:.75rem;letter-spacing:.1em}
@media(max-width:420px){header{min-height:25svh}.panel.regular{width:96%}.panel.close{width:82%}.balloon{padding:.65rem .7rem}}
@media(prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
</style>
</head>
<body>
<main id="webtoon">
  <header><h1 id="title"></h1><p id="subtitle" class="subtitle"></p><p class="scroll-hint" aria-hidden="true">↓ ゆっくりスクロール</p></header>
</main>
<script type="application/json" id="episode-data">__EPISODE_JSON__</script>
<script>
"use strict";
const episode=JSON.parse(document.getElementById("episode-data").textContent);
const main=document.getElementById("webtoon");
document.title=episode.title+" | "+episode.subtitle;
document.getElementById("title").textContent=episode.title;
document.getElementById("subtitle").textContent=episode.subtitle;
function appendPanel(block){
  const figure=document.createElement("figure");
  figure.className="panel "+(block.size||"regular")+" align-"+(block.align||"center");
  figure.dataset.beat=String(block.beat);
  figure.id=block.id;
  figure.style.marginTop=(block.gapBeforePx||0)+"px";
  figure.style.marginBottom=(block.gapAfterPx||0)+"px";
  if(block.mood)figure.dataset.mood=block.mood;
  const image=document.createElement("img");
  image.src=block.src;image.alt=block.alt;image.loading="lazy";image.decoding="async";
  figure.appendChild(image);
  (block.bubbles||[]).forEach((spec)=>{
    const bubble=document.createElement("div");
    bubble.className="balloon "+(spec.kind||"speech");
    bubble.setAttribute("role","note");
    bubble.setAttribute("aria-label",(spec.speaker?spec.speaker+"：":"")+spec.text.replace(/\s+/g," "));
    bubble.style.setProperty("--bubble-x",(spec.x??50)+"%");
    bubble.style.setProperty("--bubble-y",(spec.y??7)+"%");
    bubble.style.setProperty("--bubble-width",(spec.width??38)+"%");
    if(spec.speaker){const speaker=document.createElement("span");speaker.className="speaker";speaker.textContent=spec.speaker;bubble.appendChild(speaker)}
    const words=document.createElement("span");words.className="words";words.textContent=spec.text;bubble.appendChild(words);
    figure.appendChild(bubble);
  });
  main.appendChild(figure);
}
episode.blocks.forEach((block)=>{
  if(block.type==="panel"){appendPanel(block)}
  else if(block.type==="spacer"){
    const pause=document.createElement("div");pause.className="pause "+(block.tone||"");
    pause.style.height=block.heightVh+"svh";pause.setAttribute("aria-hidden","true");main.appendChild(pause);
  }else if(block.type==="caption"){
    const caption=document.createElement("div");caption.className="caption "+(block.tone||"quiet");
    caption.style.marginTop=(block.gapBeforePx||0)+"px";caption.style.marginBottom=(block.gapAfterPx||0)+"px";
    caption.textContent=block.text;main.appendChild(caption);
  }else if(block.type==="ending"){
    const ending=document.createElement("section");ending.className="ending "+(block.tone||"warm");
    ending.style.marginTop=(block.gapBeforePx||0)+"px";
    const title=document.createElement("strong");title.textContent=block.text;ending.appendChild(title);
    if(block.subtext){const note=document.createElement("span");note.textContent=block.subtext;ending.appendChild(note)}
    main.appendChild(ending);
  }
});
const footer=document.createElement("footer");footer.textContent="9つの物語ビート · 12コマ · v2";main.appendChild(footer);
</script>
</body>
</html>
"""


def main() -> None:
    episode = json.loads(SOURCE.read_text(encoding="utf-8"))
    title = episode["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    payload = json.dumps(episode, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    OUTPUT.write_text(HTML.replace("__TITLE__", title).replace("__EPISODE_JSON__", payload), encoding="utf-8")
    print(f"Built {OUTPUT}")


if __name__ == "__main__":
    main()
