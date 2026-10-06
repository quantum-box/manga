"""Build fifty scripts with explicit panel, voice, reaction and frame staging."""
from pathlib import Path
import html,json,re
from panel_staging import stage_episode,NOTES
ROOT=Path(__file__).resolve().parent
PROGRESS='全50話のコマ別脚本を更新。第1〜10話は改稿原画あり（ブラウザ再確認待ち）。第11〜50話は脚本のみ・作画未制作。'
def adopted(n):
 d=ROOT.parent/('v5' if n==1 else f'episode-{n:02d}')
 m=json.loads((d/'manifest.json').read_text());assert m['version']=='context-dialogue-v6'
 groups=[]
 for s in m['shots']:
  panels=s.get('panels') or [dict(beat=s.get('alt_ja',s['scene']),focus=s.get('alt_ja',s['scene']),frame=f'幅{s["widthPercent"]}%・{s["shape"]}・採用原画の一コマ',voice='採用原画内の吹き出し',lines=s['lines'])]
  groups.append(dict(asset=s['file'],context=s['scene'],panels=panels,visible_text=s.get('visible_text',[])))
 return groups
def describe(p):
 lines=[p['line']] if p.get('line') else p.get('lines',[])
 return p['beat']+' / 注目：'+p.get('focus',p.get('view','対象'))+' / 枠：'+p['frame']+' / 声：'+p.get('voice','無言')+' / '+' / '.join(l['speaker']+'：'+l['text'] for l in lines).rstrip(' /')
rows=[]
for raw in (ROOT/'episodes.tsv').read_text().splitlines():
 f=raw.split('\t');assert len(f)==8
 n=int(f[0]);title=f[1];scenes=f[2:];arc=(n-1)//10+1
 groups=adopted(n) if n<=10 else stage_episode(n,scenes)
 count=sum(len(g['panels']) for g in groups)
 if n>10:
  original=''.join(re.findall('「([^」]*)」',''.join(scenes)))
  actual=''.join(p['line']['text'] for g in groups for p in g['panels'] if p.get('line'))
  assert original==actual,(n,original,actual)
 status='改稿原画あり・ブラウザ再確認待ち' if n<=10 else '脚本のみ・作画未制作'
 out=[f'# 第{n:02d}話 {title}','',f'全50話 / 第{arc}部 / コマ別脚本更新 / {status}','',f'{count}コマ。6場面は物語の章。コマ数は固定せず、発言、受け手、手元、結果を順に描く。幅・高さ・左右位置と吹き出しの輪郭を、声と読ませる時間に合わせて変える。','','## 場面脚本','']
 for i,s in enumerate(scenes,1):out += [f'### 場面{i}','',s,'']
 out+=['## コマ別の構成','']
 if n>10:out+=['**この話の接続と見せ順**：'+NOTES[n],'']
 idx=0
 for g in groups:
  label=g['asset'] if n<=10 else f'場面{g["scene"]}'
  out += ['### '+label,'',g['context'],'']
  for p in g['panels']:
   idx+=1
   out += [f'#### コマ{idx}','',describe(p),'']
   if p.get('pause') is not None:out += [f'次までの間：390px幅で{p["pause"]}px相当（作画後に調整）。','']
  out += ['画面内資料：'+t['text'] for t in g.get('visible_text',[])]+['']
 if n<=10:
  name='v5' if n==1 else f'episode-{n:02d}'
  out += [f'[採用原画と絵コンテ](../../{name}/storyboard.md) / [縦読み](../../{name}/index.html)','']
 out+=['## 作画と確認','','人物・フォーム・能力・伏線は [bible.md](../bible.md)。負傷、疲労、服、小道具、救助済みの位置を前コマから保つ。発話の尾は口へ、思考の点は頭へ、資料には尾を付けない。文字・吹き出し・絵は一緒に生成し、HTMLへ二重に重ねない。','','360×800 / 390×844の表示幅で全文・話者・手・顔・因果と間を確認。原画、ネイティブ画像書き出し、ブラウザ、実機の結果は別々に記録。11〜50話の作画指示は、作画後の目視確認を代替しない。','']
 script=f'episodes/{n:02d}.md';(ROOT/script).write_text('\n'.join(out))
 rows.append(dict(episode=n,title=title,arc=arc,script=script,script_status='staged',art_status='revised_art_browser_pending' if n<=10 else 'not_started',panel_count=count,scenes=scenes,panel_staging=groups,continuity_notes=NOTES.get(n,'採用原画の絵コンテ・生成記録を参照。')))
assert [r['episode'] for r in rows]==list(range(1,51))
(ROOT/'episodes.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
md=['# 全50話 コマ別脚本目次','',PROGRESS,'','[脚本とコマ構成](index.html) / [設定と伏線](bible.md) / [第1〜10話の縦読み](../chapters.html)','']
for arc in range(1,6):
 md += [f'## 第{arc}部','']+[f'- [第{r["episode"]:02d}話 {r["title"]}]({r["script"]}) — {r["panel_count"]}コマ' for r in rows if r['arc']==arc]+['']
(ROOT/'README.md').write_text('\n'.join(md))
options=''.join(f'<option value="e{r["episode"]}">第{r["episode"]}話 {html.escape(r["title"])}</option>' for r in rows)
articles=[]
for r in rows:
 status='改稿原画あり・ブラウザ再確認待ち' if r['episode']<=10 else '脚本のみ・作画未制作'
 body=[f'<article id="e{r["episode"]}"><p class="tag">第{r["arc"]}部 · {status} · {r["panel_count"]}コマ</p><h2>第{r["episode"]}話 {html.escape(r["title"])}</h2>']
 for i,s in enumerate(r['scenes'],1):body.append(f'<section><h3>場面{i}</h3><p>{html.escape(s)}</p></section>')
 body.append('<details><summary>コマ別の構成を見る</summary>')
 body += ['<section>'+''.join('<p>'+html.escape(describe(p))+'</p>' for p in g['panels'])+'</section>' for g in r['panel_staging']]
 body.append('</details></article>');articles.append(''.join(body))
css='*{box-sizing:border-box}body{margin:0;background:#0b1527;color:#edfaff;font-family:system-ui,sans-serif;line-height:1.9}main{max-width:760px;margin:auto;padding:24px}h1{color:#7be9ff}h2{line-height:1.6}nav{position:sticky;top:0;background:#14263e;padding:12px;z-index:2}select{width:100%;max-width:100%;font-size:17px;padding:10px}article{scroll-margin-top:90px;padding:45px 0;border-bottom:1px solid #34516a}section{padding:8px 16px;margin:12px 0;background:#13243b;border-radius:8px}p{font-size:18px;overflow-wrap:anywhere}.tag{font-size:13px;color:#8accdf}a{color:#8ce5ff}summary{cursor:pointer;padding:12px}'
(ROOT/'index.html').write_text('<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ゼロ・ブレイク 全50話脚本</title><style>'+css+'</style><main><h1>ゼロ・ブレイク</h1><p>'+html.escape(PROGRESS)+'</p><p><a href="../chapters.html">第1〜10話を読む</a></p><nav><select aria-label="話を選ぶ" onchange="document.getElementById(this.value).scrollIntoView()">'+options+'</select></nav>'+''.join(articles)+'</main></html>')
print('Updated 50 scripts; illustrated panels:',sum(r['panel_count'] for r in rows[:10]),'; future staged panels:',sum(r['panel_count'] for r in rows[10:]))
