#!/usr/bin/env python3
"""Select generated edits without modifying raster pixels."""
from pathlib import Path
import hashlib,json,sys
BASE=Path(__file__).resolve().parents[1]
for spec in sys.argv[1:]:
    number,scene_id,edited=spec.split(':');d=BASE/f'episode-{int(number):02d}'
    art=d/'art'/f'{edited}.png';prompt=d/'generation'/f'{edited}.prompt.txt';metadata=d/'generation'/f'{edited}.json'
    assert art.is_file() and prompt.is_file() and metadata.is_file(),spec
    m=json.loads((d/'manifest.json').read_text());scene=next(s for s in m['scenes'] if s['id']==scene_id);previous=d/scene['art']
    scene['art']=f'art/{edited}.png'
    edit={'prompt':f'generation/{edited}.prompt.txt','record':f'generation/{edited}.json'}
    if edit not in scene.setdefault('edits',[]):scene['edits'].append(edit)
    (d/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
    record=json.loads(metadata.read_text())
    if not record.get('reference_files'):record['reference_files']=[{'path':str(previous.relative_to(d)),'sha256':hashlib.sha256(previous.read_bytes()).hexdigest()}]
    metadata.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    f=d/'PROMPTS.md';title=f'## 採用した修正：{edited}'
    if title not in f.read_text():f.write_text(f.read_text()+f'\n{title}\n\n```text\n{prompt.read_text()}\n```\n')
    print(f'Episode {number}: {scene_id} -> {edited}')
