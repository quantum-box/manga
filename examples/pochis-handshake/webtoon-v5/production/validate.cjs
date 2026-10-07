// NODE_PATH=<bundled node_modules> node production/validate.cjs
const fs=require('fs'),path=require('path'),assert=require('assert'),crypto=require('crypto');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
const base=path.resolve(__dirname,'..');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_EXECUTABLE_PATH?{executablePath:process.env.CHROMIUM_EXECUTABLE_PATH}:{})});
 try {
  const plan=JSON.parse(fs.readFileSync(path.join(__dirname,'plan.json')));
  const manual=JSON.parse(fs.readFileSync(path.join(__dirname,'visual-review.json')));
  const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
  for(const e of plan){
   if(process.argv.length>2&&!process.argv.slice(2).map(Number).includes(e.number))continue;
   const folder=path.join(base,'episode-'+String(e.number).padStart(2,'0'));
   if(!fs.existsSync(path.join(folder,'index.html'))) continue;
   const scenes=JSON.parse(fs.readFileSync(path.join(folder,'scenes.json')));
   const portable=fs.readFileSync(path.join(folder,'reader.html'),'utf8');
   const embedded=[...portable.matchAll(/<img\b[^>]*\bsrc="data:image\/[^;]+;base64,([^"]+)"/g)].map(m=>Buffer.from(m[1],'base64'));
   const expectedHashes=scenes.flatMap(s=>s.scroll_windows.map(()=>s.sha256));
   assert.equal(embedded.length,expectedHashes.length);
   embedded.forEach((bytes,i)=>assert.equal(sha(bytes),expectedHashes[i]));
   for(let i=0;i<10;i++){
    assert.equal(sha(fs.readFileSync(path.join(folder,scenes[i].raster_original))),scenes[i].original_sha256);
    assert.equal(sha(fs.readFileSync(path.join(folder,scenes[i].filename))),scenes[i].sha256);
   }
   const views=[];
   for(const [width,height] of [[390,844],[360,800]]){
    const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
    await page.goto(pathToFileURL(path.join(folder,'index.html')).href);
    await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));});
    const data=await page.evaluate(()=>{
     const images=[...document.images].map(i=>({src:i.getAttribute('src'),complete:i.complete,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight,top:i.getBoundingClientRect().top+scrollY,bottom:i.getBoundingClientRect().bottom+scrollY,displayWidth:i.width}));
     const figures=[...document.querySelectorAll('figure')].map(f=>({id:f.id,top:f.getBoundingClientRect().top+scrollY,bottom:f.getBoundingClientRect().bottom+scrollY,marginAfter:parseFloat(getComputedStyle(f).marginBottom),windows:[...f.querySelectorAll('.panel-window')].map(w=>({panels:w.dataset.panels,sourceRegion:w.dataset.sourceRegion,top:w.getBoundingClientRect().top+scrollY,height:w.getBoundingClientRect().height,width:w.getBoundingClientRect().width})),pauses:[...f.querySelectorAll('.pause')].map(p=>({purpose:p.dataset.purpose,height:p.getBoundingClientRect().height}))}));
     return {innerWidth,innerHeight,scrollWidth:document.documentElement.scrollWidth,scrollHeight:document.documentElement.scrollHeight,images,figures,links:[...document.querySelectorAll('a')].map(a=>a.getAttribute('href'))};
    });
    assert.equal(data.innerWidth,width);assert.equal(data.innerHeight,height);assert.equal(data.scrollWidth,width);assert.equal(data.images.length,expectedHashes.length);assert(data.images.every(i=>i.complete&&i.naturalWidth>0));assert.equal(new Set(data.images.map(i=>i.src)).size,10);
    for(let i=0;i<10;i++){
     const f=data.figures[i],s=scenes[i];
     assert(Math.abs(f.marginAfter-s.gap_after*width/360)<0.1);
     assert.equal(f.pauses.length,s.internal_pauses.length);
     f.pauses.forEach((p,j)=>assert(Math.abs(p.height-s.internal_pauses[j].pause*width/360)<0.1));
    }
    for(const href of data.links)assert(fs.existsSync(path.resolve(folder,href)));
    await page.screenshot({path:path.join(folder,'webtoon-'+width+'.jpg'),fullPage:true,type:'jpeg',quality:92});
    if(width===360){
     const mobile=path.join(folder,'review');fs.mkdirSync(mobile,{recursive:true});
     for(let i=0;i<10;i++)await page.locator('figure').nth(i).screenshot({path:path.join(mobile,'scene-'+String(i+1).padStart(2,'0')+'-360.png')});
    }
    views.push(data);await page.close();
   }
   const review=manual.episodes.find(r=>r.episode===e.number);
   assert(review.all360pxStripsRead);
   fs.writeFileSync(path.join(folder,'validation.json'),JSON.stringify({episode:e.number,views,letteringCheck:review,letteringSize:manual.lettering,gaps:scenes.map(s=>({scene:s.id,referenceWidth:360,referencePx:s.gap_after,purpose:s.pacing,internal:s.internal_pauses})),uniqueArtwork:10,displayWindows:expectedHashes.length,standaloneArtworkBytesMatch:true,physicalDeviceTest:false},null,2)+'\n');
   console.log('Episode',e.number,views.map(v=>v.innerWidth+'px / '+v.scrollHeight+'px').join(', '));
  }
  if(process.argv.length===2){
   const global=[];
   const protectedPairs=[['child','episode-01-scene-08','episode-01-scene-10'],['wolf','episode-04-scene-10','episode-05-scene-01'],['demon-king','episode-06-scene-10','episode-07-scene-01']];
   const reviewDir=path.join(base,'production','review');fs.mkdirSync(reviewDir,{recursive:true});
   for(const [width,height] of [[390,844],[360,800]]){
    const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
    await page.goto(pathToFileURL(path.join(base,'all.html')).href);
    await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));});
    const data=await page.evaluate(()=>({innerWidth,innerHeight,scrollWidth:document.documentElement.scrollWidth,scrollHeight:document.documentElement.scrollHeight,displayWindows:document.images.length,images:[...document.querySelectorAll('figure')].map(f=>({id:f.id,top:f.getBoundingClientRect().top+scrollY,bottom:f.getBoundingClientRect().bottom+scrollY,loaded:[...f.querySelectorAll('img')].every(i=>i.complete&&i.naturalWidth>0)}))}));
    assert.equal(data.innerWidth,width);assert.equal(data.scrollWidth,width);assert.equal(data.images.length,100);assert(data.images.every(i=>i.loaded));
    data.protectedReveals=[];
    for(const [name,questionID,answerID] of protectedPairs){
     const question=data.images.find(i=>i.id===questionID),answer=data.images.find(i=>i.id===answerID);
     const distance=answer.top-question.bottom;assert(distance>=height, name+' reveal is visible too early');
     data.protectedReveals.push({name,questionID,answerID,distanceCssPx:distance,viewportHeight:height});
     await page.evaluate(y=>scrollTo(0,y),question.bottom-200);
     await page.screenshot({path:path.join(reviewDir,name+'-'+width+'.png')});
    }
    await page.goto(pathToFileURL(path.join(base,'chapters.html')).href);
    assert.equal(await page.locator('.chapter-card').count(),10);
    for(const number of [1,10]){
     await page.goto(pathToFileURL(path.join(base,'episode-'+String(number).padStart(2,'0'),'reader.html')).href);
     await page.evaluate(async()=>Promise.all([...document.images].map(i=>i.decode())));
     const episodeScenes=JSON.parse(fs.readFileSync(path.join(base,'episode-'+String(number).padStart(2,'0'),'scenes.json')));
     assert.equal(await page.locator('img').count(),episodeScenes.reduce((n,s)=>n+s.scroll_windows.length,0));
    }
    global.push(data);await page.close();
   }
   fs.writeFileSync(path.join(base,'production','book-validation.json'),JSON.stringify({views:global,chapterCards:10,standaloneBrowsers:[1,10],visualReview:manual,physicalDeviceTest:false},null,2)+'\n');
   console.log('PASS:',global[0].displayWindows,'display windows from 100 artworks, 10 chapters, 3 protected reveals, standalone artwork byte parity');
  }
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
