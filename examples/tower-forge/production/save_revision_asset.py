#!/usr/bin/env python3
"""Copy unmodified built-in art and preserve the exact generation provenance."""
import argparse
import fcntl
import hashlib
import json
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('scene',type=int)
    parser.add_argument('source',type=Path)
    parser.add_argument('--repair',default='')
    parser.add_argument('--prompt',type=Path)
    parser.add_argument('--reference',action='append')
    args=parser.parse_args()
    name=f'r{args.scene:02d}'+('-'+args.repair if args.repair else '')+'.png'
    target=ROOT/'episode-01/art'/name
    if target.exists():raise SystemExit(f'Already exists: {target}')
    shutil.copyfile(args.source,target)
    path=ROOT/'production/revision-provenance.json'
    prompt=json.loads((ROOT/'production/episode-01-revision.json').read_text())['scenes'][args.scene-1]['prompt']
    if args.prompt:prompt=args.prompt.read_text()
    record=dict(episode=1,scene=args.scene,file=str(target.relative_to(ROOT/'episode-01')),
                        source=str(args.source),sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                        method='built_in_image_gen',prompt=prompt,repair=args.repair,
                        references=args.reference or (['reference/party.png'] if not args.repair else [f'episode-01/art/r{args.scene:02d}.png']))
    with path.open('a+',encoding='utf-8') as handle:
        fcntl.flock(handle,fcntl.LOCK_EX)
        handle.seek(0)
        existing=handle.read()
        records=json.loads(existing) if existing else []
        records.append(record)
        handle.seek(0);handle.truncate()
        handle.write(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    print(f'Saved {name} unmodified.')

if __name__=='__main__':main()
