"""Adopt Episode 1's scroll staging without repainting original PNGs.

Each source is packaged once. Display windows separate existing panel rows,
while generated whitespace beats carry the displaced dialogue and sounds.
"""
import hashlib
import html
import json
from pathlib import Path
from struct import unpack

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
STATE = ROOT / 'production/episode-01-scroll'
DIRECTORY = ROOT / 'v5'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def validate_layout(manifest):
    layout = manifest['scrollLayout']
    sources = {s['id']: s for s in layout['sources']}
    shots = {s['id']: s for s in manifest['shots']}
    assert len(sources) == len(layout['sources'])
    ids = set()
    actual = {key: [] for key in ('panelRefs', 'lineRefs', 'soundRefs', 'textRefs')}
    for unit in layout['units']:
        assert unit['id'] not in ids, unit['id']
        ids.add(unit['id'])
        source = sources[unit['sourceId']]
        x, y, w, h = unit['crop']
        assert 0 <= x and 0 <= y and w > 0 and h > 0
        assert x + w <= source['width'] and y + h <= source['height'], unit['id']
        assert 0 < unit['widthPercent'] <= 100 and unit['align'] in ('left', 'center', 'right')
        assert 0 <= unit['pause'] <= 720
        for key in actual:
            actual[key].extend(tuple(ref) for ref in unit.get(key, []))
    for key, field in [('panelRefs', 'panels'), ('lineRefs', 'lines'), ('soundRefs', 'sounds'), ('textRefs', 'visible_text')]:
        expected = [(s['id'], i) for s in manifest['shots'] for i in range(len(s.get(field, [s] if field == 'panels' else [])))]
        assert sorted(actual[key]) == sorted(expected), (key, actual[key], expected)
        # Spoken lines and notices stay in their canonical order; sound may precede its detail.
        if key in ('lineRefs', 'textRefs'):
            assert actual[key] == expected, key
    assert {u['sourceId'] for u in layout['units']} == set(sources)
    for source in sources.values():
        path = DIRECTORY / 'art' / source['file']
        assert sha(path) == source['sha256']
        assert unpack('>II', path.read_bytes()[16:24]) == (source['width'], source['height'])
        if source.get('record'):
            record = json.loads((REPO / source['record']).read_text())
            assert record['sha256'] == source['sha256'] and record['file'] == source['file']
            for ref in record.get('references', []):
                assert sha(REPO / ref['path']) == ref['sha256']
            if record.get('source'):
                assert sha(REPO / record['source']) == source['sha256']


def adopt(manifest):
    plan = json.loads((STATE / 'plan.json').read_text())
    manifest.update(scrollEdition=plan['edition'], scrollLayout=plan['layout'])
    manifest.setdefault('title', '最弱判定、最強の一歩。')
    manifest['change'] = '第1話全編をスクロールで段階的に開示。余白の声・音・光、短い動作、横並び・斜め枠、発見の間を場面ごとに設計。'
    validate_layout(manifest)
    dump(DIRECTORY / 'manifest.json', manifest)
    sources = manifest['scrollLayout']['sources']
    shots = {s['id']: s for s in manifest['shots']}
    css = """*{box-sizing:border-box}body{margin:0;background:#18202b;color:#203045;font-family:'Hiragino Kaku Gothic ProN','Yu Gothic',sans-serif}.episode{width:100%;max-width:480px;margin:auto;container-type:inline-size;background:white}header{height:53.8461538462cqw;padding:10.77cqw 6.154cqw;background:#111a29;color:#edf8ff}header small{font-size:3.077cqw;color:#acd7ee}h1{font-size:8.205cqw;line-height:1.4;margin:3.846cqw 0 2.564cqw}header p{font-size:3.846cqw;margin:0;line-height:1.8}.beat{margin:0;width:var(--width)}.beat.center{margin-inline:auto}.beat.right{margin-left:auto}.beat canvas{display:block;width:100%;height:auto}.pause{height:var(--pause)}footer{height:33.3333333333cqw;padding:8cqw 5cqw;text-align:center;font-size:3.846cqw;line-height:2}footer a{color:#365f8a;margin:0 3cqw}.error{padding:24px;color:#8f2222}[hidden]{display:none!important}"""
    title = html.escape(manifest['title'])
    out = [f'<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ゼロ・ブレイク 第1話 {title}</title><style>{css}</style><main class="episode"><header><small>異世界転生 × スーパーヒーロー / 第1話</small><h1>ゼロ・ブレイク</h1><p>{title}</p></header>']
    storyboard = [f'# 第1話 {manifest["title"]} — 余白とスクロールの改稿', '', '73の原作コマを段階的に見せる。余白の声・音・光はコマとは別の演出。横並びの反応と斜めの装着枠は必要な場面で残す。原画PNGは改変せず、表示窓で必要な部分だけを見せる。文字は原画に収録し、HTMLで重ねない。', '']
    for unit in manifest['scrollLayout']['units']:
        lines = [shots[s]['lines'][i]['speaker'] + '：' + shots[s]['lines'][i]['text'] for s, i in unit.get('lineRefs', [])]
        lines += ['効果音：' + shots[s]['sounds'][i] for s, i in unit.get('soundRefs', [])]
        lines += [shots[s]['visible_text'][i]['text'] for s, i in unit.get('textRefs', [])]
        label = html.escape(unit['purpose'] + '。' + ' '.join(lines), quote=True)
        _, _, w, h = unit['crop']
        # Limit decoded display surfaces to 2x the maximum reader width.
        cw = min(w, round(960 * unit['widthPercent'] / 100))
        ch = round(h * cw / w)
        out.append(f'<figure class="beat {unit["align"]}" id="{unit["id"]}" style="--width:{unit["widthPercent"]}%"><canvas width="{cw}" height="{ch}" style="aspect-ratio:{w}/{h}" role="img" aria-label="{label}" data-source="{unit["sourceId"]}" data-crop="{",".join(map(str,unit["crop"]))}"></canvas></figure><div class="pause" aria-hidden="true" style="--pause:{unit["pause"]/390*100:.10f}cqw"></div>')
        storyboard += [f'## {unit["id"]}', '', unit['purpose'], '', f'表示幅 {unit["widthPercent"]}% / {unit["align"]} / 次の間 {unit["pause"]}px（390px幅） / 表示窓 {unit["crop"]}', '', *lines, '']
    out.append('<footer>第1話 おわり<br><a href="../chapters.html">話一覧</a><a href="../episode-02/index.html">第2話へ</a></footer></main><p class="error" id="render-error" hidden>画像を読み込めませんでした。ファイル一式をそろえて開き直してください。</p><noscript><p>このリーダーはJavaScriptを使用します。全編PNG版も同梱しています。</p></noscript><div id="artwork-pool" hidden aria-hidden="true">')
    for source in sources:
        out.append(f'<img id="source-{source["id"]}" src="art/{source["file"]}" width="{source["width"]}" height="{source["height"]}" alt="">')
    out.append('</div><script>\n' + READER_JS + '\n</script></html>')
    (DIRECTORY / 'index.html').write_text(''.join(out))
    (DIRECTORY / 'storyboard.md').write_text('\n'.join(storyboard))
    log = json.loads((DIRECTORY / 'generation-log.json').read_text())
    log['scrollEdition'] = plan['edition']
    log['scrollSources'] = [json.loads((REPO / s['record']).read_text()) for s in sources if s.get('record')]
    dump(DIRECTORY / 'generation-log.json', log)
    prompts = ['\n# 余白・スクロール改稿の実行指示', '', '表示窓と間の設計は production/episode-01-scroll/plan.json。新規生成・編集7枚と採用例の原画3枚を使用。旧原画は参照・実行履歴に必要な制作資料として保持。', '']
    for record in log['scrollSources']:
        prompts += ['## ' + record['file'], '', record['method'], '', '参照：' + json.dumps(record.get('references', record.get('source', [])), ensure_ascii=False), '', '```text', record.get('prompt', 'User-approved whitespace sample reused byte-for-byte.'), '```', '']
    with (DIRECTORY / 'PROMPTS.md').open('a') as f:
        f.write('\n'.join(prompts))
    previous = json.loads((DIRECTORY / 'validation.json').read_text())
    current_hash = sha(DIRECTORY / 'index.html')
    if previous.get('readerSourceSha256') != current_hash:
        previous.update(visualReview={'status':'pending'}, mobileBrowserReview={'status':'pending','note':'Native exports do not prove browser layout.'}, physicalDeviceTested=False)
    previous.update(edition=plan['edition'], readerSourceSha256=current_hash)
    dump(DIRECTORY / 'validation.json', previous)
    print(f'Adopted Episode 1 scroll staging: {len(plan["layout"]["units"])} display beats, {len(sources)} unique PNG sources')


READER_JS = r"""(async()=>{
  try {
    // Decode each shared source once, then draw every window that uses it.
    for (const source of document.querySelectorAll('#artwork-pool img')) {
      await source.decode();
      const id=source.id.slice(7);
      for (const canvas of document.querySelectorAll('.beat canvas')) {
        if(canvas.dataset.source!==id) continue;
        const crop=canvas.dataset.crop.split(',').map(Number);
        const context=canvas.getContext('2d');
        context.drawImage(source,...crop,0,0,canvas.width,canvas.height);
      }
      source.removeAttribute('src');
    }
    document.getElementById('artwork-pool').remove();
    document.documentElement.dataset.readerReady='true';
  } catch(error) {
    document.getElementById('render-error').hidden=false;
    document.documentElement.dataset.readerReady='error';
  }
})();"""
