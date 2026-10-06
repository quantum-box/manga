# 改稿版 context-dialogue-v6 の再構築

第1〜10話の保存原画と実行記録からリーダーを再構築する。文字と吹き出しは原画内。既存PNGは変更しない。第11〜50話はコマ別脚本のみで、作画は未制作。

1. `python3 production/feedback_v6.py build 1`、`python3 production/build.py` でリーダー・絵コンテ・話一覧・実行指示を再構築する。
2. `node production/export_v6.cjs` で360/390px幅の全長画像・全素材一覧・連続窓を作る。`@napi-rs/canvas` が必要。HTMLを描画しないため、ブラウザ画面やDOMの証明にはならない。
3. `review/v6-contact-360-*.png` 全素材と390px幅の代表区間を読み、全文、話者、手、衣服、小道具、位置と因果を確認。確認したファイルと内容だけを各話の validation.json に記録する。
4. `python3 v5/package_delivery.py` と `python3 production/package_delivery.py` でZIPを作る。`python3 series/build_scripts.py` で全50話の脚本と目次を再構築。repoルートで `python3 scripts/sync_ios_webtoons.py` を実行する。
5. repoルートで `python3 examples/zero-break/production/verify_v6.py` と `python3 scripts/sync_ios_webtoons.py --check` を実行する。原画、参照、修正前、単体HTML、ZIP、書き出し、iOSを照合する。

原画生成・編集には組み込み image_gen を使う。`feedback_v6.py save` はPNGを変更せず保存し、`repair` は元を保持した兄弟ファイルへ修正を採用する。再利用にはその素材の以前の実行指示を残し、新規生成の指示と混同しない。

第1話の効果音改稿は `episode-01-sfx/records` に採用指示・元画像とハッシュを保存。`feedback_v6.py build 1` はこの記録を適用し、再構築時にも効果音を維持する。原画内の音は代替テキストと絵コンテにも記載。

`plan_feedback_v6.py` は今回の企画指示、`feedback-v6/records` は実際の実行記録。実行後に計画が変わっても、実行済みの指示を計画値で上書きしない。以前のmanifest・生成記録・プロンプトはGitの履歴で管理し、`history.py` が固定コミットから再構築の入力を直接読む。作業ツリーに旧版のコピーは作らない。履歴を省略したcloneでは、エラーに表示される `git fetch origin <コミット>` を実行してから再構築する。

ブラウザでの現行版再確認と実機確認は未実施。旧版の `check.cjs` は旧manifestを前提にした検査で、v6には使用しない。今回の環境ではローカルHTMLへのブラウザアクセスが制限されたため、別ブラウザ・localhost・直接CDPなどで迂回しない。ネイティブ画像の目視結果だけをブラウザ確認済みとして記録しない。
