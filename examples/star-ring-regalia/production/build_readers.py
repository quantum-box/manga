#!/usr/bin/env python3
"""Build the adopted episode readers without changing artwork bytes."""
import argparse
import html
import importlib.util
import json
from pathlib import Path
import struct
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKAGER = ROOT.parents[1] / 'skills/webtoon/scripts/package_reader.py'
CSS = '''*{box-sizing:border-box}html{background:#fff;color:#2d363b}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans",sans-serif}main{width:min(100%,420px);margin:auto;container-type:inline-size}header{padding:36px 24px 12px}header p{font-size:12px;letter-spacing:.12em;color:#667679}h1{font-size:24px;line-height:1.55;margin:8px 0 20px}figure{padding:0;margin:0;width:100%}figure img{display:block;width:100%;height:auto} .pause{height:var(--gap);background:#fff}footer{padding:70px 24px 100px;text-align:center}footer p{color:#667679;font-size:13px}nav{display:flex;flex-wrap:wrap;justify-content:center;gap:14px}a{color:#316366;text-underline-offset:5px;line-height:1.8}a:focus-visible{outline:3px solid #8abdb5;outline-offset:4px}.series{max-width:650px;margin:0 auto;padding:44px 24px}.series h1{font-size:32px}.series ol{padding-left:24px}.series li{padding:12px 0;border-bottom:1px solid #edf0eb}.series .intro{line-height:1.9;color:#536163}.pending{color:#929b9b}'''

def size(path):
    raw = path.read_bytes()[:24]
    if raw[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError(f'Expected source PNG: {path}')
    return struct.unpack('>II', raw[16:24])

def build_episode(ep):
    number = ep['number']
    directory = ROOT / f'episode-{number:02d}'
    assets = ep['assets']
    adoption = json.loads((directory/'adoption.json').read_text()) if (directory/'adoption.json').is_file() else {}
    if not all((directory/'art'/adoption.get(a['id'], f"{a['id']}.png")).is_file() for a in assets):
        return False
    parts = [f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>星環のレガリア 第{number}話 {html.escape(ep["title"])}</title><meta name="manga-title-id" content="star-ring-regalia"><meta name="manga-episode-id" content="episode-{number:02d}"><link rel="stylesheet" href="reader.css"></head><body><main class="episode"><header><p>星環のレガリア / 第{number}話</p><h1>{html.escape(ep["title"])}</h1></header>']
    geometry = []
    for i, asset in enumerate(assets):
        adopted = adoption.get(asset['id'], f"{asset['id']}.png")
        width, height = size(directory/'art'/adopted)
        gap = asset['gap_before_390'] if i else 0
        if gap:
            parts.append(f'<div class="pause" style="--gap:{gap/3.9:.6f}cqw" data-pacing-purpose="{html.escape(asset["pacing_purpose"], quote=True)}" aria-hidden="true"></div>')
        loading = 'eager' if i == 0 else 'lazy'
        parts.append(f'<figure id="{asset["id"]}" data-reveal="{str(asset["reveal"]).lower()}"><img src="art/{adopted}" width="{width}" height="{height}" alt="{html.escape(asset["alt"], quote=True)}" loading="{loading}" decoding="async"></figure>')
        geometry.append({'id':asset['id'],'adoptedArt':f'art/{adopted}','nativeWidth':width,'nativeHeight':height,'gapBefore390':gap,'pacingPurpose':asset['pacing_purpose'],'reveal':asset['reveal']})
    nav = []
    if number > 1 and (ROOT/f'episode-{number-1:02d}/index.html').is_file():
        nav.append(f'<a href="../episode-{number-1:02d}/index.html">前の話</a>')
    nav.append('<a class="series-index" href="../index.html">話一覧</a>')
    if (ROOT/f'episode-{number+1:02d}/index.html').is_file():
        nav.append(f'<a href="../episode-{number+1:02d}/index.html">次の話</a>')
    parts.append(f'<footer><p>第{number}話　了</p><nav aria-label="話の移動">{"".join(nav)}</nav></footer></main><script>if(window.webkit&&window.webkit.messageHandlers){{document.querySelectorAll(".series-index").forEach(a=>a.remove())}}</script></body></html>')
    (directory/'index.html').write_text('\n'.join(parts)+'\n',encoding='utf-8')
    (directory/'reader.css').write_text(CSS+'\n',encoding='utf-8')
    (directory/'layout.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    subprocess.run([sys.executable,str(PACKAGER),str(directory/'index.html'),'--output',str(directory/'reader.html'),'--force'],check=True)
    # Use the repository's lossless offline transport for large full episodes.
    # Artwork bytes are restored unchanged; companion files remain below 50 MiB.
    if (directory/'reader.html').stat().st_size >= 100 * 1024 * 1024:
        transport = ROOT.parent/'tower-farm-kitchen/production/compact_reader.py'
        spec = importlib.util.spec_from_file_location('webtoon_compact_transport', transport)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.compact(directory/'reader.html')
    return True

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--episode',type=int)
    args=parser.parse_args()
    episodes=json.loads((ROOT/'production/episodes.json').read_text())
    built=[]
    for ep in episodes:
        if args.episode and ep['number'] != args.episode:
            continue
        if build_episode(ep): built.append(ep['number'])
    links=[]
    for ep in episodes:
        n=ep['number']; title=html.escape(ep['title'])
        if (ROOT/f'episode-{n:02d}/index.html').is_file():
            links.append(f'<li><a href="episode-{n:02d}/index.html">第{n}話　{title}</a></li>')
    (ROOT/'index.html').write_text(f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>星環のレガリア</title><style>{CSS}</style></head><body><div class="series"><p>剣と魔法 × 日本 × ゲーム</p><h1>星環のレガリア</h1><p class="intro">補欠の高校生・朝倉航は、ゲームの向こうで名前を呼ばれた。<br>竜が飛ぶ空も、笑い合った町も、明日を生きている。</p><ol>{"".join(links)}</ol></div></body></html>\n',encoding='utf-8')
    print('Built episodes: '+', '.join(map(str,built)))

if __name__=='__main__':main()
