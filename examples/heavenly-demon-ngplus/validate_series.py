#!/usr/bin/env python3
"""Inspect each finished reader at actual phone widths and export its full strip."""
import argparse,json,hashlib,os
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
BASE="http://127.0.0.1:8765/examples/heavenly-demon-ngplus"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--episode",type=int,action="append");args=ap.parse_args()
 numbers=args.episode or list(range(1,11))
 results=[]
 with sync_playwright() as p:
  executable=os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE') or ('/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None)
  browser=p.chromium.launch(executable_path=executable,headless=True,args=["--no-sandbox"])
  for n in numbers:
   folder=ROOT/f"episode-{n:02d}";out=folder/"validation";out.mkdir(exist_ok=True)
   record={"chapter":n,"viewports":[],"iOSDeviceChecked":False,"lettering":{"method":"vertical text in generated art" if n>1 else "existing HTML dialogue and generated holograms","fontSizeMeasuredInImage":False,"manualReviewWidths":[]}}
   for w,h in [(390,844),(360,800)]:
    page=browser.new_page(viewport={"width":w,"height":h},device_scale_factor=1)
    for version in ["index.html","reader.html"]:
     page.goto(f"{BASE}/episode-{n:02d}/{version}",wait_until="load")
     page.wait_for_function("Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)")
     page.evaluate("document.fonts.ready")
     m=page.evaluate("""()=>({width:innerWidth,height:innerHeight,pageWidth:document.documentElement.scrollWidth,length:document.documentElement.scrollHeight,images:document.images.length,imagesLoaded:Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0),pauses:Array.from(document.querySelectorAll('.pause[data-purpose]')).map(e=>({purpose:e.dataset.purpose,height:e.getBoundingClientRect().height})),brokenLinks:Array.from(document.querySelectorAll('a')).filter(a=>!a.getAttribute('href')).length})""")
     assert m["width"]==w and m["height"]==h
     assert m["pageWidth"]==w and m["imagesLoaded"]
     manifest=json.loads((folder/'episode.json').read_text())
     expected=32 if n==1 else len(manifest.get('readingOrder',manifest['artwork']))
     assert m["images"]==expected,m
     m["version"]=version
     if n==2:m["protectedRevealDistance"]=page.evaluate("document.querySelector('#scene-2').getBoundingClientRect().top-document.querySelector('#scene-4').getBoundingClientRect().bottom");assert m["protectedRevealDistance"]>h
     if n==1:m["protectedRevealDistance"]=page.evaluate("document.querySelector('#two-fingers').getBoundingClientRect().top-document.querySelector('#catch-cue').getBoundingClientRect().bottom");assert m["protectedRevealDistance"]>h
     m['sceneOrder']=page.locator('.scene').evaluate_all("els=>els.map(e=>e.id)")
     if n>1:
      expected_order=[p.get('id',f"scene-{p['scene']}") for p in manifest['readingOrder']]
      assert m['sceneOrder']==expected_order,(m['sceneOrder'],expected_order)
     if n==10:
      positions=page.locator('#scene-3-home,#scene-4,#scene-3-return').evaluate_all("els=>els.map(e=>({id:e.id,y:e.getBoundingClientRect().top+scrollY}))")
      assert [e['id'] for e in positions]==['scene-3-home','scene-4','scene-3-return'],positions
      m['homeBeforeReturn']=positions
     record["viewports"].append(m)
     if version=="index.html":
      if w==390:page.screenshot(path=str(folder/"webtoon-full-390.jpg"),full_page=True,type="jpeg",quality=92)
      page.screenshot(path=str(out/f"opening-{w}.jpg"),type="jpeg",quality=92)
      if n>1:
       for ident in m['sceneOrder']:
        # Render unaltered originals in their actual CSS display width.
        page.locator(f"#{ident}").screenshot(path=str(out/f"{ident}-{w}.png"))
        top=page.locator(f"#{ident}").evaluate("(e)=>e.getBoundingClientRect().top+scrollY")
        for fraction in [0,.3,.65]:
         height=page.locator(f"#{ident}").evaluate("(e)=>e.getBoundingClientRect().height")
         page.evaluate("y=>window.scrollTo(0,y)",top+height*fraction)
         assert page.evaluate("document.documentElement.scrollWidth")==w
      else:
       for ident in ['ordinary-class','ordinary-home','before-playing','rest-on-step','careful-hand','warm-water']:
        top=page.locator(f'#{ident}').evaluate('(e)=>e.getBoundingClientRect().top+scrollY')
        page.evaluate('y=>window.scrollTo(0,y)',top)
        page.screenshot(path=str(out/f'pacing-{ident}-{w}.jpg'),type='jpeg',quality=92)
      page.evaluate("window.scrollTo(0,document.documentElement.scrollHeight)")
      page.screenshot(path=str(out/f"ending-{w}.jpg"),type="jpeg",quality=92)
    page.close()
   for w in [390,360]:
    pair=[r for r in record["viewports"] if r["width"]==w]
    assert pair[0]["length"]==pair[1]["length"],pair
   if n>1:
    manifest=json.loads((folder/"manifest.json").read_text())
    record["originalBytesUnchanged"]=all(hashlib.sha256((folder/a["file"]).read_bytes()).hexdigest()==a["sha256"] for a in manifest["artwork"])
    assert record["originalBytesUnchanged"]
   (folder/"validation.json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
   results.append(record);print(f"Episode {n}: both widths, both reader forms, loaded images, no horizontal overflow")
  catalog=browser.new_page(viewport={"width":360,"height":800})
  catalog.goto(BASE+"/serial.html",wait_until="load")
  assert catalog.locator("li a").count()==10
  assert catalog.evaluate("document.documentElement.scrollWidth")==360
  for n in numbers:
   link=catalog.locator("li a").nth(n-1).get_attribute("href")
   assert link==f"episode-{n:02d}/index.html"
  catalog.screenshot(path=str(ROOT/"serial-mobile.jpg"),full_page=True,type="jpeg",quality=92)
  browser.close()
 saved=[]
 for n in range(1,11):
  path=ROOT/f"episode-{n:02d}/validation.json"
  if path.exists():
   record=json.loads(path.read_text())
   if "viewports" in record:saved.append(record)
 (ROOT/"mobile-checks.json").write_text(json.dumps({"episodes":saved,"catalogEntries":10,"nativeDeviceChecked":False},ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__":main()
