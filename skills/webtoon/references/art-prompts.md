# 場面ごとの作画指示

画像生成には同じキャラクター仕様と参照画像を渡し、場面固有の構成・状態・伏せる情報を追加する。単に「縦長のWebtoon」と頼むと、横長のコマや等間隔のコマ列に戻りやすい。

日本語の会話は吹き出しとセリフを絵に含めて生成する。縦書きの列指定は[承認された実例](vertical-lettering.md)を参照する。吹き出しの数や位置は各場面の発話と構図から決める。

## 絵柄と感情を別々に指定する

「もっとアニメ風」という要望では、線の明快さ、セル塗りの影、配色、顔の造形、表情の読みやすさを具体化する。武侠という題材だけから写実的な絵柄や豪華な金装飾へ寄せない。今回の題材・爽快感・表情は[感情と行動の実例](emotion-and-causality.md)、生成する表示や効果音は[システム表示の実例](system-and-lettering.md)を参照する。

人物の顔立ち・髪・服・汚れ・持ち物は同一性の条件、眉・口・視線・手の緊張はその場面の感情として指定する。人物参照の不敵な表情まで不変条件にしない。「驚いている」だけでなく、何を見て何が分からず、どの部位に反応が出るかを指示する。

既存作画の感情を直す場合は、編集対象を先に表示し、変更する眉・瞳・口・姿勢などと、保つ人物・衣服・小道具・背景・構図を分ける。足りない因果は、前後の状態をつなぐ接写や短い動作を追加する。表情を直す指示で武器や拘束の状態まで変えない。

## 共通部分の例

```text
Use case: illustration-story.
Asset type: finished art for a smartphone vertical-scroll comic, including final dialogue and speech balloons.
Primary request: [this story and this scene].
Input images: Reference 1 establishes character identity; Reference 2 establishes palette/style. Do not copy their panel layout.
Subject: [identity, clothing, markings and recurring props].
Style/medium: [chosen art direction].
Scene/backdrop: [consistent setting and time].
Text: Render the exact Japanese dialogue below inside white speech balloons integrated with the illustration. Use true vertical Japanese typesetting: upright glyphs, top-to-bottom columns, columns ordered right-to-left. Do not rotate horizontal sentences sideways. No extra text or watermark.
Dialogue: [speaker, exact full text, balloon reading order, and each vertical column listed in right-to-left order].
Lettering: Clean printed Japanese manga gothic, dark lettering, generous inset padding, legible after smartphone downscaling. Balloon tails point to the speakers. Do not cover faces or hands.
Constraints: [unchanging identity] and [this scene's prop state].
Avoid: [information not yet revealed], extra props, duplicate characters, watermark.
```

背景の端を同色へ柔らかくつなぐ指示は、連続する場面で必要な場合だけ追加する。全作品を夜や暗色に限定しない。

文字は短い語だけでなく全文を渡す。列分けの一覧を吹き出しへラベルとして描かせないよう、全文と配置の指示を分ける。1024px幅の原画を360pxへ表示する場合、字の高さ60pxは約21pxになるが、狭いコマへ配置すればさらに小さくなる。実際のコマの表示幅から必要な原画の字の大きさを決め、生成結果を目視する。文字を小さくして無理に詰めず、列数・吹き出しの形・構図を調整する。

文字を個別編集する指定などで後から組版する場合だけ、上の `Text` を「No text or speech balloons; reserve [region] for separately typeset dialogue.」へ置き換える。無言の場面は明示して文字なしで生成する。

## 構成の指示を変える

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
