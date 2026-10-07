# 再制作と検証

`episodes.json` は導入10話の場面順とセリフの正本。`build.py prepare` は採用画像・編集記録・時刻表示を保ち、絵コンテと生成指示一覧を更新する。人物・場所・文字基準は `references` に置く。過去の生成へ渡した指示は書き換えず、変更は新しい生成記録へ残す。

1. `python3 examples/tower-farm-kitchen/production/build.py prepare` で絵コンテを整える。
2. 組み込み image_gen へ実際の指示と参照原画を渡す。`record_generation.py SOURCE TARGET [REFERENCE ...]` は原画を変更せず、指示・参照・SHA-256を記録する。
3. `adopt_edits.py 話数:場面ID:採用ファイル名` で修正を選び、`build.py 話数` で同じ原画をリーダーへ内包する。
4. `node examples/tower-farm-kitchen/production/render.cjs 話数` で390×844・360×800を全長スクロールし、各幅の確認シートを読む。
5. 実際に読めた画像だけ `validation.json` と採用した生成記録へ確認結果を記入し、`update_index.py` と `python3 scripts/sync_ios_webtoons.py` を実行する。

描画スクリプトには Playwright とブラウザーが必要。既存の実行環境を使い、`WEBTOON_PLAYWRIGHT_MODULE` でモジュールのパス、`WEBTOON_CHROME` でブラウザー実行ファイルを指定できる。macOSの標準Chromeがある場合は自動で使う。描画をやり直すと目視確認は未確認に戻る。HTMLの文字サイズ測定は原画内の縦書き文字の判定には使えない。

原画を更新したら必ず該当話の両幅で再確認する。採用外の画像は、記録された修正に必要な参照原画だけを `generation/inputs` へ置き、各生成記録の相対参照も更新する。別の公開版や旧リーダーを残さない。リーダーの画像は各話の `manifest.json` に並ぶ採用原画だけ（第1話40枚、第2〜10話は各8枚）。

現在の結果は [delivery.json](delivery.json) と [制作台帳](status.md)。ローカルでは11件の配布物Pythonテストと4件の原画格納テスト、iOS同期チェック、Swift読書コンテンツテスト（ほか四組は先行コミットで確認済み）を実行。CIとレビューは [PR #27](https://github.com/quantum-box/manga/pull/27) の最新HEADを確認する。

第1話の長尺改稿は [episode-01-scroll.json](episode-01-scroll.json) と [episode-01-review.md](episode-01-review.md)。通常版は原画PNGを直接読む。内包版が100MiBを超える場合は `compact_reader.py` がUTF-8の格納方式を使い、ブラウザーで元のPNGバイトを復元する。原画のリサイズ・再圧縮・文字の描き足しは行わない。描画スクリプトは復元した全原画のSHA-256と、通常版・単独版の全長一致も確認する。

今回の導入改稿は [episode-01-causality.json](episode-01-causality.json) に記録。格納後も100MiBを超える第1話では`reader.html`と三個の`reader-art-*.js`を同じフォルダーで使う。一ファイルだけをコピーした単独版ではない。iOS同梱版は`index.html`と原画を同期する。
