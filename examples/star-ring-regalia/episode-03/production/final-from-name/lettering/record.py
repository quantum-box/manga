"""Store unchanged image_gen originals and non-destructive display windows."""
from pathlib import Path
import hashlib
import json
import shutil
import struct
import sys
from PIL import Image

root = Path(__file__).resolve().parent
state_path = root / 'state.json'
state = json.loads(state_path.read_text())
key, source = sys.argv[1:3]
sheet = next(s for s in state['sheets'] if s['id'] == key)
source = Path(source)
raw = source.read_bytes()
assert raw[:8] == b'\x89PNG\r\n\x1a\n'
width, height = struct.unpack('>II', raw[16:24])
assert (width, height) == (1024, 1536), (width, height)
destination = root / sheet['destination']
destination.parent.mkdir(exist_ok=True)
shutil.copyfile(source, destination)
im = Image.open(source).convert('RGB')
for i, voice in enumerate(sheet['voices']):
    x, y = (i % 2) * 512, (i // 2) * 768
    # Reading pixels only: the original is never cropped, resized or retouched.
    cell = im.crop((x, y, x + 512, y + 768))
    mask = cell.convert('L').point(lambda p: 255 if p < 120 else 0)
    bounds = mask.getbbox()
    assert bounds, voice['id']
    l, t, r, b = bounds
    assert l > 5 and t > 5 and r < 507 and b < 763, (key, i, bounds)
    l, t, r, b = max(0, l - 12), max(0, t - 12), min(512, r + 12), min(768, b + 12)
    crop = [x + l, y + t, r - l, b - t]
    scale = min(.37, voice['height'] * .96 / crop[3])
    voice['cropPixels'] = crop
    voice['widthAt390'] = round(crop[2] * scale, 3)
    voice['heightAt390'] = round(crop[3] * scale, 3)
    voice['visualTextReview'] = 'pending'
sheet.update(status='generated_pending_visual_review', builtinOutput=str(source),
             sha256=hashlib.sha256(raw).hexdigest(), size=[width, height],
             pixelsEditedAfterGeneration=False)
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
print(key, [v['cropPixels'] for v in sheet['voices']])
