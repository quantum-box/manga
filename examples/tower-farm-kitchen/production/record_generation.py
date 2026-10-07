#!/usr/bin/env python3
"""Copy a built-in imagegen original, unchanged, and record provenance."""
from pathlib import Path
import hashlib
import json
import shutil
import struct
import sys

source=Path(sys.argv[1]); target=Path(sys.argv[2])
if target.exists():
    raise FileExistsError(f'Already adopted: {target}')
target.parent.mkdir(parents=True,exist_ok=True)
shutil.copyfile(source,target)
original=hashlib.sha256(source.read_bytes()).hexdigest()
assert original==hashlib.sha256(target.read_bytes()).hexdigest()
header=target.read_bytes()[:24]
assert header[:8]==b'\x89PNG\r\n\x1a\n'
width,height=struct.unpack('>II',header[16:24])
prompt=target.parent.parent/'generation'/f'{target.stem}.prompt.txt'
metadata={'tool':'built-in image_gen','source_filename':source.name,
          'adopted':str(target.relative_to(target.parent.parent)),
          'original_sha256':original,'adopted_sha256':original,
          'width':width,'height':height,'prompt_file':str(prompt.relative_to(target.parent.parent)),
          'prompt':prompt.read_text(),'text_review':'pending','continuity_review':'pending'}
references=[Path(value) for value in sys.argv[3:]]
if references:
    import os
    metadata['reference_files']=[{'path':os.path.relpath(path,target.parent.parent),
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest()} for path in references]
(target.parent.parent/'generation'/f'{target.stem}.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
print(f'Adopted {target.stem}: {width}x{height}, unchanged SHA-256')
