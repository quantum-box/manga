# 第5話：土は、点数じゃない — 全編改稿

時間：13〜17日目
開始・終了：黄化を単なる不足と決めず、土と水を分析。肥料の過剰と塩類の問題を学び、追加施肥を止める。
終了状態：回復した区画と黄化区画は別に採土。ECは同じ方法内で比較。未知の魔物粉は食用農地へ入れない。

原画と表示単位を分ける。原画の全文は以下の順序。表示窓は manifest.json の crop と同じで、原画を改変しない。会話は原画内の縦書き。次話の成果を先に描かない。

## 01-remake-yellow
見せる情報・接続・カメラ：Balt and Kou beside one SMALL seedling section with yellowing leaves, nearby section greener; Balt feels leaf then checks soil, no idiot expression or huge mature forest. Closed fertilizer sack behind them.
スクロールの目的：導入の場所と前話の状態を引き継ぐ
表示窓境界（原画y）：[0, 546, 840, 1130, 1443, 1643, 1868, 2172]。各窓の間：[50, 120, 70, 260, 170, 120, 100]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | この列だけ、黄色い。 | この列だけ、 / 黄色い。 |
| 2 | エルナ | 肥料を、増やした方がいい？ | 肥料を、増や / した方がいい / ？ |
| 3 | バルト | 足りない色とは、限らん。 | 足りない色と / は、限らん。 |
| 4 | コウ | 水と土を、別々に調べたい。 | 水と土を、別 / 々に調べたい / 。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 02-remake-samples
見せる情報・接続・カメラ：Three closeups: Kou collects soil at matched depth in affected section, Balt collects normal section separately, two sealed sample jars and a third water sample kept apart. Jars have simple colored twine, no readable labels.
スクロールの目的：相手の知識を聞いて受け止める
表示窓境界（原画y）：[0, 490, 1102, 1506, 2172]。各窓の間：[90, 180, 60, 220]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | 同じ採り方で、比べよう。 | 同じ採り方で / 、比べよう。 |
| 2 | エルナ | この紐で、区画を分けるね。 | この紐で、区 / 画を分けるね / 。 |
| 3 | バルト | 良い土と、混ぜるなよ。 | 良い土と、混 / ぜるなよ。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 03-remake-calibration
見せる情報・接続・カメラ：Iris at workshop table with fantasy conductivity probe in glass reference vessel, mechanical needle gauge and standard sample, Kou observes. No digital electronics. Two panels showing reference then sample, separate test steps, no invented numeric text.
スクロールの目的：手順と判断を短い動作でつなぐ
表示窓境界（原画y）：[0, 427, 917, 1235, 1602, 2172]。各窓の間：[45, 24, 130, 910, 70]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | イリス | 測り方が違えば、数字も違う。 | 測り方が違え / ば、数字も違 / う。 |
| 2 | コウ | 器具の基準も、確かめよう。 | 器具の基準も / 、確かめよう / 。 |
| 3 | イリス | 同じ深さ、同じ量でね。 | 同じ深さ、同 / じ量でね。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 04-remake-salts
見せる情報・接続・カメラ：Medium Iris interprets matched samples, narrow closeup high versus lower needle position WITHOUT readable numbers, lower Elna worried holding closed fertilizer sack. No visible salt crystals sprouting from plant or magical x-ray.
スクロールの目的：気づきの前後で速度を落とす
表示窓境界（原画y）：[0, 491, 930, 1213, 1578, 1771, 2172]。各窓の間：[65, 200, 90, 340, 130, 260]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | イリス | この区画は、塩類が多い。 | この区画は、 / 塩類が多い。 |
| 2 | エルナ | 肥料なのに、苦しくなるの？ | 肥料なのに、 / 苦しくなるの / ？ |
| 3 | コウ | 肥料にも、塩が含まれるんだ。 | 肥料にも、塩 / が含まれるん / だ。 |
| 4 | コウ | 色だけで、足しちゃいけなかった。 | 色だけで、足 / しちゃいけな / かった。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 05-remake-outlet
見せる情報・接続・カメラ：Kou and Balt trace drainage outlet safely toward common channel, hand on site map with simple arrows, quiet conversation. Do not flush water through bed in this scene: they are checking capacity and destination first.
スクロールの目的：選んだ行動と結果を確かめる
表示窓境界（原画y）：[0, 605, 917, 1257, 1589, 2172]。各窓の間：[40, 70, 160, 90, 120]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | 水で、薄められない？ | 水で、薄めら / れない？ |
| 2 | コウ | 薄める前に、排水先を調べる。 | 薄める前に、 / 排水先を調べ / る。 |
| 3 | バルト | 流した分は、消えんからな。 | 流した分は、 / 消えんからな / 。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 06-remake-unknown-material
見せる情報・接続・カメラ：Plain local trader offers CLOSED sack of powdered monster residue on utility lane far from food beds, Kou declines immediate use, Balt serious nearby. No corpse, gore, spreading powder, or instant fertilizer miracle. Three unequal panels.
スクロールの目的：説明の後に反応を待つ
表示窓境界（原画y）：[0, 656, 1036, 1430, 1705, 2172]。各窓の間：[160, 240, 90, 190, 340]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | 商人 | 魔物の粉なら、効くぞ。 | 魔物の粉なら / 、効くぞ。 |
| 2 | コウ | 何が入ってるか、まだ分からない。 | 何が入ってる / か、まだ分か / らない。 |
| 3 | 商人 | 今日は、買わないのか？ | 今日は、買わ / ないのか？ |
| 4 | バルト | 試すなら、食用の畑と分けろ。 | 試すなら、食 / 用の畑と分け / ろ。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 07-remake-stop-feeding
見せる情報・接続・カメラ：Closeup fertilizer sack stored closed on shelf, hand marks dated observation in notebook; lower Elna and Kou inspect unchanged seedling section and decide to wait. No instant green transformation, no flooding.
スクロールの目的：次の仕事へ状態を渡す
表示窓境界（原画y）：[0, 2172]。各窓の間：[110]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | 今日は、足すのを止める。 | 今日は、足す / のを止める。 |
| 2 | エルナ | 何もしないのは、不安だね。 | 何もしないの / は、不安だね / 。 |
| 3 | コウ | 見に来る。記録は、止めない。 | 見に来る。記 / 録は、止めな / い。 |
| 4 | エルナ | 変わるまで、記録しよう。 | 変わるまで、 / 記録しよう。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 08-remake-open-diner
見せる情報・接続・カメラ：Tall soft transition from small slow-growing seedlings under tower light to diner serving window at dusk, Elna lights lantern, Kou brings PURCHASED basket. Warm anxious faces, continuous stable garden geography.
スクロールの目的：今回の成果を受け止めて次話へ進む
表示窓境界（原画y）：[0, 358, 554, 869, 1203, 1539, 1828, 2172]。各窓の間：[140, 210, 100, 180, 270, 160, 420]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | 待ってる間にも、店は開く。 | 待ってる間に / も、店は開く / 。 |
| 2 | コウ | 今日は、仕入れた葉を使おう。 | 今日は、仕入 / れた葉を使お / う。 |
| 3 | エルナ | お客さんのお腹は、待てないから。 | お客さんのお / 腹は、待てな / いから。 |
| 4 | コウ | 畑だけじゃ、暮らせないな。 | 畑だけじゃ、 / 暮らせないな / 。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。
