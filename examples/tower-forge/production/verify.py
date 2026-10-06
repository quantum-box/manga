#!/usr/bin/env python3
"""Verify the adopted art, standalone readers and saved phone evidence."""
import base64
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Reader(HTMLParser):
    def __init__(self):
        super().__init__(); self.images=[]; self.links=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='img': self.images.append(attrs['src'])
        if tag=='a': self.links.append(attrs.get('href',''))

def check():
    adopted=json.loads((ROOT/'production/adopted-assets.json').read_text())
    image_count = 0
    for n in range(1,11):
        d=ROOT/f'episode-{n:02d}'
        ep=json.loads((d/'episode.json').read_text())
        assets=json.loads((d/'assets.json').read_text())
        count = len(ep['scenes'])
        assert len(assets)==count and count > 0, n
        source=Reader(); source.feed((d/'index.html').read_text())
        packed=Reader(); packed.feed((d/'reader.html').read_text())
        assert len(source.images)==len(packed.images)==count, n
        for i,asset in enumerate(assets,1):
            filename=adopted.get(f'{n}-{i}',{}).get('file',ep['scenes'][i-1]['file'])
            assert asset['file']==source.images[i-1]==filename, (n,i)
            data=(d/filename).read_bytes()
            assert data.startswith(b'\x89PNG\r\n\x1a\n'), (n,i)
            assert hashlib.sha256(data).hexdigest()==asset['sha256'], (n,i)
            uri=packed.images[i-1]
            assert uri.startswith('data:image/png;base64,'), (n,i)
            assert base64.b64decode(uri.split(',',1)[1])==data, (n,i)
        for link in source.links:
            path=urlsplit(link).path
            assert not path or (d/unquote(path)).is_file(), (n,link)
        review=json.loads((d/'validation.json').read_text())
        assert review['raster_lettering_visual'] in [True,'reviewed_at_both_widths'], n
        for width in [390,360]:
            assert (d/f'webtoon-{width}.jpg').is_file(), (n,width)
            assert all((d/f'validation/scene-{i:02d}-{width}.jpg').is_file() for i in range(1,count+1)), (n,width)
        image_count += count
    status=json.loads((ROOT/'production/build-status.json').read_text())
    assert status['ready_episodes']==list(range(1,11))
    print(f'Verified 10 readers, {image_count} adopted PNGs, identical embedded images, {image_count*2} phone scene captures. This does not prove story quality.')

if __name__=='__main__': check()
