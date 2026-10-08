#!/usr/bin/env python3
"""Compact UTF-8 transport for unchanged PNG bytes in a standalone HTML reader.

Seven-bit values use one byte; HTML-sensitive values share two-byte UTF-8
characters with the next value. This avoids base64's 4/3 expansion without
resizing, recompressing or editing any artwork. The decoder restores original
PNG bytes before giving each image a Blob URL.
"""
import base64
from html.parser import HTMLParser
from pathlib import Path
import json

ILLEGAL = (0, 10, 13, 34, 38, 92, 60)

def encode(raw):
    values = []
    accumulator = bits = 0
    for byte in raw:
        accumulator = (accumulator << 8) | byte
        bits += 8
        while bits >= 7:
            bits -= 7
            values.append((accumulator >> bits) & 127)
        accumulator &= (1 << bits) - 1
    if bits:
        values.append(accumulator << (7 - bits))
    out = []
    i = 0
    while i < len(values):
        value = values[i]
        if value in ILLEGAL:
            if i + 1 < len(values):
                out.append(chr(128 + (ILLEGAL.index(value) << 8) + values[i + 1]))
                i += 1
            else:
                out.append(chr(128 + (7 << 8) + value))
        else:
            out.append(chr(value))
        i += 1
    return ''.join(out)

def decode(encoded, length):
    out = bytearray()
    accumulator = bits = 0
    for char in encoded:
        code = ord(char)
        if code < 128:
            values = (code,)
        else:
            index = code >> 8
            values = (code & 127,) if index == 7 else (ILLEGAL[index], code & 127)
        for value in values:
            accumulator = (accumulator << 7) | value
            bits += 7
            if bits >= 8:
                bits -= 8
                out.append((accumulator >> bits) & 255)
            accumulator &= (1 << bits) - 1
    return bytes(out[:length])

RUNTIME = r'''<script>
window.webtoonReady=(async()=>{
 const illegal=[0,10,13,34,38,92,60];
 const payloads=[...document.querySelectorAll('script[type="application/x-webtoon-native-png"]')].map(element=>({id:element.id,data:element.textContent,length:Number(element.dataset.bytes),element}));
 payloads.push(...(window.webtoonNativeArt||[]));
 for(const payload of payloads){
  const source=payload.data,bytes=new Uint8Array(payload.length);
  let accumulator=0,bits=0,offset=0;
  const push=value=>{accumulator=(accumulator<<7)|value;bits+=7;if(bits>=8){bits-=8;if(offset<bytes.length)bytes[offset++]=(accumulator>>bits)&255;}accumulator&=(1<<bits)-1;};
  for(let i=0;i<source.length;i++){
   const code=source.charCodeAt(i);
   if(code<128)push(code);
   else{const index=code>>8;if(index!==7)push(illegal[index]);push(code&127);}
  }
  if(offset!==bytes.length)throw Error('Incomplete original artwork payload');
  const img=document.querySelector('img[data-native-art="'+payload.id+'"]');
  img.src=URL.createObjectURL(new Blob([bytes],{type:'image/png'}));
  // An offscreen lazy image can wait for scrolling before decoding. Restore
  // every source first so waiting on it cannot hide all later panels.
  if(img.loading!=='lazy')await img.decode();
  payload.element?.remove();payload.data=null;
  await new Promise(resolve=>setTimeout(resolve,0));
 }
 window.webtoonNativeArt=[];
})();
</script>'''

class CompactReader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.parts = []
        self.payloads = []
        self.payload_data = []
        self.payload_position = None
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            self.parts.append(self.get_starttag_text());return
        import html
        values = dict(attrs)
        src = values['src']
        assert src.startswith('data:image/png;base64,')
        raw = base64.b64decode(src.split(',', 1)[1])
        ident = 'native-art-' + str(len(self.payloads))
        encoded = encode(raw)
        assert decode(encoded, len(raw)) == raw
        self.payloads.append(f'<script type="application/x-webtoon-native-png" id="{ident}" data-bytes="{len(raw)}">{encoded}</script>')
        self.payload_data.append({'id':ident,'length':len(raw),'data':encoded})
        attrs = [(name, value) for name, value in attrs if name != 'src']
        attrs.append(('data-native-art', ident))
        self.parts.append('<img'+''.join(' '+name+'="'+html.escape(value,quote=True)+'"' for name,value in attrs)+'>')
    def handle_endtag(self, tag):
        if tag == 'body':
            self.payload_position=len(self.parts)
            self.parts.extend(self.payloads);self.parts.append(RUNTIME)
        self.parts.append('</'+tag+'>')
    def handle_data(self, data):self.parts.append(data)
    def handle_entityref(self, name):self.parts.append('&'+name+';')
    def handle_charref(self, name):self.parts.append('&#'+name+';')
    def handle_decl(self, declaration):self.parts.append('<!'+declaration+'>')
    def handle_comment(self, data):self.parts.append('<!--'+data+'-->')

    def external_payloads(self, path, limit_bytes=50*1024*1024):
        """Keep an oversized episode offline in bounded companion files."""
        path=Path(path)
        chunks=[];chunk=[];size=0
        for payload in self.payload_data:
            # encode() excludes quotes, backslashes, line terminators and '<'.
            # Its remaining codepoints are valid inside a JS double string.
            line='window.webtoonNativeArt.push({id:'+json.dumps(payload['id'])+',length:'+str(payload['length'])+',data:"'+payload['data']+'"});\n'
            byte_count=len(line.encode('utf-8'))
            if byte_count>=limit_bytes:raise ValueError('One artwork exceeds payload file limit')
            if chunk and size+byte_count>=limit_bytes:
                chunks.append(''.join(chunk));chunk=[];size=0
            chunk.append(line);size+=byte_count
        if chunk:chunks.append(''.join(chunk))
        names=[]
        for index, content in enumerate(chunks,1):
            name=f'{path.stem}-art-{index:02d}.js'
            (path.parent/name).write_text(content,encoding='utf-8')
            names.append(name)
        scripts=['<script>window.webtoonNativeArt=[];</script>']
        scripts.extend(f'<script src="{name}"></script>' for name in names)
        position=self.payload_position
        assert position is not None
        output=''.join(self.parts[:position]+scripts+[RUNTIME]+self.parts[position+len(self.payloads)+1:])
        return output,names

def compact(path):
    path=Path(path)
    reader=CompactReader();reader.feed(path.read_text());reader.close()
    output=''.join(reader.parts)
    size=len(output.encode('utf-8'))
    if size>=100*1024*1024:
        output,names=reader.external_payloads(path)
        path.write_text(output,encoding='utf-8')
        print(f'Packaged offline reader with {len(names)} companion payloads: {len(reader.payloads)} original PNGs unchanged')
        return
    path.write_text(output)
    print(f'Compacted standalone reader: {size:,} bytes, {len(reader.payloads)} original PNG payloads unchanged')
