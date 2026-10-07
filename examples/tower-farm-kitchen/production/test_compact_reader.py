import base64
from html.parser import HTMLParser
import unittest

from compact_reader import CompactReader, decode, encode

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

if __name__ == '__main__':unittest.main()
