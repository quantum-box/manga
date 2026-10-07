#!/usr/bin/env python3
"""Verify adopted raster bytes, offline packaging and actual phone scroll geometry."""
import argparse, base64, functools, hashlib, json, threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
P = ROOT / 'production'
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def save(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def lettering_record(d, manifest, n):
    samples = {5: [('04', '私', [194,48,220,74])], 6: [('06', '禁', [272,40,301,70])]}
    measured = []
    for ident, glyph, box in samples.get(n, []):
        file = f'validation/beat-{ident}-1-360.png'
        with Image.open(d/file) as im:
            ink = im.convert('L').crop(box).point(lambda v: 255 if v < 100 else 0)
            b = ink.getbbox()
        measured.append({'file':file, 'glyph':glyph, 'crop':box, 'threshold':100,
                         'inkWidthPx':b[2]-b[0], 'inkHeightPx':b[3]-b[1]})
    return {'referenceSizeCssPx':[19,20], 'reviewWidthCssPx':360,
            'sourceWidthsPx':sorted({a['width'] for a in manifest['artwork']}),
            'scaleAt360':sorted({round(360/a['width'],5) for a in manifest['artwork']}),
            'measuredInkSamples':measured,
            'note':'Ink bounds are not a CSS font size or a minimum for every glyph. All reading units were visually reviewed; see production/mobile-review.md.'}
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*a): pass

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--episode',type=int,action='append')
    args=ap.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(QuietHandler,directory=str(REPO)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url=f'http://127.0.0.1:{server.server_port}/examples/heavenly-demon-ngplus'
    summaries=[]
    runs=read(P/'generation.json')
    pairs=read(P/'protected.json')
    adopted_chapters = {int(n) for n in read(P/'adoption.json')}
    for episode in read(P/'scripts.json')['episodes']:
        for asset in episode['assets']:
            for line in asset[6]:
                assert not any(c in line[1]+line[2] for c in '、。'), (episode['number'],asset[0],line)
    for run in runs:
        adopted=ROOT/run['adopted']
        assert adopted.is_file() and digest(adopted)==run['sha256'],adopted
        assert all((ROOT/ref).is_file() for ref in run.get('references',[])),run['adopted']
    with sync_playwright() as pw:
        browser=pw.chromium.launch()
        for n in range(1,11):
            if n not in adopted_chapters: continue
            if args.episode and n not in args.episode: continue
            d=ROOT/f'episode-{n:02d}'
            m=read(d/'manifest.json')
            originals={}
            for a in m['artwork']:
                f=d/a['file']
                assert digest(f)==a['sha256'],f
                matching=[r for r in runs if r['episode']==n and r['id']==a['id'] and (ROOT/r['adopted'] if not Path(r['adopted']).is_absolute() else Path(r['adopted']))==f]
                assert matching,(n,a['id'])
                r=matching[-1]
                source=Path(r.get('edit',{}).get('source',r['original']))
                if source.is_file(): assert f.read_bytes()==source.read_bytes(),f
                assert not r.get('sha256') or r['sha256']==digest(f)
                originals[a['id']]=f
            out=d/'validation'
            out.mkdir(exist_ok=True)
            checks=[]
            for width,height in [(390,844),(360,800)]:
                context=browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1)
                for file in ['index.html','reader.html']:
                    page=context.new_page()
                    page.goto(f'{url}/episode-{n:02d}/{file}',wait_until='networkidle')
                    page.evaluate("async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()))}")
                    geo=page.evaluate("""()=>({width:innerWidth,height:innerHeight,documentWidth:document.documentElement.scrollWidth,length:document.documentElement.scrollHeight,figures:[...document.querySelectorAll('figure.scene')].map(f=>({id:f.id,top:f.getBoundingClientRect().top+scrollY,bottom:f.getBoundingClientRect().bottom+scrollY,width:f.getBoundingClientRect().width,loaded:f.querySelector('img').complete&&f.querySelector('img').naturalWidth>0,src:f.querySelector('img').getAttribute('src'),window:f.dataset.window}))})""")
                    assert (geo['width'],geo['height'])==(width,height)
                    assert geo['documentWidth']==width,(n,file,geo)
                    assert [x['id'] for x in geo['figures']]==[x['id'] for x in m['readingOrder']]
                    assert all(x['loaded'] and abs(x['width']-width)<.1 for x in geo['figures'])
                    for fig,order in zip(geo['figures'],m['readingOrder']):
                        if file=='reader.html':
                            assert hashlib.sha256(base64.b64decode(fig['src'].split(',',1)[1])).hexdigest()==digest(originals[order['asset']])
                        else: assert (d/fig['src']).read_bytes()==originals[order['asset']].read_bytes()
                        fig.pop('src')
                    bounds={f['id']:f for f in geo['figures']}
                    protected=[]
                    for pair in pairs.get(str(n),[]):
                        cue=bounds[pair['cue']['id']]
                        reveal=bounds[pair['reveal']['id']]
                        cue_y=cue['top']+(cue['bottom']-cue['top'])*pair['cue']['fraction']
                        reveal_y=reveal['top']+(reveal['bottom']-reveal['top'])*pair['reveal']['fraction']
                        distance=reveal_y-cue_y
                        assert distance>=height,(n,width,pair['name'],round(distance,2),height)
                        protected.append({'name':pair['name'],'cueEndY':round(cue_y,2),'revealStartY':round(reveal_y,2),'distance':round(distance,2),'viewportHeight':height,'cannotCoappear':True})
                        if file=='index.html':
                            # Consecutive real viewport captures, including all-white waiting screens.
                            y=max(0,cue_y-height*.65)
                            page.evaluate('(y)=>scrollTo(0,y)',y)
                            steps=[]
                            for k in range(4):
                                at=page.evaluate('scrollY')
                                name=f"pair-{pair['key']}-{width}-{k+1}.jpg"
                                page.screenshot(path=str(out/name),type='jpeg',quality=90)
                                steps.append({'file':'validation/'+name,'scrollY':at})
                                page.keyboard.press('PageDown')
                                page.wait_for_timeout(200)
                            protected[-1]['screens']=steps
                    if file=='index.html':
                        page.evaluate('scrollTo(0,0)')
                        page.screenshot(path=str(d/'webtoon-full-390.jpg' if width==390 else out/'full-360.jpg'),full_page=True,type='jpeg',quality=90)
                        page.screenshot(path=str(out/f'opening-{width}.jpg'),type='jpeg',quality=90)
                        for fig in geo['figures']:
                            if width==360:
                                page.locator('#'+fig['id']).screenshot(path=str(out/f"{fig['id']}-360.png"))
                        page.evaluate('scrollTo(0,document.documentElement.scrollHeight)')
                        page.screenshot(path=str(out/f'ending-{width}.jpg'),type='jpeg',quality=90)
                    else:
                        page.evaluate('scrollTo(0,0)')
                        page.screenshot(path=str(out/f'offline-opening-{width}.jpg'),type='jpeg',quality=90)
                    checks.append({'file':file,'viewport':[width,height],'dom':geo,'protected':protected,'imageBytesMatch':True})
                    page.close()
                context.close()
            v={'revision':m['revision'],'chapter':n,'originals':len(originals),'allAdoptedRasterBytesUnmodified':True,'browserChecks':checks,'manualReview':'See production/mobile-review.md; mechanical checks do not prove art or text quality.','iosPhysicalDevice':'not tested'}
            v['rasterLettering'] = lettering_record(d,m,n)
            save(d/'validation.json',v)
            summaries.append({'chapter':n,'originals':len(originals),'readingUnits':len(m['readingOrder']),'checks':len(checks)})
            print(f'Validated {n}: '+str(summaries[-1]),flush=True)
        browser.close()
    server.shutdown()
    summaries=[]
    for n in range(1,11):
        if n not in adopted_chapters: continue
        record=read(ROOT/f'episode-{n:02d}/validation.json')
        manifest=read(ROOT/f'episode-{n:02d}/manifest.json')
        assert record['revision']==manifest['revision']
        summaries.append({'chapter':n,'originals':record['originals'],'readingUnits':len(manifest['readingOrder']),'checks':len(record['browserChecks'])})
    save(ROOT/'mobile-checks.json',{'revision':'full-rebuild-2026-10-07','episodes':summaries,'viewports':[[390,844],[360,800]],'physicalDevice':'not tested'})

if __name__=='__main__': main()
