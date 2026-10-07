// Native layout export; generated/adopted PNG originals are never edited.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { createCanvas, loadImage } = require('@napi-rs/canvas');
const dir = __dirname;
const assets = JSON.parse(fs.readFileSync(path.join(dir, 'assets.json'), 'utf8'));
const sequence = [
  { id: 'route', alt: '胸の核から裸の腕へ光が走り、手首に格子が現れる。システム「装甲展開、開始。」、音「シュウウ…」。' },
  { gap: 60, purpose: '手首の格子から固定の音まで、小さな間' },
  { id: 'sound', alt: '白い余白に、手首の留め具の音「カチッ」だけ。' },
  { gap: 80, purpose: '固定された瞬間を受け止める' },
  { id: 'voice', alt: '白い余白にシステムの通知「接続完了。」だけ。縦書き、枠なし。' },
  { gap: 100, purpose: '接続完了を聞いて、姿を待つ' },
  { id: 'light', alt: '白い余白を、細いシアンの光だけが下へ流れる。人物はまだ見えない。' },
  { gap: 120, purpose: '光が消えてから、全身が初めて現れるまで' },
  { id: 'hero', alt: '黒い装甲、シアンの核と継ぎ目、赤いマフラーのレン。ミラは後ろで安全に立つ。レン「なら、今度こそ。」、音「ガキンッ！」。' },
  { gap: 100, purpose: '完成した姿の余韻' },
];

async function main() {
  const loaded = {};
  for (const a of assets) {
    const bytes = fs.readFileSync(path.join(dir, a.file));
    if (crypto.createHash('sha256').update(bytes).digest('hex') !== a.sha256) throw new Error(`Original changed: ${a.id}`);
    loaded[a.id] = await loadImage(path.join(dir, a.file));
    if (loaded[a.id].width !== a.width || loaded[a.id].height !== a.height) throw new Error(`Dimensions changed: ${a.id}`);
  }
  const widths = [{ width: 390, height: 844 }, { width: 360, height: 800 }];
  const layouts = [];
  fs.mkdirSync(path.join(dir, 'review'), { recursive: true });
  for (const viewport of widths) {
    const { width, height: windowHeight } = viewport;
    let y = 0;
    const rows = sequence.map(s => {
      const a = assets.find(a => a.id === s.id);
      const height = a ? Math.round(width * a.height / a.width) : Math.round(s.gap * width / 390);
      const row = { ...s, y, height };
      y += height;
      return row;
    });
    const canvas = createCanvas(width, y);
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, width, y);
    for (const row of rows) if (row.id) ctx.drawImage(loaded[row.id], 0, row.y, width, row.height);
    fs.writeFileSync(path.join(dir, `complete-${width}.png`), canvas.toBuffer('image/png'));
    const offsets = [];
    for (let offset = 0; offset < y - windowHeight; offset += Math.round(windowHeight * 0.65)) offsets.push(offset);
    offsets.push(Math.max(0, y - windowHeight));
    const windows = [];
    for (const [i, offset] of offsets.entries()) {
      const window = createCanvas(width, windowHeight);
      window.getContext('2d').drawImage(canvas, 0, offset, width, windowHeight, 0, 0, width, windowHeight);
      const file = `review/window-${width}-${String(i).padStart(2, '0')}.png`;
      fs.writeFileSync(path.join(dir, file), window.toBuffer('image/png'));
      windows.push({ file, offset });
    }
    layouts.push({ ...viewport, totalHeight: y, rows, windows });
  }
  fs.writeFileSync(path.join(dir, 'layout.json'), JSON.stringify({ method: 'native canvas layout, not browser rendering', layouts }, null, 2) + '\n');
  const html = `<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ゼロブレイク — 装着シーンの余白演出</title>
<style>
*{box-sizing:border-box}html,body{margin:0;background:#fff}main{width:100%;max-width:480px;margin:auto}figure{margin:0}img{display:block;width:100%;height:auto}.pause{width:100%;aspect-ratio:390 / var(--height)}
</style></head><body><main aria-label="ゼロブレイク・装着シーンの演出試作">
${sequence.map(s => {
    if (!s.id) return `<div class="pause" style="--height:${s.gap}" aria-hidden="true" data-pacing-purpose="${s.purpose}"></div>`;
    const a = assets.find(a => a.id === s.id);
    return `<figure id="${s.id}"><img src="${a.file}" width="${a.width}" height="${a.height}" alt="${s.alt}"></figure>`;
  }).join('\n')}
</main></body></html>\n`;
  fs.writeFileSync(path.join(dir, 'index.html'), html);
  const prompts = JSON.parse(fs.readFileSync(path.join(dir, 'prompts.json'), 'utf8'));
  fs.writeFileSync(path.join(dir, 'PROMPTS.md'), '# 実際に使った作画指示\n\n組み込み `image_gen` で、人物のいない余白用素材3枚を新規生成した。以下は実行した全文。元の装着・全身原画2枚は無加工で再利用。PNG原本の寸法・ハッシュ・出所は [assets.json](assets.json)。\n\n' + prompts.assets.map(a => `## ${a.id}\n\n\`\`\`text\n${a.prompt}\n\`\`\`\n`).join('\n'));
  console.log(JSON.stringify(layouts.map(l => ({ width: l.width, totalHeight: l.totalHeight, windows: l.windows.length }))));
}
main().catch(error => { console.error(error); process.exitCode = 1; });
