# 第8話 — 実際に画像生成へ渡す指示

方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。
参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。

## 01-ready

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: First small mature leafy sections at day thirty-five, other later-sown sections still small, one shaded first section smaller; Elna crouches excited, Kou checks one leaf. Gentle morning tower light, no enormous vegetables.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 採って、いい？
Vertical columns from RIGHT to LEFT: 採って、いい？

Speaker コウ (spoken, tail to speaker). Exact full text: 一株、厨房で確かめよう。
Vertical columns from RIGHT to LEFT: 一株、厨房で確 / かめよう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 02-cut

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three unequal hand shots: clean harvest basket on path, Kou cuts garden-leaf crop above soil carefully, leaves placed gently without crushing or dirty roots. Elna watches. Only selected mature sections harvested.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 土を、葉につけないように。
Vertical columns from RIGHT to LEFT: 土を、葉につけ / ないように。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 03-grade

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Elna and Kou sort leaves at designated utility table, usable irregular small leaves in one basket, damaged leaves separately in reject tray. Closeups genuine leaves and hands. Do not present rotten material as food.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 重さと、使える分を分ける。
Vertical columns from RIGHT to LEFT: 重さと、使える / 分を分ける。

Speaker エルナ (spoken, tail to speaker). Exact full text: 小さくても、使える葉はある。
Vertical columns from RIGHT to LEFT: 小さくても、使 / える葉はある。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 04-weigh

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Mechanical beam scale weighing baskets, Kou records simple tally in notebook, Elna sees modest harvest. No giant produce mountain; approximately five kilograms usable total across harvested sections.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 使える分は、五キロほど。
Vertical columns from RIGHT to LEFT: 使える分は、五 / キロほど。

Speaker エルナ (spoken, tail to speaker). Exact full text: まず、この量で考えよう。
Vertical columns from RIGHT to LEFT: まず、この量で / 考えよう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 05-kitchen

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Kitchen washed harvest transferred separately, Elna slices leaves to bite-sized pieces, Kou sets clean bowl; three different-size closeups and medium cooking view. Stable cream apron and blue headscarf.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: この大きさなら、使いやすい。
Vertical columns from RIGHT to LEFT: この大きさなら / 、使いやすい。

Speaker エルナ (spoken, tail to speaker). Exact full text: 食べやすい切り方にしよう。
Vertical columns from RIGHT to LEFT: 食べやすい切り / 方にしよう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 06-meal-reveal

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: . Do NOT depict these absent reference characters anywhere, including background: Kou, Elna, Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Large borderless appetizing hero composition: steaming grain-and-meat bowl topped with bright freshly cooked garden-leaf greens, bowl near auburn young adult customer's rough hands, lower warm eager face before first bite. Food richly drawn, no added text except exact small speech balloon.

EXACT TEXT IN READING ORDER:

Speaker 客 (spoken, tail to speaker). Exact full text: いただきます。
Vertical columns from RIGHT to LEFT: いただきます。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.

Reference 4 is ONLY the recurring customer's identity: young adult male, auburn hair, ochre cloak, simple brooch. Do not copy its layout, expressions or extra characters.

```

## 07-earned

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three panels: customer enjoys first bite silently; closeup Kou's relieved face after weeks of waiting; Elna beside him with soft pleased expression. Calm adult emotion, no instant buff numbers. Diner warm, crop plot distant.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: やっと、畑が皿になった。
Vertical columns from RIGHT to LEFT: やっと、畑が皿 / になった。

Speaker エルナ (spoken, tail to speaker). Exact full text: 私も、待ってた。
Vertical columns from RIGHT to LEFT: 私も、待ってた / 。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.

Reference 4 is ONLY the recurring customer's identity: young adult male, auburn hair, ochre cloak, simple brooch. Do not copy its layout, expressions or extra characters.

```

## 08-deliver-next

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 35日目・最初の播種から28日. 第一播種の育った二区画、計8m²を収穫。遅い一区画は残す。使用可能量は約5.1kgという創作上の実測。全48m²を同時収穫しない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Leon. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Warm evening kitchen, Kou and Elna prepare clean containers beside remaining harvest basket, Leon at doorway confirms next morning delivery. No already-packed food stored overnight: preparation is containers and schedule.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 採れた。次は、届ける番だ。
Vertical columns from RIGHT to LEFT: 採れた。次は、 / 届ける番だ。

Speaker レオン (spoken, tail to speaker). Exact full text: 明日の便、待っている。
Vertical columns from RIGHT to LEFT: 明日の便、待っ / ている。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 実際の追加生成：05-kitchen-sequence-fixed

```text
Use case: precise-object-edit. Only swap the two small preparation-detail panels in the middle: RIGHT = basket of washed whole wet green leaves (current left); LEFT = Elna chopping these leaves (current right). Move whole panels without horizontal mirroring. Keep the top washing panel, bottom cutting panel, all exact Japanese text, lettering size, faces, clothes and background unchanged. Upright Japanese vertical dialogue remains integrated in the raster. No extra text, no new actors, no changed story events, no new equipment. Preserve every element not explicitly named, same finished manga style and target aspect ratio.

```

## 実際の追加生成：07-earned-dish-fixed

```text
Use case: precise-object-edit. Edit the first referenced image only. Repair only the meal in the TOP panel of image 1 to match the already served dish in image 2: the same deep rustic speckled pottery bowl of grain, browned meat slices and glossy dark-green garden-leaf greens. The auburn-haired male customer is now eating a bite with his fork from that same bowl, with some food remaining. Preserve every face, his ochre cloak, Elna, the existing SFX, and the lower Kou and Elna dialogue panels unchanged. Preserve every element not explicitly named for repair. Keep upright Japanese vertical lettering integrated in the raster artwork, top-to-bottom columns read right-to-left. No new words, no added story events, no reflow of the existing dialogue, no new actors. High-quality finished smartphone vertical-scroll manga, same aspect ratio and resolution as target.

```

## 実際の追加生成：08-deliver-next-empty-crates

```text
Use case: precise-object-edit. Edit the first referenced image only. Repair night preparation: Kou and Elna are inspecting EMPTY clean lined transport crates and folding clean cloth liners for tomorrow's delivery, not holding or sorting raw harvested leaves at night. Remove raw harvested produce from their hands, baskets, sink and countertop in this NIGHT preparation scene. Replace those hand actions with checking an empty lined crate and folding a fresh dry liner. All crates remain visibly empty. No cooked meals packed overnight. Preserve the exact two dialogue balloons, their size and speakers, Leon at the doorway, all faces/clothes, lighting, and existing panels. Preserve every element not explicitly named for repair. Keep upright Japanese vertical lettering integrated in the raster artwork, top-to-bottom columns read right-to-left. No new words, no added story events, no reflow of the existing dialogue, no new actors. High-quality finished smartphone vertical-scroll manga, same aspect ratio and resolution as target.

```
