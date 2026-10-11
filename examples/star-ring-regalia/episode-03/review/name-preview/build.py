import json,copy,sys,math
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[5]; dest=root/'examples/star-ring-regalia/episode-03/review/name-preview'
import subprocess
# Rebuilding the draft must not silently reset a later human adoption.
adoption_path=dest/'adoption.json'
if adoption_path.exists() and json.loads(adoption_path.read_text()).get('status')!='awaiting_user_adoption':
 raise SystemExit('This composition has an adoption decision; revise explicitly rather than resetting it')
old=json.loads(subprocess.check_output(['git','show','bf149ef8c0a0b3f5de0233e54d307e598794d967:examples/star-ring-regalia/episode-03/review/name-preview/plan.json'],cwd=root)); panels=[copy.deepcopy(b) for b in old['beats'] if b['type']=='panel']; src={b['id']:copy.deepcopy(b) for b in panels}
# Preserve source sheets byte-for-byte; only change display windows and reading order.
def sheetcell(name,slot,alt,id):
 col=1 if slot%2 else 0; row=(slot-1)//2
 return dict(id=id,type='panel',image='rough/'+name,imageSize=[1024,1536],crop=[(col*512+4)/1024,(row*512+4)/1536,504/1024,504/1536],alt=alt,widthPercent=90,align='right',frame='none',purpose=alt,dialogue=[],sounds=[])
def speak(p,who,text,kind='spoken'):
 p['dialogue']=[dict(speaker=who,text=text,kind=kind,x=66,y=0,width=30,tail='down-left')];return p
changes={
'00-japan:1':sheetcell('connection.png',1,'日本の土曜の朝 航は傷のない右掌を見つめる ミルトの痛みと昨夜の問いが残る','00-japan:1'),
'00-japan:1-added-2':sheetcell('connection.png',2,'日本の台所 母を振り返り空の皿を運ぶ ゲームへ逃げる前に自分の仕事を終える','00-japan:1-added-2'),
'00-yard:1':sheetcell('connection.png',3,'ミルトの安全広場に再接続 右掌の昨日の擦り傷を見つける 剣は左腰に納刀 盾なし','00-yard:1'),
'00-yard:1-added-1':sheetcell('connection.png',4,'左掌に使えなかった銅貨が二枚 右掌の擦り傷をかばって小袋へ戻す 日本へ銅貨を運ばない','00-yard:1-added-1'),
'00-yard:2':sheetcell('connection.png',5,'安全広場から訓練場へ歩いて来た航 リゼは予備の木盾を点検 航の手に気づく','00-yard:2'),
'00-yard:2-added-1':sheetcell('connection.png',6,'リゼは航の右掌の擦り傷を見て確かめる 触れて治療する魔法は使わない','00-yard:2-added-1'),
'00-yard:2-added-2':copy.deepcopy(src['00-yard:2'])}
for p in panels:
 if p['id'] in changes:
  original_id=p['id'];p.update(changes[p['id']]);p['id']=original_id
# This version starts from the adopted episode 2 wound and failed attempt, not cheerful event recruitment.
texts={
'00-japan:1':('航（心）','こっちの手は\nなんともない','thought'),
'00-japan:1-added-1':('美和','お皿\nお願いね','spoken'),
'00-japan:1-added-2':('航','うん\n洗ってから行く','spoken'),
'00-japan:2':('航（心）','今日は\nちゃんと聞こう','thought'),
'00-yard:1':('航（心）','まだ\n残ってる','thought'),
'00-yard:1-added-1':('航（心）','パンも\n買えなかった','thought'),
'00-yard:2':('リゼ','来たね\n手はどう？','spoken'),
'00-yard:2-added-1':('航','握ると\n少し痛い','spoken'),
'00-yard:2-added-2':('リゼ','痛むなら\n途中で止めよう','spoken'),
'02-rest:2-added-1':('航','俺だけ\nすぐ疲れるのかと\n思った','spoken'),
'03-patrol:1':('リゼ','足元も見て\n私から離れないで','spoken'),
'03-patrol:3-added-1':('航','待って！\nまだ何がいるか…','spoken'),
'06-returner:2':('航','さっきの人…\n戻れたんだ','spoken'),
'07-local:1':('航','兵士さんの傷も\n作り直せば\n治る？','spoken'),
'07-local:2':('セナ','この人には\nこの身体しか\nないんだ','spoken'),
'07-local:3':('リゼ','明日は休んで\n巡回は代わるから','spoken'),
'07-promise:1-added-1':('航','縁が\n少し欠けた','spoken'),
'07-promise:1-added-2':('リゼ','見せてくれて\nありがとう\nここは直せる','spoken'),
'08-invitation:3':('怜','討伐隊\n一緒に来るか？','spoken')}
for p in panels:
 if p['id'] in texts:speak(p,*texts[p['id']])
newtexts=[('航','昨日…\n剣を抜きかけた','昨日の衝動を自分の言葉で認める'),('リゼ','抜いたあと\nどうするつもり\nだった？','勝てるかでなく行動の先を尋ねる'),('航','…わからない','聞かれて初めて準備のない自分に気づく'),('航','あの人を\n止めたかった\nだけで','掌と鞘を見て悔しさを言葉にする'),('リゼ','じゃあ今日は\n身を守る\nところから','木剣を選び実行できる範囲へ導く'),('航','うん\n教えて','相手を倒すためだけでなく習うことを選ぶ')]
new=[]
for i,(who,t,why) in enumerate(newtexts,1):
 p=sheetcell('lesson-choice.png',i,why,f'01-choice:{i}');speak(p,who,t);new.append(p)
idx=next(i for i,p in enumerate(panels) if p['id']=='01-lesson:1');panels[idx:idx+3]=new
# A rare star-ring resonance gives KOH the decisive strike, not only observation.
power_specs=[
 ('05-resonance:1',1,'航の瞳に細い環の光が映る 盾で兵士を守った直後 初めて魔力に感応する','航（心）','今…'),
 ('05-resonance:2',2,'航だけの視界 獣の肩から魔力の爪へ細い光の筋が見える 未来や相手の心は見えない','航（心）','線が\n見える'),
 ('05-resonance:3',3,'盾の後ろに兵士を残し 航が自分の右手の剣で細い筋へ短く踏み込む 足から肩と刃へ動作がつながる',None,None),
 ('05-defense:3',4,'航の一閃が獣の爪の魔力を斬り裂く 太い斜めの軌跡と衝撃で獣を退ける 決め手は航 兵士は左盾の後ろで安全',None,None),
 ('05-resonance:5',5,'援護を始めていたリゼが 航の一撃を見て剣を下げ驚く 風が決め手だったと見せない','リゼ','今の…\n航が？'),
 ('05-resonance:6',6,'光が消えた自分の右手の剣を見る航 獣は逃げ 兵士は生きている 立ったまま驚きを受け止める','航（心）','俺が…？')]
power=[]
for ident,slot,why,who,t in power_specs:
 # This source sheet has row-major left-to-right cells, unlike the earlier sources.
 col=(slot-1)%2;row=(slot-1)//2
 q=sheetcell('resonance.png',slot,why,ident)
 bounds=[(10,5,496,411),(520,5,493,411),(10,430,494,570),(522,429,491,570),(10,1020,495,508),(522,1020,491,508)]
 x,y,w,h=bounds[slot-1];q['crop']=[x/1024,y/1536,w/1024,h/1536]
 if who:speak(q,who,t,'thought' if '心' in who else 'spoken')
 if ident=='05-defense:3':q['sounds']=[dict(text='ザンッ',x=22,y=60,width=34)]
 power.append(q)
pos=next(i for i,q in enumerate(panels) if q['id']=='05-defense:3')
panels[pos:pos+1]=power

# The source middle-right hand has an incorrect back-of-hand mark. Use only the face.
face=next(p for p in panels if p['id']=='00-yard:1');face['crop']=[.507,.336,.484,.19];face['alt']='ミルトへ戻った航が右掌へ視線を落とし 顔を曇らせる 掌の傷は次の小袋のカットで確かめる'
# Replace repeated static instructions with an actual spar and an early flicker.
def motioncell(name,slot,why,ident,who=None,text=None,kind='spoken'):
 q=sheetcell(name,slot,why,ident)
 col=(slot-1)%2;row=(slot-1)//2
 q['crop']=[(col*512+10)/1024,(row*512+7)/1536,496/1024,497/1536]
 if who:speak(q,who,text,kind)
 return q
panels=[p for p in panels if p['id'] not in {'00-japan:1-added-1','00-japan:1-added-3','01-choice:2','01-choice:3','01-choice:5','02-change:2-added-1','02-change:3-added-1','06-returner:3-added-1','06-supply:1-added-1','06-supply:2-added-1','07-local:2-added-1','07-local:2-added-2','07-clinic:2-added-1'}]
for p in panels:
 if p['id']=='01-choice:1':speak(p,'航','昨日…\n剣を抜きかけた')
 if p['id']=='01-choice:4':speak(p,'航','あの人を\n止めたくて')
 if p['id']=='01-choice:6':speak(p,'リゼ','じゃあ一本\n受けてみて')
 if p['id']=='00-japan:1-added-2':speak(p,'航','皿を洗ったら\n行ってくる')
 if p['id']=='00-japan:2':speak(p,'航（心）','今度は\n守れるように','thought')
 if p['id']=='02-change:3-added-2':speak(p,'リゼ','傷つけたら\n隠さず見せてね')
 if p['id']=='06-supply:1':speak(p,'係の人','次の身体も\n予備の用意が\nいるからね')
 if p['id']=='06-supply:2':speak(p,'帰還者','剣は川か…\nひとりじゃ\n取りに行けないな')
 if p['id']=='08-invitation:1':speak(p,'怜','あの一閃\n見事だったな')
 if p['id']=='05-resonance:1':
  p['alt']=p['purpose']='盾が爪を止めた直後 航の瞳に稽古で見えた細い光が戻る'
  speak(p,'航（心）','さっきの\n光…！','thought')
 if p['id']=='05-resonance:2':speak(p,'航（心）','この筋へ\n合わせれば…','thought')
 if p['id']=='05-resonance:6':speak(p,'航（心）','剣まで\n軽くなった…？','thought')
training=[
 motioncell('training-motion.png',1,'リゼの低い薙ぎへ航が両手握りに戻り 左盾が落ちる 足と刃の動きから稽古を始める','01-spar:1','リゼ','いくよ！'),
 motioncell('training-motion.png',2,'盾より下を木剣が軽く触れ 航が足を引く ケガを足さず盾の隙を示す','01-spar:2'),
 motioncell('training-motion.png',3,'航が右木剣で打ち返すが リゼが外へ回り 空振りする','01-spar:3','航','まだ…！'),
 motioncell('training-motion.png',4,'航は片膝で体勢を戻し リゼが盾と足の隙を指す 急いだ結果が目に見える','01-spar:4','リゼ','剣だけ\n追ってる'),
 motioncell('training-motion.png',5,'リゼが外へ踏む足を実演 航が見る 地面の線と靴の方向が次の修正へつながる','01-spar:5','リゼ','外へ一歩\n盾を残して'),
 motioncell('training-motion.png',6,'航が足を動かして左盾で木剣を受ける 右木剣を自由に残す 起点 接触 結果を近く読む','01-spar:6','航','受けた！'),
 motioncell('training-flicker.png',1,'リゼが左掌から弱い風を流す 盾で防ぐ次の練習 右手は木剣','02-flicker:1','リゼ','次は風\n無理に受けず\n離れていいよ'),
 motioncell('training-flicker.png',2,'航の瞳に風とは違う細い光が映る 現在流れる魔力へ初めて感応','02-flicker:2','航（心）','今の\n細い光…','thought'),
 motioncell('training-flicker.png',3,'光の筋が空ける風の隙間へ航の足が飛ぶ 足場から太い軌道と土がつながる','02-flicker:3'),
 motioncell('training-flicker.png',4,'航がリゼの剣側の外へ異常に速く入り 右木剣を肩の手前で止める 左盾も残す リゼの間合いを一度破る','02-flicker:4'),
 motioncell('training-flicker.png',5,'リゼが予想外の速さに目を開く 教えた受けとは違う特別な踏み込みが分かる','02-flicker:5','リゼ','その踏み込み\n教えてないよ'),
 motioncell('training-flicker.png',6,'もう一度試した航の木剣をリゼが普通に受ける 光は消えたままで同じ速さは再現できない','02-flicker:6','航（心）','もう\n見えない…','thought'),
 motioncell('star-question.png',1,'水を飲んでいた航が空へ目を上げる 木剣と盾はベンチ 左腰に鋼剣を納刀','02-star:1','航','ねえ リゼ\n星環って\n何なんだろう'),
 motioncell('star-question.png',2,'ミルトの屋根の上 空全体を横切る巨大な星環 そこから細い一本の光が降りる 航の主観','02-star:2'),
 motioncell('star-question.png',3,'リゼが空の環を指す 日常で知っている範囲だけ話す 起源や運営の秘密へ進まない','02-star:3','リゼ','魔力はあそこから\n巡るって\n言われてるよ'),
 motioncell('star-question.png',4,'航が右指で星環から下りる細い線をなぞる リゼの風の光と同じだと気づく','02-star:4','航','あそこから降りる\n細い線も？\nさっきの風にも…'),
 motioncell('star-question.png',5,'リゼは航の指す何もない空を見る 線が共有されないことを表情で示す','02-star:5','リゼ','線？\nどこに？'),
 motioncell('star-question.png',6,'航が空になった右指を見る 細い光は消える 星環そのものは空に残る 答えを持たないまま先へ','02-star:6','航','今はもう\n消えちゃった')
]
start=next(i for i,p in enumerate(panels) if p['id']=='01-lesson:2')
end=next(i for i,p in enumerate(panels) if p['id']=='02-change:1')
# Keep one prop transfer; the rest of the lesson occurs through exchanges.
panels[start:end]=[panels[start]]+training
for p in panels:
 p['sourceId']=p['id'];p['effective']=True
 if p['id']=='07-promise:1-added-1':p['alt']='航は借りた盾の縁の小さな欠けを持ち主リゼへ見せる 木は自動で修復しない'
# Existing sheets leave a lettering reserve in their upper part; trim unused space, not the source image.
for p in panels:
 if p['image'] not in ['rough/connection.png','rough/lesson-choice.png','rough/training-motion.png','rough/training-flicker.png','rough/star-question.png']:
  x,y,w,h=p['crop']; p['crop']=[x,y+h*.18,w,h*.82]
# Japanese chores and quiet confession have medium close shots; geography and hero results are wide.
for i,p in enumerate(panels):
 id=p['id'];wide=any(k in id for k in ['patrol:1','beast:1','defense:3','recover:3','promise:3','invitation:3']) or id in {'01-spar:1','01-spar:3','01-spar:6','02-flicker:1','02-flicker:4','02-star:2'}
 p['widthPercent']=100 if wide else [82,92,78,94,86][i%5]
 p['align']='center' if wide else ['right','left','right','left','right'][i%5]
 p['frame']='none' if wide or i%4==0 else 'thin'
 p['newUnderstanding']=p['purpose']
# Final art must preserve these exact independent voices and layouts. No quotas on in-image lettering.
embedded={'03-patrol:3','05-recover:1','08-invitation:2'}
# Sparse scene spaces combine a main shot with a small offset detail / reply, rather than cards only.
pairs=[('03-patrol:2','03-patrol:2-added-1'),('07-promise:1','07-promise:1-added-1')]
pairfirst={a:(a,b) for a,b in pairs}; pairsecond={b for a,b in pairs}
pauses={'00-japan:1':150,'00-japan:2':260,'00-yard:1-added-1':110,'00-yard:2-added-2':120,'01-choice:2':260,'01-choice:4':200,'01-choice:6':140,'02-distance:3':130,'02-retry:3':180,'02-rest:2-added-1':150,'02-change:3-added-2':250,'03-listen:2-added-2':900,'04-beast:2':200,'05-defense:3':100,'05-recover:3':260,'06-supply:3':230,'07-local:2':280,'07-clinic:2-added-1':140,'07-promise:3':400,'08-invitation:3':330}
pauses.update({'01-choice:4':60,'01-choice:6':40,'01-spar:2':35,'01-spar:4':70,'01-spar:6':90,'02-flicker:2':45,'02-flicker:3':25,'02-flicker:4':150,'02-flicker:6':120,'02-star:2':140,'02-star:5':160,'02-star:6':100})
beats=[];decisions=[];pure=[]
def nat(p):
 _,_,w,h=p['crop'];return 390*p['widthPercent']/100*(1536*h)/(1024*w)
def addvoice(p,d,composition=None,off=0):
 longest=max(map(len,d['text'].split('\n')));height=max(170,80+longest*22)
 if p['id'] in {'03-patrol:3-added-1','05-defense:1','01-spar:1'}:height+=44
 v=dict(id=p['id']+'-voice',type='voice',speaker=d['speaker'],text=d['text'],height=height,x=67 if p['align']!='left' else 34,y=50,purpose=p['purpose']+' 発話は白地で独立して読み 同じ人物の反応へ渡す',kind=d['kind'])
 if composition:v.update(composition=composition,offsetX=0,offsetY=off,widthPercent=45,x=50)
 beats.append(v);return height
for i,p in enumerate(panels):
 d=p.get('dialogue',[]);placement='embedded' if p['id'] in embedded else 'independent' if d else 'silent'
 decisions.append(dict(id=p['id'],placement=placement,dialogue=copy.deepcopy(d),reason='切迫した呼びかけ または短い返答を動きと読む' if placement=='embedded' else '白地の声と表情の距離を保つ' if d else '新しい動作と状態を絵だけで読む'))
 # Preserve designed sound source. Reeds already contain ガサ…; do not letter it again.
 if p['id']=='03-listen:1':p['sounds']=[]
 if placement=='independent':
  p['dialogue']=[]
  if p['id'] in pairsecond:
   a=next(x for x in panels if x['id']==next(a for a,b in pairs if b==p['id']));group='space-'+a['id'];off=nat(a)*.65
   addvoice(p,d[0],group,off+nat(p)+15)
  else:addvoice(p,d[0])
 if p['id'] in pairfirst:
  p['widthPercent']=62;p.update(composition='space-'+p['id'],offsetX=0,offsetY=0,align='left')
 elif p['id'] in pairsecond:
  a=next(x for x in panels if x['id']==next(a for a,b in pairs if b==p['id']));p['widthPercent']=34;p.update(composition='space-'+a['id'],offsetX=66,offsetY=nat(a)*.65,align='right')
  # A dialogue inside the narrow detail would be illegible; already independent.
 beats.append(p)
 if p['id'] in pauses:
  h=pauses[p['id']];nxt=panels[i+1]['id'] if i+1<len(panels) else 'end'
  purpose=('草の音と停止の反応を受け 獣の姿を下で初めて見せる' if 'listen' in p['id'] else '問いの返答を待つ' if p['id']=='01-choice:2' else '結果を受け止め 次の動作や場所へ切り替える')
  g=dict(id=p['id']+'-pause',type='pause',height=h,purpose=purpose);beats.append(g);pure.append(dict(**g,before=p['id'],after=nxt,background='white',contents='none'))
# The faint continuation from reeds belongs to that one sound, not another rustle.
plan=dict(schema='webtoon-name-preview/v1',title='星環のレガリア 第3話 星環の剣筋',referenceWidth=390,colorMode='monochrome',status='awaiting_user_adoption',scope='full_episode',baseCommit='bf149ef8c0a0b3f5de0233e54d307e598794d967',beats=beats,pureGaps=pure,notes=['第2話の擦り傷 銅貨二枚 抜刀を止められた経験から続く','静的な指導と確認の反復を削り 動く稽古の攻防へ置換','航だけの光の知覚と異常な踏み込みを序盤で見せ 救助の一閃へつなぐ','空の星環から巡る魔力という日常知識と リゼに見えない細い線へ触れる','文字と余白を有効コマ数へ加算しない','本作画はこの構成の採用後'],episodeLength=dict(scope='full_episode',target=dict(widthCssPx=390,bodyHeightCssPx=[34000,60000],minContentHeightCssPx=24000,effectivePanels=[80,120]),planned=dict(effectivePanels=len(panels)),actual=None))
dest.mkdir(parents=True,exist_ok=True)
for name,obj in [('plan.json',plan),('layout-decisions.json',decisions),('effective-panels.json',dict(scope='full_episode',count=len(panels),panels=panels)),('adoption.json',dict(status='awaiting_user_adoption',scope='episode_03_revision_after_adopted_episode_02',finalArtAuthorized=False,date='2026-10-11',previousNameAdoption='Historical 2026-10-09 approval applies only to the prior episode-03 composition in Git history'))]:
 (dest/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('panels',len(panels),'beats',len(beats),'independent',sum(d['placement']=='independent' for d in decisions),'embedded',sum(d['placement']=='embedded' for d in decisions))
