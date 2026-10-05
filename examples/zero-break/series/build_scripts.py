from pathlib import Path
import json, html, re
root=Path(__file__).resolve().parent
rows=[]
for row in (root/'episodes.tsv').read_text().splitlines():
    fields=row.split('\t')
    assert len(fields)==8, (fields[0],len(fields))
    n=int(fields[0]); title=fields[1]; scenes=fields[2:]
    arc=(n-1)//10+1
    output=[f'# 第{n:02d}話 {title}', '', f'全50話 / 第{arc}部 / 脚本完成・'+('パイロット作画完成' if n==1 else '作画未制作'), '',
            '6場面の短編縦読み脚本。各場面の句点で示す動作・反応を2〜3カットに分け、約12〜18コマとして作画する。セリフは括弧内の話者の発言を縦書きの吹き出しに入れ、作画と一緒に生成する。説明文は原則として絵で見せる。', '',
            '## 場面脚本', '']
    for i, scene in enumerate(scenes,1):
        parts=[p+'。' for p in scene.split('。') if p]
        if len(parts)>1:
            cuts=[parts[0], ''.join(parts[1:])]
        else: cuts=[scene]
        if i==5:
            direction='大きな成功・新情報の絵で止まる。変身回は枠なしの縦構図。結果を直前の小コマで先に見せない。'
        elif i==6:
            direction='最後の情報を一段下で見せる。前半の快感を打ち消すだけの引きにせず、次の目的を残す。50話では引きを作らず余韻で閉じる。'
        elif i==4:
            direction='選択の顔、実行の手元、結果の順。必要な場面だけ音を先に置き、結果前に無言の間を確保。'
        elif i==1:
            direction='具体的な違和感か前話の結果から始める。状況説明の長文を背景へ載せない。'
        elif i==2:
            direction='会話は顔の反応と小道具を近いコマで交互に見せる。対立の原因をひとつに絞る。'
        else:
            direction='危機の全景から救助対象の手・顔へ寄る。危険な位置と安全な位置を描き分ける。'
        output += [f'### 場面{i}', '', scene, '', '**作画カット**', '']
        output += [f'{k}. {c}' for k,c in enumerate(cuts,1)]
        output += ['', f'**スクロール演出**：{direction}', '']
    output += ['## 連続性', '', '人物・フォーム・能力の制約は [bible.md](../bible.md) を参照。前場面の負傷、疲労、衣服、小道具をリセットしない。救出した人物は次の場面で危険位置へ戻さない。', '',
               '## 作画時の確認', '', '顔・手・受け渡しを目視。日本語は縦書き。セリフ・吹き出し・作画を一緒に生成し、全文と話者を目視確認する。390×844と360×800の実表示幅で、画像読み込み、文字、横あふれ、必要な見せ順、間を確認する。', '']
    if n == 1:
        output += ['## 第1話の詳細構成', '', '完成版 v5は30場面を描く。騎士が近づく距離と歩行、測定器までの誘導、手を置く前の迷い、接触と待つ時間、ゼロの結果と本人の反応を別々のコマへ分ける。上記6場面は章のまとまりであり、固定の6コマではない。', '', '[詳細絵コンテ](../../v5/storyboard.md) / [完成版を読む](../../v5/index.html)', '']
    slug=f'{n:02d}.md'
    (root/'episodes'/slug).write_text('\n'.join(output))
    rows.append({'episode':n,'title':title,'arc':arc,'script':'episodes/'+slug,'script_status':'complete','art_status':'pilot_complete' if n==1 else 'not_started','scenes':scenes})
assert [r['episode'] for r in rows]==list(range(1,51))
(root/'episodes.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
md=['# 全50話 脚本目次','', '全50話の場面脚本が完成。第1話のみパイロット作画済み、2〜50話の作画は未制作。','', '[全話をブラウザで読む](index.html) / [制作設定と伏線台帳](bible.md) / [第1話の縦読み](../v5/index.html)','']
for arc in range(1,6):
    md += [f'## 第{arc}部', '']
    md += [f'- [第{r["episode"]:02d}話 {r["title"]}]({r["script"]})' for r in rows if r['arc']==arc]
    md += ['']
(root/'README.md').write_text('\n'.join(md))
options=''.join(f'<option value="e{r["episode"]}">第{r["episode"]}話 {html.escape(r["title"])}</option>' for r in rows)
body=''
for r in rows:
    body+=f'<article id="e{r["episode"]}"><p class="tag">第{r["arc"]}部 · 脚本完成 · '+('第1話パイロット作画済み' if r['episode']==1 else '作画未制作')+f'</p><h2>第{r["episode"]}話 {html.escape(r["title"])}</h2>'
    for i,s in enumerate(r['scenes'],1):body+=f'<section><h3>場面{i}</h3><p>{html.escape(s)}</p></section>'
    body+='</article>'
(root/'index.html').write_text('''<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ゼロ・ブレイク 全50話脚本</title><style>*{box-sizing:border-box}body{margin:0;background:#0b1527;color:#edfaff;font-family:system-ui,sans-serif;line-height:1.9}main{max-width:760px;margin:auto;padding:24px}h1{color:#7be9ff}h2{line-height:1.6}nav{position:sticky;top:0;background:#14263e;padding:12px;z-index:2}select{max-width:100%;width:100%;font-size:17px;padding:10px}article{scroll-margin-top:90px;padding:45px 0;border-bottom:1px solid #34516a}section{padding:8px 16px;margin:12px 0;background:#13243b;border-radius:8px}p{font-size:18px;overflow-wrap:anywhere}.tag{font-size:13px;color:#8accdf}a{color:#8ce5ff}</style><main><h1>ゼロ・ブレイク</h1><p>全50話・完結脚本。各話6場面の短編連載。<br>第1話のみ作画済み。2〜50話の作画は未制作。</p><p><a href="../v5/index.html">第1話を縦読みで読む</a></p><nav><select aria-label="話を選ぶ" onchange="document.getElementById(this.value).scrollIntoView()">'''+options+'</select></nav>'+body+'</main></html>')
print('50 scripts generated; 300 story scenes; 49 episodes not illustrated')
