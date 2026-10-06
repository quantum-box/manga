# 第06話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：18素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-dawn-plan.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/01-dawn-plan.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Dawn beside upper sky rail loading platform, Ren Mira Noa study paper roster; convoy carriage beyond closed gate. Seventeen live prisoners expected, no arbitrary extra vehicle or advanced form.
Exact layout, camera and mechanics: Upper wide dawn platform geography and CLOSED gate, one occupied sky-rail carriage beyond. Lower horizontal RIGHT Ren face exact dialogue 3 large upright columns / LEFT Mira/Noa share roster, bare Ren hands. No armor or prisoners rescued yet.
Exact speech in chronological order: [{"speaker": "Ren", "text": "一人ずつ、確認する。", "columns": ["一人ずつ、", "確認する。"], "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```

## remake-roster.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/02-roster.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close Mira pencil marking a row on roster, large exact number 十七人 visible. Names depicted abstract except friend ハル. No all-rescued marks yet.
Exact layout, camera and mechanics: Short horizontal row RIGHT Mira pencil finds expected total 十七人 / LEFT finger stops on only legible name ハル. Blank boxes remain unchecked before rescue, other names abstract ruled strokes, no victory marks. Same roster carried throughout.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["サラ…"]
Exact visible prop text: [{"text": "十七人", "type": "prop", "orientation": "horizontal"}, {"text": "ハル", "type": "prop", "orientation": "horizontal"}]. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```

## remake-rail-geography.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/03-rail-geography.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Sky-rail prisoner carriage above cloud chasm, solid maintenance catwalk with ladder to carriage on left, secure exit gate at upper platform. Establish safe rescue route before peril. No falling carriage yet.
Exact layout, camera and mechanics: ONE wide overhead geography view: occupied rail compartment beside intact maintenance catwalk, ladder lies folded on catwalk, secure exit gate at far end, cloud chasm below. Clear route and anchor ledge before danger. No carriage falling or enemy close-up.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```

## remake-inspection.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/04-inspection.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa crawls through underside maintenance hatch using orange gloves and simple tool, orange hair/goggles consistent. Train held stationary beside catwalk.
Exact layout, camera and mechanics: Upper short horizontal RIGHT Noa orange glove opens underside hatch / LEFT small hand tool releases access catch. Lower angled larger Noa crawls through same maintenance hatch, feet supported by intact catwalk, train stationary. No magical lock breaking.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["カチ"]
Exact visible prop text: []. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```

## remake-e06-unlock.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/v6-unlock.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa unlocks prisoner compartment from service panel; inside young adult Haru dark brown short hair green workshirt grey trousers, relieved. Single door opening, no escape complete yet.
Exact layout, camera and mechanics: Upper Noa orange glove turns service latch. Middle short horizontal RIGHT single compartment door opens / LEFT Haru adult18 brown short hair GREEN eyes GREEN work shirt grey trousers visibly recognizes Noa inside. Lower Noa face exact dialogue in3 large columns with calm speech tail. Haru is NOT a small boy; occupants still inside.
Exact speech in chronological order: [{"speaker": "Noa", "text": "ハル、迎えに来た。", "type": "speech"}]
Exact effects (each once, near physical cause): ["カチャ"]
Exact visible prop text: []. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```

## remake-security-wakes.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-security-wakes-before-correction.png"]

採用時の指示：

```text
Edit this finished Japanese colour Webtoon. Mandatory story/continuity correction below takes priority over the reference's current composition. Replace layout with EXACT FOUR framed panels. Top full width closeup Ren's ordinary black-shirt chest, tiny CYAN star waking under red scarf. Middle horizontal row: RIGHT bare forearm with cyan wire lattice, LEFT SAME arm covered by black faceted plates locking, ONE カチッ beside lock. Bottom wide panel grey STONE guardian PURPLE core awakening, its stone foot presses a rail coupling; ONE ゴゴ…; COUPLING NOT BROKEN YET. Ren fully basic black/cyan armored once at edge, no helmet. Do not show a huge full-size Ren portrait instead of assembly. Preserve anime character designs, golden steampunk city, clean upright Japanese integrated lettering. At1024 width actual glyphs80-90px. NO rules/separator lines within balloons. No added dialogue or effects, no duplicate figures within a panel.
```

## remake-wrong-target.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-wrong-target-before-correction.png"]

採用時の指示：

```text
Edit this Japanese full-colour Webtoon artwork, preserve characters and existing panels except specified local correction. Change ONLY lowest panel: remove Mira from carriage window. Keep carriage occupied by ordinary residents, and keep Ren armored face foreground. Mira is already on safe catwalk, so she must NOT be in carriage. All three panels and one ガキン unchanged.
```

## remake-carriage-falls.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-carriage-falls-before-correction.png"]

採用時の指示：

```text
Edit this finished Japanese colour Webtoon. Mandatory story/continuity correction below takes priority over the reference's current composition. Preserve two diagonal panels, scenery and one ギギ…. Bottom Ren MUST have full BLACK faceted BASIC chest/arms/legs armor with CYAN star and seams, same as previous scene. Mira dress remains. Both stand on intact side catwalk; one occupied rear carriage tilts away over gap with all residents still inside. No ordinary bare forearms/shirt here, no residents in air, no new form. Preserve anime character designs, golden steampunk city, clean upright Japanese integrated lettering. At1024 width actual glyphs80-90px. NO rules/separator lines within balloons. No added dialogue or effects, no duplicate figures within a panel.
```

## remake-change-choice.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-change-choice-before-correction.png"]

採用時の指示：

```text
Edit this finished Japanese colour Webtoon. Mandatory story/continuity correction below takes priority over the reference's current composition. Replace with exact THREE framed panels. Top large Ren full basic black/cyan armor chooses rescue, speaks exact 敵より、先に！ in upright vertical two large columns with jagged balloon tail to his mouth. Middle horizontal RIGHT closeup armored hand is clenched; LEFT SAME hand opens toward rail carriage. This clenched-to-open order must be right-to-left. No other words or sounds. Red scarf unchanged. Preserve anime character designs, golden steampunk city, clean upright Japanese integrated lettering. At1024 width actual glyphs80-90px. NO rules/separator lines within balloons. No added dialogue or effects, no duplicate figures within a panel.
```

## remake-catch-carriage.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/10-catch-carriage.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren in basic black armor grabs falling compartment UNDER its floor from braced catwalk support; feet secure against support ledge, lifts weight, seventeen captives still inside. Not floating without anchor.
Exact layout, camera and mechanics: Upper horizontal RIGHT ordinary anchored armored boot wedges solid catwalk support ledge / LEFT both armored hands contact UNDERSIDE of SAME tilted compartment floor. Lower large diagonal geography Ren shoulders/body brace upward holding car, both feet anchored on solid ledge, people still INSIDE windows. Catwalk intact, no levitation/no extra Ren in same panel. Exactly one ドン at contact.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ドン"]
Exact visible prop text: []. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```

## remake-armor-peeling.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-armor-peeling-before-correction.png"]

採用時の指示：

```text
Edit this Japanese full-colour Webtoon artwork, preserve characters and existing panels except specified local correction. Replace every GREY STONE slab directly above Ren's hands with continuous RIVETED STEEL underside of the SAME rescue rail carriage. This is a TRAIN CAR FLOOR with bolt rows, metal chassis/rectangular beams, NOT rock/rubble/stone. In top and bottom BOTH armored hands press metal underside, never release. Keep all four panels, cracked black-cyan plates, core/boots inserts, exact large thought 長くは、もたない。 and one ピシ…. Mira remains beside him. No other edits.
```

## remake-e06-ladder.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-e06-ladder-before-correction.png"]

採用時の指示：

```text
Edit this Japanese full-colour Webtoon artwork, preserve characters and existing panels except specified local correction. Keep the present geometry, four panels, dialogues, horizontal locked bridge ladder, armored Ren BOTH hands below carriage floor. Add exactly ONE integrated sound カチッ near Noa's orange-gloved hand locking ladder's metal clamp in middle LEFT panel. No other sounds. No separator lines in balloons. Leave Ren support and text unchanged.
```

## remake-help-next.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-help-next-before-correction.png"]

採用時の指示：

```text
Edit this finished Japanese colour Webtoon. Mandatory story/continuity correction below takes priority over the reference's current composition. Replace with EXACT THREE panels. Top wide: occupied carriage LEFT, intact catwalk RIGHT, rigid ladder bridges HORIZONTALLY across gap with both ends LOCKED. A resident already safe on catwalk supports hand of SAME small yellow-dress girl crossing from carriage. Haru short brown hair green work shirt stays LAST INSIDE carriage door behind her. Ren full basic black/cyan armor/red scarf BELOW, BOTH armored hands support carriage floor continuously and BOTH boots on intact catwalk. Bottom horizontal RIGHT clasp of resident and girl's hands ONE ぎゅ… / LEFT Ren face effort with both arms still up. No speech. Do not draw a vertical ladder or anyone climbing down. Preserve anime character designs, golden steampunk city, clean upright Japanese integrated lettering. At1024 width actual glyphs80-90px. NO rules/separator lines within balloons. No added dialogue or effects, no duplicate figures within a panel.
```

## remake-last-hand.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-last-hand-before-correction.png"]

採用時の指示：

```text
Edit this finished Japanese colour Webtoon. Mandatory story/continuity correction below takes priority over the reference's current composition. Preserve two-panel Noa rescuing adult Haru with exact 手を、離すな！ and one ガシッ. Remove SILVER-HAIRED KNIGHT ROOK from upper background completely; he has not arrived yet. Keep Mira and saved residents behind Noa. Haru brown short hair green eyes green work shirt is LAST leaving carriage, Noa orange gloved hand firmly holds wrist. Carriage visible empty behind Haru. Preserve anime character designs, golden steampunk city, clean upright Japanese integrated lettering. At1024 width actual glyphs80-90px. NO rules/separator lines within balloons. No added dialogue or effects, no duplicate figures within a panel.
```

## remake-all-seventeen.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-all-seventeen-before-correction.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. Correct ONLY the clipboard's check list: the current image has too many boxes. Draw EXACTLY 17 red tick boxes arranged in clearly separated groups of FIVE + FIVE + FIVE + TWO, with blank gaps between groups. Count explicitly: first group 5, second group 5, third group 5, final group 2. Heading 十七人 and first name ハル only. No row numbers, no extra boxes. Clipboard has 17, not 18/19/20. Do not show any other checked sheet in the background. Preserve 3 framed panels, Haru green workshirt and Mira with flower, one カッ by pen, silent relieved reunion. No speech.
```

## remake-e06-release.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e06-e06-release-before-correction.png"]

採用時の指示：

```text
Edit this Japanese full-colour Webtoon artwork, preserve characters and existing panels except specified local correction. Keep four panels with empty carriage falling away and Ren armor dissolving then exhausted ordinary cloth-shirt knees. ONLY fix top Ren's feet: BOTH boots must stand on BROAD FLAT INTACT METAL WALKWAY FLOOR, not a narrow railing, not a ledge beam. Widen foreground platform directly underneath both soles, stable support. Keep SAME empty falling carriage/one シュウ…/exact …全員、いるな。 unchanged.
```

## remake-pass.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/17-pass.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Freed Haru with brown hair, green eyes and green shirt hands Mira the metal pass marked 英雄認定場 on the outside safe catwalk.
Exact layout, camera and mechanics: ONE horizontal right-to-left handoff: RIGHT adult Haru brown short hair GREEN eyes/green workshirt holds ONE metal pass / LEFT Mira bare fingers receive SAME pass. Exact big horizontal prop label 英雄認定場, rest plain. Safe catwalk in morning, Noa not mistaken for Haru, Ren ordinary shirt.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["スッ"]
Exact visible prop text: [{"text": "英雄認定場", "type": "prop", "orientation": "horizontal"}]. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```

## remake-e06-rook-blocks.png

built-in image_gen

参照：["examples/zero-break/episode-06/art/v6-rook-blocks.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: At exit gate Rook silver armor blue cape stands with sheathed sword blocking group. Ren unarmored kneeling stands slowly, Noa and Mira shelter17 survivors behind.
Exact layout, camera and mechanics: Upper wide exit gate Rook silver hair silver/gold armor BLUE cape sword SHEATHED blocks path, first exact line large. Middle horizontal RIGHT Rook black glove lowered by sheathed sword / LEFT unarmored tired Ren starts standing. Lower Rook sober face second exact line3largecols. Mira/Noa protect survivors behind; no drawn blade, arrest/rescue outcome or fight yet.
Exact speech in chronological order: [{"speaker": "Rook", "text": "王室への反逆、", "type": "speech"}, {"speaker": "Rook", "text": "という扱いになる。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

PHONE READABILITY OVERRIDE: all spoken/thought Japanese glyphs must be 80-90px ACTUAL character height at1024px width, split lines into2-3 upright vertical columns of at most6 glyphs, right-to-left column order. Enlarge white balloons and speech panel height as needed, no tiny type. Each specified effect exactly ONCE. True horizontal rows only at most2 panels (except simple reaction inserts), no tall side panel spanning multiple stacked rows. All rescue supports persist across later moments until explicitly released.
```
