# 第3話「星環の剣筋」の構成確認

[PRプレビューで読む](https://pr94--manga-server.txcloud.app/?episode=name-star-ring-regalia-episode-03-0d1453d6a68d)。85コマの全話ネームです。2026-10-11、動きの少なさ・特別さの片鱗・星環への言及という指摘を受けて改稿。**構成未採用・本作画未着手**。

低い薙ぎと空振りから盾の修正へ。弱い風に航だけが細い光を見て、リゼの間合いを一度だけ異常に速く破ります。空の星環から巡る魔力の話をし、降りる細い線はリゼに見えません。救助で同じ光が戻り、航の剣撃が獣を退けます。道具確認と救助後の説明の反復を短くしました。

独立した吹き出し60発話（通常声48・強い呼びかけ3・心の声9）と絵の3発話。尾・トゲ・雲形と点を使い分けます。[balloon-decisions.json](balloon-decisions.json)に対応人物を記録。

390px幅で本編42,932px、純余白5,645px、内容37,288px、85有効コマ。目標は本編34,000〜60,000px・内容24,000px以上・80〜120コマ。360px幅は本編39,629px、内容34,514px。両幅の全編を確認し画像失敗と横はみ出し0。実機未確認。

[storyboard.md](storyboard.md)、[layout-decisions.json](layout-decisions.json)、[validation.json](validation.json)が正本。改稿は現在のファイルを置換し、旧版はGit履歴へ残します。既存完成原稿の公開やiOSはこの未採用ネームで差し替えていません。

再構成：python3 build.py → python3 rebuild_reader.py → python3 write_storyboard.py。表示確認：node render_review.cjs → Python/Pillowでsummarize_review.py。新しい3原画は組み込みimage_genで生成し無加工で保存。[PROMPT-motion.md](PROMPT-motion.md)と[generation.json](generation.json)に実行指示と出所を記録。
