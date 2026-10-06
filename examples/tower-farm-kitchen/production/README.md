# 再制作と検証

`episodes.json` は導入10話の場面順とセリフの正本。`build.py prepare` は採用画像・編集記録・時刻表示を保ち、絵コンテと生成指示一覧を更新する。人物・場所・文字基準は `references` に置く。過去の生成へ渡した指示は書き換えず、変更は新しい生成記録へ残す。

1. `python3 examples/tower-farm-kitchen/production/build.py prepare` で絵コンテを整える。
2. 組み込み image_gen へ実際の指示と参照原画を渡す。`record_generation.py SOURCE TARGET [REFERENCE ...]` は原画を変更せず、指示・参照・SHA-256を記録する。
3. `adopt_edits.py 話数:場面ID:採用ファイル名` で修正を選び、`build.py 話数` で同じ原画をリーダーへ内包する。
4. `node examples/tower-farm-kitchen/production/render.cjs 話数` で390×844・360×800を全長スクロールし、各幅の確認シートを読む。
5. 実際に読めた画像だけ `validation.json` と採用した生成記録へ確認結果を記入し、`update_index.py` と `python3 scripts/sync_ios_webtoons.py` を実行する。

描画スクリプトには Playwright とブラウザーが必要。既存の実行環境を使い、`WEBTOON_PLAYWRIGHT_MODULE` でモジュールのパス、`WEBTOON_CHROME` でブラウザー実行ファイルを指定できる。macOSの標準Chromeがある場合は自動で使う。描画をやり直すと目視確認は未確認に戻る。HTMLの文字サイズ測定は原画内の縦書き文字の判定には使えない。

原画を更新したら必ず該当話の両幅で再確認する。採用外の画像は、記録された修正に必要な参照原画だけを `generation/inputs` へ置き、各生成記録の相対参照も更新する。別の公開版や旧リーダーを残さない。リーダーの画像は各話の `manifest.json` に並ぶ八枚だけ。

現在の結果は [delivery.json](delivery.json) と [制作台帳](status.md)。ローカルでは11件のPythonテスト、iOS同期チェック、五つのSwiftカタログ・読書テストを実行。CIとレビューは [PR #27](https://github.com/quantum-box/manga/pull/27) の最新HEADを確認する。
