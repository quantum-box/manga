import base64
from html.parser import HTMLParser
import unittest
from pathlib import Path
import re
import tempfile
import json
import shutil
import subprocess

from compact_reader import CompactReader, RUNTIME, decode, encode

class PayloadReader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.payload = ''
        self.inside = False
        self.length = 0
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'script' and values.get('type') == 'application/x-webtoon-native-png':
            self.inside = True
            self.length = int(values['data-bytes'])
    def handle_endtag(self, tag):
        if tag == 'script':self.inside = False
    def handle_data(self, data):
        if self.inside:self.payload += data

class CompactTransportTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('node'), 'Node is required for decoder execution')
    def test_offscreen_lazy_images_do_not_block_later_sources(self):
        originals = [bytes(range(256))*n for n in (1, 2, 3)]
        payloads = [{'id':f'native-art-{i}', 'length':len(raw), 'data':encode(raw)} for i, raw in enumerate(originals)]
        setup = r'''
const images=Array.from({length:3},(_,i)=>({loading:i?'lazy':'eager',src:null,decode(){return i?new Promise(()=>{}):Promise.resolve();}}));
const restored=[];
const URL={createObjectURL(blob){restored.push(blob);return 'blob:'+restored.length;}};
const window={webtoonNativeArt:PAYLOADS};
const document={querySelectorAll(){return [];},querySelector(selector){return images[Number(selector.match(/native-art-(\d+)/)[1])];}};
'''.replace('PAYLOADS', json.dumps(payloads))
        runtime = RUNTIME.removeprefix('<script>').removesuffix('</script>')
        finish = r'''
(async()=>{
 let timer;
 try{
  await Promise.race([window.webtoonReady,new Promise((_,reject)=>{timer=setTimeout(()=>reject(Error('Offscreen image blocked subsequent sources')),250);})]);
  clearTimeout(timer);
  if(images.some(image=>!image.src))throw Error('Missing image source');
  console.log(JSON.stringify(await Promise.all(restored.map(async blob=>[...new Uint8Array(await blob.arrayBuffer())]))));
 }catch(error){clearTimeout(timer);console.error(error.message);process.exitCode=1;}
})();
'''
        result = subprocess.run([shutil.which('node'), '-e', setup+runtime+finish], capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), [list(raw) for raw in originals])

    def test_all_bytes_and_html_delimiters(self):
        raw = bytes(range(256))*4 + b'</script>\r\n\x00"&\\'
        encoded = encode(raw)
        self.assertEqual(decode(encoded, len(raw)), raw)
        self.assertEqual(encoded.encode('utf-8').decode('utf-8'), encoded)
        for forbidden in '\x00\r\n<"&\\':self.assertNotIn(forbidden, encoded)
        self.assertLess(len(encoded.encode()),len(base64.b64encode(raw)))

    def test_partial_final_groups(self):
        for length in range(258):
            for raw in [bytes(length),bytes(i%256 for i in range(length)),bytes((i*97+length)%256 for i in range(length))]:
                with self.subTest(length=length):
                    self.assertEqual(decode(encode(raw),len(raw)),raw)

    def test_html_round_trip_and_japanese_metadata(self):
        raw = bytes(range(256))*8
        source = '<!doctype html><html><head><meta charset="utf-8"><title>水の出口</title></head><body><img alt="コウ&amp;エルナ" src="data:image/png;base64,'+base64.b64encode(raw).decode()+'" width="887" height="1774"></body></html>'
        reader = CompactReader();reader.feed(source);reader.close()
        output = ''.join(reader.parts)
        self.assertIn('<title>水の出口</title>',output)
        self.assertIn('alt="コウ&amp;エルナ"',output)
        parsed = PayloadReader();parsed.feed(output)
        self.assertEqual(decode(parsed.payload,parsed.length),raw)
        self.assertIn('window.webtoonReady=',output)

    def test_companion_payload_boundaries_and_byte_equality(self):
        originals=[bytes(range(256))*n+b'</script>\r\n\x00"&\\' for n in (2,3,4)]
        source='<html><head><title>水の出口</title></head><body>'+''.join('<img alt="水" src="data:image/png;base64,'+base64.b64encode(raw).decode()+'">' for raw in originals)+'</body></html>'
        reader=CompactReader();reader.feed(source);reader.close()
        with tempfile.TemporaryDirectory() as directory:
            output,names=reader.external_payloads(Path(directory)/'reader.html',limit_bytes=1500)
            self.assertEqual(len(names),3)
            restored=[]
            for name in names:
                path=Path(directory)/name
                self.assertLess(path.stat().st_size,1500)
                self.assertIn('<script src="'+name+'"></script>',output)
                length=int(re.search(r'length:(\d+)',path.read_text()).group(1))
                payload=re.search(r'data:"([^"]*)"',path.read_text()).group(1)
                restored.append(decode(payload,length))
            self.assertEqual(restored,originals)
            self.assertIn('<title>水の出口</title>',output)
            self.assertIn('window.webtoonReady=',output)
            self.assertNotIn('application/x-webtoon-native-png" id=',output)

if __name__ == '__main__':unittest.main()
