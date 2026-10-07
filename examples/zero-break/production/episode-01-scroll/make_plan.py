"""Freeze the adopted Episode 1 display windows and their narrative references."""
import hashlib
import json
from pathlib import Path
from struct import unpack

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
STATE = Path(__file__).resolve().parent
m = json.loads((ROOT/'v5/manifest.json').read_text())
shots = {s['id']: s for s in m['shots']}
sources = {}
units = []


def add(id, shot, purpose, crop=None, width=100, align='center', pause=48,
        panels=(), lines=(), sounds=(), texts=(), new=None):
    source_id = new or shot
    if source_id not in sources:
        if new:
            record_path = STATE/'records'/(new+'.json')
            record = json.loads(record_path.read_text())
            file = record['file']
        else:
            file = shots[shot]['file']
        raw = (ROOT/'v5/art'/file).read_bytes()
        w,h = unpack('>II',raw[16:24])
        source = dict(id=source_id,file=file,width=w,height=h,sha256=hashlib.sha256(raw).hexdigest())
        if new: source['record'] = str(record_path.relative_to(REPO))
        sources[source_id] = source
    source = sources[source_id]
    units.append(dict(id=id, sourceId=source_id,
        crop=crop or [0,0,source['width'],source['height']],
        widthPercent=width,align=align,pause=pause,purpose=purpose,
        panelRefs=[[shot,i] for i in panels],lineRefs=[[shot,i] for i in lines],
        soundRefs=[[shot,i] for i in sounds],textRefs=[[shot,i] for i in texts]))


def whole(shot, purpose, **kw):
    s=shots[shot]
    add(shot,shot,purpose,panels=range(len(s.get('panels',[s]))),
        lines=range(len(s['lines'])),sounds=range(len(s.get('sounds',[]))),
        texts=range(len(s.get('visible_text',[]))),**kw)


whole('memory','雨の事故の記憶。届かなかった手だけが残る',pause=520)
add('wake-eyes','e01-waking','白い世界で目を開ける',[0,0,726,470],panels=[0],lines=[0],pause=220)
add('sky-city','e01-waking','スクロールで空都の全景を開く',[0,476,726,1098],panels=[1],texts=[0],pause=155)
add('wake-memory','e01-waking','事故の記憶との食い違い',[0,1580,726,584],panels=[2],lines=[1],pause=160)
whole('footsteps','顔より先に靴音が届く',width=76,align='right',pause=42)
whole('knight_arrives','近づいてきた騎士を初めて見せる',width=92,pause=130)
add('greeting-call','e01-greeting','騎士が手を差し出す前の呼びかけ',[0,0,836,535],panels=[0],lines=[0],pause=32)
add('greeting-response','e01-greeting','差し出す手と返事を横並びで近くつなぐ',[0,544,836,466],panels=[1,2],lines=[1],sounds=[0],pause=22)
add('greeting-help','e01-greeting','手を握って起き上がる',[0,1018,836,863],panels=[3],lines=[2],sounds=[1],pause=85)
add('rook-name','e01-rook-name','ルークの名乗り',[0,93,724,794],panels=[0],lines=[0],pause=42)
add('rook-two-shot','e01-rook-name','二人の距離と立ち位置を確認',[0,921,724,1175],panels=[1],pause=110)
for i,(y,h,phrase) in enumerate([(0,449,'空の国を説明'),(458,533,'レンが空を見上げる'),(1007,273,'服の違いに視線を寄せる'),(1294,322,'転生者だと気づく'),(1630,512,'レン自身が受け止める')]):
    add('orientation-'+str(i+1),'e01-orientation',phrase,[0,y,724,h],panels=[i],lines=[i],pause=[70,65,24,65,150][i])
for i,(y,h,phrase) in enumerate([(0,432,'まず魔力を測ると伝える'),(448,686,'測定場所まで移動する'),(1146,461,'水晶と手を置く場所を見せる'),(1619,532,'使える魔力量がわかると聞く')]):
    add('measurement-guide-'+str(i+1),'e01-instruction',phrase,[0,y,724,h],panels=[i],lines=[i],pause=[70,100,60,125][i])
whole('hesitation','力への期待を一拍置く',width=90,pause=75)
whole('touch','指先が水晶に触れる短い動作',width=78,align='right',pause=35)
add('waiting-question','e01-waiting','手を置いたまま確かめる',[0,9,724,1131],panels=[0],lines=[0],pause=120)
add('waiting-voice','e01-waiting','画面外のルークの声だけが白い余白に残る',new='wait-voice',panels=[1],lines=[1],pause=80)
add('waiting-device','e01-waiting','数値の出ていない装置。まだ結果は見せない',[0,1753,724,388],panels=[2],width=86,align='right',pause=420)
whole('result','長い待ちの後、物理装置のゼロを初めて見せる',width=88,align='right',pause=180)
add('zero-verdict','e01-confirmation','ルークの短い判定',[0,66,724,804],panels=[0],lines=[0],pause=65)
add('zero-eyes','e01-confirmation','説明より先に目の反応',[0,896,724,186],panels=[1],width=92,pause=100)
add('zero-answer','e01-confirmation','レンがゼロを聞き返す',[0,1107,724,1033],panels=[2],lines=[1],pause=160)
whole('stakes','戦えないという現実を伝える',width=94,pause=85)
whole('rejection','騎士の評価が落ちる',width=88,align='right',pause=235)
add('empty-hand','zero_reaction','黙って裸の手を見る。思考の文字は次の余白へ',[380,0,742,1402],panels=[0],width=80,pause=135)
add('despair-voice','zero_reaction','何もできないという思いだけが白く残る',new='despair-voice',lines=[0],pause=320)
add('distant-tremor','tremor','まだ原因を見せず、振動の音だけを聞かせる',new='tremor-sound',sounds=[0],pause=145)
add('boot-tremor','tremor','足元の石が跳ねる。音の物理的な反応',new='tremor-detail',panels=[0],width=80,align='left',pause=105)
add('danger-warning','e01-danger','警告が入り、振動の原因へ視線を誘導',[0,0,724,358],panels=[0],lines=[0],pause=150)
add('danger-geography','e01-danger','巨兵、橋のミラ、上のレン、下の幌を一画面でつなぐ',[0,358,724,1317],panels=[1],sounds=[0,1],pause=25)
add('danger-princess','e01-danger','橋にいる人物が姫だとわかる',[0,1692,724,480],panels=[2],lines=[1],pause=35)
whole('fall','落下の縦方向を画面いっぱいに追う',pause=160)
add('decision-voice','leap','魔力はなくても手を伸ばす。飛ぶ前の決意だけを余白で読む',new='decision-voice',lines=[0],pause=85)
add('leap','leap','素手で飛び出す。決意は繰り返さず動作音へ',new='leap-no-thought',panels=[0],sounds=[0],pause=16)
whole('e01-catch','手をつかみ、幌へ向かう動作を短くつなぐ',pause=22)
whole('landing','幌で衝撃を受け、生存を確かめる',pause=155)
add('safe-both','e01-safe-01','二人とも生きていることを確かめる',[0,10,836,746],panels=[0],pause=85)
add('safe-thanks','e01-safe-01','お礼とレンの反応を横並びで見る',[0,772,836,390],panels=[1,2],lines=[0],pause=55)
add('safe-mira','e01-safe-01','救った相手が名乗る',[0,1181,836,685],panels=[3],lines=[1],pause=72)
add('princess-name','e01-safe-02','王女だと明かす',[0,0,724,394],panels=[0],lines=[0],pause=70)
add('princess-reaction','e01-safe-02','驚きは小さい目の接写で示す',[0,413,724,151],panels=[1],pause=55)
add('ren-name','e01-safe-02','レンが名乗り返す',[0,582,724,503],panels=[2],lines=[1],pause=80)
add('safe-relief','e01-safe-02','無事だったことを優先する',[0,1100,724,1072],panels=[3],lines=[2],pause=220)
for i,(y,h,phrase) in enumerate([(0,604,'音と位置で巨兵が再接近する'),(622,310,'危険が続くと気づく'),(949,502,'ミラを後ろへ下げる'),(1471,698,'今度は自分が止めると決める')]):
    add('approach-'+str(i+1),'e01-approach',phrase,[0,y,725,h],panels=[i],lines=[] if i==0 else [i-1],sounds=[0] if i==0 else [1] if i==2 else [],pause=[35,40,40,180][i])
add('core-first-light','e01-core','まだ素手。胸に最初の星がともる',[0,0,724,1092],panels=[0],lines=[0],sounds=[0],pause=90)
add('core-condition','e01-core','救命行動が起動条件だったと表示する',[0,1118,724,429],panels=[1],texts=[0],pause=90)
add('core-armor-name','e01-core','装甲の名を知る',[0,1564,724,575],panels=[2],texts=[1],pause=140)
add('armor-start','e01-armor-route','胸の核から装甲展開を開始する',[0,0,887,1193],panels=[0],texts=[0],pause=55)
add('armor-route','e01-armor-route','光が腕へ走り、装甲の経路を見せる',[0,1203,887,556],panels=[1],sounds=[0],pause=40)
add('armor-click','e01-armor-assemble','一つの接続音だけが余白で鳴る',new='click',sounds=[0],pause=42)
add('armor-parts','e01-armor-assemble','手首と脚を斜めの横並びで装着する',[0,0,946,706],new='assembly-click-off',panels=[0,1],sounds=[1],pause=18)
add('armor-lock','e01-armor-assemble','胸の装甲が固定される',[0,719,946,917],new='assembly-click-off',panels=[2],sounds=[2],texts=[0],pause=32)
add('armor-movement','e01-armor-check','握った手で動作を確かめる',[0,0,887,1127],panels=[0],lines=[0],sounds=[0],pause=48)
add('core-reserve','e01-armor-check','六区画のうち四つ点灯。有限の救済核を見せる',[0,1145,887,337],panels=[1],texts=[0],width=90,pause=75)
add('connection-voice','e01-armor-check','接続完了の通知だけが余白に出る',new='notice',texts=[1],pause=55)
add('connection-light','e01-armor-check','細い光だけが次の姿へ視線を運ぶ',new='light',pause=160)
whole('hero','全身装甲を初めて披露する。ミラは背後で安全',pause=80)
whole('punch','一撃で紫の核を砕く。音を動作に密着させる',pause=210)
for i,(y,h,phrase) in enumerate([(0,511,'ミラが魔力ゼロなのか確かめる'),(532,529,'レンは短く答える'),(1088,225,'装甲の手が緩む'),(1333,839,'役立たずではなかったという余韻')]):
    add('relief-'+str(i+1),'e01-relief',phrase,[0,y,724,h],panels=[i],lines=[i] if i<2 else [2] if i==3 else [],pause=[55,48,110,360][i])
add('fragment-pickup','e01-fragment','破片を拾う。王冠の面はまだ見せない',[0,0,724,364],panels=[0],width=90,align='left',pause=680)
add('fragment-emblem','e01-fragment','次のスクロールで王冠の紋章を初めて発見',[0,383,724,607],panels=[1],pause=200)
add('fragment-recognition','e01-fragment','ミラが王家の工房の紋章だと告げる',[0,1016,724,444],panels=[2],lines=[0],pause=180)
add('fragment-question','e01-fragment','なぜ襲ったのか。答えを次話へ残す',[0,1480,724,683],panels=[3],lines=[1],pause=460)

plan = dict(edition='scroll-pacing-20261007',sourceCommit='336aea791f6f11c698a7d28f399b687e8a2876fb',
    scope='Complete Episode 1; canonical dialogue, 73 panel beats and staged lore preserved',
    layout=dict(referenceWidth=390,paper='#ffffff',sources=list(sources.values()),units=units),
    review=dict(browser='pending',physicalDevice='not_run'))
(STATE/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(f'{len(units)} display beats, {len(sources)} unique sources')
