"""Record an explicitly completed native 360/390 px visual review."""
import argparse
import hashlib
import json
from pathlib import Path

STATE = Path(__file__).resolve().parent
REPO = STATE.parents[3]

def mark(episode):
    directory = REPO / f'examples/zero-break/episode-{episode:02d}'
    proof_path = directory / 'raster-export-validation.json'
    proof = json.loads(proof_path.read_text())
    manifest = json.loads((directory / 'manifest.json').read_text())
    proof['edition'] = manifest.get('remakeEdition', manifest['version'])
    assert {e['width'] for e in proof['exports']} == {360, 390}
    boards = sorted((directory / 'review').glob('v6-contact-*.png'))
    expected = 2 * ((len(manifest['shots']) + 3) // 4)
    assert len(boards) == expected
    reviewed = [dict(path=str(p.relative_to(REPO)), sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in boards]
    for shot in manifest['shots']:
        path = REPO / shot['remakeRevisionRecord']
        record = json.loads(path.read_text())
        assert hashlib.sha256((directory / 'art' / shot['file']).read_bytes()).hexdigest() == record['sha256']
        record['mobileImageReview'] = dict(status='passed', widths=[360,390], method='human visual review of native raster contact boards; no browser', artifacts=reviewed)
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    proof['visualReview'] = dict(status='passed', widths=[360,390], method='native raster contact boards and sequence windows', artifacts=reviewed)
    proof_path.write_text(json.dumps(proof, ensure_ascii=False, indent=2)+'\n')
    validation_path = directory / 'validation.json'
    validation = json.loads(validation_path.read_text())
    assert validation['readerSourceSha256'] == hashlib.sha256((directory / 'index.html').read_bytes()).hexdigest()
    validation['visualReview'] = proof['visualReview']
    validation_path.write_text(json.dumps(validation, ensure_ascii=False, indent=2)+'\n')
    print(f'Episode {episode}: native mobile visual review recorded; browser remains pending')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('episode', type=int)
    args = parser.parse_args()
    mark(args.episode)
