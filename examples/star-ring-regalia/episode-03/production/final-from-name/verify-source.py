"""Check adopted composition, offline bytes, and both phone widths."""
from pathlib import Path
import base64
import hashlib
import json
import re
from html.parser import HTMLParser

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
assert len(external[1]) == len(offline[1]) == len(state['assets']) == 20
for key, path in external[1].items():
    assert base64.b64decode(offline[1][key].split(',',1)[1]) == (ep/path).read_bytes()
for asset in state['assets']:
    assert hashlib.sha256((p/asset['destination']).read_bytes()).hexdigest() == asset['sha256']
# Lettering is deliberately retained verbatim from the adopted reader.
class Voices(HTMLParser):
    def __init__(self, source, target='voice-copy'):
        super().__init__(); self.voices=[]; self.depth=0; self.target=target; self.feed(source)
    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get('class','').split()
        if self.depth:
            if tag not in ['br', 'img', 'hr']: self.depth+=1
            if tag == 'br': self.voices[-1]+='\n'
        elif self.target in classes:
            self.depth=1; self.voices.append('')
    def handle_endtag(self, tag):
        if self.depth: self.depth-=1
    def handle_data(self, data):
        if self.depth: self.voices[-1]+=data
adopted_voices = Voices((name/'index.html').read_text()).voices
assert len(adopted_voices) == 60
assert adopted_voices == Voices(external[0]).voices
embedded_voices = Voices((name/'index.html').read_text(), 'dialogue-text').voices
assert len(embedded_voices) == 3
assert embedded_voices == Voices(external[0], 'dialogue-text').voices
m = read(p/'review/measurements.json')
for width, data in m.items():
    assert data['innerWidth'] == data['readerWidth'] == int(width)
    assert data['failedImages'] == 0 and not data['overflow']
    assert len(data['panels']) == 85 and len(data['voices']) == 60
    for v in data['voiceFit']:
        b,c,t = v['box'],v['copy'],v['beat']
        assert c['left'] >= b['left']+10 and c['right'] <= b['right']-10, v['id']
        assert c['top'] >= b['top']+10 and c['bottom'] <= b['bottom']-10, v['id']
        assert b['top'] >= t['top']-2 and b['bottom']+24 <= t['bottom']+12, v['id']
whitespace = read(p/'review/whitespace.json')
assert 34000 <= whitespace['390']['bodyHeightCssPx'] <= 60000
assert whitespace['390']['contentHeightCssPx'] >= 24000
print('PASS: approved 85-panel layout; 20 exact offline PNGs; 60 voices at 390/360; regular length')
