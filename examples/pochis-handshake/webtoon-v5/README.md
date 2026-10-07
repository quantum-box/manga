# 転生したら柴犬だった。 第1〜30話

[第1〜30話を続けて読む](all.html) · [話一覧](chapters.html) · [第11話](episode-11/index.html) · [第30話](episode-30/index.html)

第1〜10話の採用済み再制作版に、第11〜30話の続編を追加。各話10枚・約40コマ、計300枚・約1,200コマ。村の水路の修復を通して、声が届かない身体での協力、役割の線引き、休む日、野生の狼との距離、試験の中断と修理を描く。第30話では、毎日握手しなくても仲間でいられる関係に着地する。

日本語の縦書き会話・吹き出し・絵は一体のラスター画像。HTMLに会話を重ねない。ポチ・ミラ・魔王の人物参照を共有し、文字、天候、村と城の位置、水路の通水状態、旗による合図、握手の動作を生成後に修正した。

## 余白と読む速さ

300場面の後の間を内容別に指定。原画内の白いコマ間に88か所の間を足し、原画300枚を388の表示窓で読む。隣接窓は同じ境界を共有し、全画素を保つ。基準幅360pxから本文幅に比例し、文字を縮めて余白を作らない。

動作と合図は近く、返事待ちや怖さ、休息は長く。子供・狼・魔王の初登場に加え、第12話の声と子羊、第15話の怖い門と魔王、第29話の通水開始と村への到着をスクロールの先で見せる。第18話の足が動かない犬、第30話の握手への返事には原画内の待つ間を置く。

[表示範囲と間](production/scroll-layout.json)、[目視確認](production/visual-review.json)、各話 validation.json に表示窓、画像ハッシュ、実測幅、余白、連続スクロール窓を記録。

## 読む・保存する

話一覧から各話へ進み、末尾で前後の話へ移動する。reader.html は画像とCSSを内包した単独ファイル。all.html は全300枚の連続リーダー。各話 webtoon-390.jpg / webtoon-360.jpg は完成画像。

## 制作資料と確認

[シリーズ設定](series-bible.md)、[連続性](continuity.md)、[全話計画](production/plan.json)、[生成記録](production/generation-records.json)、[制作状況](production/status.md)。各話 storyboard.md / scenes.json / PROMPTS.md に台詞、間、採用画像のSHA256、生成・編集指示を記録する。

原画PNGと修正元は採用作画の制作資料。配布画像は同寸法のWebP。旧版の本文・配布物はGit履歴で管理し、共有人物参照は ../references/ に保持する。

全300枚を360px幅で通読。続編の修正画像も再確認。文字高は目視で約19〜28px。390×844・360×800の読み込み・話移動・表示窓と余白をPlaywrightで確認し、単独リーダーの画像バイトとiOS同梱HTML・CSS・画像を照合する。実機確認は未実施。公開はPR経由のCI・レビュー・mainへの取り込み後に行う。

Pillow対応Pythonで `python production/assemble_continuation.py`、`python production/build.py`。PlaywrightとChromium対応Nodeで `node production/validate.cjs`。リポジトリ直下で `python scripts/sync_ios_webtoons.py`、`--check` で同梱版を照合する。
