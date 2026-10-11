# 第3話の構成確認

[PRプレビューで読む](https://pr94--manga-server.txcloud.app/?episode=name-star-ring-regalia-episode-03-c0bfb1865a38)と、104コマの全話を縦に読めます。ローカルの確認用HTMLは[index.html](index.html)です。2026-10-11、第2話「明日のある町」の最新版の続きとして更新しました。構成は未採用です。

会話62発話は尾つき、切迫した制止2発話は太いトゲ、心の声8発話は雲形と点へ修正しました。絵に残る4発話と合わせて76発話です。対応する人物への尾と点の方向は[balloon-decisions.json](balloon-decisions.json)に記録しています。

詳細は[storyboard.md](storyboard.md)、完成版へ渡す配置は[layout-decisions.json](layout-decisions.json)、実量と確認範囲は[validation.json](validation.json)。本作画はこの構成への返答を受けてから進めます。

旧ネームはGit bf149ef8c0a0b3f5de0233e54d307e598794d967に保存済み。既存の原画は現行の表示窓から使用する制作素材です。旧完成版をこのネームで公開カタログやiOSへ差し替えてはいません。

390px幅の実量は、本編48,853px、純余白6,271px、内容42,581px、104有効コマ。実量はvalidation.jsonを参照。基準は本編34,000〜60,000px、内容24,000px以上、80〜120コマ。360px幅でも全編を確認し、画像読み込み失敗・横はみ出しは両幅とも0。実機での確認は未実施。

再構成：`python3 build.py` → `python3 rebuild_reader.py` → `python3 write_storyboard.py`。表示確認はPlaywrightとPillowを利用して `node render_review.cjs` → `python3 summarize_review.py`。新しい生成と旧原画の出所は[PROMPTS.md](PROMPTS.md)。
