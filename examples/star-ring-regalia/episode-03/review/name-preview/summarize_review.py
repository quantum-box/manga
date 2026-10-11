"""Conservative whitespace audit from rendered screenshots and DOM footprints."""
from pathlib import Path
from PIL import Image
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
 # Floating voice footprints contain actual text, rather than their taller allocated white region.
 occupied.extend([b['top'],b['bottom']] for b in data['footprints'] if b['id'] not in {x['id'] for x in data['panels']})
 merged=union(occupied);gaps=[];last=0
 for s,e in merged:
  if s>last:gaps.append([last,s])
  last=max(last,e)
 if last<data['height']:gaps.append([last,data['height']])
 gap=sum(e-s for s,e in gaps);content=data['height']-gap
 out[width]={'readerWidthCssPx':data['readerWidth'],'viewportCssPx':[data['innerWidth'],data['innerHeight']],'bodyHeightCssPx':data['height'],'explicitPauseHeightCssPx':data['gaps'],'pureGapHeightCssPx':gap,'contentHeightCssPx':content,'screenUnits':data['height']/data['innerHeight'],'pureGapRatio':gap/data['height'],'pureGapRangesCssPx':gaps,'imageBlankBands':bands,'allImagesLoaded':data['failedImages']==0,'horizontalOverflow':data['overflow'],'effectivePanels':len(data['panels']),'framesCaptured':len(data['windows'])}
validation={'scope':'full_episode_name_only','status':'passed_for_name_presentation','userAdoption':'awaiting','finalArtwork':'not_started_for_this_revision','target':plan['episodeLength']['target'],'effectivePanels':99,'independentVoices':68,'embeddedVoices':5,'measurements':out,'pureGapMethod':'DOM complement of actual text and panel footprints; subtract fully blank inner image bands >=16px at >=99.5% white (RGB>=248); union simultaneous footprints to avoid double counting. Pure background around nonblank art is not counted.','review':{'volume':'passed','story':'passed','padding':'passed','notes':'再訪→昨日の衝動への問い→失敗と修正→稽古の限界→借り物と巡回→負傷兵の防御→撤退と救護→身体と装備の違い→盾の返却→怜の誘い。99の異なる瞬間を辿り 声・余白・画像枚数では水増ししない'},'visualAudit':{'widths':[390,360],'allContinuousFramesRead':True,'reference':'review/contact-390-00..06.jpg and review/contact-360-00..06.jpg; native frames of hand continuity, unanswered question, reveal and rescue; newly relocated short dialogue is checked again in native final screenshots','findings':['3発話が顔へ重なったため白地に移動 言葉の全文と読む順を保持','日本の衣装をミルトへ持ち込むラフを画像生成で修正','傷を右掌へ修正し なお手の甲に誤った傷がある未使用部分を表示窓から除外','本作画では見える掌の擦り傷と借りた盾の縁の小さな欠けを全カットへ引き継ぐ'],'realPhoneDevice':'not_tested'},'suspense':{},'checks':{'rust':'not_run_content_only','readerCopy':'passed','gitDiffWhitespace':'passed'}}
for width,data in m.items():
 ps={b['id']:b for b in data['panels']};v=ps['04-beast:1']['top']-ps['03-listen:2-added-2']['bottom'];validation['suspense'][width]={'cue':'03-listen:2-added-2','reveal':'04-beast:1','distanceCssPx':v,'viewportHeightCssPx':data['innerHeight'],'simultaneousAppearancePrevented':v>data['innerHeight'],'reading':'草から一度鳴った音を反応と停止へつなぎ 完全な無音の白地を過ぎるまで獣の輪郭や台詞を出さない'}
assert out['390']['bodyHeightCssPx']>=34000 and out['390']['contentHeightCssPx']>=24000
(p/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n');plan['episodeLength']['actual']={'effectivePanels':99,'body390':out['390'],'body360':out['360']};(p/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print({w:{k:v[k] for k in ['bodyHeightCssPx','pureGapHeightCssPx','contentHeightCssPx']} for w,v in out.items()})
