// Verify CSS windows and shared original payloads; export native phone scroll pixels.
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require(process.env.WEBTOON_PLAYWRIGHT_MODULE||'playwright');
const sharp=require(process.env.WEBTOON_SHARP_MODULE||require.resolve('sharp',{paths:[path.dirname(require.resolve(process.env.WEBTOON_PLAYWRIGHT_MODULE||'playwright'))]}));
const crypto=require('crypto'),base=path.resolve(__dirname,'../..');
async function exportScroll(page,width,height,scrollHeight,output,review){
 const tiles=[];
 for(let top=0;top<scrollHeight;top+=height){
  const scrollY=await page.evaluate(async y=>{scrollTo(0,y);await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));return window.scrollY;},top);
  const frame=await page.screenshot({animations:'disabled'}),tileHeight=Math.min(height,scrollHeight-top),offset=Math.round(top-scrollY);
  const input=await sharp(frame).extract({left:0,top:offset,width,height:tileHeight}).png().toBuffer();tiles.push({input,left:0,top,height:tileHeight});
 }
 await sharp({create:{width,height:scrollHeight,channels:4,background:'#fffaf0'}}).composite(tiles.map(({input,left,top})=>({input,left,top}))).png().toFile(output);
 const actual=await sharp(output).ensureAlpha().raw().toBuffer();for(const tile of tiles){const expected=await sharp(tile.input).ensureAlpha().raw().toBuffer();if(!actual.subarray(tile.top*width*4,(tile.top+tile.height)*width*4).equals(expected))throw Error('Native export mismatch');}
 for(let i=0;i<tiles.length;i+=4){const subset=tiles.slice(i,i+4);await sharp({create:{width:width*subset.length,height,channels:4,background:'#fffaf0'}}).composite(subset.map((t,j)=>({input:t.input,left:j*width,top:0}))).png().toFile(path.join(review,`scroll-${width}-${i/4}.png`));}
 return {method:'native phone viewport tiles',tileCount:tiles.length,pixelEquality:'passed_all_tiles'};
}
(async()=>{const browser=await chromium.launch({headless:true,executablePath:process.env.WEBTOON_CHROME||(process.platform==='darwin'&&fs.existsSync('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')?'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome':undefined)});try{
 for(const arg of process.argv.slice(2)){
  const n=Number(arg),dir=path.join(base,`episode-${String(n).padStart(2,'0')}`),m=JSON.parse(fs.readFileSync(path.join(dir,'manifest.json'))),review=path.join(dir,'review');fs.mkdirSync(review,{recursive:true});
  const result={episode:n,revision:m.revision,artworkTextReview:'pending',continuityReview:'pending',windowBoundaryReview:'pending',scrollPacingVisualReview:'pending',originalArtworkCount:m.sources.length,displayWindowCount:m.scenes.length,viewports:[]};
  for(const [width,height] of [[390,844],[360,800]]){
   const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});await page.goto(pathToFileURL(path.join(dir,'reader.html')).href);await page.evaluate(async()=>{await window.webtoonReady;await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));});
   const metrics=await page.evaluate(()=>({innerWidth,innerHeight,scrollWidth:document.documentElement.scrollWidth,scrollHeight:document.documentElement.scrollHeight,images:[...document.images].map(i=>({width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete&&i.naturalWidth>0})),windows:[...document.querySelectorAll('figure.scene')].map(e=>{const r=e.getBoundingClientRect(),img=e.querySelector('img').getBoundingClientRect();return{id:e.id,top:r.top+scrollY,height:r.height,width:r.width,imageOffset:img.top-r.top,pause:parseFloat(getComputedStyle(e).marginBottom)};})}));
   if(metrics.innerWidth!==width||metrics.innerHeight!==height||metrics.scrollWidth!==width||metrics.images.length!==m.scenes.length||!metrics.images.every(i=>i.loaded))throw Error(`Episode ${n}/${width}: wrong viewport or missing artwork`);
   for(let i=0;i<m.scenes.length;i++){const crop=m.scenes[i].crop,g=metrics.windows[i];if(Math.abs(g.height-crop.height/crop.width*width)>.06||Math.abs(g.imageOffset+crop.y/crop.width*width)>.06)throw Error('CSS window changes crop');}
   const hashes=await page.evaluate(async()=>{const out={};for(const img of document.images){if(out[img.dataset.artId])continue;const bytes=await(await fetch(img.src)).arrayBuffer(),hash=await crypto.subtle.digest('SHA-256',bytes);out[img.dataset.artId]=[...new Uint8Array(hash)].map(v=>v.toString(16).padStart(2,'0')).join('');}return out;});
   for(const s of m.sources)if(hashes[s.id]!==s.sha256)throw Error('Standalone payload changed original PNG');
   metrics.originalArtworkHashes=hashes;
   metrics.fullScrollExport=await exportScroll(page,width,height,metrics.scrollHeight,path.join(dir,`complete-${width}.png`),review);
   metrics.protectedIntervals=[];
   for(let i=0;i<m.scenes.length-1;i++){const s=m.scenes[i],g=metrics.windows[i],next=metrics.windows[i+1];if(s.pauseAt390>=800){const distance=next.top-(g.top+g.height);if(distance<height)throw Error('Protected response shown with preceding panel');metrics.protectedIntervals.push({cueWindow:s.id,answerWindow:m.scenes[i+1].id,distance,requiredViewportHeight:height});for(const [label,y] of [['cue',g.top],['pause',g.top+g.height+distance*.25],['answer',next.top-100]]){await page.evaluate(y=>scrollTo(0,y),y);await page.screenshot({path:path.join(review,`protected-${width}-${s.id}-${label}.png`)});}}}
   await page.goto(pathToFileURL(path.join(dir,'index.html')).href);await page.evaluate(async()=>Promise.all([...document.images].map(i=>i.decode())));const editable=await page.evaluate(()=>({width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,count:document.images.length,loaded:[...document.images].every(i=>i.complete&&i.naturalWidth>0)}));if(editable.width!==width||editable.height!==metrics.scrollHeight||editable.count!==m.scenes.length||!editable.loaded)throw Error('Editable reader differs');metrics.editableReaderMatches=true;result.viewports.push(metrics);await page.close();
  }
  fs.writeFileSync(path.join(dir,'validation.json'),JSON.stringify(result,null,2)+'\n');console.log(`Episode ${n}: ${m.sources.length} originals / ${m.scenes.length} windows, exact bytes, 390×844 + 360×800, native captures. Visual checks pending.`);
 }
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1});
