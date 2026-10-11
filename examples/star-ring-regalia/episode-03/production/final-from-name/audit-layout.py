"""Conservative whitespace audit from rendered screenshots and DOM footprints."""
from pathlib import Path
from PIL import Image, ImageDraw
import json, math
p=Path(__file__).resolve().parent;m=json.loads((p/'review/measurements.json').read_text());plan=json.loads((p.parent.parent/'review/name-preview/plan.json').read_text());out={}
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
(p/'review/whitespace.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
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
