#!/usr/bin/env python3
"""Prepare one completed chapter; preserve adopted PNG bytes and phone pauses."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))
from export_latest_webtoons import adopted_chapters

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--episode', type=int, required=True)
    parser.add_argument('--output', type=Path, default=REPO/'publish-output/star-ring-regalia')
    args = parser.parse_args()
    chapter = next(c for c in adopted_chapters(REPO) if c['series'] == 'star-ring-regalia' and c['number'] == args.episode)
    source = ROOT / f'episode-{args.episode:02d}'
    layout = json.loads((source/'layout.json').read_text())
    episode = json.loads((source/'episode.json').read_text())
    alts = {a['id']: a['alt'] for a in episode['assets']}
    target = args.output.resolve() / chapter['id']
    target.mkdir(parents=True, exist_ok=True)
    blocks, assets = [], []
    cover = None
    for item in layout:
        data = (source/item['adoptedArt']).read_bytes()
        sha = hashlib.sha256(data).hexdigest()
        name = f'art-{sha[:24]}.png'
        shutil.copyfile(source/item['adoptedArt'], target/name)
        assets.append({'name':name,'sha256':sha,'bytes':len(data)})
        if item['gapBefore390']:
            blocks.append({'type':'spacer','size':f"phone-{item['gapBefore390']}"})
        blocks.append({'type':'image','src':name,'alt':alts[item['id']]})
        if item['id'] == episode.get('cover_asset_id', '05-first-sky'): cover = name
    blocks.append({'type':'ending','text':f'第{args.episode}話　了'})
    payload = {'title':chapter['title'],'subtitle':chapter['subtitle'],'cover':cover or assets[0]['name'],'blocks':blocks}
    (target/'episode.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    chapter.update(assets=assets,pixelWidth=layout[0]['nativeWidth'],phoneWidth=390)
    manifest = {'baseURL':'https://manga-server.txcloud.app','chapter':chapter}
    (target/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(target/'episode.json')

if __name__ == '__main__': main()
