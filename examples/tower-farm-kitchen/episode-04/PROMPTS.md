# 第4話 — 実際に画像生成へ渡す指示

方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。
参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。

## 01-carry

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Kou carries two manageable wooden water buckets along path, not over crop bed; small closeup blistered palm; Elna at diner kitchen doorway worried about empty prep table. Seedlings small, daytime.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 水を運ぶだけで、午前が終わる。
Vertical columns from RIGHT to LEFT: 水を運ぶだけで / 、午前が終わる / 。

Speaker エルナ (spoken, tail to speaker). Exact full text: 仕込みにも、来てほしい。
Vertical columns from RIGHT to LEFT: 仕込みにも、来 / てほしい。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 02-iris

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Iris. Do NOT depict these absent reference characters anywhere, including background: Elna, Balt, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Iris enters beside empty wooden tank and laid-out ceramic pipe segments; medium Kou faces her, lower her hand sketches tank above beds. Goggles on forehead, navy short hair. No modern PVC or electronics.

EXACT TEXT IN READING ORDER:

Speaker イリス (spoken, tail to speaker). Exact full text: 桶を上げれば、流れるよ。
Vertical columns from RIGHT to LEFT: 桶を上げれば、 / 流れるよ。

Speaker コウ (spoken, tail to speaker). Exact full text: 同じ量を、配れる？
Vertical columns from RIGHT to LEFT: 同じ量を、配れ / る？

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 03-stand

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Balt, Iris. Do NOT depict these absent reference characters anywhere, including background: Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three practical construction panels: Iris checks tank and support sketch, Kou and Balt assemble braced thick timber free-standing platform, Elna sees strong diagonal bracing. Water tank is still empty until stand complete. Do not place 160kg on flimsy roof.

EXACT TEXT IN READING ORDER:

Speaker イリス (spoken, tail to speaker). Exact full text: 水だけで、百六十キロ。
Vertical columns from RIGHT to LEFT: 水だけで、百六 / 十キロ。

Speaker コウ (spoken, tail to speaker). Exact full text: 台から、作り直そう。
Vertical columns from RIGHT to LEFT: 台から、作り直 / そう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 04-unequal

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Iris. Do NOT depict these absent reference characters anywhere, including background: Elna, Balt, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three unequal closeups same elapsed test: different outlets pour into identical measuring cups, near cup contains more than far cup; lower Kou and Iris looking at difference. Tank only modest height, pipe has clear joints and accessible valves.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 手前ばかり、多い。
Vertical columns from RIGHT to LEFT: 手前ばかり、多 / い。

Speaker イリス (spoken, tail to speaker). Exact full text: 高さと、管の長さが違うから。
Vertical columns from RIGHT to LEFT: 高さと、管の長 / さが違うから。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 05-zones

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Iris. Do NOT depict these absent reference characters anywhere, including background: Elna, Balt, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Iris points to simple wooden stopcock, Kou opens ONE bed section and measures delivered water; other sections closed. Hands and pipe physically coherent. Main outlet larger than tiny modern drip emitter.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 一列ずつ開けて、量を測る。
Vertical columns from RIGHT to LEFT: 一列ずつ開けて / 、量を測る。

Speaker イリス (spoken, tail to speaker). Exact full text: 壊れても、直せる形にしよう。
Vertical columns from RIGHT to LEFT: 壊れても、直せ / る形にしよう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 06-clean

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Elna, Iris. Do NOT depict these absent reference characters anywhere, including background: Kou, Balt, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Two closeups and one face panel: removable mesh filter lifted from accessible housing, Elna rinses removable part in utility basin, Iris shows simple fitting. Irrigation tool cleaning not on food-prep surface.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: この網、私にも外せる？
Vertical columns from RIGHT to LEFT: この網、私にも / 外せる？

Speaker イリス (spoken, tail to speaker). Exact full text: うん。ここを、緩めて。
Vertical columns from RIGHT to LEFT: うん。ここを、 / 緩めて。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 07-magic-lift

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Iris. Do NOT depict these absent reference characters anywhere, including background: Elna, Balt, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Tall composition: small water spell lifts EXISTING water from source barrel to raised tank, luminous blue stream visibly connects both water bodies, source level falls; then valve sends stored water gently to one section while Iris lowers hand exhausted but satisfied. No conjured infinite water.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 魔法は、桶に上げる時だけ。
Vertical columns from RIGHT to LEFT: 魔法は、桶に上 / げる時だけ。

Speaker イリス (spoken, tail to speaker). Exact full text: 流す間は、手が空くね。
Vertical columns from RIGHT to LEFT: 流す間は、手が / 空くね。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 08-time-saved

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 8〜12日目. 160L桶は独立した丈夫な架台。配水は最初、一列ずつ容器で量を測る。細い自動点滴を既製品として出さない。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Large warm scene: Kou crouches inspecting SMALL seedlings, water delivery controlled in one background section; lower Elna invites him at blue-awning diner, still modest plot, no broad mature crop. His hands relaxed.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 空いた時間で、苗を見る。
Vertical columns from RIGHT to LEFT: 空いた時間で、 / 苗を見る。

Speaker エルナ (spoken, tail to speaker). Exact full text: それから、昼ごはんを作ろう。
Vertical columns from RIGHT to LEFT: それから、昼ご / はんを作ろう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.
```

## 実際の追加生成：01-carry-before-build

```text
Use case: precise-object-edit. Remove the raised barrel and its elevated wooden support from the upper-left background. Replace that area with ordinary paving and a small source-water tub standing at ground level. No raised water tank or finished irrigation system exists yet in this scene. Preserve all other panels, faces, anatomy, tools, backgrounds, lighting, exact Japanese dialogue, font size, balloons and speaker tails unchanged except where explicitly requested. No added words, actors or future events.

```

## 実際の追加生成：02-iris-proposal

```text
Use case: precise-object-edit. This is the PROPOSAL before construction. In the upper panel lower the EMPTY wooden tank onto the ground, remove its raised support and all installed irrigation pipes from the crop beds. Keep the loose ceramic pipe parts on the table. Replace both middle demonstration inserts that currently show flowing water with SILENT closeups of unassembled ceramic pipe joints and a plain empty measuring bucket. No water flows anywhere. Preserve the paper DRAWING of the future raised tank in Iris's hands; only that sketch may show the planned system. Preserve all other panels, faces, anatomy, tools, backgrounds, lighting, exact Japanese dialogue, font size, balloons and speaker tails unchanged except where explicitly requested. No added words, actors or future events.

```

## 実際の追加生成：04-unequal-reading-order

```text
Use case: precise-object-edit. In the LOWER conversation panel swap the left/right positions of the two characters and their associated speech balloons, so Kou is at the RIGHT with exact text『手前ばかり、多い。』 read FIRST; Iris is at the LEFT with exact text『高さと、管の長さが違うから。』 read SECOND. Keep upright vertical Japanese, no horizontal mirroring or reversed glyphs. Preserve exact expressions and clothing. In upper measuring panels adjust the far outlet branch to sit slightly HIGHER than the near outlet, with coherent pipe joints, so both elevation and path length differences are visibly plausible. Keep the near cup fuller than far cup, all cups equal in shape. Preserve all other panels, faces, anatomy, tools, backgrounds, lighting, exact Japanese dialogue, font size, balloons and speaker tails unchanged except where explicitly requested. No added words, actors or future events.

```

## 実際の追加生成：06-clean-closed-first

```text
Edit this exact vertical Japanese fantasy comic sheet, retaining its dimensions, painted style, all panel borders, faces, colors, dialogue, and every panel below the first panel unchanged. Fix only the filter in the TOP FIRST PANEL: Elna has not opened or removed it yet. The black cylindrical mesh cartridge must be fully seated INSIDE the clear upright filter housing, with its black round top lid screwed completely closed, flush to the top collar. No mesh or cartridge protrudes above the housing. Elna's right fingertips REST gently on the CLOSED lid as she asks how to remove it; she is not lifting anything. Elna and Iris keep their existing body positions. The top balloon must keep the exact existing Japanese vertical wording この網、私にも外せる？ with its question mark, large legible letters and correct tail to Elna. The middle RIGHT panel is then Iris explaining うん。ここを、緩めて。, the middle LEFT panel is the subsequent actual cartridge removal, and the bottom panel is Elna washing the removed cartridge. These three later panels and all their lettering must remain identical to the input. The sequence is closed first, explain second, remove third, rinse fourth. Do not modify anything else.

```

## 実際の追加生成：06-clean-sequence-fixed

```text
Use case: precise-object-edit. Repair the operation sequence. In the TOP panel Elna asks この網、私にも外せる。 while touching the collar of the CLOSED assembled mesh filter, with the cartridge still INSIDE, not already pulled out. Preserve both women's faces, poses, exact text and clothes. In the MIDDLE row move Iris's instruction panel うん。ここを緩めて。 to the RIGHT, and the closeup of the mesh cartridge being pulled out to the LEFT, with no horizontal mirroring. Leave the bottom outdoor rinsing panel unchanged. Keep the exact black collar, glass housing, mesh cylinder, tank and all dialogue size. Upright Japanese vertical dialogue remains integrated in the raster. No extra text, no new actors, no changed story events, no new equipment. Preserve every element not explicitly named, same finished manga style and target aspect ratio.

```

## 実際の追加生成：07-magic-lift-caster

```text
Use case: precise-object-edit. In the UPPER large panel make IRIS the water-spell caster: her hand visibly guides the blue lifted stream from the source barrel to the raised tank. Kou's currently raised arm must be lowered into a relaxed observing pose; no magic emanates from Kou or his hand. Keep Kou on the left as the speaker of exact text『魔法は、桶に上げる時だけ。』, with its balloon tail still to him. Iris remains the navy-haired technician with copper goggles. The blue stream is lifted EXISTING water, continuously connects the low source tub to the raised tank, not from thin air. Keep all lower panels unchanged. Preserve all other panels, faces, anatomy, tools, backgrounds, lighting, exact Japanese dialogue, font size, balloons and speaker tails unchanged except where explicitly requested. No added words, actors or future events.

```

## 実際の追加生成：08-time-saved-sequence-fixed

```text
Use case: precise-object-edit. Only reorder the THREE tiny sowing-action panels beneath the top panel: RIGHT = palm holding tiny dark seeds (current left), CENTER = finger places a seed (current center), LEFT = watering the newly sown soil (current right). Move entire panels without horizontal mirroring. Preserve all other panels, exact dialogue, faces, dishes, seed size and young seedlings. Upright Japanese vertical dialogue remains integrated in the raster. No extra text, no new actors, no changed story events, no new equipment. Preserve every element not explicitly named, same finished manga style and target aspect ratio.

```
