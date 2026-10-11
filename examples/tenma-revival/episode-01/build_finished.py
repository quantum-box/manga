#!/usr/bin/env python3
"""Compose adopted final art without mutating generated original pixels."""
import base64,html,json,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent
OUT=BASE/'finished'
p=json.loads((BASE/'production.json').read_text())
records=json.loads((OUT/'generation.json').read_text())
bounds=json.loads((OUT/'crop-bounds.json').read_text())
assets={str(i):f'art/scene-{i:02d}.png' for i in range(1,27)}
large=set(p['largePanels']);fast={2,3,4,13,14,22,27,29,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,67,68,71,87,89,90,91,97}
flow=[];ledger=[]
for s,cells in enumerate(p['scenes']):
 for j,description in enumerate(cells):
  n=s*4+j+1;w=100 if n in large else [84,80,88,76][j]
  side=['left','right','center','right'][j]
  d=p['dialogue'][s][j];alt=description
  if d:alt+=' '+d[0]+'「'+d[1].replace('\n',' ')+'」'
  for e in p.get('extraDialogue',{}).get(str(n),[]):alt+=' '+e['speaker']+'「'+e['text'].replace('\n',' ')+'」'
  source=assets[str(s+1)]
  x,y,cw,ch=bounds[s]['bounds'][j];iw,ih=bounds[s]['size']
  crop=f'--cw:{cw};--ch:{ch};--iw:{iw/cw*100:.6f}%;--ih:{ih/ch*100:.6f}%;--cx:{-x/cw*100:.6f}%;--cy:{-y/ch*100:.6f}%'
  cover=' data-cover-frame' if n==1 else ''
  if n==50:
   flow.append('<div class="row">')
  if n in (50,51):w=100
  flow.append(f'<figure id="p{n:03d}" data-panel="{n}" class="panel {side}" style="--w:{w}%;--col:{j%2};--row:{j//2};{crop}"><div class="crop"{cover}><img src="{source}" width="1024" height="1536" alt="{html.escape(alt,quote=True)}" decoding="async"></div></figure>')
  if n==51:flow.append('</div>')
  gap=0 if n in fast or n in (50,51) else 14
  if str(n) in p['pauses']:
   gap=p['pauses'][str(n)];kind='transition';reason=p['pauseReasons'][s]
  else:kind='response';reason='短い反応・返答を受け止める'
  if gap:flow.append(f'<div class="pause {kind}" data-after="{n}" data-css-height="{gap}" style="--pause:{gap/390*100:.6f}cqw" aria-label="{html.escape(reason)}"></div>')
  ledger.append({'id':f'p{n:03d}','source':source,'cell':[j%2,j//2],'cropBounds':[x,y,cw,ch],'effective':n not in (5,40,52,64),'widthPercent':w,'gapAfter':gap,'gapRole':reason,'dialogue':d,'extraDialogue':p.get('extraDialogue',{}).get(str(n),[]),'sfx':p['sounds'][s][j],'description':description})
css="""*{box-sizing:border-box}html,body{margin:0;background:#fff;color:#222}body{font-family:system-ui,sans-serif}main{max-width:480px;margin:auto;container-type:inline-size}header{padding:40px 22px 28px}header h1{font-size:24px;line-height:1.4;margin:0 0 14px}header p{font-size:16px;margin:0}figure{margin:0}.panel{width:var(--w)}.left{margin-right:auto}.right{margin-left:auto}.center{margin-left:auto;margin-right:auto}.crop{position:relative;width:100%;aspect-ratio:var(--cw)/var(--ch);overflow:hidden;background:white}.crop img{position:absolute;max-width:none;width:var(--iw);height:var(--ih);left:var(--cx);top:var(--cy);display:block}.pause{height:var(--pause)}.row{display:flex;align-items:center;gap:8px}.row .panel{width:calc(50% - 4px)}footer{padding:64px 24px 90px;text-align:center;font-size:16px}footer p{line-height:1.8}a{color:inherit}"""
body='<header><h1>天魔神教、再興</h1><p>第1話　膝をつくな</p></header><div id="comic-body">'+''.join(flow)+'</div><footer class="ending"><p>第1話 おわり</p><p>共に立つ者を探しに</p><a href="#p001">冒頭へ</a></footer>'
document='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="preload" as="image" href="art/cover.jpg"><title>天魔神教、再興 第1話 膝をつくな</title><style>'+css+'</style></head><body><main>'+body+'</main></body></html>'
(OUT/'index.html').write_text(document)
# Embed each original once through a source map, not 104 copies.
standalone=document.replace('href="art/cover.jpg"','href="data:image/jpeg;base64,'+base64.b64encode((OUT/'art/cover.jpg').read_bytes()).decode()+'"')
for k,v in assets.items():standalone=standalone.replace('src="'+v+'"','data-source="'+k+'"')
encoded={k:'data:image/png;base64,'+base64.b64encode((OUT/v).read_bytes()).decode() for k,v in assets.items()}
loader='<script type="application/json" id="artwork-sources">'+json.dumps(encoded)+'</script><script>const assets=JSON.parse(document.getElementById("artwork-sources").textContent);for(const img of document.querySelectorAll("img[data-source]"))img.src=assets[img.dataset.source];</script>'
standalone=standalone.replace('</body>',loader+'</body>')
(OUT/'reader.html').write_text(standalone)
(OUT/'panel-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'panels':104,'effective':100,'standaloneBytes':(OUT/'reader.html').stat().st_size,'estimatedBody390':sum((585*(l['widthPercent']/100)/2 if i+1 in (50,51) else 585*l['widthPercent']/100)+l['gapAfter'] for i,l in enumerate(ledger))},ensure_ascii=False))

