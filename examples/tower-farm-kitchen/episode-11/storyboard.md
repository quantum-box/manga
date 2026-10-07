# 第11話：空席が消えた朝 — 続話制作

時間：43日目
開始・終了：帰還食堂へ攻略者が仲間を連れて戻り、十六食を売り切る。翌日の予約と実際の代金を得る。
終了状態：一営業日の十六食は自給と仕入れの合計。全48m²の安定収穫ではない。ロウは第9話の十二食を食べた攻略者の一人。店は混雑したが注文を断り分け、無限に追加調理しない。収入は費用を引く前の売上。

原画と表示単位を分ける。原画の全文は以下の順序。表示窓は manifest.json の crop と同じで、原画を改変しない。会話は原画内の縦書き。次話の成果を先に描かない。

## 01-morning-footsteps
見せる情報・接続・カメラ：Early morning at the same blue-awning diner. Broad quiet establishing empty tables, Elna ties her apron; narrow closeup Kou straightens clean bowls. Below, two close uneven panels: Kou hears footsteps on the left paved lane then looks towards the doorway. Do NOT reveal the arriving crowd yet.
スクロールの目的：足音だけを先に届けて来客を待たせる
表示窓境界（原画y）：[0, 509, 1040, 1558, 1783, 2171]。各窓の間：[90, 120, 240, 260, 900]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | 今日は
何人来るかな | 今日は / 何人来るかな |
| 2 | コウ | 昨日の分は
用意できてる | 昨日の分は / 用意できてる |
| 3 | コウ | ……誰か来た | ……誰か来た |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 02-returning-party-cast
見せる情報・接続・カメラ：Reveal the returning customers only here. Row is a capable male adventurer age30 with short rust-auburn hair, ochre cloak, leather cuirass and sheathed steel sword, unlike silver-haired Leon. He stands at the lane doorway with two adult teammates. Row smiles remembering the prior meal; Elna recognizes him; separate reaction of Kou, no food served yet.
スクロールの目的：前の納品が新しい客を呼んだことを見せる
表示窓境界（原画y）：[0, 1123, 2172]。各窓の間：[160, 150]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | ロウ | ここだ
俺たちの飯を
作ってくれた店 | ここだ / 俺たちの飯を / 作ってくれた店 |
| 2 | ロウ | 今日は
仲間も連れてきた | 今日は / 仲間も連れてきた |
| 3 | エルナ | あの十二食の！ | あの十二食の！ |
| 4 | コウ | ……三人も | ……三人も |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 03-line-at-the-awning
見せる情報・接続・カメラ：The same lane a little later, not another city. Kou steps outside carrying an empty wooden order board, sees several small groups gathering under the blue awning. Large borderless reveal of a modest but obvious queue of about10 adults, then Elna startled closeup, then a gray-haired ordinary customer asking politely. Do not draw 100people or a royal parade.
スクロールの目的：空席だった店と行列の差を大きく披露する
表示窓境界（原画y）：[0, 2172]。各窓の間：[350]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | 客 | ここの定食が
うまいって
聞いてきた | ここの定食が / うまいって / 聞いてきた |
| 2 | エルナ | こんなに…… | こんなに…… |
| 3 | コウ | 順番に
案内します | 順番に / 案内します |
| 4 | ロウ | 俺だけの店には
できなかったな | 俺だけの店には / できなかったな |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 04-sixteen-servings
見せる情報・接続・カメラ：Inside the same compact diner kitchen. Elna with clean hands portions simmered stew into ceramic shallow bowls; Kou checks sixteen serving tokens in two short rows of8 on a separate clean service shelf, NOT a notebook on food. Meat and barley purchased, leaf greens partly harvested. Short paired ladle and serving-hand closeups, broader teamwork, guests still waiting.
スクロールの目的：数と手順を守りながら素早く食事へつなぐ
表示窓境界（原画y）：[0, 923, 1688, 2172]。各窓の間：[90, 140, 80]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | コウ | 今日は
十六食まで | 今日は / 十六食まで |
| 2 | エルナ | うん
一皿ずつ
ちゃんと出そう | うん / 一皿ずつ / ちゃんと出そう |
| 3 | コウ | お待たせしました | お待たせしました |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 05-dish-reveal
見せる情報・接続・カメラ：Heroic appetizing food reveal in warm afternoon diner light. One large borderless glazed beef carrot leaf-green barley stew in ivory ceramic bowl, smooth rich russet-brown gravy, tender beef chunks and carrot cross-sections, soft green leaves, steam rises through sparse cream area. Small top hand places bowl, then dish takes most of scroll; an adjacent simple piece of bread. NO customer mouth, bite or reaction yet. No beadlike grain texture. Bottom tiny spoon about to lift but does not touch mouth.
スクロールの目的：湯気と料理を味わい食べた反応は下へ残す
表示窓境界（原画y）：[0, 2172]。各窓の間：[910]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | お腹いっぱい
食べてね | お腹いっぱい / 食べてね |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 06-one-bite-and-smile
見せる情報・接続・カメラ：Same Row sits at wooden table, same ceramic stew and bread. First spoon lifts a realistic small beef and carrot bite, next Row eats, quiet widened eyes separate, then a big relieved smile and shoulders relaxing. Adult teammate only at edge, never Leon. Finally Row looks toward Elna and Kou at counter. Food quantity decreases after bite, spoon not doubled.
スクロールの目的：ひと口から驚きと指名までを受け止める
表示窓境界（原画y）：[0, 459, 707, 1014, 1379, 1696, 2172]。各窓の間：[170, 260, 180, 120, 150, 250]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | ロウ | ……うまい | ……うまい |
| 2 | ロウ | 戦いのあとに
欲しかったのは
こういう飯だ | 戦いのあとに / 欲しかったのは / こういう飯だ |
| 3 | 仲間 | 帰ってくる理由が
増えたな | 帰ってくる理由が / 増えたな |
| 4 | ロウ | 次も
ここにしよう | 次も / ここにしよう |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 07-sold-out-coins
見せる情報・接続・カメラ：Late afternoon, used empty ceramic bowls collected apart from clean counter. Elna receives last customer copper coins; later counts sales with Kou at dry ledger desk, no money beside cooking food. Ledger abstract marks only. First show empty serving-pot and all16tokens turned over, then copper coin stacks, Elna stunned delighted face. Meal price6copper, total gross96copper, not net profit.
スクロールの目的：売り切れと代金を具体的な報酬として見せる
表示窓境界（原画y）：[0, 472, 781, 1107, 1400, 1708, 2172]。各窓の間：[100, 180, 170, 90, 130, 420]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | エルナ | 十六食
全部出た…… | 十六食 / 全部出た…… |
| 2 | コウ | 売上は
九十六銅貨 | 売上は / 九十六銅貨 |
| 3 | コウ | 仕入れと費用は
ここから払う | 仕入れと費用は / ここから払う |
| 4 | エルナ | それでも
全部選んでもらえた | それでも / 全部選んでもらえた |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。

## 08-tomorrow-reservation
見せる情報・接続・カメラ：Quiet evening at clean empty diner, warm lamps, no crowd now. Row at doorway gives a small blank paper reservation token to Elna, no actual inscription; closeup Elna holds it then Kou looks at now-empty chairs with happy disbelief, final large shared smile. No next-floor journey, new crops or new contract yet. Sparse ivory ending with rising warm lamp glow.
スクロールの目的：次の来店の約束と二人の喜びに余韻を残す
表示窓境界（原画y）：[0, 312, 769, 1038, 2172]。各窓の間：[180, 140, 180, 430]px（390px幅）。

| 順 | 話者 | 正確な全文 | 縦列・右から左 |
| --- | --- | --- | --- |
| 1 | ロウ | 明日の分も
取っておいてくれ | 明日の分も / 取っておいてくれ |
| 2 | エルナ | また来て
くれるんだ | また来て / くれるんだ |
| 3 | コウ | 俺たちの仕事が
帰ってきたな | 俺たちの仕事が / 帰ってきたな |
| 4 | エルナ | 明日も
この店を開けよう | 明日も / この店を開けよう |

伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。
