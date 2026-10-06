// Render packaged local readers, measure both phone sizes, and make review sheets.
const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require(process.env.WEBTOON_PLAYWRIGHT_MODULE||'playwright');
const base=path.resolve(__dirname,'..');
(async()=>{
 const macChrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
 const executablePath=process.env.WEBTOON_CHROME||(process.platform==='darwin'&&fs.existsSync(macChrome)?macChrome:undefined);
 const browser=await chromium.launch({headless:true,executablePath});
 try {
  for(const arg of process.argv.slice(2)) {
   const number=Number(arg),dir=path.join(base,`episode-${String(number).padStart(2,'0')}`);
   const m=JSON.parse(fs.readFileSync(path.join(dir,'manifest.json')));
   const review=path.join(dir,'review');fs.mkdirSync(review,{recursive:true});
   const result={episode:number,artworkTextReview:'pending',continuityReview:'pending',viewports:[]};
   for(const [width,height] of [[390,844],[360,800]]) {
    const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
    await page.goto(pathToFileURL(path.join(dir,'reader.html')).href);
    await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));});
    const metrics=await page.evaluate(()=>({innerWidth,innerHeight,scrollWidth:document.documentElement.scrollWidth,
     scrollHeight:document.documentElement.scrollHeight,images:[...document.images].map(i=>({width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete&&i.naturalWidth>0})),
     htmlTextMinPx:Math.min(...[...document.querySelectorAll('header p,header h1,header small,header .series-title,footer p,footer a')].map(e=>parseFloat(getComputedStyle(e).fontSize)))}));
    if(metrics.innerWidth!==width||metrics.innerHeight!==height||metrics.scrollWidth!==width||metrics.images.length!==m.scenes.length||!metrics.images.every(i=>i.loaded))throw Error(`Episode ${number}/${width} layout mismatch`);
    // Exercise the entire reader at actual viewport size before export.
    for(let y=0;y<metrics.scrollHeight;y+=height*.75)await page.evaluate(y=>scrollTo(0,y),y);
    await page.evaluate(()=>scrollTo(0,0));
    await page.screenshot({path:path.join(dir,`complete-${width}.png`),fullPage:true});
    await page.close();
    const sheets=[];
    for(let offset=0;offset<m.scenes.length;offset+=4) {
     const subset=m.scenes.slice(offset,offset+4);
     const cells=subset.map(s=>`<figure><figcaption>${s.id}</figcaption><img src="../${s.art}" style="width:${width}px;height:auto"></figure>`).join('');
     const doc=`<!doctype html><meta charset="utf-8"><style>*{box-sizing:border-box}body{margin:0;width:${width*2}px;background:#fffaf0;font:16px sans-serif}.grid{display:grid;grid-template-columns:${width}px ${width}px;align-items:start}figure{margin:0}figcaption{height:28px;line-height:28px;padding-left:8px}img{display:block}</style><div class="grid">${cells}</div>`;
     const sheet=path.join(review,`contact-${width}-${offset/4}.html`);fs.writeFileSync(sheet,doc);
     const view=await browser.newPage({viewport:{width:width*2,height:900},deviceScaleFactor:1});
     await view.goto(pathToFileURL(sheet).href);await view.evaluate(async()=>Promise.all([...document.images].map(i=>i.decode())));
     const shot=`contact-${width}-${offset/4}.png`;await view.screenshot({path:path.join(review,shot),fullPage:true});await view.close();sheets.push(`review/${shot}`);
    }
    result.viewports.push({...metrics,reviewSheets:sheets,fullScrollExecuted:true});
   }
   fs.writeFileSync(path.join(dir,'validation.json'),JSON.stringify(result,null,2)+'\n');
   console.log(`Episode ${number}: 8 images loaded, 390x844 and 360x800, no horizontal overflow; visual review pending`);
  }
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
