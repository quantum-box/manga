# 場面ごとの作画指示

画像生成には同じキャラクター仕様と参照画像を渡し、場面固有の構成・状態・伏せる情報を追加する。単に「縦長のWebtoon」と頼むと、横長のコマや等間隔のコマ列に戻りやすい。

## 共通部分の例

```text
Use case: illustration-story.
Asset type: finished art for a smartphone vertical-scroll comic.
Primary request: [this story and this scene].
Input images: Reference 1 establishes character identity; Reference 2 establishes palette/style. Do not copy their panel layout.
Subject: [identity, clothing, markings and recurring props].
Style/medium: [chosen art direction].
Scene/backdrop: [consistent setting and time].
Text: No text, lettering, speech bubbles or caption boxes. Japanese lettering is typeset separately.
Constraints: [unchanging identity] and [this scene's prop state].
Avoid: [information not yet revealed], extra props, duplicate characters, watermark.
```

背景の端を同色へ柔らかくつなぐ指示は、連続する場面で必要な場合だけ追加する。全作品を夜や暗色に限定しない。

## 構成の指示を変える

**短い動作を密に読む場面**

```text
Three quick sequential shots of one person's action. Unequal sizes and widths, staggered downward with small gaps. First shot shows face and action; the following shots are small close-ups. They are successive moments, not simultaneous duplicate characters. Do not use three identical rectangles.
```

**下へ視点を運ぶ場面**

```text
One tall continuous borderless composition, not a grid or stack of panels. At the top, [initial viewpoint]. Through the middle, [motif leading the eye downward] and quieter detail. At the bottom, [new viewpoint or destination]. The reveal [X] must not be visible in this image. Leave usable space near [region] for lettering.
```

**下で見せる答え**

```text
A large readable close-up, with enough space above the subject for separately typeset dialogue. This is the first scene where [hidden feature] appears. Preserve character identity. [Prop] is now [new state], not [previous state].
```

これらの場面数、割合、縦横比は例であり固定しない。役割に合う密度と長さに調整する。

## 状態表で防ぐ問題

| 対象 | 初め | 渡す瞬間 | 後 |
| --- | --- | --- | --- |
| 鍵のような小道具 | Aが一本持つ | AからBの手へ | Bだけが持つ。A側に重複しない |
| 正体を示す帽子など | 描かない | まだ描かない | 正体を見せる場面だけ描く |
| キャラクターの模様・服装 | 参照を固定 | 同じ | 同じ。変更するなら話の中で説明 |

完成した画像を見て確認する。指示文に書けていることは、画像が正しくできた証拠にはならない。
