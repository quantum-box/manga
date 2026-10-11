# 第3話の構成確認

[index.html](index.html) を開くと、99コマの全話を縦に読めます。2026-10-11、第2話「明日のある町」の最新版の続きとして更新しました。構成は未採用です。

詳細は[storyboard.md](storyboard.md)、完成版へ渡す配置は[layout-decisions.json](layout-decisions.json)、実量と確認範囲は[validation.json](validation.json)。本作画はこの構成への返答を受けてから進めます。

旧ネームはGit bf149ef8c0a0b3f5de0233e54d307e598794d967に保存済み。既存の原画は現行の表示窓から使用する制作素材です。旧完成版をこのネームで公開カタログやiOSへ差し替えてはいません。

390px幅の実量は、本編46,657px、純余白10,103px、内容36,555px、99有効コマ。基準は本編34,000〜60,000px、内容24,000px以上、80〜120コマ。360px幅でも全編を確認し、画像読み込み失敗・横はみ出しは両幅とも0。実機での確認は未実施。

再構成：`python3 build.py` → `python3 rebuild_reader.py`。表示確認はPlaywrightとPillowを利用して `node render_review.cjs` → `python3 summarize_review.py`。新しい生成と旧原画の出所は[PROMPTS.md](PROMPTS.md)。
