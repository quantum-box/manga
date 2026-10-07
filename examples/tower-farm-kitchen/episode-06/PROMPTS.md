# 第6話 — 実際に画像生成へ渡す指示

方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。
参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。

## 01-large-portion

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Warm diner kitchen, Elna cheerfully adds extra food to guest bowl, Kou next to small ledger looks concerned but kind. Two unequal panels bowl then faces. Do not imply new seedlings harvested.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 大盛り、つけといたよ。
Vertical columns from RIGHT to LEFT: 大盛り、つけと / いたよ。

Speaker コウ (spoken, tail to speaker). Exact full text: その分の原価は？
Vertical columns from RIGHT to LEFT: その分の原価は / ？

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 02-costs

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three hand closeups: purchased grain sack and meat basket invoice with abstract marks, seed packet and tool, Kou's worn hands. Elna listening beside counter, purchased produce basket visible.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 自分の畑の野菜も、ただじゃない。
Vertical columns from RIGHT to LEFT: 自分の畑の野菜 / も、ただじゃな / い。

Speaker コウ (spoken, tail to speaker). Exact full text: 種と、働いた時間がある。
Vertical columns from RIGHT to LEFT: 種と、働いた時 / 間がある。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 03-coins

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Top view six copper coins next to one meal, smaller closeup several expense piles and ledger sketch, lower Kou explaining to Elna. Exactly six sale coins in first view. NO readable text besides dialogue, no profit waterfall chart.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 六枚もらって、全部は残らない。
Vertical columns from RIGHT to LEFT: 六枚もらって、 / 全部は残らない / 。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 04-wages

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three intimate unequal conversation panels: Kou earnest at ledger, Elna surprised and thoughtful, Kou replies. Quiet kitchen after closing, table clean, no other speakers.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 残りから、家賃と賃金を払う。
Vertical columns from RIGHT to LEFT: 残りから、家賃 / と賃金を払う。

Speaker エルナ (spoken, tail to speaker). Exact full text: 私たちの働いた分も？
Vertical columns from RIGHT to LEFT: 私たちの働いた / 分も？

Speaker コウ (spoken, tail to speaker). Exact full text: そこを削ると、続かない。
Vertical columns from RIGHT to LEFT: そこを削ると、 / 続かない。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 05-two-dishes

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Elna and Kou choose two practical dishes on clean prep counter, one grain-and-meat bowl and one soup, shared ingredients laid separately. Small inset simple blank menu board without text. Do not display dozens of fancy dishes.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 今日は、二品に絞ろう。
Vertical columns from RIGHT to LEFT: 今日は、二品に / 絞ろう。

Speaker コウ (spoken, tail to speaker). Exact full text: 同じ仕込みで、出せるものに。
Vertical columns from RIGHT to LEFT: 同じ仕込みで、 / 出せるものに。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 06-cook

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Unequal closeups: washed leaves chopped on designated board; Elna adds leaves LAST to steaming pan or pot; larger shoulder view her timing heat. Kou only assists by handing clean ingredients. Food moisture and steam appetizing, no magical fireworks.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 葉は、最後に。
Vertical columns from RIGHT to LEFT: 葉は、最後に。

Speaker エルナ (spoken, tail to speaker). Exact full text: 色と食感を、残したい。
Vertical columns from RIGHT to LEFT: 色と食感を、残 / したい。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 07-reservation

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Auburn-haired young adult customer in ochre cloak returns at counter with steaming dish; medium Elna listens smiling, lower Kou looks toward seedling plot outside. Same customer as episode three, not Leon.

EXACT TEXT IN READING ORDER:

Speaker 客 (spoken, tail to speaker). Exact full text: 次の帰りも、この席に来たい。
Vertical columns from RIGHT to LEFT: 次の帰りも、こ / の席に来たい。

Speaker エルナ (spoken, tail to speaker). Exact full text: 予約、受けていいかな。
Vertical columns from RIGHT to LEFT: 予約、受けてい / いかな。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.

Reference 4 is ONLY the recurring customer's identity: young adult male, auburn hair, ochre cloak, simple brooch. Do not copy its layout, expressions or extra characters.

```

## 08-limit

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 18〜20日目. 主食と肉、葉菜の多くは仕入れ。6銅貨定食の差引2.6は賃金や家賃を払う原資で純利益ではない。庭葉はまだ苗。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Large quiet partnership scene under blue awning: Elna writes small reservation list with abstract marks, Kou beside her holding crop notebook, small plot at dusk. Serious hopeful sense of limited but workable business.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 畑に合わせて、数を決めよう。
Vertical columns from RIGHT to LEFT: 畑に合わせて、 / 数を決めよう。

Speaker エルナ (spoken, tail to speaker). Exact full text: 売り切れも、先に伝える。
Vertical columns from RIGHT to LEFT: 売り切れも、先 / に伝える。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```
