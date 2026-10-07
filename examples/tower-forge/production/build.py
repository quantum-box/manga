#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build episodes whose adopted raster scenes exist; length follows the story."""
import hashlib
import html
import json
import struct
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGER = ROOT.parents[1] / 'skills/webtoon/scripts/package_reader.py'
STYLE = '''*{box-sizing:border-box}html{color-scheme:light}body{margin:0;background:#e5e9ee;color:#273347;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN",sans-serif}main{width:100%;max-width:640px;margin:auto;background:white;container-type:inline-size}header{padding:42px 22px 32px;text-align:center;background:#fff}header a,footer a{color:#365178;text-decoration:none;font-size:16px}header p{font-size:16px;margin:24px 0 10px;letter-spacing:.12em}h1{font-size:28px;line-height:1.5;margin:0}figure{margin:0}figure img{display:block;width:100%;height:auto}.gap{height:var(--gap);background:white}footer{padding:45px 24px;text-align:center;display:flex;gap:24px;justify-content:center}footer a{font-size:18px}a:focus-visible{outline:3px solid #d98238;outline-offset:4px}'''

def dims(path):
    data=path.read_bytes()
    if data[:8]!=b'\x89PNG\r\n\x1a\n':raise ValueError(f'Expected PNG: {path}')
    return struct.unpack('>II',data[16:24])

def main():
    eps=[json.loads((ROOT/f'episode-{n:02d}/episode.json').read_text(encoding='utf-8')) for n in range(1,11)]
    adopted_file=ROOT/'production/adopted-assets.json'
    adopted=json.loads(adopted_file.read_text(encoding='utf-8')) if adopted_file.exists() else {}
    ready=[]
    for ep in eps:
        n=ep['number'];d=ROOT/f'episode-{n:02d}'
        files=[adopted.get(f'{n}-{i}',{}).get('file',s['file']) for i,s in enumerate(ep['scenes'],1)]
        if not all((d/file).exists() for file in files):continue
        parts=[f'<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>塔を灯す剣｜第{n}話</title><style>{STYLE}</style><main><header><a href="../chapters.html">話一覧</a><p>塔を灯す剣 · 第{n}話</p><h1>{html.escape(ep["title"])}</h1></header>']
        if ep.get('opening_caption'):
            parts.append(f'<p style="padding:20px 28px 50px;margin:0;text-align:center;line-height:1.9;font-size:18px">{html.escape(ep["opening_caption"])}</p>')
        hashes=[]
        for i,(scene,file) in enumerate(zip(ep['scenes'],files),1):
            if scene.get('opening_caption'):
                parts.append(f'<p style="padding:24px 28px;margin:0;text-align:center;line-height:1.9;font-size:18px">{html.escape(scene["opening_caption"])}</p>')
            path=d/file;w,h=dims(path)
            texts=' '.join(f'{p["speaker"]}「{p["text"]}」' for p in scene['panels'] if p['text'])
            sounds=' '.join(sound['text'] for p in scene['panels'] for sound in p.get('sounds',[]))
            if sounds:texts+=' 効果音：'+sounds
            ui=' '.join(line for p in scene['panels'] for window in p.get('ui',[]) for line in window['lines'])
            if ui:texts+=' HUD：'+ui
            alt=f'{scene["name"]}。{scene["location"]}。{texts}。会話は縦書きの吹き出しとして画像に含む。'
            parts.append(f'<figure id="scene-{i:02d}"><img src="{file}" width="{w}" height="{h}" alt="{html.escape(alt,quote=True)}"></figure>')
            if scene['gap']:parts.append(f'<div class="gap" aria-hidden="true" style="--gap:{scene["gap"]/3.9:.3f}cqw"></div>')
            hashes.append(dict(file=file,width=w,height=h,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        parts.append('<footer>')
        if n>1:parts.append(f'<a href="../episode-{n-1:02d}/index.html">前の話</a>')
        parts.append('<a href="../chapters.html">話一覧</a>')
        if n<10 and all((ROOT/f'episode-{n+1:02d}'/adopted.get(f'{n+1}-{i}',{}).get('file',s['file'])).exists() for i,s in enumerate(eps[n]['scenes'],1)):
            next_label='次の話（初稿）' if ep.get('revision') and not eps[n].get('revision') else '次の話'
            parts.append(f'<a href="../episode-{n+1:02d}/index.html">{next_label}</a>')
        parts.append('</footer></main></html>')
        (d/'index.html').write_text('\n'.join(parts),encoding='utf-8')
        subprocess.run(['python3',str(PACKAGER),str(d/'index.html'),'--output',str(d/'reader.html'),'--force'],check=True,capture_output=True)
        (d/'assets.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        ready.append(n)
    cards=[]
    for ep in eps:
        n=ep['number']
        if n in ready:
            note='改稿' if ep.get('revision') else '初稿・改稿待ち'
            cards.append(f'<a class="card" href="episode-{n:02d}/index.html"><strong>第{n}話</strong><span>{html.escape(ep["title"])}<small style="display:block;margin-top:8px">{note}</small></span></a>')
        else:cards.append(f'<div class="card pending"><strong>第{n}話</strong><span>{html.escape(ep["title"])}</span><small>脚本完成・作画中</small></div>')
    page='''<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>塔を灯す剣｜第1〜10話</title><style>*{box-sizing:border-box}body{margin:0;background:#f6f4ef;color:#253148;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN",sans-serif}main{max-width:760px;margin:auto;padding:40px 24px 80px}h1{font-size:36px;margin:20px 0}p{line-height:1.9;font-size:18px}.eyebrow{font-size:14px;color:#6b7280;letter-spacing:.14em}.card{display:flex;gap:16px;padding:22px 0;border-top:1px solid #cbd0d4;color:inherit;text-decoration:none;font-size:18px;line-height:1.5}.pending{color:#8b9097}.card small{font-size:12px}.hero{width:100%;height:auto;display:block;margin:24px 0}.links a{color:#365178}</style><main><p class="eyebrow">VRMMORPG · 剣と魔法 · 塔攻略</p><h1>塔を灯す剣</h1><p>自分の作った剣で、未踏の塔へ。<br>三人の遠征は、消えた街の灯りから始まる。</p>'''
    if ready:
        page+='<p><a href="episode-01/index.html" style="display:inline-block;padding:14px 24px;background:#253148;color:white;text-decoration:none;border-radius:4px">第1話から読む</a></p>'
        cover_scene=eps[0].get('cover_scene',1)
        cover=adopted.get(f'1-{cover_scene}',{}).get('file',eps[0]['scenes'][cover_scene-1]['file'])
        page+=f'<img class="hero" style="height:clamp(190px,42vw,400px);object-fit:cover;object-position:center 50%" src="episode-01/{cover}" alt="巨大な塔のある剣と魔法の街リューメル">'
    page+=''.join(cards)+'<p class="links"><a href="series/bible.md">企画と設定</a> · <a href="series/technical-design.md">技術設計</a></p></main></html>'
    (ROOT/'chapters.html').write_text(page,encoding='utf-8')
    (ROOT/'production/build-status.json').write_text(json.dumps(dict(ready_episodes=ready,expected_episodes=list(range(1,11))),indent=2)+'\n')
    print('Readable episodes: '+', '.join(map(str,ready)))

if __name__=='__main__':main()
