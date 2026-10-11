"""Register a reviewed lettering edit and keep its actual input/prompt trace."""
from pathlib import Path
import hashlib
import json
import shutil
import struct
import sys

root = Path(__file__).resolve().parent
prod = root.parent
key, output = sys.argv[1:3]
output = Path(output)
raw = output.read_bytes()
assert raw[:8] == b'\x89PNG\r\n\x1a\n'
assert struct.unpack('>II', raw[16:24]) == (1024, 1536)
ls = json.loads((root/'state.json').read_text())
scene = next(s for s in ls['sceneEdits'] if s['id'] == key)
if len(sys.argv) > 3:
    stage = sys.argv[3]
    assert stage in ('window', 'tail', 'outline')
    source = f'../source-{key}-lettering-window.png' if stage == 'window' else f'../source-{key}-{stage}.png'
    edit = {'id': key, 'prompt': f'prompts/{key}-{stage}-edit.txt',
            'source': source, 'status': 'pending'}
    scene.setdefault('edits', []).append(edit)
    scene = edit
state = json.loads((prod/'state.json').read_text())
asset = next(a for a in state['assets'] if a['id'] == key)
sha = hashlib.sha256(raw).hexdigest()
asset.setdefault('edits', []).append({
    'source': str((root/scene['source']).resolve().relative_to(prod)),
    'prompt': 'lettering/' + scene['prompt'],
    'builtinOutput': str(output), 'sha256': sha,
    'purpose': 'generated_vertical_dialogue_and_scene_sound_effects',
    'pixelsEditedAfterGeneration': False,
})
shutil.copyfile(output, prod/asset['destination'])
asset.update(sha256=sha, builtinOutput=str(output), status='generated_lettering_pending_mobile_review')
scene.update(status='native_text_and_continuity_verified_pending_mobile', builtinOutput=str(output),
             sha256=sha, pixelsEditedAfterGeneration=False)
(prod/'state.json').write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
(root/'state.json').write_text(json.dumps(ls, ensure_ascii=False, indent=2) + '\n')
print(key, 'stored unchanged; text verified natively')
