# 第09話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：18素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-workshop-return.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/01-workshop-return.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels: top wide NIGHT warm workshop freed residents on cots, no armor; lower horizontal RIGHT Noa connects black crystal/silver-pedestal magic meter / LEFT Mira holds SAME amber brass memory crystal from trial. Rook without license guards door. Ren bare hands and ordinary black sleeves/red scarf throughout chapter.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rescue team back in warm workshop at night, freed residents rest on cots; Noa connects neutral magic meter near unarmored Ren, Mira holds trial memory crystal, Rook guards closed door.
Exact layout, camera and mechanics: EXACT 3 panels: top wide NIGHT warm workshop freed residents on cots, no armor; lower horizontal RIGHT Noa connects black crystal/silver-pedestal magic meter / LEFT Mira holds SAME amber brass memory crystal from trial. Rook without license guards door. Ren bare hands and ordinary black sleeves/red scarf throughout chapter.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["カチッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION — overrides conflicting original imagery:
Maintain EXACT 3 frames top establishing / bottom RIGHT then LEFT. Remove ALL black/cyan wrist braces: Ren has BOTH completely bare wrists and hands, black short sleeves, red scarf. The test instrument is the BLACK dark crystal on a SILVER pedestal, not a blue orb. Mira holds the SAME slender pointed AMBER crystal in a narrow brass base from Episode 8, never a fat faceted chunk. Establish cot with frail grey-bearded elder brown vest and brass bellows mask. Rook at door. No text.
```

## remake-zero-again.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/02-zero-again.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels: top RIGHT Ren BARE hand touches black crystal / LEFT same silver-pedestal physical plate shows exact big horizontal ０. Lower wide Ren and Noa take in still-zero reading at workshop bench. No black armor. SAME meter as Episode1.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close original black crystal-on-silver-pedestal meter from episode1 now at workshop bench shows exact big ０ on horizontal plaque. Ren bare hand on crystal, no armor.
Exact layout, camera and mechanics: EXACT 3 panels: top RIGHT Ren BARE hand touches black crystal / LEFT same silver-pedestal physical plate shows exact big horizontal ０. Lower wide Ren and Noa take in still-zero reading at workshop bench. No black armor. SAME meter as Episode1.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ピッ"]
Exact visible prop text: [{"text": "０", "type": "raster label", "review": "pending"}]. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-replay.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/03-replay.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels: top Noa replays recorded trace says exact line in two big vertical columns; middle RIGHT still-flat mechanical needle / LEFT physical recording shows cyan tiny chest rescue star while needle stays flat. Bottom Ren unarmored considers discrepancy. ONE カタ… at recorder, no invented readings.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa slowly replays paper/oscilloscope line: magic needle flat while cyan chest glow visible in recording. Gesture toward discrepancy, device design consistent.
Exact layout, camera and mechanics: EXACT 4 panels: top Noa replays recorded trace says exact line in two big vertical columns; middle RIGHT still-flat mechanical needle / LEFT physical recording shows cyan tiny chest rescue star while needle stays flat. Bottom Ren unarmored considers discrepancy. ONE カタ… at recorder, no invented readings.
Exact speech in chronological order: [{"speaker": "Noa", "text": "針は、動いてない。", "columns": ["針は、", "動いてない。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["カタ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e09-other-axis.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/v6-other-axis.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top Mira says 空じゃない。; middle RIGHT flat trace on PAPER with exact large horizontal 魔力 / LEFT rising rescue trace on PAPER with exact large horizontal 救助負荷 . Bottom Mira says 測る箱が違う。 in two large columns, Ren watching without instant mastery. TWO separate measurement axes not holographic HUD.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Mira draws TWO clear simple graph axes on paper, one flat, one rises during rescuing; exact large horizontal labels 魔力 and 救助負荷 . Ren leans in, not instantly master explanation.
Exact layout, camera and mechanics: EXACT 4 panels top Mira says 空じゃない。; middle RIGHT flat trace on PAPER with exact large horizontal 魔力 / LEFT rising rescue trace on PAPER with exact large horizontal 救助負荷 . Bottom Mira says 測る箱が違う。 in two large columns, Ren watching without instant mastery. TWO separate measurement axes not holographic HUD.
Exact speech in chronological order: [{"speaker": "Mira", "text": "空じゃない。", "type": "speech"}, {"speaker": "Mira", "text": "測る箱が違う。", "type": "speech"}]
Exact effects (each once, near physical cause): ["サラ…"]
Exact visible prop text: [{"text": "魔力", "type": "raster label", "review": "visually confirmed in generated image"}, {"text": "救助負荷", "type": "raster label", "review": "visually confirmed in generated image"}]. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-understand.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/05-understand.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels: top Ren ordinary black sleeves/red scarf touches faint CYAN star at cloth chest; lower RIGHT bare fingertips over cloth tiny star / LEFT Ren relieved says ゼロでも、ここにはある。 in THREE large vertical columns. No plates or gauntlets anywhere.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren touches bare chest over faint cyan core, eyes widen with slow relief, red scarf moved slightly but same outfit.
Exact layout, camera and mechanics: EXACT 3 panels: top Ren ordinary black sleeves/red scarf touches faint CYAN star at cloth chest; lower RIGHT bare fingertips over cloth tiny star / LEFT Ren relieved says ゼロでも、ここにはある。 in THREE large vertical columns. No plates or gauntlets anywhere.
Exact speech in chronological order: [{"speaker": "Ren", "text": "ゼロでも、ここにはある。", "columns": ["ゼロでも、", "ここには", "ある。"], "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-siege.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/06-siege.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels: top NIGHT outside workshop geography royal guards around door AND supply pillar; lower RIGHT boots stop at door / LEFT guard reaches SUPPLY lever. Quiet threatening ONEザッ. No attack inside yet, no new enemy identity.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Outside night alley, grey armored royal guards surround workshop main door and power pillar. Inside team not yet fighting, no graphic force.
Exact layout, camera and mechanics: EXACT 3 panels: top NIGHT outside workshop geography royal guards around door AND supply pillar; lower RIGHT boots stop at door / LEFT guard reaches SUPPLY lever. Quiet threatening ONEザッ. No attack inside yet, no new enemy identity.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ザッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-cut-power.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/07-cut-power.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 diagonal panels: top helmeted guard pulls street supply-fuse lever ONEガチャン; middle intact workshop lamp loses light; bottom SAME lamp dark, street cable disconnected physically. No cyan or patient recovery yet.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Guard lever cuts workshop supply cable at street fuse box, lanterns inside dim visible through window. Ordinary electrical sabotage, no future villain face.
Exact layout, camera and mechanics: EXACT 3 diagonal panels: top helmeted guard pulls street supply-fuse lever ONEガチャン; middle intact workshop lamp loses light; bottom SAME lamp dark, street cable disconnected physically. No cyan or patient recovery yet.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ガチャン"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e09-ventilator-stops.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/v6-ventilator-stops.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels: top grey-bearded BROWN VEST elderly man from Episode5 on cot, unchanged brass bellows connected to breathing mask; lower RIGHT bellows collapses/stops / LEFT Mira worried says 呼吸の装置が…！ TWO huge vertical columns jagged balloon. Patient distressed but alive. No armor, no recovered smile.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Inside simple medical alcove, OLD MAN brown vest grey beard saved in episode5 on cot uses brass bellows breathing assistance, motion slows; Mira notices distress, no death or gore.
Exact layout, camera and mechanics: EXACT 3 panels: top grey-bearded BROWN VEST elderly man from Episode5 on cot, unchanged brass bellows connected to breathing mask; lower RIGHT bellows collapses/stops / LEFT Mira worried says 呼吸の装置が…！ TWO huge vertical columns jagged balloon. Patient distressed but alive. No armor, no recovered smile.
Exact speech in chronological order: [{"speaker": "Mira", "text": "呼吸の装置が…！", "type": "speech"}]
Exact effects (each once, near physical cause): ["すぅ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-check-patient.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/09-check-patient.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels: top Ren bare hands checks SAME brown-vest elder wrist on cot; lower RIGHT closeup bare fingers at wrist/ shallow breath / LEFT Noa orange gloves takes isolated battery-sized CIRCUIT BOX from shelf. No immediate recovery. No powered city grid.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren unarmored kneels beside same elderly man with shallow breath, checks wrist while Noa pulls isolated test circuit box from shelf. No immediate success.
Exact layout, camera and mechanics: EXACT 3 panels: top Ren bare hands checks SAME brown-vest elder wrist on cot; lower RIGHT closeup bare fingers at wrist/ shallow breath / LEFT Noa orange gloves takes isolated battery-sized CIRCUIT BOX from shelf. No immediate recovery. No powered city grid.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e09-isolate-circuit.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/v6-isolate-circuit.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top Noa says 街の線とは、 in two huge cols; middle RIGHT Noa unplugs ventilator cable from city connector / LEFT connects SAME ventilator wire into isolated portable box, ONEカチッ. Bottom Noa says 切り離す。 in big upright lettering; Ren BARE hand on dedicated isolated terminal. City cable visibly abandoned separate. No full armor, no new Link form.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa connects ONLY isolated rescue-core circuit to ventilator, physical copper leads and safety switch visible; no connection to city main grid or new form. Ren keeps one bare hand on terminal.
Exact layout, camera and mechanics: EXACT 4 panels top Noa says 街の線とは、 in two huge cols; middle RIGHT Noa unplugs ventilator cable from city connector / LEFT connects SAME ventilator wire into isolated portable box, ONEカチッ. Bottom Noa says 切り離す。 in big upright lettering; Ren BARE hand on dedicated isolated terminal. City cable visibly abandoned separate. No full armor, no new Link form.
Exact speech in chronological order: [{"speaker": "Noa", "text": "街の線とは、", "type": "speech"}, {"speaker": "Noa", "text": "切り離す。", "type": "speech"}]
Exact effects (each once, near physical cause): ["カチッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION — overrides conflicting original imagery:
Rebuild EXACT 4 panels, rows [1],[2,3],[4], right-first. TOP Noa speaks vertical 「街の線とは、」 with unplug action imminent. MIDDLE RIGHT: orange gloved hand COMPLETELY unplugs the BLACK city cable from wall socket, ONE SFX「カチッ」. MIDDLE LEFT: that BLACK city plug lies visibly DISCONNECTED on floor by wall; a DIFFERENT RED ventilator lead is plugged into a self-contained RECTANGULAR BRASS BOX on cot-side table. BOTTOM: same disconnected BLACK plug visible apart from box and SAME RED isolated hose/cable exits box to elder's mask; Noa says vertical 「切り離す。」. Box has CYAN vertical glass indicator on FRONT and TWO FLAT COPPER CONTACT PADS ON TOP for Ren's palms. No handles, cranks or circular cylinders. Ren bare hands wait beside pads. Distinct cable colors, impossible to interpret city cable as reconnected. No power reaching elder yet.
```

## remake-give-power.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/11-give-power.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels: top cloth tiny cyan star/ Ren bare hands on dedicated circuit says 戦う力は、あとでいい。 in3 huge columns. Middle RIGHT faint energy through his bare fingers into copper terminal / LEFT same copper wire to brass bellows beginning smallest movement. Bottom wide Ren UNARMORED concentrates at same terminal beside elder, no completed recovery before breathing cue.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren concentrates faint CYAN energy from chest into isolated lead with BOTH arms UNARMORED, no full armor or attack. Bellows starts first small motion, he sacrifices combat output.
Exact layout, camera and mechanics: EXACT 4 panels: top cloth tiny cyan star/ Ren bare hands on dedicated circuit says 戦う力は、あとでいい。 in3 huge columns. Middle RIGHT faint energy through his bare fingers into copper terminal / LEFT same copper wire to brass bellows beginning smallest movement. Bottom wide Ren UNARMORED concentrates at same terminal beside elder, no completed recovery before breathing cue.
Exact speech in chronological order: [{"speaker": "Ren", "text": "戦う力は、あとでいい。", "columns": ["戦う力は、", "あとでいい。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["ジ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION — overrides conflicting original imagery:
Rebuild EXACT 4 frames [1],[2,3],[4]. SAME rectangular brass isolated box, cyan vertical FRONT glass and TWO FLAT COPPER PADS ON TOP; RED cable/hose to elder's brass bellows mask. City BLACK cable lies UNPLUGGED by wall. TOP Ren bare short-sleeve and red scarf says exactly 「戦う力は、あとでいい。」 in TWO or THREE huge upright vertical columns, palms approaching pads. RIGHT MIDDLE both completely BARE palms touch both COPPER pads, CYAN energy flows from hands to box, ONE SFX 「ジ…」. LEFT MIDDLE bellows FIRST begin to expand, elder face kept out of crop. BOTTOM wide Ren CONTINUOUSLY presses both pads, no crank, lever, handgrip, cylinder, armor or mechanical wrist brace. Mira observes, Noa orange gloves; elder on cot. Show rescue energy entering isolated device; no recovered elder face before later beat.
```

## remake-rook-guard.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/12-rook-guard.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 2 diagonal panels: top outside blows ONEガンッ hit SAME STEEL shield braced at workshop door; bottom Rook silver armor/blue cape/black gloves, sword sheathed, holds shut door. Through doorway glimpse Ren ordinary black sleeves BARE hands still on isolated terminal, NEVER detached. Rook has no knight badge.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rook silver armor blue cape holds steel shield against workshop door under guards' blows, protects exhausted unarmored Ren inside. No miraculous limitless power.
Exact layout, camera and mechanics: EXACT 2 diagonal panels: top outside blows ONEガンッ hit SAME STEEL shield braced at workshop door; bottom Rook silver armor/blue cape/black gloves, sword sheathed, holds shut door. Through doorway glimpse Ren ordinary black sleeves BARE hands still on isolated terminal, NEVER detached. Rook has no knight badge.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ガンッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-breath-cue.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/13-breath-cue.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 quiet panels: top brass bellows small expansion; middle RIGHT tiny cyan indicator pulse / LEFT copper isolated lead continuous to Ren BARE hand. Patient FACE OUTSIDE crop throughout. ONEフッ at bellows. Wait for clear breathing response next image.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close brass ventilator bellows expands and cyan indicator starts tiny pulse, patient face still outside crop. Wait for actual breathing response, no healthy smile shown yet.
Exact layout, camera and mechanics: EXACT 3 quiet panels: top brass bellows small expansion; middle RIGHT tiny cyan indicator pulse / LEFT copper isolated lead continuous to Ren BARE hand. Patient FACE OUTSIDE crop throughout. ONEフッ at bellows. Wait for clear breathing response next image.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["フッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION — overrides conflicting original imagery:
Rebuild EXACT 3 frames [1],[2,3]. SAME RECTANGULAR BRASS BOX with CYAN vertical FRONT glass and TWO FLAT COPPER PADS ON TOP. TOP Ren's BOTH BARE palms continuously press the two pads, CYAN energy into box, RED hose to frail elder's bellows mask. No crank, lever, handle or cylindrical device anywhere. Elder's face is HIDDEN by crop, no recovered eyes/expression. MIDDLE RIGHT cyan indicator cycles. MIDDLE LEFT bellows FIRST expand with ONE 「フッ」 near moving bellows. No dialogue. Keep night cot-side location and red scarf.
```

## remake-e09-breath-returns.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/v6-breath-returns.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top FIRST brown-vest grey-bearded elder chest lifts beneath blanket; middle RIGHT hand relaxes / LEFT mask breath clears; bottom Mira says 息が、戻った。 TWO huge cols, Ren visible cloth black sleeves at dedicated terminal STILL powering continuously. No new form.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST clear elderly man inhales, chest visibly lifts under blanket, hand relaxes; Mira relieved nearby, Ren remains at powered circuit.
Exact layout, camera and mechanics: EXACT 4 panels top FIRST brown-vest grey-bearded elder chest lifts beneath blanket; middle RIGHT hand relaxes / LEFT mask breath clears; bottom Mira says 息が、戻った。 TWO huge cols, Ren visible cloth black sleeves at dedicated terminal STILL powering continuously. No new form.
Exact speech in chronological order: [{"speaker": "Mira", "text": "息が、戻った。", "type": "speech"}]
Exact effects (each once, near physical cause): ["すう…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION — overrides conflicting original imagery:
Rebuild into EXACT FOUR frames with true white gutters [1],[2,3],[4], NOT a tall side-panel spanning earlier beats. TOP FIRST the same frail grey-bearded elder brown vest visibly takes a breath through brass bellows mask, chest lifts, ONE 「すう…」. MIDDLE RIGHT tense old fingers relax. MIDDLE LEFT first clearer recovered eyes above same mask. BOTTOM Mira says exactly 「息が、戻った。」 in huge TWO upright vertical columns. Ren in background CONTINUOUSLY powers SAME RECTANGULAR BRASS BOX: BOTH BARE palms flat on TWO COPPER PADS ON TOP, CYAN vertical FRONT glass indicator and RED hose to mask. No crank, lever, handle, armor or cylindrical machine. Black city lead remains disconnected. No miraculous instant recovery before inhalation.
```

## remake-small-line-r2.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/15-small-line.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top physical paper recorder draws SMALL rising cyan trace, no large number; lower RIGHT orange Noa glove points / LEFT Noa says ちゃんと、届いてる。 TWO huge upright columns. Night dim room patient breathing and Ren still on circuit if visible. ONEカリ… at paper roller.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Output paper recorder draws a small unmistakably rising cyan line, Noa points with oil stained orange glove, no huge numeric gain, no upgraded gadget.
Exact layout, camera and mechanics: EXACT 3 panels top physical paper recorder draws SMALL rising cyan trace, no large number; lower RIGHT orange Noa glove points / LEFT Noa says ちゃんと、届いてる。 TWO huge upright columns. Night dim room patient breathing and Ren still on circuit if visible. ONEカリ… at paper roller.
Exact speech in chronological order: [{"speaker": "Noa", "text": "ちゃんと、届いてる。", "columns": ["ちゃんと、", "届いてる。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["カリ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL CONTINUITY CORRECTION: Keep EXACT THREE panels [1],[2,3]. Top paper recorder draws ONE small rising cyan line with ONE カリ… near pen. Middle RIGHT Noa's ORANGE glove points at line, says exactly 「ちゃんと、届いてる。」 in TWO huge upright vertical columns with correct mouth tail. Middle LEFT Ren has completely BARE hands, BLACK short sleeves and RED scarf; BOTH PALMS continuously press TWO COPPER TOP CONTACT PADS of SAME isolated BRASS cot-side power box with CYAN VERTICAL FRONT glass. No hand on chin, no hand free, no walking off. Grey-haired grey-bearded frail elder in BROWN vest with same brass bellows mask and RED hose rests on cot behind. No black-haired replacement patient. No crank or handles or armor. This is still ongoing rescue power, not an idle discussion.
```

## remake-signal.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/16-signal.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top Noa orange gloved finger follows weak sensor trace, keeps patient isolated circuit intact; lower RIGHT faint remote transmission on SEPARATE receiver / LEFT fine route on PAPER city map with ENDPOINT HIDDEN below fold. ONEピ… at receiver. Not energy backfeeding city grid, no 王宮直下 label yet.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa sees a faint stray transmission travelling out of isolated sensor toward thin separate line on city map. Do not show location label yet.
Exact layout, camera and mechanics: EXACT 3 panels top Noa orange gloved finger follows weak sensor trace, keeps patient isolated circuit intact; lower RIGHT faint remote transmission on SEPARATE receiver / LEFT fine route on PAPER city map with ENDPOINT HIDDEN below fold. ONEピ… at receiver. Not energy backfeeding city grid, no 王宮直下 label yet.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ピ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION — overrides conflicting original imagery:
Rebuild EXACT THREE frames [1],[2,3], no repeated redundant map frames. TOP Noa alone listens to a SEPARATE SMALL ROUND BRASS RADIO RECEIVER with short antenna; disconnected city cable MUST remain disconnected and no connection between radio and ventilator. MIDDLE RIGHT receiver makes ONE 「ピ…」. MIDDLE LEFT Noa orange glove reaches folded map; destination and palace labels completely HIDDEN. Ren is OFFSCREEN and CONTINUES powering ventilator offscreen, so never depict Ren free hands or walking away. Night workshop, warm candle light.
```

## remake-under-palace.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/17-under-palace.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top physical map unfolds ONEバサッ; middle RIGHT Mira fingertip on route / LEFT FIRST destination beneath WHITE palace towers exact big HORIZONTAL 王宮直下 on paper. Clear underground route ends beneath palace, no new villain/torture images.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST reveal city map route goes into chamber DIRECTLY beneath royal palace white towers; map exact large label 王宮直下 . Mira traces destination, no fuel torture depiction.
Exact layout, camera and mechanics: EXACT 3 panels top physical map unfolds ONEバサッ; middle RIGHT Mira fingertip on route / LEFT FIRST destination beneath WHITE palace towers exact big HORIZONTAL 王宮直下 on paper. Clear underground route ends beneath palace, no new villain/torture images.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["バサッ"]
Exact visible prop text: [{"text": "王宮直下", "type": "raster label", "review": "pending"}]. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION — overrides conflicting original imagery:
Rebuild EXACT THREE frames [1],[2,3], right-first. TOP Mira and Noa unfold paper map, ONE 「バサッ」. Ren is OFFSCREEN CONTINUOUSLY powering ventilator, so remove Ren unfolding map. MIDDLE RIGHT Mira points to route before destination label. MIDDLE LEFT FIRST reveals label exactly 「王宮直下」 in large readable physical HORIZONTAL Japanese on same map, red route terminates beneath palace. No dialogue. No extra text or additional destination labels. Night workshop.
```

## remake-e09-location.png

built-in image_gen

参照：["examples/zero-break/episode-09/art/v6-location.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top Mira says ここが、; middle RIGHT paper city map 王宮直下 physical route / LEFT Noa studies it; bottom Mira says 消えた街区の行き先。 THREE huge vertical columns. Ren black short-sleeved shirt/red scarf BARE hands STILL at isolated terminal beside breathing elder; Rook stays at door. No armor/no unplugged Ren.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Mira holds traced map while Ren still powers ventilator, eyes resolved. Rook keeps protective door, Noa watches line.
Exact layout, camera and mechanics: EXACT 4 panels top Mira says ここが、; middle RIGHT paper city map 王宮直下 physical route / LEFT Noa studies it; bottom Mira says 消えた街区の行き先。 THREE huge vertical columns. Ren black short-sleeved shirt/red scarf BARE hands STILL at isolated terminal beside breathing elder; Rook stays at door. No armor/no unplugged Ren.
Exact speech in chronological order: [{"speaker": "Mira", "text": "ここが、", "type": "speech"}, {"speaker": "Mira", "text": "消えた街区の行き先。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: [{"text": "王宮直下", "type": "raster label", "review": "visually confirmed in generated image"}]. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```
