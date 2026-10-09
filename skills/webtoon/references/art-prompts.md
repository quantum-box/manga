# 場面ごとの作画指示

画像生成には同じキャラクター仕様と参照画像を渡し、場面固有の構成・状態・伏せる情報を追加する。単に「縦長のWebtoon」と頼むと、全幅の矩形を縦へ積むだけの構成や目的のない均等なコマ列に戻りやすい。横長・横並び・斜めのコマも、会話や動作の役割に合うところで使う。

作画前に[余白とスクロール](scroll-pacing.md)で間の位置を決める。待たせる前後の情報を一枚の漫画ページへ詰めず、今回の素材で見せる範囲だけを生成する。横並びや斜め枠が必要でも、全素材を多段の漫画ページへ固定しない。

日本語の会話は吹き出しとセリフを絵に含めて生成する。縦書きの列指定は[承認された実例](vertical-lettering.md)を参照する。吹き出しの数や位置は各場面の発話と構図から決める。

## 絵柄と感情を別々に指定する

「もっとアニメ風」という要望では、線の明快さ、セル塗りの影、配色、顔の造形、表情の読みやすさを具体化する。武侠という題材だけから写実的な絵柄や豪華な金装飾へ寄せない。今回の題材・爽快感・表情は[感情と行動の実例](emotion-and-causality.md)、生成する表示や効果音は[システム表示の実例](system-and-lettering.md)を参照する。

人物の顔立ち・髪・服・汚れ・持ち物は同一性の条件、眉・口・視線・手の緊張はその場面の感情として指定する。人物参照の不敵な表情まで不変条件にしない。「驚いている」だけでなく、何を見て何が分からず、どの部位に反応が出るかを指示する。

感情が重要な発話は、[セリフの意図と反応](emotion-and-causality.md)を脚本で決め、下の `Dialogue intent` と `Visible acting` へ渡す。発話前の感情、相手へ求めること、言った後の変化を絵の演技へつなぐ。生成モデルにセリフの改作を任せず、確定した全文を渡す。

既存作画の感情を直す場合は、編集対象を先に表示し、変更する眉・瞳・口・姿勢などと、保つ人物・衣服・小道具・背景・構図を分ける。足りない因果は、前後の状態をつなぐ接写や短い動作を追加する。表情を直す指示で武器や拘束の状態まで変えない。

## 動きと見せ場のエフェクト

戦闘・アクションの具体的な構成と生成指示は[格好よい戦闘をネームから作る](action-direction.md)を使う。採用例の画像、場面全体の配置、専用原画の判断、ラフ用の指示例を同梱する。

戦闘では、動きが追えることに加え、主動作で「カッケー！！！」と思える見せ場を作る。何が格好よく映る瞬間かを決め、姿勢、シルエット、重心、遠近感、カメラの角度を組み合わせる。攻撃の大きさだけでなく、相手の強さ、主人公の判断や覚悟が伝わる演技を選ぶ。

エフェクトは発生源、軌道、接触や結果をつなぐ。大きな軌跡の帯、速度線、接触点へ集まる衝撃線、砂煙や火花を、動作・舞台・絵柄に合わせて大胆に使う。薙ぎ払い、踏み切り、武器の衝突を同じ飾りで済ませず、進む方向と力の変化を描き分ける。枠を跨ぐ身体や武器、効果音も選択肢に含め、スマホ幅で読順と見せ場の輪郭を確認する。

全コマを同じ強さで埋めず、予備動作、判断、相手の反応、静かな結果との密度差で主動作を際立たせる。派手な演出でも顔、握り手、武器の連続した輪郭、接触点を読めるままにする。軌跡は線や帯で示し、人物や武器の複製で一本の動作を曖昧にしない。

[『橋上の一歩』の戦闘ネーム](action-name-preview/README.md)は、2026-10-09にコマ配置と動きを示すエフェクトの方向をユーザーが採用した部分試作。[跳躍から反撃の表示例](action-name-preview/review/composition-390-c05.png)で、枠抜け、軌道と接触、前後の反応を確認する。24コマ、白黒の絵柄、橋や武器、一話の分量、本作画への移行を全作品の固定条件にしない。

## 食べ物のある場面

[食欲が伝わる料理と食事](food-art.md)を読み、料理名、実際の食材と調理段階、食欲を伝える形・質感、器と量を生成指示へ追加する。`delicious / highly detailed food` だけに任せず、今回の料理で何を見せると美味しそうかを指定する。同じ料理の調理・配膳・ひと口には共通条件を渡す。料理の接写以外でも、画面に食べ物があれば適用する。

```text
Food: [dish, established ingredients, cooking stage, vessel and portion]. Make it appetizing in the established comic style, readable at phone width.
Appetite cues: [dish-appropriate browning, soft cut surfaces, restrained gloss, sauce thickness, steam or freshness]. Keep the ingredient silhouettes clear.
Texture: Preserve the natural identity of [rice / beans / other ingredients], grouped with soft tonal variation. Avoid dense repetitive bead-like bumps, hole patterns, pinpoint highlights on every grain and excessive foam. Do not replace the actual dish with a generic smooth soup.
Continuity: [same recipe, vessel, ingredient size and current portion]. This asset shows only [cooking / serving / one bite / reaction]; do not add later reactions or extra panels.
```

使わない食材や表現は例から削り、温度や調理法に合う要素を選ぶ。編集では料理を変える範囲と、維持する人物・手・器・文字・背景・コマ割りを分ける。実際の生成指示と確認結果を残し、過去の指示は書き換えない。

## 共通部分の例

```text
Use case: illustration-story.
Asset type: finished art for a smartphone vertical-scroll comic, including final dialogue and speech balloons.
Primary request: [this story and this scene].
Input images: Reference 1 establishes character identity; Reference 2 establishes palette/style. Do not copy their panel layout.
Subject: [identity, clothing, markings and recurring props].
Style/medium: [chosen art direction].
Scene/backdrop: [consistent setting and time].
Camera: [distance: wide / medium / close-up; height and angle; whose viewpoint, if relevant].
Composition: [primary focal element and path to the next beat; reserve the planned balloon area without covering faces, hands or clues].
Text: Render only the specified dialogue, sound effects and in-world display text. Integrate them with the illustration. Speech uses white balloons and true vertical Japanese: upright glyphs, top-to-bottom columns ordered right-to-left. Do not rotate horizontal sentences sideways. No unlisted text or watermark.
Text breaks: Omit Japanese commas and full stops, and sentence-separating commas or periods. Preserve specified expressive marks and meaningful symbols. Use the supplied phrase-boundary line breaks; for vertical dialogue, each line becomes one column. Do not split words or leave a lone particle or final character.
Dialogue: [speaker, exact full text without sentence punctuation and with planned line breaks, balloon reading order, and each vertical column listed in right-to-left order].
Dialogue intent: [for spoken dialogue: what this speaker wants from THIS listener now, their established relationship/register, and any feeling or fact the speaker holds back; for thought: the character's own doubt, wish, realization or decision, with no listener required or invented; omit for assets with no character voice]. Preserve the exact supplied words.
Sound effects: [exact word, producing action/material, position relative to the source, scale and drawn letter style, beginning/continuation/end; or none only when no sound persists, with a reason for quiet]. Keep sounds outside speech/thought balloons; their orientation follows the action, separately from dialogue.
Voice: [spoken / thought; intended listener if any; volume, emotion and breath for THIS utterance].
Visible acting: [for character beats only: the emotional change in THIS moment through the relevant eyeline, brows, mouth, hands, posture or breath; listener response only if included in this beat; any inappropriate default expression to avoid; omit for assets without characters]. Do not add later reactions or automatic tears, sweat or shouting.
Balloon design: [contour, line weight/color, white inner padding, and continuous speech tail or thought dots].
Lettering: Clean printed Japanese manga gothic, dark lettering, generous inset padding, legible after smartphone downscaling. Balloon tails point to the speakers. Do not cover faces or hands.
Constraints: [unchanging identity] and [this scene's prop state].
Avoid: [information not yet revealed], extra props, duplicate characters, watermark.
```

背景の端を同色へ柔らかくつなぐ指示は、連続する場面で必要な場合だけ追加する。全作品を夜や暗色に限定しない。

[吹き出しの実例](speech-balloons.md)に従い、通常の楕円、柔らかな輪郭、揺れる線、太いトゲ、雲形などを発話の役割で選ぶ。参照画像の全吹き出しを同じ形にコピーしない。輪郭だけを直す編集では、セリフ・コマ割り・話者・表情を保つ条件と、変更する線・尾を分けて指示する。

会話の指示では、参照にいる人物を全員描かせず、そのコマで画面内にいる人物・注目する対象と、画面外の話者や聞き手を分ける。場所、左右の関係、姿勢、小道具の状態は前のコマから保つ。[状況と会話の実例](context-and-dialogue.md)のように、反応や返答まで一枚へ詰めず、今回描く発話だけを渡す。接写を理由に新しい場所・動作・人物を足さない。

```text
This panel continues the SAME conversation in the SAME location.
Visible subject: [speaker face / listener reaction / the object being discussed].
Offscreen: [who remains nearby and on which side].
Single beat: [what the reader understands now].
Carry forward: [eyeline, posture, background marker and prop state].
Exact dialogue for THIS panel only: [text, or no dialogue/thought balloons].
Exact sound effects for THIS panel only: [word, source/origin moment, placement and drawn style, beginning/continuation/end; or none only when no sound persists]. Do not use 'silent' for a wordless panel whose sound persists. Do not duplicate the complete inscription in each panel when one sound spans several moments.
Do not include later replies, new locations, or every character from the reference.
```

文字は短い語だけでなく全文を渡す。列分けの一覧を吹き出しへラベルとして描かせないよう、全文と配置の指示を分ける。1024px幅の原画を360pxへ表示する場合、字の高さ60pxは約21pxになるが、狭いコマへ配置すればさらに小さくなる。実際のコマの表示幅から必要な原画の字の大きさを決め、生成結果を目視する。文字を小さくして無理に詰めず、列数・吹き出しの形・構図を調整する。

文字を個別編集する指定などで後から組版する場合だけ、後組版する文字の種類と予約領域を指定する。セリフだけを後組版し、効果音は絵と一緒に作る場合は `No dialogue or speech balloons; render only the specified sound effects.` とする。全ての文字を後組版する場合、または完全な静けさを意図する場合にだけ `No text, balloons or sound effects.` を使う。

「無言」を自動で文字なしへ変換しない。発話なしと発生音・継続音の有無を分けて指定する。たとえば歩くコマは `Dialogue: none. Sound effects: two separate コツ inscriptions near the boots, small hard lettering, no comma between them.`、継続音もなく聞き手が言葉を受け止めるコマは `Dialogue: none. Sound effects: none; preserve a quiet reaction.` と分ける。セリフと音が共存するコマも別々に指定する。効果音を `speaker: 音` の発話へ入れず、音のない感情コマへ動作音を一律に足さない。過去の実使用指示は履歴として保ち、修正した次回用指示や実行した編集指示と区別する。

## 構成の指示を変える

複数コマへ続く音は[コマと余白を跨ぐ音](cross-panel-sounds.md)の発生・継続の記録と生成例を使う。後続コマでは同じ音の継続を明示し、新しい音の追加や全文の複製と区別する。発話のないコマ、音が継続するコマ、完全な無音のコマを別々に指定する。

間の前後を別素材にするときは、次のように作画と組版の役割を分けて指定する。空白の中へ計画にない飾りや追加コマを生成しない。長さはリーダーの実際の表示で調整する。

```text
Scroll beat for THIS asset: [cue / reaction / reveal / aftermath].
Show only: [the information the reader sees at this moment].
End this asset before: [the reply, full armor, identity or source revealed later].
Pacing plan: after this asset, the reader crosses [a brief breath / a long quiet gap / a sparse continuous background] before [the next information]. The gap is arranged in the reader; do not compress both moments into a multi-panel page.
Edge treatment: [blend into the chosen page color / continue the background motif / retain a deliberate border].
Do not include later beats, bonus inset panels, a decorative grid, or a complete print-manga page.
```

余白そのものをこの原画へ描く場合だけ、その領域と地色・背景の疎さを指定する。待ちの目的と次に見る情報を渡し、全画像に同じ大余白を追加する指示にしない。

**効果音だけ・セリフだけ・視覚演出だけの余白**も生成単位にできる。通常の人物会話カットの共通指示をそのまま使わず、その区間に置く要素だけを指定する。文字を置く場合は全文と縦書きの列順、声なら話者と吹き出し・尾の有無を指定し、視覚演出だけの場合は文字を生成しない。

```text
Asset type: a sparse, borderless scroll-pacing beat on [chosen page color].
Only visible content: [the exact Japanese sound / the exact spoken or thought line / the planned light, shadow, ripple or trail].
Placement: [vertical position, direction, spacing of repeats and fading]. Retain broad unoccupied space around it, with lettering legible at phone width.
For a voice beat: [speaker or deliberately unidentified voice, spoken/thought, balloon or floating vertical lettering].
Do not add characters, extra dialogue, scenery, panel grids or unplanned ornaments. Keep [the later reveal] absent.
```

複数のコマを一枚へ生成するときは「大小をつける」だけで済ませず、各コマの役割と相対的な幅・高さ・配置・枠の有無を指示する。たとえば「全幅の状況確認→右寄せの会話→左寄せの浅い目元→大きな名乗り」。小コマはその面積に合う対象へ描き直し、全景を縮めたり絵を押し潰したりしない。生成後は文字だけでなく、本当に形と面積に差が出たか見る。[大小を直した実例](context-and-dialogue.md)の数値や配列は今回だけの選択。

横並びでは同じ段に入るコマ、右から左への順、次の段への移動を明記する。斜めではどの外枠やコマ間を傾けるかを指定し、絵や文字を丸ごと回転させない。[横並びと斜め枠の制作例](panel-layout.md)を参照する。生成結果の形と読順を目視し、指示した数値がそのまま出たとは扱わない。

**短い動作を密に読む場面**

```text
Three quick sequential shots of one person's action. Unequal sizes and widths, staggered downward with small gaps. First shot shows face and action; the following shots are small close-ups. They are successive moments, not simultaneous duplicate characters. Do not use three identical rectangles.
```

**下へ視点を運ぶ場面**

```text
One tall continuous borderless composition, not a grid or stack of panels. At the top, [initial viewpoint]. Through the middle, [motif leading the eye downward] and quieter detail. At the bottom, [new viewpoint or destination]. The reveal [X] must not be visible in this image. Integrate [the exact dialogue and balloons, or explicitly no dialogue] near [region] while keeping the vertical visual path clear.
```

**下で見せる答え**

```text
A large readable close-up, with [exact dialogue] inside a vertically lettered speech balloon near the speaker, without hiding the face or the reveal. This is the first scene where [hidden feature] appears. Preserve character identity. [Prop] is now [new state], not [previous state].
```

これらの場面数、割合、縦横比は例であり固定しない。役割に合う密度と長さに調整する。

## 状態表で防ぐ問題

| 対象 | 初め | 渡す瞬間 | 後 |
| --- | --- | --- | --- |
| 鍵のような小道具 | Aが一本持つ | AからBの手へ | Bだけが持つ。A側に重複しない |
| 正体を示す帽子など | 描かない | まだ描かない | 正体を見せる場面だけ描く |
| キャラクターの模様・服装 | 参照を固定 | 同じ | 同じ。変更するなら話の中で説明 |

完成した画像を見て確認する。指示文に書けていることは、画像が正しくできた証拠にはならない。

## 文字を余白へ移す編集

元のセリフや効果音を独立した余白へ移す場合は、再掲するだけで終えない。原画で除去する文字、吹き出し・尾・思考点・強調線の範囲と、その部分へ戻す背景を指定し、その他の文字、人物、手足、衣服、枠と寸法を保つ。安全な表示窓で文字を外せる場合は原画を変えず、文字や顔を切る場合だけ編集・再作画を選ぶ。[第1話の全編改稿例](scroll-revision-lessons.md)のように、移動元と余白の文字が一度だけ読め、音の発生源と通知の種類が前後でつながるか確認する。
