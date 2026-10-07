# 第10話 — 実際に画像生成へ渡す指示

方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。
参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。

## 01-second-harvest

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Balt. Do NOT depict these absent reference characters anywhere, including background: Elna, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Same four beds with age-staggered sections: Kou and Balt harvest newly ready section while earlier harvested section is bare or freshly resown and younger sections remain smaller. Twine markers visible. Two hand closeups plus broad context.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 次の区画が、つながった。
Vertical columns from RIGHT to LEFT: 次の区画が、つ / ながった。

Speaker バルト (spoken, tail to speaker). Exact full text: 予定が、少し読めてきたな。
Vertical columns from RIGHT to LEFT: 予定が、少し読 / めてきたな。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 02-sixteen

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Elna at reservation ledger with sixteen simple small marks, Kou beside bought produce basket and own harvest; outside supplier acknowledges arrangement. Two unequal panels include limited supply clearly.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: まずは、一日十六食。
Vertical columns from RIGHT to LEFT: まずは、一日十 / 六食。

Speaker コウ (spoken, tail to speaker). Exact full text: 足りない時の仕入れも、決めてある。
Vertical columns from RIGHT to LEFT: 足りない時の仕 / 入れも、決めて / ある。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 03-partners

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three intimate panels at clean diner counter: Elna earnest facing Kou, her hand placing shop key on table, Kou thoughtfully reaching to joint crop-and-menu notebook rather than seizing key. Adult respectful partnership.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 畑と厨房、一緒に決めたい。
Vertical columns from RIGHT to LEFT: 畑と厨房、一緒 / に決めたい。

Speaker エルナ (spoken, tail to speaker). Exact full text: 店の相棒に、なってくれる？
Vertical columns from RIGHT to LEFT: 店の相棒に、な / ってくれる？

Speaker コウ (spoken, tail to speaker). Exact full text: 働く分も、きちんと分けよう。
Vertical columns from RIGHT to LEFT: 働く分も、きち / んと分けよう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 04-maintenance

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Iris. Do NOT depict these absent reference characters anywhere, including background: Balt, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Iris shows Elna how to open removable irrigation filter housing beside sturdy tank stand; Kou stands back listening, not doing every task. Closeups demonstrate same fitting as episode four; no modern gadgets.

EXACT TEXT IN READING ORDER:

Speaker イリス (spoken, tail to speaker). Exact full text: 詰まったら、ここを開ける。
Vertical columns from RIGHT to LEFT: 詰まったら、こ / こを開ける。

Speaker エルナ (spoken, tail to speaker). Exact full text: 直し方も、店に残しておく。
Vertical columns from RIGHT to LEFT: 直し方も、店に / 残しておく。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.

Reference 4 defines ONLY the irrigation filter, fitting and tank hardware. Preserve this same accessible removable housing in the new maintenance scene. Do not copy its panel composition.

```

## 05-seed-future

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Balt. Do NOT depict these absent reference characters anywhere, including background: Elna, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Balt and Kou beside small separate reserved seed-production strip of garden-leaf plants, a few plants left standing, NOT mature seed harvested already. Hand places plain marker, separate harvest basket for food.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: この畝は、次の種を残す。
Vertical columns from RIGHT to LEFT: この畝は、次の / 種を残す。

Speaker バルト (spoken, tail to speaker). Exact full text: 売る分だけじゃ、先へ続かん。
Vertical columns from RIGHT to LEFT: 売る分だけじゃ / 、先へ続かん。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 06-returner

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Large borderless warm diner entrance view: auburn young adult customer in ochre cloak returns slightly dusty from expedition, Elna smiles at serving window, empty familiar seat in foreground and hot meal ready. Kou assists quietly behind her, no duplicate character heads.

EXACT TEXT IN READING ORDER:

Speaker 客 (spoken, tail to speaker). Exact full text: 帰ってきたよ。
Vertical columns from RIGHT to LEFT: 帰ってきたよ。

Speaker エルナ (spoken, tail to speaker). Exact full text: おかえり。席、空いてる。
Vertical columns from RIGHT to LEFT: おかえり。席、 / 空いてる。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.

Reference 4 is ONLY the recurring customer's identity: young adult male, auburn hair, ochre cloak, simple brooch. Do not copy its layout, expressions or extra characters.

```

## 07-share-work

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Balt, Iris. Do NOT depict these absent reference characters anywhere, including background: Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Kou and Elna share plain illustrated maintenance/crop notebook on porch, smaller montage Balt observing seedlings and Iris storing spare fitting; characters in separate successive frames, not simultaneously duplicated. Quiet achieved trust, no magical new world omniscience.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 俺がいなくても、回るように。
Vertical columns from RIGHT to LEFT: 俺がいなくても / 、回るように。

Speaker エルナ (spoken, tail to speaker). Exact full text: そのための店、だね。
Vertical columns from RIGHT to LEFT: そのための店、 / だね。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 08-next-floor

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 42日目. 第二播種の一部と遅れていた第一播種区画を収穫。全48m²の安定供給実績はまだない。16食は自給と仕入れを合わせた営業枠。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Leon. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Final large scene: Leon at blue-awning diner brings small parchment sketch of colder upper-floor outpost, Kou and Elna look toward distant ascending stone stairs. Warm kitchen foreground and cool stairway beyond establish future, not new farm already built upstairs.

EXACT TEXT IN READING ORDER:

Speaker レオン (spoken, tail to speaker). Exact full text: 七階でも、この飯を出せるか？
Vertical columns from RIGHT to LEFT: 七階でも、この / 飯を出せるか？

Speaker コウ (spoken, tail to speaker). Exact full text: まず、畑と台所を見に行こう。
Vertical columns from RIGHT to LEFT: まず、畑と台所 / を見に行こう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.

CROP CONTINUITY: Newly sown garden-leaf seeds are tiny DARK BROWN-BLACK round seeds about 2mm across, never pale peas or beans. Preserve this physical seed identity across tests and sowing. Garden-leaf is a broad-leaf leafy crop; new sowings never become mature roots, carrots or fruit. Notebook drawings of future growth are plans, not real plants outside the notebook.

MANDATORY READING ORDER: Every sequential dialogue must appear in a strictly later, LOWER panel than the previous dialogue. Never put two sequential speaking panels side by side at the same height. Silent hand/tool inserts may be side by side. Do not reorder speech for composition. One main speaking panel per listed line is preferred. Spell casting is performed by Iris, not by Kou. Unknown future measurements and crops stay unpictured.
```

## 実際の追加生成：01-second-harvest-crop-fixed

```text
Use case: precise-object-edit. Edit the first referenced image only. Repair two agricultural details in image 1. Reference image 2 gives clean base-cut harvest; reference image 3 gives seed identity. Replace pale pearl-like seeds in the RIGHT middle sowing closeup with tiny DARK BROWN/BLACK approximately 2 mm round garden-leaf seeds. In ALL harvest views, Kou and Balt harvest green leaves by cutting just above soil using a small knife, as in image 2; harvested bunches contain NO attached soil and NO dirty dangling roots. Replace Kou's dirt-covered uprooted bunch with a clean cut-leaf bunch, and the LEFT middle closeup with a clean base cut above the soil. Keep the varied bed ages, same small newly sown patch, dialogue exact 次の区画が、つながった。 and 予定が、少し読めてきたな。, panels, faces, clothes and light. Sow and harvest are independent parallel tasks, not an instant-growth sequence. Preserve every element not explicitly named for repair. Keep upright Japanese vertical lettering integrated in the raster artwork, top-to-bottom columns read right-to-left. No new words, no added story events, no reflow of the existing dialogue, no new actors. High-quality finished smartphone vertical-scroll manga, same aspect ratio and resolution as target.

```

## 実際の追加生成：02-sixteen-slots-fixed

```text
Use case: precise-object-edit. Edit the first referenced image only. Only repair the reservation grid drawn in the notebook: EXACTLY SIXTEEN cells arranged as a clear 4 by 4 grid, each with one small black reservation dot, in the notebook closeup and corresponding top-panel notebook. No 3 by 4 twelve-cell grid. Keep the handwritten title 予約. Preserve all other panels, foods, hands, faces, exact speech balloons including 一日十六食, and font size. This is sixteen service reservations, not a claim that the farm alone supplies all sixteen. Preserve every element not explicitly named for repair. Keep upright Japanese vertical lettering integrated in the raster artwork, top-to-bottom columns read right-to-left. No new words, no added story events, no reflow of the existing dialogue, no new actors. High-quality finished smartphone vertical-scroll manga, same aspect ratio and resolution as target.

```

## 実際の追加生成：04-maintenance-sequence-fixed

```text
Use case: precise-object-edit. Edit the first referenced image only. Only reorder the three narrow maintenance action panels in the MIDDLE ROW for Japanese right-to-left reading: RIGHT = gloved hand opens the threaded filter collar (current left), CENTER = mesh cartridge pulled out (current center), LEFT = bare hands rinse cartridge at the outdoor utility tap (current right). Move whole panels WITHOUT horizontal mirroring; preserve the arrow and device shapes inside each panel. Keep all other panels, faces, book diagram, lettering, exact dialogue and font sizes unchanged. Preserve every element not explicitly named for repair. Keep upright Japanese vertical lettering integrated in the raster artwork, top-to-bottom columns read right-to-left. No new words, no added story events, no reflow of the existing dialogue, no new actors. High-quality finished smartphone vertical-scroll manga, same aspect ratio and resolution as target.

```
