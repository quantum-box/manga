#!/usr/bin/env node
/*
 * Export the finished short as upload-ready episode assets.
 *
 * This intentionally reads the already packaged reader and gives it to
 * Playwright with page.setContent(). It does not navigate to a file URL,
 * start a server, use CDP, or touch the source artwork.
 */

const fs = require("node:fs/promises");
const path = require("node:path");
const crypto = require("node:crypto");

let playwright;
try {
  playwright = require(process.env.PLAYWRIGHT_MODULE || "playwright");
} catch (error) {
  console.error("Playwright is required. Expose it with NODE_PATH or PLAYWRIGHT_MODULE:", error.message);
  process.exit(2);
}

const EPISODE_ROOT = path.resolve(__dirname);
const READER_PATH = path.join(EPISODE_ROOT, "reader.html");
const TITLE = "ホームを裂く一閃";
const CSS_WIDTH = 390;
const VIEWPORT_HEIGHT = 844;
const DPR = 3;
const MAX_STRIP_CSS_HEIGHT = 1800;
const MAX_BYTES = 16 * 1024 * 1024;
const EXPECTED_PANELS = 20;

function sha256(bytes) {
  return crypto.createHash("sha256").update(bytes).digest("hex");
}

function stableName(prefix, bytes, extension) {
  return `${prefix}-${sha256(bytes).slice(0, 24)}.${extension}`;
}

function pngDimensions(bytes) {
  const signature = Buffer.from("89504e470d0a1a0a", "hex");
  if (bytes.length < 24 || !bytes.subarray(0, 8).equals(signature)) {
    throw new Error("Screenshot is not a PNG");
  }
  return {width: bytes.readUInt32BE(16), height: bytes.readUInt32BE(20)};
}

function jpegDimensions(bytes) {
  if (bytes.length < 4 || bytes[0] !== 0xff || bytes[1] !== 0xd8) {
    throw new Error("Cover is not a JPEG");
  }
  let offset = 2;
  while (offset + 9 < bytes.length) {
    while (offset < bytes.length && bytes[offset] !== 0xff) offset += 1;
    while (offset < bytes.length && bytes[offset] === 0xff) offset += 1;
    if (offset >= bytes.length) break;
    const marker = bytes[offset++];
    if (marker === 0xd8 || marker === 0xd9) continue;
    if (offset + 2 > bytes.length) break;
    const length = bytes.readUInt16BE(offset);
    if (length < 2 || offset + length > bytes.length) break;
    const isFrame = (marker >= 0xc0 && marker <= 0xc3) ||
      (marker >= 0xc5 && marker <= 0xc7) ||
      (marker >= 0xc9 && marker <= 0xcb) ||
      (marker >= 0xcd && marker <= 0xcf);
    if (isFrame && length >= 7) {
      return {
        height: bytes.readUInt16BE(offset + 3),
        width: bytes.readUInt16BE(offset + 5),
      };
    }
    offset += length;
  }
  throw new Error("Could not read JPEG dimensions");
}

async function readHash(relativePath) {
  const absolutePath = path.join(EPISODE_ROOT, relativePath);
  const bytes = await fs.readFile(absolutePath);
  return {path: relativePath, sha256: sha256(bytes), bytes: bytes.length};
}

async function sourceHashes() {
  const relativePaths = [
    "reader.html",
    "index.html",
    "reader.css",
    "production/layout.json",
    "review/name-preview/plan.json",
  ];
  const artNames = (await fs.readdir(path.join(EPISODE_ROOT, "art")))
    .filter((name) => /\.(png|jpe?g|webp)$/i.test(name))
    .sort();
  relativePaths.push(...artNames.map((name) => path.posix.join("art", name)));
  const entries = {};
  for (const relativePath of relativePaths) entries[relativePath] = await readHash(relativePath);
  return entries;
}

async function checkOutputIsEmpty(outputPath) {
  try {
    const stat = await fs.stat(outputPath);
    if (!stat.isDirectory()) throw new Error(`--output is not a directory: ${outputPath}`);
    const entries = await fs.readdir(outputPath);
    if (entries.length) throw new Error(`--output must be empty: ${outputPath}`);
  } catch (error) {
    if (error.code === "ENOENT") return;
    throw error;
  }
}

async function waitForReader(page) {
  await page.waitForFunction(() => document.documentElement.dataset.readerReady === "true", null,
    {timeout: 120000});
  await page.evaluate(async () => {
    if (document.fonts && document.fonts.ready) await document.fonts.ready;
    const images = [...document.images];
    await Promise.all(images.map((image) => image.decode ? image.decode() : undefined));
  });
  const state = await page.evaluate(() => ({
    ready: document.documentElement.dataset.readerReady,
    reader: window.__readerReady || null,
    imageStates: [...document.images].map((image) => ({
      id: image.dataset.assetId || null,
      complete: image.complete,
      naturalWidth: image.naturalWidth,
      naturalHeight: image.naturalHeight,
    })),
    fonts: document.fonts ? document.fonts.status : "unsupported",
  }));
  if (state.ready !== "true") throw new Error(`Reader did not become ready: ${JSON.stringify(state)}`);
  if (state.reader && state.reader.errors && state.reader.errors.length) {
    throw new Error(`Reader reported errors: ${state.reader.errors.join("; ")}`);
  }
  const failedImages = state.imageStates.filter((image) =>
    !image.complete || image.naturalWidth <= 0 || image.naturalHeight <= 0);
  if (failedImages.length) throw new Error(`Images failed to decode: ${JSON.stringify(failedImages)}`);
  if (state.fonts !== "loaded" && state.fonts !== "unsupported") {
    throw new Error(`Fonts did not finish loading: ${state.fonts}`);
  }
  return state;
}

async function inspectReader(page) {
  const metrics = await page.evaluate(({expectedPanels}) => {
    const main = document.querySelector("main.episode");
    const body = document.querySelector(".episode-body");
    const header = document.querySelector(".episode-header");
    const footer = document.querySelector(".episode-footer");
    const p15 = document.querySelector("#beat-p15 canvas");
    if (!main || !body || !header || !footer || !p15) {
      throw new Error("Reader must contain episode header, body, footer, and visible p15 canvas");
    }
    const bodyRect = body.getBoundingClientRect();
    const p15Rect = p15.getBoundingClientRect();
    const title = document.querySelector(".episode-header h1")?.textContent?.trim() || "";
    const ending = document.querySelector(".episode-footer")?.textContent?.trim() || "";
    const reader = window.__readerReady || {};
    const panelCount = document.querySelectorAll('.episode-body [data-kind="panel"]').length;
    const canvasCount = document.querySelectorAll('.episode-body canvas[data-source]').length;
    const soundCount = document.querySelectorAll('.episode-body [data-kind="sound"]').length;
    return {
      title,
      ending,
      bodyTop: bodyRect.top + scrollY,
      bodyBottom: bodyRect.bottom + scrollY,
      bodyHeight: bodyRect.height,
      bodyWidth: bodyRect.width,
      viewportWidth: innerWidth,
      viewportHeight: innerHeight,
      scrollWidth: document.documentElement.scrollWidth,
      bodyScrollWidth: document.body.scrollWidth,
      episodeScrollHeight: document.documentElement.scrollHeight,
      panelCount,
      canvasCount,
      soundCount,
      reader,
      p15: {
        visible: !!(p15Rect.width && p15Rect.height),
        left: p15Rect.left,
        top: p15Rect.top + scrollY,
        width: p15Rect.width,
        height: p15Rect.height,
        drawn: p15.dataset.drawn === "true",
      },
      headerBottom: header.getBoundingClientRect().bottom + scrollY,
      footerTop: footer.getBoundingClientRect().top + scrollY,
      expectedPanels,
    };
  }, {expectedPanels: EXPECTED_PANELS});

  if (metrics.title !== TITLE) throw new Error(`Unexpected reader title: ${metrics.title}`);
  if (!metrics.ending.includes("おわり")) throw new Error("Reader footer does not contain おわり");
  if (metrics.viewportWidth !== CSS_WIDTH || metrics.viewportHeight !== VIEWPORT_HEIGHT) {
    throw new Error(`Unexpected viewport: ${metrics.viewportWidth}x${metrics.viewportHeight}`);
  }
  if (metrics.bodyWidth !== CSS_WIDTH) throw new Error(`Body width is ${metrics.bodyWidth}, expected ${CSS_WIDTH}`);
  if (metrics.scrollWidth > CSS_WIDTH || metrics.bodyScrollWidth > CSS_WIDTH) {
    throw new Error(`Reader overflows CSS width: ${metrics.scrollWidth}/${metrics.bodyScrollWidth}`);
  }
  if (metrics.panelCount !== EXPECTED_PANELS || metrics.canvasCount !== 22 || metrics.soundCount !== 2) {
    throw new Error(`Unexpected reader structure: ${JSON.stringify(metrics)}`);
  }
  if (!metrics.p15.visible || !metrics.p15.drawn || metrics.p15.width !== CSS_WIDTH) {
    throw new Error(`p15 canvas is not a visible full-width canvas: ${JSON.stringify(metrics.p15)}`);
  }
  if (metrics.bodyHeight <= 0 || metrics.bodyBottom <= metrics.bodyTop) {
    throw new Error("Reader body has no measurable height");
  }
  return metrics;
}

async function captureProduct(page, metrics) {
  const strips = [];
  const stripCount = Math.ceil(metrics.bodyHeight / MAX_STRIP_CSS_HEIGHT);
  for (let index = 0; index < stripCount; index += 1) {
    const offset = index * MAX_STRIP_CSS_HEIGHT;
    const height = Math.min(MAX_STRIP_CSS_HEIGHT, metrics.bodyHeight - offset);
    const bytes = await page.screenshot({
      type: "png",
      scale: "device",
      fullPage: true,
      captureBeyondViewport: true,
      clip: {x: 0, y: metrics.bodyTop + offset, width: CSS_WIDTH, height},
    });
    const dimensions = pngDimensions(bytes);
    if (dimensions.width !== CSS_WIDTH * DPR) {
      throw new Error(`Strip ${index + 1} is ${dimensions.width}px wide, expected ${CSS_WIDTH * DPR}`);
    }
    if (dimensions.height <= 0 || dimensions.height > MAX_STRIP_CSS_HEIGHT * DPR) {
      throw new Error(`Strip ${index + 1} has invalid height ${dimensions.height}px`);
    }
    if (bytes.length > MAX_BYTES) {
      throw new Error(`Strip ${index + 1} exceeds 16MiB (${bytes.length} bytes)`);
    }
    strips.push({
      bytes,
      name: stableName("retina", bytes, "png"),
      dimensions,
      cssY: metrics.bodyTop + offset,
      cssHeight: height,
    });
  }

  const coverBytes = await page.locator("#beat-p15 canvas").screenshot({
    type: "jpeg",
    quality: 88,
    scale: "css",
  });
  const coverDimensions = jpegDimensions(coverBytes);
  if (coverDimensions.width !== CSS_WIDTH) {
    throw new Error(`Cover is ${coverDimensions.width}px wide, expected visible CSS width ${CSS_WIDTH}`);
  }
  if (!coverDimensions.height || coverBytes.length > MAX_BYTES) {
    throw new Error(`Invalid cover: ${coverDimensions.width}x${coverDimensions.height}, ${coverBytes.length} bytes`);
  }
  return {
    strips,
    cover: {
      bytes: coverBytes,
      name: stableName("cover", coverBytes, "jpg"),
      dimensions: coverDimensions,
    },
  };
}

async function writeProduct(outputPath, metrics, captured, hashes) {
  await checkOutputIsEmpty(outputPath);
  await fs.mkdir(outputPath, {recursive: true});
  for (const strip of captured.strips) await fs.writeFile(path.join(outputPath, strip.name), strip.bytes);
  await fs.writeFile(path.join(outputPath, captured.cover.name), captured.cover.bytes);

  const blocks = captured.strips.map((strip, index) => ({
    type: "image",
    src: strip.name,
    alt: `${TITLE} 本文 ${index + 1}`,
  }));
  blocks.push({type: "ending", text: "おわり"});
  const episode = {
    title: TITLE,
    subtitle: TITLE,
    cover: captured.cover.name,
    blocks,
  };
  await fs.writeFile(path.join(outputPath, "episode.json"), JSON.stringify(episode, null, 2) + "\n");

  const assets = [
    ...captured.strips.map((strip) => ({
      name: strip.name,
      type: "image",
      mime: "image/png",
      sha256: sha256(strip.bytes),
      bytes: strip.bytes.length,
      pixelWidth: strip.dimensions.width,
      pixelHeight: strip.dimensions.height,
      cssY: strip.cssY,
      cssHeight: strip.cssHeight,
    })),
    {
      name: captured.cover.name,
      type: "cover",
      mime: "image/jpeg",
      sha256: sha256(captured.cover.bytes),
      bytes: captured.cover.bytes.length,
      pixelWidth: captured.cover.dimensions.width,
      pixelHeight: captured.cover.dimensions.height,
      source: "visible #beat-p15 canvas at 390 CSS px",
    },
  ];
  const manifest = {
    schema: "platform-cleave/product-export/v1",
    title: TITLE,
    subtitle: TITLE,
    episode: "episode-01",
    scope: "20-panel combat short; approved partial episode; normal-episode length rules excluded",
    publicationPending: true,
    render: {
      cssWidth: CSS_WIDTH,
      viewportHeight: VIEWPORT_HEIGHT,
      deviceScaleFactor: DPR,
      pixelWidth: CSS_WIDTH * DPR,
      maxStripCssHeight: MAX_STRIP_CSS_HEIGHT,
      bodyHeight: metrics.bodyHeight,
      bodyTop: metrics.bodyTop,
      stripCount: captured.strips.length,
      panelCount: metrics.panelCount,
      soundSpanCount: metrics.soundCount,
    },
    readerSha256: hashes["reader.html"].sha256,
    sourceHashes: hashes,
    cover: captured.cover.name,
    assets,
    blocks,
  };
  await fs.writeFile(path.join(outputPath, "manifest.json"), JSON.stringify(manifest, null, 2) + "\n");

  const provenance = {
    schema: "platform-cleave/product-provenance/v1",
    title: TITLE,
    source: {
      reader: "reader.html",
      readerSha256: hashes["reader.html"].sha256,
      files: hashes,
    },
    render: {
      method: "Playwright Chromium page.setContent",
      navigated: false,
      network: false,
      cdp: false,
      viewport: [CSS_WIDTH, VIEWPORT_HEIGHT],
      deviceScaleFactor: DPR,
      bodyTop: metrics.bodyTop,
      bodyHeight: metrics.bodyHeight,
      panelCount: metrics.panelCount,
      stripCount: captured.strips.length,
      stripCssHeightMaximum: MAX_STRIP_CSS_HEIGHT,
    },
    generatedAssets: assets,
    publicationPending: true,
    shortScope: true,
  };
  await fs.writeFile(path.join(outputPath, "provenance.json"), JSON.stringify(provenance, null, 2) + "\n");

  const writtenEpisode = JSON.parse(await fs.readFile(path.join(outputPath, "episode.json"), "utf8"));
  if (writtenEpisode.title !== TITLE || writtenEpisode.subtitle !== TITLE ||
      writtenEpisode.blocks.at(-1)?.text !== "おわり") {
    throw new Error("Written episode.json failed title/subtitle/ending verification");
  }
  for (const strip of captured.strips) {
    const written = await fs.readFile(path.join(outputPath, strip.name));
    const dimensions = pngDimensions(written);
    if (dimensions.width !== CSS_WIDTH * DPR || dimensions.height <= 0 || written.length > MAX_BYTES) {
      throw new Error(`Written PNG failed verification: ${strip.name}`);
    }
  }
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length !== 2 || args[0] !== "--output") {
    throw new Error("Usage: export_product.cjs --output /absolute/empty/output-directory");
  }
  const outputPath = path.resolve(args[1]);
  if (!path.isAbsolute(args[1])) throw new Error("--output must be an absolute path");
  await checkOutputIsEmpty(outputPath);
  await fs.access(READER_PATH);
  const html = await fs.readFile(READER_PATH, "utf8");
  const readerBytes = Buffer.from(html, "utf8");
  const hashes = await sourceHashes();
  hashes["reader.html"].sha256 = sha256(readerBytes);

  const browser = await playwright.chromium.launch({headless: true});
  let metrics;
  let captured;
  try {
    const page = await browser.newPage({
      viewport: {width: CSS_WIDTH, height: VIEWPORT_HEIGHT},
      deviceScaleFactor: DPR,
    });
    const pageErrors = [];
    page.on("pageerror", (error) => pageErrors.push(String(error)));
    await page.setContent(html, {waitUntil: "load"});
    await waitForReader(page);
    metrics = await inspectReader(page);
    if (pageErrors.length) throw new Error(`Page errors during reader load: ${pageErrors.join("; ")}`);
    captured = await captureProduct(page, metrics);
    await page.close();
  } finally {
    await browser.close();
  }
  await writeProduct(outputPath, metrics, captured, hashes);
  console.log(JSON.stringify({
    output: outputPath,
    strips: captured.strips.length,
    bodyHeight: metrics.bodyHeight,
    cover: captured.cover.name,
    readerSha256: hashes["reader.html"].sha256,
    publicationPending: true,
  }, null, 2));
}

main().catch((error) => {
  console.error(error.stack || error.message);
  process.exitCode = 1;
});
