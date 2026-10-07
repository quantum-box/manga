# ゼロブレイク：装着シーンの余白演出

「起動と手首 → 音だけ → システム通知だけ → 光だけ → 完成した全身」を読む短い試作。[単体リーダーZIP](reader.zip) を展開して `reader.html`、または [390px幅の完成画像](complete-390.png) を開く。

『ゼロブレイク』第1話の既存原画2枚と、新たに組み込み `image_gen` で生成した余白素材3枚を使用。漫画ページの外側に等間隔の空白を加える構成ではなく、音・通知・光を独立した表示単位にして、姿を見せる順を変えている。第1話の正式な採用版を置き換えるものではない。

2026-10-07、ユーザーが「上手くできてる」と評価し、Webtoonスキルへの収録を依頼。[スキルの採用例](../../../../skills/webtoon/references/whitespace-example.md)へ完成画像・連続した画面窓・作画指示を同梱している。

絵コンテは [storyboard.md](storyboard.md)、実行した指示は [PROMPTS.md](PROMPTS.md)、余白の長さとネイティブ画面窓は [layout.json](layout.json)、確認した範囲は [validation.json](validation.json)。

`node render.cjs` でHTML・360/390px完成画像・連続した画面窓を出力する（`@napi-rs/canvas` が必要）。原本PNGを加工せず、配置と縮小だけを出力へ反映する。`python3 ../../../../skills/webtoon/scripts/package_reader.py index.html --output reader.html --force` で単体リーダーを作る。

生成された `reader.html` はGit対象外とし、同一バイトのHTMLを `reader.zip` へ収録する。ZIPは原稿5枚を埋め込み、ネット接続なしで読める。

ローカルHTMLへのブラウザアクセス制限があるため、ブラウザ・DOM・実機での確認は未実施。ネイティブ画面窓をブラウザのスクリーンショットとして扱わない。正式な話数カタログ・iOS同梱・公開サーバーには登録していない。
