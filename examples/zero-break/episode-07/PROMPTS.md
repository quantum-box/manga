# 第07話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：18素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-e07-girl-steps.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/v6-girl-steps.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. In the TOP panel recolor ONLY Noa's hair to vivid ORANGE, keeping his adult face, goggles on his head, green eyes, blue overalls, black shirt, orange work gloves. Rook's sword must be COMPLETELY SHEATHED, only hilt and black gloved hand visible; replace the exposed blade in the top and detail panels with dark scabbard and hilt. Girl speaks exactly この人、私たちを出してくれた。 and ONE タッ. Keep 4 panels top, RIGHT hilt detail / LEFT girl's hand, bottom girl.
```

## remake-hand-stops.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/02-hand-stops.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. Rook does NOT draw his sword. Replace any exposed silver blade with the CLOSED dark sword scabbard, hilt and guard. Black gloved hand clenches the hilt beside the scabbard throat. Keep the two horizontal panels RIGHT clenched hand ONE ぎゅ… / LEFT blue eye stopping at girl's voice. No speech.
```

## remake-superior.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/03-superior.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Older stern commander age45 short black greying hair dark navy cape silver armor with square gold collar, arrives holding stamped order sheet. Rook listens.
Exact layout, camera and mechanics: Upper geography commander arrives from intact exit with stamped order paper, Rook foreground listens, evacuees protected BEHIND Mira. Lower full-width stern commander face delivers exact order in RIGHT 囚人を / LEFT 再収容しろ。 glyph80-90px. Commander45 BLACK hair with grey temples short BLACK beard navy cape squared gold silver armor, NEVER silver-haired young Rook. His hands hold order, sword not raised.
Exact speech in chronological order: [{"speaker": "Commander", "text": "囚人を再収容しろ。", "columns": ["囚人を", "再収容しろ。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["コツ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-princess-refuses.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/04-princess-refuses.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. Commander is the SAME mature 45-year-old dark-haired man with GREY TEMPLES and a short BLACK BEARD, navy cape and engraved silver/gold armor. Change ONLY his side profile foreground hair/face to this, never silver-haired young Rook. Mira speaks 王女の名で、拒みます。 in giant vertical text. Noa orange hair. Keep single panel.
```

## remake-e07-suspension.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/v6-suspension.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. Keep top and bottom speech panels exact あなたの権限は、 then 停止された。 Swap the two middle images so RIGHT side FIRST shows mature bearded Commander's black glove breaking royal seal chain with ONE パキッ; LEFT side SECOND shows Mira's shocked blue eyes. This cause-before-reaction reading order is mandatory. No new text.
```

## remake-collapse-cue.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/06-collapse-cue.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Grey security guardian purple core advances from damaged rail, cracks under commander boots spread into corridor, no people falling yet. Only effect ミシッ .
Exact layout, camera and mechanics: Upper shallow guardian stone foot PURPLE core approaches damaged rail to corridor. Lower wide crack starts beneath commander ordinary silver boots along floor toward empty corridor edge. People still stand safely, no falling bodies yet. EXACT ONE ミシッ at crack, pause before next collapse. Show safe exit corridor at far end.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ミシッ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-collapse.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/07-collapse.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Corridor floor breaks under commander and residents at near edge, guardian arm smashing beam; Rook turns toward trapped elderly man white hair navy vest among17, Mira keeps girl away. Clear safe exit above.
Exact layout, camera and mechanics: Upper diagonal panel guardian stone arm hits ONE support beam, crack crosses floor. Lower large tilted wide geography SAME floor section falls beneath commander's near edge and residents, intact escape exit ABOVE/behind Rook clearly visible. Rook turns to SAME white-haired older evacuee NAVY vest (not earlier brown-vest workshop survivor), Mira holds yellow girl back, Noa nearby. ONE ガラッ at broken floor, no rescue completed yet, no ambiguous floating feet.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ガラッ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-discard-order.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/08-discard-order.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close Rook drops stamped order sheet from black glove; other hand grips real rescue shield. Fallen sheet not sword, no new permit here.
Exact layout, camera and mechanics: SHORT horizontal row RIGHT Rook black glove OPENS releasing single STAMPED order paper / LEFT that SAME paper falls while his OTHER black glove grips steel rescue shield strap. One sheet only; sword safely sheathed. No replacement badge or new royal permit. ONE パサッ at falling paper.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["パサッ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-e07-shield.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/v6-shield.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rook silver armor and blue cape raises steel shield over evacuees to catch rubble, leads them toward intact exit.
Exact layout, camera and mechanics: Upper large Rook silver-gold armor BLUE cape puts STEEL shield between falling rubble and residents. Jagged exact こっちへ！ split2cols and tail to Rook mouth. Middle horizontal row RIGHT shield catches ONE stone クンッ? use specified ガンッ only / LEFT same yellow girl ducks near Mira. Lower wide Rook leads all survivors under shield toward INTACT exit, exact 頭を下げろ！ two largecols. Ren not holding shield, no duplicate Rook.
Exact speech in chronological order: [{"speaker": "Rook", "text": "こっちへ！", "type": "speech"}, {"speaker": "Rook", "text": "頭を下げろ！", "type": "speech"}]
Exact effects (each once, near physical cause): ["ガンッ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-ren-holds.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/10-ren-holds.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. Keep TOP cloth chest's tiny cyan star. SWAP middle panels: RIGHT FIRST bare hand with cyan light lattice forming; LEFT SECOND black/cyan plates attaching with ONE カチッ. Bottom Ren in BASIC black/cyan armor, red scarf, face uncovered, BOTH hands brace the SAME guardian wrist against a stone wall. BOTH boots must rest firmly on a BROAD FLAT intact stone floor. No raised foot, narrow ledge or ungrounded bracing. No speech.
```

## remake-rook-carries.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/11-rook-carries.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rook carries same elderly evacuee white hair navy vest on back up clear corridor, Mira leads girl, Noa guides Haru. Supports body safely.
Exact layout, camera and mechanics: Upper large Rook carries SAME white-haired older man NAVY vest safely on BACK uphill through clear exit, Rook steel shield stowed, silver armor/cape supports old man's legs. Exact speech そっちは任せる。 split RIGHT そっちは / LEFT 任せる。 glyph80-90px. Lower horizontal row RIGHT Mira leads YELLOW girl / LEFT Noa ORANGE gloves guides adult Haru brown hair GREEN shirt. Ren OFFSCREEN restrains guardian; do NOT insert Ren walking beside them.
Exact speech in chronological order: [{"speaker": "Rook", "text": "そっちは任せる。", "columns": ["そっちは", "任せる。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["タッ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-ren-answer.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/12-ren-answer.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren looks over shoulder toward escaping Rook while maintaining guardian wrist restraint, exhausted but trusting.
Exact layout, camera and mechanics: One large strong frame Ren BASIC black armor cyan seams/weak star/red scarf turns BLUE eyes over shoulder toward escaping Rook while BOTH armored hands stay gripping SAME guardian wrist against wall and BOTH feet remain planted on same intact floor. Exact 任せた。 big calm oval tail to Ren mouth, no detached extra hand, no released load.
Exact speech in chronological order: [{"speaker": "Ren", "text": "任せた。", "columns": ["任せた。"], "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-escape.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/13-escape.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. Delete the invented bottom speech balloon entirely and reconstruct unobscured artwork. There is NO dialogue in this scene. Keep top Rook settling the same white-haired NAVY-VEST elderly man onto a wooden bench, ONE コト… at contact; bottom RIGHT unarmored Ren / LEFT Rook silently confirming safety. Ren black short sleeve, red scarf and bare hands; Noa orange; yellow-dress girl; Haru olive workshirt.
```

## remake-e07-apology.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/v6-apology.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rook bends head to seated Ren without theatrical kneeling; hands empty, remorse face. Survivors in safe yard.
Exact layout, camera and mechanics: Upper Rook bows HEAD only toward seated tired unarmored Ren, exact 見ないふりをした。 large3cols 見ない / ふりを / した。 . Middle horizontal row RIGHT Rook EMPTY black gloves / LEFT survivors resting safe yard. Lower Rook remorse face exact 謝って終わらせない。 split RIGHT 謝って / MIDDLE 終わらせ / LEFT ない。 glyph80-90px. No theatrical kneeling, no instant restored princess power.
Exact speech in chronological order: [{"speaker": "Rook", "text": "見ないふりをした。", "type": "speech"}, {"speaker": "Rook", "text": "謝って終わらせない。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-return-license.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/15-return-license.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rook places his OWN silver knight license badge on rescue team's wooden table, takes plain rescue rope instead. Mira and Ren watch gesture, no restored royal authority.
Exact layout, camera and mechanics: Three genuine frames [1,2]/3: upper RIGHT Rook puts his OWN single silver knight BADGE on rescue team's wooden table with ONE コトッ / upper LEFT black glove reaches for PLAIN rescue rope instead. Lower medium Rook holds rope while Mira and Ren quietly observe concrete choice, no dialogue. Badge has abstract emblem only no invented words. Entry pass/royal seal not confused with badge.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["コトッ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-e07-accept-work.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/v6-accept-work.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren holds rope end toward Rook, mutual practical trust rather than instant friendship; Rook accepts.
Exact layout, camera and mechanics: Upper medium unarmored Ren offers ONE plain rope end toward Rook, exact じゃあ、次の人を一緒に。 three largecols じゃあ、 / 次の人を / 一緒に。 tailmouth. Lower horizontal row RIGHT Rook black glove accepts SAME offered rope / LEFT mutual eye contact with practical calm. Both characters ordinary rescue task, no additional armor for Ren/no instant celebratorycrowd.
Exact speech in chronological order: [{"speaker": "Ren", "text": "じゃあ、次の人を一緒に。", "type": "speech"}]
Exact effects (each once, near physical cause): ["ぎゅ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-invitation-cue.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/17-invitation-cue.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa intercepts discarded commander's communicator at desk, pulses of cyan light, Mira leans to read. No inviter identity yet.
Exact layout, camera and mechanics: Upper horizontal row RIGHT adult Noa orange glove catches discarded COMMANDER brass communicator at desk / LEFT tiny CYAN indicator pulse at same device. Lower wide Mira leans toward it and Ren looks up, invitation wording NOT visible yet, inviter face/identity hidden. ONE ピッ at device, no visible interface numbers.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ピッ"]
Exact visible prop text: []. No other text.

Lettering: NO ruled separator lines inside speech balloons. Actual Japanese upright glyph height80-90px at1024px width. Reading order within every row RIGHT side of canvas FIRST, LEFT side SECOND; mechanisms must show cause before result. Each effect exactly once. Ren supporting a load NEVER releases it until civilians safe.
```

## remake-invitation.png

built-in image_gen

参照：["examples/zero-break/episode-07/art/18-invitation.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit ONLY the attached comic. Preserve exact anime rendering, 1024 px width, framed panels and gutters, all canon text except any deletion explicitly requested below. Upright Japanese glyphs 80-90 px and clean unruled balloons. Preserve character identity and rescued civilians. Read each horizontal row RIGHT first then LEFT. No future transformations. Replace the ROUND compass/locket in BOTH panels with the SAME rectangular dark brass communicator seen in the preceding cue: rectangular bevelled brass case, black backing with gold fleur-de-lis and cyan indicator. TOP same rectangular device screen shows exactly 英雄認定場 on first horizontal line and レン様 on second. Bottom Ren BARE hands holding SAME rectangular device says exactly 俺を、待ってる？ in two giant upright vertical columns. No other text or name.
```
