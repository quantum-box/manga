# 第9話 — 実際に画像生成へ渡す指示

方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。
参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。

## 01-twelve

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Elna prepares twelve simple clean covered food containers on kitchen table, Kou confirms at ledger, background bought grain and meat with harvested leaves. Three panels cooking, lids, plan. No overflowing hundred-meal feast.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 三階の集結所まで、十二食。
Vertical columns from RIGHT to LEFT: 三階の集結所ま / で、十二食。

Speaker コウ (spoken, tail to speaker). Exact full text: 温かいうちに、渡そう。
Vertical columns from RIGHT to LEFT: 温かいうちに、 / 渡そう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 02-tools

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Two designated clean cooking pots, Elna points to kitchen-only utensils, small inset dirty irrigation buckets remain OUTSIDE on separate utility shelf; Kou wipes hands before touching packed food. Two unequal panels, no unsafe mixing.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: この鍋は、料理だけ。
Vertical columns from RIGHT to LEFT: この鍋は、料理 / だけ。

Speaker コウ (spoken, tail to speaker). Exact full text: 畑の桶とは、混ぜない。
Vertical columns from RIGHT to LEFT: 畑の桶とは、混 / ぜない。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 03-delay

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Stone gate lane inside third floor, Kou with small covered handcart of food, local gate worker in beige points to waiting cargo queue, Elna worried. No fighting or sword attack, delay is transport coordination.

EXACT TEXT IN READING ORDER:

Speaker 係員 (spoken, tail to speaker). Exact full text: 今日は、通行便が遅れる。
Vertical columns from RIGHT to LEFT: 今日は、通行便 / が遅れる。

Speaker コウ (spoken, tail to speaker). Exact full text: 受け渡し場所を、変えられる？
Vertical columns from RIGHT to LEFT: 受け渡し場所を / 、変えられる？

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 04-contact

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Leon. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Leon at nearby third-floor assembly entrance instructs assistant while Kou and Elna listen, short hand gesture showing safe nearby pickup location, clear geographical continuity and no gate bypass.

EXACT TEXT IN READING ORDER:

Speaker レオン (spoken, tail to speaker). Exact full text: 入口側で受け取る。連絡は俺がする。
Vertical columns from RIGHT to LEFT: 入口側で受け取 / る。連絡は俺が / する。

Speaker エルナ (spoken, tail to speaker). Exact full text: その場所なら、間に合う。
Vertical columns from RIGHT to LEFT: その場所なら、 / 間に合う。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 05-cart

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: One tall continuous scene of small handcart rolling down paved lane from diner toward visible nearby third-floor assembly arch, Elna walking beside Kou; closeup careful hands securing covered containers, no exposed food or magical flying cart.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 鍋を持つ人も、攻略隊なんだな。
Vertical columns from RIGHT to LEFT: 鍋を持つ人も、 / 攻略隊なんだな / 。

Speaker エルナ (spoken, tail to speaker). Exact full text: 食べるところまでが、私たちの仕事。
Vertical columns from RIGHT to LEFT: 食べるところま / でが、私たちの / 仕事。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 07-proof

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Leon. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Leon checks all twelve recipients and signs delivery note with abstract marks, closeup professional respectful face, Kou listening with Elna nearby. No vast gold payment or instant huge contract.

EXACT TEXT IN READING ORDER:

Speaker レオン (spoken, tail to speaker). Exact full text: 十二食、欠けずに届いた。
Vertical columns from RIGHT to LEFT: 十二食、欠けず / に届いた。

Speaker レオン (spoken, tail to speaker). Exact full text: 次は、続けられるかを見よう。
Vertical columns from RIGHT to LEFT: 次は、続けられ / るかを見よう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 06-team-eats

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: . Do NOT depict these absent reference characters anywhere, including background: Kou, Elna, Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three unequal panels in assembly courtyard: modest adult adventurer squad receives covered meals, one tired brown-haired swordswoman tastes hot greens and grain, relaxed smiles around low table. Weapons sheathed away from food. No wounded person magically healed.

EXACT TEXT IN READING ORDER:

Speaker 隊員 (spoken, tail to speaker). Exact full text: 今日は、ちゃんと飯を食えた。
Vertical columns from RIGHT to LEFT: 今日は、ちゃん / と飯を食えた。

Speaker 隊員 (spoken, tail to speaker). Exact full text: 帰ったら、店にも寄る。
Vertical columns from RIGHT to LEFT: 帰ったら、店に / も寄る。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 08-one-delivery

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 36日目. 十二食を三階の集結所へ。七階へ無検証の長距離配送をしない。料理は当日調理。供給は自家収穫と仕入れ。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Large quiet evening return to diner, empty cleanable containers and handcart, Kou and Elna sit on porch tired but satisfied. Plot not magically mature everywhere. Small lantern warmth under blue awning.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 一便はできた。毎日は、これからだ。
Vertical columns from RIGHT to LEFT: 一便はできた。 / 毎日は、これか / らだ。

Speaker エルナ (spoken, tail to speaker). Exact full text: 今日は、この十二人分でいい。
Vertical columns from RIGHT to LEFT: 今日は、この十 / 二人分でいい。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 実際の追加生成：01-twelve-bowls-fixed

```text
Use case: precise-object-edit. Edit the first referenced image only. Establish the delivery prop consistently. In the TOP establishing panel place EXACTLY TWELVE round, brown glazed POTTERY meal bowls (smooth ceramic interior, no wood grain), matching fitted brown pottery lids. Arrange 3 rows of 4 bowls, fully visible and countable, with no extra bowls in the background. Elna holds her ladle over ONE open bowl ON THE TABLE; she does NOT hold an additional bowl. The open bowl contains grain, browned meat, orange root-vegetable pieces and dark green garden-leaf greens. Eleven bowls are lidded; one remains open while she portions it. Replace the rectangular white boxes throughout this page with this same brown round pottery bowl and fitted lid. Preserve exact Japanese 三階の集結所まで、十二食。 and 温かいうちに、渡そう。, face identity, panel order, all other objects and lettering size. The middle action row already reads correctly from right (filled bowl) to left (lid closes), keep that order. Preserve every element not explicitly named for repair. Keep upright Japanese vertical lettering integrated in the raster artwork, top-to-bottom columns read right-to-left. No new words, no added story events, no reflow of the existing dialogue, no new actors. High-quality finished smartphone vertical-scroll manga, same aspect ratio and resolution as target.

```

## 実際の追加生成：01-twelve-count-fixed

```text
Use case: precise-object-edit. Image 1 is the target. Any second reference is ONLY for the brown glazed pottery food-bowl design, not its counts, cast, layout or events. Only correct the count in the TOP panel. It currently has twelve lidded bowls PLUS a thirteenth open bowl behind them. Remove the lidded bowl in the REAR ROW, SECOND FROM THE LEFT, and move the current open bowl into that exact position instead. Erase the old separate thirteenth open-bowl position to show only table. Elna's ladle and hand now serve this open bowl in the rear-row second-from-left slot. Final inventory on that table is EXACTLY 12 brown pottery bowls in THREE ROWS OF FOUR: front 4 lidded, middle 4 lidded, rear 3 lidded + 1 open. Keep the established pottery design and all other panels/text exactly unchanged. Preserve every element not named for repair. Upright integrated raster Japanese vertical lettering, columns right-to-left. No new speech or story events, no font shrinking, no digital overlays. Same finished manga style and target aspect ratio.

```

## 実際の追加生成：02-tools-separated-fixed

```text
Use case: precise-object-edit. Image 1 is the target. Any second reference is ONLY for the brown glazed pottery food-bowl design, not its counts, cast, layout or events. Remove every dirty garden bucket from the INSIDE kitchen shelves. Replace those shelf objects with clean cooking pots and clean ceramic crockery. A garden bucket may be visible only THROUGH the distant open back doorway, OUTSIDE in the garden beyond the clear wall/door threshold, never on kitchen shelves or next to food. The spoon/cooking-pot assignment poster stays unchanged. Replace the lower foreground wooden open meal boxes with brown glazed pottery meal bowls from reference 2, with fitted lids and food inside. All other characters, faces, cooking pots and exact dialogue remain unchanged. Preserve every element not named for repair. Upright integrated raster Japanese vertical lettering, columns right-to-left. No new speech or story events, no font shrinking, no digital overlays. Same finished manga style and target aspect ratio.

```

## 実際の追加生成：03-delay-cargo-fixed

```text
Use case: precise-object-edit. Image 1 is the target. Any second reference is ONLY for the brown glazed pottery food-bowl design, not its counts, cast, layout or events. Only standardize the cart cargo in every panel. It carries TWO dedicated clean wooden food-transport outer crates with padded clean cotton liners, containing the brown fitted-lid glazed pottery bowls from reference 2 (six per crate, twelve total), and ONE closed metal cooking/serving pot. No loose bread, uncovered cooked food, open stew in wooden boxes, or garden buckets on the cart. In the upper establishing panel both outer crates are closed and covered with clean cloth. The bottom left cargo-detail panel can show one outer crate lid open, revealing SIX individually CLOSED pottery bowls packed 3 by 2; the other crate and single pot stay closed. Preserve the cart structure, porter, Kou/Elna, all exact dialogue, faces and other panels. Preserve every element not named for repair. Upright integrated raster Japanese vertical lettering, columns right-to-left. No new speech or story events, no font shrinking, no digital overlays. Same finished manga style and target aspect ratio.

```

## 実際の追加生成：05-cart-cargo-fixed

```text
Use case: precise-object-edit. Image 1 is the target. Any second reference is ONLY for the brown glazed pottery food-bowl design, not its counts, cast, layout or events. Only standardize the cart cargo in every panel: TWO dedicated clean wooden padded food-transport outer crates containing twelve individually fitted-lid brown glazed pottery bowls, six per crate, plus ONE closed metal cooking/serving pot under the clean cloth. Remove extra metal pots, garden pails, loose food and bread baskets. Keep the left closeup of Kou checking the single metal cooking pot lid; the right closeup shows Elna securing the clean cloth over one outer crate. All food remains enclosed. Preserve all faces, exact dialogue including 鍋を持つ人も、攻略隊なんだな。, font size and other panels. Preserve every element not named for repair. Upright integrated raster Japanese vertical lettering, columns right-to-left. No new speech or story events, no font shrinking, no digital overlays. Same finished manga style and target aspect ratio.

```

## 実際の追加生成：06-team-eats-cast-fixed

```text
Use case: precise-object-edit. Image 1 is the target. Any second reference is ONLY for the brown glazed pottery food-bowl design, not its counts, cast, layout or events. Repair delivery cast and bowls. The TOP panel is the third-floor assembly dining table for a twelve-person ADVENTURER squad with Kou and Elna standing as caterers. Balt and Iris are NOT present: replace the seated gray-bearded farmer in the brown hat with an unrelated middle-aged female adventurer in an olive cloak with no hat; replace the seated short-navy-haired goggle-wearing technician with an unrelated dark-skinned male adventurer with short cropped hair, a navy traveling cloak and NO goggles. Preserve Leon, Kou, Elna and the red-haired female squad member. Add the remaining squad members farther down the same long table to indicate the twelve-person team, including the brown-haired man speaking in the bottom panel; varied faces/cloaks, weapons sheathed away from food. No other named main cast. Replace EVERY wooden meal bowl with the same brown glazed POTTERY bowl from reference 2, now open, containing grain with browned meat/root vegetables and garden-leaf greens. No wood grain on bowl interiors. The lower red-haired woman and brown-haired male speakers and exact dialogue remain unchanged. Keep large readable speech and panel order. Preserve every element not named for repair. Upright integrated raster Japanese vertical lettering, columns right-to-left. No new speech or story events, no font shrinking, no digital overlays. Same finished manga style and target aspect ratio.

```

## 実際の追加生成：07-proof-bowls-fixed

```text
Use case: precise-object-edit. Image 1 is the target. Any second reference is ONLY for the brown glazed pottery food-bowl design, not its counts, cast, layout or events. Only standardize the delivery receipt and bowls. Replace all wooden bento-kit boxes, miniature plates, wrapped food bundles and extra dishes in the TOP establishing panel with EXACTLY TWELVE brown glazed POTTERY meal bowls of the design from reference 2, arranged clearly as THREE ROWS OF FOUR fully visible on the table. These twelve bowls are open for count verification and contain grain, browned meat/root vegetables and garden-leaf greens. No thirteenth bowl and no held bowl. Replace the left meal-detail inset with a close view of these same pottery bowls. The receipt checklist inset has twelve simple checkmarks, with no newly invented words. Preserve all faces, Leon's clipboard, exact two Japanese dialogue balloons and font size. Preserve every element not named for repair. Upright integrated raster Japanese vertical lettering, columns right-to-left. No new speech or story events, no font shrinking, no digital overlays. Same finished manga style and target aspect ratio.

```

## 実際の追加生成：08-one-delivery-cargo-fixed

```text
Use case: precise-object-edit. Image 1 is the target. Any second reference is ONLY for the brown glazed pottery food-bowl design, not its counts, cast, layout or events. Only standardize the RETURN cart: TWO now-empty wooden food-transport outer crates with clean folded padded cotton liners plus ONE closed metal cooking/serving pot, matching the delivery cart. Remove extra garden pails, buckets and metal pots. No remaining food or unexplained filled containers on the cart. All faces, poses, blue-awning diner, exact two dialogue balloons and panels stay unchanged. Preserve every element not named for repair. Upright integrated raster Japanese vertical lettering, columns right-to-left. No new speech or story events, no font shrinking, no digital overlays. Same finished manga style and target aspect ratio.

```
