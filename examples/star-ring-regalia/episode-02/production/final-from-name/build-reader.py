# -*- coding: utf-8 -*-
"""Render the adopted beat stream, keeping lettering separate by default."""
from pathlib import Path
import json, struct, html, sys
prod=Path(__file__).resolve().parent
ep=prod.parents[1]
name=ep/'review/name-preview'
plan=json.loads((name/'plan.json').read_text())
cells=json.loads((prod/'source-crops.json').read_text())
decisions=json.loads((prod/'layout-decisions.json').read_text())
choices={p['id']:p for p in decisions['panels']}
rows=[];layout=[];voice_count=0
escape=lambda s:html.escape(s,quote=True)
# Sound effects outside the selected crop are typeset once beside their source action.
external_sfx={1:('キーン コーン',8,86),95:('ピン',76,12)}
for beat in plan['beats']:
 pid=beat['id'].removesuffix('-voice')
 if beat['type']=='pause':
  rows.append(f'<div id="{escape(beat["id"])}" class="pause" style="height:{beat["height"]/390*100:.6f}cqw" data-purpose="{escape(beat["purpose"])}" aria-hidden="true"></div>')
  continue
 choice=choices[pid]
 if beat['type']=='voice':
  if choice['lettering']=='integrated':continue
  tone=next(p['dialogue'][0]['tone'] for p in plan['panels'] if p['id']==pid)
  copy='<br>'.join(escape(s) for s in beat['text'].splitlines())
  # No speaker names printed: the sequence and preceding acting establish the voice.
  rows.append(f'<div id="{escape(beat["id"])}" class="voice tone-{tone}" data-speaker="{escape(beat["speaker"])}" style="height:{beat["height"]/390*100:.6f}cqw"><div class="balloon" style="left:{beat["x"]}%;top:{beat["y"]}%"><span class="voice-copy">{copy}</span></div></div>')
  voice_count+=1
  continue
 n=int(pid[1:]);idx=(n-1)//4+1;cell=(n-1)%4
 script=plan['panels'][n-1]
 src=f'art/f{idx:02}.png'
 if script['dialogue'] and choice['lettering']=='separate' and n!=71:
  src=f'art/layout-f{idx:02}.png'
 f=ep/src
 if not f.exists():raise SystemExit(f'Missing adopted art: {src}')
 w,h=struct.unpack('>II',f.read_bytes()[16:24])
 cx,cy,cw,ch=cells[f'art/f{idx:02}.png'][cell]
 # Edited sheets preserve source size and cell boundaries.
 rx,ry,rw,rh=choice['cropWithinCell']
 cx,cy,cw,ch=cx+rx*cw,cy+ry*ch,rw*cw,rh*ch
 width=beat['widthPercent'];align=beat['align']
 margin='0 auto' if align=='center' else '0 0 0 auto' if align=='right' else '0 auto 0 0'
 alt=script['newUnderstanding']+'。'+' / '.join(d['speaker']+'「'+d['text'].replace('\n','')+'」' for d in script['dialogue'])
 if script['sound']['text']:alt+=' / 効果音 '+script['sound']['text']
 frame=' border:1px solid #666;' if beat['frame']=='thin' else ''
 style=f'width:{width}%;aspect-ratio:{cw}/{ch};margin:{margin};{frame}'
 ist=f'width:{w/cw*100:.6f}%;left:{-cx/cw*100:.6f}%;top:{-cy/ch*100:.6f}%;'
 sfx=''
 if n in external_sfx:
  text,x,y=external_sfx[n];sfx=f'<span class="sfx" style="left:{x}%;top:{y}%">{escape(text)}</span>'
 rows.append(f'<figure id="{pid}" class="panel" style="{style}" data-lettering="{choice["lettering"]}" data-source="{src}"><img src="{src}" alt="{escape(alt)}" style="{ist}" loading="eager">{sfx}</figure>')
 layout.append({'id':pid,'adoptedArt':src,'nativeWidth':w,'nativeHeight':h,'sourceCrop':[cx,cy,cw,ch],'widthPercent':width,'align':align,'lettering':choice['lettering'],'nameFrame':beat['frame'],'cropReason':choice['cropReason'],'alt':alt})
css='''*{box-sizing:border-box}html{scroll-behavior:auto}body{margin:0;background:#f1efeb;color:#24211e;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN",sans-serif}main{width:100%;max-width:390px;margin:0 auto;background:white;container-type:inline-size}header{padding:42px 22px 50px;background:white}h1{font-size:27px;line-height:1.5;margin:10px 0}header p{font-size:15px;letter-spacing:.08em;margin:0}#episode-body{background:#fff}.panel{position:relative;overflow:hidden;padding:0}.panel img{position:absolute;display:block;max-width:none;height:auto}.pause{width:100%;background:white}.voice{position:relative;width:100%;background:white}.balloon{position:absolute;transform:translate(-50%,-50%);background:#fff;border:1.6px solid #51463e;border-radius:49% / 36%;padding:13px 22px 16px;max-width:84%;min-width:76px;text-align:center}.voice-copy{display:inline-block;writing-mode:vertical-rl;text-orientation:mixed;font-size:clamp(19px,5.4cqw,22px);font-weight:600;line-height:1.4;white-space:nowrap}.tone-soft .balloon{border-width:1.1px;border-radius:47% 53% 44% 56% / 38% 35% 45% 42%}.tone-shout .balloon{border:2.5px solid #382e2b;border-radius:9% 21% 12% 18%;outline:1px solid #8b776a;outline-offset:3px}.tone-thought .balloon{border:1.3px dashed #746355;border-radius:40% 48% 42% 50%}.tone-display .balloon{border:1px solid #678092;border-radius:3px;background:#f4fbff;padding:15px 20px}.tone-display .voice-copy{writing-mode:horizontal-tb;white-space:pre-line;font-size:20px}.sfx{position:absolute;color:#264b70;font-size:27px;font-weight:900;text-shadow:1px 1px white,-1px -1px white;transform:rotate(-8deg);max-width:76%}footer{padding:72px 20px;text-align:center;font-size:15px;line-height:2}footer a{color:#4b596e}'''
page='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>星環のレガリア 第2話 明日のある町</title><link rel="stylesheet" href="reader.css"></head><body><main><header><p>星環のレガリア　第2話</p><h1>明日のある町</h1></header><section id="episode-body" aria-label="第2話 本編">'+''.join(rows)+'</section><footer>つづく</footer></main></body></html>'
(ep/'reader.css').write_text(css)
(ep/'index.html').write_text(page)
(ep/'layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
(prod/'render-plan.json').write_text(json.dumps({'effectivePanels':len(layout),'separateVoices':voice_count,'integratedVoices':len([p for p in plan['panels'] if p['dialogue']])-voice_count,'body':'#episode-body','nameBeatSource':'review/name-preview/plan.json','panels':layout},ensure_ascii=False,indent=2)+'\n')
print(f'Built {len(layout)} panels and {voice_count} independent voices from adopted name beats')
