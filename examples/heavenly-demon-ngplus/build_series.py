#!/usr/bin/env python3
"""Build finished NG+ episodes without altering image originals."""
import argparse, hashlib, html, json, struct, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
TITLE="天魔、二周目。"
GAPS={2:[980,340],3:[240,690],4:[210,520],5:[900,470],6:[530,390],7:[460,530],8:[370,650],9:[640,540],10:[350,710]}
CSS="""*{box-sizing:border-box}html{background:#eceff2;color:#17222e;color-scheme:light}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Sans','Yu Gothic',sans-serif}.episode{width:100%;max-width:480px;margin:auto;background:white;container-type:inline-size}header{padding:32px 8% 42px}h1{font-family:'Yu Mincho',serif;font-size:clamp(36px,10cqw,48px);line-height:1.25;margin:12px 0 18px}h1 span{color:#a88130}.eyebrow,.hint{font-size:12px;color:#627d89;letter-spacing:.09em}.subtitle{font-size:17px;line-height:1.7;margin:0}.scene{margin:0;width:100%}.scene img{display:block;width:100%;height:auto}.pause{background:white;width:100%}footer{padding:65px 8%;text-align:center;border-top:1px solid #e1e8e9}footer p{font-size:19px;line-height:1.7}footer small{font-size:13px}.chapter-links{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:36px}a{color:#405969;text-underline-offset:4px}.chapter-links a{padding:12px 8px;min-height:44px}a:focus-visible{outline:3px solid #a88130;outline-offset:3px}"""
def esc(v):return html.escape(str(v),quote=True)
def chapters():
 return [{"number":1,"title":"処刑する相手、間違えてるぞ","reward":"生還、内功120年、飛燕歩"}]+[json.loads((ROOT/f"episode-{n:02d}/scene-script.json").read_text()) for n in range(2,11)]
def package(folder):
 subprocess.run([sys.executable,str(REPO/"skills/webtoon/scripts/package_reader.py"),str(folder/"index.html"),"--force"],check=True,capture_output=True)
def first_navigation():
 folder=ROOT/"episode-01";source=folder/"index.html";doc=source.read_text()
 if 'id="serial-chapter-links"' not in doc:
  nav='<nav id="serial-chapter-links" aria-label="話を移動" style="display:flex;justify-content:center;gap:24px;margin-top:32px;font-size:19px"><a style="color:#405969;padding:12px 0" href="../serial.html">話一覧</a><a style="color:#405969;padding:12px 0" href="../episode-02/index.html">第2話 →</a></nav>'
  source.write_text(doc.replace('</footer>',nav+'</footer>'));package(folder)
def build(ch,all_ch):
 n=ch["number"];folder=ROOT/f"episode-{n:02d}"
 content=[];artwork=[];board=[f"# {TITLE} 第{n}話 {ch['title']}\n\nこの話で得るものは{ch['reward']}。\n\n各場面4コマ、全12コマ。原画内の会話は縦書き。上から下、列は右から左。発話ごとの全文と話者を以下に記録。"];prompts=[]
 for s in ch["scenes"]:
  i=s["number"];raw=(folder/f"art/{i:02d}.png").read_bytes()
  if raw[:8]!=b"\x89PNG\r\n\x1a\n":raise ValueError("Not PNG")
  w,h=struct.unpack(">II",raw[16:24])
  alt=s["name"]+"。"+"".join(p.get("speaker","システム")+"「"+("。".join(p["system"]) if p.get("system") else p["text"])+"」。" for p in s["panels"])
  if i>1:content.append(f'<div class="pause" id="pause-{i}" style="height:{GAPS[n][i-2]/3.9:.4f}cqw" data-purpose="{esc(s["purpose"])}" aria-hidden="true"></div>')
  if s.get("transitionNarration"):
   words="<br>".join(esc(x) for x in s["transitionNarration"].split("\n"))
   content.append(f'<p class="transition" style="font-size:19px;line-height:1.9;padding:24px 8%;margin:0">{words}</p>')
  content.append(f'<figure class="scene" id="scene-{i}" data-vignettes="4"><img src="art/{i:02d}.png" width="{w}" height="{h}" alt="{esc(alt)}" decoding="sync"></figure>')
  artwork.append({"file":f"art/{i:02d}.png","width":w,"height":h,"sha256":hashlib.sha256(raw).hexdigest()})
  board.append(f"## 場面{i} {s['name']}\n\n間の役割　{s['purpose']}\n\n密度　小さな表情や手の接写と大きな動作・発見を混ぜる。後の場面の人物や結末を先出ししない。")
  if s.get("transitionNarration"):board.append("ナレーション　"+s["transitionNarration"])
  for j,p in enumerate(s["panels"],1):
   words=" / ".join(p["system"]) if p.get("system") else p["text"]
   board.append(f"### コマ{(i-1)*4+j}\n\n作画　{p['art']}\n\n{p.get('speaker','システム')}　{words}")
  prov=json.loads((folder/f"provenance-{i:02d}.json").read_text())
  prompts.append(f"## 場面{i} {s['name']}\n\n原本 {prov['original']}\n\n採用 {prov['adopted']}\n\n~~~text\n{prov['prompt']}\n~~~")
 links=[f'<a href="../episode-{n-1:02d}/index.html">← 第{n-1}話</a>','<a href="../serial.html">話一覧</a>']
 if n<10:links.append(f'<a href="../episode-{n+1:02d}/index.html">第{n+1}話 →</a>')
 ending="第一部 完" if n==10 else f"次回「{all_ch[n]['title']}」"
 doc=f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#ffffff"><title>{esc(TITLE)} 第{n}話 {esc(ch["title"])}</title><link rel="stylesheet" href="reader.css"></head><body><main class="episode"><header><p class="eyebrow">武侠 × 異世界転生 × 強くてニューゲーム</p><h1>天魔、<br><span>二周目。</span></h1><p class="subtitle">第{n}話　{esc(ch["title"])}</p><p class="hint">下へスクロール ↓</p></header>{"".join(content)}<div class="pause" style="height:65cqw" aria-hidden="true" data-purpose="余韻から次話へ"></div><footer><p>第{n}話 完</p><p>{esc(ending)}</p><nav class="chapter-links" aria-label="話を移動">{"".join(links)}</nav><small>{esc(TITLE)} ／ ORIGINAL WEBTOON</small></footer></main></body></html>'
 (folder/"reader.css").write_text(CSS);(folder/"index.html").write_text(doc)
 (folder/"storyboard.md").write_text("\n\n".join(board));(folder/"PROMPTS.md").write_text("\n".join(line.rstrip() for line in "\n\n".join(prompts).splitlines())+"\n")
 manifest={"title":TITLE,"chapter":n,"subtitle":ch["title"],"artwork":artwork,"generatedOriginals":3,"vignettes":12,"lettering":"vertical Japanese dialogue in image originals","readingTimeMeasured":False,"protectedReveal":{"cue":"scene-1","answer":"scene-2"} if n==2 else None}
 for name in ["episode.json","manifest.json"]:(folder/name).write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 package(folder);print(f"Built episode {n}: 3 originals, 12 vignettes, embedded reader")
def serial(all_ch):
 rows="".join(f'<li><a href="episode-{c["number"]:02d}/index.html">第{c["number"]}話　{esc(c["title"])}</a></li>' for c in all_ch)
 style="*{box-sizing:border-box}body{margin:0;background:#eceff2;color:#17222e;font-family:-apple-system,BlinkMacSystemFont,'Yu Gothic',sans-serif}main{max-width:480px;margin:auto;background:white;min-height:100vh}header{padding:42px 8% 28px}h1{font-family:'Yu Mincho',serif;font-size:40px;line-height:1.25}h1 span{color:#a88130}p{font-size:17px;line-height:1.8}ol{list-style:none;margin:0;padding:0 8% 48px}li{border-top:1px solid #e0e8ea}a{display:block;color:#314b57;text-decoration:none;padding:22px 0;line-height:1.7;font-size:17px}a:focus-visible{outline:3px solid #a88130}"
 doc=f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE} 第1〜10話</title><style>{style}</style></head><body><main><header><p>武侠 × 異世界転生 × 強くてニューゲーム</p><h1>天魔、<br><span>二周目。</span></h1><p>レベル999でも、死ぬのは怖い。<br>生きて帰るための二周目、全10話。</p></header><ol>{rows}</ol></main></body></html>'
 (ROOT/"serial.html").write_text(doc)
 plan={"title":TITLE,"chapters":[{k:c[k] for k in ["number","title","reward"]} for c in all_ch],"principle":"LV.999の身体と学生本人の恐怖・理解・選択を分ける。弱体化や修行で引き延ばさない。"}
 (ROOT/"series-plan.json").write_text(json.dumps(plan,ensure_ascii=False,indent=2)+"\n")
def main():
 p=argparse.ArgumentParser();p.add_argument("--episode",type=int,action="append");args=p.parse_args();all_ch=chapters()
 first_navigation()
 for ch in all_ch[1:]:
  if not args.episode or ch["number"] in args.episode:build(ch,all_ch)
 serial(all_ch)
if __name__=="__main__":main()
