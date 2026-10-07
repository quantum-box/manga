#!/usr/bin/env python3
"""Build the adopted rewrite from immutable raster originals and recorded windows."""
import argparse
import hashlib
import html
import json
import subprocess
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
PRODUCTION = ROOT / 'production'
REVISION = 'full-rebuild-2026-10-07'
CSS = '''*{box-sizing:border-box}html{background:#edf0f1;color:#17222e;color-scheme:light}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Yu Gothic",sans-serif}.episode{width:100%;max-width:480px;margin:auto;background:#fff;container-type:inline-size}header{padding:34px 8% 50px}h1{font-family:"Yu Mincho",serif;font-size:clamp(36px,10cqw,48px);line-height:1.3;margin:12px 0 20px}h1 span{color:#886632}.eyebrow,.hint{font-size:12px;color:#62747d;letter-spacing:.08em}.subtitle{font-size:19px;line-height:1.8;margin:0}.scene{margin:0;width:100%}.scene img{display:block;width:100%;height:auto}.window{width:100%;overflow:hidden}.window img{width:100%;height:100%;object-fit:cover}.pause{background:white;width:100%}footer{padding:55px 8% 70px;text-align:center}footer p{font-size:19px;line-height:1.8}nav{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:36px}a{color:#3a5561;text-underline-offset:4px;padding:12px 6px;min-height:44px}a:focus-visible{outline:3px solid #886632}'''

def read(p):
    return json.loads(p.read_text(encoding='utf-8'))

def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def esc(v):
    return html.escape(str(v), quote=True)

def build(e):
    n = e['number']
    folder = ROOT / f'episode-{n:02d}'
    layout = read(PRODUCTION / 'layout.json').get(str(n), {})
    jobs = {j['id']: j for j in read(PRODUCTION / 'jobs.json') if j['episode'] == n}
    generations = read(PRODUCTION / 'generation.json')
    content, artwork, order, prompts = [], [], [], []
    board = [f"# 天魔、二周目。 第{n}話 {e['title']}\n\n変化：{e['change']}\n\n開始：{e['start']}\n\n終了：{e['end']}"]
    for a in e['assets']:
        ident, name, shape, gap, purpose, art, lines, sound, hidden = a
        leaf = f'art/rebuild-{ident}.png'
        leaf = read(PRODUCTION / 'adoption.json').get(str(n), {}).get(ident, leaf)
        path = folder / leaf
        if not path.is_file():
            raise FileNotFoundError(path)
        with Image.open(path) as im:
            w, h = im.size
        artwork.append({'id':ident,'file':leaf,'width':w,'height':h,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        windows = layout.get(ident, [{'range':[0,h], 'gap':gap}])
        for k, win in enumerate(windows):
            lo, hi = win['range']
            assert 0 <= lo < hi <= h, (leaf,win,h)
            after = win.get('gap', gap if k == 0 else 100)
            key = f'beat-{ident}-{k+1}'
            if content:
                content.append(f'<div class="pause" id="pause-{key}" style="height:{after/3.9:.5f}cqw" data-purpose="{esc(purpose)}" aria-hidden="true"></div>')
            shown_lines = [lines[i] for i in win.get('lines', range(len(lines)))]
            shown_sound = win.get('sound', sound)
            alt = win.get('description', name)+ '。' + ''.join(s+'「'+t+'」。' for s,t,_,_ in shown_lines)
            if not shown_sound.startswith(('none', 'no sound')):
                alt += ' 効果音：'+shown_sound
            img = f'<img src="{leaf}" width="{w}" height="{h}" alt="{esc(alt)}" decoding="sync">'
            if [lo,hi] != [0,h]:
                span = hi-lo
                offset = lo/(h-span)*100
                img = '<div class="window" style="aspect-ratio:'+str(w)+'/'+str(span)+'">'+img.replace(' decoding=',f' style="object-position:50% {offset:.7f}%" decoding=')+'</div>'
            content.append(f'<figure class="scene" id="{key}" data-source="{leaf}" data-window="{lo},{hi}">{img}</figure>')
            order.append({'id':key,'asset':ident,'range':[lo,hi],'gap390':after,'purpose':purpose})
        board.append(f'## {ident} {name}\n\n読者の理解／間：{purpose}\n\n描くもの／カメラ／立ち位置：{art}\n\n伏せる情報／状態：{hidden}\n\n作画形式：{shape}。読む順は上から下、同段の小コマは右から左。\n\n原画：{leaf} {w}×{h}。表示窓：{json.dumps(windows,ensure_ascii=False)}\n\n効果音（発話と別）：{sound}\n\n発話：'+ ('\n'.join(f'{speaker}「{full}」／縦列 右→左：{cols}／声：{voice}' for speaker,full,cols,voice in lines) or 'なし。'))
        runs = [r for r in generations if r.get('episode') == n and r.get('id') == ident]
        adopted_runs = [r for r in runs if Path(r['adopted']) == path]
        if not adopted_runs:
            raise ValueError(f'Missing adopted generation: {path}')
        run = adopted_runs[-1]
        actual = run.get('edit') or run
        prompts.append('## '+ident+' '+name+'\n\n採用原画：'+leaf+'。画像生成原本を無加工で配置。表示範囲だけをCSSで記録。\n\n```text\n'+actual['prompt']+'\n```\n\n生成原本：`'+actual.get('source', run['original'])+'`\n\n入力資料：'+', '.join('`'+p+'`' for p in actual.get('references', [actual['original']] if 'edit' in run and run['edit'] else run.get('references', []))))
    nav = []
    if n > 1:
        nav.append(f'<a href="../episode-{n-1:02d}/index.html">← 第{n-1}話</a>')
    nav.append('<a href="../serial.html">話一覧</a>')
    if n < 10:
        nav.append(f'<a href="../episode-{n+1:02d}/index.html">第{n+1}話 →</a>')
    ending = '導入編 完' if n == 10 else ''
    doc = f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>天魔、二周目。 第{n}話 {esc(e["title"])}</title><link rel="stylesheet" href="reader.css"></head><body><main class="episode"><header><p class="eyebrow">武侠 × 異世界転生 × 強くてニューゲーム</p><h1>天魔、<br><span>二周目。</span></h1><p class="subtitle">第{n}話　{esc(e["title"])}</p><p class="hint">下へスクロール ↓</p></header><section id="comic-body">{"".join(content)}</section><div class="pause" style="height:85cqw" aria-hidden="true"></div><footer><p>第{n}話 完</p><p>{ending}</p><nav>{"".join(nav)}</nav></footer></main></body></html>'
    (folder/'index.html').write_text(doc,encoding='utf-8')
    (folder/'reader.css').write_text(CSS,encoding='utf-8')
    (folder/'storyboard.md').write_text('\n\n'.join(board)+'\n',encoding='utf-8')
    (folder/'PROMPTS.md').write_text('\n\n'.join(prompts)+'\n',encoding='utf-8')
    manifest={'title':'天魔、二周目。','chapter':n,'subtitle':e['title'],'revision':REVISION,'artwork':artwork,'readingOrder':order,'lettering':'integrated vertical Japanese in immutable image originals','startState':e['start'],'endState':e['end']}
    save(folder/'manifest.json',manifest)
    save(folder/'episode.json',manifest)
    subprocess.run([sys.executable,str(REPO/'skills/webtoon/scripts/package_reader.py'),str(folder/'index.html'),'--force'],check=True,capture_output=True)
    print(f'Built {n}: {len(artwork)} originals, {len(order)} reading units')

def serial(episodes):
    rows=''.join(f'<li><a href="episode-{e["number"]:02d}/index.html">第{e["number"]}話　{esc(e["title"])}</a></li>' for e in episodes)
    style=CSS+'ol{list-style:none;margin:0;padding:0 8% 50px}li{border-top:1px solid #e0e8ea}li a{display:block;text-decoration:none;font-size:19px;line-height:1.8;padding:22px 0}'
    (ROOT/'serial.html').write_text(f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>天魔、二周目。</title><style>{style}</style></head><body><main class="episode"><header><h1>天魔、<br><span>二周目。</span></h1><p class="subtitle">最強の身体でも、死ぬのは怖い。<br>知らなかった声を聞く、二周目。</p></header><ol>{rows}</ol></main></body></html>',encoding='utf-8')

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--episode',type=int,action='append')
    args=ap.parse_args()
    episodes=read(PRODUCTION/'scripts.json')['episodes']
    for e in episodes:
        if not args.episode or e['number'] in args.episode:
            build(e)
    serial(episodes)
