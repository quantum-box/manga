"""Record scope, real CSS measurements and immutable generated-asset provenance."""
import hashlib
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = Path.home() / '.codex/skills/webtoon'
def read(path):
    return json.loads(path.read_text())
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def write(name, data):
    (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

panels = read(ROOT / 'plan-notes.json')['panels']
plan = read(ROOT / 'plan.json')
ids = [p['id'] for p in panels]
excluded = ['p005', 'p006', 'p007', 'p016', 'p017', 'p025', 'p028',
            'p031', 'p033', 'p041', 'p087']
effective = [i for i in ids if i not in excluded]
assert ids == [f'p{i:03}' for i in range(1, 97)]
assert [b['id'] for b in plan['beats'] if b['type'] == 'panel'] == ids
assert len(effective) == 85
assets = []
for image in sorted((ROOT / 'rough').glob('*.png')):
    meta_path = image.with_suffix('.generation.json')
    meta = read(meta_path)
    source = Path(meta.get('sourcePath') or meta['sourcepath'])
    copied_hash = digest(image)
    cache_hash = digest(source)
    assert copied_hash == cache_hash, image
    raw = image.read_bytes()
    assets.append(dict(file=str(image.relative_to(ROOT)), sourcePath=str(source),
        sha256=copied_hash, sourceSha256=cache_hash, bytesIdentical=True,
        imageSize=list(struct.unpack('>II', raw[16:24])),
        metadata=str(meta_path.relative_to(ROOT))))
write('generation.json', dict(tool='built-in image_gen', state='name, user adoption pending',
    reference='examples/star-ring-regalia/reference/cast.png',
    referenceRole='Character identity and costume; source cells reorganized in authored HTML',
    assets=assets, manualImageEditing=False))

measurements = []
for width in [390, 360]:
    layout = read(ROOT / f'review/layout-{width}.json')
    windows = read(ROOT / f'review/windows-{width}.json')
    assert len(layout['panels']) == 96
    assert layout['imageFailures'] == 0
    assert not layout['copyOverflow'] and not layout['horizontalCopyOverflow']
    assert layout['documentWidth'] == width
    assert float(layout['fontSize'].rstrip('px')) >= 19
    measurements.append(dict(widthCssPx=width, heightCssPx=layout['viewport']['height'],
        dpr=layout['viewport']['dpr'], bodyHeightCssPx=layout['bodyHeightCssPx'],
        pureGapHeightCssPx=layout['pureGapHeightCssPx'], contentHeightCssPx=layout['contentHeightCssPx'],
        displayCuts=96, effectivePanels=len(effective), screenshotCount=len(windows),
        copyOverflow=0, horizontalCopyOverflow=0, imageFailures=0,
        dialogueFontSize=layout['fontSize'],
        source=f'review/layout-{width}.json', windows=f'review/windows-{width}.json',
        internalImageBlank=layout['imageInternalBlank']))
base = measurements[0]
assert 34000 <= base['bodyHeightCssPx'] <= 60000
assert base['contentHeightCssPx'] >= 24000
assert 80 <= len(effective) <= 120
positions = {p['id']: p for p in read(ROOT / 'review/layout-390.json')['panels']}
assert positions['p024']['y'] < positions['p026']['y'] < positions['p027']['y']
assert positions['p083']['y'] < positions['p085']['y'] < positions['p092']['y']
write('validation.json', dict(date='2026-10-10', requestedEpisodes=[1, 2, 3],
    episode=1, scope='Complete episode name; final art and publication await adoption',
    state='ready for user composition review',
    skill=dict(path=str(SKILL / 'SKILL.md'), sha256=digest(SKILL / 'SKILL.md')),
    measurements=measurements, effectivePanelIds=effective, excludedPanelIds=excluded,
    volumeVerdict='pass', storyVerdict='pass', paddingVerdict='pass',
    effectiveMethod='New action, understanding or reaction; exclude eleven transition/support cuts and all voice, sound and blank beats. p053 now establishes the frayed rope that causes the incident.',
    storyEvidence=['Reserve disappointment and own purchase precede voluntary connection',
        'Freeing the cart jolts its cargo; a visibly frayed rope snaps; Koh catches a falling medicine chest and Lize helps haul it to safety; relief leads into names and the later medicine request',
        'Water, device and willing spirit are learned through visible work and practice',
        'One medicine parcel: Sena at p079-p081; Koh at p082-p084; handoff at p085; Lize afterward',
        '20:50 triggers an honest handoff, safe logout and Japan 21:00 return'],
    paddingEvidence='Pure whitespace counted independently; repeated/support moments excluded conservatively',
    checks=dict(native390=True, native360=True, device=False, userAdoption=False,
        finishedArtwork=False, pullRequest=False, merged=False, uploaded=False,
        publicReader=False, rustChecksRun=False),
    files=dict(html='index.html', storyboard='storyboard.md', visualAudit='visual-audit-final.md',
        generation='generation.json'),
    htmlSha256=digest(ROOT / 'index.html')))
print(json.dumps(dict(state='ready for review', effectivePanels=len(effective),
    measurements=measurements, sourceCopiesVerified=len(assets)), ensure_ascii=False))
