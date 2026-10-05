#!/usr/bin/env python3
"""Keep the 1170px render size while choosing PNG or high-quality WebP for delivery."""
import argparse, concurrent.futures, hashlib, io, json
from pathlib import Path
from PIL import Image
parser = argparse.ArgumentParser()
parser.add_argument('source', type=Path)
parser.add_argument('output', type=Path)
args = parser.parse_args()
for manifest in sorted(args.source.glob('*/render.json')):
    folder = args.output / manifest.parent.name
    folder.mkdir(parents=True, exist_ok=True)
    metadata = json.loads(manifest.read_text())
    def convert(block):
        data = (manifest.parent / block['src']).read_bytes()
        image = Image.open(io.BytesIO(data))
        if image.width != 1170:
            raise ValueError('Expected original 1170px render, not an upscaled preview')
        compressed = io.BytesIO()
        image.convert('RGB').save(compressed, format='WEBP', quality=93, method=4)
        webp = compressed.getvalue()
        extension = 'png'
        if len(webp) < len(data) * 0.8:
            data, extension = webp, 'webp'
        name = 'retina-' + hashlib.sha256(data).hexdigest()[:24] + '.' + extension
        (folder / name).write_bytes(data)
        return dict(block, src=name), len(data)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        converted = list(pool.map(convert, metadata['blocks']))
    metadata['blocks'] = [block for block, _ in converted]
    metadata['bytes'] = sum(size for _, size in converted)
    (folder / 'render.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2))
    print(manifest.parent.name, round(metadata['bytes']/1024), 'KB', flush=True)
