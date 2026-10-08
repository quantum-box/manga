# 天魔、二周目。

[第1〜10話を読む](serial.html)。最強の身体でも、死ぬのは怖い。ゲームで聞かなかった声を聞く二周目。

脚本・作画・台詞・スクロール構成を全面改稿。処刑の危機、証人と証拠の確認、公の審理、門を出る選択を十話で描く。帰還と剣の行方は未解決。この十話を導入編として完成させた。

| 話 | タイトル | 変化 |
|---|---|---|
| 1 | [死にたくない](episode-01/index.html) | 見知らぬ処刑を現実の危機として感じ、自分の指で刃を止める。 |
| 2 | [強い手で、壊さない](episode-02/index.html) | 攻撃を防ぎ、生きている相手を確かめ、自分の強さと恐怖を受け止める。 |
| 3 | [俺の罪は誰のもの](episode-03/index.html) | 罪状と証拠を聞き、ゲームの記憶と事実を分ける。 |
| 4 | [逃げる前に](episode-04/index.html) | 逃げられる力を確かめたうえで、もう一人の証人を置いて行かないと決める。 |
| 5 | [鍛冶場の証人](episode-05/index.html) | 攻略上の脇役の名が、一人の働く人へ変わる。協力の条件を聞く。 |
| 6 | [同じ傷、違う証拠](episode-06/index.html) | 事件前の修理依頼を現物と日付で確かめる。主人公と鍛冶師が役割を持って協力する。 |
| 7 | [聞かなかった声](episode-07/index.html) | ハン自身の労働記録と聞かれなかった証言を知り、公開の場で聞く約束をする。 |
| 8 | [刃を抜かずに](episode-08/index.html) | 審理へ向かう証人を襲撃から守り、相手と証拠を壊さない力の使い方を選ぶ。 |
| 9 | [雑役弟子の名前](episode-09/index.html) | 証拠と証言の照合で処刑・盗難の冤罪を取り消す。ハンが名前を取り戻す。 |
| 10 | [門の外へ](episode-10/index.html) | 自由になって休み、旅の目的を自分で選び、見送られて門を出る。 |

## 原稿と制作資料

組み込み image_gen で絵・吹き出し・日本語縦書きを一緒に生成した62点の採用原画。原本のPNGを無加工で配置し、台詞をHTMLで重ねない。文字を直す場合は画像を編集し直す。

各話の index.html と reader.css は組版元、reader.html は画像とCSSを内包する単体HTML、webtoon-full-390.jpg はブラウザ書き出しの完成画像。storyboard.md に話者・全文・縦列・カメラ・状態・見せ順、PROMPTS.md に採用した実際の生成指示を残す。表示窓は production/layout.json に原本座標と用途を記録した。

[設定の入口](series/bible.md)・[全話の脚本](production/scripts.json)・[生成指示](PROMPTS.md)・[スマホ通読](production/mobile-review.md)・[制作状況](production/status.md)。

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

必要な場合だけ package_series.py で最新版をZIPへまとめられる。ZIPをGitに保管しない。公開はPRのmain取り込み後に[共通公開手順](../../server/README.md#全作品を採用版だけに更新する)を使い、最新版が読めた後に同じ話の旧版をサーバーから除く。
