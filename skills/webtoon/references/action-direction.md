# 格好よい戦闘をネームから作る

戦闘・アクションのネームや作画を組むとき、「もっと派手に」「枠をはみ出して」「動きが分かるように」と直すときに使う。読者が動きを追え、その主動作で「カッケー！！！」と思えることを目指す。演出の基準は[動きと見せ場のエフェクト](art-prompts.md#動きと見せ場のエフェクト)、ネームの出力と返答待ちは[構成ネームのプレビュー](name-preview.md)に従う。

## 設計前に採用例の画像を見る

『橋上の一歩』は2026-10-09にコマ配置と戦闘エフェクトの方向をユーザーが採用した部分試作。次の連続画像を画像表示ツールで見てから、今回の構成と生成指示を決める。リンクを読むだけで参照済みにしない。

| 連続画像 | 判断に使うところ |
| --- | --- |
| [槍の薙ぎ払いと剣の落下](action-name-preview/review/composition-390-c02.png) | 手前へ伸びる大きな槍と軌道、斜めの枠を跨ぐ身体、脇の小さな反応、失敗の結果までの間 |
| [跳躍から反撃](action-name-preview/review/composition-390-c05.png) | 踏み切りから身体へ続く軌跡、大きな跳躍と小さな反応・着地、一つの接触点へ集まる衝撃と枠外の音 |
| [反撃後の結果と余韻](action-name-preview/review/composition-390-c06.png) | 派手な衝撃が終わり、武器の位置、道が開いたこと、主人公の感情が静かに読める空間 |

小さい幅の見え方は[360pxの跳躍と反撃](action-name-preview/review/composition-360-c05.png)も使う。[実際の読む順と配置](action-name-preview/plan.json)、[実行した画像編集指示](action-name-preview/art-provenance.json)、[表示確認の範囲](action-name-preview/validation.json)を必要に応じて読む。プレビューでは人物・枠・動きのエフェクトを原画に描き、セリフと効果音はHTMLで組んでいる。

24コマ、橋、白黒、剣と槍、同じ配置や寸法を次の作品へコピーするための見本ではない。この例の採用は戦闘の演出方向であり、一話全体の分量や本作画・公開の確認を代わりに済ませるものではない。

## 今回の場面へ移す手順

1. **見せ場と因果を決める。** 何を格好よく見せる瞬間かを一文で決める。直前の判断、動作の起点、進む方向、接触や通過、直後の結果を絵コンテへつなぐ。人物の左右、足場、小道具の数と位置、相手の反応も記録する。
2. **場面全体の空間を組む。** 主動作へ大きな面積を渡し、予備動作、目・手・足の接写、反応、着地や結果を役割に合う面積と位置へ置く。全幅のカードを積むだけにせず、枠なし、横長、ずらした小コマ、斜め、脇の声や音を選ぶ。次の情報を先に見せず、密な動作と待つ区間を分ける。
3. **主動作の原画を作る。** シルエット、身体のひねり、重心、手前と奥の差、カメラの角度を指定する。枠抜けを使うなら原画内の枠と、そこを跨ぐ身体・武器・軌跡を一緒に描く。既存の小さなセルでは収まらない見せ場は専用原画にし、表示窓で突出部分を切らない。
4. **動きの線と音を合わせる。** 起点から軌道、接触や結果へつながる太い帯、速度線、衝撃、砂煙などを選ぶ。薙ぎ払い・跳躍・衝突を描き分け、効果音の発生源と終わる位置を決める。静かな判断や余韻まで埋めず、顔、握り手、武器の輪郭、セリフを残す。
5. **360/390pxで連続して読む。** 主動作だけの拡大画像で済ませず、その前の予兆と後の結果まで確認する。読順、動きの起点と方向、枠抜け、顔と手、武器の数、音とセリフの欠けを見て補修する。見た作例と今回使った判断、実行した指示、表示確認を制作資料へ残す。新しいネームはHTMLを開き、読める画像も会話へ出して返答を待つ。

配置の操作は[場面の空間を組み直す判断](panel-layout.md#矩形の列から場面の空間へ組み直す)、余白は[余白とスクロール](scroll-pacing.md)と[人物を描かない余白](whitespace-example.md)を使う。主動作の数、枠抜けの回数、配置の型を全場面へ固定しない。

## 主動作のラフを生成する指示例

`imagegen` と組み込み `image_gen` で生成する際に、今回の動作と参照の役割へ置き換える。これは文字をHTMLで重ねるネーム用の例。本作画では[作画指示](art-prompts.md)の採用済み文字方式へ戻す。実行したプロンプトを記録し、過去の実行指示を次回用のひな形へ書き換えない。

```text
Asset type: one rough black-and-white manga name image for a smartphone vertical-scroll comic.
Reference roles: [character identity / costume and prop state / drawing style]. Preserve those roles without copying the reference panel grid.
Single moment: [THIS action only]. Stop before [the later reaction or outcome].
Established geography and state: [each character's side, footing, one prop's current location, and the intended travel direction].
Hero moment: make [the chosen action] feel powerful and memorable through [silhouette, body twist, weight shift, foreshortening and camera angle].
Motion: begin at [origin], travel toward [direction], and show [contact or passage appropriate to THIS moment].
Effects: [specific broad wake / speed streaks / dust / impact rays] follow that motion. Anchor them to [foot / weapon / contact / other actual source]; keep [quiet or not-yet-contacted area] clear.
Frame treatment: [borderless / drawn inner oblique frame]. For a breakout, let [specified body or weapon parts and wake] visibly cross the DRAWN inner frame into the surrounding page area. Keep the complete protruding silhouette in the source.
Readable anchors: preserve [face, closed grip, continuous weapon outline, landing cue or other necessary detail]. Do not accidentally duplicate a character, hand, weapon or contact point.
Lettering reserve: keep [the planned speech and sound areas] usable without shrinking the action or hiding its anchors.
Text: no lettering or speech balloons in this rough source; the exact planned speech and sounds will be composed separately in the preview.
```

エフェクトだけを強める編集では、編集対象を先に表示し、保つ人物・ポーズ・武器・背景・枠と、変える軌跡・砂煙・衝撃を分ける。枠抜けをCSSの斜めマスクだけで代用すると身体や武器を切りやすい。原画に描いた突出を保つ表示窓を使い、枠内だけの表示へ戻っていないか確認する。原本を歪めたりPNGを後加工して演出を足したりせず、必要な原画編集には画像生成ツールを使う。

## 直すべき兆候

主動作と接写が同じ大きさで続く、人物カードの幅や左右寄せだけが違う、軌跡が足や武器につながらない、接触前から衝撃が出る、枠抜けが表示窓で消える、派手な線で顔や握り手が読めない、反応や静かな結果まで同じ強さで埋まる場合は見直す。主動作の原画と前後の配置のどちらに原因があるか分け、評価された部分を保って直す。
