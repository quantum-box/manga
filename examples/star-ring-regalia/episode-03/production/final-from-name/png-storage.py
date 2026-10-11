"""Lossless offline storage encoding; no artwork pixels or originals are edited."""
import struct
import zlib

def chunks(raw):
    assert raw[:8] == b'\x89PNG\r\n\x1a\n'
    pos = 8
    result = []
    while pos < len(raw):
        length = struct.unpack('>I', raw[pos:pos + 4])[0]
        kind = raw[pos + 4:pos + 8]
        data = raw[pos + 8:pos + 8 + length]
        crc = struct.unpack('>I', raw[pos + 8 + length:pos + 12 + length])[0]
        assert zlib.crc32(kind + data) == crc
        result.append((kind, data))
        pos += length + 12
    assert pos == len(raw)
    return result

def pixel_stream(raw):
    return zlib.decompress(b''.join(data for kind, data in chunks(raw) if kind == b'IDAT'))

def offline_encoding(raw):
    original = chunks(raw)
    compressed = zlib.compress(pixel_stream(raw), 9)
    output = bytearray(raw[:8])
    wrote_idat = False
    for kind, data in original:
        if kind == b'IDAT':
            if wrote_idat:
                continue
            data = compressed
            wrote_idat = True
        output += struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    encoded = bytes(output) if len(output) < len(raw) else raw
    # Identical filtered pixels and every non-IDAT chunk ensure exact decoded art.
    assert pixel_stream(encoded) == pixel_stream(raw)
    assert [(k, d) for k, d in chunks(encoded) if k != b'IDAT'] == [(k, d) for k, d in original if k != b'IDAT']
    return encoded
