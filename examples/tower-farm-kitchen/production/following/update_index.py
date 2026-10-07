#!/usr/bin/env python3
"""Expose only the requested chapter after its original and phone review passes."""
import json,re,sys,html
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]
ROOT=BASE.parents[1]
DATA=json.loads(Path(__file__).with_name('episodes.json').read_text())
def update(n):
 ep=next(e for e in DATA if e['number']==n)
 d=BASE/f'episode-{n:02d}'
 validation=json.loads((d/'validation.json').read_text())
 for key in ('artworkTextReview','continuityReview','windowBoundaryReview','scrollPacingVisualReview'):
  if not str(validation.get(key,'')).startswith('passed'):raise ValueError(f'Unreviewed chapter {n}: {key}')
 for filename in ('index.html','reader.html','manifest.json'):
  if not (d/filename).is_file():raise ValueError(f'Missing {filename}')
 p=ROOT/'content/catalog.json';c=json.loads(p.read_text());s=next(x for x in c if x['id']=='tower-farm-kitchen')
 source=f'examples/tower-farm-kitchen/episode-{n:02d}/index.html'
 item={'id':f'episode-{n:02d}','number':n,'title':ep['title'],'edition':'','source':source,'background':'#fffaf0'}
 existing=next((i for i in s['episodes'] if i['number']==n),None)
 if existing is None:s['episodes'].append(item)
 elif existing!=item:raise ValueError('Conflicting already-adopted chapter')
 s['episodes'].sort(key=lambda e:e['number']);p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 p=BASE/'chapters.html';t=p.read_text();items=''.join(f'<li><a href="episode-{e["number"]:02d}/index.html">第{e["number"]}話　{html.escape(e["title"])}<span>読む →</span></a></li>' for e in s['episodes'])
 t=re.sub(r'<ol>.*?</ol>','<ol>'+items+'</ol>',t,flags=re.S);p.write_text(t)
 p=BASE/'series/bible.md';t=p.read_text();t=re.sub(r'completed_art_episodes: \[[^\n]*\]','completed_art_episodes: '+str([e['number'] for e in s['episodes']]),t);p.write_text(t)
 p=BASE/'series/continuity.md';t=p.read_text();heading=f'## 第{n}話の確認済み終了状態'
 if heading not in t:t+=f'\n{heading}\n\n{ep["time"]}。{ep["state"]}\n'
 p.write_text(t)
 print(f'Adopted {n}: {ep["title"]}; visible count {len(s["episodes"])}')
if __name__=='__main__':
 for n in sys.argv[1:]:update(int(n))
