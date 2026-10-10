"""Bundle each unchanged source PNG once, shared by its four display crops."""
from pathlib import Path
from html.parser import HTMLParser
import base64, json, hashlib, html, re
prod=Path(__file__).resolve().parent
ep=prod.parents[1]
source=(ep/'index.html').read_text()
files=list(dict.fromkeys(re.findall(r'<img src="([^"]+)"',source)))
chunks=[]; lines=[]; size=0; hashes={}
for i,f in enumerate(files):
 raw=(ep/f).read_bytes(); hashes[f]=hashlib.sha256(raw).hexdigest()
 line='window.regaliaArt['+json.dumps(f)+']='+json.dumps(base64.b64encode(raw).decode())+';\n'
 if size+len(line)>40*1024*1024 and lines: chunks.append(''.join(lines)); lines=[];size=0
 lines.append(line);size+=len(line)
if lines:chunks.append(''.join(lines))
css=(ep/'reader.css').read_text();source=source.replace('<link rel="stylesheet" href="reader.css">','<style>'+css+'</style>')
source=re.sub(r'<img src="([^"]+)"',lambda m:'<img data-art="'+m[1]+'"',source)
scripts=['<script>window.regaliaArt={};</script>']
for i,chunk in enumerate(chunks,1):
 name=f'reader-art-{i:02}.js';(ep/name).write_text(chunk);scripts.append(f'<script src="{name}"></script>')
scripts.append('''<script>window.webtoonReady=(async()=>{for(const [file,data] of Object.entries(window.regaliaArt)){const raw=atob(data),bytes=Uint8Array.from(raw,c=>c.charCodeAt(0)),url=URL.createObjectURL(new Blob([bytes],{type:'image/png'}));const images=[...document.querySelectorAll('img[data-art="'+file+'"]')];for(const img of images)img.src=url;await Promise.all(images.map(i=>i.decode()));}window.regaliaArt={};})();</script>''')
source=source.replace('</body>',''.join(scripts)+'</body>')
(ep/'reader.html').write_text(source)
(prod/'offline-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(f'Packaged {len(files)} unchanged PNGs once in {len(chunks)} companion files')
