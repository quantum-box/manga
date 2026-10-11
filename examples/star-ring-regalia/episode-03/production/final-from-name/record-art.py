"""Save the selected built-in image output unchanged and make restart state explicit."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import struct

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('asset')
parser.add_argument('output', type=Path)
args = parser.parse_args()
prod = Path(__file__).resolve().parent
state_path = prod / 'state.json'
state = json.loads(state_path.read_text())
a = next(a for a in state['assets'] if a['id'] == args.asset)
raw = args.output.read_bytes()
if not raw.startswith(b'\x89PNG\r\n\x1a\n'):
    raise SystemExit('Expected original PNG')
size = struct.unpack('>II', raw[16:24])
if size != (1024, 1536):
    raise SystemExit(f'Inspect changed original dimensions: {size}')
shutil.copyfile(args.output, prod / a['destination'])
a.update(status='generated_pending_reader_review', builtinOutput=args.output.name,
         sha256=hashlib.sha256(raw).hexdigest(), imageSize=list(size), pixelsEditedAfterGeneration=False)
state['completedAssets'] = sum(a['status'] != 'pending' for a in state['assets'])
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
print(f'{args.asset} saved unchanged; {state["completedAssets"]}/{len(state["assets"])} assets generated')
