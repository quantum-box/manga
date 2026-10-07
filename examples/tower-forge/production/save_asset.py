#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copy each unmodified generated PNG and record its source hash immediately."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('episode',type=int);parser.add_argument('scene',type=int);parser.add_argument('source',type=Path)
    args=parser.parse_args()
    target=ROOT/f'episode-{args.episode:02d}/art/{args.scene:02d}.png'
    if target.exists():raise SystemExit(f'Already exists, do not overwrite: {target}')
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(args.source,target)
    manifest=ROOT/'production/asset-provenance.json'
    records=json.loads(manifest.read_text()) if manifest.exists() else []
    references=['reference/party.png']
    if args.episode in [6,7,8,9]:references.append('episode-03/art/01.png')
    if args.episode==7:references.append('episode-06/art/04.png')
    if args.episode in [8,9]:references.append('episode-07/art/04-door.png')
    if args.episode==9:references.append('episode-08/art/04.png')
    if args.episode==10:references.extend(['episode-05/art/01.png','episode-09/art/03.png'])
    record=dict(episode=args.episode,scene=args.scene,source=str(args.source),adopted=str(target.relative_to(ROOT)),sha256=hashlib.sha256(target.read_bytes()).hexdigest(),method='built_in_image_gen',prompt=f'episode-{args.episode:02d}/PROMPTS-USED.md',references=references)
    records.append(record);manifest.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Saved episode {args.episode}, scene {args.scene}.')
if __name__=='__main__':main()
