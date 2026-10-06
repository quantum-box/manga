# 第10話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：20素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-festival.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/01-festival.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top wide DAY festival intact stone projection tower, audience and EMPTY stone plaza marked for later load landing; lower RIGHT Noa plugs SAME amber memory crystal into brass projector / LEFT Mira at podium and Ren BARE forearms cloth black sleeves/red scarf, Rook no knight badge. No tragedy yet.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Day festival plaza in sky city, white banners, audience faces expect celebration. Noa runs brass projector, Mira near podium, Ren unarmored red scarf nearby, Rook in plain duty armor without license. No tragedy yet. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 3 panels top wide DAY festival intact stone projection tower, audience and EMPTY stone plaza marked for later load landing; lower RIGHT Noa plugs SAME amber memory crystal into brass projector / LEFT Mira at podium and Ren BARE forearms cloth black sleeves/red scarf, Rook no knight badge. No tragedy yet.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["カチッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION overriding conflicting original image:
Keep EXACT THREE panels [1],[2,3], original day arena composition and EMPTY stone landing patch, tower still intact. MIDDLE RIGHT replace the fat amber lump with SAME SLENDER POINTED AMBER crystal held in its narrow BRASS BASE used by Mira in Episode 8; Noa's orange gloved hand inserts its BASE into brass projector socket, ONE カチッ. Never blue crystal. MIDDLE LEFT group watches. No new text. Preserve completely bare Ren and Rook.
```

## remake-e10-evidence.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/v6-evidence.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top Mira speaks 消された人には、 in3 large columns; middle RIGHT physical projector shows Episode5 TRANSPORT CONDUIT residents / LEFT same screen shows Episode8 adult people chained as targets, no new content. Bottom Mira says 名前があります。 in2 large cols, concerned citizens stop laughing. Ren still unarmored if present.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Projector beam FIRST shows silhouettes in transport conduit from episode5 and humans shackled as targets from8, recognizable records, no unreadable long caption. Audience laughter ends, concerned faces foreground. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 4 panels top Mira speaks 消された人には、 in3 large columns; middle RIGHT physical projector shows Episode5 TRANSPORT CONDUIT residents / LEFT same screen shows Episode8 adult people chained as targets, no new content. Bottom Mira says 名前があります。 in2 large cols, concerned citizens stop laughing. Ren still unarmored if present.
Exact speech in chronological order: [{"speaker": "Mira", "text": "消された人には、", "type": "speech"}, {"speaker": "Mira", "text": "名前があります。", "type": "speech"}]
Exact effects (each once, near physical cause): ["ざわ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-cut-switch.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/03-cut-switch.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top SAME MATURE45 Commander black-grey temples short black beard/navy cape silvergoldarmor yells 映像を止めろ！ two huge cols jagged mouth tail; lower RIGHT his gloved hand reaches projector switch / LEFT Noa orange gloves pulls SAME projector cable out of reach. No arrest yet, no silverhaired young substitute. Ren UNARMORED if visible.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Same older commander black greying hair navy cape from7 reaches projector power switch angrily; Noa keeps projection cable out of grasp. No arrest yet. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso. Match commander in episode7 scene03 EXACTLY: short black hair greying at temples, neatly trimmed BLACK beard and moustache, navy cape, ornate SILVER/GOLD armor. Same mature face, no younger silver-haired substitute.
Exact layout, camera and mechanics: EXACT 3 panels top SAME MATURE45 Commander black-grey temples short black beard/navy cape silvergoldarmor yells 映像を止めろ！ two huge cols jagged mouth tail; lower RIGHT his gloved hand reaches projector switch / LEFT Noa orange gloves pulls SAME projector cable out of reach. No arrest yet, no silverhaired young substitute. Ren UNARMORED if visible.
Exact speech in chronological order: [{"speaker": "Commander", "text": "映像を止めろ！", "columns": ["映像を", "止めろ！"], "type": "speech"}]
Exact effects (each once, near physical cause): ["バッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-giant-arrives.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/04-giant-arrives.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top guardian GREY STONE PURPLE core BEHIND stone projection tower, arm rises BEFORE hit; lower RIGHT stone foot ONEズン… / LEFT Ren still BLACK CLOTH bare arms turns hearing it, audience at base geography visible. No broken tower yet, no armor.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Concealment guardian GREY stone purple core approaches projection tower behind stage and raises arm. Audience at tower base, Ren turns at low rumble. No falling result yet. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 3 panels top guardian GREY STONE PURPLE core BEHIND stone projection tower, arm rises BEFORE hit; lower RIGHT stone foot ONEズン… / LEFT Ren still BLACK CLOTH bare arms turns hearing it, audience at base geography visible. No broken tower yet, no armor.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ズン…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-tower-hit.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/05-tower-hit.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 diagonal panels top guardian grey fist impacts STONE tower support ONEドゴン; middle SAME THICK STONE crossbeam bends/drops and projector fades; bottom Noa orange goggles safely ducks inside INTACT kiosk. ALL falling load stone, not metal train, wood, or steel beam. Ren if visible unarmored. No complete rescue.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Guardian fist smashes tower support, projection light falters, steel beam bends overhead; Noa drops under control booth safely. Only effect ドゴン . Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 3 diagonal panels top guardian grey fist impacts STONE tower support ONEドゴン; middle SAME THICK STONE crossbeam bends/drops and projector fades; bottom Noa orange goggles safely ducks inside INTACT kiosk. ALL falling load stone, not metal train, wood, or steel beam. Ren if visible unarmored. No complete rescue.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ドゴン"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-two-choices.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/06-two-choices.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top wide Ren between tower evidence crystal ABOVE and two trapped spectators BELOW FALL PATH same stone beam; middle RIGHT damaged memory projector / LEFT frightened Episode2 OLIVE GREEN shirt brown-haired8boy and BROWN shawl/white blouse mother. Bottom unarmored Ren eye/gaze moves downward to lives. No rescue yet. BOTH arms bare.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren unarmored between damaged tower's exposed memory projector ABOVE and startled spectators BELOW leaning fall path. His gaze moves down from evidence to lives, scene geographically clear. No rescue yet. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 4 panels top wide Ren between tower evidence crystal ABOVE and two trapped spectators BELOW FALL PATH same stone beam; middle RIGHT damaged memory projector / LEFT frightened Episode2 OLIVE GREEN shirt brown-haired8boy and BROWN shawl/white blouse mother. Bottom unarmored Ren eye/gaze moves downward to lives. No rescue yet. BOTH arms bare.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ミシ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e10-choice.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/v6-choice.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top unarmored Ren says 証拠は写せる。 two huge vertical cols; middle RIGHT bare hand grips red scarf / LEFT looks toward trapped boy+mother; bottom Ren says 人は戻せない。 two huge cols and starts ordinary boot toward them. NO armor plates yet. No copied hero.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close Ren grips red scarf and starts toward trapped spectators, blue eyes resolute, a real choice before full armor. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 4 panels top unarmored Ren says 証拠は写せる。 two huge vertical cols; middle RIGHT bare hand grips red scarf / LEFT looks toward trapped boy+mother; bottom Ren says 人は戻せない。 two huge cols and starts ordinary boot toward them. NO armor plates yet. No copied hero.
Exact speech in chronological order: [{"speaker": "Ren", "text": "証拠は写せる。", "type": "speech"}, {"speaker": "Ren", "text": "人は戻せない。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-run.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/08-run.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top ordinary boot pushes off towards falling stone beam ONEダッ; middle RIGHT bare arm cyan lattice / LEFT SAME arm black faceted BASIC plates lock ONEカチッ; bottom full Ren BASIC black/cyan armor, exposed face/redscarf runs toward spectators. No speed form until Episode12, no white/gold armor. Show real assembly BEFORE completed body.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren launches toward spectators as basic black armor/cyan seams forms in motion, scarf streak follows path; no new speed form before episode12. ONLY established BASIC BLACK faceted armor with thin CYAN seams and CYAN star forms; no new speed form, white armor, gold armor, helmet or face mask.
Exact layout, camera and mechanics: EXACT 4 panels top ordinary boot pushes off towards falling stone beam ONEダッ; middle RIGHT bare arm cyan lattice / LEFT SAME arm black faceted BASIC plates lock ONEカチッ; bottom full Ren BASIC black/cyan armor, exposed face/redscarf runs toward spectators. No speed form until Episode12, no white/gold armor. Show real assembly BEFORE completed body.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ダッ", "カチッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-catch-tower.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/09-catch-tower.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top FULL BASIC black-cyan Ren BOTH hands catch SAME thick STONE crossbeam ONEドン; lower RIGHT BOTH boots on broad intact STONE GROUND knees anchored / LEFT wide geography same beam overhead two crouched spectators, EMPTY stone ground adjacent for later lowering. BOTH armored hands stay overhead. No balancing on railing. Never release until all clear.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren BASIC complete black armor catches falling tower crossbeam over two crouching spectators and directs it away toward EMPTY stone patch. Clear hands support beam, legs braced, no random damage to people. Ren wears the established FULL BASIC BLACK faceted armor, thin CYAN seams, CYAN chest star, BOTH armored hands continuously supporting this SAME tower beam. Red scarf, exposed face and black hair. Both boots planted on broad intact STONE GROUND, knees braced, no balancing on railing. No teleporting between holds. The fallen load is the SAME thick STONE tower crossbeam as scene09, not an iron train or wooden beam.
Exact layout, camera and mechanics: EXACT 3 panels top FULL BASIC black-cyan Ren BOTH hands catch SAME thick STONE crossbeam ONEドン; lower RIGHT BOTH boots on broad intact STONE GROUND knees anchored / LEFT wide geography same beam overhead two crouched spectators, EMPTY stone ground adjacent for later lowering. BOTH armored hands stay overhead. No balancing on railing. Never release until all clear.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ドン"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e10-noa-copy.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/v6-noa-copy.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top Noa says 一つ消しても、 two huge cols; middle RIGHT orange gloved hand inserts COPIED SAME amber memory crystal into independent shop relay ONEカチッ / LEFT independent small screen lights same evidence. Bottom Noa says 終わらない。 largecols. Do NOT draw Ren anywhere; he is elsewhere continuously holding stone beam. No new Link network power.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa under intact kiosk plugs memory crystal duplicate into SMALL separate shop relay, old main tower abandoned. Orange hair/goggles/blue overalls, no future citywide link form. Do NOT draw Ren anywhere in this frame. He remains OFF CAMERA in full black-cyan basic armor continuously holding the fallen beam up until every spectator is clear. No duplicate hero helping Noa/Mira here.
Exact layout, camera and mechanics: EXACT 4 panels top Noa says 一つ消しても、 two huge cols; middle RIGHT orange gloved hand inserts COPIED SAME amber memory crystal into independent shop relay ONEカチッ / LEFT independent small screen lights same evidence. Bottom Noa says 終わらない。 largecols. Do NOT draw Ren anywhere; he is elsewhere continuously holding stone beam. No new Link network power.
Exact speech in chronological order: [{"speaker": "Noa", "text": "一つ消しても、", "type": "speech"}, {"speaker": "Noa", "text": "終わらない。", "type": "speech"}]
Exact effects (each once, near physical cause): ["カチッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION overriding conflicting original image:
Keep EXACT FOUR panels [1],[2,3],[4] right-first. Preserve dialogues exactly 「一つ消しても、」「終わらない。」 in HUGE upright vertical columns. Middle RIGHT orange gloved hand inserts SAME SLENDER POINTED AMBER crystal on NARROW BRASS BASE from Episode 8, never BLUE crystal or fat amber lump. ONE カチッ. Middle LEFT an independently powered screen shows the SAME prisoner evidence currently on festival tower, not a decorative crystal in church. Ren NEVER appears anywhere because he continuously supports the stone beam offscreen. Noa in intact brass kiosk, DAY sunlight outside, no night sky.
```

## remake-distributed.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/11-distributed.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. ONE continuous wide streetscape with THREE DIFFERENT small shop windows showing SAME transport evidence, independently powered ordinary screens, citizens watching. Can add lower horizontal RIGHT citizen stunned face / LEFT another neighbor screen, EXACT 3panels overall. ONEピッ at first screen. NO REN anywhere, he continues holding beam offscreen.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Three DIFFERENT small shop windows down street each show same transport silhouette evidence, everyday screens powered independently. One continuous streetscape, not repeated identical panels. Citizens watch stunned; no overlay words. Do NOT draw Ren anywhere in this frame. He remains OFF CAMERA in full black-cyan basic armor continuously holding the fallen beam up until every spectator is clear. No duplicate hero helping Noa/Mira here.
Exact layout, camera and mechanics: ONE continuous wide streetscape with THREE DIFFERENT small shop windows showing SAME transport evidence, independently powered ordinary screens, citizens watching. Can add lower horizontal RIGHT citizen stunned face / LEFT another neighbor screen, EXACT 3panels overall. ONEピッ at first screen. NO REN anywhere, he continues holding beam offscreen.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ピッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e10-name-them.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/v6-name-them.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top Mira brass street relay microphone and roster says 十七人です。 twohugecols; middle RIGHT SAME list handwritten names / LEFT citizens hear and look to concrete saved residents. Bottom Mira says 一人ずつ、ここにいます。 threehugecols. NO REN anywhere. No duplicate hero leaves stone beam.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Mira speaks into simple brass relay microphone from safe street, copied roster in hand. Exact short dialogue preserves human names over numbers. Do NOT draw Ren anywhere in this frame. He remains OFF CAMERA in full black-cyan basic armor continuously holding the fallen beam up until every spectator is clear. No duplicate hero helping Noa/Mira here.
Exact layout, camera and mechanics: EXACT 4 panels top Mira brass street relay microphone and roster says 十七人です。 twohugecols; middle RIGHT SAME list handwritten names / LEFT citizens hear and look to concrete saved residents. Bottom Mira says 一人ずつ、ここにいます。 threehugecols. NO REN anywhere. No duplicate hero leaves stone beam.
Exact speech in chronological order: [{"speaker": "Mira", "text": "十七人です。", "type": "speech"}, {"speaker": "Mira", "text": "一人ずつ、ここにいます。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-evacuation.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/13-evacuation.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 chronological panels: top wide FULL BASIC black/cyan armored Ren BOTH HANDS continuously holds SAME THICK STONE tower beam BOTH BOOTS anchored broad intact STONE ground. Last brownhaired BLUEeyed 8boy OLIVE GREEN shirt/BROWN breeches under load; Rook silverarmor bluecape blackgloves leads him towards mother BROWN hooded shawl/WHITE blouse OUTSIDE load path. Middle RIGHT boy boot crosses safety edge ONEタッ / LEFT SAME boy reaches SAME mother safe. Ren remains same anchored position. Show route not already-safe BEFORE crossing.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Spectators now walk OUT from under crossbeam along Mira-marked safe lane, Ren holds beam; Rook guides last small child green shirt to mother. Do not show final safe group before crossing. Ren wears the established FULL BASIC BLACK faceted armor, thin CYAN seams, CYAN chest star, BOTH armored hands continuously supporting this SAME tower beam. Red scarf, exposed face and black hair. Both boots planted on broad intact STONE GROUND, knees braced, no balancing on railing. No teleporting between holds. Rook guides the same family from episode2: 8-year-old brown-haired blue-eyed boy in OLIVE GREEN short-sleeve shirt and brown breeches, mother in BROWN hooded shawl and WHITE blouse. The boy crosses toward mother; both must end safely outside beam path. The fallen load is the SAME thick STONE tower crossbeam as scene09, not an iron train or wooden beam.
Exact layout, camera and mechanics: EXACT 3 chronological panels: top wide FULL BASIC black/cyan armored Ren BOTH HANDS continuously holds SAME THICK STONE tower beam BOTH BOOTS anchored broad intact STONE ground. Last brownhaired BLUEeyed 8boy OLIVE GREEN shirt/BROWN breeches under load; Rook silverarmor bluecape blackgloves leads him towards mother BROWN hooded shawl/WHITE blouse OUTSIDE load path. Middle RIGHT boy boot crosses safety edge ONEタッ / LEFT SAME boy reaches SAME mother safe. Ren remains same anchored position. Show route not already-safe BEFORE crossing.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["タッ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-set-beam.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/14-set-beam.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels AFTER ALL spectators safe: top wide LAST green shirt boy and brown shawl mother safely outside load path Rooknear; middle FULL BASIC black/cyan Ren guides SAME THICK STONE beam down with BOTH armored hands at low side, BOTH boots broad stoneground; bottom macro beam touches EMPTY stone plaza with ONEゴトン dust at actual STONEGROUND contact. No overhead load remains, no extra civilians beneath.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: After ALL spectators are outside the beam path, the SAME thick STONE tower crossbeam settles onto the EMPTY plaza ground with dust at visible stone-ground contact. Ren in fading BASIC BLACK-CYAN armor kneels beside it, both hands guiding its low side until the load rests. No overhead load remains.
Exact layout, camera and mechanics: EXACT 3 panels AFTER ALL spectators safe: top wide LAST green shirt boy and brown shawl mother safely outside load path Rooknear; middle FULL BASIC black/cyan Ren guides SAME THICK STONE beam down with BOTH armored hands at low side, BOTH boots broad stoneground; bottom macro beam touches EMPTY stone plaza with ONEゴトン dust at actual STONEGROUND contact. No overhead load remains, no extra civilians beneath.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ゴトン"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-first-clap.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/15-first-clap.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top SAME stone beam visibly rests on empty ground, Ren armor fades to ordinary black fabric shirt/BARE forearms as he leans on it; lower RIGHT Mira hands FIRST cautious clap ONEパチ / LEFT surrounding crowd silent hands DOWN. NO others clap until next image. No stone in air.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Mira gives the FIRST cautious clap beside the rescued audience while all others stare in silence. Ren unarmored leans on the safely lowered STONE beam. Only effect パチ. Applause spreads to the entire audience in the following scene.
Exact layout, camera and mechanics: EXACT 3 panels top SAME stone beam visibly rests on empty ground, Ren armor fades to ordinary black fabric shirt/BARE forearms as he leans on it; lower RIGHT Mira hands FIRST cautious clap ONEパチ / LEFT surrounding crowd silent hands DOWN. NO others clap until next image. No stone in air.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["パチ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.

FINAL MANDATORY CONTINUITY CORRECTION overriding conflicting original image:
Rebuild EXACT THREE frames [1],[2,3], right-first. TOP wide plaza after successful rescue: the SAME massive grey STONE beam now rests HORIZONTALLY DIRECTLY ON EMPTY GROUND along background, knee-height at most; it is NOT leaning overhead, elevated, balanced against tower, or resting on Ren. Ren stands entirely FREE of any load, black/cyan basic armor disappearing to bare black short sleeves and red scarf. Mira approaches, crowd's hands DOWN, SILENT. MIDDLE RIGHT close Mira's two hands perform FIRST single clap with exactly ONE パチ near contact. MIDDLE LEFT still-silent crowd, eyes soften but hands down; same boy about 8 olive shirt and mother brown shawl white blouse safe together. No duplicated パチ in establishing frame, no applause until next scene. No dialogue, no overhead load.
```

## remake-recognized.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/16-recognized.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top broad crowd now applauds facing Ren with saved brown shawl mother+green shirt boy foreground ONEパチパチ; lower RIGHT ordinary shirt Ren BARE hand to cloth chest / LEFT his surprised wet eyes exact thought …届いたんだ。 two huge upright cols CLOUD WITH DOTS. Mira Noa present, no boasting/armor.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Broad crowd now applauds rescued exhausted Ren, Mira and Noa beside him; Ren hand to chest with surprised wet eyes, not boastful. Show concrete saved families facing him. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 3 panels top broad crowd now applauds facing Ren with saved brown shawl mother+green shirt boy foreground ONEパチパチ; lower RIGHT ordinary shirt Ren BARE hand to cloth chest / LEFT his surprised wet eyes exact thought …届いたんだ。 two huge upright cols CLOUD WITH DOTS. Mira Noa present, no boasting/armor.
Exact speech in chronological order: [{"speaker": "Ren thought", "text": "…届いたんだ。", "columns": ["…届いたんだ。"], "type": "thought"}]
Exact effects (each once, near physical cause): ["パチパチ"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e10-arrest.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/v6-arrest.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top Rook silverhair silvergoldarmor/bluecape/blackgloves says 今度は、; middle RIGHT reaches SAME mature Commander's wrist / LEFT closes lawful METAL cuff ONEカチャン, commander blackgrey temples trimmed BLACK beard navycape alive uninjured. Bottom Rook says 見ないふりをしない。 THREEhugecols. No knight license, evidence+citizens witness. No revenge violence.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rook restrains commander's wrist with lawful metal cuffs beside copied evidence, commander alive uninjured. Rook carries no knight license; civil witnesses nearby, no revenge violence. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso. Match commander in episode7 scene03 EXACTLY: short black hair greying at temples, neatly trimmed BLACK beard and moustache, navy cape, ornate SILVER/GOLD armor. Same mature face, no younger silver-haired substitute.
Exact layout, camera and mechanics: EXACT 4 panels top Rook silverhair silvergoldarmor/bluecape/blackgloves says 今度は、; middle RIGHT reaches SAME mature Commander's wrist / LEFT closes lawful METAL cuff ONEカチャン, commander blackgrey temples trimmed BLACK beard navycape alive uninjured. Bottom Rook says 見ないふりをしない。 THREEhugecols. No knight license, evidence+citizens witness. No revenge violence.
Exact speech in chronological order: [{"speaker": "Rook", "text": "今度は、", "type": "speech"}, {"speaker": "Rook", "text": "見ないふりをしない。", "type": "speech"}]
Exact effects (each once, near physical cause): ["カチャン"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-base.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/18-base.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 panels top actual SAME handmade wooden sign exact big 救助隊 outside warm workshop; middle RIGHT Haru green workshirt and survivors repair doorway ONEカン / LEFT Ren BARE hands ordinary black shirt/redscarf shares bread with Mira Noa Rook at workbench. Quiet concrete achievement. No upgraded armor.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Lower-city workshop transformed into modest official rescue base with SAME handmade plaque 救助隊 . Ren Mira Noa Rook share bread at workbench; Haru and survivors outside help repairs. Clear warm first-arc achievement. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
Exact layout, camera and mechanics: EXACT 3 panels top actual SAME handmade wooden sign exact big 救助隊 outside warm workshop; middle RIGHT Haru green workshirt and survivors repair doorway ONEカン / LEFT Ren BARE hands ordinary black shirt/redscarf shares bread with Mira Noa Rook at workbench. Quiet concrete achievement. No upgraded armor.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["カン"]
Exact visible prop text: [{"text": "救助隊", "type": "raster label", "review": "pending"}]. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-white-armor-cue.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/19-white-armor-cue.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 3 quiet panels top palace shadows and white armored BOOTS, upper body outside crop; lower RIGHT GOLD star on back partially in wall reflection / LEFT ONLY back of LIVING ancient male hero short pale hair WHITE faceted armor. Face TOTALLY HIDDEN, no name. NO Ren Mira Rook Noa, NO redscarf, NO cyan star, NO living statue duplicate.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Deep palace shadow, LIVING ancient hero back turned: faceted WHITE armor and GOLD star partly reflected in wall, adult short pale hair obscured face. No exact identity or name yet; quiet ominous contrast to happy base. Draw ONLY the living ancient white armored hero seen FROM BEHIND and palace architecture. NO Ren, NO Mira, NO Rook, NO Noa, no red scarf, no cyan chest star. Short pale hair, WHITE faceted armor with a GOLD star on its back or reflection. FACE fully hidden; name not revealed. No duplicate living hero in front.
Exact layout, camera and mechanics: EXACT 3 quiet panels top palace shadows and white armored BOOTS, upper body outside crop; lower RIGHT GOLD star on back partially in wall reflection / LEFT ONLY back of LIVING ancient male hero short pale hair WHITE faceted armor. Face TOTALLY HIDDEN, no name. NO Ren Mira Rook Noa, NO redscarf, NO cyan star, NO living statue duplicate.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["コツ…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```

## remake-e10-close-gates.png

built-in image_gen

参照：["examples/zero-break/episode-10/art/v6-close-gates.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
MANDATORY FIRST: Completely recompose the supplied target into the EXACT separate framed panel sequence below. Its old composition is discarded; only characters, plot and setting are references. EXACT 4 panels top hidden-face ancient WHITE armored hero seen FROM BEHIND says ゼロを、 upright bigcols; middle RIGHT massive palace gate starts lowering ONEゴウン… / LEFT gate almost shut no protagonists trapped; bottom same white/gold backsilhouette HIGH ABOVE says 上げてはいけない。 THREEbigcols balloon tail toward unseen head/back silhouette, no thoughtdots. FACE remains hidden, no name, no redscarf or cyanstar.
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Massive palace gates all lowering toward shut stone, white armored silhouette far above, no protagonist trapped or killed. Ominous exact dialogue from unseen white hero. Draw ONLY the living ancient white armored hero seen FROM BEHIND and palace architecture. NO Ren, NO Mira, NO Rook, NO Noa, no red scarf, no cyan chest star. Short pale hair, WHITE faceted armor with a GOLD star on its back or reflection. FACE fully hidden; name not revealed. No duplicate living hero in front.
Exact layout, camera and mechanics: EXACT 4 panels top hidden-face ancient WHITE armored hero seen FROM BEHIND says ゼロを、 upright bigcols; middle RIGHT massive palace gate starts lowering ONEゴウン… / LEFT gate almost shut no protagonists trapped; bottom same white/gold backsilhouette HIGH ABOVE says 上げてはいけない。 THREEbigcols balloon tail toward unseen head/back silhouette, no thoughtdots. FACE remains hidden, no name, no redscarf or cyanstar.
Exact speech in chronological order: [{"speaker": "Unknown", "text": "ゼロを、", "type": "speech"}, {"speaker": "Unknown", "text": "上げてはいけない。", "type": "speech"}]
Exact effects (each once, near physical cause): ["ゴウン…"]
Exact visible prop text: []. No other text.

FINAL PHONE OVERRIDE: 80-90px ACTUAL Japanese glyph height on1024px width, 2-3 vertical upright columns max6glyph each. No ruled lines inside balloons. RIGHT panel first then LEFT. Each sound exactly once. All of Chapter9 is NIGHT except memory replay; keep every Ren arm UNARMORED in Chapter9. Ren in Chapter10 never releases the same stone beam until all spectators clear. Reference2 only frames/style. No added outcomes or dialogue.
```
