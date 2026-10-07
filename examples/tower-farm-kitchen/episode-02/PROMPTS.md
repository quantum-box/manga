# 第2話 — 実際に画像生成へ渡す指示

方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。
参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。

## 01-morning

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Same garden at early light, two unequal panels: Kou examines yesterday's marked wilted plant still rooted, Elna behind him with empty watering can set down; closeup his cautious face and wet ground beginning to dry. No recovered jungle overnight.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: まだ、戻らないな。
Vertical columns from RIGHT to LEFT: まだ、戻らない / な。

Speaker エルナ (spoken, tail to speaker). Exact full text: 待つのも、仕事？
Vertical columns from RIGHT to LEFT: 待つのも、仕事 / ？

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 02-balt

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Balt. Do NOT depict these absent reference characters anywhere, including background: Elna, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Wide Balt arrives on walking path in brown hat; separate closeup Balt observing marked plant; lower Kou listens. Balt is experienced and practical, not foolish. Dug plant from yesterday lies separately and is not replanted alive.

EXACT TEXT IN READING ORDER:

Speaker バルト (spoken, tail to speaker). Exact full text: 昨日と同じ株を見ろ。
Vertical columns from RIGHT to LEFT: 昨日と同じ株を / 見ろ。

Speaker バルト (spoken, tail to speaker). Exact full text: 抜いた株は、元には戻らん。
Vertical columns from RIGHT to LEFT: 抜いた株は、元 / には戻らん。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 03-compare

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Elna. Do NOT depict these absent reference characters anywhere, including background: Kou, Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Overhead plot with one marked comparison strip and other rows; hand closeup tying plain twine marker without cutting roots; Elna looking from changed strip to remaining area. Plants vary realistically, no flashy transformation.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: この列だけ、別に記録する。
Vertical columns from RIGHT to LEFT: この列だけ、別 / に記録する。

Speaker エルナ (spoken, tail to speaker). Exact full text: 全部を、変えないの？
Vertical columns from RIGHT to LEFT: 全部を、変えな / いの？

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 04-record

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Two unequal panels: Kou writes simple marks and blank spaces in notebook at plot edge; closeup Elna reading over shoulder. A subtle empty translucent recording frame may hover but NO added visible text or numerical claims. Notebook has sketch marks only.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 知らない数字は、空欄でいい。
Vertical columns from RIGHT to LEFT: 知らない数字は / 、空欄でいい。

Speaker バルト (spoken, tail to speaker). Exact full text: 分かったことだけ、残せ。
Vertical columns from RIGHT to LEFT: 分かったことだ / け、残せ。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 05-new-roots

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Balt. Do NOT depict these absent reference characters anywhere, including background: Kou, Elna, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Time has advanced to day five. Three panels: same twine marker and modestly less wilted plant, gentle root inspection showing a few NEW white fine roots amid remaining damaged roots, Balt's restrained pleased expression. Recovery is partial, no instant glow or giant growth.

EXACT TEXT IN READING ORDER:

Speaker コウ (spoken, tail to speaker). Exact full text: 新しい根だ。
Vertical columns from RIGHT to LEFT: 新しい根だ。

Speaker バルト (spoken, tail to speaker). Exact full text: まだ弱い。急ぐな。
Vertical columns from RIGHT to LEFT: まだ弱い。急ぐ / な。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 06-loss

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Large quiet panel of bare damaged strip where dead plants have been removed, Elna kneeling with sad face; lower Kou quietly placing tray to plan new sowing. Do not fill dead area with new mature plants.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: こっちは、戻らないのね。
Vertical columns from RIGHT to LEFT: こっちは、戻ら / ないのね。

Speaker コウ (spoken, tail to speaker). Exact full text: 次の苗を、育てよう。
Vertical columns from RIGHT to LEFT: 次の苗を、育て / よう。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 07-existing-harvest

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna, Balt. Do NOT depict these absent reference characters anywhere, including background: Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Three unequal shots: Balt shows a surviving mature garden-leaf plant; Kou cuts usable leaves gently into clean shallow basket; Elna checks leaf size for kitchen. Source is surviving established plants, not seeds sown in this story.

EXACT TEXT IN READING ORDER:

Speaker バルト (spoken, tail to speaker). Exact full text: この葉は、若いうちが柔らかい。
Vertical columns from RIGHT to LEFT: この葉は、若い / うちが柔らかい / 。

Speaker エルナ (spoken, tail to speaker). Exact full text: 切りやすい大きさが、欲しい。
Vertical columns from RIGHT to LEFT: 切りやすい大き / さが、欲しい。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 08-dish

```text
Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.

EPISODE TIME AND STATE: 2〜5日目. 排水は動く。新しい根は数日後に一部で確認。株数と収量をまだ保証しない。バルトが現地の知識を渡す。

CAST LOCK: The ONLY main-reference characters allowed in this image are: Kou, Elna. Do NOT depict these absent reference characters anywhere, including background: Balt, Iris, Leon. Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.

SCENE: Warm kitchen: basket passed from Kou's hands to Elna, narrow chopping closeup, large finished steaming dish at counter and their faces. Keep raw garden work off cooking surface. No magical buff display.

EXACT TEXT IN READING ORDER:

Speaker エルナ (spoken, tail to speaker). Exact full text: 食べる人まで、畑の続きだね。
Vertical columns from RIGHT to LEFT: 食べる人まで、 / 畑の続きだね。

Speaker コウ (spoken, tail to speaker). Exact full text: 来週の分も、作りたい。
Vertical columns from RIGHT to LEFT: 来週の分も、作 / りたい。

Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.
```

## 実際の追加生成：05-new-roots-timed

```text
Use case: precise-object-edit. Add one small clean white rectangular narration caption in empty space at the top, with exact upright vertical Japanese text『五日目』, columns top-to-bottom, crisp readable manga lettering. This marks several days since drainage repair. Do not move or change characters, roots, plant or marker. Existing dialogue must stay exact and unchanged. Preserve all panels, character identity, faces, hands, clothing, poses, tools, architecture, food, lighting and ALL existing Japanese dialogue, punctuation, size, balloons and speaker tails completely unchanged except the explicitly named edit. Do not add other text, characters or events.

```

## 実際の追加生成：06-loss-cleared

```text
Use case: precise-object-edit. Edit this finished Japanese comic ONLY in the dead garden strip: remove all standing dead stems, dead vines and brown wilted leaves from the damaged row in the upper panel and from the foreground/lower panel. These dead plants have been cleared before re-sowing. Replace the removed stems with bare rough brown soil and a few small detached dead fragments on the surface. The dead row must be visibly empty and unplanted, with no living crops. Keep all other plants outside this row unchanged. Keep all panel boundaries, faces, hands, poses, tray of seed bowls, tools, architecture, lighting, colors, exact Japanese text, font size, balloon shapes and tails completely unchanged. Exact text remains エルナ『こっちは、戻らないのね。』 and コウ『次の苗を、育てよう。』. Do not add any text, seedling, character or event.

```

## 実際の追加生成：08-dish-sequence-fixed

```text
Use case: precise-object-edit. Only swap the two small cooking-action panels in the middle row: RIGHT = chopping carrots (currently left); LEFT = stew simmering in pot (currently right). Japanese temporal reading must proceed from right to left. Move whole panels, without horizontally mirroring. Preserve all exact text, faces, meals, other panels and SFX. Upright Japanese vertical dialogue remains integrated in the raster. No extra text, no new actors, no changed story events, no new equipment. Preserve every element not explicitly named, same finished manga style and target aspect ratio.

```
