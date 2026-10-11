# 第3話「星環の剣筋」構成ネーム

状態：2026-10-11改稿。**未採用・本作画未着手**。第2話の最新版から続く。旧第3話への承認をこの改稿へ適用しない。

## 構成

| 区間 | 新しい動きと理解 | 絵のID |
| --- | --- | --- |
| 朝と再訪 | 日本の無傷の手からミルトの擦り傷と銅貨二枚へ。昨日の抜刀しかけた衝動を話す | 00-japan〜01-choice |
| 動く稽古 | リゼが低く薙ぐ→盾が落ち足へ触れる→航が打ち返し空振り→外へ一歩を教わり受ける | 01-lesson〜01-spar |
| 特別さの片鱗 | 弱い風に細い光が見える→異常に速く踏み込む→木剣を肩の手前で止める→リゼが驚く。再試行は普通に止められる | 02-flicker |
| 星環 | 空の巨大な環と魔力の巡りという日常知識に触れる。降りている線を尋ねてもリゼには見えない | 02-star |
| 巡回と実戦 | 先走った帰還者が消え、兵士が負傷。航が盾で守ると稽古の光が戻り、自分の剣で獣を退ける | 03-patrol〜05-recover |
| 救護と次の一歩 | 身体を作り直せる帰還者と休養が必要な兵士。盾の傷を報告して返し、一閃を見た怜から討伐隊へ誘われる | 06-returner〜08-invitation |

主筋は「守れなかった昨日の航が、稽古で自分だけの光を見て、実戦で一閃を決める」。道具の確認、指示と返事、救護後の供給説明の反復を削った。力は一度だけの速さと一撃で具体的に見せ、原因の説明や習得済みの魔法にはしない。怜は親切な先輩。誘いへの返答は第4話へ。

## 連続性

基点は第2話PR #93 / main bf149ef8。右掌の擦り傷、使わなかった銅貨二枚、抜刀を止められた経験を引き継ぐ。日本には傷や道具を移さない。赤髪の帰還者は第2話の金髪の加害者とは別人。

稽古の木剣は右手、木盾は左。自分の鋼剣は左腰に納刀。木剣を返してから鋼剣を確かめて納め、予備盾を借りて巡回する。救助時は右鋼剣、左木盾。負傷兵の傷は右前腕。剣を納めてから支え、盾は拭いて訓練場の棚へ返す。原画に掌の小傷が省略された瞬間も治癒した意味にしない。

星環は空全体に渡る自然の巨大な環。普通の人が知っている「魔力が巡ると言われている」という話までに留める。航だけに見える細い線は現在の魔力の流れで、未来や人の心ではない。最初の感応は稽古、初めての決定的な剣撃は救助。再現方法・起源・世界の真相・守護者の役割・水不足は明かさない。風の稽古は安全な弱い流れであり、リゼへ木剣を当てない。特別な動きの後も立って話せる。

## 分量とレイアウト

85有効コマ、独立した吹き出し60発話と絵に置く3発話。通常声48は尾つき、強い呼びかけ3はトゲ、心の声9は雲形と点。声・音・余白をコマへ数えない。目標は390 CSS pxの本編34,000〜60,000px、内容24,000px以上、80〜120有効コマ。実量はvalidation.jsonを参照。

主動作は広く、足や視線は小さく、驚きは間を置く。稽古の接触・空振り・修正は近く読み、異常な踏み込みは100%幅、星環の空も100%幅。足跡と盾の返却は大小の接写を同じ場面空間へ組む。対話は縦の列を明示しスマホ幅で全文を読む。

草の音→反応→停止→足場→無音900px→獣の姿という間を残す。ガサ…は原画に一度ありHTMLで重ねない。静けさは直前の動く稽古・巡回と対比する。

## 演出参照

webtoonのaction-directionとname-preview、speech-balloonsを使用。橋上の一歩の薙ぎ・跳躍・反撃後、空を踏むの強化後の肘打ちと踏み切りを画像表示で参照。見せ場の起点→移動→接触または停止→結果を今回の稽古と救助へ移す。既存の決定打ラフを保ち、今回の稽古と星環は組み込みimage_genで3原画を追加した。PROMPT-motion.mdとgeneration.jsonへ実行指示と出所を記録。

## コマごとの判断

### 001 00-japan:1

- 絵・新しい理解：日本の土曜の朝 航は傷のない右掌を見つめる ミルトの痛みと昨夜の問いが残る
- 接続：第2話末尾の問いの結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：82% right 枠=none 表示窓=[0.50390625, 0.0026041666666666665, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：150px 結果を受け止め 次の動作や場所へ切り替える 次=00-japan:1-added-2
- 感情・意図：発話相手へ求めること：日本の土曜の朝 航は傷のない右掌を見つめる ミルトの痛みと昨夜の問いが残る。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-left 対応人物=00-japan:1 無彩色
- 航（心）／thought／independent
```
こっちの手は
なんともない
```

### 002 00-japan:1-added-2

- 絵・新しい理解：日本の台所 母を振り返り空の皿を運ぶ ゲームへ逃げる前に自分の仕事を終える
- 接続：00-japan:1の結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：92% left 枠=thin 表示窓=[0.00390625, 0.0026041666666666665, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：日本の台所 母を振り返り空の皿を運ぶ ゲームへ逃げる前に自分の仕事を終える。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=00-japan:1-added-2 無彩色
- 航／spoken／independent
```
皿を洗ったら
行ってくる
```

### 003 00-japan:2

- 絵・新しい理解：KOH dries his empty hands after washing his own breakfast plate, then reaches toward ordinary headset on shelf; clean plate is in drain rack, no fantasy item in Japan.
- 接続：00-japan:1-added-2の結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：78% right 枠=thin 表示窓=[0.5029296875, 0.7239453125, 0.4921875, 0.2727994791666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：260px 結果を受け止め 次の動作や場所へ切り替える 次=00-yard:1
- 感情・意図：発話相手へ求めること：KOH dries his empty hands after washing his own breakfast plate, then reaches toward ordinary headset on shelf; clean plate is in drain rack, no fantasy item in Japan.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-left 対応人物=00-japan:2 無彩色
- 航（心）／thought／independent
```
今度は
守れるように
```

### 004 00-yard:1

- 絵・新しい理解：ミルトへ戻った航が右掌へ視線を落とし 顔を曇らせる 掌の傷は次の小袋のカットで確かめる
- 接続：00-japan:2の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：94% left 枠=thin 表示窓=[0.507, 0.336, 0.484, 0.19]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：ミルトの安全広場に再接続 右掌の昨日の擦り傷を見つける 剣は左腰に納刀 盾なし。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-right 対応人物=00-yard:1 無彩色
- 航（心）／thought／independent
```
まだ
残ってる
```

### 005 00-yard:1-added-1

- 絵・新しい理解：左掌に使えなかった銅貨が二枚 右掌の擦り傷をかばって小袋へ戻す 日本へ銅貨を運ばない
- 接続：00-yard:1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：86% right 枠=none 表示窓=[0.00390625, 0.3359375, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：110px 結果を受け止め 次の動作や場所へ切り替える 次=00-yard:2
- 感情・意図：発話相手へ求めること：左掌に使えなかった銅貨が二枚 右掌の擦り傷をかばって小袋へ戻す 日本へ銅貨を運ばない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-left 対応人物=00-yard:1-added-1 無彩色
- 航（心）／thought／independent
```
パンも
買えなかった
```

### 006 00-yard:2

- 絵・新しい理解：安全広場から訓練場へ歩いて来た航 リゼは予備の木盾を点検 航の手に気づく
- 接続：00-yard:1-added-1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：82% right 枠=thin 表示窓=[0.50390625, 0.6692708333333334, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：安全広場から訓練場へ歩いて来た航 リゼは予備の木盾を点検 航の手に気づく。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=00-yard:2 無彩色
- リゼ／spoken／independent
```
来たね
手はどう？
```

### 007 00-yard:2-added-1

- 絵・新しい理解：リゼは航の右掌の擦り傷を見て確かめる 触れて治療する魔法は使わない
- 接続：00-yard:2の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：92% left 枠=thin 表示窓=[0.00390625, 0.6692708333333334, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：リゼは航の右掌の擦り傷を見て確かめる 触れて治療する魔法は使わない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=00-yard:2-added-1 無彩色
- 航／spoken／independent
```
握ると
少し痛い
```

### 008 00-yard:2-added-2

- 絵・新しい理解：Medium LIZE looks up from the strap and smiles practically, hand remains on spare shield, her own short sword sheathed.
- 接続：00-yard:2-added-1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.06407552083333333, 0.48828125, 0.27707031249999997]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：120px 結果を受け止め 次の動作や場所へ切り替える 次=01-choice:1
- 感情・意図：発話相手へ求めること：Medium LIZE looks up from the strap and smiles practically, hand remains on spare shield, her own short sword sheathed.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=00-yard:2-added-2 無彩色
- リゼ／spoken／independent
```
痛むなら
途中で止めよう
```

### 009 01-choice:1

- 絵・新しい理解：昨日の衝動を自分の言葉で認める
- 接続：00-yard:2-added-2の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：94% left 枠=none 表示窓=[0.50390625, 0.0026041666666666665, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：昨日の衝動を自分の言葉で認める。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=01-choice:1 無彩色
- 航／spoken／independent
```
昨日…
剣を抜きかけた
```

### 010 01-choice:4

- 絵・新しい理解：掌と鞘を見て悔しさを言葉にする
- 接続：01-choice:1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：86% right 枠=thin 表示窓=[0.00390625, 0.3359375, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：60px 結果を受け止め 次の動作や場所へ切り替える 次=01-choice:6
- 感情・意図：発話相手へ求めること：掌と鞘を見て悔しさを言葉にする。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=01-choice:4 無彩色
- 航／spoken／independent
```
あの人を
止めたくて
```

### 011 01-choice:6

- 絵・新しい理解：相手を倒すためだけでなく習うことを選ぶ
- 接続：01-choice:4の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：82% right 枠=thin 表示窓=[0.00390625, 0.6692708333333334, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：40px 結果を受け止め 次の動作や場所へ切り替える 次=01-lesson:2
- 感情・意図：発話相手へ求めること：相手を倒すためだけでなく習うことを選ぶ。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=01-choice:6 無彩色
- リゼ／spoken／independent
```
じゃあ一本
受けてみて
```

### 012 01-lesson:2

- 絵・新しい理解：Medium LIZE hands him ONE practice shield, short sword in scabbard.
- 接続：01-choice:6の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.06196614583333333, 0.4892578125, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium LIZE hands him ONE practice shield, short sword in scabbard.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=01-lesson:2 無彩色
- リゼ／spoken／independent
```
まずこれ
持ってみて
```

### 013 01-spar:1

- 絵・新しい理解：リゼの低い薙ぎへ航が両手握りに戻り 左盾が落ちる 足と刃の動きから稽古を始める
- 接続：01-lesson:2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応
- 幅と配置：100% center 枠=none 表示窓=[0.009765625, 0.004557291666666667, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：リゼの低い薙ぎへ航が両手握りに戻り 左盾が落ちる 足と刃の動きから稽古を始める。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：離れた相手へ届く切迫した制止を太いトゲで示す 尾または点の方向=down-left 対応人物=01-spar:1 無彩色
- リゼ／spoken／independent
```
いくよ！
```

### 014 01-spar:2

- 絵・新しい理解：盾より下を木剣が軽く触れ 航が足を引く ケガを足さず盾の隙を示す
- 接続：01-spar:1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応
- 幅と配置：94% left 枠=thin 表示窓=[0.509765625, 0.004557291666666667, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：35px 結果を受け止め 次の動作や場所へ切り替える 次=01-spar:3
- 感情・意図：新しい動作または反応：盾より下を木剣が軽く触れ 航が足を引く ケガを足さず盾の隙を示す。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 015 01-spar:3

- 絵・新しい理解：航が右木剣で打ち返すが リゼが外へ回り 空振りする
- 接続：01-spar:2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応
- 幅と配置：100% center 枠=none 表示窓=[0.009765625, 0.337890625, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：航が右木剣で打ち返すが リゼが外へ回り 空振りする。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=01-spar:3 無彩色
- 航／spoken／independent
```
まだ…！
```

### 016 01-spar:4

- 絵・新しい理解：航は片膝で体勢を戻し リゼが盾と足の隙を指す 急いだ結果が目に見える
- 接続：01-spar:3の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応
- 幅と配置：82% right 枠=thin 表示窓=[0.509765625, 0.337890625, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：70px 結果を受け止め 次の動作や場所へ切り替える 次=01-spar:5
- 感情・意図：発話相手へ求めること：航は片膝で体勢を戻し リゼが盾と足の隙を指す 急いだ結果が目に見える。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=01-spar:4 無彩色
- リゼ／spoken／independent
```
剣だけ
追ってる
```

### 017 01-spar:5

- 絵・新しい理解：リゼが外へ踏む足を実演 航が見る 地面の線と靴の方向が次の修正へつながる
- 接続：01-spar:4の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応
- 幅と配置：92% left 枠=none 表示窓=[0.009765625, 0.6712239583333334, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：リゼが外へ踏む足を実演 航が見る 地面の線と靴の方向が次の修正へつながる。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=01-spar:5 無彩色
- リゼ／spoken／independent
```
外へ一歩
盾を残して
```

### 018 01-spar:6

- 絵・新しい理解：航が足を動かして左盾で木剣を受ける 右木剣を自由に残す 起点 接触 結果を近く読む
- 接続：01-spar:5の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応
- 幅と配置：100% center 枠=none 表示窓=[0.509765625, 0.6712239583333334, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：90px 結果を受け止め 次の動作や場所へ切り替える 次=02-flicker:1
- 感情・意図：発話相手へ求めること：航が足を動かして左盾で木剣を受ける 右木剣を自由に残す 起点 接触 結果を近く読む。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=01-spar:6 無彩色
- 航／spoken／independent
```
受けた！
```

### 019 02-flicker:1

- 絵・新しい理解：リゼが左掌から弱い風を流す 盾で防ぐ次の練習 右手は木剣
- 接続：01-spar:6の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：100% center 枠=none 表示窓=[0.009765625, 0.004557291666666667, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：リゼが左掌から弱い風を流す 盾で防ぐ次の練習 右手は木剣。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-flicker:1 無彩色
- リゼ／spoken／independent
```
次は風
無理に受けず
離れていいよ
```

### 020 02-flicker:2

- 絵・新しい理解：航の瞳に風とは違う細い光が映る 現在流れる魔力へ初めて感応
- 接続：02-flicker:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：86% right 枠=thin 表示窓=[0.509765625, 0.004557291666666667, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：45px 結果を受け止め 次の動作や場所へ切り替える 次=02-flicker:3
- 感情・意図：発話相手へ求めること：航の瞳に風とは違う細い光が映る 現在流れる魔力へ初めて感応。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-left 対応人物=02-flicker:2 無彩色
- 航（心）／thought／independent
```
今の
細い光…
```

### 021 02-flicker:3

- 絵・新しい理解：光の筋が空ける風の隙間へ航の足が飛ぶ 足場から太い軌道と土がつながる
- 接続：02-flicker:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：82% right 枠=none 表示窓=[0.009765625, 0.337890625, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：25px 結果を受け止め 次の動作や場所へ切り替える 次=02-flicker:4
- 感情・意図：新しい動作または反応：光の筋が空ける風の隙間へ航の足が飛ぶ 足場から太い軌道と土がつながる。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 022 02-flicker:4

- 絵・新しい理解：航がリゼの剣側の外へ異常に速く入り 右木剣を肩の手前で止める 左盾も残す リゼの間合いを一度破る
- 接続：02-flicker:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：100% center 枠=none 表示窓=[0.509765625, 0.337890625, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：150px 結果を受け止め 次の動作や場所へ切り替える 次=02-flicker:5
- 感情・意図：新しい動作または反応：航がリゼの剣側の外へ異常に速く入り 右木剣を肩の手前で止める 左盾も残す リゼの間合いを一度破る。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 023 02-flicker:5

- 絵・新しい理解：リゼが予想外の速さに目を開く 教えた受けとは違う特別な踏み込みが分かる
- 接続：02-flicker:4の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=thin 表示窓=[0.009765625, 0.6712239583333334, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：リゼが予想外の速さに目を開く 教えた受けとは違う特別な踏み込みが分かる。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-flicker:5 無彩色
- リゼ／spoken／independent
```
その踏み込み
教えてないよ
```

### 024 02-flicker:6

- 絵・新しい理解：もう一度試した航の木剣をリゼが普通に受ける 光は消えたままで同じ速さは再現できない
- 接続：02-flicker:5の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：94% left 枠=thin 表示窓=[0.509765625, 0.6712239583333334, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：120px 結果を受け止め 次の動作や場所へ切り替える 次=02-star:1
- 感情・意図：発話相手へ求めること：もう一度試した航の木剣をリゼが普通に受ける 光は消えたままで同じ速さは再現できない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-right 対応人物=02-flicker:6 無彩色
- 航（心）／thought／independent
```
もう
見えない…
```

### 025 02-star:1

- 絵・新しい理解：水を飲んでいた航が空へ目を上げる 木剣と盾はベンチ 左腰に鋼剣を納刀
- 接続：02-flicker:6の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：86% right 枠=none 表示窓=[0.009765625, 0.004557291666666667, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：水を飲んでいた航が空へ目を上げる 木剣と盾はベンチ 左腰に鋼剣を納刀。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-star:1 無彩色
- 航／spoken／independent
```
ねえ リゼ
星環って
何なんだろう
```

### 026 02-star:2

- 絵・新しい理解：ミルトの屋根の上 空全体を横切る巨大な星環 そこから細い一本の光が降りる 航の主観
- 接続：02-star:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：100% center 枠=none 表示窓=[0.509765625, 0.004557291666666667, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：140px 結果を受け止め 次の動作や場所へ切り替える 次=02-star:3
- 感情・意図：新しい動作または反応：ミルトの屋根の上 空全体を横切る巨大な星環 そこから細い一本の光が降りる 航の主観。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 027 02-star:3

- 絵・新しい理解：リゼが空の環を指す 日常で知っている範囲だけ話す 起源や運営の秘密へ進まない
- 接続：02-star:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：92% left 枠=thin 表示窓=[0.009765625, 0.337890625, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：リゼが空の環を指す 日常で知っている範囲だけ話す 起源や運営の秘密へ進まない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-star:3 無彩色
- リゼ／spoken／independent
```
魔力はあそこから
巡るって
言われてるよ
```

### 028 02-star:4

- 絵・新しい理解：航が右指で星環から下りる細い線をなぞる リゼの風の光と同じだと気づく
- 接続：02-star:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=thin 表示窓=[0.509765625, 0.337890625, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：航が右指で星環から下りる細い線をなぞる リゼの風の光と同じだと気づく。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-star:4 無彩色
- 航／spoken／independent
```
あそこから降りる
細い線も？
さっきの風にも…
```

### 029 02-star:5

- 絵・新しい理解：リゼは航の指す何もない空を見る 線が共有されないことを表情で示す
- 接続：02-star:4の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：94% left 枠=none 表示窓=[0.009765625, 0.6712239583333334, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：160px 結果を受け止め 次の動作や場所へ切り替える 次=02-star:6
- 感情・意図：発話相手へ求めること：リゼは航の指す何もない空を見る 線が共有されないことを表情で示す。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-star:5 無彩色
- リゼ／spoken／independent
```
線？
どこに？
```

### 030 02-star:6

- 絵・新しい理解：航が空になった右指を見る 細い光は消える 星環そのものは空に残る 答えを持たないまま先へ
- 接続：02-star:5の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：86% right 枠=thin 表示窓=[0.509765625, 0.6712239583333334, 0.484375, 0.3235677083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：100px 結果を受け止め 次の動作や場所へ切り替える 次=02-change:1
- 感情・意図：発話相手へ求めること：航が空になった右指を見る 細い光は消える 星環そのものは空に残る 答えを持たないまま先へ。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-star:6 無彩色
- 航／spoken／independent
```
今はもう
消えちゃった
```

### 031 02-change:1

- 絵・新しい理解：Shallow KOH returns ONE wooden practice sword to shared bench beside the other spare practice tools, not holding steel yet. Shield rests at bench edge.
- 接続：02-star:6の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：82% right 枠=thin 表示窓=[0.5048828125, 0.397734375, 0.490234375, 0.2637239583333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow KOH returns ONE wooden practice sword to shared bench beside the other spare practice tools, not holding steel yet. Shield rests at bench edge.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 032 02-change:2

- 絵・新しい理解：Medium KOH uses RIGHT hand to draw his OWN plain straight steel sword briefly from brown scabbard, LEFT holds scabbard, recognizes heavier weight. No shield in hands during this check.
- 接続：02-change:1の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.397734375, 0.490234375, 0.2637239583333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH uses RIGHT hand to draw his OWN plain straight steel sword briefly from brown scabbard, LEFT holds scabbard, recognizes heavier weight. No shield in hands during this check.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=02-change:2 無彩色
- 航／spoken／independent
```
こっちは
もっと重い
```

### 033 02-change:3

- 絵・新しい理解：Medium KOH has resheathed steel sword and picks the ONE spare wooden shield up with LEFT hand for patrol. LIZE points to this specific bench, explains ownership and return place.
- 接続：02-change:2の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：78% right 枠=none 表示窓=[0.0048828125, 0.7271484375, 0.490234375, 0.26959635416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH has resheathed steel sword and picks the ONE spare wooden shield up with LEFT hand for patrol. LIZE points to this specific bench, explains ownership and return place.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=02-change:3 無彩色
- リゼ／spoken／independent
```
盾は私の予備
帰ったらここへ
```

### 034 02-change:3-added-2

- 絵・新しい理解：LIZE points to same bench and spare shelf, expects responsibility not perfect untouched gear.
- 接続：02-change:3の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：94% left 枠=thin 表示窓=[0.0048828125, 0.06419270833333333, 0.4873046875, 0.27760416666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：250px 結果を受け止め 次の動作や場所へ切り替える 次=03-patrol:1
- 感情・意図：発話相手へ求めること：LIZE points to same bench and spare shelf, expects responsibility not perfect untouched gear.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=02-change:3-added-2 無彩色
- リゼ／spoken／independent
```
傷つけたら
隠さず見せてね
```

### 035 03-patrol:1

- 絵・新しい理解：Wide: patrol walks riverbank, steel blade sheathed, water plentiful.
- 接続：02-change:3-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.501953125, 0.4060807291666667, 0.4931640625, 0.26319010416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Wide: patrol walks riverbank, steel blade sheathed, water plentiful.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=03-patrol:1 無彩色
- リゼ／spoken／independent
```
足元も見て
私から離れないで
```

### 036 03-patrol:1-added-1

- 絵・新しい理解：Nameless LOCAL guard gray hair dark goatee steel helmet sand scarf brown leather armor asks KOH on river path, ordinary check not hostile NPC.
- 接続：03-patrol:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.0048828125, 0.4060807291666667, 0.4873046875, 0.26319010416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Nameless LOCAL guard gray hair dark goatee steel helmet sand scarf brown leather armor asks KOH on river path, ordinary check not hostile NPC.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=03-patrol:1-added-1 無彩色
- 兵士／spoken／independent
```
巡回は
初めて？
```

### 037 03-patrol:1-added-2

- 絵・新しい理解：KOH nods, LEFT shield slung RIGHT hand empty near own sheathed steel, answers guard as person.
- 接続：03-patrol:1-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.501953125, 0.7335546875, 0.4931640625, 0.26319010416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH nods, LEFT shield slung RIGHT hand empty near own sheathed steel, answers guard as person.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=03-patrol:1-added-2 無彩色
- 航／spoken／independent
```
はい
足元も見ます
```

### 038 03-patrol:2

- 絵・新しい理解：Small close: fresh claw tracks in mud under reeds, ominous but not gore.
- 接続：03-patrol:1-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：62% left 枠=thin 表示窓=[0.0048828125, 0.7335546875, 0.4873046875, 0.26319010416666666] 場面空間=space-03-patrol:2 x=0 y=0
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Small close: fresh claw tracks in mud under reeds, ominous but not gore.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 039 03-patrol:2-added-1

- 絵・新しい理解：LIZE crouches beside fresh pawprint without touching dangerous reeds, compares it with nearby river mud, healthy water behind.
- 接続：03-patrol:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：34% right 枠=thin 表示窓=[0.5078125, 0.07087239583333332, 0.4873046875, 0.3080338541666667] 場面空間=space-03-patrol:2 x=66 y=127.32974789579158
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE crouches beside fresh pawprint without touching dangerous reeds, compares it with nearby river mud, healthy water behind.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=up-right 対応人物=03-patrol:2-added-1 無彩色
- リゼ／spoken／independent
```
川へ来るのは
人だけじゃない
```

### 040 03-patrol:3

- 絵・新しい理解：Medium: impulsive red-haired PLAYER traveler runs past the patrol with flashy steel sword.
- 接続：03-patrol:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：86% right 枠=thin 表示窓=[0.5078125, 0.43627604166666667, 0.4873046875, 0.2316927083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium: impulsive red-haired PLAYER traveler runs past the patrol with flashy steel sword.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 帰還者／spoken／embedded
```
任せろ！
```

### 041 03-patrol:3-added-1

- 絵・新しい理解：KOH reaches empty RIGHT hand toward red-player back, asks him to wait; local guard and LIZE still together on path.
- 接続：03-patrol:3の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：82% right 枠=none 表示窓=[0.0048828125, 0.43627604166666667, 0.4931640625, 0.2316927083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH reaches empty RIGHT hand toward red-player back, asks him to wait; local guard and LIZE still together on path.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：離れた相手へ届く切迫した制止を太いトゲで示す 尾または点の方向=down-left 対応人物=03-patrol:3-added-1 無彩色
- 航／spoken／independent
```
待って！
まだ何がいるか…
```

### 042 03-listen:1

- 絵・新しい理解：Shallow empty reeds shiver near muddy path, only grass and moving leaves. A SINGLE ガサ… inscription starts at right side of reeds and extends toward panel border. No eyes or claws or creature silhouette yet.
- 接続：03-patrol:3-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=thin 表示窓=[0.5078125, 0.7324869791666666, 0.4873046875, 0.26425781249999997]
- 音：新しく鳴る ガサ… 草の原画に一度だけ 以後は同じ音の点へ減衰
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow empty reeds shiver near muddy path, only grass and moving leaves. A SINGLE ガサ… inscription starts at right side of reeds and extends toward panel border. No eyes or claws or creature silhouette yet.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 043 03-listen:2

- 絵・新しい理解：Small KOH eye-and-left-shield close-up reacts to the offscreen rustle as he slips the borrowed shield from its walking sling onto LEFT forearm; red-haired bronze-armored traveler back only in farther edge, turning ahead. Continue the same sound with faint trailing … into large white bottom fade, no second complete inscription. No visible beast.
- 接続：03-listen:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.7324869791666666, 0.4931640625, 0.26425781249999997]
- 音：前の草の音が続く 追加のガサを描かず 薄い点が止まるまで 警戒する目と手を優先
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Small KOH eye-and-left-shield close-up reacts to the offscreen rustle as he slips the borrowed shield from its walking sling onto LEFT forearm; red-haired bronze-armored traveler back only in farther edge, turning ahead. Continue the same sound with faint trailing … into large white bottom fade, no second complete inscription. No visible beast.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 044 03-listen:2-added-1

- 絵・新しい理解：LIZE raises empty RIGHT fingers to stop patrol, listens toward grass, her own short sword still sheathed. ONE faint trailing dots from grass sound can continue, no new ガサ and no creature.
- 接続：03-listen:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：94% left 枠=thin 表示窓=[0.501953125, 0.06290364583333333, 0.4931640625, 0.2717317708333333]
- 音：前の草の音が続く 追加のガサを描かず 薄い点が止まるまで 警戒する目と手を優先
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：LIZE raises empty RIGHT fingers to stop patrol, listens toward grass, her own short sword still sheathed. ONE faint trailing dots from grass sound can continue, no new ガサ and no creature.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 045 03-listen:2-added-2

- 絵・新しい理解：KOH shifts one boot onto firmer path so wounded guard will later have space behind him; LEFT shield ready, RIGHT hand on own sheathed hilt. No advance or monster shown.
- 接続：03-listen:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：86% right 枠=none 表示窓=[0.0048828125, 0.06290364583333333, 0.4873046875, 0.2717317708333333]
- 音：前の草の音が続く 追加のガサを描かず 薄い点が止まるまで 警戒する目と手を優先
- 余白：900px 草の音と停止の反応を受け 獣の姿を下で初めて見せる 次=04-beast:1
- 感情・意図：新しい動作または反応：KOH shifts one boot onto firmer path so wounded guard will later have space behind him; LEFT shield ready, RIGHT hand on own sheathed hilt. No advance or monster shown.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 046 04-beast:1

- 絵・新しい理解：Large angled action shot: lean dark riverwolf-like monster leaps from reeds at the impulsive red-haired PLAYER; KOH in foreground frightened, shield held low, LIZE already reacts. Not the black-horn guardian.
- 接続：03-listen:2-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.501953125, 0.3973958333333333, 0.4931640625, 0.25625]
- 音：新しく鳴る ガッ 動作の接点へ置き 前の音と混同しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Large angled action shot: lean dark riverwolf-like monster leaps from reeds at the impulsive red-haired PLAYER; KOH in foreground frightened, shield held low, LIZE already reacts. Not the black-horn guardian.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 047 04-beast:2

- 絵・新しい理解：Shallow immediate result: the red-haired PLAYER avatar dissolves into pale construction light after the claw strike, with his steel sword falling into mud. The LOCAL guardsman tried to cover him and receives a small non-graphic scratch on his RIGHT forearm; KOH sees the guard crouch. No corpse, no injury to a Japanese person, no HUD and no dialogue.
- 接続：04-beast:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.3973958333333333, 0.4873046875, 0.25625]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：200px 結果を受け止め 次の動作や場所へ切り替える 次=04-beast:2-added-1
- 感情・意図：新しい動作または反応：Shallow immediate result: the red-haired PLAYER avatar dissolves into pale construction light after the claw strike, with his steel sword falling into mud. The LOCAL guardsman tried to cover him and receives a small non-graphic scratch on his RIGHT forearm; KOH sees the guard crouch. No corpse, no injury to a Japanese person, no HUD and no dialogue.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 048 04-beast:2-added-1

- 絵・新しい理解：KOH turns sharply from fading player construction light to LOCAL guard physical RIGHT forearm wound, chooses real hurt person rather than vanished avatar.
- 接続：04-beast:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=thin 表示窓=[0.501953125, 0.7207421875, 0.4931640625, 0.27600260416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH turns sharply from fading player construction light to LOCAL guard physical RIGHT forearm wound, chooses real hurt person rather than vanished avatar.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 049 04-find:1

- 絵・新しい理解：Shallow dropped red-player steel sword lies on mud near reeds, not vanished and not automatically returned. A boot of the injured LOCAL guard braces beside it; his RIGHT forearm held close, blood only a tiny restrained mark.
- 接続：04-beast:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：94% left 枠=none 表示窓=[0.0048828125, 0.7207421875, 0.4873046875, 0.27600260416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow dropped red-player steel sword lies on mud near reeds, not vanished and not automatically returned. A boot of the injured LOCAL guard braces beside it; his RIGHT forearm held close, blood only a tiny restrained mark.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 050 05-defense:1

- 絵・新しい理解：Medium: KOH steps LEFT beside local wounded guard, raises borrowed shield, right hand grips sword.
- 接続：04-find:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.06442708333333333, 0.4892578125, 0.27867187499999996]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium: KOH steps LEFT beside local wounded guard, raises borrowed shield, right hand grips sword.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：離れた相手へ届く切迫した制止を太いトゲで示す 尾または点の方向=down-left 対応人物=05-defense:1 無彩色
- リゼ／spoken／independent
```
その人の前に！
```

### 051 05-defense:2

- 絵・新しい理解：Two quick close-up moments right-to-left within ONE shallow row: shield blocks claw; LIZE gathers pale wind around short sword.
- 接続：05-defense:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：82% right 枠=thin 表示窓=[0.50390625, 0.405390625, 0.4912109375, 0.2541145833333333]
- 音：新しく鳴る ガン 動作の接点へ置き 前の音と混同しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Two quick close-up moments right-to-left within ONE shallow row: shield blocks claw; LIZE gathers pale wind around short sword.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 052 05-resonance:1

- 絵・新しい理解：盾が爪を止めた直後 航の瞳に稽古で見えた細い光が戻る
- 接続：05-defense:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=thin 表示窓=[0.009765625, 0.051419270833333336, 0.484375, 0.21941406249999998]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：盾が爪を止めた直後 航の瞳に稽古で見えた細い光が戻る。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-right 対応人物=05-resonance:1 無彩色
- 航（心）／thought／independent
```
さっきの
光…！
```

### 053 05-resonance:2

- 絵・新しい理解：航だけの視界 獣の肩から魔力の爪へ細い光の筋が見える 未来や相手の心は見えない
- 接続：05-resonance:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=none 表示窓=[0.5078125, 0.051419270833333336, 0.4814453125, 0.21941406249999998]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：航だけの視界 獣の肩から魔力の爪へ細い光の筋が見える 未来や相手の心は見えない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-left 対応人物=05-resonance:2 無彩色
- 航（心）／thought／independent
```
この筋へ
合わせれば…
```

### 054 05-resonance:3

- 絵・新しい理解：盾の後ろに兵士を残し 航が自分の右手の剣で細い筋へ短く踏み込む 足から肩と刃へ動作がつながる
- 接続：05-resonance:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：94% left 枠=thin 表示窓=[0.009765625, 0.34674479166666666, 0.482421875, 0.30429687499999997]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：盾の後ろに兵士を残し 航が自分の右手の剣で細い筋へ短く踏み込む 足から肩と刃へ動作がつながる。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 055 05-defense:3

- 絵・新しい理解：航の一閃が獣の爪の魔力を斬り裂く 太い斜めの軌跡と衝撃で獣を退ける 決め手は航 兵士は左盾の後ろで安全
- 接続：05-resonance:3の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.509765625, 0.34609375, 0.4794921875, 0.30429687499999997]
- 音：新しく鳴る ザンッ 刃が爪の魔力を断つ起点から斜めの軌跡へ 効果音は画像の爪や航の顔を隠さない
- 余白：100px 結果を受け止め 次の動作や場所へ切り替える 次=05-resonance:5
- 感情・意図：新しい動作または反応：航の一閃が獣の爪の魔力を斬り裂く 太い斜めの軌跡と衝撃で獣を退ける 決め手は航 兵士は左盾の後ろで安全。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 056 05-resonance:5

- 絵・新しい理解：援護を始めていたリゼが 航の一撃を見て剣を下げ驚く 風が決め手だったと見せない
- 接続：05-defense:3の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：82% right 枠=thin 表示窓=[0.009765625, 0.72359375, 0.4833984375, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：援護を始めていたリゼが 航の一撃を見て剣を下げ驚く 風が決め手だったと見せない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=05-resonance:5 無彩色
- リゼ／spoken／independent
```
今の…
航が？
```

### 057 05-resonance:6

- 絵・新しい理解：光が消えた自分の右手の剣を見る航 獣は逃げ 兵士は生きている 立ったまま驚きを受け止める
- 接続：05-resonance:5の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=none 表示窓=[0.509765625, 0.72359375, 0.4794921875, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：光が消えた自分の右手の剣を見る航 獣は逃げ 兵士は生きている 立ったまま驚きを受け止める。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：心の声を雲形と点で示す 尾または点の方向=down-right 対応人物=05-resonance:6 無彩色
- 航（心）／thought／independent
```
剣まで
軽くなった…？
```

### 058 05-recover:1

- 絵・新しい理解：Wide wolf retreats physically into reeds on LEFT far bank edge, same dark lean animal with tail, visible direction and diminishing distance. LIZE sword down but alert, no creature dissolved or respawned.
- 接続：05-resonance:6の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.725546875, 0.4892578125, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Wide wolf retreats physically into reeds on LEFT far bank edge, same dark lean animal with tail, visible direction and diminishing distance. LIZE sword down but alert, no creature dissolved or respawned.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- リゼ／spoken／embedded
```
追わないで
```

### 059 05-recover:1-added-1

- 絵・新しい理解：KOH begins one step after retreating wolf but stops when LIZE warns, chooses guard over pursuit and turns back.
- 接続：05-recover:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：94% left 枠=thin 表示窓=[0.5048828125, 0.06196614583333333, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH begins one step after retreating wolf but stops when LIZE warns, chooses guard over pursuit and turns back.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 060 05-recover:2

- 絵・新しい理解：Medium LOCAL guard uses healthy LEFT hand to press cloth against wounded RIGHT forearm. Polearm rests upright against a tree during this pause. KOH left shield low and own sword resheathed stands beside him.
- 接続：05-recover:1-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.06196614583333333, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium LOCAL guard uses healthy LEFT hand to press cloth against wounded RIGHT forearm. Polearm rests upright against a tree during this pause. KOH left shield low and own sword resheathed stands beside him.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=05-recover:2 無彩色
- 航／spoken／independent
```
歩けますか
```

### 061 05-recover:2-added-1

- 絵・新しい理解：LOCAL guard nods that he can walk, healthy LEFT hand presses RIGHT injury cloth, polearm leans beside tree during pause.
- 接続：05-recover:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：82% right 枠=none 表示窓=[0.5048828125, 0.3948828125, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LOCAL guard nods that he can walk, healthy LEFT hand presses RIGHT injury cloth, polearm leans beside tree during pause.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=05-recover:2-added-1 無彩色
- 兵士／spoken／independent
```
ゆっくりなら
歩ける
```

### 062 05-recover:2-added-2

- 絵・新しい理解：KOH resheathes his steel sword and gently supports the guard above the injured RIGHT forearm at his RIGHT upper arm with his free RIGHT hand. He does not press the wound. LEFT shield lowered. LIZE temporarily carries the polearm; before walking on, she returns it to the guard healthy LEFT hand.
- 接続：05-recover:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.3948828125, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH resheathes his steel sword and gently supports the guard above the injured RIGHT forearm at his RIGHT upper arm with his free RIGHT hand. He does not press the wound. LEFT shield lowered. LIZE temporarily carries the polearm; before walking on, she returns it to the guard healthy LEFT hand.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 063 05-recover:3

- 絵・新しい理解：Wide three walk back toward visible Milt gate at same river path. KOH matches LOCAL guard pace, LIZE walks outer side keeping watch. Dropped red-player sword remains behind in mud near reeds, not magically collected.
- 接続：05-recover:2-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.5048828125, 0.72875, 0.490234375, 0.2679947916666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：260px 結果を受け止め 次の動作や場所へ切り替える 次=05-recover:3-added-1
- 感情・意図：新しい動作または反応：Wide three walk back toward visible Milt gate at same river path. KOH matches LOCAL guard pace, LIZE walks outer side keeping watch. Dropped red-player sword remains behind in mud near reeds, not magically collected.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 064 05-recover:3-added-1

- 絵・新しい理解：KOH and the injured guard pause on the clinic steps. SENA takes over the guard care from the doorway and sends KOH to get water nearby. The guard is no longer left in danger, and the next scene is the nearby safe square.
- 接続：05-recover:3の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.0048828125, 0.72875, 0.490234375, 0.2679947916666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH and the injured guard pause on the clinic steps. SENA takes over the guard care from the doorway and sends KOH to get water nearby. The guard is no longer left in danger, and the next scene is the nearby safe square.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=05-recover:3-added-1 無彩色
- セナ／spoken／independent
```
ここで診るよ
水を飲んで
おいで
```

### 065 06-returner:1

- 絵・新しい理解：Wide: the red-haired PLAYER reappears in plain replacement clothes, weapon lost, KOH and AKARI nearby.
- 接続：05-recover:3-added-1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：86% right 枠=none 表示窓=[0.5029296875, 0.06184895833333333, 0.4921875, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Wide: the red-haired PLAYER reappears in plain replacement clothes, weapon lost, KOH and AKARI nearby.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=06-returner:1 無彩色
- 帰還者／spoken／independent
```
戻れた
でも剣がない
```

### 066 06-returner:2

- 絵・新しい理解：Close KOH listens with relief, sword sheathed and shield lowered.
- 接続：06-returner:1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.06184895833333333, 0.48828125, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Close KOH listens with relief, sword sheathed and shield lowered.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=06-returner:2 無彩色
- 航／spoken／independent
```
さっきの人…
戻れたんだ
```

### 067 06-returner:3

- 絵・新しい理解：AKARI in orange game jacket checks a readable blue HUD only for herself.
- 接続：06-returner:2の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：92% left 枠=thin 表示窓=[0.5029296875, 0.3945833333333333, 0.4921875, 0.2701302083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：AKARI in orange game jacket checks a readable blue HUD only for herself.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=06-returner:3 無彩色
- 灯里／spoken／independent
```
身体を
作り直すんだって
```

### 068 06-supply:1

- 絵・新しい理解：Medium local supply clerk points to a modest waiting bench and almost empty replacement-clothes shelf; gives plain spare boot pair to regenerated PLAYER in beige clothes, not his lost armor or sword.
- 接続：06-returner:3の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：78% right 枠=thin 表示窓=[0.5029296875, 0.7298177083333334, 0.4921875, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium local supply clerk points to a modest waiting bench and almost empty replacement-clothes shelf; gives plain spare boot pair to regenerated PLAYER in beige clothes, not his lost armor or sword.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down 対応人物=06-supply:1 無彩色
- 係の人／spoken／independent
```
次の身体も
予備の用意が
いるからね
```

### 069 06-supply:2

- 絵・新しい理解：Shallow regenerated red-haired PLAYER looks at empty hands and plain clothes, remembers his weapon still physically at riverbank.
- 接続：06-supply:1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：94% left 枠=none 表示窓=[0.50390625, 0.06220052083333333, 0.4912109375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Shallow regenerated red-haired PLAYER looks at empty hands and plain clothes, remembers his weapon still physically at riverbank.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=06-supply:2 無彩色
- 帰還者／spoken／independent
```
剣は川か…
ひとりじゃ
取りに行けないな
```

### 070 06-supply:3

- 絵・新しい理解：Medium AKARI lowers her own brass communicator, speaks to KOH with relief for person in Japan, her wooden bow remains on back.
- 接続：06-supply:2の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：86% right 枠=thin 表示窓=[0.50390625, 0.3945442708333333, 0.4912109375, 0.2610546875]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：230px 結果を受け止め 次の動作や場所へ切り替える 次=07-local:1
- 感情・意図：発話相手へ求めること：Medium AKARI lowers her own brass communicator, speaks to KOH with relief for person in Japan, her wooden bow remains on back.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=06-supply:3 無彩色
- 灯里／spoken／independent
```
日本の身体は
無事だって
```

### 071 07-local:1

- 絵・新しい理解：Medium KOH looks toward the LOCAL guard, worried.
- 接続：06-supply:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.3945442708333333, 0.4892578125, 0.2610546875]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH looks toward the LOCAL guard, worried.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=07-local:1 無彩色
- 航／spoken／independent
```
兵士さんの傷も
作り直せば
治る？
```

### 072 07-local:2

- 絵・新しい理解：SENA calm close-up, one clean bandage in hands.
- 接続：07-local:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：92% left 枠=thin 表示窓=[0.50390625, 0.72234375, 0.4912109375, 0.2744010416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：280px 結果を受け止め 次の動作や場所へ切り替える 次=07-local:3
- 感情・意図：発話相手へ求めること：SENA calm close-up, one clean bandage in hands.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=07-local:2 無彩色
- セナ／spoken／independent
```
この人には
この身体しか
ないんだ
```

### 073 07-local:3

- 絵・新しい理解：LIZE tightens bandage, clear difference to player; tired expression.
- 接続：07-local:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=none 表示窓=[0.0048828125, 0.06243489583333334, 0.4873046875, 0.26959635416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE tightens bandage, clear difference to player; tired expression.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=07-local:3 無彩色
- リゼ／spoken／independent
```
明日は休んで
巡回は代わるから
```

### 074 07-clinic:1

- 絵・新しい理解：Shallow LIZE moves ONE patrol token from tomorrow active row to a reserve peg beside the clinic board. No readable unexplained bureaucratic chart, no giant UI, no promise to heal instantly.
- 接続：07-local:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：94% left 枠=thin 表示窓=[0.501953125, 0.3971354166666667, 0.4931640625, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow LIZE moves ONE patrol token from tomorrow active row to a reserve peg beside the clinic board. No readable unexplained bureaucratic chart, no giant UI, no promise to heal instantly.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 075 07-clinic:2

- 絵・新しい理解：Medium SENA closes ONE wooden medicine box gently beside seated LOCAL guard, addresses KOH with practical thanks. Guard rests right bandaged arm on lap, same gray hair and goatee.
- 接続：07-clinic:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.3971354166666667, 0.4873046875, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium SENA closes ONE wooden medicine box gently beside seated LOCAL guard, addresses KOH with practical thanks. Guard rests right bandaged arm on lap, same gray hair and goatee.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=07-clinic:2 無彩色
- セナ／spoken／independent
```
休ませる場所まで
運んでくれて
助かった
```

### 076 07-promise:1

- 絵・新しい理解：Close KOH uses plain cloth to wipe mud from ONE wooden shield rim on bench, shield detached from LEFT arm, his own steel sword stays sheathed at belt. No magically repaired cracks.
- 接続：07-clinic:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：62% left 枠=thin 表示窓=[0.0048828125, 0.7292838541666666, 0.4873046875, 0.2674609375] 場面空間=space-07-promise:1 x=0 y=0
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Close KOH uses plain cloth to wipe mud from ONE wooden shield rim on bench, shield detached from LEFT arm, his own steel sword stays sheathed at belt. No magically repaired cracks.。次の行動の理由として見せる。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 発話なし

### 077 07-promise:1-added-1

- 絵・新しい理解：航は借りた盾の縁の小さな欠けを持ち主リゼへ見せる 木は自動で修復しない
- 接続：07-promise:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：34% right 枠=none 表示窓=[0.5048828125, 0.06208333333333334, 0.490234375, 0.2679947916666667] 場面空間=space-07-promise:1 x=66 y=129.3959507014028
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH shows ONE small scrape on borrowed shield metal rim to LIZE, remembers promised responsibility; wood uncracked until future6.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=up-right 対応人物=07-promise:1-added-1 無彩色
- 航／spoken／independent
```
縁が
少し欠けた
```

### 078 07-promise:1-added-2

- 絵・新しい理解：LIZE checks rim with empty fingers, relieved rather than scolds; same shield on bench.
- 接続：07-promise:1-added-1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.06208333333333334, 0.490234375, 0.2679947916666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE checks rim with empty fingers, relieved rather than scolds; same shield on bench.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down 対応人物=07-promise:1-added-2 無彩色
- リゼ／spoken／independent
```
見せてくれて
ありがとう
ここは直せる
```

### 079 07-promise:2

- 絵・新しい理解：Medium KOH looks up from cleaned shield toward LIZE, asks rather than silently claims borrowed property.
- 接続：07-promise:1-added-2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：94% left 枠=thin 表示窓=[0.5048828125, 0.3952994791666667, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH looks up from cleaned shield toward LIZE, asks rather than silently claims borrowed property.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=07-promise:2 無彩色
- 航／spoken／independent
```
明日も
借りていい？
```

### 080 07-promise:3

- 絵・新しい理解：Wide LIZE points toward spare shield shelf right above the same bench. KOH places ONE cleaned shield there and removes hand, now shieldless.
- 接続：07-promise:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：100% center 枠=none 表示窓=[0.0048828125, 0.3952994791666667, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：400px 結果を受け止め 次の動作や場所へ切り替える 次=08-invitation:1
- 感情・意図：発話相手へ求めること：Wide LIZE points toward spare shield shelf right above the same bench. KOH places ONE cleaned shield there and removes hand, now shieldless.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=07-promise:3 無彩色
- リゼ／spoken／independent
```
ここに置いて
次も一緒に
練習しよう
```

### 081 08-invitation:1

- 絵・新しい理解：REI in silver armor and deep red short cloak approaches KOH, sword sheathed, friendly.
- 接続：07-promise:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：82% right 枠=none 表示窓=[0.5048828125, 0.7282161458333334, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：REI in silver armor and deep red short cloak approaches KOH, sword sheathed, friendly.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=08-invitation:1 無彩色
- 怜／spoken／independent
```
あの一閃
見事だったな
```

### 082 08-invitation:2

- 絵・新しい理解：Close KOH recognizes his admired player, startled but delighted. KOH hands empty, NO shield, own steel sword remains sheathed.
- 接続：08-invitation:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.7282161458333334, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Close KOH recognizes his admired player, startled but delighted. KOH hands empty, NO shield, own steel sword remains sheathed.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色
- 航／spoken／embedded
```
……レイさん？
```

### 083 08-invitation:2-added-1

- 絵・新しい理解：KOH straightens posture, recognizes REI from familiar raid videos, now asks as nervous youth, hands empty no shield.
- 接続：08-invitation:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=thin 表示窓=[0.50390625, 0.06641927083333332, 0.4912109375, 0.2877473958333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH straightens posture, recognizes REI from familiar raid videos, now asks as nervous youth, hands empty no shield.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=08-invitation:2-added-1 無彩色
- 航／spoken／independent
```
動画で
見てました
```

### 084 08-invitation:2-added-2

- 絵・新しい理解：REI smiles and gestures toward real training yard instead of superiority or secret chosen-one favor.
- 接続：08-invitation:2-added-1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：94% left 枠=thin 表示窓=[0.0048828125, 0.06641927083333332, 0.4892578125, 0.2877473958333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：REI smiles and gestures toward real training yard instead of superiority or secret chosen-one favor.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-right 対応人物=08-invitation:2-added-2 無彩色
- 怜／spoken／independent
```
ここでは
一緒に練習しよう
```

### 085 08-invitation:3

- 絵・新しい理解：Large REI offers an open empty hand, a genuine invitation.
- 接続：08-invitation:2-added-2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：100% center 枠=none 表示窓=[0.50390625, 0.4190364583333333, 0.4912109375, 0.265859375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：330px 結果を受け止め 次の動作や場所へ切り替える 次=end
- 感情・意図：発話相手へ求めること：Large REI offers an open empty hand, a genuine invitation.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：声に出す会話を細い輪郭と話者へ向く尾で示す 尾または点の方向=down-left 対応人物=08-invitation:3 無彩色
- 怜／spoken／independent
```
討伐隊
一緒に来るか？
```
