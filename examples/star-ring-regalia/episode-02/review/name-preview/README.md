# 星環のレガリア 第2話「明日のある町」ネーム

状態：**採用待ち**。本作画・公開は未着手。既存の第2話、カタログ、iOS配布物は変更していない。

- [読む：軽量HTML](preview.html)（roughディレクトリを隣に置く）
- [読む：画像内蔵HTML](index.html)（単体で持ち運び可能、約60MB）
- [全文・コマ別意図](storyboard.md) / [構成データ](plan.json)
- [確認結果](validation.json) / [生成履歴と原画ハッシュ](generation.json)
- [390px全体像](complete-390.jpg) / [360px全体像](complete-360.jpg)

## 確認

96有効コマ。390px幅で本編48,309px、登録純余白4,880px、余白を除く内容43,429px。360pxでも横はみ出し・文字切れ・画像ロード失敗なし。連続表示窓は `review/`、DOM実測は `dom-measurements.json`。

薬の配達、エダの明日、粉からパンへの結果、道を間違えて音で戻る選択、空袋の返却、銅貨二枚による返礼、リゼの巡回、討伐隊の誘いを全話でつないだ。縦書きセリフ・発話別吹き出し・効果音をHTMLで重ねている。

## 再生成

このディレクトリで `python3 build-preview.py`。計測はPlaywrightが利用できるNode環境で `node render-preview.cjs`。新たな画像生成は不要。`preview.html` と `index.html` は同一構成・同一原画を表示する。

## 次の工程

ユーザーの「ネームOK、本作画にGO！」を受けてから本作画へ進む。修正指示があればこのネームを更新する。採用前に公開中の版を削除しない。
