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
# The source middle-right hand has an incorrect back-of-hand mark. Use only the face.
face=next(p for p in panels if p['id']=='00-yard:1');face['crop']=[.507,.336,.484,.19];face['alt']='ミルトへ戻った航が右掌へ視線を落とし 顔を曇らせる 掌の傷は次の小袋のカットで確かめる'
# Original name has a safe two-handed kendo failure; no successful new technique or magic for KOH.
for p in panels:
 p['sourceId']=p['id'];p['effective']=True
 if p['id']=='07-promise:1-added-1':p['alt']='航は借りた盾の縁の小さな欠けを持ち主リゼへ見せる 木は自動で修復しない'
# Existing sheets leave a lettering reserve in their upper part; trim unused space, not the source image.
for p in panels:
 if p['image'] not in ['rough/connection.png','rough/lesson-choice.png']:
  x,y,w,h=p['crop']; p['crop']=[x,y+h*.18,w,h*.82]
# Japanese chores and quiet confession have medium close shots; geography and hero results are wide.
for i,p in enumerate(panels):
 id=p['id'];wide=any(k in id for k in ['patrol:1','beast:1','defense:3','recover:3','promise:3','invitation:3'])
 p['widthPercent']=100 if wide else [82,92,78,94,86][i%5]
 p['align']='center' if wide else ['right','left','right','left','right'][i%5]
 p['frame']='none' if wide or i%4==0 else 'thin'
 p['newUnderstanding']=p['purpose']
# Final art must preserve these exact independent voices and layouts. No quotas on in-image lettering.
embedded={'01-grip:2','03-patrol:3','05-defense:3','05-recover:1','08-invitation:2'}
# Sparse scene spaces combine a main shot with a small offset detail / reply, rather than cards only.
pairs=[('01-grip:2-added-1','01-grip:3'),('02-distance:1','02-distance:1-added-1'),('02-rest:1','02-rest:1-added-1'),('03-patrol:2','03-patrol:2-added-1'),('07-promise:1','07-promise:1-added-1')]
pairfirst={a:(a,b) for a,b in pairs}; pairsecond={b for a,b in pairs}
pauses={'00-japan:1':150,'00-japan:2':260,'00-yard:1-added-1':110,'00-yard:2-added-2':120,'01-choice:2':260,'01-choice:4':200,'01-choice:6':140,'02-distance:3':130,'02-retry:3':180,'02-rest:2-added-1':150,'02-change:3-added-2':250,'03-listen:2-added-2':900,'04-beast:2':200,'05-defense:3':100,'05-recover:3':260,'06-supply:3':230,'07-local:2':280,'07-clinic:2-added-1':140,'07-promise:3':400,'08-invitation:3':330}
beats=[];decisions=[];pure=[]
def nat(p):
 _,_,w,h=p['crop'];return 390*p['widthPercent']/100*(1536*h)/(1024*w)
def addvoice(p,d,composition=None,off=0):
 longest=max(map(len,d['text'].split('\n')));height=max(170,80+longest*22)
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
plan=dict(schema='webtoon-name-preview/v1',title='星環のレガリア 第3話 戻れる剣、戻れない剣',referenceWidth=390,colorMode='monochrome',status='awaiting_user_adoption',scope='full_episode',baseCommit='bf149ef8c0a0b3f5de0233e54d307e598794d967',beats=beats,pureGaps=pure,notes=['第2話の擦り傷 銅貨二枚 抜刀を止められた経験から続く','文字と余白を有効コマ数へ加算しない','本作画はこの構成の採用後'],episodeLength=dict(scope='full_episode',target=dict(widthCssPx=390,bodyHeightCssPx=[34000,60000],minContentHeightCssPx=24000,effectivePanels=[80,120]),planned=dict(effectivePanels=len(panels)),actual=None))
dest.mkdir(parents=True,exist_ok=True)
for name,obj in [('plan.json',plan),('layout-decisions.json',decisions),('effective-panels.json',dict(scope='full_episode',count=len(panels),panels=panels)),('adoption.json',dict(status='awaiting_user_adoption',scope='episode_03_revision_after_adopted_episode_02',finalArtAuthorized=False,date='2026-10-11',previousNameAdoption='Historical 2026-10-09 approval applies only to the prior episode-03 composition in Git history'))]:
 (dest/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('panels',len(panels),'beats',len(beats),'independent',sum(d['placement']=='independent' for d in decisions),'embedded',sum(d['placement']=='embedded' for d in decisions))
