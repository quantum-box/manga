#!/usr/bin/env python3
"""Preview generated final-art originals without replacing the adopted reader."""
import argparse, hashlib, html, json, struct
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('plan',type=Path)
parser.add_argument('--episode-dir',type=Path,required=True)
args=parser.parse_args()
plan=json.loads(args.plan.read_text());root=args.episode_dir.resolve()
parts=['<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>星環のレガリア 作画確認</title><style>*{box-sizing:border-box}body{margin:0;background:white}main{width:min(100%,420px);margin:auto;container-type:inline-size}img{display:block;width:100%;height:auto}figure{margin:0}.pause{height:var(--gap)}.pending{padding:40px 20px;border:1px dashed #777;font:16px sans-serif}</style><main>']
geometry=[]
for a in plan['assets']:
 path=root/a['file'];gap=a['gapBefore390']
 if gap:parts.append(f'<div class="pause" style="--gap:{gap/3.9:.6f}cqw" aria-hidden="true"></div>')
 if path.exists():
  raw=path.read_bytes();assert raw[:8]==b'\x89PNG\r\n\x1a\n';w,h=struct.unpack('>II',raw[16:24])
  src='../../'+a['file']
  parts.append(f'<figure id="{a["id"]}"><img src="{src}" width="{w}" height="{h}" alt="{html.escape(a["alt"],quote=True)}"></figure>')
  geometry.append({'id':a['id'],'width':w,'height':h,'imageHeight390':h*390/w,'gapBefore390':gap,'sha256':hashlib.sha256(raw).hexdigest()})
 else:parts.append(f'<div class="pending">未制作：{html.escape(a["id"])}</div>')
parts.append('</main></html>')
out=root/'review/final-from-name';out.mkdir(parents=True,exist_ok=True)
(out/'index.html').write_text('\n'.join(parts)+'\n')
(out/'generated-geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'generated':len(geometry),'total':len(plan['assets']),'generatedImageHeight390':sum(g['imageHeight390'] for g in geometry),'preview':str(out/'index.html')},ensure_ascii=False))
