// node render_retina_reader.cjs sources.json output-directory [Chromium executable]
// Requires Playwright; renders the original layout at 390 CSS px and 3x pixel density.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');
(async () => {
  const [manifest, output, executablePath] = process.argv.slice(2);
  if (!manifest || !output) throw Error('Provide sources.json and output directory');
  const sources = JSON.parse(fs.readFileSync(manifest));
  const browser = await chromium.launch({headless:true, ...(executablePath ? {executablePath} : {})});
  try {
    for (const [id, source] of Object.entries(sources)) {
      const settings = typeof source === 'string' ? {source} : source;
      const folder = path.join(output, id); fs.mkdirSync(folder, {recursive:true});
      if (fs.existsSync(path.join(folder, 'render.json'))) continue;
      const page = await browser.newPage({viewport:{width:390,height:844},deviceScaleFactor:3});
      await page.goto(pathToFileURL(path.resolve(settings.source)).href);
      // Windowed readers finish drawing their shared raw artwork before export.
      await page.waitForFunction(() => !document.querySelector('main canvas[data-source]') ||
        document.documentElement.dataset.readerReady !== undefined);
      await page.evaluate(async () => {
        if(document.documentElement.dataset.readerReady === 'error') throw Error('Reader artwork failed to decode');
        document.querySelectorAll('img').forEach(img => img.loading = 'eager');
        await document.fonts.ready;
        await Promise.all([...document.images].map(img => img.decode()));
      });
      const size = await page.evaluate(bodyOnly => {
        const main = document.querySelector('main');
        const header = main?.querySelector('header'), footer = main?.querySelector('footer');
        if (bodyOnly && (!header || !footer)) throw Error('Reader needs a header and footer');
        return {width:document.documentElement.scrollWidth,
          top:bodyOnly ? Math.floor(header.getBoundingClientRect().bottom + scrollY) : 0,
          bottom:bodyOnly ? Math.ceil(footer.getBoundingClientRect().top + scrollY) : document.documentElement.scrollHeight,
          ending:bodyOnly ? footer.innerText : ''};
      }, Boolean(settings.bodyOnly));
      if (size.width !== 390) throw Error(`${id}: source overflows the phone width (${size.width})`);
      if (size.bottom <= size.top) throw Error(`${id}: empty reader body`);
      let cover;
      if (settings.bodyOnly) {
        const bytes = await page.locator('main img, main canvas').first().screenshot({type:'jpeg',quality:88,scale:'css'});
        cover = 'cover-'+crypto.createHash('sha256').update(bytes).digest('hex').slice(0,24)+'.jpg';
        fs.writeFileSync(path.join(folder,cover),bytes);
      }
      const cdp = await page.context().newCDPSession(page);
      const blocks = []; let total = 0;
      for (let y=size.top; y<size.bottom; y+=1800) {
        const shot = await cdp.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y,width:390,height:Math.min(1800,size.bottom-y),scale:3}});
        const bytes = Buffer.from(shot.data,'base64');
        if (bytes.readUInt32BE(16) !== 1170) throw Error('Rendered image is not 1170 pixels wide');
        if (bytes.length > 16*1024*1024) throw Error('Image exceeds upload limit');
        const name = 'retina-'+crypto.createHash('sha256').update(bytes).digest('hex').slice(0,24)+'.png';
        fs.writeFileSync(path.join(folder,name),bytes); total+=bytes.length;
        blocks.push({type:'image',src:name,alt:`${settings.subtitle || id} 本文 ${blocks.length+1}`});
      }
      fs.writeFileSync(path.join(folder,'render.json'),JSON.stringify({source:settings.source,sourceDigest:settings.sourceDigest,
        cssWidth:390,pixelWidth:1170,cssHeight:size.bottom-size.top,bodyTop:size.top,bodyBottom:size.bottom,
        ending:size.ending,cover,bytes:total,blocks},null,2));
      console.log(id,blocks.length,'images',Math.round(total/1024)+'KB'); await page.close();
    }
  } finally { await browser.close(); }
})().catch(error=>{console.error(error.message);process.exitCode=1});
