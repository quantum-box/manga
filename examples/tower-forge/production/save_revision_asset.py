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
    parser.add_argument('--episode',type=int,default=1)
    parser.add_argument('--repair',default='')
    parser.add_argument('--prompt',type=Path,required=True)
    parser.add_argument('--reference',action='append')
    args=parser.parse_args()
    episode_dir=ROOT/f'episode-{args.episode:02d}'
    name=f'r{args.scene:02d}'+('-'+args.repair if args.repair else '')+'.png'
    target=episode_dir/'art'/name
    if target.exists():raise SystemExit(f'Already exists: {target}')
    prompt=args.prompt.read_text()
    shutil.copyfile(args.source,target)
    path=ROOT/'production/revision-provenance.json'
    record=dict(episode=args.episode,scene=args.scene,file=str(target.relative_to(episode_dir)),
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
