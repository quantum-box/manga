#!/usr/bin/env python3
"""Propose full-width panel/gutter boundaries for subsequent visual review."""
from pathlib import Path
import json
import numpy as np
from PIL import Image
BASE=Path(__file__).resolve().parents[2]
CONFIG=Path(__file__).with_name('windows.proposed.json')
config=json.loads(CONFIG.read_text()) if CONFIG.exists() else {}
for ep in range(2,11):
 for p in sorted((BASE/f'episode-{ep:02d}'/'art').glob('*remake*.png')):
  key=f'{ep}/'+('00-remake-opening' if p.stem=='remake-00-opening' else p.stem)
  if key in config:continue
  a=np.asarray(Image.open(p).convert('RGB'));h,w,_=a.shape
  b=a[:,int(w*.015):int(w*.985)]
  dark=(b.mean(axis=2)<105).mean(axis=1)>.88
  white=((b[:,:,0]>235)&(b[:,:,1]>228)&(b[:,:,2]>211)).mean(axis=1)>.94
  cand=np.flatnonzero(dark|white)
  groups=[]
  for y in cand:
   if not groups or y>groups[-1][-1]+24:groups.append([int(y)])
   else:groups[-1].append(int(y))
  cuts=[]
  for g in groups:
   y=(g[0]+g[-1])//2
   if y<130 or y>h-130 or (cuts and y-cuts[-1]<125):continue
   cuts.append(y)
  # These are proposals; validation remains pending until images and seams are read.
  i=int(p.name[:2])-1 if p.name[:2].isdigit() else -1
  rhythmic=[[50,120,70,260,170,120],[90,180,60,140,270,130],[45,24,130,240,80,160],[65,200,90,340,130,190],[40,70,160,90,230,150],[160,240,90,190,300,110],[65,30,130,220,140,180],[140,210,100,180,270,160]]
  pauses=[rhythmic[max(0,i)][j%6] for j in range(len(cuts))]+[160 if i<0 else [100,220,70,260,120,340,110,420][i]]
  if i==2 and len(cuts)>=4:pauses[3]=910
  config[key]={'cuts':cuts,'pauses':pauses,'review':'proposed: must visually check boundaries, dialogue and state','method':'full-width dark frame / ivory gutter; original PNG unchanged'}
CONFIG.write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
for key,value in config.items():print(key,value['cuts'])
