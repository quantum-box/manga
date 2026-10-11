"""Check adopted composition, offline pixels, and both phone widths."""
from pathlib import Path
import base64
import hashlib
import json
import re
import html
import runpy
png_storage = runpy.run_path(str(Path(__file__).with_name('png-storage.py')))

p = Path(__file__).resolve().parent
ep = p.parents[1]
name = ep / 'review/name-preview'
read = lambda f: json.loads(f.read_text())
adoption, plan, state = [read(f) for f in [name/'adoption.json', name/'plan.json', p/'state.json']]
assert hashlib.sha256((name/'index.html').read_bytes()).hexdigest() == adoption['approvedHtmlSha256']
panels = [b for b in plan['beats'] if b['type'] == 'panel']
layout = read(ep/'layout.json')
assert len(layout) == len(panels) == 85
for adopted, final in zip(panels, layout):
    assert {k:v for k,v in adopted.items() if k != 'image'} == {k:v for k,v in final.items() if k != 'image'}
def mapping(html):
    return json.loads(re.search(r'<script type="application/json" id="artwork-sources">(.*?)</script>', html, re.S)[1])
external, offline = [(f.read_text(), mapping(f.read_text())) for f in [ep/'index.html', ep/'reader.html']]
letters = read(p/'lettering/state.json')
assert len(external[1]) == len(offline[1]) == len(state['assets']) + len(letters['sheets']) == 35
for key, path in external[1].items():
    inside = base64.b64decode(offline[1][key].split(',',1)[1])
    original = (ep/path).read_bytes()
    if key.startswith('letter-'):
        assert png_storage['pixel_stream'](inside) == png_storage['pixel_stream'](original)
        assert [(k,d) for k,d in png_storage['chunks'](inside) if k != b'IDAT'] == [(k,d) for k,d in png_storage['chunks'](original) if k != b'IDAT']
    else:
        assert inside == original
for asset in state['assets']:
    assert hashlib.sha256((p/asset['destination']).read_bytes()).hexdigest() == asset['sha256']
# Metadata equality is distinct from the recorded visual review of raster glyphs.
adopted_voices = [b for b in plan['beats'] if b['type'] == 'voice']
generated_voices = [v for s in letters['sheets'] for v in s['voices']]
assert len(adopted_voices) == len(generated_voices) == 60
for a, v in zip(adopted_voices, generated_voices):
    assert all(a[k] == v[k] for k in ('id', 'text', 'speaker'))
    assert v['visualTextReview'] == 'exact_full_text_and_columns_verified_native'
    assert v['mobileReview'] == 'readable_390_360'
    alt = html.escape(v['speaker'] + '「' + v['text'].replace('\n', ' ') + '」', quote=True)
    assert f'alt="{alt}"' in external[0]
for sheet in letters['sheets']:
    assert hashlib.sha256((p/'lettering'/sheet['destination']).read_bytes()).hexdigest() == sheet['sha256']
    assert not sheet['pixelsEditedAfterGeneration']
assert len(letters['embeddedDialogue']) == 3
assert all(e['visualTextReview'] == 'exact_full_text_verified_native_and_390_360' for e in letters['embeddedDialogue'])
assert not re.search(r'class="(?:voice-copy|voice-balloon|dialogue |dialogue-text|sfx)', external[0])
m = read(p/'review/measurements.json')
for width, data in m.items():
    assert data['innerWidth'] == data['readerWidth'] == int(width)
    assert data['failedImages'] == 0 and not data['overflow']
    assert len(data['panels']) == 85 and len(data['voices']) == 60
    assert len(data['voiceFit']) == 60
    for v in data['voiceFit']:
        b,t = v['box'],v['beat']
        assert b['left'] >= t['left'] - 1 and b['right'] <= t['right'] + 1, v['id']
        assert b['top'] >= t['top'] - 1 and b['bottom'] <= t['bottom'] + 1, v['id']
whitespace = read(p/'review/whitespace.json')
assert 34000 <= whitespace['390']['bodyHeightCssPx'] <= 60000
assert whitespace['390']['contentHeightCssPx'] >= 24000
print('PASS: approved 85-panel layout; 35 pixel-identical offline artworks; 63 generated dialogues with visual review at 390/360; regular length')
