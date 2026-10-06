# 塔を灯す剣

[第1話から読む](episode-01/index.html) · [第1〜10話の一覧](chapters.html)

VRMMORPG《星環の塔 ONLINE》を舞台に、自分の作った剣で塔の頂上を目指すカイと、盾役のセナ、魔法使いのイリスを描く初稿。剣と魔法の王道の冒険に、有限の部品で作る装備、試験、連携、共同工房を組み込む。

## 制作範囲

第1〜10話は全40場面の完成作画。台詞と縦書きの吹き出しを原画に一体生成し、160の脚本上の動作・理解・反応を大小のコマへ分けた。各話の `index.html` は画像参照式、`reader.html` は画像を内包した単一HTML。`webtoon-390.jpg` と `webtoon-360.jpg` はブラウザー表示から保存した全長画像。

200話以上の指定に対し、[240話の全体構成](series/roadmap.md)を12アークで仮設計。第11〜240話は長期構想であり、完成作画や各話の詳細脚本ではない。作品名と人物・展開は初案で、ユーザーの採用確認はまだ行っていない。

## 設定と制作資料

1. [作品の核と全体方針](series/bible.md)
2. [ゲームの世界とルール](series/world.md)・[人物](series/characters.md)
3. [実装を想像できる技術設計](series/technical-design.md)：架空ゲームの設計案と一次資料。ゲーム自体を実装・性能検証した成果ではない。
4. [導入10話](series/opening-arc.md)・[連続性](series/continuity.md)
5. [制作状態](production/status.md)：各話の `storyboard.md`、実使用 `PROMPTS-USED.md`、原画、採用画像のハッシュ、局所修正、スマホ検証を記録。

## 確認と再構築

390×844・360×800 CSS pxで全話の画像読み込み、横はみ出し、画像内の縦書き、話者、所持品、場面の順を確認。これはブラウザーでの確認であり、物理スマートフォンやiOS実機の確認ではない。

```sh
python3 examples/tower-forge/production/build.py
python3 examples/tower-forge/production/verify.py
python3 scripts/sync_ios_webtoons.py
python3 scripts/sync_ios_webtoons.py --check
```

組み込み image_gen の原本を保存し、必要な修正だけ編集機能で作った。採用画像は `production/adopted-assets.json`、原本は `production/asset-provenance.json`、修正の正確な指示は `production/repairs.json`。画像生成を再実行せずにリーダーを再構築できる。原本は採用版の編集元として残し、旧話版のリーダーは併存させない。

ローカルのカタログとiOS同梱データへ収録。配信サーバーへの公開、TestFlight配布、GitHubへの公開は実施していない。
