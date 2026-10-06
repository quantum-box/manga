// Render the completed comic as phone-sized browser viewports, without editing art.
const { chromium } = require('playwright');
const { PNG } = require('pngjs');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');
const numbers = process.argv.slice(2).map(Number);
const episodes = numbers.length ? numbers : Array.from({ length: 9 }, (_, i) => i + 2);
const chrome = process.env.CHROMIUM_EXECUTABLE_PATH ||
  (fs.existsSync('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' : undefined);
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');

(async () => {
  const browser = await chromium.launch({ headless: true, ...(chrome ? { executablePath: chrome } : {}) });
  try {
    for (const number of episodes) {
      const directory = path.join(root, `episode-${String(number).padStart(2, '0')}`);
      const manifest = JSON.parse(fs.readFileSync(path.join(directory, 'manifest.json')));
      const reader = fs.readFileSync(path.join(directory, 'reader.html'), 'utf8');
      const embedded = [...reader.matchAll(/src="data:image\/png;base64,([A-Za-z0-9+/=]+)"/g)];
      if (embedded.length !== manifest.shots.length) throw Error(`Missing embedded art in episode ${number}`);
      for (let i = 0; i < embedded.length; i++) {
        const original = fs.readFileSync(path.join(directory, 'art', manifest.shots[i].file));
        if (!Buffer.from(embedded[i][1], 'base64').equals(original) || sha(original) !== manifest.shots[i].sha256)
          throw Error(`Artwork mismatch: ${number}/${manifest.shots[i].id}`);
      }
      const review = path.join(directory, 'review');
      fs.mkdirSync(review, { recursive: true });
      const views = [];
      for (const viewport of [{ width: 390, height: 844 }, { width: 360, height: 800 }]) {
        const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
        await page.goto(pathToFileURL(path.join(directory, 'reader.html')).href);
        await page.waitForLoadState('load');
        const result = await page.evaluate(() => ({
          width: innerWidth, viewportHeight: innerHeight,
          pageWidth: document.documentElement.scrollWidth,
          pageHeight: document.documentElement.scrollHeight,
          images: [...document.images].map(i => ({ loaded: i.complete && i.naturalWidth > 0,
            naturalWidth: i.naturalWidth, naturalHeight: i.naturalHeight,
            displayWidth: i.getBoundingClientRect().width })),
          order: [...document.querySelectorAll('figure.scene')].map(e => ({
            id: e.id, top: e.getBoundingClientRect().top, height: e.getBoundingClientRect().height })),
          htmlDialogueCount: document.querySelectorAll('.dialogue,.thought,.system,.bubble').length,
          pending: document.querySelectorAll('.pending').length,
        }));
        if (result.width !== viewport.width || result.pageWidth > viewport.width || result.pending ||
            result.images.length !== manifest.shots.length || result.images.some(i => !i.loaded) ||
            result.htmlDialogueCount || result.order.map(x => x.id).join(',') !== manifest.shots.map(s => s.id).join(','))
          throw Error(`Invalid phone reader: ${JSON.stringify(result)}`);
        result.reveals = manifest.revealPairs.map(pair => {
          const cue = result.order.find(o => o.id === pair.cue), answer = result.order.find(o => o.id === pair.answer);
          const distance = answer.top + answer.height * (pair.answerTop ?? 0) - cue.top - cue.height * (pair.cueBottom ?? 1);
          if (pair.minDistance && distance < pair.minDistance * viewport.width / 390)
            throw Error(`Reveal is too close: ${number}/${pair.answer}`);
          return { ...pair, distance, measuredWithInspectedAnchors: pair.cueBottom !== undefined && pair.answerTop !== undefined };
        });
        for (const shot of manifest.shots) {
          await page.locator(`#${shot.id}`).screenshot({ path: path.join(review, `scene-${viewport.width}-${shot.id}.png`) });
        }
        // Avoid Chromium's tall full-page capture limit: join ordinary scroll views.
        const full = new PNG({ width: viewport.width, height: result.pageHeight });
        const tiles = [];
        for (let y = 0; y < result.pageHeight; y += viewport.height) {
          const actual = await page.evaluate(y => { scrollTo(0, y); return scrollY; }, y);
          const raw = await page.screenshot({ path: path.join(review, `screen-${viewport.width}-${tiles.length}.png`) });
          const tile = PNG.sync.read(raw), offset = y - actual;
          const rows = Math.min(viewport.height, result.pageHeight - y), stride = viewport.width * 4;
          if (tile.width !== viewport.width || tile.height !== viewport.height || offset < 0 || offset + rows > tile.height)
            throw Error('Incorrect viewport tile geometry');
          for (let r = 0; r < rows; r++)
            tile.data.copy(full.data, (y + r) * stride, (offset + r) * stride, (offset + r + 1) * stride);
          tiles.push({ raw, y, offset, rows });
        }
        const fullBytes = PNG.sync.write(full), reread = PNG.sync.read(fullBytes);
        for (const t of tiles) {
          const tile = PNG.sync.read(t.raw), stride = viewport.width * 4;
          for (let row = 0; row < t.rows; row++) {
            if (!reread.data.subarray((t.y + row) * stride, (t.y + row + 1) * stride)
                .equals(tile.data.subarray((t.offset + row) * stride, (t.offset + row + 1) * stride)))
              throw Error('Full raster differs from a displayed scroll viewport');
          }
        }
        fs.writeFileSync(path.join(directory, `complete-${viewport.width}.png`), fullBytes);
        result.rasterExport = { method: 'joined unchanged browser scroll viewport pixels', tiles: tiles.length,
          width: viewport.width, height: result.pageHeight, allScrollTilesMatch: true };
        views.push(result);
        await page.close();
      }
      // Four actual 360px scene captures per sheet, for readable visual review.
      for (let start = 0; start < manifest.shots.length; start += 4) {
        const group = manifest.shots.slice(start, start + 4), images = group.map(s => {
          const filename = path.join(review, `scene-360-${s.id}.png`);
          const bytes = fs.readFileSync(filename), png = PNG.sync.read(bytes);
          return { shot: s, bytes, width: png.width, height: png.height };
        });
        const rowHeights = [Math.max(...images.slice(0, 2).map(i => i.height)),
          images.length > 2 ? Math.max(...images.slice(2).map(i => i.height)) : 0];
        const page = await browser.newPage({ viewport: { width: 740, height: rowHeights.reduce((a, b) => a + b, 0) + 140 }, deviceScaleFactor: 1 });
        await page.setContent('<style>*{box-sizing:border-box}body{margin:0;background:#edf3f7}main{display:grid;grid-template-columns:360px 360px;gap:14px 10px;padding:5px}section{width:360px}p{margin:0;height:32px;font:13px sans-serif}img{display:block;max-width:360px;height:auto}</style><main>' +
          images.map(i => `<section><p>第${number}話 ${i.shot.file}</p><img width="${i.width}" height="${i.height}" src="data:image/png;base64,${i.bytes.toString('base64')}"></section>`).join('') + '</main>');
        await page.waitForFunction(() => [...document.images].every(i => i.complete && i.naturalWidth));
        await page.screenshot({ path: path.join(review, `contact-360-${start / 4}.png`), fullPage: true });
        await page.close();
      }
      fs.writeFileSync(path.join(directory, 'validation.json'), JSON.stringify({
        episode: number, title: manifest.title, method: 'built-in image_gen',
        sourceArtworkBytesPreserved: true, selfContainedReader: true,
        viewports: views, visualReview: { status: 'pending', evidence: 'review/contact-360-*.png',
          limits: 'Browser phone renders; raster text requires visual review, not DOM font measurements. Physical device not tested.' },
      }, null, 2) + '\n');
      console.log(JSON.stringify({ episode: number, images: manifest.shots.length,
        heights: views.map(v => [v.width, v.pageHeight]), visualReview: 'pending' }));
    }
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
