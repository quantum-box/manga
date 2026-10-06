# 第1話 — 実際に画像生成へ渡す指示

方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。
参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。

## 01-arrival

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: One tall borderless vertical scene: Kou startled and unsteady on the paved lane at the top; his eyes follow immense pale sandstone ribs to the glowing ceiling; downward motion returns to his dirt-stained hands and green apron. Tower interior only, NOT open outdoor sky. He remembers farming but no Earth scene. Two separate moments, not duplicate simultaneous people.

EXACT TEXT IN READING ORDER:

Speaker コウ・心 (thought, cloud with dots). Exact full text: 畑にいたはずなのに。
Vertical columns from RIGHT to LEFT: 畑にいたはずな / のに。

Speaker コウ (spoken, tail to speaker). Exact full text: ここ、どこだ……。
Vertical columns from RIGHT to LEFT: ここ、どこだ… / …。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 02-gate

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: Three unequal panels: medium Kou facing a plain wooden administrative desk; closer offscreen clerk's hand indicating a closed stone gate diagram without lettering; closeup Kou absorbing the answer. Clerk is an ordinary older adult in beige robe, not Leon. Show patient exchange, hope and worry.

EXACT TEXT IN READING ORDER:

Speaker 係員 (spoken, tail to speaker). Exact full text: 帰還の門は、今は閉じてる。
Vertical columns from RIGHT to LEFT: 帰還の門は、今 / は閉じてる。

Speaker コウ (spoken, tail to speaker). Exact full text: 帰る方法は、あるんですね？
Vertical columns from RIGHT to LEFT: 帰る方法は、あ / るんですね？

Speaker 係員 (spoken, tail to speaker). Exact full text: 調査待ちだ。まずは寝床だ。
Vertical columns from RIGHT to LEFT: 調査待ちだ。ま / ずは寝床だ。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 03-diner

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: Wide panel: Kou pauses outside diner blue awning, hungry, Elna at serving window to his left. Small inset of his hand on stomach. Lower medium panel of Elna turning toward vegetable plot. Keep paved lane left and beds right of diner.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 飯代なら、働きます。
Vertical columns from RIGHT to LEFT: 飯代なら、働き / ます。

Speaker エルナ (spoken, tail to speaker). Exact full text: 畑を、見られる？
Vertical columns from RIGHT to LEFT: 畑を、見られる / ？

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 04-wet-soil

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: Three unequal panels in the same plot: wide Elna left and crouching Kou right beside wilted broad leafy vegetables; closeup her tense hand holding a small fertilizer sack closed; lower closeup Kou pressing moist soil, not pouring water. Water remains pooled, drain is still blocked.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 水も肥料も、増やしたのに。
Vertical columns from RIGHT to LEFT: 水も肥料も、増 / やしたのに。

Speaker コウ (spoken, tail to speaker). Exact full text: この土、ずっと湿ってる？
Vertical columns from RIGHT to LEFT: この土、ずっと / 湿ってる？

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 05-roots

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: Two medium panels with a narrow hand closeup between: Kou gently exposes one small plant's roots with a trowel; dark compact wet root zone and some damaged roots, no instant healthy glow; Elna silently watches and responds to his cautious expression. Exactly one dug plant, nearby plants remain rooted.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 葉より先に、根を見たい。
Vertical columns from RIGHT to LEFT: 葉より先に、根 / を見たい。

Speaker コウ (spoken, tail to speaker). Exact full text: 悪い場所も、残して比べよう。
Vertical columns from RIGHT to LEFT: 悪い場所も、残 / して比べよう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 06-permission

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: Three unequal conversation panels at removable wooden drain inspection cover near plot edge: Kou asks while pointing at cover; Elna with diner blue awning behind answers; their hands reach for the same cover after permission. Drain not flowing yet, leaves and silt block its opening.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: この出口、誰が管理してる？
Vertical columns from RIGHT to LEFT: この出口、誰が / 管理してる？

Speaker エルナ (spoken, tail to speaker). Exact full text: 店の区画は、私が掃除する決まり。
Vertical columns from RIGHT to LEFT: 店の区画は、私 / が掃除する決ま / り。

Speaker コウ (spoken, tail to speaker). Exact full text: 開けてもいい？
Vertical columns from RIGHT to LEFT: 開けてもいい？

Speaker エルナ (spoken, tail to speaker). Exact full text: うん。お願い。
Vertical columns from RIGHT to LEFT: うん。お願い。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 07-flow

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: One tall flowing composition plus two small unequal hand closeups at the top: Kou removes leaf litter and silt from accessible outlet, Elna holds lifted cover aside; clear visible flow then follows the channel downward and out safely to common drain. No digging through structural wall, no flooding other houses, wilted plants remain wilted. The visible action causes the flow.

EXACT TEXT IN READING ORDER:

Physical sound only, exact text: ごぼっ. Near the outlet where air and water move; no speech balloon.

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 08-first-meal

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, target about 60px glyph height in a 1024px-wide original so it remains readable at 360px width. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 召喚当日・昼から夕方. 三階へ召喚。帰還門は調査中。エルナの区画で修理許可を得る。枯れた株は回復しない。

SCENE: Three panels with final large warm scene: Elna sets a steaming barley-and-meat bowl on diner counter for Kou; closeup his rough hands near the bowl as he looks worried toward the still wilted garden; final Elna's gentle expression and Kou's relieved face in warm kitchen lamplight. Vegetables and grain are already purchased or existing, not newly grown. No miraculous lush plot.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 今日は、ここで食べて。
Vertical columns from RIGHT to LEFT: 今日は、ここで / 食べて。

Speaker コウ (spoken, tail to speaker). Exact full text: まだ、畑は治ってない。
Vertical columns from RIGHT to LEFT: まだ、畑は治っ / てない。

Speaker エルナ (spoken, tail to speaker). Exact full text: でも、水は動いたよ。
Vertical columns from RIGHT to LEFT: でも、水は動い / たよ。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 実際の追加生成：01-arrival-lettered

```text
Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the dialogue lettering and the necessary white speech/thought balloon areas. Enlarge EVERY Japanese dialogue glyph to approximately 1.7 TIMES its current height and width; final glyph height around 7 percent of full canvas width, including any small-panel dialogue. Enlarge balloons and reflow vertical columns to fit, with generous white inset. Do NOT make letters small to keep the original balloon size. Preserve ALL exact wording, punctuation, speakers and balloon reading order. Upright vertical Japanese: top-to-bottom, columns RIGHT TO LEFT. Do not display speaker labels or quotation marks. Thought stays a cloud with dots; speech tails stay attached to the correct speaker. Keep every panel boundary, character face/expression/pose/hand/clothing, tool, plant condition, bowl, food, architecture and color unchanged except the small areas needed for bigger balloons. Do not cover faces, hands or important evidence. Preserve any existing sound effects unchanged. No added people, words or repeated dialogue. Strong clean printed manga gothic, easy to read on a phone.
EXACT DIALOGUE IN ORDER: コウ・心「畑にいたはずなのに。」 / コウ「ここ、どこだ……。」

```

## 実際の追加生成：02-gate-lettered

```text
Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the dialogue lettering and the necessary white speech/thought balloon areas. Enlarge EVERY Japanese dialogue glyph to approximately 1.7 TIMES its current height and width; final glyph height around 7 percent of full canvas width, including any small-panel dialogue. Enlarge balloons and reflow vertical columns to fit, with generous white inset. Do NOT make letters small to keep the original balloon size. Preserve ALL exact wording, punctuation, speakers and balloon reading order. Upright vertical Japanese: top-to-bottom, columns RIGHT TO LEFT. Do not display speaker labels or quotation marks. Thought stays a cloud with dots; speech tails stay attached to the correct speaker. Keep every panel boundary, character face/expression/pose/hand/clothing, tool, plant condition, bowl, food, architecture and color unchanged except the small areas needed for bigger balloons. Do not cover faces, hands or important evidence. Preserve any existing sound effects unchanged. No added people, words or repeated dialogue. Strong clean printed manga gothic, easy to read on a phone.
EXACT DIALOGUE IN ORDER: 係員「帰還の門は、今は閉じてる。」 / コウ「帰る方法は、あるんですね？」 / 係員「調査待ちだ。まずは寝床だ。」

```

## 実際の追加生成：03-diner-lettered

```text
Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the dialogue lettering and the necessary white speech/thought balloon areas. Enlarge EVERY Japanese dialogue glyph to approximately 1.7 TIMES its current height and width; final glyph height around 7 percent of full canvas width, including any small-panel dialogue. Enlarge balloons and reflow vertical columns to fit, with generous white inset. Do NOT make letters small to keep the original balloon size. Preserve ALL exact wording, punctuation, speakers and balloon reading order. Upright vertical Japanese: top-to-bottom, columns RIGHT TO LEFT. Do not display speaker labels or quotation marks. Thought stays a cloud with dots; speech tails stay attached to the correct speaker. Keep every panel boundary, character face/expression/pose/hand/clothing, tool, plant condition, bowl, food, architecture and color unchanged except the small areas needed for bigger balloons. Do not cover faces, hands or important evidence. Preserve any existing sound effects unchanged. No added people, words or repeated dialogue. Strong clean printed manga gothic, easy to read on a phone.
EXACT DIALOGUE IN ORDER: コウ「飯代なら、働きます。」 / エルナ「畑を、見られる？」

```

## 実際の追加生成：04-wet-soil-lettered

```text
Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the dialogue lettering and the necessary white speech/thought balloon areas. Enlarge EVERY Japanese dialogue glyph to approximately 1.7 TIMES its current height and width; final glyph height around 7 percent of full canvas width, including any small-panel dialogue. Enlarge balloons and reflow vertical columns to fit, with generous white inset. Do NOT make letters small to keep the original balloon size. Preserve ALL exact wording, punctuation, speakers and balloon reading order. Upright vertical Japanese: top-to-bottom, columns RIGHT TO LEFT. Do not display speaker labels or quotation marks. Thought stays a cloud with dots; speech tails stay attached to the correct speaker. Keep every panel boundary, character face/expression/pose/hand/clothing, tool, plant condition, bowl, food, architecture and color unchanged except the small areas needed for bigger balloons. Do not cover faces, hands or important evidence. Preserve any existing sound effects unchanged. No added people, words or repeated dialogue. Strong clean printed manga gothic, easy to read on a phone.
EXACT DIALOGUE IN ORDER: エルナ「水も肥料も、増やしたのに。」 / コウ「この土、ずっと湿ってる？」

```

## 実際の追加生成：05-roots-lettered

```text
Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the dialogue lettering and the necessary white speech/thought balloon areas. Enlarge EVERY Japanese dialogue glyph to approximately 1.7 TIMES its current height and width; final glyph height around 7 percent of full canvas width, including any small-panel dialogue. Enlarge balloons and reflow vertical columns to fit, with generous white inset. Do NOT make letters small to keep the original balloon size. Preserve ALL exact wording, punctuation, speakers and balloon reading order. Upright vertical Japanese: top-to-bottom, columns RIGHT TO LEFT. Do not display speaker labels or quotation marks. Thought stays a cloud with dots; speech tails stay attached to the correct speaker. Keep every panel boundary, character face/expression/pose/hand/clothing, tool, plant condition, bowl, food, architecture and color unchanged except the small areas needed for bigger balloons. Do not cover faces, hands or important evidence. Preserve any existing sound effects unchanged. No added people, words or repeated dialogue. Strong clean printed manga gothic, easy to read on a phone.
EXACT DIALOGUE IN ORDER: コウ「葉より先に、根を見たい。」 / コウ「悪い場所も、残して比べよう。」

```

## 実際の追加生成：05-roots-repaired

```text
Use case: precise-object-edit. Edit this existing vertical anime Webtoon art ONLY to correct the crop and root-zone condition during a diagnosis of waterlogged soil. Keep every panel boundary, composition, camera, character face, expression, hand, pose, clothing, trowel, background, speech balloon, and ALL exact Japanese lettering unchanged. Keep both dialogue texts exactly: 葉より先に、根を見たい。 / 悪い場所も、残して比べよう。 In all three panels, the ONE selected plant being dug, inspected and held by Kou must be the SAME modest garden-leaf plant with slightly wilted drooping yellow-green leaves, NOT a healthy fully recovered bright green plant. Its exposed roots show some darker damaged fine roots and sparse pale roots, no glowing magic or instant new growth. The soil immediately around its excavated root zone looks dark and moist/compacted, consistent with waterlogging. Nearby plants may vary, with some drooping yellow leaves in this same affected strip; do not turn the whole garden into dead plants. Preserve anatomy and the plant handoff continuity. No extra text, no other edits.

```

## 実際の追加生成：06-permission-lettered

```text
Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the speech lettering and the necessary speech balloon shapes/white areas. Increase EVERY Japanese dialogue glyph to about 1.7 TIMES its current height and width. The resulting glyph height must be approximately 7 percent of the full image width, including the small lower-panel dialogue. Make balloons wider/taller as needed, reorganize vertical column breaks to fit; do NOT solve by making the lettering small again. Keep ALL exact text and speakers, upright vertical top-to-bottom Japanese, columns right-to-left. Exact text in order: コウ『この出口、誰が管理してる？』 / エルナ『店の区画は、私が掃除する決まり。』 / コウ『開けてもいい？』 / エルナ『うん。お願い。』. Natural columns for Elna's long line from right to left: 店の区画は、 / 私が掃除する / 決まり。 Keep all panel boundaries, characters, faces, expressions, hands, poses, clothing, background, wooden cover, drain and water completely unchanged except tiny background areas replaced by enlarged white balloons. Preserve correct balloon tails. Do not cover faces or hands. Strong crisp readable printed manga Gothic, generous inset. No added people, words or balloons.

```

## 実際の追加生成：07-flow-repaired

```text
Use case: precise-object-edit. Correct ONLY the central cast in this existing vertical anime comic scene. This takes place in episode one, before Balt, Iris or Leon have appeared. The ONLY two people allowed anywhere are Kou (black-haired farmer, brown jacket, green apron) and Elna (red-brown-haired cook, blue headscarf, cream apron). REMOVE the three standing background observers completely: older man in brown hat on left, navy-haired woman in goggles on right, silver-haired man in navy cloak on far right. Fill their former areas naturally with the same garden and diner background. Keep Kou and Elna, all their faces/expressions/poses/hands/clothing, panel layout, all drain parts, cover, water motion, wilted plants, light, colors and exact sound text ごぼっ unchanged. No added people or text. The scene shows Kou clearing a blocked outlet while Elna holds the wooden inspection cover, and water flowing safely down the channel; surrounding damaged plants remain wilted. Do not turn it into a new cast-group illustration.

```

## 実際の追加生成：08-first-meal-lettered

```text
Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the dialogue lettering and the necessary white speech/thought balloon areas. Enlarge EVERY Japanese dialogue glyph to approximately 1.7 TIMES its current height and width; final glyph height around 7 percent of full canvas width, including any small-panel dialogue. Enlarge balloons and reflow vertical columns to fit, with generous white inset. Do NOT make letters small to keep the original balloon size. Preserve ALL exact wording, punctuation, speakers and balloon reading order. Upright vertical Japanese: top-to-bottom, columns RIGHT TO LEFT. Do not display speaker labels or quotation marks. Thought stays a cloud with dots; speech tails stay attached to the correct speaker. Keep every panel boundary, character face/expression/pose/hand/clothing, tool, plant condition, bowl, food, architecture and color unchanged except the small areas needed for bigger balloons. Do not cover faces, hands or important evidence. Preserve any existing sound effects unchanged. No added people, words or repeated dialogue. Strong clean printed manga gothic, easy to read on a phone.
EXACT DIALOGUE IN ORDER: エルナ「今日は、ここで食べて。」 / コウ「まだ、畑は治ってない。」 / エルナ「でも、水は動いたよ。」

```
