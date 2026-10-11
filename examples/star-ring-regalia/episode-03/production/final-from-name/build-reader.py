"""Finish the adopted beat stream, with recorded whitespace artwork extensions."""
from pathlib import Path
import base64
import hashlib
import html
import json
import re
import shutil
import struct
import runpy

offline_encoding = runpy.run_path(str(Path(__file__).with_name('png-storage.py')))['offline_encoding']

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
    embedded[f'asset-{i}'] = 'data:image/png;base64,' + base64.b64encode(offline_encoding(raw)).decode()
    provenance.append({'id': a['id'], 'path': path, 'sha256': hashlib.sha256(raw).hexdigest(),
                       'nameSource': source, 'prompt': a['prompt'],
                       'editSource': a.get('editSource'), 'editPrompt': a.get('editPrompt'),
                       'edits': a.get('edits', []),
                       'builtinOutput': a['builtinOutput'], 'pixelsEditedAfterGeneration': False})

lettering = json.loads((prod / 'lettering/state.json').read_text())
voices = {}
for sheet in lettering['sheets']:
    if not sheet.get('sha256'):
        raise SystemExit(f'Lettering has not been generated: {sheet["id"]}')
    raw = (prod / 'lettering' / sheet['destination']).read_bytes()
    if hashlib.sha256(raw).hexdigest() != sheet['sha256']:
        raise SystemExit(f'Lettering original changed: {sheet["id"]}')
    asset_id = f'letter-{sheet["id"]}'
    external[asset_id] = f'art/{sheet["id"]}.png'
    embedded[asset_id] = 'data:image/png;base64,' + base64.b64encode(offline_encoding(raw)).decode()
    for voice in sheet['voices']:
        voices[voice['id']] = {**voice, 'asset': asset_id}
    provenance.append({**{k: sheet[k] for k in ('id', 'sha256', 'prompt', 'builtinOutput', 'pixelsEditedAfterGeneration')}, 'edits': sheet.get('edits', [])})

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
# All lettering is image_gen artwork. HTML contains accessibility metadata only.
def generated_voice(match):
    opening, body = match.groups()
    beat_id = re.search(r'data-beat-id="([^"]+)"', opening)[1]
    voice = voices[beat_id]
    x, y, width, height = voice['cropPixels']
    position = re.search(r'<div class="floating-copy" style="([^"]+)"', body)[1]
    position = re.sub(r'top:[\d.]+%;', 'top:50%;', position)
    display_width = voice['widthAt390'] / 390 * 100
    style = (f'--crop-ratio:{width / height};--crop-image-width:{1024 / width * 100}%;'
             f'--crop-left:{-x / width * 100}%;--crop-top:{-y / height * 100}%;')
    alt = html.escape(voice['speaker'] + '「' + voice['text'].replace('\n', ' ') + '」', quote=True)
    return (opening + f'<div class="floating-copy" style="{position}width:{display_width:.6f}cqw;max-width:none;">'
            f'<div class="voice-art generated-lettering" style="{style}"><div class="crop-window">'
            f'<img data-asset="{voice["asset"]}" alt="{alt}" width="1024" height="1536">'
            '</div></div></div></section>')
h, count = re.subn(r'(<section class="text-beat voice[^>]+>)(.*?)</section>', generated_voice, h, flags=re.S)
if count != 60:
    raise SystemExit(f'Expected 60 generated voice regions, got {count}')
h, count = re.subn(r'<div class="dialogue [^>]+>.*?</div></div>', '', h, flags=re.S)
if count != 3:
    raise SystemExit(f'Expected 3 embedded generated dialogues, got {count}')
h = re.sub(r'<span class="sfx"[^>]*>.*?</span>', '', h, flags=re.S)
for beat in plan['beats']:
    if beat['type'] != 'panel':
        continue
    text = ' '.join(d['speaker'] + '「' + d['text'].replace('\n', ' ') + '」' for d in beat.get('dialogue', []))
    sound = ' '.join(s['text'] for s in beat.get('sounds', []))
    if beat['id'] == '03-listen:1':
        sound = 'ガサ…'
    if text or sound:
        pattern = r'(<figure[^>]*data-beat-id="' + re.escape(beat['id']) + r'".*?<img[^>]*alt=")([^"]*)(")'
        extra = html.escape(' ' + text + (' 効果音 ' + sound if sound else ''), quote=True)
        h, count = re.subn(pattern, lambda m: m[1] + m[2] + extra + m[3], h, flags=re.S)
        if count != 1:
            raise SystemExit(f'Embedded text must have one accessible panel: {beat["id"]}')
h = h.replace('</style>', '''
.generated-lettering{position:relative;width:100%;display:block}
.generated-lettering .crop-window{position:relative;width:100%;overflow:hidden;aspect-ratio:var(--crop-ratio)}
.generated-lettering img{position:absolute;display:block;width:var(--crop-image-width);max-width:none;height:auto;left:var(--crop-left);top:var(--crop-top)}
</style>''', 1)
h = h.replace('id="name-preview-assets"', 'id="artwork-sources"').replace('getElementById("name-preview-assets")', 'getElementById("artwork-sources")')
# Three finished-art extensions keep the same narrative moments and all dialogue.
# Effects and whitespace are generated together; CSS only displays their raw pixels.
effects = json.loads((prod / 'effects/state.json').read_text())
extensions = {a['beatId']: a for a in effects['assets']}
for a in effects['assets']:
    raw = (ep / a['path']).read_bytes()
    if hashlib.sha256(raw).hexdigest() != a['sha256']:
        raise SystemExit(f'Effect original changed: {a["id"]}')
    external[a['id']] = a['path']
    embedded[a['id']] = 'data:image/png;base64,' + base64.b64encode(offline_encoding(raw)).decode()
    pattern = r'<figure[^>]*data-beat-id="' + re.escape(a['beatId']) + r'".*?</figure>'
    previous = re.search(pattern, h, re.S)[0]
    alt = re.search(r'alt="([^"]*)"', previous)[1]
    w, height = a['imageSize']
    replacement = (f'<figure class="panel align-center effect-extension" data-beat-id="{a["beatId"]}" '
                   f'style="--panel-width:100%;"><img data-asset="{a["id"]}" alt="{alt}" '
                   f'width="{w}" height="{height}"></figure>')
    h, count = re.subn(pattern, lambda _: replacement, h, flags=re.S)
    if count != 1:
        raise SystemExit(f'Expected one extension target: {a["beatId"]}')
    provenance.append({**a, 'pixelsEditedAfterGeneration': False})
asset_pattern = r'(<script type="application/json" id="artwork-sources">).*?(</script>)'
def write_reader(path, mapping):
    page = re.sub(asset_pattern, lambda m: m[1] + json.dumps(mapping, ensure_ascii=False) + m[2], h, flags=re.S)
    path.write_text(page)
write_reader(ep / 'index.html', external)
write_reader(ep / 'reader.html', embedded)
panels = [b for b in plan['beats'] if b['type'] == 'panel']
layout = [{**b, 'image': external[f'asset-{sources.index(b["image"])}']} for b in panels]
for panel in layout:
    if panel['id'] in extensions:
        a = extensions[panel['id']]
        panel.update(image=a['path'], imageSize=a['imageSize'], crop=[0, 0, 1, 1],
                     widthPercent=100, align='center', frame='none')
(ep / 'layout.json').write_text(json.dumps(layout, ensure_ascii=False, indent=2) + '\n')
(prod / 'source-crops.json').write_text(json.dumps(layout, ensure_ascii=False, indent=2) + '\n')
(prod / 'art-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')
print(f'Built {len(panels)} panels / {len(external)} originals; 63 generated dialogues, three whitespace extensions')
