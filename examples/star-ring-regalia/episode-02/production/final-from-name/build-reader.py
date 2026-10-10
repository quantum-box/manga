# -*- coding: utf-8 -*-
from pathlib import Path
import json, struct, html, sys
prod=Path(__file__).resolve().parent;ep=prod.parents[1];repo=ep.parents[2];name=ep/'review/name-preview'
plan=json.loads((name/'plan.json').read_text());crops=json.loads((prod/'source-crops.json').read_text());rows=[];layout=[]
gaps={int(g['next'][1:]):g for g in plan['pureGaps']}
# Preserve the approved name and apply the later spacing-only revision.
pacing=json.loads((prod/'pacing.json').read_text())
gaps.update({int(g['next'][1:]):g for g in pacing['overrides']})
for i,p in enumerate(plan['panels']):
 n=i+1;idx=i//4+1;cell=i%4;src=f'art/f{idx:02}.png';f=ep/src
 if not f.exists():
  print('Missing '+src,file=sys.stderr);sys.exit(1)
 w,h=struct.unpack('>II',f.read_bytes()[16:24]);gap=gaps.get(n)
 if gap:rows.append(f'<div class="pause" style="height:{gap["height"]/390*100:.6f}cqw" aria-hidden="true" data-purpose="{html.escape(gap["purpose"],quote=True)}"></div>')
 width=p['layout']['widthPercent'];width=max(width,94) if p['dialogue'] else width
 align=p['layout']['align'];margin='0 auto' if align=='center' else '0 0 0 auto' if align=='right' else '0 auto 0 0'
 alt=p['newUnderstanding']+'。'+' / '.join(d['speaker']+'「'+d['text'].replace('\n','')+'」' for d in p['dialogue'])
 if p['sound']['text']:alt+=' / 効果音 '+p['sound']['text']
 # Each source uses its actual visible cell boundary; generated grids are not always equal.
 cx,cy,cw,ch=crops[src][cell]
 style=f'width:{width}%;aspect-ratio:{cw}/{ch};margin:{margin};'
 ist=f'width:{w/cw*100:.6f}%;left:{-cx/cw*100:.6f}%;top:{-cy/ch*100:.6f}%;'
 rows.append(f'<figure id="p{n:03}" class="panel" style="{style}" data-source="{src}" data-effective="true"><img src="{src}" alt="{html.escape(alt,quote=True)}" style="{ist}" loading="eager"></figure>')
 layout.append({'id':p['id'],'adoptedArt':src,'nativeWidth':w,'nativeHeight':h,'sourceCrop':[cx,cy,cw,ch],'widthPercent':width,'align':align,'gapBefore390':gap['height'] if gap else 0,'pacingPurpose':p['newUnderstanding'],'alt':alt})
css='''*{box-sizing:border-box}html{scroll-behavior:auto}body{margin:0;background:#f1efeb;color:#24211e;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN",sans-serif}main{width:100%;max-width:390px;margin:0 auto;background:white;container-type:inline-size}header{padding:42px 22px 50px;background:white}h1{font-size:27px;line-height:1.5;margin:10px 0}header p{font-size:15px;letter-spacing:.08em;margin:0}#episode-body{background:#fff}.panel{position:relative;overflow:hidden;padding:0;border:0}.panel img{position:absolute;display:block;max-width:none;height:auto}.pause{width:100%;background:white}footer{padding:72px 20px;text-align:center;font-size:15px;line-height:2}footer a{color:#4b596e}'''
page='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>星環のレガリア 第2話 明日のある町</title><link rel="stylesheet" href="reader.css"></head><body><main><header><p>星環のレガリア　第2話</p><h1>明日のある町</h1></header><section id="episode-body" aria-label="第2話 本編">'+''.join(rows)+'</section><footer>つづく</footer></main></body></html>'
(ep/'reader.css').write_text(css);(ep/'index.html').write_text(page);(ep/'layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
(prod/'render-plan.json').write_text(json.dumps({'effectivePanels':96,'sourceSheets':24,'body':'#episode-body','panels':layout},ensure_ascii=False,indent=2)+'\n')
print('Built finished reader with 96 independent display crops and adopted gaps')
