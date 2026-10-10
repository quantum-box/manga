// Export the local artwork review at native phone widths; no network writes.
const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
(async()=>{
  const root=path.resolve(process.argv[2]);
  const browser=await chromium.launch({headless:true});
  try {
    for(const [width,height] of [[390,844],[360,800]]){
      const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
      await page.goto(pathToFileURL(path.join(root,'index.html')).href);
      await page.evaluate(async()=>{await Promise.all([...document.images].map(i=>i.decode()));});
      const figures=await page.locator('figure').all();
      const geometry=[];
      for(const figure of figures){
        const id=await figure.getAttribute('id');
        if(process.argv.length>3 && !process.argv.slice(3).includes(id)) continue;
        try { await figure.screenshot({path:path.join(root,`${id}-${width}.png`),scale:'css',animations:'disabled',timeout:120000}); }
        catch(error) { throw new Error(`${id} at ${width}px: ${error.message}`); }
        geometry.push(await figure.evaluate(el=>({id:el.id,y:el.offsetTop,width:el.getBoundingClientRect().width,height:el.getBoundingClientRect().height})));
      }
      const viewport=await page.evaluate(()=>({width:innerWidth,height:innerHeight,dpr:devicePixelRatio,documentWidth:document.documentElement.scrollWidth}));
      fs.writeFileSync(path.join(root,`layout-${width}.json`),JSON.stringify({viewport,figures:geometry},null,2));
      await page.close();
    }
  } finally {await browser.close();}
})();
