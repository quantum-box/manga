# AI漫画制作プロジェクト

スマートフォンで読むオリジナルWebtoonを制作し、セリフ・縦構図・余白・登場順を保ったままiOSアプリに収録する実験プロジェクト。

## 読める作品

| 作品 | ジャンル | あらすじ |
| --- | --- | --- |
| [星環のレガリア](examples/star-ring-regalia/index.html) | 剣と魔法・日本・ゲーム | ゲームの向こうで、君の名前を呼ぶ。 |
| [塔の農夫は、英雄を食わせる](examples/tower-farm-kitchen/chapters.html) | 剣と魔法・塔・農業・飲食店 | 畑から、英雄の明日の一皿を。 |
| [塔を灯す剣](examples/tower-forge/chapters.html) | VRMMORPG・剣と魔法・塔攻略 | 自分の作った剣で、未踏の塔へ。 |
| [ゼロ・ブレイク](examples/zero-break/chapters.html) | 異世界転生・スーパーヒーロー | 最弱判定、最強の一歩。 |
| [天魔、二周目。](examples/heavenly-demon-ngplus/README.md) | 武侠・異世界転生・強くてニューゲーム | 第1〜10話を全面改稿。処刑の恐怖から、証人・証拠・公開審理、門を出る選択まで |
| [剣聖、仇の弟子に転生する](examples/swordsaint-enemy-disciple/README.md) | 武侠・転生 | 俺を殺した男が、今度は俺の師匠。 |
| [終電後の落とし物係](examples/lost-property-clerk/webtoon-v3/README.md) | 日常・幻想 | 雨の跡をたどると、小さな窓口。 |
| [星を拾う夜](examples/star-lighthouse/webtoon-v2/README.md) | SF | 宇宙の静けさに、ひとつの返事。 |
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
