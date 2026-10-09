#!/usr/bin/env node
/*
 * Capture and measure the packaged reader without navigating to a file URL.
 * The HTML is supplied to Playwright with page.setContent(), so this checks
 * the same self-contained offline artifact that a reader receives.
 */

const fs = require("node:fs/promises");
const path = require("node:path");

let playwright;
try {
  playwright = require("playwright");
} catch (error) {
  console.error("Install or expose Playwright before running capture_reader.cjs:", error.message);
  process.exit(2);
}

const episodeDir = path.resolve(__dirname, "..");
const readerPath = path.join(episodeDir, "reader.html");
const outputDir = path.join(episodeDir, "validation", "reader-captures");
const widths = [360, 390];
const heights = {360: 800, 390: 844};

async function waitForReader(page) {
  await page.waitForFunction(() => window.__readerReady &&
    window.__readerReady.drawn === window.__readerReady.canvases, null, {timeout: 30000});
  await page.evaluate(async () => {
    if (document.fonts && document.fonts.ready) await document.fonts.ready;
    await Promise.all([...document.images].map((image) => image.decode ? image.decode().catch(() => {}) : undefined));
  });
}

async function captureWidth(browser, width) {
  const page = await browser.newPage({
    viewport: {width, height: heights[width]},
    deviceScaleFactor: 1,
  });
  const pageErrors = [];
  const consoleErrors = [];
  page.on("pageerror", (error) => pageErrors.push(String(error)));
  page.on("console", (message) => {
    if (message.type() === "error") consoleErrors.push(message.text());
  });

  const html = await fs.readFile(readerPath, "utf8");
  await page.setContent(html, {waitUntil: "load"});
  await waitForReader(page);

  const metrics = await page.evaluate(() => {
    const pool = [...document.querySelectorAll("#asset-pool img")];
    const canvases = [...document.querySelectorAll("canvas[data-asset]")];
    const panels = [...document.querySelectorAll('[data-kind="panel"]')];
    const soundBeats = [...document.querySelectorAll('[data-kind="sound"]')];
    const captions = [...document.querySelectorAll("figcaption.sr-only")];
    const refs = canvases.map((canvas) => canvas.dataset.asset);
    const poolIds = pool.map((image) => image.dataset.assetId);
    const visibleOverlaySelectors = [".dialogue", ".bubble", ".sound", ".sfx"];
    const visibleOverlayCount = visibleOverlaySelectors.reduce((count, selector) =>
      count + [...document.querySelectorAll(selector)].filter((element) => {
        const style = getComputedStyle(element);
        return style.display !== "none" && style.visibility !== "hidden";
      }).length, 0);
    const imageIntegrity = pool.map((image) => ({
      id: image.dataset.assetId,
      loaded: image.complete && image.naturalWidth > 0 && image.naturalHeight > 0,
      embedded: image.src.startsWith("data:image/"),
      width: image.naturalWidth,
      height: image.naturalHeight,
    }));
    const canvasIntegrity = canvases.map((canvas) => ({
      id: canvas.closest("[data-beat-id]")?.dataset.beatId,
      asset: canvas.dataset.asset,
      drawn: canvas.dataset.drawn === "true",
      width: canvas.width,
      height: canvas.height,
      cssWidth: canvas.getBoundingClientRect().width,
      cssHeight: canvas.getBoundingClientRect().height,
      left: canvas.getBoundingClientRect().left,
      top: canvas.getBoundingClientRect().top,
    }));
    const geometry = (element) => {
      const rect = element.getBoundingClientRect();
      return {id: element.dataset.beatId, left: rect.left, top: rect.top,
        width: rect.width, height: rect.height};
    };
    const groups = (selector, key) => [...document.querySelectorAll(selector)].map((group) => ({
      name: group.dataset[key], ...geometry(group),
      members: [...group.querySelectorAll('[data-kind="panel"]')].map(geometry),
    }));
    return {
      viewportWidth: innerWidth,
      viewportHeight: innerHeight,
      scrollWidth: document.documentElement.scrollWidth,
      bodyScrollWidth: document.body.scrollWidth,
      scrollHeight: document.documentElement.scrollHeight,
      panelCount: panels.length,
      soundBeatCount: soundBeats.length,
      pauseCount: document.querySelectorAll('[data-kind="pause"]').length,
      canvasCount: canvases.length,
      captionCount: captions.length,
      sourceAssetCount: pool.length,
      uniqueSourceAssetCount: new Set(poolIds).size,
      referencedSourceAssetCount: new Set(refs).size,
      unresolvedRefs: refs.filter((ref) => !poolIds.includes(ref)),
      visibleOverlayCount,
      drawnCanvasCount: canvasIntegrity.filter((item) => item.drawn).length,
      imageIntegrity,
      canvasIntegrity,
      fontsReady: document.fonts ? document.fonts.status === "loaded" : true,
      episodeHeight: document.querySelector('.episode').getBoundingClientRect().height,
      bodyHeight: document.querySelector('.episode-body').getBoundingClientRect().height,
      explicitPauseHeight: [...document.querySelectorAll('.pause')]
        .reduce((sum, element) => sum + element.getBoundingClientRect().height, 0),
      rows: groups('.panel-row', 'row'),
      compositions: groups('.composition', 'composition'),
      soundSlots: soundBeats.map(geometry),
    };
  });

  const captureDir = path.join(outputDir, String(width));
  await fs.mkdir(captureDir, {recursive: true});
  await page.screenshot({path: path.join(captureDir, "full.png"), fullPage: true});

  // Native panel captures expose crop and lettering errors hidden by a full-page thumbnail.
  for (const panel of await page.locator('[data-kind="panel"]').all()) {
    const id = await panel.getAttribute('data-beat-id');
    await panel.screenshot({path: path.join(captureDir, `${id}.png`)});
  }
  await page.evaluate(() => window.scrollTo(0, 0));
  const partHeight = Math.ceil(metrics.scrollHeight / 4);
  for (let index = 0; index < 4; index += 1) {
    const y = index * partHeight;
    const height = Math.min(partHeight, metrics.scrollHeight - y);
    await page.screenshot({path: path.join(captureDir, `part-${index + 1}.png`),
      clip: {x: 0, y, width, height}, fullPage: true});
  }

  const maxScroll = Math.max(0, metrics.scrollHeight - heights[width]);
  const windows = [];
  for (let index = 0; index < 4; index += 1) {
    const y = index === 3 ? maxScroll : Math.round(maxScroll * index / 3);
    await page.evaluate((scrollY) => window.scrollTo(0, scrollY), y);
    await page.waitForTimeout(80);
    await page.screenshot({path: path.join(captureDir, `window-${String(index).padStart(2, "0")}.png`)});
    windows.push({index, y, height: heights[width]});
  }

  await page.close();
  return {
    ...metrics,
    pageErrors,
    consoleErrors,
    scrollWindows: windows,
    fullCapture: path.join("validation", "reader-captures", String(width), "full.png"),
  };
}

async function main() {
  await fs.access(readerPath);
  await fs.mkdir(outputDir, {recursive: true});
  const browser = await playwright.chromium.launch({headless: true});
  const results = {};
  try {
    for (const width of widths) results[width] = await captureWidth(browser, width);
  } finally {
    await browser.close();
  }
  const report = {
    schema: "platform-cleave/finished-reader-validation/v1",
    source: "reader.html",
    method: "Playwright page.setContent, DPR1, real scroll windows",
    widths,
    results,
    checks: {
      allImagesLoaded: widths.every((width) => results[width].imageIntegrity.every((image) => image.loaded)),
      allCanvasesDrawn: widths.every((width) => results[width].drawnCanvasCount === results[width].canvasCount),
      expectedTwentyPanels: widths.every((width) => results[width].panelCount === 20),
      expectedTwoSoundSpans: widths.every((width) => results[width].soundBeatCount === 2),
      captionsCoverEveryCanvas: widths.every((width) => results[width].captionCount === results[width].canvasCount),
      allCanvasSourcesResolve: widths.every((width) => results[width].unresolvedRefs.length === 0),
      expectedSevenSourceAssets: widths.every((width) => results[width].sourceAssetCount === 7),
      exportCompatibleStructure: widths.every((width) => results[width].canvasCount === 22),
      approvedParallelRows: widths.every((width) => {
        const rows = results[width].rows;
        return rows.length === 2 && rows.every((row) => row.members.length === 2 &&
          Math.abs(row.members[0].top - row.members[1].top) < 1 &&
          row.members[0].left > row.members[1].left);
      }),
      approvedCompositionOffsets: widths.every((width) => {
        const groups = results[width].compositions;
        const expected = {'counter-load': [[0,18],[53,75]], 'off-balance': [[51,0],[0,245]]};
        return groups.length === 2 && groups.every((group) =>
          group.members.length === 2 && group.members.every((member, index) => {
            const [x,y] = expected[group.name][index];
            return Math.abs(member.left - group.left - x / 100 * width) < 1 &&
              Math.abs(member.top - group.top - y / 390 * width) < 1;
          }));
      }),
      approvedSoundSlotHeights: widths.every((width) => results[width].soundSlots.every((slot) =>
        Math.abs(slot.height - ({ring:180, 'footstep-away':230}[slot.id]) / 390 * width) < 1 &&
        Math.abs(slot.height - results[width].canvasIntegrity.find((canvas) => canvas.id === slot.id).cssHeight) < 1)),
      allCanvasGeometryPositive: widths.every((width) => results[width].canvasIntegrity.every((canvas) =>
        canvas.cssWidth > 0 && canvas.cssHeight > 0 && canvas.width > 0 && canvas.height > 0)),
      uniqueSourcesEmbeddedOnce: widths.every((width) =>
        results[width].sourceAssetCount === results[width].uniqueSourceAssetCount &&
        results[width].imageIntegrity.every((image) => image.embedded)),
      noVisibleHtmlLetteringOverlays: widths.every((width) => results[width].visibleOverlayCount === 0),
      noHorizontalOverflow: widths.every((width) =>
        results[width].scrollWidth <= results[width].viewportWidth &&
        results[width].bodyScrollWidth <= results[width].viewportWidth),
      noPageOrConsoleErrors: widths.every((width) =>
        results[width].pageErrors.length === 0 && results[width].consoleErrors.length === 0),
    },
  };
  await fs.writeFile(path.join(outputDir, "metrics.json"), JSON.stringify(report, null, 2) + "\n");
  console.log(JSON.stringify(report.checks, null, 2));
  if (Object.values(report.checks).some((value) => !value)) process.exitCode = 1;
}

main().catch((error) => {
  console.error(error.stack || error.message);
  process.exitCode = 1;
});
