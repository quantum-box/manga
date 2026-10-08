# 天魔、二周目。制作記録

## 原稿と制作資料

組み込み image_gen で絵・吹き出し・日本語縦書きを一緒に生成した62点の採用原画。原本のPNGを無加工で配置し、台詞をHTMLで重ねない。文字を直す場合は画像を編集し直す。

各話の index.html と reader.css は組版元、reader.html は画像とCSSを内包する単体HTML、webtoon-full-390.jpg はブラウザ書き出しの完成画像。storyboard.md に話者・全文・縦列・カメラ・状態・見せ順、PROMPTS.md に採用した実際の生成指示を残す。表示窓は production/layout.json に原本座標と用途を記録した。

[設定の入口](../series/bible.md)・[全話の脚本](scripts.json)・[生成指示](../PROMPTS.md)・[スマホ通読](mobile-review.md)・[制作状況](status.md)。

旧稿の本文、画像、配布物、確認記録は除去した。旧稿は基準コミット f30be21ae237417a911ea00814d0ad5c84b9b7c8、作画途中は作業ブランチの保存コミット9992538から確認できる。最新版が編集入力として使う原本だけを production/inputs に残す。人物参照も制作資料として保持する。

## 再出力

Python、Pillow、PlaywrightとChromiumを使う。検証は一時HTTPサーバーを自動起動する。

~~~sh
python3 examples/heavenly-demon-ngplus/build_series.py
python3 examples/heavenly-demon-ngplus/validate_series.py
python3 scripts/sync_ios_webtoons.py
python3 scripts/sync_ios_webtoons.py --check
~~~

390×844・360×800 CSS pxのDOM実測、全画像、読み順、原本と単体HTMLの画像バイト、横はみ出し、重要な前兆と結果の距離を各話の validation.json に記録。原画の品質は機械確認と別に、全表示単位と重要区間の連続画面を通読する。iOS同梱版の同期と、iPhone実機・TestFlight起動は別に扱う。

必要な場合だけ package_series.py で最新版をZIPへまとめられる。ZIPをGitに保管しない。公開はPRのmain取り込み後に[共通公開手順](../../../server/README.md#全作品を採用版だけに更新する)を使い、最新版が読めた後に同じ話の旧版をサーバーから除く。
