# 第3話「戻れる剣、戻れない剣」構成ネーム

状態：2026-10-11の第2話最新版から続く新しい構成。**未採用・本作画未着手**。旧第3話への2026-10-09の承認を、この変更の承認として扱わない。旧完成原稿の配布・公開データは、このネームの採用と完成版の検証が終わるまで差し替えない。

## 構成

| 区間 | 変化 | 絵のID |
| --- | --- | --- |
| 土曜の朝と再訪 | 日本の無傷の手から、ミルトで残る擦り傷と銅貨二枚へ。昨日の自分の行動をリゼに話す | 00-japan〜01-choice |
| 稽古 | 剣道の両手握りが盾を邪魔する。肘と足を修正して一度受け、限界と休憩を覚える | 01-lesson〜02-rest |
| 借り物と巡回 | 木剣を返して鋼剣を安全に納める。予備の木盾を借りて、返す場所を確認して川へ歩く | 02-change〜03-listen |
| 川辺の獣 | 別の赤髪の帰還者が先走り身体を失う。航は兵士を盾で守り、リゼの風と協力して撤退する | 04-beast〜05-recover |
| 戻れる身体と戻らない仕事 | 帰還者の再生成には用意が必要。装備は戻らず、兵士の右前腕は治療と休養が必要 | 06-returner〜07-clinic |
| 結果と誘い | 盾の傷を隠さず持ち主へ見せ、棚へ返す。次の稽古を頼んだ航へ、怜が討伐隊に誘う | 07-promise〜08-invitation |

冒頭の問いは「昨日 抜いたあとに何ができたのか」。今回の成果は敵の討伐でも昨日の加害者との決着でもなく、仲間の声を聞いて負傷兵を生きたまま休める場所へ運ぶこと。怜は本当に親切な先輩として登場する。参加の返答と討伐隊の詳細は第4話へ残す。

## 第2話からの連続性

基点はPR #93のmain bf149ef8c0a0b3f5de0233e54d307e598794d967。第1話の最新完成稿と、第2話の採用ネーム・adoption.json・layout-decisions.json・layout-revision.md、seriesのbible/world/characters/opening-arc/roadmap/continuityを確認。

- 日本の航の身体には傷を移さない。ミルトでの右手掌の擦り傷は残す。手首と手の甲の負傷へ変えない。旧ラフの細部に傷が省略されるカットも、状態が回復した意味にはしない。本作画では見える掌へ同じ傷を引き継ぐ。
- 銅貨二枚は使わず小袋へ戻す。日本への持出し、パンの購入、補給品の支払いに流用しない。
- 第2話の荷運び人の右手首は未治癒。加害者への対応を勝手に決着させない。第3話の赤髪の帰還者は第2話の金髪の加害者とは別人。
- 航の剣は右手、鞘は左腰。木剣を返してから鋼剣へ持ち替える。予備の木盾は左。リゼの短剣と風以外の新技は使わない。訓練は痛みを隠さず途中で止められる条件から始める。
- 再生成は帰還者の身体だけ。無限の供給や自動の装備回収を足さない。現地兵の右前腕をセナが治療し、仕事の代役も決める。町の川は正常。水不足・守護者の姿と役割・独立した世界の真相は先出ししない。

## 分量とレイアウト

全話99の異なる動作・理解・選択・結果を計上。声・音・純余白を有効コマへ足さない。目標は390 CSS pxの本編34,000〜60,000px、内容24,000px以上、80〜120有効コマ。実量は本編46,657px、純余白10,103px、内容36,555px、99有効コマ。端数を含む実測と360px幅の値はvalidation.jsonを正本とする。

68発話を白地に独立、5発話を身体動作や短い反応の絵へ。17原画の使える訓練・救護ラフを無加工で参照し、接続と稽古前の告白を2原画で追加。原画の枚数とコマ数を混同しない。読みやすい縦列で句読点を使わず、自然な問いと制止には？と！を残す。

5か所で大きな絵と脇の小さな接写・白地の返答を同じ場面の空間へ置く。単純な全幅のカード列に揃えない。右側の小カットから始める横並びは、この話では無理に追加せず、JSONの順と縦の位置で読順を指定。主動作は広く、手・足の理解は小さく、救助後は密度を落とす。

純余白20か所にはplan.json/pureGapsのID、前後、役割、高さを対応。獣の直前は草の音→航の反応→リゼの停止→足場を選ぶ→900pxの無音の間→姿。ガサ…は原画内に一度あり、同じ言葉をHTMLに重ねない。続く点は同じ音の減衰で、二度目の草の音にはしない。

## 演出参照と適用

webtoonスキルのname-preview、episode-length、approved-example、scroll-pacing、whitespace-example、emotion-and-causality、speech-balloons、action-directionを読了。approved-webtoon、spacious-before/after、zero-breakの全長と音→通知→光→出現の390px連続窓、橋上の一歩の薙ぎ→跳躍→反撃後、空を踏むの肘打ちと跳躍の強化後を画像で確認。

使った判断：短い稽古の失敗と修正は近く読む。質問の返答、獣の発見、救護後の理解と盾の返却には違う長さの間を置く。独立した声が先に届き表情が後に現れる順、主動作の起点→接触→撤退の結果、人物を描かない沈黙を選ぶ。作例の内容や枚数は転用しない。

## コマごとの判断

改行は縦書きの列区切り。音の発生と継続は別に記録。無言を無音と同義にしない。

### 001 00-japan:1

- 絵・新しい理解：日本の土曜の朝 航は傷のない右掌を見つめる ミルトの痛みと昨夜の問いが残る
- 接続：第2話末尾の問いの結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：82% right 枠=none 表示窓=[0.50390625, 0.0026041666666666665, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：150px 結果を受け止め 次の動作や場所へ切り替える 次=00-japan:1-added-1
- 感情・意図：発話相手へ求めること：日本の土曜の朝 航は傷のない右掌を見つめる ミルトの痛みと昨夜の問いが残る。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航（心）／thought／independent
```
こっちの手は
なんともない
```

### 002 00-japan:1-added-1

- 絵・新しい理解：MIWA places one empty serving plate near KOH, asks him to clear his own breakfast before game. KOH looks up from ordinary physical phone.
- 接続：00-japan:1の結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.06278645833333334, 0.48828125, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：MIWA places one empty serving plate near KOH, asks him to clear his own breakfast before game. KOH looks up from ordinary physical phone.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 美和／spoken／independent
```
お皿
お願いね
```

### 003 00-japan:1-added-2

- 絵・新しい理解：日本の台所 母を振り返り空の皿を運ぶ ゲームへ逃げる前に自分の仕事を終える
- 接続：00-japan:1-added-1の結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：78% right 枠=thin 表示窓=[0.00390625, 0.0026041666666666665, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：日本の台所 母を振り返り空の皿を運ぶ ゲームへ逃げる前に自分の仕事を終える。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
うん
洗ってから行く
```

### 004 00-japan:1-added-3

- 絵・新しい理解：KOH washes his one breakfast plate at real Japan sink, then dries his empty RIGHT hand, ordinary water sound, no fantasy injury.
- 接続：00-japan:1-added-2の結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：94% left 枠=thin 表示窓=[0.0048828125, 0.3975651041666667, 0.48828125, 0.2599869791666667]
- 音：新しく鳴る サァ… 動作の接点へ置き 前の音と混同しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH washes his one breakfast plate at real Japan sink, then dries his empty RIGHT hand, ordinary water sound, no fantasy injury.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 005 00-japan:2

- 絵・新しい理解：KOH dries his empty hands after washing his own breakfast plate, then reaches toward ordinary headset on shelf; clean plate is in drain rack, no fantasy item in Japan.
- 接続：00-japan:1-added-3の結果を受ける。日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷
- 幅と配置：86% right 枠=none 表示窓=[0.5029296875, 0.7239453125, 0.4921875, 0.2727994791666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：260px 結果を受け止め 次の動作や場所へ切り替える 次=00-yard:1
- 感情・意図：発話相手へ求めること：KOH dries his empty hands after washing his own breakfast plate, then reaches toward ordinary headset on shelf; clean plate is in drain rack, no fantasy item in Japan.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航（心）／thought／independent
```
今日は
ちゃんと聞こう
```

### 006 00-yard:1

- 絵・新しい理解：ミルトへ戻った航が右掌へ視線を落とし 顔を曇らせる 掌の傷は次の小袋のカットで確かめる
- 接続：00-japan:2の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：82% right 枠=thin 表示窓=[0.507, 0.336, 0.484, 0.19]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：ミルトの安全広場に再接続 右掌の昨日の擦り傷を見つける 剣は左腰に納刀 盾なし。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航（心）／thought／independent
```
まだ
残ってる
```

### 007 00-yard:1-added-1

- 絵・新しい理解：左掌に使えなかった銅貨が二枚 右掌の擦り傷をかばって小袋へ戻す 日本へ銅貨を運ばない
- 接続：00-yard:1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：92% left 枠=thin 表示窓=[0.00390625, 0.3359375, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：110px 結果を受け止め 次の動作や場所へ切り替える 次=00-yard:2
- 感情・意図：発話相手へ求めること：左掌に使えなかった銅貨が二枚 右掌の擦り傷をかばって小袋へ戻す 日本へ銅貨を運ばない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航（心）／thought／independent
```
パンも
買えなかった
```

### 008 00-yard:2

- 絵・新しい理解：安全広場から訓練場へ歩いて来た航 リゼは予備の木盾を点検 航の手に気づく
- 接続：00-yard:1-added-1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：78% right 枠=thin 表示窓=[0.50390625, 0.6692708333333334, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：安全広場から訓練場へ歩いて来た航 リゼは予備の木盾を点検 航の手に気づく。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
来たね
手はどう？
```

### 009 00-yard:2-added-1

- 絵・新しい理解：リゼは航の右掌の擦り傷を見て確かめる 触れて治療する魔法は使わない
- 接続：00-yard:2の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：94% left 枠=none 表示窓=[0.00390625, 0.6692708333333334, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：リゼは航の右掌の擦り傷を見て確かめる 触れて治療する魔法は使わない。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
握ると
少し痛い
```

### 010 00-yard:2-added-2

- 絵・新しい理解：Medium LIZE looks up from the strap and smiles practically, hand remains on spare shield, her own short sword sheathed.
- 接続：00-yard:2-added-1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.06407552083333333, 0.48828125, 0.27707031249999997]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：120px 結果を受け止め 次の動作や場所へ切り替える 次=01-choice:1
- 感情・意図：発話相手へ求めること：Medium LIZE looks up from the strap and smiles practically, hand remains on spare shield, her own short sword sheathed.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
痛むなら
途中で止めよう
```

### 011 01-choice:1

- 絵・新しい理解：昨日の衝動を自分の言葉で認める
- 接続：00-yard:2-added-2の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：82% right 枠=thin 表示窓=[0.50390625, 0.0026041666666666665, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：昨日の衝動を自分の言葉で認める。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
昨日…
剣を抜きかけた
```

### 012 01-choice:2

- 絵・新しい理解：勝てるかでなく行動の先を尋ねる
- 接続：01-choice:1の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：92% left 枠=thin 表示窓=[0.00390625, 0.0026041666666666665, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：260px 問いの返答を待つ 次=01-choice:3
- 感情・意図：発話相手へ求めること：勝てるかでなく行動の先を尋ねる。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
抜いたあと
どうするつもり
だった？
```

### 013 01-choice:3

- 絵・新しい理解：聞かれて初めて準備のない自分に気づく
- 接続：01-choice:2の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：78% right 枠=none 表示窓=[0.50390625, 0.3359375, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：聞かれて初めて準備のない自分に気づく。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
…わからない
```

### 014 01-choice:4

- 絵・新しい理解：掌と鞘を見て悔しさを言葉にする
- 接続：01-choice:3の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：94% left 枠=thin 表示窓=[0.00390625, 0.3359375, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：200px 結果を受け止め 次の動作や場所へ切り替える 次=01-choice:5
- 感情・意図：発話相手へ求めること：掌と鞘を見て悔しさを言葉にする。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
あの人を
止めたかった
だけで
```

### 015 01-choice:5

- 絵・新しい理解：木剣を選び実行できる範囲へ導く
- 接続：01-choice:4の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：86% right 枠=thin 表示窓=[0.50390625, 0.6692708333333334, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：木剣を選び実行できる範囲へ導く。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
じゃあ今日は
身を守る
ところから
```

### 016 01-choice:6

- 絵・新しい理解：相手を倒すためだけでなく習うことを選ぶ
- 接続：01-choice:5の結果を受ける。ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし
- 幅と配置：82% right 枠=thin 表示窓=[0.00390625, 0.6692708333333334, 0.4921875, 0.328125]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：140px 結果を受け止め 次の動作や場所へ切り替える 次=01-lesson:2
- 感情・意図：発話相手へ求めること：相手を倒すためだけでなく習うことを選ぶ。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
うん
教えて
```

### 017 01-lesson:2

- 絵・新しい理解：Medium LIZE hands him ONE practice shield, short sword in scabbard.
- 接続：01-choice:6の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：92% left 枠=none 表示窓=[0.0048828125, 0.06196614583333333, 0.4892578125, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium LIZE hands him ONE practice shield, short sword in scabbard.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
まずこれ
持ってみて
```

### 018 01-lesson:3

- 絵・新しい理解：Close: KOH awkwardly raises shield left hand and practice sword right, elbows stiff.
- 接続：01-lesson:2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：78% right 枠=thin 表示窓=[0.50390625, 0.3941796875, 0.4912109375, 0.26532552083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Close: KOH awkwardly raises shield left hand and practice sword right, elbows stiff.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
重い……
```

### 019 01-lesson:3-added-1

- 絵・新しい理解：KOH left wrist drops slightly under shield weight, right wooden blade points awkwardly inward, reveals failed physical control rather than heroic stance.
- 接続：01-lesson:3の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：94% left 枠=thin 表示窓=[0.0048828125, 0.3941796875, 0.4892578125, 0.26532552083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH left wrist drops slightly under shield weight, right wooden blade points awkwardly inward, reveals failed physical control rather than heroic stance.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 020 01-lesson:3-added-2

- 絵・新しい理解：LIZE touches shield rim lightly and moves her fingers away so KOH must support it himself.
- 接続：01-lesson:3-added-1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：86% right 枠=thin 表示窓=[0.50390625, 0.725546875, 0.4912109375, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE touches shield rim lightly and moves her fingers away so KOH must support it himself.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
握りだけで
支えないで
```

### 021 01-grip:1

- 絵・新しい理解：Shallow rear of shield close-up: KOH LEFT fingers go around inner wooden grip and forearm under leather strap. Correct wrist anatomy, only ONE grip and shield.
- 接続：01-lesson:3-added-2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：82% right 枠=none 表示窓=[0.0048828125, 0.725546875, 0.4892578125, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Shallow rear of shield close-up: KOH LEFT fingers go around inner wooden grip and forearm under leather strap. Correct wrist anatomy, only ONE grip and shield.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ（画面外）／spoken／independent
```
肘を
固めないで
```

### 022 01-grip:2

- 絵・新しい理解：Medium KOH bends LEFT elbow slightly and lowers shield rim so his RIGHT wooden sword can move freely. LIZE points toward his elbow without pulling his arm.
- 接続：01-grip:1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：92% left 枠=thin 表示窓=[0.5029296875, 0.06255208333333333, 0.4921875, 0.2701302083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH bends LEFT elbow slightly and lowers shield rim so his RIGHT wooden sword can move freely. LIZE points toward his elbow without pulling his arm.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／embedded
```
こう？
```

### 023 01-grip:2-added-1

- 絵・新しい理解：KOH rotates RIGHT wooden sword slowly outward, sees it no longer catches shield rim, tests correction before attack.
- 接続：01-grip:2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：62% left 枠=thin 表示窓=[0.0048828125, 0.06255208333333333, 0.48828125, 0.2701302083333333] 場面空間=space-01-grip:2-added-1 x=0 y=0
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH rotates RIGHT wooden sword slowly outward, sees it no longer catches shield rim, tests correction before attack.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
右手が
動くようになった
```

### 024 01-grip:3

- 絵・新しい理解：Shallow boots on stone dust then shoulders: KOH feet a little staggered, shield left, wooden sword right, eyes look across top rim at LIZE.
- 接続：01-grip:2-added-1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：34% right 枠=thin 表示窓=[0.5029296875, 0.39673177083333333, 0.4921875, 0.2621223958333333] 場面空間=space-01-grip:2-added-1 x=66 y=130.4259528
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Shallow boots on stone dust then shoulders: KOH feet a little staggered, shield left, wooden sword right, eyes look across top rim at LIZE.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
相手と足元
両方見るの
```

### 025 01-grip:3-added-1

- 絵・新しい理解：LIZE takes one unhurried sideways step; KOH tracks her shoulder and his own planted foot together without striking, understanding demonstrated.
- 接続：01-grip:3の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：86% right 枠=none 表示窓=[0.0048828125, 0.39673177083333333, 0.48828125, 0.2621223958333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：LIZE takes one unhurried sideways step; KOH tracks her shoulder and his own planted foot together without striking, understanding demonstrated.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 026 02-distance:1

- 絵・新しい理解：Shallow foot close-up: KOH takes kendo stance, tries to step into range.
- 接続：01-grip:3-added-1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：62% left 枠=thin 表示窓=[0.5029296875, 0.7250130208333334, 0.4921875, 0.2717317708333333] 場面空間=space-02-distance:1 x=0 y=0
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Shallow foot close-up: KOH takes kendo stance, tries to step into range.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航（心）／thought／independent
```
この間合いなら
```

### 027 02-distance:1-added-1

- 絵・新しい理解：KOH sees LIZE sword tip closer and reflexively brings LEFT hand toward his RIGHT wooden hilt; shield strap still on left forearm, old kendo habit creates obstruction.
- 接続：02-distance:1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：34% right 枠=thin 表示窓=[0.0048828125, 0.7250130208333334, 0.48828125, 0.2717317708333333] 場面空間=space-02-distance:1 x=66 y=130.15796547619047
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH sees LIZE sword tip closer and reflexively brings LEFT hand toward his RIGHT wooden hilt; shield strap still on left forearm, old kendo habit creates obstruction.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 028 02-distance:2

- 絵・新しい理解：Diagonal dynamic action: LIZE lightly shifts his shield aside with wooden sword, controls him without injury. KOH reflexively reverts to his real-world TWO-HANDED kendo grip; shield hangs awkwardly from LEFT forearm and obstructs his RIGHT arm. This is the failed habit the next retry corrects, not a new correct stance.
- 接続：02-distance:1-added-1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：78% right 枠=thin 表示窓=[0.5048828125, 0.06805989583333333, 0.490234375, 0.29522135416666667]
- 音：新しく鳴る コン 動作の接点へ置き 前の音と混同しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Diagonal dynamic action: LIZE lightly shifts his shield aside with wooden sword, controls him without injury. KOH reflexively reverts to his real-world TWO-HANDED kendo grip; shield hangs awkwardly from LEFT forearm and obstructs his RIGHT arm. This is the failed habit the next retry corrects, not a new correct stance.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 029 02-distance:3

- 絵・新しい理解：Large KOH surprised face, shield fouls his right arm.
- 接続：02-distance:2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：94% left 枠=none 表示窓=[0.0048828125, 0.06805989583333333, 0.490234375, 0.29522135416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：130px 結果を受け止め 次の動作や場所へ切り替える 次=02-distance:3-added-1
- 感情・意図：発話相手へ求めること：Large KOH surprised face, shield fouls his right arm.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ（画面外）／spoken／independent
```
剣だけを
見ないで
```

### 030 02-distance:3-added-1

- 絵・新しい理解：KOH looks down at shield catching his own right arm and lowers wooden blade; recognizes his own habit caused failure.
- 接続：02-distance:3の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：86% right 枠=thin 表示窓=[0.5048828125, 0.42908854166666666, 0.490234375, 0.2701302083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH looks down at shield catching his own right arm and lowers wooden blade; recognizes his own habit caused failure.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
いつもの握りに
戻ってた
```

### 031 02-distance:3-added-2

- 絵・新しい理解：LIZE lowers her practice sword and lets him reset rather than attacks again.
- 接続：02-distance:3-added-1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.42908854166666666, 0.490234375, 0.2701302083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE lowers her practice sword and lets him reset rather than attacks again.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
盾の場所を
残して動いて
```

### 032 02-retry:1

- 絵・新しい理解：Medium KOH breathes out, deliberately lowers the LEFT shield a little and places RIGHT wooden sword outside shield edge; embarrassed but determined.
- 接続：02-distance:3-added-2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：92% left 枠=thin 表示窓=[0.5048828125, 0.7581119791666666, 0.490234375, 0.23863281249999999]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH breathes out, deliberately lowers the LEFT shield a little and places RIGHT wooden sword outside shield edge; embarrassed but determined.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
もう一回
いい？
```

### 033 02-retry:2

- 絵・新しい理解：Large diagonal controlled contact: LIZE wooden practice sword gently touches KOH shield rim, KOH shifts LEFT boot half a step back, shield not fused with right hand, no explosive magic.
- 接続：02-retry:1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：78% right 枠=none 表示窓=[0.0048828125, 0.7581119791666666, 0.490234375, 0.23863281249999999]
- 音：新しく鳴る コン 動作の接点へ置き 前の音と混同しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Large diagonal controlled contact: LIZE wooden practice sword gently touches KOH shield rim, KOH shifts LEFT boot half a step back, shield not fused with right hand, no explosive magic.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 034 02-retry:2-added-1

- 絵・新しい理解：KOH keeps shield up AFTER the single touch, prevents reflexive pursuit; he looks at LIZE and his feet, breathing returns.
- 接続：02-retry:2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：94% left 枠=thin 表示窓=[0.5048828125, 0.06196614583333333, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH keeps shield up AFTER the single touch, prevents reflexive pursuit; he looks at LIZE and his feet, breathing returns.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 035 02-retry:2-added-2

- 絵・新しい理解：KOH asks why she did not hit harder; curiosity now tied to successful first receive.
- 接続：02-retry:2-added-1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.06196614583333333, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH asks why she did not hit harder; curiosity now tied to successful first receive.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
強く来たら
どうなる？
```

### 036 02-retry:2-added-3

- 絵・新しい理解：LIZE states novice limit and practical need to move instead of claiming invincible blocking.
- 接続：02-retry:2-added-2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：82% right 枠=thin 表示窓=[0.5048828125, 0.395, 0.490234375, 0.2690625]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE states novice limit and practical need to move instead of claiming invincible blocking.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
全部は受けない
危ない時は離れる
```

### 037 02-retry:3

- 絵・新しい理解：Shallow LIZE approving face, her wooden sword lowered after one successful touch. KOH remains a novice, no grand victory.
- 接続：02-retry:2-added-3の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：92% left 枠=none 表示窓=[0.0048828125, 0.395, 0.490234375, 0.2690625]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：180px 結果を受け止め 次の動作や場所へ切り替える 次=02-rest:1
- 感情・意図：発話相手へ求めること：Shallow LIZE approving face, her wooden sword lowered after one successful touch. KOH remains a novice, no grand victory.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
今の感じ
```

### 038 02-rest:1

- 絵・新しい理解：Close KOH LEFT hand trembles mildly as he lowers borrowed shield onto bench. Not a severe injury. Sweat at temple, shoulders relax.
- 接続：02-retry:3の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：62% left 枠=thin 表示窓=[0.5048828125, 0.7292838541666666, 0.490234375, 0.2674609375] 場面空間=space-02-rest:1 x=0 y=0
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Close KOH LEFT hand trembles mildly as he lowers borrowed shield onto bench. Not a severe injury. Sweat at temple, shoulders relax.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
腕が
震える……
```

### 039 02-rest:1-added-1

- 絵・新しい理解：KOH tries to raise LEFT wrist once more, stops when it trembles, chooses to set shield down; not another training failure counted as a repeat lesson.
- 接続：02-rest:1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：34% right 枠=thin 表示窓=[0.0048828125, 0.7292838541666666, 0.490234375, 0.2674609375] 場面空間=space-02-rest:1 x=66 y=128.62266812749004
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH tries to raise LEFT wrist once more, stops when it trembles, chooses to set shield down; not another training failure counted as a repeat lesson.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 040 02-rest:2

- 絵・新しい理解：Medium KOH sits and drinks from ONE plain water flask; LIZE rests beside bench rather than pushes him immediately back to combat.
- 接続：02-rest:1-added-1の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：86% right 枠=thin 表示窓=[0.5048828125, 0.06266927083333333, 0.490234375, 0.27066406249999997]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH sits and drinks from ONE plain water flask; LIZE rests beside bench rather than pushes him immediately back to combat.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
休むのも
練習
```

### 041 02-rest:2-added-1

- 絵・新しい理解：KOH wipes sweat with empty right sleeve and watches other local trainees take turns, recognizes practice is ordinary work too.
- 接続：02-rest:2の結果を受ける。同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし
- 幅と配置：82% right 枠=none 表示窓=[0.0048828125, 0.06266927083333333, 0.490234375, 0.27066406249999997]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：150px 結果を受け止め 次の動作や場所へ切り替える 次=02-change:1
- 感情・意図：発話相手へ求めること：KOH wipes sweat with empty right sleeve and watches other local trainees take turns, recognizes practice is ordinary work too.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
俺だけ
すぐ疲れるのかと
思った
```

### 042 02-change:1

- 絵・新しい理解：Shallow KOH returns ONE wooden practice sword to shared bench beside the other spare practice tools, not holding steel yet. Shield rests at bench edge.
- 接続：02-rest:2-added-1の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：92% left 枠=thin 表示窓=[0.5048828125, 0.397734375, 0.490234375, 0.2637239583333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow KOH returns ONE wooden practice sword to shared bench beside the other spare practice tools, not holding steel yet. Shield rests at bench edge.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 043 02-change:2

- 絵・新しい理解：Medium KOH uses RIGHT hand to draw his OWN plain straight steel sword briefly from brown scabbard, LEFT holds scabbard, recognizes heavier weight. No shield in hands during this check.
- 接続：02-change:1の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.397734375, 0.490234375, 0.2637239583333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH uses RIGHT hand to draw his OWN plain straight steel sword briefly from brown scabbard, LEFT holds scabbard, recognizes heavier weight. No shield in hands during this check.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
こっちは
もっと重い
```

### 044 02-change:2-added-1

- 絵・新しい理解：KOH compares the REAL steel edge against wooden practice blade on bench, pulls steel blade away from people and resheathes with care, no speech or magic.
- 接続：02-change:2の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：94% left 枠=thin 表示窓=[0.5048828125, 0.7271484375, 0.490234375, 0.26959635416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH compares the REAL steel edge against wooden practice blade on bench, pulls steel blade away from people and resheathes with care, no speech or magic.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 045 02-change:3

- 絵・新しい理解：Medium KOH has resheathed steel sword and picks the ONE spare wooden shield up with LEFT hand for patrol. LIZE points to this specific bench, explains ownership and return place.
- 接続：02-change:2-added-1の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：86% right 枠=none 表示窓=[0.0048828125, 0.7271484375, 0.490234375, 0.26959635416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH has resheathed steel sword and picks the ONE spare wooden shield up with LEFT hand for patrol. LIZE points to this specific bench, explains ownership and return place.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
盾は私の予備
帰ったらここへ
```

### 046 02-change:3-added-1

- 絵・新しい理解：KOH looks at borrowed shield rim and asks owner before leaving, steel sheathed at LEFT hip.
- 接続：02-change:3の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：82% right 枠=thin 表示窓=[0.501953125, 0.06419270833333333, 0.4931640625, 0.27760416666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH looks at borrowed shield rim and asks owner before leaving, steel sheathed at LEFT hip.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
傷つけたら
どうすればいい？
```

### 047 02-change:3-added-2

- 絵・新しい理解：LIZE points to same bench and spare shelf, expects responsibility not perfect untouched gear.
- 接続：02-change:3-added-1の結果を受ける。訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.06419270833333333, 0.4873046875, 0.27760416666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：250px 結果を受け止め 次の動作や場所へ切り替える 次=03-patrol:1
- 感情・意図：発話相手へ求めること：LIZE points to same bench and spare shelf, expects responsibility not perfect untouched gear.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
隠さず見せて
一緒に直すから
```

### 048 03-patrol:1

- 絵・新しい理解：Wide: patrol walks riverbank, steel blade sheathed, water plentiful.
- 接続：02-change:3-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.501953125, 0.4060807291666667, 0.4931640625, 0.26319010416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Wide: patrol walks riverbank, steel blade sheathed, water plentiful.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
足元も見て
私から離れないで
```

### 049 03-patrol:1-added-1

- 絵・新しい理解：Nameless LOCAL guard gray hair dark goatee steel helmet sand scarf brown leather armor asks KOH on river path, ordinary check not hostile NPC.
- 接続：03-patrol:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.0048828125, 0.4060807291666667, 0.4873046875, 0.26319010416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Nameless LOCAL guard gray hair dark goatee steel helmet sand scarf brown leather armor asks KOH on river path, ordinary check not hostile NPC.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 兵士／spoken／independent
```
巡回は
初めて？
```

### 050 03-patrol:1-added-2

- 絵・新しい理解：KOH nods, LEFT shield slung RIGHT hand empty near own sheathed steel, answers guard as person.
- 接続：03-patrol:1-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.501953125, 0.7335546875, 0.4931640625, 0.26319010416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH nods, LEFT shield slung RIGHT hand empty near own sheathed steel, answers guard as person.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
はい
足元も見ます
```

### 051 03-patrol:2

- 絵・新しい理解：Small close: fresh claw tracks in mud under reeds, ominous but not gore.
- 接続：03-patrol:1-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：62% left 枠=thin 表示窓=[0.0048828125, 0.7335546875, 0.4873046875, 0.26319010416666666] 場面空間=space-03-patrol:2 x=0 y=0
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Small close: fresh claw tracks in mud under reeds, ominous but not gore.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 052 03-patrol:2-added-1

- 絵・新しい理解：LIZE crouches beside fresh pawprint without touching dangerous reeds, compares it with nearby river mud, healthy water behind.
- 接続：03-patrol:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：34% right 枠=thin 表示窓=[0.5078125, 0.07087239583333332, 0.4873046875, 0.3080338541666667] 場面空間=space-03-patrol:2 x=66 y=127.32974789579158
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE crouches beside fresh pawprint without touching dangerous reeds, compares it with nearby river mud, healthy water behind.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
川へ来るのは
人だけじゃない
```

### 053 03-patrol:3

- 絵・新しい理解：Medium: impulsive red-haired PLAYER traveler runs past the patrol with flashy steel sword.
- 接続：03-patrol:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=none 表示窓=[0.5078125, 0.43627604166666667, 0.4873046875, 0.2316927083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium: impulsive red-haired PLAYER traveler runs past the patrol with flashy steel sword.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 帰還者／spoken／embedded
```
任せろ！
```

### 054 03-patrol:3-added-1

- 絵・新しい理解：KOH reaches empty RIGHT hand toward red-player back, asks him to wait; local guard and LIZE still together on path.
- 接続：03-patrol:3の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：94% left 枠=thin 表示窓=[0.0048828125, 0.43627604166666667, 0.4931640625, 0.2316927083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH reaches empty RIGHT hand toward red-player back, asks him to wait; local guard and LIZE still together on path.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
待って！
まだ何がいるか…
```

### 055 03-listen:1

- 絵・新しい理解：Shallow empty reeds shiver near muddy path, only grass and moving leaves. A SINGLE ガサ… inscription starts at right side of reeds and extends toward panel border. No eyes or claws or creature silhouette yet.
- 接続：03-patrol:3-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：86% right 枠=thin 表示窓=[0.5078125, 0.7324869791666666, 0.4873046875, 0.26425781249999997]
- 音：新しく鳴る ガサ… 草の原画に一度だけ 以後は同じ音の点へ減衰
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow empty reeds shiver near muddy path, only grass and moving leaves. A SINGLE ガサ… inscription starts at right side of reeds and extends toward panel border. No eyes or claws or creature silhouette yet.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 056 03-listen:2

- 絵・新しい理解：Small KOH eye-and-left-shield close-up reacts to the offscreen rustle as he slips the borrowed shield from its walking sling onto LEFT forearm; red-haired bronze-armored traveler back only in farther edge, turning ahead. Continue the same sound with faint trailing … into large white bottom fade, no second complete inscription. No visible beast.
- 接続：03-listen:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.7324869791666666, 0.4931640625, 0.26425781249999997]
- 音：前の草の音が続く 追加のガサを描かず 薄い点が止まるまで 警戒する目と手を優先
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Small KOH eye-and-left-shield close-up reacts to the offscreen rustle as he slips the borrowed shield from its walking sling onto LEFT forearm; red-haired bronze-armored traveler back only in farther edge, turning ahead. Continue the same sound with faint trailing … into large white bottom fade, no second complete inscription. No visible beast.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 057 03-listen:2-added-1

- 絵・新しい理解：LIZE raises empty RIGHT fingers to stop patrol, listens toward grass, her own short sword still sheathed. ONE faint trailing dots from grass sound can continue, no new ガサ and no creature.
- 接続：03-listen:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=none 表示窓=[0.501953125, 0.06290364583333333, 0.4931640625, 0.2717317708333333]
- 音：前の草の音が続く 追加のガサを描かず 薄い点が止まるまで 警戒する目と手を優先
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：LIZE raises empty RIGHT fingers to stop patrol, listens toward grass, her own short sword still sheathed. ONE faint trailing dots from grass sound can continue, no new ガサ and no creature.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 058 03-listen:2-added-2

- 絵・新しい理解：KOH shifts one boot onto firmer path so wounded guard will later have space behind him; LEFT shield ready, RIGHT hand on own sheathed hilt. No advance or monster shown.
- 接続：03-listen:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.06290364583333333, 0.4873046875, 0.2717317708333333]
- 音：前の草の音が続く 追加のガサを描かず 薄い点が止まるまで 警戒する目と手を優先
- 余白：900px 草の音と停止の反応を受け 獣の姿を下で初めて見せる 次=04-beast:1
- 感情・意図：新しい動作または反応：KOH shifts one boot onto firmer path so wounded guard will later have space behind him; LEFT shield ready, RIGHT hand on own sheathed hilt. No advance or monster shown.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 059 04-beast:1

- 絵・新しい理解：Large angled action shot: lean dark riverwolf-like monster leaps from reeds at the impulsive red-haired PLAYER; KOH in foreground frightened, shield held low, LIZE already reacts. Not the black-horn guardian.
- 接続：03-listen:2-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.501953125, 0.3973958333333333, 0.4931640625, 0.25625]
- 音：新しく鳴る ガッ 動作の接点へ置き 前の音と混同しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Large angled action shot: lean dark riverwolf-like monster leaps from reeds at the impulsive red-haired PLAYER; KOH in foreground frightened, shield held low, LIZE already reacts. Not the black-horn guardian.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 060 04-beast:2

- 絵・新しい理解：Shallow immediate result: the red-haired PLAYER avatar dissolves into pale construction light after the claw strike, with his steel sword falling into mud. The LOCAL guardsman tried to cover him and receives a small non-graphic scratch on his RIGHT forearm; KOH sees the guard crouch. No corpse, no injury to a Japanese person, no HUD and no dialogue.
- 接続：04-beast:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.3973958333333333, 0.4873046875, 0.25625]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：200px 結果を受け止め 次の動作や場所へ切り替える 次=04-beast:2-added-1
- 感情・意図：新しい動作または反応：Shallow immediate result: the red-haired PLAYER avatar dissolves into pale construction light after the claw strike, with his steel sword falling into mud. The LOCAL guardsman tried to cover him and receives a small non-graphic scratch on his RIGHT forearm; KOH sees the guard crouch. No corpse, no injury to a Japanese person, no HUD and no dialogue.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 061 04-beast:2-added-1

- 絵・新しい理解：KOH turns sharply from fading player construction light to LOCAL guard physical RIGHT forearm wound, chooses real hurt person rather than vanished avatar.
- 接続：04-beast:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：82% right 枠=none 表示窓=[0.501953125, 0.7207421875, 0.4931640625, 0.27600260416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH turns sharply from fading player construction light to LOCAL guard physical RIGHT forearm wound, chooses real hurt person rather than vanished avatar.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 062 04-find:1

- 絵・新しい理解：Shallow dropped red-player steel sword lies on mud near reeds, not vanished and not automatically returned. A boot of the injured LOCAL guard braces beside it; his RIGHT forearm held close, blood only a tiny restrained mark.
- 接続：04-beast:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.7207421875, 0.4873046875, 0.27600260416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow dropped red-player steel sword lies on mud near reeds, not vanished and not automatically returned. A boot of the injured LOCAL guard braces beside it; his RIGHT forearm held close, blood only a tiny restrained mark.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 063 05-defense:1

- 絵・新しい理解：Medium: KOH steps LEFT beside local wounded guard, raises borrowed shield, right hand grips sword.
- 接続：04-find:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.06442708333333333, 0.4892578125, 0.27867187499999996]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium: KOH steps LEFT beside local wounded guard, raises borrowed shield, right hand grips sword.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
その人の前に！
```

### 064 05-defense:2

- 絵・新しい理解：Two quick close-up moments right-to-left within ONE shallow row: shield blocks claw; LIZE gathers pale wind around short sword.
- 接続：05-defense:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：94% left 枠=thin 表示窓=[0.50390625, 0.405390625, 0.4912109375, 0.2541145833333333]
- 音：新しく鳴る ガン 動作の接点へ置き 前の音と混同しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Two quick close-up moments right-to-left within ONE shallow row: shield blocks claw; LIZE gathers pale wind around short sword.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 065 05-defense:3

- 絵・新しい理解：Wide: LIZE pushes beast back with wind and KOH keeps injured guard behind shield.
- 接続：05-defense:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.50390625, 0.725546875, 0.4912109375, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：100px 結果を受け止め 次の動作や場所へ切り替える 次=05-recover:1
- 感情・意図：発話相手へ求めること：Wide: LIZE pushes beast back with wind and KOH keeps injured guard behind shield.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／embedded
```
今離れて！
```

### 066 05-recover:1

- 絵・新しい理解：Wide wolf retreats physically into reeds on LEFT far bank edge, same dark lean animal with tail, visible direction and diminishing distance. LIZE sword down but alert, no creature dissolved or respawned.
- 接続：05-defense:3の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.725546875, 0.4892578125, 0.27119791666666665]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Wide wolf retreats physically into reeds on LEFT far bank edge, same dark lean animal with tail, visible direction and diminishing distance. LIZE sword down but alert, no creature dissolved or respawned.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／embedded
```
追わないで
```

### 067 05-recover:1-added-1

- 絵・新しい理解：KOH begins one step after retreating wolf but stops when LIZE warns, chooses guard over pursuit and turns back.
- 接続：05-recover:1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：92% left 枠=thin 表示窓=[0.5048828125, 0.06196614583333333, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH begins one step after retreating wolf but stops when LIZE warns, chooses guard over pursuit and turns back.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 068 05-recover:2

- 絵・新しい理解：Medium LOCAL guard uses healthy LEFT hand to press cloth against wounded RIGHT forearm. Polearm rests upright against a tree during this pause. KOH left shield low and own sword resheathed stands beside him.
- 接続：05-recover:1-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.06196614583333333, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium LOCAL guard uses healthy LEFT hand to press cloth against wounded RIGHT forearm. Polearm rests upright against a tree during this pause. KOH left shield low and own sword resheathed stands beside him.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
歩けますか
```

### 069 05-recover:2-added-1

- 絵・新しい理解：LOCAL guard nods that he can walk, healthy LEFT hand presses RIGHT injury cloth, polearm leans beside tree during pause.
- 接続：05-recover:2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：94% left 枠=none 表示窓=[0.5048828125, 0.3948828125, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LOCAL guard nods that he can walk, healthy LEFT hand presses RIGHT injury cloth, polearm leans beside tree during pause.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 兵士／spoken／independent
```
ゆっくりなら
歩ける
```

### 070 05-recover:2-added-2

- 絵・新しい理解：KOH resheathes his steel sword and gently supports the guard above the injured RIGHT forearm at his RIGHT upper arm with his free RIGHT hand. He does not press the wound. LEFT shield lowered. LIZE temporarily carries the polearm; before walking on, she returns it to the guard healthy LEFT hand.
- 接続：05-recover:2-added-1の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.3948828125, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：KOH resheathes his steel sword and gently supports the guard above the injured RIGHT forearm at his RIGHT upper arm with his free RIGHT hand. He does not press the wound. LEFT shield lowered. LIZE temporarily carries the polearm; before walking on, she returns it to the guard healthy LEFT hand.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 071 05-recover:3

- 絵・新しい理解：Wide three walk back toward visible Milt gate at same river path. KOH matches LOCAL guard pace, LIZE walks outer side keeping watch. Dropped red-player sword remains behind in mud near reeds, not magically collected.
- 接続：05-recover:2-added-2の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.5048828125, 0.72875, 0.490234375, 0.2679947916666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：260px 結果を受け止め 次の動作や場所へ切り替える 次=05-recover:3-added-1
- 感情・意図：新しい動作または反応：Wide three walk back toward visible Milt gate at same river path. KOH matches LOCAL guard pace, LIZE walks outer side keeping watch. Dropped red-player sword remains behind in mud near reeds, not magically collected.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 072 05-recover:3-added-1

- 絵・新しい理解：KOH and the injured guard pause on the clinic steps. SENA takes over the guard care from the doorway and sends KOH to get water nearby. The guard is no longer left in danger, and the next scene is the nearby safe square.
- 接続：05-recover:3の結果を受ける。ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常
- 幅と配置：100% center 枠=none 表示窓=[0.0048828125, 0.72875, 0.490234375, 0.2679947916666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH and the injured guard pause on the clinic steps. SENA takes over the guard care from the doorway and sends KOH to get water nearby. The guard is no longer left in danger, and the next scene is the nearby safe square.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- セナ／spoken／independent
```
ここで診るよ
水を飲んで
おいで
```

### 073 06-returner:1

- 絵・新しい理解：Wide: the red-haired PLAYER reappears in plain replacement clothes, weapon lost, KOH and AKARI nearby.
- 接続：05-recover:3-added-1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：78% right 枠=none 表示窓=[0.5029296875, 0.06184895833333333, 0.4921875, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Wide: the red-haired PLAYER reappears in plain replacement clothes, weapon lost, KOH and AKARI nearby.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 帰還者／spoken／independent
```
戻れた
でも剣がない
```

### 074 06-returner:2

- 絵・新しい理解：Close KOH listens with relief, sword sheathed and shield lowered.
- 接続：06-returner:1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：94% left 枠=thin 表示窓=[0.0048828125, 0.06184895833333333, 0.48828125, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Close KOH listens with relief, sword sheathed and shield lowered.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
さっきの人…
戻れたんだ
```

### 075 06-returner:3

- 絵・新しい理解：AKARI in orange game jacket checks a readable blue HUD only for herself.
- 接続：06-returner:2の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：86% right 枠=thin 表示窓=[0.5029296875, 0.3945833333333333, 0.4921875, 0.2701302083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：AKARI in orange game jacket checks a readable blue HUD only for herself.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 灯里／spoken／independent
```
身体を
作り直すんだって
```

### 076 06-returner:3-added-1

- 絵・新しい理解：KOH looks at same regenerated red-haired player wrists, asks whether his earlier gear has returned.
- 接続：06-returner:3の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.3945833333333333, 0.48828125, 0.2701302083333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH looks at same regenerated red-haired player wrists, asks whether his earlier gear has returned.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
剣や鎧も
一緒に戻る？
```

### 077 06-supply:1

- 絵・新しい理解：Medium local supply clerk points to a modest waiting bench and almost empty replacement-clothes shelf; gives plain spare boot pair to regenerated PLAYER in beige clothes, not his lost armor or sword.
- 接続：06-returner:3-added-1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：92% left 枠=none 表示窓=[0.5029296875, 0.7298177083333334, 0.4921875, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium local supply clerk points to a modest waiting bench and almost empty replacement-clothes shelf; gives plain spare boot pair to regenerated PLAYER in beige clothes, not his lost armor or sword.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 係の人／spoken／independent
```
次の身体も
用意がいる
```

### 078 06-supply:1-added-1

- 絵・新しい理解：Local supply clerk indicates waiting bench and almost empty spare shelf, makes finite supply consequence practical.
- 接続：06-supply:1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.7298177083333334, 0.48828125, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Local supply clerk indicates waiting bench and almost empty spare shelf, makes finite supply consequence practical.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 係の人／spoken／independent
```
予備がなければ
待ってもらうよ
```

### 079 06-supply:2

- 絵・新しい理解：Shallow regenerated red-haired PLAYER looks at empty hands and plain clothes, remembers his weapon still physically at riverbank.
- 接続：06-supply:1-added-1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：94% left 枠=thin 表示窓=[0.50390625, 0.06220052083333333, 0.4912109375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Shallow regenerated red-haired PLAYER looks at empty hands and plain clothes, remembers his weapon still physically at riverbank.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 帰還者／spoken／independent
```
剣は川に
落ちたままだ
```

### 080 06-supply:2-added-1

- 絵・新しい理解：Regenerated player looks toward river path outside gate then touches his plain replacement sleeve, hears own loss as practical task.
- 接続：06-supply:2の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：86% right 枠=thin 表示窓=[0.0048828125, 0.06220052083333333, 0.4892578125, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Regenerated player looks toward river path outside gate then touches his plain replacement sleeve, hears own loss as practical task.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 帰還者／spoken／independent
```
ひとりじゃ
取りに行けないな
```

### 081 06-supply:3

- 絵・新しい理解：Medium AKARI lowers her own brass communicator, speaks to KOH with relief for person in Japan, her wooden bow remains on back.
- 接続：06-supply:2-added-1の結果を受ける。町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物
- 幅と配置：82% right 枠=none 表示窓=[0.50390625, 0.3945442708333333, 0.4912109375, 0.2610546875]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：230px 結果を受け止め 次の動作や場所へ切り替える 次=07-local:1
- 感情・意図：発話相手へ求めること：Medium AKARI lowers her own brass communicator, speaks to KOH with relief for person in Japan, her wooden bow remains on back.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 灯里／spoken／independent
```
日本の身体は
無事だって
```

### 082 07-local:1

- 絵・新しい理解：Medium KOH looks toward the LOCAL guard, worried.
- 接続：06-supply:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.3945442708333333, 0.4892578125, 0.2610546875]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH looks toward the LOCAL guard, worried.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
兵士さんの傷も
作り直せば
治る？
```

### 083 07-local:2

- 絵・新しい理解：SENA calm close-up, one clean bandage in hands.
- 接続：07-local:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=thin 表示窓=[0.50390625, 0.72234375, 0.4912109375, 0.2744010416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：280px 結果を受け止め 次の動作や場所へ切り替える 次=07-local:2-added-1
- 感情・意図：発話相手へ求めること：SENA calm close-up, one clean bandage in hands.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- セナ／spoken／independent
```
この人には
この身体しか
ないんだ
```

### 084 07-local:2-added-1

- 絵・新しい理解：KOH looks at SAME guard right forearm and asks about tomorrow rather than revival again.
- 接続：07-local:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：94% left 枠=thin 表示窓=[0.0048828125, 0.72234375, 0.4892578125, 0.2744010416666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH looks at SAME guard right forearm and asks about tomorrow rather than revival again.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
明日の巡回は
どうするんですか
```

### 085 07-local:2-added-2

- 絵・新しい理解：LOCAL guard rests bandaged RIGHT hand on lap, accepts actual recovery time.
- 接続：07-local:2-added-1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：86% right 枠=none 表示窓=[0.501953125, 0.06243489583333334, 0.4931640625, 0.26959635416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LOCAL guard rests bandaged RIGHT hand on lap, accepts actual recovery time.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 兵士／spoken／independent
```
治るまで
休むしかないな
```

### 086 07-local:3

- 絵・新しい理解：LIZE tightens bandage, clear difference to player; tired expression.
- 接続：07-local:2-added-2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.06243489583333334, 0.4873046875, 0.26959635416666666]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE tightens bandage, clear difference to player; tired expression.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
明日は休んで
巡回は代わるから
```

### 087 07-clinic:1

- 絵・新しい理解：Shallow LIZE moves ONE patrol token from tomorrow active row to a reserve peg beside the clinic board. No readable unexplained bureaucratic chart, no giant UI, no promise to heal instantly.
- 接続：07-local:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：92% left 枠=thin 表示窓=[0.501953125, 0.3971354166666667, 0.4931640625, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Shallow LIZE moves ONE patrol token from tomorrow active row to a reserve peg beside the clinic board. No readable unexplained bureaucratic chart, no giant UI, no promise to heal instantly.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 088 07-clinic:2

- 絵・新しい理解：Medium SENA closes ONE wooden medicine box gently beside seated LOCAL guard, addresses KOH with practical thanks. Guard rests right bandaged arm on lap, same gray hair and goatee.
- 接続：07-clinic:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.3971354166666667, 0.4873046875, 0.2669270833333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium SENA closes ONE wooden medicine box gently beside seated LOCAL guard, addresses KOH with practical thanks. Guard rests right bandaged arm on lap, same gray hair and goatee.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- セナ／spoken／independent
```
休ませる場所まで
運んでくれて
助かった
```

### 089 07-clinic:2-added-1

- 絵・新しい理解：KOH takes guard empty water cup to clinic washing basin, performs small useful post-rescue task; SENA begins arranging tomorrow medicine, no new medical dose detail.
- 接続：07-clinic:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：94% left 枠=none 表示窓=[0.501953125, 0.7292838541666666, 0.4931640625, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：140px 結果を受け止め 次の動作や場所へ切り替える 次=07-promise:1
- 感情・意図：新しい動作または反応：KOH takes guard empty water cup to clinic washing basin, performs small useful post-rescue task; SENA begins arranging tomorrow medicine, no new medical dose detail.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 090 07-promise:1

- 絵・新しい理解：Close KOH uses plain cloth to wipe mud from ONE wooden shield rim on bench, shield detached from LEFT arm, his own steel sword stays sheathed at belt. No magically repaired cracks.
- 接続：07-clinic:2-added-1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：62% left 枠=thin 表示窓=[0.0048828125, 0.7292838541666666, 0.4873046875, 0.2674609375] 場面空間=space-07-promise:1 x=0 y=0
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：新しい動作または反応：Close KOH uses plain cloth to wipe mud from ONE wooden shield rim on bench, shield detached from LEFT arm, his own steel sword stays sheathed at belt. No magically repaired cracks.。次の行動の理由として見せる。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 発話なし

### 091 07-promise:1-added-1

- 絵・新しい理解：航は借りた盾の縁の小さな欠けを持ち主リゼへ見せる 木は自動で修復しない
- 接続：07-promise:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：34% right 枠=thin 表示窓=[0.5048828125, 0.06208333333333334, 0.490234375, 0.2679947916666667] 場面空間=space-07-promise:1 x=66 y=129.3959507014028
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH shows ONE small scrape on borrowed shield metal rim to LIZE, remembers promised responsibility; wood uncracked until future6.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
縁が
少し欠けた
```

### 092 07-promise:1-added-2

- 絵・新しい理解：LIZE checks rim with empty fingers, relieved rather than scolds; same shield on bench.
- 接続：07-promise:1-added-1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：92% left 枠=thin 表示窓=[0.0048828125, 0.06208333333333334, 0.490234375, 0.2679947916666667]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：LIZE checks rim with empty fingers, relieved rather than scolds; same shield on bench.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
見せてくれて
ありがとう
ここは直せる
```

### 093 07-promise:2

- 絵・新しい理解：Medium KOH looks up from cleaned shield toward LIZE, asks rather than silently claims borrowed property.
- 接続：07-promise:1-added-2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=none 表示窓=[0.5048828125, 0.3952994791666667, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Medium KOH looks up from cleaned shield toward LIZE, asks rather than silently claims borrowed property.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
明日も
借りていい？
```

### 094 07-promise:3

- 絵・新しい理解：Wide LIZE points toward spare shield shelf right above the same bench. KOH places ONE cleaned shield there and removes hand, now shieldless.
- 接続：07-promise:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：100% center 枠=none 表示窓=[0.0048828125, 0.3952994791666667, 0.490234375, 0.2674609375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：400px 結果を受け止め 次の動作や場所へ切り替える 次=08-invitation:1
- 感情・意図：発話相手へ求めること：Wide LIZE points toward spare shield shelf right above the same bench. KOH places ONE cleaned shield there and removes hand, now shieldless.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- リゼ／spoken／independent
```
ここに置いて
次も一緒に
練習しよう
```

### 095 08-invitation:1

- 絵・新しい理解：REI in silver armor and deep red short cloak approaches KOH, sword sheathed, friendly.
- 接続：07-promise:3の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：86% right 枠=thin 表示窓=[0.5048828125, 0.7282161458333334, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：REI in silver armor and deep red short cloak approaches KOH, sword sheathed, friendly.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 怜／spoken／independent
```
さっきの盾
よく出せたな
```

### 096 08-invitation:2

- 絵・新しい理解：Close KOH recognizes his admired player, startled but delighted. KOH hands empty, NO shield, own steel sword remains sheathed.
- 接続：08-invitation:1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：82% right 枠=thin 表示窓=[0.0048828125, 0.7282161458333334, 0.490234375, 0.2685286458333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：Close KOH recognizes his admired player, startled but delighted. KOH hands empty, NO shield, own steel sword remains sheathed.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／embedded
```
……レイさん？
```

### 097 08-invitation:2-added-1

- 絵・新しい理解：KOH straightens posture, recognizes REI from familiar raid videos, now asks as nervous youth, hands empty no shield.
- 接続：08-invitation:2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：92% left 枠=none 表示窓=[0.50390625, 0.06641927083333332, 0.4912109375, 0.2877473958333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：KOH straightens posture, recognizes REI from familiar raid videos, now asks as nervous youth, hands empty no shield.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 航／spoken／independent
```
動画で
見てました
```

### 098 08-invitation:2-added-2

- 絵・新しい理解：REI smiles and gestures toward real training yard instead of superiority or secret chosen-one favor.
- 接続：08-invitation:2-added-1の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：78% right 枠=thin 表示窓=[0.0048828125, 0.06641927083333332, 0.4892578125, 0.2877473958333333]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：追加の純余白なし 動作または応酬を近く読む
- 感情・意図：発話相手へ求めること：REI smiles and gestures toward real training yard instead of superiority or secret chosen-one favor.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 怜／spoken／independent
```
ここでは
一緒に練習しよう
```

### 099 08-invitation:3

- 絵・新しい理解：Large REI offers an open empty hand, a genuine invitation.
- 接続：08-invitation:2-added-2の結果を受ける。町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀
- 幅と配置：100% center 枠=none 表示窓=[0.50390625, 0.4190364583333333, 0.4912109375, 0.265859375]
- 音：効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない
- 余白：330px 結果を受け止め 次の動作や場所へ切り替える 次=end
- 感情・意図：発話相手へ求めること：Large REI offers an open empty hand, a genuine invitation.。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。
- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。
- 怜／spoken／independent
```
討伐隊
一緒に来るか？
```
