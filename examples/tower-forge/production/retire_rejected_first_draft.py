#!/usr/bin/env python3
"""Retire the rejected first chapter from this checkout; Git retains its history."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    reader=(ROOT/'episode-01/index.html').read_text()
    assert 'art/r01-monitor.png' in reader and 'art/r14.png' in reader
    old_names=['01.png','01-anatomy.png','02.png','03.png','04.png']
    for name in old_names:
        assert f'src="art/{name}"' not in reader
    for name in old_names:
        path=ROOT/'episode-01/art'/name
        if path.exists():path.unlink()
    for filename in ['asset-provenance.json','repairs.json','used-prompts-initial.json']:
        path=ROOT/'production'/filename
        records=json.loads(path.read_text())
        assert isinstance(records,list),filename
        records=[r for r in records if r.get('episode')!=1]
        path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    print('Rejected chapter-one art retired. Native revision edit sources retained. Old edition remains in Git commit 6c4ee6a.')

if __name__=='__main__':main()
