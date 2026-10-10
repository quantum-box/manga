#!/usr/bin/env python3
"""Copy one generated original unchanged and record its provenance."""
import argparse
import fcntl
import hashlib
import json
import shutil
import struct
import tempfile
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('plan', type=Path)
parser.add_argument('asset_id')
parser.add_argument('source', type=Path)
parser.add_argument('--file', help='Sibling filename relative to the episode')
parser.add_argument('--prompt', type=Path, help='Exact prompt used for this call')
parser.add_argument('--reference', action='append', default=[], help='Actual input reference image for this call')
args = parser.parse_args()
lock_name = hashlib.sha256(str(args.plan.resolve()).encode()).hexdigest()
lock = open(Path(tempfile.gettempdir()) / f'webtoon-plan-{lock_name}.lock', 'a')
fcntl.flock(lock, fcntl.LOCK_EX)
plan = json.loads(args.plan.read_text())
asset = next(a for a in plan['assets'] if a['id'] == args.asset_id)
if args.file:
    asset.setdefault('sourceHistory', []).append({
        'file': asset['file'], 'generation': asset.get('generation'),
        'role': 'unchanged source for image edit',
        'visualReview': asset.get('visualReview'),
    })
    asset['file'] = args.file
episode = args.plan.resolve().parents[2]
target = episode / asset['file']
if target.exists():
    raise SystemExit(f'Refusing to overwrite existing original: {target}')
raw = args.source.read_bytes()
assert raw[:8] == b'\x89PNG\r\n\x1a\n'
target.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(args.source, target)
assert target.read_bytes() == raw
asset.pop('visualReview', None)
asset.update(status='generated; visual review pending', generation={
    'tool': 'built-in image_gen',
    'source': str(args.source.resolve()),
    'sha256': hashlib.sha256(raw).hexdigest(),
    'bytes': len(raw),
    'nativeSize': list(struct.unpack('>II', raw[16:24])),
    'bytesIdentical': True,
    'manualImageEditing': False,
    'recordedAt': datetime.now(timezone.utc).isoformat(),
})
if args.reference:
    asset['generation']['referenceImages'] = args.reference
if args.prompt:
    asset['generation']['prompt'] = str(args.prompt)
    asset['generation']['promptSha256'] = hashlib.sha256(args.prompt.read_bytes()).hexdigest()
args.plan.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'asset': asset['id'], 'original': str(target),
    'size': asset['generation']['nativeSize'], 'status': asset['status']}))
