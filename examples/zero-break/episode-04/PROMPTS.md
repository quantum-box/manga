# 第04話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：18素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-back-stairs.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/01-back-stairs.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Mira guides unarmored Ren down palace rear spiral stairs toward closed heavy workshop door; sunshine above, warm amber light below. No prison bars.
Exact layout, camera and mechanics: Upper shallow ordinary boot steps downward on palace rear spiral stairs. Lower large over-shoulder geography: Mira ahead guides ONE unarmored Ren from sunlight toward closed heavy workshop door and warm amber lower light. Ren exact spoken question, large two-column balloon. No prison bars or Noa/room reveal yet.
Exact speech in chronological order: [{"speaker": "Ren", "text": "牢屋じゃないよな。", "columns": ["牢屋じゃ", "ないよな。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["コツ…"]
Exact visible prop text: []. No other text.

```

## remake-key.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/02-key.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close Mira inserts a single brass key and turns it in workshop lock, bare fingers visible; door still closed, room and new character hidden.
Exact layout, camera and mechanics: SHORT horizontal row RIGHT Mira bare fingers insert ONE brass key / LEFT SAME key turns in lock. Door stays closed; workshop and new character hidden. White gutter between genuine separate panels; sound at lock.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["カチャ"]
Exact visible prop text: []. No other text.

```

## remake-workshop.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/03-workshop.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST reveal open oily workshop: pipes, wooden workbench, round pressure boiler at back, young adult orange-haired mechanic Noa in blue overalls and goggles on head, waving from bench. Mira and Ren enter, no danger.
Exact layout, camera and mechanics: One large workshop FIRST reveal: doorway foreground Ren/Mira, oily pipes and wooden workbench lead eye to round boiler at back, ONE adult orange-haired Noa waving from bench. Mira exact introduction of workshop large, tail to her mouth. Warm indoor amber light, no danger/steam leak yet.
Exact speech in chronological order: [{"speaker": "Mira", "text": "私たちの工房よ。", "columns": ["私たちの", "工房よ。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["ギィ…"]
Exact visible prop text: []. No other text.

```

## remake-e04-noa-r2.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/remake-e04-noa.png"]

採用時の指示：

```text
Edit only the lettering of this current Webtoon for PHONE legibility. Preserve all art, frames, prop continuity and sounds. Actual upright Japanese glyph height80-90px at1024px width, black clear lettering, roomy balloon2-3columns, enlarge panel/balloon space if needed without covering eyes, hands or working diagram. Panel1 Mira exact 整備士のノアよ。 split RIGHT 整備士の / LEFT ノアよ。 . Panel2 Noa exact 魔力ゼロ？ split RIGHT 魔力 / LEFT ゼロ？ . Panel4 Noa exact こっちじゃ普通。 split RIGHT こっちじゃ / LEFT 普通。 . All oval tails to correct speaker mouth. Exactly4 frames1/[2,3]/4 and same broken meter.
```

## remake-catch.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/05-catch.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close Ren's bare hands catch same broken handheld meter, Noa orange glove releases it, no duplicate meter. Face softening from tension.
Exact layout, camera and mechanics: Short horizontal row RIGHT Noa orange glove releases ONE broken handheld meter toward Ren bare palms / LEFT same meter rests securely in both bare hands. No duplicate meter/teleportation. Below small Ren relieved eye insert. No arm plates.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["パシッ"]
Exact visible prop text: []. No other text.

```

## remake-common.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/06-common.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren smiles slightly at Noa, no armor. Mira gathers a copper testing lead but no new advanced power gadget.
Exact layout, camera and mechanics: One quiet large unarmored Ren softening face, exact line in three legible columns. Small ordinary hands/meter at bottom anchors bench, Mira nearby prepares simple copper lead. No advanced gadget or power reveal.
Exact speech in chronological order: [{"speaker": "Ren", "text": "…俺だけじゃないんだ。", "columns": ["…俺だけ", "じゃないんだ。"], "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

```

## remake-fault.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e04-fault-before-correction.png"]

採用時の指示：

```text
Edit this existing Webtoon image with small continuity corrections. Preserve its polished anime rendering, character identities, phone-legible type and actual frame layout. Keep the exact two side-by-side panels (read RIGHT gauge then LEFT vibrating red valve), every brass pipe and every sound placement intact. Remove EVERY readable numeral, number and letter from the round pressure-gauge dial. Keep only plain black tick marks, the high pressure needle, and a simple red danger arc. Weathered brass circular rim, pale dial, pipe connection unchanged. The same gauge later releases pressure: no invented scale. Preserve exactly ONE カタカタ next to valve, no extra text. No character/event changes.
```

## remake-notice.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e04-notice-before-correction.png"]

採用時の指示：

```text
Edit this existing Webtoon image with small continuity corrections. Preserve its polished anime rendering, character identities, phone-legible type and actual frame layout. Keep exactly two stacked panels and exact Noa dialogue 圧力が、戻らない。 in large upright Japanese vertical lettering with orange-haired adult Noa speaking and tail to his mouth. The steam sound シュー… is incorrectly printed twice. Preserve the single upper-panel シュー… at the actual leaking pipe. REMOVE ONLY the lower duplicated シュー… and restore the surrounding background there. Any readable numbers on background pressure-gauge dials must be removed, leaving plain tick marks, a red danger arc and high needle. Preserve Ren ordinary soft black shirt, red scarf, bare hands, tiny cyan chest star; no chest armor yet. Preserve all poses, workshop geometry and frame count.
```

## remake-cover.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/09-cover.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren moves between Noa and leaking boiler, raises one black armored forearm; full body stays black shirt/red scarf, energy limited. Noa ducks beside control pipes.
Exact layout, camera and mechanics: Upper short close-up cyan lattice and black plates snap onto ONLY ONE Ren forearm. Lower large diagonal protective scene: Ren single armored forearm between Noa and leaking boiler, other hand BARE, torso soft black shirt/red scarf. Exact warning in jagged balloon tail to REN MOUTH. Noa ducks toward controls; no full armor or projected shield.
Exact speech in chronological order: [{"speaker": "Ren", "text": "下がって！", "columns": ["下がって！"], "type": "speech"}]
Exact effects (each once, near physical cause): ["カチッ"]
Exact visible prop text: []. No other text.

```

## remake-valve-search.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e04-valve-search-before-correction.png"]

採用時の指示：

```text
Edit this existing Webtoon image with small continuity corrections. Preserve its polished anime rendering, character identities, phone-legible type and actual frame layout. Preserve these exact three panels: upper geography, lower RIGHT orange-gloved Noa tracing the brass pipe joint, lower LEFT jammed red valve with exactly one カタ… . Correct ONLY Ren's protective arm pose in the UPPER panel: his LEFT forearm and LEFT hand remain clad in black faceted armor with thin cyan seams and are RAISED with palm facing the boiler/steam, physically shielding adult Noa between the leaking pipe and Noa's face. His RIGHT forearm and RIGHT hand are BARE, relaxed/lowered, not touching any pipe. His torso is a soft black shirt and red scarf, no full armor. Noa follows the pipe from behind this protection. Keep pipe route, orange gloves, red valve and all frames unchanged. Remove readable dial numerals if present; abstract ticks and red band only. No speech added, no duplicated sounds.
```

## remake-e04-pipe-map-r2.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/remake-e04-pipe-map.png"]

採用時の指示：

```text
Edit only the lettering of this current Webtoon for PHONE legibility. Preserve all art, frames, prop continuity and sounds. Actual upright Japanese glyph height80-90px at1024px width, black clear lettering, roomy balloon2-3columns, enlarge panel/balloon space if needed without covering eyes, hands or working diagram. Panel1 Mira exact この弁で、 split RIGHT この / LEFT 弁で、 . Panel4 Mira exact 圧を逃がせる。 split RIGHT 圧を / LEFT 逃がせる。 . Exactly4 panels1/[2,3]/4, every blue/red connected pipe line, Noa's correspondence to brass wheel, exactly ONE バサッ remain. Tails to Mira mouth.
```

## remake-open-valve.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e04-open-valve-before-correction.png"]

採用時の指示：

```text
Edit this existing Webtoon image with small continuity corrections. Preserve its polished anime rendering, character identities, phone-legible type and actual frame layout. Preserve exactly these three panels and their causal order: upper RIGHT orange-gloved Noa opens the SAME brass relief wheel with exactly one ギュッ; upper LEFT gauge needle has fallen; lower wide panel relief steam exits upward with exactly one プシュー. On the pressure gauge remove EVERY numeral/letter: weathered circular brass rim, pale dial, plain black ticks, simple red danger arc, low needle. Crucial continuity correction in LOWER wide panel: Ren STILL has his LEFT forearm and LEFT hand clad in black faceted partial armor with thin cyan seams. Raise that LEFT armored palm protectively between Noa and the boiler so he continues guarding against the final loose cap in the next strip. His RIGHT hand remains BARE, torso remains a SOFT black shirt with red scarf. No full body armor and no deactivation yet. Preserve Noa's orange glove turning wheel, Mira's position, pipe connections and frame count. No dialogue, no other text, no duplicate characters.
```

## remake-last-fragment.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/13-last-fragment.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: One loose metal cap fragment flies; Ren's single armored forearm catches it with other bare hand holding Noa back safely. Boiler now vented, all three uninjured.
Exact layout, camera and mechanics: Upper shallow ONE loose cap fragment approaches. Lower large diagonal Ren SAME single black-cyan armored forearm catches/deflects it, other BARE hand keeps Noa back on safe side. Boiler already venting upward, all three uninjured. One fragment only, no blast outcome.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["カンッ"]
Exact visible prop text: []. No other text.

```

## remake-shared-load.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/14-shared-load.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren exhales and lowers armored forearm, looks to smiling Noa and Mira; sparse steam clears.
Exact layout, camera and mechanics: One large Ren relieved face, exact line in three or four readable vertical columns. He lowers SAME armored forearm; other hand bare, shirt/scarf unchanged. Smiling Noa and Mira farther behind, sparse steam clearing, no new event.
Exact speech in chronological order: [{"speaker": "Ren", "text": "全部、俺が受けなくていいのか。", "columns": ["全部、俺が", "受けなくて", "いいのか。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["ふぅ…"]
Exact visible prop text: []. No other text.

```

## remake-e04-finite-r2.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/remake-e04-finite.png"]

採用時の指示：

```text
Edit only the lettering of this current Webtoon for PHONE legibility. Preserve all art, frames, prop continuity and sounds. Actual upright Japanese glyph height80-90px at1024px width, black clear lettering, roomy balloon2-3columns, enlarge panel/balloon space if needed without covering eyes, hands or working diagram. Panel1 Noa exact 有限だよ。 split RIGHT 有限 / LEFT だよ。 . Panel3 Noa exact でも、使い方は変えられる。 split RIGHT でも、 / MIDDLE 使い方は / LEFT 変えられる。 . Exactly3 stacked panels, declining blue plot abstract/no numbers, ONE サラ… . Tails to Noa mouth.
```

## remake-team-sign-r2.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/remake-team-sign.png"]

採用時の指示：

```text
The wooden sign in BOTH its appearances must say exactly 救助隊 in three LARGE horizontal Japanese characters. The middle character is 助, its LEFT radical is 且 with enclosed horizontal strokes; it is NOT 功. Replace only lettering to exact 救助隊, retain actual plaque perspective and clear readable thick calligraphy. No extra letters. Exactly3 panels[1,2]/3, sign-lifting hands/poses, ONE コトッ unchanged.
```

## remake-missing-wires.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/17-missing-wires.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close Noa's orange-gloved finger traces blank disconnected block on city circuit map. No residents shown disappearing, no full conspiracy answer.
Exact layout, camera and mechanics: One quiet macro map, Noa orange-gloved finger traces an EMPTY disconnected block among simple connected city circuits. No readable location names/numbers, no people vanishing or conspiracy answer. End on blank absence, no sound clutter.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

```

## remake-e04-friend.png

built-in image_gen

参照：["examples/zero-break/episode-04/art/v6-friend.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa beside blank block map, hand clenched, goggles pushed up, worried genuine personal face. Ren watches empathetically.
Exact layout, camera and mechanics: Upper Noa worried face first exact line. Middle horizontal row RIGHT orange-gloved hand clenches beside blank map / LEFT Ren empathetic eyes. Lower larger Noa second exact line. Warm workshop light, personal concern; no friend image, kidnapping scene or later captives yet.
Exact speech in chronological order: [{"speaker": "Noa", "text": "昨日まで、", "type": "speech"}, {"speaker": "Noa", "text": "友達が住んでた。", "type": "speech"}]
Exact effects (each once, near physical cause): ["ギュ…"]
Exact visible prop text: []. No other text.

```
