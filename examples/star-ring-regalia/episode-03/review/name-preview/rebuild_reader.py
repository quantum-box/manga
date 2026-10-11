"""Render the checked-in plan with the repository builder and episode lettering."""
from pathlib import Path
import json,re,subprocess,sys
p=Path(__file__).resolve().parent
root=p.parents[4]
subprocess.run([sys.executable,str(root/'skills/webtoon/scripts/build_name_preview.py'),str(p/'plan.json'),'--output',str(p/'index.html'),'--force'],check=True)
h=(p/'index.html').read_text()
plan=json.loads((p/'plan.json').read_text())
shouts={'03-patrol:3-added-1-voice','05-defense:1-voice','01-spar:1-voice'}
tail_overrides={
 '01-choice:6-voice':'down-right','01-spar:1-voice':'down-left','01-spar:4-voice':'down-right',
 '01-spar:5-voice':'down-left','02-flicker:1-voice':'down-left','02-flicker:5-voice':'down-left',
 '02-star:1-voice':'down-left','02-star:3-voice':'down-left','02-star:4-voice':'down-left',
 '02-star:5-voice':'down-left','02-star:6-voice':'down-left',
 '00-yard:2-voice':'down-right','01-choice:5-voice':'down-right','01-lesson:2-voice':'down-left',
 '02-retry:2-added-2-voice':'down-right','02-retry:3-voice':'down-left','02-rest:2-voice':'down-right',
 '02-change:2-voice':'down-right','03-patrol:1-voice':'down-right','05-recover:3-added-1-voice':'down-right',
 '06-returner:1-voice':'down-right','06-supply:1-voice':'down','06-supply:2-voice':'down-left',
 '07-local:1-voice':'down-left','07-local:2-added-1-voice':'down-left',
 '07-promise:1-added-2-voice':'down','07-promise:3-voice':'down-right'
}
outlines={
 'thought':'M15 16 C10 5 35 2 44 10 C57 1 80 4 82 15 C98 14 103 31 92 39 C104 49 102 67 90 71 C99 86 83 98 70 91 C59 104 38 103 31 93 C13 102 1 85 10 74 C-2 65 -1 47 9 41 C-1 32 1 18 15 16 Z',
 'shout':'M10 10 L22 14 L27 2 L37 10 L47 1 L55 10 L68 3 L73 15 L88 10 L86 24 L99 30 L90 40 L99 49 L90 58 L99 72 L86 75 L90 90 L74 86 L68 99 L56 90 L44 99 L36 90 L23 98 L19 84 L4 88 L11 73 L1 65 L10 55 L1 42 L12 35 L3 22 L15 23 Z'
}
decisions=[]
for beat in plan['beats']:
 if beat['type']!='voice':continue
 kind='thought' if beat['kind']=='thought' else 'shout' if beat['id'] in shouts else 'spoken'
 tail=tail_overrides.get(beat['id'],'up-right' if beat.get('composition') else 'down-left' if beat['x']>50 else 'down-right' if beat['x']<50 else 'down')
 pattern=r'(<section class="[^"]*" data-beat-id="'+re.escape(beat['id'])+r'"[^>]*><div class="floating-copy"[^>]*>)(.*?)(</div></section>)'
 def wrap(m):
  start=m[1].replace('class="text-beat voice','class="text-beat voice voice-'+kind+' voice-tail-'+tail).replace('top:50%;','top:46%;')
  body=m[2];at=body.index('<span class="voice-copy">')
  shape=('<svg class="voice-outline" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="'+outlines[kind]+'"/></svg>') if kind in outlines else ''
  return start+body[:at]+'<div class="voice-balloon">'+shape+body[at:]+'</div>'+m[3]
 h,count=re.subn(pattern,wrap,h,flags=re.S)
 assert count==1,beat['id']
 decisions.append({'id':beat['id'],'speaker':beat['speaker'],'kind':kind,'tail':tail,'targetPanel':beat['id'].removesuffix('-voice'),
                   'reason':'心の声を雲形と点で示す' if kind=='thought' else '離れた相手へ届く切迫した制止を太いトゲで示す' if kind=='shout' else '声に出す会話を細い輪郭と話者へ向く尾で示す'})
css='''
.voice .voice-balloon { position:relative; display:inline-flex; align-items:center; justify-content:center;
 padding:4.4cqw 5.6cqw; background:#fff; border:2px solid #343434; border-radius:47% / 22%; }
.voice .voice-copy { position:relative; z-index:1; color:#292929; }
.voice-spoken .voice-balloon::after,.voice-shout .voice-balloon::after { content:""; position:absolute; left:32%; bottom:-12px;
 width:18px; height:18px; background:#fff; border-right:2px solid #343434; border-bottom:2px solid #343434;
 transform:rotate(50deg) skew(-15deg); }
.voice-tail-down-right .voice-balloon::after { left:auto; right:32%; transform:rotate(30deg) skew(15deg); }
.voice-tail-down .voice-balloon::after { left:50%; transform:translateX(-50%) rotate(45deg); }
.voice-tail-up-right .voice-balloon::after { left:auto; right:-11px; bottom:auto; top:24%; transform:rotate(-50deg) skew(15deg); }
.voice-outline { position:absolute; inset:-3px; width:calc(100% + 6px); height:calc(100% + 6px); overflow:visible; }
.voice-outline path { fill:#fff; stroke:#343434; stroke-width:2; vector-effect:non-scaling-stroke; stroke-linejoin:round; }
.voice-thought .voice-balloon,.voice-shout .voice-balloon { border-color:transparent; border-radius:0; background:transparent; }
.voice-thought .voice-balloon::after,.voice-thought .voice-balloon::before { content:""; position:absolute;
 background:#fff; border:1.5px solid #343434; border-radius:50%; width:8px; height:8px; left:29%; bottom:-14px; }
.voice-thought .voice-balloon::before { width:5px; height:5px; left:21%; bottom:-24px; }
.voice-shout .voice-outline path { stroke-width:3; stroke-linejoin:miter; }
.voice-shout .voice-copy { font-weight:900; }
.voice-shout .voice-balloon { padding:7cqw 6.5cqw; }
.voice-shout .voice-balloon::after { border-width:3px; }
'''
h=h.replace('</style>',css+'\n</style>',1)
h=h.replace('</style>', '\n[data-beat-id="03-patrol:3"] .balloon,[data-beat-id="05-defense:1"] .balloon,[data-beat-id="05-defense:3"] .balloon{border-width:3px;border-radius:17% 24% 16% 22%}\n[data-beat-id="05-recover:1"] .balloon{border-width:2px;border-radius:36%}\n</style>',1)
(p/'index.html').write_text(h)
(p/'balloon-decisions.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
