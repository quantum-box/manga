# 転生したら柴犬だった。 全10話 再制作版

[全10話を続けて読む](all.html) · [話一覧](chapters.html) · [第1話](episode-01/index.html)

各話が短かったため、全10話を各10枚・約40コマへ作り直した。採用作画は100枚。前版の40枚から2.5倍へ増やし、身体の戸惑い、助けを伝える失敗、同行する理由、旅の疲れ、狼や魔王への恐怖、練習と協力、村へ水が届いた結果を順に描く。第3話の「おて」が第10話の自発的な握手につながる。

日本語の縦書き台詞・吹き出し・絵は一体のラスター画像。HTMLで会話を重ねない。生成には同じキャラクター参照を使用し、物の受け渡し・水路の状態・登場順を確認して必要な画像を修正した。

## 読む・保存する

話一覧から各話へ進み、末尾で前後の話へ移動できる。各話 reader.html は画像・CSSを内包した単独ファイル。all.html は全100枚を連続して読むリーダー。episode-01/webtoon-390.jpg などはブラウザで書き出した完成画像。

## 制作資料

[シリーズ設定](series-bible.md)、[連続性](continuity.md)、[全話の絵コンテ・台詞計画](production/plan.json)、[実際の生成記録](production/generation-records.json)、[修正記録](production/issues.json)。各話 storyboard.md / scenes.json / PROMPTS.md に読む順番、間、採用画像のSHA256、元の生成指示と編集指示を記録する。

原画PNGとその修正元は採用版の制作資料。配布には同じ寸法のWebPを使用し、Web・単独リーダー・iOS同梱の採用画像をバイトで照合する。旧版の本文・リーダー・配布物はGitの履歴で管理し、共有の人物参照は ../references/ に保持する。

## 確認と再出力

各話 validation.json は390×844・360×800の実測幅、全長、読み込み、話移動を記録する。360pxの全100枚で日本語・話者・人物と物の連続性を目視確認した。文字高は概ね19〜28pxの目視見積り。実機確認・本番公開は未実施。

Pillowが使えるPythonで `python production/build.py`。PlaywrightとChromiumが使える環境で `node production/validate.cjs`。必要に応じて `CHROMIUM_EXECUTABLE_PATH` を設定する。リポジトリ直下で `python scripts/sync_ios_webtoons.py` によりiOSへ同梱し、`--check` で照合する。
