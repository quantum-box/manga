"""Refresh delivery documentation from the verified adopted artifacts."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
STATE = Path(__file__).resolve().parent
def read(path): return json.loads(path.read_text())
def write(path, value): path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
report = read(ROOT/'production/feedback-v6/artifact-verification.json')
assert report['status']=='passed_artifact_checks' and report['webtoon_remake_records']==166
chapters = []
for n in range(1,11):
    d = ROOT/('v5' if n==1 else f'episode-{n:02d}')
    m = read(d/'manifest.json')
    delivery = read(d/'delivery-validation.json')
    raster = read(d/'raster-export-validation.json')
    row = dict(episode=n, assets=len(m['shots']), panels=m['panel_count'],
               readerSha256=delivery['readerSha256'], archiveSha256=delivery['archiveSha256'],
               archiveBytes=delivery['archiveBytes'], nativeReview=raster.get('visualReview'),
               browserReview='unchanged prior edition' if n==1 else 'pending',
               physicalDeviceTested=False)
    chapters.append(row)
    if n==1: continue
    assert m['remakeEdition']=='webtoon-remake-20261006'
    assert raster['visualReview']['status']=='passed'
    (d/'README.md').write_text(f"""# 第{n}話 {m['title']}

Webtoonスキルで全{len(m['shots'])}画像・{m['panel_count']}コマを再作画。

[縦読み](index.html) / [単体ZIP](reader.zip) / [絵コンテ](storyboard.md) / [実行指示](PROMPTS.md)

[390px幅の全長画像](complete-390.png) / [360px幅の全長画像](complete-360.png)

日本語の縦書き、吹き出し、効果音は原画と一緒に生成。横並びは比較と受け手、斜め枠は移動と衝撃、広いコマは位置関係と決断に使う。人物・服・手足・同じ小道具・支え続ける荷重・原因から結果の順を原寸と360/390px幅の全素材で目視確認済み。

実行した生成指示・修正指示・参照と修正前のハッシュは [今回の記録](../production/webtoon-remake/records/)。以前の原画は今回の参照入力として必要なものを保持し、採用リーダーとiOSには今回の原画だけを収録。旧配布物と旧検査画像はGitの履歴で管理。

全長画像と review/v6-contact-* はネイティブCanvasの書き出し。ブラウザと実機の確認は未実施。原画・埋め込みPNG・ZIPのCRCと展開HTML・iOS同梱版はバイト照合済み。検査状態は validation.json、raster-export-validation.json、delivery-validation.json。
""")
write(ROOT/'production/delivery-summary.json',dict(
    edition='webtoon-remake-20261006',status='passed_artifact_checks',
    completedArtworkEpisodes=list(range(1,11)),remadeEpisodes=list(range(2,11)),
    remadeArtworks=166,remadePanels=sum(c['panels'] for c in chapters[1:]),
    illustratedArtworks=report['totals']['reader_images'],illustratedPanels=report['totals']['panels'],
    scriptEpisodes=50,scriptOnlyEpisodes=list(range(11,51)),
    sourceAndEmbeddedAndIOSBytesMatch=True,browserPhoneReview=False,
    browserReview='pending for remade episodes 2-10',physicalDeviceTested=False,
    publication='not published; branch/PR delivery',chapters=chapters))
table=['|話|原画|コマ|原寸・360/390px|ブラウザ|','|---|---:|---:|---|---|']
table += [f'|{c["episode"]}|{c["assets"]}|{c["panels"]}|確認済み|未実施|' for c in chapters[1:]]
(STATE/'status.md').write_text('# 第2〜10話のWebtoon再作画\n\n依頼：2026-10-06「2話以降も全部webtoonスキルで作り直して」。作画済み全9話を再作画。第11〜50話は既存脚本のみ。\n\n全166枚・483コマ。原寸と360/390px幅の全素材を確認済み。原画、埋め込みPNG、ZIP、iOSと全50話の目次を照合済み。第1話は既存採用版を保持。\n\n'+'\n'.join(table)+'\n\n横並び・斜め枠・間、効果音、段階的な装着、機構の原因と結果を各話で再設計。第6話の17人照合、第7話の命令書と盾、第8話の救出と証拠、第9話の独立した呼吸装置、第10話の荷重と避難を接続して確認。新フォームと正体の公開順は保持。\n\n公開更新・ブラウザ・実機確認は未実施。実行指示は episode-*-plan.json と records、修正実行は episode-*-repairs*.json と採用記録。原画のPNGは一切加工していない。\n')
root=ROOT/'README.md'
text=root.read_text().replace('第1〜10話は199画像・324コマ','第1〜10話は199画像・556コマ')
for c in chapters[1:]:
    import re
    text=re.sub(r'(?m)^(\|'+str(c['episode'])+r'\|[^\n]*?\|)\d+ / \d+(\|[^\n]*)$',lambda m:m[1]+f'{c["assets"]} / {c["panels"]}'+m[2],text)
text=text.replace('新規生成54素材・承認見本の再利用3素材を採用。','第2〜10話の全166素材をWebtoonスキルで再作画。原寸と360/390px幅の全素材を確認。以前の会話改稿は新規生成54素材・承認見本再利用3素材の記録として保持。')
text=text.replace('[制作手順](production/README.md)', '[今回の再作画](production/webtoon-remake/status.md) / [制作手順](production/README.md)')
root.write_text(text)
print('Updated delivery documentation for 9 remade episodes')
