# 第02話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：20素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-hunger.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e02-hunger-before-correction.png"]

採用時の指示：

```text
Edit this comic precisely; preserve its main upper shot, Ren's exact face/clothing/armor/location, and the single large upper sound ぐう… . Correct ONLY these issues: swap the TWO lower-panel SUBJECTS so RIGHT lower panel contains close black GLOVED HAND pressing stomach, LEFT lower panel contains the weak cyan chest star. Keep each hand anatomically correct; no extra hand. REMOVE every tiny white sound or letter in the lower row; only the original upper sound remains once. Make the cyan core and cyan armor seams FAINT and low energy in ALL three panels, still recognizably cyan star; no extinguished core, no new system labels. Preserve the pristine Japanese upper ぐう… punctuation. White gutters, the lower divider may remain diagonal; do not rotate lettering or whole panels. All other art unchanged.
```

## remake-untransform.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/02-untransform.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Close bare Ren hand emerging as black arm armor flakes into tiny blue light; red scarf remains, black short sleeve shirt underneath. Exhaustion, no new danger.
Exact layout and camera: Upper shallow core dimming insert; middle horizontal row RIGHT black wrist armor loosens into cyan motes / LEFT same hand now bare; lower larger view of the ordinary black short sleeve. All armor finishes fading before Mira touches him.
Exact speech in chronological order: []
Exact effects (each once, associated with physical cause): ["シュゥ…"]
Exact existing visible prop text: []. No other text.

```

## remake-e02-support-r2.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/remake-e02-support.png"]

採用時の指示：

```text
Edit ONLY the speech balloon and its Japanese lettering in the lower RIGHT panel. Current text is too small on a phone. Keep the exact line 英雄も、お腹は空くんですね。 once, upright Japanese top-to-bottom, columns right-to-left. Reflow into THREE columns RIGHT 英雄も、 / MIDDLE お腹は空く / LEFT んですね。 . Actual black glyphs must be about64px tall on this1024px canvas, bold and crisp. Enlarge white balloon to about330px wide and480px high on the LEFT side of Mira's lower panel; her full face, mouth, eyes, hand stay visible on RIGHT. Tail still points continuously at Mira mouth. Remove old tiny lettering completely before replacement, no duplicated letters or other dialogue. Preserve Ren eye insert and large upper support panel, ふら… once, exact faces/clothes/background and all panel borders. No new people.
```

## remake-invoice.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/04-invoice.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Rook in silver armor, blue cape, black gloves offers a paper sheet across the plaza. Ren's bare hand accepts the sheet. Paper is geometric unreadable lines only, no invented numbers.
Exact layout and camera: Upper medium Rook reserved silver-armored speaking face; lower shallow wide exchange of paper from his BLACK glove to Ren BARE fingers. The paper has abstract marks, no amounts.
Exact speech in chronological order: [{"speaker": "Rook", "text": "無許可の戦闘だ。", "columns": ["無許可の", "戦闘だ。"], "type": "speech"}]
Exact effects (each once, associated with physical cause): ["サッ"]
Exact existing visible prop text: []. No other text.

```

## remake-e02-debt.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/v6-debt.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Close unarmored Ren looking up from the same sheet with shocked eyebrows, chest not glowing. Mira and Rook remain beside plaza rubble.
Exact layout and camera: Upper horizontal row RIGHT invoice in BARE fingers / LEFT startled blue eye; lower larger Ren face asks exact line. Keep the source panel meanings and paper unchanged.
Exact speech in chronological order: [{"speaker": "Ren", "text": "助けたら、借金？", "type": "speech"}]
Exact effects (each once, associated with physical cause): ["ペラ…"]
Exact existing visible prop text: []. No other text.

```

## remake-crack.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/06-crack.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Close crack widening across a white aqueduct support above a gap. Water leaks downward. Only effect ミシ… . No people or rescue outcome.
Exact layout and camera: Two connected details: upper shallow hairline crack in white support, lower taller view follows leaking water down the SAME support. No people, no rescue result, no already-formed bridge.
Exact speech in chronological order: []
Exact effects (each once, associated with physical cause): ["ミシ…", "ポタ…"]
Exact existing visible prop text: []. No other text.

```

## remake-stranded.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/07-stranded.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Vertically establish damaged aqueduct: mother in brown shawl and small boy in green shirt stranded on tilted upper ledge; open gap below; rescuers Ren and Mira on intact LOWER opposite ledge. Clear unsafe and safe positions, no bridge yet.
Exact layout and camera: Large borderless vertical geography: family on UPPER RIGHT broken ledge, rescuers on LOWER LEFT intact ledge, gap between. Mother with brown shawl and boy with OLIVE GREEN shirt. Shouted mother line at top points to her mouth. Preserve one geography; no duplicate people.
Exact speech in chronological order: [{"speaker": "Mother", "text": "誰か…！", "columns": ["誰か…！"], "type": "speech"}]
Exact effects (each once, associated with physical cause): ["ゴロ…"]
Exact existing visible prop text: []. No other text.

```

## remake-barrier.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/08-barrier.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Rook's gloved palm bars Ren at a cordon on intact lower ledge; stranded parent and child on opposite distant ledge, no armor yet.
Exact layout and camera: Upper shallow black-gloved palm blocking Ren; lower medium Rook face speaks with family far above behind. Ren unarmored on lower-left safe ledge. No attack or bridge yet.
Exact speech in chronological order: [{"speaker": "Rook", "text": "立入禁止だ。", "columns": ["立入禁止だ。"], "type": "speech"}]
Exact effects (each once, associated with physical cause): ["スッ"]
Exact existing visible prop text: []. No other text.

```

## remake-set-down.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e02-set-down-before-correction.png"]

採用時の指示：

```text
Precisely edit this comic. Critical continuity repair: the LOWER panel currently has two Miras including a small child-shaped duplicate. Remove BOTH blonde figures from the lower background and replace their area with seamless empty white-city stone/sky. Ren and Rook remain unchanged; no other people in lower panel. Recompose ONLY the first two paper-action panels into a SHORT HORIZONTAL ROW: RIGHT hand places paper with トン once; LEFT bare hand releases paper. Below this row keep a larger Ren eye/face reaction, clear empty background. Reading RIGHT then LEFT then DOWN. Keep exact unarmored shirt/red scarf/bare hands. Keep abstract unreadable paper marks, no new text. Preserve drawing style, no mother or boy.
```

## remake-choice.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/10-choice.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Unarmored Ren leans toward danger, teeth set but visibly tired, Mira behind him sees his decision.
Exact layout and camera: Large emotional Ren face and forward-leaning ordinary-shirt shoulders. Keep the exact dialogue large; small edge of safe stone and scarf connects the place. No armor yet. Silent lower hand starting to reach.
Exact speech in chronological order: [{"speaker": "Ren", "text": "まだ、手は届く。", "columns": ["まだ、", "手は届く。"], "type": "speech"}]
Exact effects (each once, associated with physical cause): ["ギュ…"]
Exact existing visible prop text: []. No other text.

```

## remake-e02-hold-r2.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/remake-e02-hold.png"]

採用時の指示：

```text
Edit ONLY BOTH Ren speech balloons and their lettering. All art and panel borders MUST stay unchanged, especially beam sloping LOWER LEFT to UPPER RIGHT and BOTH boots braced. Phone-readable UPRIGHT actual glyphs65px tall on this1024-wide artwork. Upper line exact 戦う燃料がないなら、 in THREE columns RIGHT 戦う燃 / MIDDLE 料がない / LEFT なら、 . Enlarge white upper balloon within upper-right empty space; Ren face stays visible. Lower line exact 持ち上げるだけだ。 in THREE columns RIGHT 持ち上 / MIDDLE げるだ / LEFT けだ。 . Enlarge lower balloon into empty sky gap, about300px wide and350px tall, no covered hands, boots, beam contacts or family faces. Tails point to REN'S mouth, never mother. Remove old tiny glyphs completely before replacement, no duplicate dialogue. Preserve カチッ and ギギ… once each and all artwork.
```

## remake-rope-r2.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/remake-rope.png"]

採用時の指示：

```text
Recompose ONLY the LOWER large speech panel into a closer Mira-only speaker shot. Preserve upper RIGHT knot/LEFT citizens horizontal row EXACTLY. Lower panel shows ONE Mira waist-up beside same intact white-stone column/rope, face and hands large and clear; no visible Ren body in this lower panel. Ren CONTINUES holding the same beam offscreen, as shown by previous/next frames; a small same beam edge may remain at right. Lower speech exact この縄を、支えてください。 once in THREE UPRIGHT columns RIGHT この縄を、 / MIDDLE 支えて / LEFT ください。 . Make actual glyph height70px on1024 width, balloon at right with generous white padding, mouth tail to MIRA. No tiny text, thought dots, future safe family or invented captions. Preserve キュッ once in top knot panel. Detailed anime style, Mira identity/clothes and daytime light unchanged.
```

## remake-cross.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/13-cross.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Mother and boy cautiously step along held beam, grasping taut safety rope; residents pull rope from safe side, Ren's armor cracks while holding weight. They are MIDWAY, not safe yet.
Exact layout and camera: Large diagonal panel mother and boy MIDWAY on same inclined stone beam from upper-right toward lower-left, both holding taut safety rope; below shallow pair RIGHT Ren armored hands maintain load / LEFT residents pull safety rope. No one is safe yet.
Exact speech in chronological order: []
Exact effects (each once, associated with physical cause): ["ギシ…", "ザッ"]
Exact existing visible prop text: []. No other text.

```

## remake-safe.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/14-safe.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Mother and boy now both on dry intact safe ledge, hugging each other, relieved faces. Rope slack, beam still secured, no return to dangerous position.
Exact layout and camera: Wide safety establishing both mother and boy on intact LOWER LEFT safe ledge, followed by larger tender embrace with boy exact line. Their clothing matches earlier shots. Rope now slack. Ren stays supporting beam offscreen until safe.
Exact speech in chronological order: [{"speaker": "Boy", "text": "お母さん…！", "columns": ["お母さん…！"], "type": "speech"}]
Exact effects (each once, associated with physical cause): ["ぎゅ…"]
Exact existing visible prop text: []. No other text.

```

## remake-exhale.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e02-exhale-before-correction.png"]

採用時の指示：

```text
Edit ONLY lower-panel Ren's white speech balloon/lettering and its tail. Preserve exact spoken よかった…。 once, UPRIGHT bold glyphs about65px tall on1024 width, large enough for360px phone. Tail must connect down to REN'S MOUTH at left, not hair/forehead or Mira. Make soft wavering breathless outline, no thought dots. Top hands panel and ふぅ… unchanged; all faces, hands, costumes, cup and background unchanged. No other text.
```

## remake-e02-responsibility.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e02-e02-responsibility-before-correction.png"]

採用時の指示：

```text
Edit ONLY TWO Mira speech balloons and lettering in this comic. Phone-readable actual glyph height60-65px on1024-wide canvas. First upper line exact 王家の責任です。 in TWO upright columns RIGHT 王家の / LEFT 責任です。 . Enlarge first balloon into empty space without hiding any face. Second lower line exact あなた一人に払わせません。 in FOUR upright columns RIGHT to LEFT あなた / 一人に / 払わせ / ません。 . Widen lower balloon as needed, preserve Mira eyes/nose/mouth and paper/hands, her composed soft thin outline. Every spoken tail ends at Mira MOUTH, not forehead or Ren. Remove prior text completely, no duplicate or invented letters. Preserve all three rows, horizontal ring/paper vs Ren-eye row, パサ… once, all art/clothes/geography.
```

## remake-cancel.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e02-cancel-before-correction.png"]

採用時の指示：

```text
Edit ONLY Rook's lower-panel speech balloon and lettering. Exact text …承知しました。 once, upright vertical columns RIGHT …承知 / LEFT しました。 . Actual glyph height60-65px on1024 width for a360px phone. Enlarge balloon into empty background, keep ALL faces/hands/ring/paper visible. Tail continuously points at ROOK'S MOUTH on right. Calm ordinary oval, not thought dots. Preserve top horizontal reaction/ring row, lower shared scene, トン once, original art and all identities.
```

## remake-turn-fragment.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/18-turn-fragment.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: Mira turns over the guardian fragment already found in episode1; its outer crown crest turns away; backside still hidden from camera. Ren leans closer, curiosity replaces relief. No workshop number visible yet.
Exact layout and camera: A single quiet close-up: Mira fingers begin turning the SAME guardian core shard. Outer crown side turns away, REVERSE face and workshop inscription COMPLETELY HIDDEN until next image. No label or lettering on hidden side.
Exact speech in chronological order: []
Exact effects (each once, associated with physical cause): ["くる…"]
Exact existing visible prop text: []. No other text.

```

## remake-workshop-number.png

built-in image_gen

参照：["examples/zero-break/episode-02/art/19-workshop-number.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.

Existing moment and strict continuity: FIRST close reveal backside guardian fragment with etched small crown plus exact horizontal plate text 王室工房　七番 . Mira's fingertips and surprised eyes behind. Only this label on metal, not a speech balloon.
Exact layout and camera: One large macro reveal of SAME fragment REVERSE face with exact plate text 王室工房　七番, upright clear horizontal inscription, small existing crown. Fingers and Mira surprised eyes at edge. Do not name later enemy.
Exact speech in chronological order: []
Exact effects (each once, associated with physical cause): []
Exact existing visible prop text: []. No other text.

```

## remake-e02-inside-threat.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e02-e02-inside-threat-before-correction.png"]

採用時の指示：

```text
Edit ONLY the speech balloon/lettering in middle RIGHT Mira panel. Exact line これ、外から来た魔物じゃない。 once. UPRIGHT vertical glyphs actual60px tall on1024 width. THREE columns RIGHT これ、外から / MIDDLE 来た魔物じゃ / LEFT ない。 . Use a larger white balloon on far RIGHT inside Mira panel, reflow lettering to fit, never shrink. Her eyes, nose, mouth, hand and single shard remain visible. Tail continuously ends at Mira MOUTH. Preserve large upper shared scene, lower-left Ren reaction, palace ending view, all borders and all art/clothing. No new text or future enemy.
```
