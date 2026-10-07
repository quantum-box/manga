# 再制作と検証

`episodes.json` は導入10話の場面順とセリフの正本。`build.py prepare` は採用画像・編集記録・時刻表示を保ち、絵コンテと生成指示一覧を更新する。人物・場所・文字基準は `references` に置く。過去の生成へ渡した指示は書き換えず、変更は新しい生成記録へ残す。

1. `python3 examples/tower-farm-kitchen/production/build.py prepare` で絵コンテを整える。
2. 組み込み image_gen へ実際の指示と参照原画を渡す。`record_generation.py SOURCE TARGET [REFERENCE ...]` は原画を変更せず、指示・参照・SHA-256を記録する。
3. `adopt_edits.py 話数:場面ID:採用ファイル名` で修正を選び、`build.py 話数` で同じ原画をリーダーへ内包する。
4. `node examples/tower-farm-kitchen/production/render.cjs 話数` で390×844・360×800を全長スクロールし、各幅の確認シートを読む。
5. 実際に読めた画像だけ `validation.json` と採用した生成記録へ確認結果を記入し、`update_index.py` と `python3 scripts/sync_ios_webtoons.py` を実行する。

描画スクリプトには Playwright とブラウザーが必要。既存の実行環境を使い、`WEBTOON_PLAYWRIGHT_MODULE` でモジュールのパス、`WEBTOON_CHROME` でブラウザー実行ファイルを指定できる。macOSの標準Chromeがある場合は自動で使う。描画をやり直すと目視確認は未確認に戻る。HTMLの文字サイズ測定は原画内の縦書き文字の判定には使えない。

全長PNGは実際のスマホ画面を順に撮り、Sharpで表示画素をそのまま連結する。32,768pxを超えるChromeの一括キャプチャで後半が冒頭へ巻き戻る問題を避け、全ての画面と連結後の画素一致を確認する。原画は編集しない。SharpはPlaywrightと同じランタイムから解決し、別配置なら`WEBTOON_SHARP_MODULE`で指定する。

原画を更新したら必ず該当話の両幅で再確認する。採用外の画像は、記録された修正に必要な参照原画だけを `generation/inputs` へ置き、各生成記録の相対参照も更新する。別の公開版や旧リーダーを残さない。リーダーの画像は各話の `manifest.json` に並ぶ採用原画だけ（第1話40枚、第2話9枚、第3〜10話は各8枚）。

現在の結果は [delivery.json](delivery.json) と [制作台帳](status.md)。第2〜10話の改稿手順・確認範囲・境界判断は [remake/review.md](remake/review.md)。CIとレビューは続編改稿PRの最新HEADを確認する。

第1話の長尺改稿は [episode-01-scroll.json](episode-01-scroll.json) と [episode-01-review.md](episode-01-review.md)。通常版は原画PNGを直接読む。内包版が100MiBを超える場合は `compact_reader.py` がUTF-8の格納方式を使い、ブラウザーで元のPNGバイトを復元する。原画のリサイズ・再圧縮・文字の描き足しは行わない。描画スクリプトは復元した全原画のSHA-256と、通常版・単独版の全長一致も確認する。

今回の導入改稿は [episode-01-causality.json](episode-01-causality.json) に記録。格納後も100MiBを超える第1話では`reader.html`と三個の`reader-art-*.js`を同じフォルダーで使う。一ファイルだけをコピーした単独版ではない。iOS同梱版は`index.html`と原画を同期する。

料理の改稿は [episode-01-food.json](episode-01-food.json) に記録。第1話の調理・配膳・ひと口の3原画を、なめらかな煮汁と読みやすい具の形で揃えた。粒の密集を避ける基準は [food-art.md](../series/food-art.md) と新規作画用の共通プロンプトへ反映。過去に実行した指示は保存し、採用原画をリサイズ・再圧縮しない。

## 第2〜10話の全編改稿

`remake/episodes.json` と `remake/windows.json` に、採用した場面・会話・表示窓・余白を保存。`remake/package.py 2 ... 10` で包装し、`remake/render.cjs 2 ... 10` で両スマホ幅を確認する。メインの `build.py 話数` も改稿版へ振り分ける。画像は各話の `art/*remake*.png`、実際の指示と無加工SHA-256は `generation/*remake*`。再包装は原画を変更しない。

単独HTMLは原画を一度だけ格納し、同じ原画を使う表示窓に共通のBlob URLを渡す。JavaScriptを使う。通常の `index.html` はPNGとCSSで読める。両者の高さ・原画バイト・全長キャプチャの画素一致を検証する。検証用レビューHTMLの参照も相対パスで、別のチェックアウトで読める。
