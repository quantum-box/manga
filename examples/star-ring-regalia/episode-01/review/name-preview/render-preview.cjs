// NODE_PATH=<bundled node_modules> node render-preview.cjs
// Renders the saved standalone name; no network or production writes.
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const root = __dirname;
  const review = path.join(root, 'review');
  fs.mkdirSync(review, {recursive: true});
  const browser = await chromium.launch({headless: true});
  const results = [];
  try {
    if (process.argv.includes('--cart-excerpt')) {
      const page = await browser.newPage({viewport: {width: 360, height: 800}, deviceScaleFactor: 1});
      await page.goto(pathToFileURL(path.join(root, 'index.html')).href);
      await page.evaluate(async () => {
        await document.fonts.ready;
        await Promise.all([...document.images].map(image => image.decode()));
      });
      const top = await page.locator('[data-beat-id="p057-voice-0"]').evaluate(element =>
        element.getBoundingClientRect().top + scrollY - 30);
      const captures = [];
      for (let index = 0; index < 2; index++) {
        await page.evaluate(y => scrollTo(0, y), top + index * 680);
        const file = `cart-360-${String(index + 1).padStart(2, '0')}.jpg`;
        await page.screenshot({path: path.join(review, file), type: 'jpeg', quality: 88, scale: 'css'});
        captures.push({file: `review/${file}`, scrollY: await page.evaluate(() => scrollY)});
      }
      fs.writeFileSync(path.join(review, 'cart-excerpt.json'), JSON.stringify({width: 360, height: 800,
        dpr: 1, overlapCssPx: 120, source: 'index.html', captures}, null, 2));
      console.log(JSON.stringify({cartExcerpt: captures}));
      await page.close();
      return;
    }
    for (const [width, height] of [[390, 844], [360, 800]]) {
      const page = await browser.newPage({viewport: {width, height}, deviceScaleFactor: 1});
      await page.goto(pathToFileURL(path.join(root, 'index.html')).href);
      await page.evaluate(async () => {
        await document.fonts.ready;
        await Promise.all([...document.images].map(image => image.decode()));
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      });
      const layout = await page.evaluate(() => {
        const box = element => {
          const r = element.getBoundingClientRect();
          return {x: r.x, y: r.y + scrollY, width: r.width, height: r.height,
            right: r.right, bottom: r.bottom + scrollY};
        };
        const flow = document.getElementById('preview-flow');
        const flowBox = box(flow);
        const panels = [...flow.querySelectorAll('figure.panel')].map(element => ({
          id: element.dataset.beatId, ...box(element),
          crop: {x: element.style.getPropertyValue('--crop-x'), y: element.style.getPropertyValue('--crop-y'),
            width: element.style.getPropertyValue('--crop-w'), height: element.style.getPropertyValue('--crop-h')},
          copy: [...element.querySelectorAll('.balloon, .sfx')].map(copy => ({text: copy.innerText, ...box(copy)}))
        }));
        const text = [...flow.querySelectorAll('.floating-copy')].map(element => ({
          id: element.closest('[data-beat-id]').dataset.beatId, text: element.innerText, ...box(element)
        }));
        // p091 fades to a wholly empty bottom band. Its final 22% is excluded
        // after native-size visual review; borders alone do not make content.
        const imageInternalBlank = panels.filter(p => p.id === 'p091').map(p => ({
          panel: p.id, top: p.y + p.height * .78, height: p.height * .22,
          reason: 'Full-width blank bottom band below the portrait fade; visually inspected'
        }));
        const intervals = [...panels.map(p => [p.y, p.bottom - (p.id === 'p091' ? p.height * .22 : 0)]),
          ...panels.flatMap(p => p.copy.map(c => [c.y, c.bottom])), ...text.map(t => [t.y, t.bottom])]
          .sort((a, b) => a[0] - b[0]);
        const union = [];
        for (const [start, end] of intervals) {
          const last = union[union.length - 1];
          if (last && start <= last[1]) last[1] = Math.max(last[1], end);
          else union.push([start, end]);
        }
        const gaps = [];
        let cursor = flowBox.y;
        for (const [start, end] of union) {
          if (start > cursor) gaps.push({top: cursor - flowBox.y, height: start - cursor});
          cursor = Math.max(cursor, end);
        }
        if (cursor < flowBox.bottom) gaps.push({top: cursor - flowBox.y, height: flowBox.bottom - cursor});
        const pureGapHeight = gaps.reduce((sum, gap) => sum + gap.height, 0);
        const copyOverflow = panels.flatMap(panel => panel.copy.filter(copy =>
          copy.x < panel.x - 1 || copy.right > panel.right + 1 || copy.y < panel.y - 1 || copy.bottom > panel.bottom + 1
        ).map(copy => ({panel: panel.id, copy})));
        const allCopy = [...panels.flatMap(p => p.copy), ...text];
        const horizontalCopyOverflow = allCopy.filter(copy => copy.x < -1 || copy.right > innerWidth + 1);
        return {viewport: {width: innerWidth, height: innerHeight, dpr: devicePixelRatio},
          flow: flowBox, bodyHeightCssPx: flowBox.height, pureGapHeightCssPx: pureGapHeight,
          contentHeightCssPx: flowBox.height - pureGapHeight, screenUnits: flowBox.height / innerHeight,
          documentWidth: document.documentElement.scrollWidth, panels, text, pureGaps: gaps, imageInternalBlank,
          copyOverflow, horizontalCopyOverflow,
          imageFailures: [...document.images].filter(image => !image.complete || !image.naturalWidth).length,
          fontSize: getComputedStyle(flow.querySelector('.dialogue-text') || flow.querySelector('.voice-copy')).fontSize};
      });
      fs.writeFileSync(path.join(review, `layout-${width}.json`), JSON.stringify(layout, null, 2));
      await page.locator('#preview-flow').screenshot({path: path.join(root, `complete-${width}.jpg`), type: 'jpeg', quality: 85, scale: 'css'});
      const windows = [];
      for (let y = layout.flow.y, index = 1; y < layout.flow.bottom; y += height - 120, index++) {
        await page.evaluate(y => scrollTo(0, y), y);
        const actual = await page.evaluate(() => scrollY);
        const filename = `window-${width}-${String(index).padStart(2, '0')}.jpg`;
        await page.screenshot({path: path.join(review, filename), type: 'jpeg', quality: 83, scale: 'css'});
        windows.push({file: `review/${filename}`, scrollY: actual, bodyOffset: actual - layout.flow.y});
      }
      fs.writeFileSync(path.join(review, `windows-${width}.json`), JSON.stringify(windows, null, 2));
      results.push({width, height, ...layout, windows});
      console.log(JSON.stringify({width, bodyHeight: layout.bodyHeightCssPx, pureGap: layout.pureGapHeightCssPx,
        contentHeight: layout.contentHeightCssPx, panels: layout.panels.length, copyOverflow: layout.copyOverflow.length,
        horizontalCopyOverflow: layout.horizontalCopyOverflow.length, imagesFailed: layout.imageFailures}));
      await page.close();
    }
    fs.writeFileSync(path.join(review, 'browser-checks.json'), JSON.stringify(results.map(({panels, text, ...r}) => r), null, 2));
  } finally { await browser.close(); }
})().catch(error => {console.error(error); process.exitCode = 1;});
