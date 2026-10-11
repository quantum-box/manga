"""Finish the adopted beat stream by replacing roughs, never changing its layout."""
from pathlib import Path
import base64
import hashlib
import json
import re
import shutil
import struct

prod = Path(__file__).resolve().parent
ep = prod.parents[1]
name = ep / 'review/name-preview'
adoption = json.loads((name / 'adoption.json').read_text())
if adoption['status'] != 'adopted' or not adoption['finalArtAuthorized']:
    raise SystemExit('A recorded adoption is required')
approved = (name / 'index.html').read_bytes()
if hashlib.sha256(approved).hexdigest() != adoption['approvedHtmlSha256']:
    raise SystemExit('Approved reader has changed; re-adopt before production')
plan = json.loads((name / 'plan.json').read_text())
state = json.loads((prod / 'state.json').read_text())
assets = {a['rough']: a for a in state['assets']}
sources = list(dict.fromkeys(b['image'] for b in plan['beats'] if b['type'] == 'panel'))
external, embedded, provenance = {}, {}, []
for i, source in enumerate(sources):
    a = assets[source]
    raw = (prod / a['destination']).read_bytes()
    size = struct.unpack('>II', raw[16:24])
    expected = next(b['imageSize'] for b in plan['beats'] if b.get('image') == source)
    if list(size) != expected:
        raise SystemExit(f'Changed cell geometry in {a["id"]}: {size} != {expected}')
    path = f'art/{a["id"]}.png'
    (ep / 'art').mkdir(exist_ok=True)
    if (prod / a['destination']).resolve() != (ep / path).resolve():
        shutil.copyfile(prod / a['destination'], ep / path)
    external[f'asset-{i}'] = path
    embedded[f'asset-{i}'] = 'data:image/png;base64,' + base64.b64encode(raw).decode()
    provenance.append({'id': a['id'], 'path': path, 'sha256': hashlib.sha256(raw).hexdigest(),
                       'nameSource': source, 'prompt': a['prompt'],
                       'editSource': a.get('editSource'), 'editPrompt': a.get('editPrompt'),
                       'edits': a.get('edits', []),
                       'builtinOutput': a['builtinOutput'], 'pixelsEditedAfterGeneration': False})

h = approved.decode()
h = h.replace(' — ネーム確認用', '').replace(' ネーム確認用', '')
h = re.sub(r'<header class="draft-bar">.*?</header>',
           '<header class="episode-heading"><p>星環のレガリア　第3話</p><h1>星環の剣筋</h1></header>', h, flags=re.S)
h = re.sub(r'<details class="notes".*?</details>', '', h, flags=re.S)
h = re.sub(r'<details class="measurement".*?</details>', '', h, flags=re.S)
h = re.sub(r'<footer class="end-note">.*?</footer>', '<footer class="end-note"><p>つづく</p><nav><a href="../episode-02/index.html">前の話</a><br><a class="series-index" href="../index.html">話一覧</a></nav></footer>', h, flags=re.S)
h = h.replace('</head>', '<meta name="manga-title-id" content="star-ring-regalia"><meta name="manga-episode-id" content="episode-03"></head>', 1)
h = h.replace('#preview-flow { filter: grayscale(1); }', '#preview-flow { filter: none; }')
h = h.replace('preview-flow', 'episode-body')
h = h.replace('</style>', '\n.episode-heading{padding:42px 22px 50px}.episode-heading p{font-size:15px;letter-spacing:.08em;margin:0}.episode-heading h1{font-size:27px;line-height:1.5;margin:10px 0}\n</style>', 1)
# The rough painted this sound; finished art deliberately omits letters.
pattern = r'(<figure[^>]*data-beat-id="03-listen:1".*?)(</figure>)'
h, count = re.subn(pattern, r'\1<span class="sfx" aria-label="草の音 ガサ…" style="--x:72%;--y:65%">ガサ…</span>\2', h, flags=re.S)
if count != 1:
    raise SystemExit('Rustle source must occur once')
h = h.replace('id="name-preview-assets"', 'id="artwork-sources"').replace('getElementById("name-preview-assets")', 'getElementById("artwork-sources")')
asset_pattern = r'(<script type="application/json" id="artwork-sources">).*?(</script>)'
def write_reader(path, mapping):
    page = re.sub(asset_pattern, lambda m: m[1] + json.dumps(mapping, ensure_ascii=False) + m[2], h, flags=re.S)
    path.write_text(page)
write_reader(ep / 'index.html', external)
write_reader(ep / 'reader.html', embedded)
panels = [b for b in plan['beats'] if b['type'] == 'panel']
layout = [{**b, 'image': external[f'asset-{sources.index(b["image"])}']} for b in panels]
(ep / 'layout.json').write_text(json.dumps(layout, ensure_ascii=False, indent=2) + '\n')
(prod / 'source-crops.json').write_text(json.dumps(layout, ensure_ascii=False, indent=2) + '\n')
(prod / 'art-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')
print(f'Built {len(panels)} panels / {len(external)} masters; adopted voices and spacing preserved')
