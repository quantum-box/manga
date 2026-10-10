# -*- coding: utf-8 -*-
import base64, hashlib, importlib.util, json, re, struct, sys
from pathlib import Path
ROOT=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent; ROOT.mkdir(parents=True,exist_ok=True)
groups=json.loads((ROOT/'source-scenes.json').read_text())
panels=[]; beats=[]; tones={}; gaps=[]
scene_gap={9:(160,'昨日の気掛かりを持ってミルトへ戻る'),17:(120,'感謝の返事を受け今日の約束を確認'),25:(170,'薬を受け取って橋を渡る'),33:(200,'扉が開くのを待ち配達相手へ名乗る'),40:(230,'明日の話への返事を聞いて家を離れる'),41:(160,'届け終えた空の手でパン屋へ向かう'),49:(160,'贈り物の温度を受けベンチで口に運ぶ'),52:(180,'おいしさを受け止め昨日の粉を思い出す'),57:(210,'食べ終えた後に次の依頼が届く'),60:(150,'水を辿って一人で仕事場へ着く'),63:(200,'手の中の対価を自信として受け止める'),65:(200,'帰る道に運ぶ人の日常がある'),66:(100,'穏やかな荷車の音に急かす声が割り込む'),70:(120,'転倒の衝撃を受けて駆け寄る'),73:(160,'去ろうとする相手の前に立つ'),75:(80,'責任を拒まれて引き下がれない'),77:(100,'相手の言葉を受ける間'),79:(240,'押し倒され声を失ったあと手が剣へ動く'),80:(100,'刃を抜く前に手を止める'),83:(200,'相手が去っても怪我と荷物が残る'),86:(160,'口では手伝うと言えても指が震える'),88:(230,'慰めを受け取れず悔しさが出る'),89:(160,'後始末にかかった時間を歩いてつなぐ'),91:(200,'患者を渡した後で二人が話す'),93:(220,'剣を教えてほしいという言葉を聞いて考える'),94:(250,'約束しても気持ちは晴れない'),95:(240,'買えなかったパンから強さの募集へ'),96:(250,'募集を見て本人の未熟な願いが残る')}
soft={7,14,23,32,34,36,38,39,40,44,48,50,51,54,55,56,67,71,87,88,91,92,93}
shout={6,12,42,59,66,70,72,75}
details={9,25,35,45,62,68,79,86}
faces={3,4,7,13,15,38,47,50,51,56,63,74,76,78,88,92,93,96}
speaker_x={2:35,5:60,6:25,11:30,13:35,20:30,21:35,22:70,24:30,27:30,29:25,32:70,33:35,34:70,37:35,39:40,40:75,41:35,44:70,46:65,48:20,51:65,52:35,55:65,57:30,58:65,59:40,60:40,61:65,62:55,66:65,67:40,70:35,71:35,72:35,73:35,74:65,75:35,76:60,80:65,81:35,82:60,84:35,85:35,87:65,88:35,90:65,91:65,92:35,93:65}
landscapes={10,27,29,32,40,48,58,60,64,65,69,77,81,83,89,94}
for gi,(name,rows) in enumerate(groups):
 for j,(art,speaker,line,sound,purpose) in enumerate(rows):
  n=gi*8+j+1; pid=f'p{n:03}'; sheet=ROOT/'rough'/f'sheet-{gi+1:02}.png'
  raw=sheet.read_bytes(); w,h=struct.unpack('>II',raw[16:24]); cellw=w/2; cellh=h/4
  # Trim only the explicitly reserved blank lettering strip, never the acting.
  x=(j%2)*cellw+2; y=(j//2)*cellh+cellh*.22
  crop=[x/w,y/h,(cellw-4)/w,(cellh*.78-2)/h]
  width=72 if n in details else 82 if n in faces else 100 if n in landscapes else 94
  align='right' if speaker in ('航','航・心') else 'left' if speaker=='リゼ' else 'center'
  if n in scene_gap and n!=1:
   gh,why=scene_gap[n]; gap=dict(id=f'gap-{pid}',type='pause',height=gh,purpose=why)
   beats.append(gap);gaps.append(gap|dict(previous=f'p{n-1:03}',next=pid,content='none',background='white'))
  tone='thought' if speaker=='航・心' else 'display' if speaker=='表示' else 'soft' if n in soft else 'shout' if n in shout else 'normal'
  if line:
   longest=max(map(len,line.splitlines())); vh=max(150,42+longest*22)
   v=dict(id=pid+'-voice',type='voice',speaker=speaker,text=line,height=vh,x=speaker_x.get(n,50),y=49,purpose=purpose+'。言葉の後に同じ瞬間の顔・手を読む')
   beats.append(v);tones[v['id']]=tone
  panel=dict(id=pid,type='panel',image=f'rough/sheet-{gi+1:02}.png',imageSize=[w,h],crop=crop,alt=purpose+'。'+art,widthPercent=width,align=align,frame='none' if n in landscapes else 'thin',purpose=purpose,dialogue=[],sounds=[])
  if sound: panel['sounds']=[dict(text=sound,x=22,y=82)]
  beats.append(panel)
  state=('日本・学校の制服と鞄' if n<=5 else '日本・自宅の服とヘッドセット' if n<=8 else '初期服・剣は左腰に納刀・盾なし')
  if n<=56:
   state+=('／薬はセナの手元' if 18<=n<=21 else '／薬一包みを航が保持・略図あり' if 22<=n<=33 else '／薬はエダへ渡る' if n==34 else '／薬はエダの卓上・航の手は空' if 35<=n<=45 else '／贈り物のパン一つ・貨幣なし' if 46<=n<=53 else '／贈り物のパン食了' if n>=54 else '')
  else:
   state+=('／空袋を受け取る' if n==57 else '／空袋を保持・リゼは巡回支度で別行動' if 58<=n<=60 else '／空袋を職人に返却' if n==61 else '／銅貨二枚を受領し所持・パン未購入' if 62<=n<=77 else '／銅貨二枚が足元へ落ちる・右手掌を擦る' if 78<=n<=84 else '／拾った銅貨二枚は腰袋へ・パン未購入・右手掌に擦り傷')
   if 69<=n:state+='／荷運び人は右手首を痛めたまま'
   if 84<=n:state+='／荷運び人の右手首に包帯'
   if 80<=n:state+='／航は抜刀していない'
  panels.append(dict(id=pid,scene=name,art=art,newUnderstanding=purpose,effective=True,camera='detail' if n in details else 'close acting' if n in faces else 'establishing/path' if n in landscapes else 'medium action',dialogue=[] if not line else [dict(speaker=speaker,text=line,columns=line.splitlines(),tone=tone,intent=purpose)],sound=dict(mode=('continuation' if n in {89} else 'new') if sound else 'no lettering',text=sound,reason='動作と音源を示す' if sound else '会話と表情を優先し背景音の文字を足さない'),connection=f'{name}・前コマの結果を受ける',propState=state,layout=dict(widthPercent=width,align=align),hold='真相・死者・戦闘・魔法成功・盾取得は見せない'))
plan=dict(schema='webtoon-name-preview/v1',title='星環のレガリア 第2話「明日のある町」',referenceWidth=390,colorMode='monochrome',status='awaiting_user_adoption',scope='full_episode',beats=beats,notes=['第2話の構成確認用ネーム。本作画・公開版ではありません。','通常話目標：本編34,000〜60,000px／内容24,000px以上／有効80〜120コマ。'],episodeLength=dict(scope='full_episode',target=dict(widthCssPx=390,bodyHeightCssPx=[34000,60000],minContentHeightCssPx=24000,effectivePanels=[80,120]),planned=dict(effectivePanels=96)),panels=panels,pureGaps=gaps)
(ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
(ROOT/'lettering-tones.json').write_text(json.dumps(tones,ensure_ascii=False,indent=2))
spec=importlib.util.spec_from_file_location('name_builder',ROOT.parents[4]/'skills/webtoon/scripts/build_name_preview.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
sys.argv=['build_name_preview.py',str(ROOT/'plan.json'),'--output',str(ROOT/'index.html'),'--force'];mod.main()
page=(ROOT/'index.html').read_text()
for ident,tone in tones.items():
 page=page.replace(f'class="text-beat voice" data-beat-id="{ident}"',f'class="text-beat voice tone-{tone}" data-beat-id="{ident}"')
# Source bytes are embedded once; each crop references the same browser image.
pool={}
def dedupe(m):
 value=m.group(1)
 if value not in pool:pool[value]=f'rough-{len(pool):02}'
 return 'data-source="'+pool[value]+'"'
page=re.sub(r'src="(data:image/[^\"]+)"',dedupe,page)
js='<script>const roughPool='+json.dumps({v:k for k,v in pool.items()})+';for(const img of document.querySelectorAll("img[data-source]")){img.src=roughPool[img.dataset.source];}</script>'
page=page.replace('</body>',js+'</body>')
style='''<style>
#preview-flow{filter:none}.crop-window img{filter:grayscale(1)}
.floating-speaker{font-size:10px;color:#555}.voice-copy{color:#111;line-height:1.4}.floating-copy{box-sizing:border-box;background:white;padding:13px 22px 16px;border:1.8px solid #333;border-radius:49% / 36%;min-width:76px}
.voice .floating-copy:after{content:"";position:absolute;bottom:-13px;left:46%;width:13px;height:18px;background:white;border-right:1.5px solid #333;border-bottom:1.5px solid #333;transform:skew(-20deg) rotate(35deg);filter:none}
[data-beat-id="p001-voice"] .floating-copy:after,[data-beat-id="p076-voice"] .floating-copy:after{display:none}
.tone-soft .floating-copy{border-width:1.1px;border-radius:47% 53% 44% 56% / 38% 35% 45% 42%}
.tone-shout .floating-copy{border:3px solid #222;border-radius:9% 21% 12% 18%;outline:2px solid #777;outline-offset:4px}
.tone-thought .floating-copy{border:2px dashed #444;border-radius:40% 48% 42% 50%;box-shadow:5px 0 0 -3px #777,-5px 0 0 -3px #777}
.tone-thought .floating-copy:after{content:"••";background:none;border:none;clip-path:none;filter:none;font-size:23px;letter-spacing:5px;left:45%;bottom:-30px;transform:rotate(25deg);width:50px}
.tone-display .floating-copy{border:1px solid #444;border-radius:3px;padding:15px 20px}.tone-display .floating-copy:after{display:none}
.tone-display .voice-copy{writing-mode:horizontal-tb;white-space:pre-line;font-size:20px}.tone-display .voice-copy br{display:block}.sfx{color:#111}
.end-note{font-size:13px}.panel.frame-thin.cropped .crop-window{border:1px solid #666;box-sizing:border-box}
</style>'''
page=page.replace('</head>',style+'</head>')
(ROOT/'index.html').write_text(page)
# Lightweight local-browser twin; byte-identical source images, same DOM/CSS.
browser_page=page
for asset in (ROOT/'rough').glob('*.png'):
 encoded='data:image/png;base64,'+base64.b64encode(asset.read_bytes()).decode()
 browser_page=browser_page.replace(encoded,'rough/'+asset.name)
(ROOT/'preview.html').write_text(browser_page)
md=['# 第2話「明日のある町」構成ネーム','', '状態：未採用。採用後に本作画へ進む。既存の本作画・公開カタログ・iOSは変更しない。','', '## 構成の軸','約束を守り再訪→薬を届けパンを味わう→一人で運び賃を得る→無謀な帰還者が荷運び人を転ばせる→航は抗議して押し倒される→リゼが抜刀を止め救護する→後始末と震え→剣の稽古を頼む→買えなかったパンと強さへの焦り。','', '96の独立した動作・理解・返答・選択を有効コマとして計画。文字や余白は加算しない。','', '## 引継ぎ','基点 main e11f2ee970aaec5d13123322cbbb3e472e9766ee。第1話の約束・薬箱救助・納刀した初期剣・未習得の魔法と盾を維持。','', '## 演出参照','webtoon: name-preview, episode-length, speech-balloons, approved-example, vertical-lettering, scroll-pacing, whitespace-example, mobile-reader, emotion-and-causality, reader-perspective, context-and-dialogue, panel-layout, art-prompts, scroll-revision-lessons。採用例の完成画像と連続窓を確認。短い応酬、転倒から手の震えへ変える密度差、沈黙と抜刀直前の間を採用。絵柄・固定枚数は流用しない。','', '## コマ別の全文・音・状態']
for p in panels:
 md+=['',f'### {p["id"]} — {p["scene"]}',f'- 理解・意図：{p["newUnderstanding"]}',f'- 絵・カメラ：{p["art"]} / {p["camera"]}',f'- 接続：{p["connection"]}',f'- 小道具・身体：{p["propState"]}',f'- 音：{p["sound"]["text"] or "文字なし"} / {p["sound"]["reason"]}',f'- 余白：{next((g["purpose"] for g in gaps if g["next"]==p["id"]),"応酬または動作を近く読む。追加の純余白なし")}',f'- 伏せる：{p["hold"]}']
 for d in p['dialogue']:md+=['- '+d['speaker']+'／'+d['tone']+'／全文（改行＝右から左の縦列）：','```',d['text'],'```']
(ROOT/'storyboard.md').write_text('\n'.join(md)+'\n')
print(json.dumps(dict(panels=len(panels),beats=len(beats),htmlBytes=(ROOT/'index.html').stat().st_size)))
