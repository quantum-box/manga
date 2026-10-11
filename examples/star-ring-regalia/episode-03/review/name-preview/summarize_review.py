"""Conservative whitespace audit from rendered screenshots and DOM footprints."""
from pathlib import Path
from PIL import Image, ImageDraw
import json, math
p=Path(__file__).resolve().parent;m=json.loads((p/'review/measurements.json').read_text());plan=json.loads((p/'plan.json').read_text());out={}
def union(a):
 result=[]
 for s,e in sorted(a):
  if result and s<=result[-1][1]:result[-1][1]=max(e,result[-1][1])
  elif e>s:result.append([s,e])
 return result
for width,data in m.items():
 im=Image.open(p/f'review/full-{width}.png').convert('RGB');occupied=[];bands=[]
 for b in data['panels']:
  x0=max(0,math.ceil(b['left'])+3);x1=min(im.width,math.floor(b['right'])-3);y0=math.ceil(data['top']+b['top'])+2;y1=math.floor(data['top']+b['bottom'])-2
  empty=[];start=None
  # Only full-width blank runs within a panel. Borders and watercolor content are excluded.
  for y in range(y0,y1):
   row=list(im.crop((x0,y,x1,y+1)).getdata());blank=row and sum(min(rgb)>=248 for rgb in row)/len(row)>=.995
   if blank and start is None:start=y
   if not blank and start is not None:
    if y-start>=16:empty.append([start-data['top'],y-data['top']])
    start=None
  if start is not None and y1-start>=16:empty.append([start-data['top'],y1-data['top']])
  last=b['top']
  for s,e in empty:
   occupied.append([last,s]);last=e;bands.append({'panel':b['id'],'top':s,'bottom':e,'height':e-s})
  occupied.append([last,b['bottom']])
 # Floating voice footprints include the balloon; add its tail/dots below the outline.
 occupied.extend([b['top'],b['bottom']] for b in data['footprints'] if b['id'] not in {x['id'] for x in data['panels']})
 occupied.extend([v['box']['top'],v['box']['bottom']+24] for v in data.get('voiceFit',[]))
 merged=union(occupied);gaps=[];last=0
 for s,e in merged:
  if s>last:gaps.append([last,s])
  last=max(last,e)
 if last<data['height']:gaps.append([last,data['height']])
 gap=sum(e-s for s,e in gaps);content=data['height']-gap
 out[width]={'readerWidthCssPx':data['readerWidth'],'viewportCssPx':[data['innerWidth'],data['innerHeight']],'bodyHeightCssPx':data['height'],'explicitPauseHeightCssPx':data['gaps'],'pureGapHeightCssPx':gap,'contentHeightCssPx':content,'screenUnits':data['height']/data['innerHeight'],'pureGapRatio':gap/data['height'],'pureGapRangesCssPx':gaps,'imageBlankBands':bands,'allImagesLoaded':data['failedImages']==0,'horizontalOverflow':data['overflow'],'effectivePanels':len(data['panels']),'framesCaptured':len(data['windows'])}
validation={'scope':'full_episode_name_only','status':'passed_for_name_presentation','userAdoption':'awaiting','finalArtwork':'not_started_for_this_revision','target':plan['episodeLength']['target'],'effectivePanels':len([b for b in plan['beats'] if b['type']=='panel']),'independentVoices':len([b for b in plan['beats'] if b['type']=='voice']),'embeddedVoices':sum(len(b.get('dialogue',[])) for b in plan['beats'] if b['type']=='panel'),'measurements':out,'pureGapMethod':'DOM complement of text/balloon and panel footprints, including 24px below balloon outlines for tails and thought dots; subtract fully blank inner image bands >=16px at >=99.5% white (RGB>=248); union simultaneous footprints to avoid double counting. Pure background around nonblank art is not counted.','review':{'volume':'passed','story':'passed','padding':'passed','notes':'再訪→昨日の衝動→低い薙ぎと空振り→外へ一歩で受ける→風の光→異常な踏み込み→リゼの驚き→再試行→星環と見えない線→巡回→負傷兵の防御→同じ光と一閃→救護→身体と装備の違い→盾の返却→怜の誘い。85の異なる瞬間を辿り反復を削る'},'visualAudit':{'widths':[390,360],'allContinuousFramesRead':True,'reviewMethod':'All 60 independent voices are reviewed with their neighboring panels in balloons-390-00..05 and balloons-360-00..05. Text insets and allocated voice regions are measured in both widths. The 85 panel crops, including 18 new training/star-ring moments, are reviewed; full continuous windows are refreshed.','reference':'review/balloons-390-00..05.jpg and review/balloons-360-00..05.jpg; refreshed review/contact-390-00..07.jpg and review/contact-360-00..07.jpg; native windows for speech, thought, urgent warning and combined detail layouts','findings':['独立した60発話を吹き出しに配置 字と輪郭の内側余白と尾の方向を確認','星環共鳴の知覚から踏み込み 一閃 リゼの驚き 逃げる獣までを両幅で確認','3発話が顔へ重なったため白地に移動 言葉の全文と読む順を保持','日本の衣装をミルトへ持ち込むラフを画像生成で修正','傷を右掌へ修正し なお手の甲に誤った傷がある未使用部分を表示窓から除外','本作画では見える掌の擦り傷と借りた盾の縁の小さな欠けを全カットへ引き継ぐ'],'realPhoneDevice':'not_tested'},'suspense':{},'checks':{'rust':'not_run_content_only','readerCopy':'passed','gitDiffWhitespace':'passed'}}
validation['balloons']={'independent':60,'spoken':47,'urgentShouts':3,'thoughts':10,'embedded':3,'source':'balloon-decisions.json','voiceTextRevised':True,'newArtworkSheets':3,'pixelsEditedAfterGeneration':False,'shapeAndTailAudit':'Both widths: 60 voice regions with neighboring panels; ordinary speech uses tails, urgent calls use thick spikes, thoughts use cloud outlines and dots'}
choices=json.loads((p/'balloon-decisions.json').read_text())
validation['balloons'].update(independent=len(choices),spoken=sum(c['kind']=='spoken' for c in choices),urgentShouts=sum(c['kind']=='shout' for c in choices),thoughts=sum(c['kind']=='thought' for c in choices))
for width,data in m.items():
 for v in data.get('voiceFit',[]):
  b,c,t=v['box'],v['copy'],v['beat']
  assert c['left']>=b['left']+10 and c['right']<=b['right']-10 and c['top']>=b['top']+10 and c['bottom']<=b['bottom']-10,v['id']
  assert b['top']>=t['top']-2 and b['bottom']+24<=t['bottom']+12,v['id']
 ps={b['id']:b for b in data['panels']};v=ps['04-beast:1']['top']-ps['03-listen:2-added-2']['bottom'];validation['suspense'][width]={'cue':'03-listen:2-added-2','reveal':'04-beast:1','distanceCssPx':v,'viewportHeightCssPx':data['innerHeight'],'simultaneousAppearancePrevented':v>data['innerHeight'],'reading':'草から一度鳴った音を反応と停止へつなぎ 完全な無音の白地を過ぎるまで獣の輪郭や台詞を出さない'}
assert 34000<=out['390']['bodyHeightCssPx']<=60000 and out['390']['contentHeightCssPx']>=24000
assert 80<=validation['effectivePanels']<=120
assert all(d['failedImages']==0 and not d['overflow'] for d in m.values())
(p/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n');plan['episodeLength']['actual']={'effectivePanels':len([b for b in plan['beats'] if b['type']=='panel']),'body390':out['390'],'body360':out['360']};(p/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print({w:{k:v[k] for k in ['bodyHeightCssPx','pureGapHeightCssPx','contentHeightCssPx']} for w,v in out.items()})
for width,data in m.items():
 im=Image.open(p/f'review/full-{width}.png').convert('RGB');w=int(width)
 for group in range(math.ceil(len(data['voices'])/12)):
  sheet=Image.new('RGB',(w*3,440*4),'#ddd');draw=ImageDraw.Draw(sheet)
  for i,v in enumerate(data['voices'][group*12:(group+1)*12]):
   start=max(0,int(data['top']+v['top']-25));end=min(im.height,int(data['top']+v['bottom']+110))
   crop=im.crop((0,start,w,end))
   if crop.height>410:crop=crop.resize((round(w*410/crop.height),410))
   x=(i%3)*w;y=(i//3)*440;sheet.paste(crop,(x,y+24));draw.text((x+5,y+6),v['id'],fill='#000')
  sheet.save(p/f'review/balloons-{width}-{group:02d}.jpg',quality=92)
 for group in range(math.ceil(len(data['windows'])/9)):
  h=data['innerHeight'];sheet=Image.new('RGB',(w*3,(h+24)*3),'#ddd');draw=ImageDraw.Draw(sheet)
  for i,v in enumerate(data['windows'][group*9:(group+1)*9]):
   frame=Image.open(p/'review'/v['file']).convert('RGB');x=(i%3)*w;y=(i//3)*(h+24)
   sheet.paste(frame,(x,y+24));draw.text((x+5,y+5),v['file'],fill='#000')
  sheet.save(p/f'review/contact-{width}-{group:02d}.jpg',quality=92)
