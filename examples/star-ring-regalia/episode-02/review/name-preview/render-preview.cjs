const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require('playwright');
const root=process.argv[2]||__dirname;
(async()=>{const browser=await chromium.launch({headless:true});const all=[];
try{for(const [width,height] of [[390,844],[360,800]]){
const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
await page.goto(pathToFileURL(path.join(root,'index.html')).href);
await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));});
const metrics=await page.evaluate(()=>{const flow=document.querySelector('#preview-flow');const rect=flow.getBoundingClientRect();const gaps=[...flow.querySelectorAll('.pause')].map(e=>({id:e.dataset.beatId,top:e.getBoundingClientRect().top+scrollY,height:e.getBoundingClientRect().height}));const overflow=[...document.querySelectorAll('.voice-copy,.dialogue-text')].flatMap(e=>{const r=e.getBoundingClientRect(),b=e.parentElement.getBoundingClientRect();return r.left<b.left-1||r.right>b.right+1||r.top<b.top-1||r.bottom>b.bottom+1?[{id:e.closest('[data-beat-id]').dataset.beatId,text:e.textContent,r:r.toJSON(),b:b.toJSON()}]:[]});return{viewport:[innerWidth,innerHeight],bodyWidth:rect.width,bodyHeight:rect.height,pureGapHeight:gaps.reduce((a,g)=>a+g.height,0),contentHeight:rect.height-gaps.reduce((a,g)=>a+g.height,0),horizontalOverflow:document.documentElement.scrollWidth>innerWidth,panels:flow.querySelectorAll('figure.panel').length,images:document.images.length,imagesFailed:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).length,minFont:Math.min(...[...document.querySelectorAll('.voice-copy')].map(e=>parseFloat(getComputedStyle(e).fontSize))),overflow,gaps};});
fs.mkdirSync(path.join(root,'review'),{recursive:true});
await page.locator('#preview-flow').screenshot({path:path.join(root,`complete-${width}.jpg`),type:'jpeg',quality:86,scale:'css',timeout:120000});
// Complete overlapping phone windows preserve every part at readable resolution.
const bounds=await page.locator('#preview-flow').evaluate(e=>({top:e.getBoundingClientRect().top+scrollY,bottom:e.getBoundingClientRect().bottom+scrollY}));
const windows=[];for(let y=bounds.top,k=1;y<bounds.bottom;y+=height-100,k++){
await page.evaluate(y=>scrollTo(0,y),y);const file=`review/window-${width}-${String(k).padStart(3,'0')}.jpg`;
await page.screenshot({path:path.join(root,file),type:'jpeg',quality:85,scale:'css'});windows.push({file,y:await page.evaluate(()=>scrollY)});}
const excerpts=[];for(const [name,id] of [['medicine','p034'],['eda','p036-voice'],['bread','p049'],['listen','p067'],['waterpath','p070'],['wheel','p071'],['wage','p077'],['gift','p085-voice'],['farewell','p091-voice'],['dusk','p094'],['ending','p095-voice']]){
const loc=page.locator(`[data-beat-id="${id}"]`);const y=await loc.evaluate(e=>e.getBoundingClientRect().top+scrollY-15);await page.evaluate(y=>scrollTo(0,y),y);
const file=`review/${name}-${width}.jpg`;await page.screenshot({path:path.join(root,file),type:'jpeg',quality:92,scale:'css'});excerpts.push({id,file,y});}
all.push({...metrics,windows,excerpts});await page.close();}
fs.writeFileSync(path.join(root,'dom-measurements.json'),JSON.stringify(all,null,2));console.log(JSON.stringify(all.map(({windows,excerpts,gaps,...r})=>r),null,2));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});
