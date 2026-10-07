const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require(process.env.WEBTOON_PLAYWRIGHT_MODULE||'playwright');
const base=path.resolve(__dirname,'../..');
(async()=>{const browser=await chromium.launch({headless:true,executablePath:process.env.WEBTOON_CHROME||(process.platform==='darwin'&&fs.existsSync('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')?'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome':undefined)});try{
 const config=JSON.parse(fs.readFileSync(path.join(__dirname,'windows.json'))),out=path.join(__dirname,'review');fs.mkdirSync(out,{recursive:true});
 for(const arg of process.argv.slice(2)){
  const n=Number(arg),dir=path.join(base,`episode-${String(n).padStart(2,'0')}`),files=fs.readdirSync(path.join(dir,'art')).filter(f=>f.includes('remake')&&f.endsWith('.png')).sort();
  for(let offset=0;offset<files.length;offset+=4){
   const cells=files.slice(offset,offset+4).map(f=>{const raw=fs.readFileSync(path.join(dir,'art',f)),w=raw.readUInt32BE(16),h=raw.readUInt32BE(20),id=f==='remake-00-opening.png'?'00-remake-opening':path.basename(f,'.png'),cuts=config[`${n}/${id}`]?.cuts||[];return `<figure><figcaption>${n}/${f}</figcaption><div class="original"><img src="${path.relative(out,path.join(dir,'art',f))}">${cuts.map(y=>`<span style="top:${y/w*360}px">${y}</span>`).join('')}</div></figure>`;});
   const page=await browser.newPage({viewport:{width:720,height:900},deviceScaleFactor:1});const doc=`<!doctype html><meta charset="utf-8"><style>*{box-sizing:border-box}body{margin:0;background:#fffaf0;font:14px sans-serif}.grid{display:grid;grid-template-columns:360px 360px;align-items:start}figure{margin:0}figcaption{height:24px}.original{position:relative}img{display:block;width:360px;height:auto}span{position:absolute;left:0;width:100%;border-top:1px solid #f22;color:red;font-weight:bold;background:transparent}</style><div class="grid">${cells.join('')}</div>`;const file=path.join(out,`episode-${n}-sources-${offset/4}.html`);fs.writeFileSync(file,doc);await page.goto(pathToFileURL(file).href);await page.evaluate(async()=>Promise.all([...document.images].map(i=>i.decode())));await page.screenshot({path:path.join(out,`episode-${n}-sources-${offset/4}.png`),fullPage:true});await page.close();
  }
  console.log(`Review sheets: episode ${n}, ${files.length} sources with proposed window boundaries`);
 }
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1});
