# ネームプレビューの短い試作

`帰還` は機能を確かめるための短い場面で、既存の連載作品の採用原稿ではない。[HTML](index.html)を開いて縦に読む。[plan.json](plan.json)の読む順・列分け・位置・コマ幅・余白を直して再出力できる。

```bash
python3 skills/webtoon/scripts/build_name_preview.py \
  skills/webtoon/references/name-preview/plan.json \
  --output skills/webtoon/references/name-preview/index.html --force
```

## 場面の意図

夕暮れの手当て用の天幕へ、怪我をした兵士が戻る。治療係は心配を冷たい丁寧語で隠し、兵士は腕を押さえながら平気なふりをする。治療係が強がりを見抜く → 中へ誘う → 兵士が助けを受け入れる → 同じ天幕で手当てする、という接続を入れる。最後に二人が本音を返し合う。

足音は帰還時、布の音は手当て時に一度ずつ置く。それ以外の音を入れない理由と、人物の意図・反応・間は各要素の `purpose` に記録した。接写には原本の表示窓を使い、原本画像のバイトは加工していない。

## 確認の範囲

- Chromiumの390×844と360×800、倍率1で表示し、全長画像と150px重複する連続画面を保存した。[390px全長](review/full-390.png)・[360px全長](review/full-360.png)。
- 両幅で画像5つが読み込まれ、横方向のはみ出しとJavaScriptエラーはなかった。セリフは約21px・19px。[計測結果](review/browser-metrics.json)。
- 実際の連続画面を読み、顔・手・吹き出し・音・場面の接続を確認した。強がる返答と手の接写、手当てへの誘い、受け入れる返事が読む順にある。
- 原本は1536×1024の画像生成結果。プレビュー出力は390px・360px幅のPNGで、完成作画の解像度・生成料金を保証するものではない。
- 実機・Safari・ユーザーの構成採用・完成原稿の合格・公開は未確認。ネームを提示した後は返答を待つ。

この試作は一場面の部分プレビューで、通常の一話の分量ではない。幅390 CSS pxで本編高2,639.53125 CSS px、明示した余白293 CSS px、その余白だけを除いた高2,346.53125 CSS px、表示カット5つ。自動計測では画像内等の他の純余白や、有効コマへの計上を判定していない。[構成計測の表示](review/measurement-390.png)で数値を確認できる。

計測UIと構成メモを開閉しても本編高は変わらず、DPRを1から3へ変えてもCSS pxの計測値は同じだった。360pxへのリサイズで再計測され、800px幅の画面では基準390pxへ収まる。画像が壊れた場合は失敗数を表示することも確認した。

## ラフ絵の生成記録

組み込み `image_gen` で白黒の4場面を1枚の資料として生成した。文字・吹き出しは画像に含めずHTMLへ置く。`sketches.png` は生成された画像をそのままコピーしたもの。

原本 SHA-256: `cd71424e33efa80ba2e5b4d6a60e46efae637cb1a8ad7b82489ec49cbabaacf9`

実行したプロンプト:

```text
Use case: illustration-story
Asset type: rough storyboard source image for a webtoon name-preview feature
Primary request: Create one monochrome pencil storyboard contact sheet with exactly four independent drawings arranged in a clean 2x2 grid. This is rough, low-resolution-looking manga name art, not a finished illustration. No text, no speech balloons, no panel numbers, no extra cells.
Scene/backdrop: Same contemporary canvas treatment tent scene at dusk, kept visually consistent across all four views.
Subject: The same two young adults in every drawing. Healer on the RIGHT: short light bob hair, plain white work coat/apron. Quiet returning soldier on the LEFT: short dark hair, dark travel tunic, injured RIGHT forearm. Keep left/right positions, identities, and prop state consistent.
Style/medium: loose unpolished manga thumbnail / name drawing, graphite pencil linework, sparse gray hatching, simple blocking, large readable faces and hands, no rendered detail.
Composition/framing: Four equal cells in a 2x2 arrangement with generous white inner margin in every cell so each can be cropped separately. No border text or labels. Each drawing must be clearly separated by whitespace.
Top-left cell: wide establishing shot outside a canvas treatment tent at dusk. Soldier on LEFT has just returned, protects his injured right forearm. Healer on RIGHT sees him and stands tense.
Top-right cell: close-up of healer on RIGHT looking LEFT toward the soldier, outwardly controlled and cold but eyes worried, lips slightly tight, one tense hand near chest.
Bottom-left cell: close-up of soldier on LEFT looking RIGHT but averting his eye, pretending he is fine, injured right forearm held toward his chest, jaw strained.
Bottom-right cell: inside the same canvas tent. Healer on RIGHT carefully cleans the soldier's extended right forearm with a cloth; a basin sits on a plain table. Soldier on LEFT relaxes his shoulders as he accepts help. Healer's worry softens into tenderness.
Lighting/mood: dusk outside, quiet tension that softens into care inside; emotional acting must be visible in posture, eyes, mouth, and hands.
Color palette: black, graphite gray, white only; no color.
Constraints: exactly four drawings only; keep each drawing independent and crop-friendly; no written SFX or any text anywhere; no powers, weapons, or new characters; preserve healer RIGHT / soldier LEFT in all views; preserve injured RIGHT forearm.
Avoid: finished anime rendering, polished color art, extra figures, weapons, magic effects, decorative typography, captions, dialogue, sound effects, speech bubbles, panel numbering, border clutter, tiny unreadable faces, cropped hands, ambiguous character identities.
```

生成結果は指示より細かい鉛筆画になった。今後のネームではより粗い線・少ない背景を指定してよい。腕の左右を含む細部の連続性は本作画でも再確認する。
