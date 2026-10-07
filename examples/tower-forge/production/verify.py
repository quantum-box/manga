#!/usr/bin/env python3
"""Verify the adopted art, readers and saved phone evidence."""
import base64
import hashlib
import json
import struct
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def jpeg_size(path):
    data=path.read_bytes()
    assert data[:2]==b'\xff\xd8',path
    position=2
    while position<len(data):
        assert data[position]==255,(path,position)
        while data[position]==255:position+=1
        marker=data[position];position+=1
        if marker in [1,216,217] or 208<=marker<=215:continue
        length=struct.unpack('>H',data[position:position+2])[0]
        if marker in [192,193,194,195,197,198,199,201,202,203,205,206,207]:
            height,width=struct.unpack('>HH',data[position+3:position+7])
            return width,height
        position+=length
    raise AssertionError(path)

class Reader(HTMLParser):
    def __init__(self):
        super().__init__(); self.images=[]; self.links=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='img': self.images.append(attrs['src'])
        if tag=='a': self.links.append(attrs.get('href',''))


def check_source_references(root=ROOT):
    """Keep only reachable generation inputs, including inputs shared across episodes."""
    def normalized(value):
        value = value.removeprefix("examples/tower-forge/")
        return str((root / value).resolve().relative_to(root.resolve()))
    records = {}
    for name in ["asset-provenance.json", "shared-inputs.json", "repairs.json", "revision-provenance.json"]:
        for record in json.loads((root / "production" / name).read_text()):
            key = record["adopted"] if "adopted" in record else f"episode-{record['episode']:02d}/" + record["file"]
            if name == "repairs.json":
                key = str(Path(f"episode-{record['episode']:02d}") / key)
                record = dict(record)
                record["references"] = list(record.get("references", [])) + [
                    str(Path(f"episode-{record['episode']:02d}") / record["edit_source"])]
            records[normalized(key)] = record
    adopted = json.loads((root / "production/adopted-assets.json").read_text())
    pending = []
    for path in root.glob("episode-*/episode.json"):
        episode = json.loads(path.read_text())
        for i, scene in enumerate(episode["scenes"], 1):
            filename = adopted.get(f"{episode['number']}-{i}", {}).get("file", scene["file"])
            pending.append(str(path.parent.relative_to(root) / filename))
    visited = set()
    while pending:
        key = normalized(pending.pop())
        if key in visited:
            continue
        visited.add(key)
        path = root / key
        if not path.is_file():
            raise ValueError("Missing current generation input: " + key)
        record = records.get(key)
        if record is None:
            raise ValueError("Missing generation input hash record: " + key)
        if hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError("Generation input bytes differ: " + key)
        pending.extend(record.get("references", []))
    return visited

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
            if ep.get('revision') == 'continuation-2026-10-07':
                assert uri==filename, (n,i)
                assert (d/'reader.html').read_bytes()==(d/'index.html').read_bytes(), n
            else:
                assert uri.startswith('data:image/png;base64,'), (n,i)
                assert base64.b64decode(uri.split(',',1)[1])==data, (n,i)
        for link in source.links:
            path=urlsplit(link).path
            assert not path or (d/unquote(path)).is_file(), (n,link)
        review=json.loads((d/'validation.json').read_text())
        assert review['raster_lettering_visual'] in [True,'reviewed_at_both_widths'], n
        if ep.get('revision') == 'continuation-2026-10-07':
            assert review['revision'] == ep['revision'], n
            assert review['sceneCount'] == count, n
            assert review['adopted_sha256'] == [a['sha256'] for a in assets], n
            assert review['reader_sha256'] == hashlib.sha256((d/'index.html').read_bytes()).hexdigest(), n
        for width in [390,360]:
            full=next((x for x in review.get('full_reader_captures',[]) if x['width']==width),None)
            if full:
                y=0
                for part in full['parts']:
                    assert part['y']==y,(n,width,part)
                    actual=jpeg_size(d/part['file'])
                    assert actual[0]==width and abs(actual[1]-part['height'])<=1,(n,part,actual)
                    y+=part['height']
                assert y==full['pageHeight'],(n,width,y)
            else:
                assert ep.get('revision') != 'continuation-2026-10-07', (n,width,'missing current full reader capture')
                assert (d/f'webtoon-{width}.jpg').is_file(), (n,width)
            assert all((d/f'validation/scene-{i:02d}-{width}.jpg').is_file() for i in range(1,count+1)), (n,width)
            if ep.get('game_revision') or ep.get('revision'):
                assert sum(len(s['panels']) for s in ep['scenes'])==ep['narrative_panel_count']
                for i,asset in enumerate(assets,1):
                    actual=jpeg_size(d/f'validation/scene-{i:02d}-{width}.jpg')
                    expected=width*asset['height']/asset['width']
                    assert actual[0]==width and abs(actual[1]-expected)<=1,(n,i,width,actual,expected)
        image_count += count
    check_source_references()
    status=json.loads((ROOT/'production/build-status.json').read_text())
    assert status['ready_episodes']==list(range(1,11))
    print(f'Verified 10 readers, {image_count} adopted PNGs, matching reader bytes/references, {image_count*2} phone scene captures. This does not prove story quality.')

if __name__=='__main__': check()
