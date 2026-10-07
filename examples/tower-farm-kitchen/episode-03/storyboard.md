# 第3話：一度に播くな — 全編改稿

時間：5〜7日目
開始・終了：人気への期待を作付けへ変える。十二区画の分割播種を始め、初収穫までは仕入れる。
終了状態：既存の成株を順に使い、復旧区画を播種。最初の庭葉は7日目に播く。28日栽培は見込みで確定値ではない。

原画と表示単位を分ける。原画の全文は以下の順序。表示窓は manifest.json の crop と同じで、原画を改変しない。会話は原画内の縦書き。次話の成果を先に描かない。

## 01-remake-customer
見せる情報・接続・カメラ：Diner counter, young adult adventurer with auburn short hair and muted ochre cloak finishes bowl; Elna listens smiling then worried. Small inset empty leafy garnish plate. This recurring customer is not Leon.
スクロールの目的：導入の場所と前話の状態を引き継ぐ
表示窓境界（原画y）：[0, 481, 1035, 1442, 2172]。各窓の間：[60, 120, 180, 200]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | 客 | 明日も、この葉を頼む。 | 明日も、この / 葉を頼む。 |
| 2 | エルナ | ……明日も？ | ……明日も？ |
| 3 | エルナ | ありがとう。量を確かめておくね。 | ありがとう。 / 量を確かめて / おくね。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 02-remake-empty-basket
見せる情報・接続・カメラ：Kou and Elna outside serving window, clean empty harvest basket in foreground; two unequal closeups basket and Kou's thoughtful face. Existing harvest has been used, garden cannot immediately replace it.
スクロールの目的：相手の知識を聞いて受け止める
表示窓境界（原画y）：[0, 672, 997, 1350, 1773, 2172]。各窓の間：[60, 120, 180, 60, 200]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | 今日の籠、もう空っぽ。 | 今日の籠、も / う空っぽ。 |
| 2 | コウ | 一度に採れたら、次は空く。 | 一度に採れた / ら、次は空く / 。 |
| 3 | エルナ | 畑にも、仕込みがいるんだ。 | 畑にも、仕込 / みがいるんだ / 。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 03-remake-native-seed
見せる情報・接続・カメラ：Balt on plot path shows tiny native seed in palm, Kou listens close, lower panel glowing ceiling vein and differently shaded bed corner. Plain seed packet without labels.
スクロールの目的：手順と判断を短い動作でつなぐ
表示窓境界（原画y）：[0, 606, 963, 1301, 2172]。各窓の間：[45, 24, 130, 70]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | この種は、どんな場所で育つ？ | この種は、ど / んな場所で育 / つ？ |
| 2 | バルト | 庭葉は、光が弱いと遅れる。 | 庭葉は、光が / 弱いと遅れる / 。 |
| 3 | コウ | ここで育つ速さを、測ろう。 | ここで育つ速 / さを、測ろう / 。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 04-remake-germination
見せる情報・接続・カメラ：Three brief closeups: handful of small seeds; Kou places an equal counted sample on damp cloth in shallow dish; notebook makes tally marks with room for future result. No sprouts already in newly set test, no predicted yield on screen.
スクロールの目的：気づきの前後で速度を落とす
表示窓境界（原画y）：[0, 544, 832, 1107, 1448, 1712, 2172]。各窓の間：[60, 120, 180, 60, 120, 200]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | これだけ、別に播くの？ | これだけ、別 / に播くの？ |
| 2 | コウ | 全部の種が、芽を出すとは限らない。 | 全部の種が、 / 芽を出すとは / 限らない。 |
| 3 | コウ | 同じ数を置いて、出た芽を数える。 | 同じ数を置い / て、出た芽を / 数える。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 05-remake-twelve-plots
見せる情報・接続・カメラ：Elevated plot view with FOUR long parallel beds, each divided into THREE equal subsections by small twine markers, total twelve sections; medium Kou and Elna looking at plain sketched plan. Bed widths consistent, no implausible giant farm. Leave words off diagram.
スクロールの目的：選んだ行動と結果を確かめる
表示窓境界（原画y）：[0, 391, 826, 1101, 1366, 1768, 2164]。各窓の間：[60, 910, 60, 70, 160, 120]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | 四つの畝を、十二に分ける。 | 四つの畝を、 / 十二に分ける / 。 |
| 2 | エルナ | 全部、今日播くの？ | 全部、今日播 / くの？ |
| 3 | コウ | 七日ずつ、播く日をずらそう。 | 七日ずつ、播 / く日をずらそ / う。 |
| 4 | エルナ | 採る日も、ずらしたいんだね。 | 採る日も、ず / らしたいんだ / ね。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 06-remake-sow
見せる情報・接続・カメラ：Three unequal hand-action panels: Elna makes shallow sowing line in prepared bed; Kou sows tiny seeds in one selected section; soil gently covers seeds. Only first three of twelve sections are sown this week; other sections stay bare or contain existing plants. No germination in same instant.
スクロールの目的：説明の後に反応を待つ
表示窓境界（原画y）：[0, 581, 1063, 1359, 1661, 2172]。各窓の間：[60, 120, 180, 60, 200]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | 今日は、この三つ。 | 今日は、この / 三つ。 |
| 2 | コウ | 深く埋めすぎないで。 | 深く埋めすぎ / ないで。 |
| 3 | エルナ | ……このくらい？ | ……このくら / い？ |
| 4 | コウ | うん。次は、七日後だ。 | うん。次は、 / 七日後だ。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 07-remake-buy
見せる情報・接続・カメラ：Diner back door, local farmer delivers basket of existing leafy vegetables, Elna and Kou accept and tally purchase. Distinct plain brown-clothed adult supplier, not main cast duplicated. Bought grain sack also visible.
スクロールの目的：次の仕事へ状態を渡す
表示窓境界（原画y）：[0, 492, 751, 1096, 1427, 1759, 2172]。各窓の間：[65, 30, 130, 220, 140, 110]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | 最初の収穫までは、仕入れる。 | 最初の収穫ま / では、仕入れ / る。 |
| 2 | エルナ | その代金も、計算に入れよう。 | その代金も、 / 計算に入れよ / う。 |
| 3 | コウ | 畑が遅れても、店を止めないために。 | 畑が遅れても / 、店を止めな / いために。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 08-remake-calendar
見せる情報・接続・カメラ：Large quiet evening scene under blue awning, Kou and Elna beside notebook with four simple week columns and small drawings, no readable diagram text; tiny new sown beds visible through window at ground, no mature crop there. Their serious hopeful faces dominate.
スクロールの目的：今回の成果を受け止めて次話へ進む
表示窓境界（原画y）：[0, 906, 2172]。各窓の間：[260, 420]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | 明日の客と、四週間後の畑。 | 明日の客と、 / 四週間後の畑 / 。 |
| 2 | エルナ | 両方、見ていくんだね。 | 両方、見てい / くんだね。 |
| 3 | コウ | 四週間は、まだ見込みだけど。 | 四週間は、ま / だ見込みだけ / ど。 |
| 4 | エルナ | じゃあ、毎日確かめよう。 | じゃあ、毎日 / 確かめよう。 |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。
