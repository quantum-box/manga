# 第1話 v4 全16場面の実際の生成指示

## 表示確認後の修正指示

以下は全16場面の初稿生成後に実行した画像編集。修正前の原画を `source/` に保存した。

### 01-memory

```text
Edit this image ONLY to enlarge the Japanese narration. Keep exact rain, hand, scarf, crosswalk, dark art and single panel unchanged.
Current text is too small at phone size. Enlarge ACTUAL visible glyphs by 1.5 times, to about 70px per glyph on this image width. Use bold crisp upright Japanese manga gothic. Expand the top-right white rectangular box toward the left and downward in the existing sky as needed, never cover the hand.
Exact text: 最後に覚えているのは、届かなかった手。
TRUE vertical text, top to bottom, columns from right to left. Columns RIGHT to LEFT:
最後に / 覚えている / のは、 / 届かなかった / 手。
No extra words, no labels, no horizontal text, no new characters or scene elements. Keep narrative text punctuation exact. The box can be wider than before. Lettering must read clearly at 360px display.
```

### 03-guide

```text
Edit ONLY the dialogue lettering and the size/placement of the EXISTING speech balloons in reference 1. Reference 2 is the approved large-letter vertical manga example, use its readable letter scale, not its words, pose, or characters.
Keep the same characters, exact costumes, faces, emotion, bare hand, dark crystal, and single-panel setting in reference 1. Preserve ALL exact wording and punctuation. Current long-dialogue glyphs become too small at 360px. Increase every glyph's ACTUAL HEIGHT at least 1.45 times to about 66px on a 1024px-wide image. Use clean bold upright Japanese manga gothic. Reduce excess gaps between columns, enlarge white balloons into available sky/architecture and lower-body areas; keep faces, pointing/touching hands and black crystal visible. You may recompose open space slightly or use a taller portrait to fit, but no new moment or panel. Do not merely scale up the canvas with the same tiny lettering. Do not shrink font to fit.
All writing is vertical: TOP TO BOTTOM; columns RIGHT TO LEFT. Exactly 3 balloons. Balloon/box order, exact words and right-to-left columns:
1. Rook, speech, upper right, first. Exact complete text: ここは、空に浮かぶ国だ。お前は転生者だな。. Columns RIGHT to LEFT: ここは、 / 空に浮かぶ / 国だ。 / お前は / 転生者だな。.
2. Ren, speech, upper left, second. Exact complete text: ……転生？　俺が？. Columns RIGHT to LEFT: ……転生？ / 俺が？.
3. Rook, speech, lower right, third; never cover pointing hand or crystal. Exact complete text: 異世界から来た者は、まず魔力を測る。水晶に手を置け。. Columns RIGHT to LEFT: 異世界から / 来た者は、 / まず魔力を / 測る。 / 水晶に / 手を置け。.
Keep speech tails toward the proper speaker; thought dots toward Ren. No extra words, labels, watermark, horizontal text, English, armor or magic. This edit is specifically to make Japanese letters readable around 20px at smartphone size.
```

### 04-verdict

```text
Edit ONLY the dialogue lettering and the size/placement of the EXISTING speech balloons in reference 1. Reference 2 is the approved large-letter vertical manga example, use its readable letter scale, not its words, pose, or characters.
Keep the same characters, exact costumes, faces, emotion, bare hand, dark crystal, and single-panel setting in reference 1. Preserve ALL exact wording and punctuation. Current long-dialogue glyphs become too small at 360px. Increase every glyph's ACTUAL HEIGHT at least 1.45 times to about 66px on a 1024px-wide image. Use clean bold upright Japanese manga gothic. Reduce excess gaps between columns, enlarge white balloons into available sky/architecture and lower-body areas; keep faces, pointing/touching hands and black crystal visible. You may recompose open space slightly or use a taller portrait to fit, but no new moment or panel. Do not merely scale up the canvas with the same tiny lettering. Do not shrink font to fit.
All writing is vertical: TOP TO BOTTOM; columns RIGHT TO LEFT. Exactly 3 balloons. Balloon/box order, exact words and right-to-left columns:
1. Rook, speech, upper right, first. Exact complete text: 魔力、ゼロ。. Columns RIGHT to LEFT: 魔力、 / ゼロ。.
2. Rook, speech, right middle, second. Exact complete text: この国では、魔力がない者は戦えない。ハズレの転生者か。. Columns RIGHT to LEFT: この国では、 / 魔力がない / 者は / 戦えない。 / ハズレの / 転生者か。.
3. Ren thought, thought, lower left, third. Exact complete text: ……ここでも、何もできないのか。. Columns RIGHT to LEFT: ……ここでも、 / 何もできない / のか。.
Keep speech tails toward the proper speaker; thought dots toward Ren. No extra words, labels, watermark, horizontal text, English, armor or magic. This edit is specifically to make Japanese letters readable around 20px at smartphone size.
```

### 12-approach

```text
Precise edit of this finished manga image. Keep the full art, poses, character identity, exact black unarmored shirt and red scarf, BARE hands, Mira behind Ren, giant stone guardian and glowing violet core, all speech lettering and two sound effects unchanged.
Fix ONLY ownership of the top thought balloon. The cloud says Ren's thought, not the giant's thought. Its small dotted tail currently visually belongs to the giant. Keep the cloud and its exact large vertical text 「まだ、来るのか。」 but redirect or relocate its dotted tail clearly toward REN'S BLACK-HAIRED HEAD in the middle-left of the picture. The three or more small white thought dots should travel diagonally down-LEFT toward Ren, with the last small dot visibly next to Ren's forehead/hair, never next to the giant. If needed move the cloud into the upper LEFT open sky above Ren and adjust the nearby sound-effect position. Do not cover Ren's or Mira's face, the giant's face or the violet chest core.
Exact thought text, no quotation marks: まだ、来るのか。
Vertical columns RIGHT to LEFT: まだ、 / 来るのか。
Keep the lower speech balloon intact: ミラ、下がって。今度は俺が止める。
Keep sound effects ズン。 and ズン。 once each. No new balloon, word, panel, armor or character. Japanese text remains upright vertical, each column top to bottom and columns right to left.
```

## 全場面の初稿生成指示

方式：組み込み `image_gen`。v3の各原画を場面の参照、承認された縦書き版を絵柄・文字の参照として使用。全16場面を独立したコマとして再生成。

## 01-memory

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1280 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Rainy night crosswalk memory: close bare reaching hand and red scarf, bright distant headlights. Show no body, injured person or face. One dreamlike close shot, dark blue night margins.

EXACT LETTERING, in the following reading order:
Balloon/box 1: narration; speaker: Ren narration; position: upper right in a narrow rectangular white narration box.
Exact complete text: 最後に覚えているのは、届かなかった手。
Columns RIGHT to LEFT: column 1: 最後に | column 2: 覚えている | column 3: のは、 | column 4: 届かなかった | column 5: 手。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 1 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 02-arrival

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1792 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Ren wakes seated on a stone stair in a white fantasy plaza and looks up at floating white towers, blue sky and hanging blue banners. Unarmored black short sleeves, charcoal trousers, crimson scarf, bare hands. Establish his confusion and the new world. Preserve the clear establishing view, large enough face.

EXACT LETTERING, in the following reading order:
Balloon/box 1: thought; speaker: Ren thought; position: upper right.
Exact complete text: ……ここ、どこだ。
Columns RIGHT to LEFT: column 1: ……ここ、 | column 2: どこだ。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: narration; speaker: location; position: small upper left rectangular location label.
Exact complete text: 空都リュミエル
Columns RIGHT to LEFT: column 1: 空都 | column 2: リュミエル.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 3: thought; speaker: Ren thought; position: lower left near Ren.
Exact complete text: 俺、事故に遭ったはずじゃ……。
Columns RIGHT to LEFT: column 1: 俺、事故に | column 2: 遭ったはず | column 3: じゃ……。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 3 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 03-guide

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1792 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Same Ren left and silver-haired knight Rook right at magic assessment station. Rook wears silver armor and blue cape, explains sternly and points to an UNLIT black crystal. One conversational moment, all three balloons integrated. Faces in middle and crystal/pointing hands clearly visible below. No armor or magic on Ren.

EXACT LETTERING, in the following reading order:
Balloon/box 1: speech; speaker: Rook; position: upper right, first.
Exact complete text: ここは、空に浮かぶ国だ。お前は転生者だな。
Columns RIGHT to LEFT: column 1: ここは、 | column 2: 空に浮かぶ | column 3: 国だ。 | column 4: お前は | column 5: 転生者だな。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: speech; speaker: Ren; position: upper left, second.
Exact complete text: ……転生？　俺が？
Columns RIGHT to LEFT: column 1: ……転生？ | column 2: 俺が？.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 3: speech; speaker: Rook; position: lower right, third; never cover pointing hand or crystal.
Exact complete text: 異世界から来た者は、まず魔力を測る。水晶に手を置け。
Columns RIGHT to LEFT: column 1: 異世界から | column 2: 来た者は、 | column 3: まず魔力を | column 4: 測る。 | column 5: 水晶に | column 6: 手を置け。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 3 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 04-verdict

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1792 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Ren puts his BARE palm on a pitch-black unlit crystal, discouraged. Rook present to his right delivers the result and dismisses him. No chest glow or armor. Crystal remains completely dark. A close tense scene; balloons distributed above and beside faces, the hand/crystal still clear.

EXACT LETTERING, in the following reading order:
Balloon/box 1: speech; speaker: Rook; position: upper right, first.
Exact complete text: 魔力、ゼロ。
Columns RIGHT to LEFT: column 1: 魔力、 | column 2: ゼロ。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: speech; speaker: Rook; position: right middle, second.
Exact complete text: この国では、魔力がない者は戦えない。ハズレの転生者か。
Columns RIGHT to LEFT: column 1: この国では、 | column 2: 魔力がない | column 3: 者は | column 4: 戦えない。 | column 5: ハズレの | column 6: 転生者か。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 3: thought; speaker: Ren thought; position: lower left, third.
Exact complete text: ……ここでも、何もできないのか。
Columns RIGHT to LEFT: column 1: ……ここでも、 | column 2: 何もできない | column 3: のか。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 3 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 06-giant

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1536 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: The SAME giant black stone guardian, armored stone limbs, violet fissures and a violet diamond-shaped chest core, goes berserk and breaks a high stone bridge. Princess Mira small but identifiable ON bridge, before falling. Establish high bridge above a lower balcony (Ren's assessment level) above a broad cargo canvas awning and soft cargo on a lower plaza. Two warning voices from small background guards or offscreen; no extra main characters. Giant fills upper background.

EXACT LETTERING, in the following reading order:
Balloon/box 1: shout; speaker: warning guard A; position: upper right with tail toward offscreen guard, first.
Exact complete text: 警備巨兵が暴走した！
Columns RIGHT to LEFT: column 1: 警備巨兵が | column 2: 暴走した！.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: shout; speaker: warning guard B; position: lower left with tail toward offscreen guard, second.
Exact complete text: 姫様が、橋にいる！
Columns RIGHT to LEFT: column 1: 姫様が、 | column 2: 橋にいる！.
Do not render the words column, speaker, or other instruction labels.
Draw these sound effects once each as upright vertical Japanese outside balloons, without obscuring art: ズ……ン。.
Exactly 2 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 07-fall

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x2048 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Mira ONLY falling from the just-broken bridge, through open blue sky, past the lower stone balcony toward a large cargo canvas awning. ONE continuous vertical view with descending rubble trail; no other copies of Mira, no Ren, no armored hero. Her dress and blue/gold details remain intact and modest. Borderless, pale sky and WHITE natural light fade at bottom, edges harmonize with pale page. Her fearful face visible near upper third.

EXACT LETTERING, in the following reading order:
Balloon/box 1: shout; speaker: Mira; position: upper right near Mira; dash is a vertical Japanese dash.
Exact complete text: 誰か——！
Columns RIGHT to LEFT: column 1: 誰か | column 2: ——！.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 1 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 08-leap

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1536 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Unarmored Ren leaps decisively from the LOWER balcony toward Mira and the cargo awning below. Show push-off stone balcony behind, descending direction, streaming red scarf and reaching bare hand. He is not magically flying and has no armor or blue core. One shot of the choice to jump; his face stays clearly visible.

EXACT LETTERING, in the following reading order:
Balloon/box 1: thought; speaker: Ren thought; position: upper right in the open sky.
Exact complete text: 魔力がなくても、手くらい、伸ばせる。
Columns RIGHT to LEFT: column 1: 魔力が | column 2: なくても、 | column 3: 手くらい、 | column 4: 伸ばせる。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 1 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 09-catch

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1280 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Close shot in midair: unarmored Ren catches Mira in both BARE arms, supporting her back and knees. Bodies and limbs correct, red scarf streaming, white towers and cargo awning below indicate downward motion. His shout is directed to Mira. Keep both faces visible, no glow or armor, no second pair of people.

EXACT LETTERING, in the following reading order:
Balloon/box 1: shout; speaker: Ren; position: upper right near Ren's head, clear tail to Ren.
Exact complete text: つかまって！
Columns RIGHT to LEFT: column 1: つかまって！.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 1 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 10-landing

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1280 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Immediately after catching: Ren still cradles Mira as they sink into and tear a large tan cargo canvas, cushioned by soft bundled cargo. Broken canvas supports and harmless debris, both alive. Ren bare hands, black shirt, red scarf, minor bruises. One concrete landing moment, NOT standing yet. No giant in foreground and no armor.

EXACT LETTERING, in the following reading order:
Balloon/box 1: thought; speaker: Ren thought; position: upper right near Ren.
Exact complete text: ……生きてる。
Columns RIGHT to LEFT: column 1: ……生きてる。.
Do not render the words column, speaker, or other instruction labels.
Draw these sound effects once each as upright vertical Japanese outside balloons, without obscuring art: ドサッ。.
Exactly 1 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 11-safe

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1536 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Re-render the approved vertical-lettered rescue conversation as a new finished panel with the same scene and same two balloons. Mira standing safely right, blonde braid white/blue/gold dress, hand on Ren's shoulder; Ren kneeling/sitting left, bruised bare hands, black short sleeves, charcoal trousers, crimson scarf, still unarmored. Torn cargo awning and white city behind. Same warm anime art and grateful expressions; exact accepted lettering.

EXACT LETTERING, in the following reading order:
Balloon/box 1: speech; speaker: Mira; position: upper right, first.
Exact complete text: ありがとう。私はミラ。この国の王女よ。
Columns RIGHT to LEFT: column 1: ありがとう。 | column 2: 私はミラ。 | column 3: この国の | column 4: 王女よ。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: speech; speaker: Ren; position: left slightly lower, second.
Exact complete text: レンだ。無事なら、それで。
Columns RIGHT to LEFT: column 1: レンだ。 | column 2: 無事なら、 | column 3: それで。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 2 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 12-approach

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1792 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: SAME black stone guardian with violet diamond chest core and violet cracks now approaches on the lower SOLID plaza. Ren still unarmored black short sleeves and red scarf, BARE hands out to shield standing Mira behind him. Torn canvas and cargo remain behind them. Giant, both people and ground show clear depth. Ren looks alarmed then resolute, no armor/glow.

EXACT LETTERING, in the following reading order:
Balloon/box 1: thought; speaker: Ren thought; position: upper right, first.
Exact complete text: まだ、来るのか。
Columns RIGHT to LEFT: column 1: まだ、 | column 2: 来るのか。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: speech; speaker: Ren; position: lower right beside Ren with clear tail, second.
Exact complete text: ミラ、下がって。今度は俺が止める。
Columns RIGHT to LEFT: column 1: ミラ、 | column 2: 下がって。 | column 3: 今度は俺が | column 4: 止める。.
Do not render the words column, speaker, or other instruction labels.
Draw these sound effects once each as upright vertical Japanese outside balloons, without obscuring art: ズン。 / ズン。.
Exactly 2 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 13-core

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1792 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: A close shot of Ren's BARE hand and his still SOFT BLACK SHIRT at the chest as a cyan star-like core first glows through the fabric. Not full armor; no transformed silhouette anywhere. Dark blue mood, cyan illumination. One small white vertical thought balloon and two vertical rectangular cyan system notices integrated in sequence. Preserve hand anatomy and shirt. System notices are opaque dark cyan rectangles with readable pale cyan upright Japanese lettering, not a speech tail.

EXACT LETTERING, in the following reading order:
Balloon/box 1: thought; speaker: Ren thought; position: upper right, first.
Exact complete text: これは……？
Columns RIGHT to LEFT: column 1: これは……？.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: system; speaker: system; position: middle-left below chest close-up, second.
Exact complete text: 救命行動を確認。救済核、起動。
Columns RIGHT to LEFT: column 1: 救命行動を | column 2: 確認。 | column 3: 救済核、 | column 4: 起動。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 3: system; speaker: system; position: bottom right, third.
Exact complete text: 装甲名：ゼロ・ブレイク
Columns RIGHT to LEFT: column 1: 装甲名： | column 2: ゼロ・ | column 3: ブレイク.
Do not render the words column, speaker, or other instruction labels.
Draw these sound effects once each as upright vertical Japanese outside balloons, without obscuring art: ドクン。.
Exactly 3 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 14-hero

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x2048 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: FIRST full armor reveal. Low camera, full-length Ren in exact sleek black angular plate suit, star-shaped cyan chest core and cyan seams, red scarf, armored gloves and boots. Same black hair/blue eyes. Mira safely STANDING on solid ground behind right, not held or falling. White floating city. Dynamic but stable hero stance, not punching yet. Naturally white/cyan light at image edges and bottom blending into pale page; borderless single continuous picture. Balloon integrated near Ren's head, not a detached caption.

EXACT LETTERING, in the following reading order:
Balloon/box 1: speech; speaker: Ren; position: upper right, tail to Ren.
Exact complete text: なら、今度こそ。
Columns RIGHT to LEFT: column 1: なら、 | column 2: 今度こそ。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 1 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 15-punch

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1280 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: The armored Ren punches the SAME giant's VIOLET DIAMOND CHEST CORE with a black armored fist, red scarf whips back, cyan power lights impact, purple stone fragments fly. Clear single point of impact at enemy chest, giant otherwise black stone/violet cracks. He protects Mira behind him; she is not in the strike path. One close explosive action shot, not a collage, no new weapon.

EXACT LETTERING, in the following reading order:
Balloon/box 1: shout; speaker: Ren; position: upper right or clear sky near Ren, tail to Ren.
Exact complete text: ゼロ・ブレイク！
Columns RIGHT to LEFT: column 1: ゼロ・ | column 2: ブレイク！.
Do not render the words column, speaker, or other instruction labels.
Draw these sound effects once each as upright vertical Japanese outside balloons, without obscuring art: ドンッ！.
Exactly 1 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 16-relief

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1536 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: On the same safe solid plaza AFTER the giant stopped, Ren in black armor and red scarf and Mira in white/blue/gold dress smile in relief. Both stand safely, gentle eye contact. Broken stone in background, not an attacking giant. Ren armor includes cyan star core and armored gloves. Two vertical speech balloons arranged as Mira first then Ren.

EXACT LETTERING, in the following reading order:
Balloon/box 1: speech; speaker: Mira; position: upper right, first.
Exact complete text: あなた、本当に魔力ゼロなの？
Columns RIGHT to LEFT: column 1: あなた、 | column 2: 本当に | column 3: 魔力ゼロ | column 4: なの？.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: speech; speaker: Ren; position: left slightly lower, second.
Exact complete text: みたいだ。けど、役立たずじゃなかった。
Columns RIGHT to LEFT: column 1: みたいだ。 | column 2: けど、 | column 3: 役立たず | column 4: じゃなかった。.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 2 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```

## 17-fragment

```text
Use case: illustration-story, identity-preserve re-render.
Asset type: final Japanese anime WEBTOON picture INCLUDING all speech balloons, thought balloons, narration, effects and exact Japanese VERTICAL lettering as part of the generated raster.
Reference 1 is the source scene: preserve event, character identity and scene continuity, but redesign its layout to integrate the exact lettering. Reference 2 (if supplied) is ONLY the user-approved anime art and vertical lettering reference: do not copy its rescue pose, words, balloon count, or unarmored state into other scenes.
One single illustrated moment per output, NOT a storyboard sheet, montage, grid, duplicate character sequence, or multiple pages. High-quality Japanese anime faces with crisp linework and detailed but readable colored backgrounds. Adult characters. Ren: 19, black spiky hair, blue eyes, crimson scarf. Mira: blonde braid, blue eyes, white/blue/gold dress. Rook: silver hair, silver armor, blue cape.
TRUE Japanese vertical writing: every glyph upright, each column TOP TO BOTTOM and column order RIGHT TO LEFT. Do not rotate horizontal sentences sideways. Each specified list of columns is ordered from RIGHTMOST to LEFTMOST. Use clean bold Japanese manga gothic, solid black in white balloons, no pseudo-glyphs, no English, no labels or quoted delimiters. Exact wording and punctuation only. Allocate ACTUAL visible glyph height about 66–72px at 1024px image width, comfortable at 360px display even with modest page margins. Fit by reshaping balloons and arranging open sky/architecture, never by shrinking lettering. Normal speech has a smooth oval with a tail toward the speaker; thought has cloud outline and tiny dots; shout can have an energetic irregular outline. Narration/system use rectangles without speaker tails. Do not cover faces, bare hands, the crystal, core, or clue. Avoid overlapping bubbles or words. Read balloons top-to-bottom by specified positions, with rightmost first when at a shared height.
Keep exact costumes and props at this story phase. Do not leak a later transformation, royal crest, enemy defeat or rescue result. No watermarks. Unless the scene requests borderless bleed, draw a clean thin dark comic border. All requested typography must be generated WITH the picture; nothing will be added later to correct tiny text.

Preferred output aspect: 1024x1536 portrait. Compose for this shape; use margins for lettering as needed.
Scene and invariants: Macro shot of Ren's BLACK ARMORED GLOVE holding a purple-black broken guardian core fragment with an UNMISTAKABLE SMALL CROWN CREST engraved on it. This is FIRST crown-crest reveal. White city ground out of focus. Mira speaks from offscreen right and Ren replies from offscreen left; balloon tails point toward their offscreen positions, never pretend the stone speaks. Keep the entire glove/thumb, fragment and crown visible. Single clue close-up.

EXACT LETTERING, in the following reading order:
Balloon/box 1: speech; speaker: Mira offscreen; position: upper right, first; tail to offscreen right.
Exact complete text: その紋章……王家の工房のものよ。
Columns RIGHT to LEFT: column 1: その紋章…… | column 2: 王家の工房の | column 3: ものよ。.
Do not render the words column, speaker, or other instruction labels.

Balloon/box 2: speech; speaker: Ren offscreen; position: lower left, second; tail to offscreen left.
Exact complete text: じゃあ、なんで俺たちを襲った？
Columns RIGHT to LEFT: column 1: じゃあ、 | column 2: なんで | column 3: 俺たちを | column 4: 襲った？.
Do not render the words column, speaker, or other instruction labels.
No extra sound effects or lettering.
Exactly 2 balloons/boxes only. Preserve all exact dialogue, readable at mobile width.
```
