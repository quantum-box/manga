# AI漫画制作プロジェクト

スマートフォンで読むオリジナルWebtoonを制作し、セリフ・縦構図・余白・登場順を保ったままiOSアプリに収録する実験プロジェクト。

## 読める作品

| 作品 | ジャンル | 採用版 |
| --- | --- | --- |
| [星環のレガリア](examples/star-ring-regalia/index.html) | 剣と魔法・日本・ゲーム | 第1話「補欠の空」の完成作画・スマホ確認。200話以上の企画と240話の仮構成 |
| [塔の農夫は、英雄を食わせる](examples/tower-farm-kitchen/chapters.html) | 剣と魔法・塔・農業・飲食店 | 完成作画とスマホ確認10話。全240話のロードマップと導入10話の脚本 |
| [塔を灯す剣](examples/tower-forge/chapters.html) | VRMMORPG・剣と魔法・塔攻略 | 読者の指摘に対応し第1話を55コマで改稿。第2〜10話は初稿・改稿待ち。240話の仮構成とゲームの技術設計も収録 |
| [ゼロ・ブレイク](examples/zero-break/chapters.html) | 異世界転生・スーパーヒーロー | 第1〜10話の縦書き完成作画・全196場面。接近、測定、救助の手順と反応を描く。全50話の場面脚本も収録 |
| [天魔、二周目。](examples/heavenly-demon-ngplus/README.md) | 武侠・異世界転生・強くてニューゲーム | 第1〜10話の増補版。会話と反応を厚くしたアニメ風。処刑場から自由な帰還まで |
| [剣聖、仇の弟子に転生する](examples/swordsaint-enemy-disciple/README.md) | 武侠・転生 | 第1〜10話。白背景・ゆっくり版で連続して読める |
| [終電後の落とし物係](examples/lost-property-clerk/webtoon-v3/README.md) | 日常・幻想 | 雨、猫、足跡をたどる縦読み短編 v3 |
| [星を拾う夜](examples/star-lighthouse/webtoon-v2/README.md) | SF | 静けさと巨大な親の登場を広い余白で描く v2 |
| [転生したら柴犬だった。](examples/pochis-handshake/webtoon-v5/README.md) | ファンタジー | 声はワン、手は肉球。柴犬になった元人間が村の水路を直し、働く・休む・断る選択を見つけていく |

各作品の`index.html`が編集可能な本文。`reader.html`はオフライン用で、塔の農夫の第1話は同じフォルダーの`reader-art-*.js`三個を一緒に使う。ほかの作品は画像を内包した単一HTMLでも読める。採用版の脚本、プロンプト、検証記録、全長スクリーンショットも各例に保存する。同じ話は採用済みの最新版だけを残し、旧版はGitの履歴で管理する。最新版が使う原画・参照素材は残す。作業方針は[AGENTS.md](AGENTS.md)を参照。

## iOSアプリ

[起動・収録方法](ios/README.md)。タイトル検索、ジャンル絞り込み、作品詳細、話と版の選択、お気に入り、オフライン縦読みを実装。

完成したHTMLと画像をWKWebViewで表示するため、文字組みやスクロールの間がブラウザ版と同じ構成になる。作品メタデータは[content/catalog.json](content/catalog.json)、同梱するファイルは`ios/Manga/Webtoons`。

## 制作知見と再利用スキル

新連載：[星環のレガリア 第1話「補欠の空」](examples/star-ring-regalia/episode-01/index.html)。8原画と日本語縦書き、[単体リーダー](examples/star-ring-regalia/episode-01/reader.html)、スマホ検証、カタログ・iOS同梱版を収録。[企画](docs/star-ring-regalia/series/bible.md)は200話以上を目標に、世界観・人物・240話の仮構成・導入10話の先行設計を含む。今回の完成原稿は第1話。サーバー公開はこのPRのマージ後に行う。

1. [制作で採用した知見](docs/webtoon-production.md)：広い余白、密度の変化、登場順、文字の分離、スマホ検証。
2. [Webtoonスキル](skills/webtoon/SKILL.md)：全体話数を50話・100話・200話以上から選び、世界観・人物・物語を設計。このリポジトリでは[AGENTS.md](AGENTS.md)に従い、一話の作画・スマホ確認、PR、マージ、サーバー公開確認を終えてから次話を作画する。
3. [武侠・転生・回帰の調査](docs/murim-reincarnation.md)：公式作品ページとオリジナル第1話の企画。
4. [初期のWebtoon再調査](docs/webtoon-research.md)と[最初の企画メモ](docs/initial-proposal.md)：方向転換前の仮説と参考資料。

スキルを使う場合は`skills/webtoon`をCodexの個人スキルフォルダへコピーし、`$webtoon`で呼び出す。repoに画像付きの一式を保存しているため、別環境でも再利用できる。

## 収録物の更新と確認

```sh
python3 scripts/sync_ios_webtoons.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/sync_ios_webtoons.py --check
```

画像生成は制作時に行い、アプリ実行時のAPI接続は不要。配信サービスへの投稿やTestFlightへの配布は別工程。

## 配信サーバー

[Webtoon配信サーバー](server/README.md): Rust / Cloudflare Workers + Tachyon Storage。
