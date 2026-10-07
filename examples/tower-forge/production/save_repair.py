#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import hashlib
import json
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('episode',type=int);p.add_argument('scene',type=int);p.add_argument('source',type=Path);p.add_argument('suffix');p.add_argument('prompt',type=Path)
a=p.parse_args();name=f'art/{a.scene:02d}-{a.suffix}.png';target=ROOT/f'episode-{a.episode:02d}'/name
if target.exists():raise SystemExit('Repair target already exists')
shutil.copyfile(a.source,target)
file=ROOT/'production/adopted-assets.json';adopted=json.loads(file.read_text());key=f'{a.episode}-{a.scene}'
previous=adopted.get(key,{}).get('file',f'art/{a.scene:02d}.png')
adopted[key]=dict(file=name,edit_source=previous,reason=a.suffix)
file.write_text(json.dumps(adopted,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
log=ROOT/'production/repairs.json';records=json.loads(log.read_text()) if log.exists() else []
records.append(dict(episode=a.episode,scene=a.scene,source=str(a.source),adopted=name,edit_source=previous,sha256=hashlib.sha256(target.read_bytes()).hexdigest(),prompt=a.prompt.read_text(encoding='utf-8')))
log.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Adopted repair {key}: {name}')
