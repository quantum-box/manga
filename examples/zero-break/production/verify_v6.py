"""Verify adopted v6 artifacts without starting an HTML renderer or browser."""
import base64,hashlib,json,re,zipfile
from pathlib import Path
from struct import unpack
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
STATE=ROOT/'production/feedback-v6'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def directory(n):return ROOT/('v5' if n==1 else f'episode-{n:02d}')
totals=dict(baseline_artworks=0,reader_images=0,panels=0,adopted_revision_records=0,scripts=0)
chapters=[]
sound_revisions=0
inserted_artworks=0
inserted_panels=0
for n in range(1,11):
 d=directory(n);m=load(d/'manifest.json');baseline=load(STATE/'baseline'/f'episode-{n:02d}.json')
 assert m['version']=='context-dialogue-v6'
 covered=set()
 for s in m['shots']:covered.update(s.get('replaces',[s['id']]))
 assert covered=={s['id'] for s in baseline['shots']},n
 for s in baseline['shots']:
  p=d/'art'/(s['file']+('.png' if n==1 else ''))
  assert sha(p)==s['baseline_sha256'],p
  totals['baseline_artworks']+=1
 index=(d/'index.html').read_text()
 local=re.findall(r'<img[^>]+src="art/([^"]+)"',index)
 assert local==[s['file'] for s in m['shots']]
 embedded=re.finditer(r'data:image/png;base64,([A-Za-z0-9+/=]+)',(d/'reader.html').read_text())
 count=0
 for s in m['shots']:
  match=next(embedded)
  raw=base64.b64decode(match.group(1),validate=True)
  assert raw==(d/'art'/s['file']).read_bytes(),s['id']
  record_path=STATE/'records'/(s['id']+'.json')
  if record_path.exists():
   r=load(record_path);assert r['sha256']==sha(d/'art'/r['file'])
   assert r['panels']==s['panels']
   if not s.get('revisionRecord'):
    assert r['file']==s['file'] and r['prompt']==s['prompt']
   for ref in r['references']:assert sha(REPO/ref['path'])==ref['sha256']
   for old in r.get('repair_history',[]):
    assert sha(d/'art'/old['file'])==old['sha256']
   if r.get('repairBefore'):
    old=r['repairBefore'];assert sha(d/'art'/old['file'])==old['sha256']
   assert (record_path.parent/r['visual_review']['chapter_validation']).is_file()
   assert r['prompt'] and r['method'];totals['adopted_revision_records']+=1
  if s.get('revisionRecord'):
   r=load(REPO/s['revisionRecord'])
   assert r['file']==s['file'] and r['sha256']==sha(d/'art'/s['file'])
   assert r['prompt']==s['prompt'] and r['sounds']==s['sounds']
   assert r['preservedLines']==s['lines'] and r['panels']==s.get('panels',[])
   assert r['preservedVisibleText']==s.get('visible_text',[])
   before=r['repairBefore'];assert sha(d/'art'/before['file'])==before['sha256']
   for ref in r['references']:assert sha(REPO/ref['path'])==ref['sha256']
   assert r['method'] and r['prompt']
   sound_revisions+=1
  if s.get('insertionRecord'):
   r=load(REPO/s['insertionRecord'])
   assert r['shot']['id']==s['id'] and r['shot']['file']==s['file']
   assert r['sha256']==sha(d/'art'/s['file']) and r['prompt']==s['prompt']
   for key in ('lines','panels','sounds','visible_text'):
    assert r['shot'].get(key,[])==s.get(key,[])
   for ref in r['references']:assert sha(REPO/ref['path'])==ref['sha256']
   if r.get('repairBefore'):
    before=r['repairBefore'];assert sha(d/'art'/before['file'])==before['sha256']
   assert s['replaces']==[] and r['method'] and r['prompt']
   inserted_artworks+=1;inserted_panels+=len(s['panels'])
  count+=1
 assert next(embedded,None) is None
 assert count==len(m['shots'])
 with zipfile.ZipFile(d/'reader.zip') as z:
  assert z.namelist()==['reader.html'] and z.testzip() is None
  assert z.read('reader.html')==(d/'reader.html').read_bytes()
 delivery=load(d/'delivery-validation.json')
 assert delivery['readerSha256']==sha(d/'reader.html') and delivery['archiveSha256']==sha(d/'reader.zip')
 raster=load(d/'raster-export-validation.json')
 assert raster['browserPixelsCompared'] is False
 assert raster['sourceHashes']==[dict(id=s['id'],file=s['file'],sha256=sha(d/'art'/s['file'])) for s in m['shots']]
 for export in raster['exports']:
  assert export['width'] in (360,390) and export['sha256']==sha(d/export['file'])
  w,h=unpack('>II',(d/export['file']).read_bytes()[16:24]);assert (w,h)==(export['width'],export['height'])
  assert len(export['positions'])==count
  for pos in export['positions']:assert 0<=pos['x'] and pos['x']+pos['width']<=w+.001 and pos['y']+pos['height']<=h
 panel_count=sum(len(s.get('panels',[s])) for s in m['shots']);assert panel_count==m['panel_count']
 ios=REPO/'ios/Manga/Webtoons/zero-break'/f'episode-{n:02d}'
 assert (ios/'index.html').read_bytes()==(d/'index.html').read_bytes()
 for s in m['shots']:assert (ios/'art'/s['file']).read_bytes()==(d/'art'/s['file']).read_bytes()
 totals['reader_images']+=count;totals['panels']+=panel_count
 chapters.append(dict(episode=n,assets=count,panels=panel_count,source_sha256=sha(d/'index.html'),browser_review='pending'))
scripts=load(ROOT/'series/episodes.json');assert len(scripts)==50
for n,row in enumerate(scripts,1):
 assert row['episode']==n and (ROOT/'series'/row['script']).is_file()
 assert row['panel_count']==sum(len(g['panels']) for g in row['panel_staging'])
 if n<=10:assert row['panel_count']==chapters[n-1]['panels']
 else:
  assert row['art_status']=='not_started'
  quote_text=''.join(re.findall('「([^」]*)」',''.join(row['scenes'])))
  staged=''.join(p['line']['text'] for g in row['panel_staging'] for p in g['panels'] if p.get('line'))
  assert quote_text==staged,n
 totals['scripts']+=1
assert totals==dict(baseline_artworks=196,reader_images=196+inserted_artworks,panels=317+inserted_panels,adopted_revision_records=57,scripts=50),totals
report=dict(edition='context-dialogue-v6',status='passed_artifact_checks',totals=totals,chapters=chapters,
 sound_effect_revision_records=sound_revisions,
 inserted_artworks=inserted_artworks,inserted_panels=inserted_panels,
 checks=['all prior source PNG hashes preserved','every baseline scene represented','actual revision prompts, references and repaired originals preserved','standalone embedded PNGs match raw source bytes','ZIP CRC and extracted HTML match','native export hashes, width and source geometry','iOS HTML and PNG bytes match adopted sources','all fifty scripts staged; existing quoted text preserved for 11-50'],
 browser_review='pending; native exports do not prove browser layout',physical_device_review='not_run')
(STATE/'artifact-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(totals))
