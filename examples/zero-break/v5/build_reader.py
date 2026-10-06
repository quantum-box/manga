from pathlib import Path
from struct import unpack
import html,json,subprocess,sys
root=Path(__file__).resolve().parent
data=json.loads((root/'manifest.json').read_text())
if data.get('version') == 'context-dialogue-v6':
    subprocess.run([sys.executable,str(root.parent/'production/feedback_v6.py'),'build','1'],check=True)
    raise SystemExit(0)
css="""*{box-sizing:border-box}body{margin:0;background:#18202b;color:#203045;font-family:'Hiragino Kaku Gothic ProN','Yu Gothic',sans-serif}.episode{width:100%;max-width:480px;margin:auto;container-type:inline-size;background:#f7fbff}header{padding:54px 24px 48px;background:#111a29;color:#ecf8ff}header small{font-size:12px;letter-spacing:.14em;color:#9bdeee}h1{margin:18px 0 8px;font-size:clamp(31px,8.8cqw,42px);font-style:italic;line-height:1.4;text-shadow:2px 2px #b8475f}header p{margin:0;font-size:14px;line-height:1.9}.scene{position:relative;margin:0}.scene img{display:block;width:100%;height:auto}.night{background:#111a29;padding-top:12px}.wide,.left,.right{width:96%}.wide{margin:auto}.left{margin-right:auto}.right{margin-left:auto}.dark{background:#0c1e2e;width:100%}.bleed{width:100%}.pause{height:var(--pause);background:var(--paper,#f7fbff)}.transition{height:24cqw}.to-dark{background:linear-gradient(#f7fbff,#0c1e2e)}.to-light{background:linear-gradient(#0c1e2e,#d9f5ff,#f7fbff)}footer{padding:40px 24px 70px;font-size:13px;text-align:center;line-height:2;color:#59728a}footer a{color:#466b92}.pending{padding:20px;color:#724a50;background:#ffe9e9}"""
out=['<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ゼロ・ブレイク 第1話 v5 — 縦書き</title><style>'+css+'</style><main class="episode">','<header><small>異世界転生 × スーパーヒーロー / 第1話</small><h1>ゼロ・ブレイク</h1><p>最弱判定、最強の一歩。</p></header>']
pending=[]
for s in data['shots']:
    if s['id']=='core':out.append('<div class="transition to-dark" aria-hidden="true"></div>')
    if s['id']=='hero':out.append('<div class="transition to-light" aria-hidden="true"></div>')
    f=root/'art'/(s['file']+'.png')
    if not f.exists():
        pending.append(s['file']);out.append('<div class="pending">制作中：'+html.escape(s['id'])+'</div>');continue
    w,h=unpack('>II',f.read_bytes()[16:24])
    alt=s.get('alt_ja',s['scene'])+' '+ ' '.join(l['speaker']+'『'+l['text']+'』' for l in s['lines'])
    out.append('<figure class="scene '+s['shape']+'" id="'+s['id']+'"><img src="art/'+s['file']+'.png" width="'+str(w)+'" height="'+str(h)+'" alt="'+html.escape(alt)+'"></figure>')
    bg='#111a29' if s['id']=='memory' else '#0c1e2e' if s['id']=='core' else '#f7fbff'
    gap=round(s['pause']/390*100,2)
    out.append('<div class="pause" aria-hidden="true" style="--pause:'+str(gap)+'cqw;--paper:'+bg+'"></div>')
out.append('<footer>第1話 おわり<br><a href="../episode-02/index.html">第2話「英雄の請求書」へ</a></footer></main></html>')
(root/'index.html').write_text(''.join(out))
print('Scenes built:',len(data['shots'])-len(pending),'pending:',len(pending))
