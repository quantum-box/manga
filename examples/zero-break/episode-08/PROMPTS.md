# 第08話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：18素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-corridor.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/01-corridor.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren unarmored red scarf, Mira white blue gold gown and Rook without license walk long white certification hall. Framing statues only calves and immense shadow, white hero head not visible yet.
Exact layout, camera and mechanics: Upper long white hall geography only statue CALVES at extreme edges and immense unknown shadow, NO head/torso/star reveal. Lower horizontal row RIGHT ordinary Ren boot walks with one コツ… / LEFT Mira and silver-haired Rook without knight badge look upward. Noa absent, stays at workshop. Team Ren ordinary soft blackshirt/red scarf/BARE hands. No text.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["コツ…"]
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-portrait.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/02-portrait.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST full huge WHITE armored ancient hero statue with GOLD chest star, no visible living face; small red-scarf Ren below looks up. Retain unknown name, no Arata caption.
Exact layout, camera and mechanics: One large FIRST reveal huge WHITE armored ancient hero STATUE with GOLD chest star, sculpted face featureless/shadowed as statue not living named man. Small unarmored red-scarf Ren at base looks up exact 誰だ、この人。 two large upright cols 誰だ、 / この人。 tailRenmouth, no Arata/name/origin caption. Gold star sharply contrasts ordinary Ren tinycyanpoint.
Exact speech in chronological order: [{"speaker": "Ren", "text": "誰だ、この人。", "columns": ["誰だ、", "この人。"], "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-e08-first-hero.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/v6-first-hero-gold.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Thin masked ceremony guide in grey formal robe points to white statue, neutral expression. Ren Mira listen.
Exact layout, camera and mechanics: Upper thin masked ceremony guide GREY formal robe points to same white ancient statue without living face. Middle horizontal row RIGHT guide pointing fingers / LEFT Ren/Mira listening eyes. Lower guide exact 初代勇者です。 split RIGHT 初代 / LEFT 勇者です。 actualglyph80-90px, calm oval tailguidemouth/under mask. Rook nearby noNoa, no name added.
Exact speech in chronological order: [{"speaker": "Guide", "text": "初代勇者です。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-e08-compare-star.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/v6-compare-star.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Mira looks from statue GOLD star to Ren's faint CYAN chest point visible at scarf shirt neckline. Close bodily clue, not equal color or new form.
Exact layout, camera and mechanics: Upper Mira face exact 星の形が、 two largecols 星の / 形が、 . Middle horizontal row RIGHT STATUE GOLD star shape / LEFT Ren SOFT black cloth neckline tiny CYAN star same shape but different color, NEVER black armor torso. Lower Mira exact 同じ…。 big upright, whispered oval tailmouth. No copying newpower/fullarmor/name/origin reveal.
Exact speech in chronological order: [{"speaker": "Mira", "text": "星の形が、", "type": "speech"}, {"speaker": "Mira", "text": "同じ…。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-trial-door.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/05-trial-door.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Guide opens iron trial door with one key, team waits behind; targets and prisoners hidden until next scene. No later evidence text yet.
Exact layout, camera and mechanics: Short horizontal row RIGHT guide inserts ONE iron key into lock / LEFT guide turns SAME key with ONE カチャ. Lower wide closed heavy IRON trial door begins opening narrow DARK slit, residents/targetplatforms still hidden completely. Ren/Mira/Rook wait behind, no magicaldetection/addedword.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["カチャ"]
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-human-targets.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/06-human-targets.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST trial hall reveal: living adult residents shackled upright on movable training target platforms; mechanical launchers aimed nearby. Graphic violence absent, ropes/chain clear, lives endangered. Ren shocked.
Exact layout, camera and mechanics: Upper large FIRST hall reveal: LIVING ADULT residents chained UPRIGHT to separate training-target platforms, mechanical launchers aim near them; no wounds/gore and no targets shaped as children. Middle horizontal row RIGHT chain attached wrist/rail / LEFT loaded physical launcher pointed towardplatform. Lower big Ren shocked BARE hands, exact 人を、的にするのか。 split RIGHT 人を、 / MIDDLE 的にする / LEFT のか。 actualglyph80-90px. No attack fired yet, no extra expositionalcaption.
Exact speech in chronological order: [{"speaker": "Ren", "text": "人を、的にするのか。", "columns": ["人を、", "的にするのか。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["ガタ…"]
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-e08-refuse.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/v6-refuse.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren turns away from offered ceremonial sword, opens empty hand toward captive adults; expression controlled outrage.
Exact layout, camera and mechanics: Upper horizontal row RIGHT offered ceremonial sword in guide's hand / LEFT Ren BARE hand opens AWAY from sword, refuses to take it. Lower large Ren controlled outrage looking toward captive adults exact こんな試験、受けない。 split RIGHT こんな / MIDDLE 試験、 / LEFT 受けない。 glyph80-90px mouthtail. No full armor, no violence, Mira/Rookprepareassist.
Exact speech in chronological order: [{"speaker": "Ren", "text": "こんな試験、受けない。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-disqualify.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/08-disqualify.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ceremony guide pulls bell rope and points to exit with judge gesture. Bell effect カン . No attack or ren armor yet.
Exact layout, camera and mechanics: Upper masked grey guide pulls ONE physical bell-rope with ONE カン at bell. Lower medium guide points toward EXIT exact 失格です。 two large upright cols 失格 / です。 ovaltailguide. Unarmored Ren in edge hears it without followingexit. No securityattack yet, no mandatorysworduse.
Exact speech in chronological order: [{"speaker": "Guide", "text": "失格です。", "columns": ["失格です。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["カン"]
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-turn-back.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/09-turn-back.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren turns his BACK to guide and walks toward captive adult's dangling chain, bare hand already reaching. Rook and Mira prepare to assist, no full armor.
Exact layout, camera and mechanics: Upper ordinary Ren turns BACK to guide and walks toward chain-bound adult, BARE hands/softblackshirt/red scarf. Lower horizontal row RIGHT bare reachinghand toward SAME dangling chain / LEFT resident frightened eye looking at Ren, not alreadyfreed. Mira/Rookprepare assistance near door, ONE タッ at boot. No fullarmor.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["タッ"]
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-cut-chain.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/10-cut-chain.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit the attached comic, preserving exact style, color and Japanese canon dialogue. All lettering raster integrated upright Japanese 80-90px at1024px; no separators inside balloons, no new dialogue, no watermark. True framed panels and gutters. Each horizontal row reads RIGHT first then LEFT. Rebuild as FOUR panels: TOP full-width Ren black short sleeve/red scarf BARE hands one on resident shoulder and left hand reaching chain, tiny CYAN light lattice starting on bare left arm; middle RIGHT bare light lattice detail then middle LEFT BLACK/CYAN plates assembling ONLY on LEFT forearm with ONE カチッ; BOTTOM Ren's LEFT armored hand breaks ONE chain link with ONE ガキン while RIGHT BARE hand steadies resident. No armor on torso/right hand/legs, no other prisoner freed yet, no other effects.
```

## remake-guards-run.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/11-guards-run.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Grey helmeted guards run from statue shadow toward freeing team; Rook raises shield at doorway, Mira guides freed residents behind him. Not an enemy victory image.
Exact layout, camera and mechanics: Upper long corridor grey helmeted guards RUN from statue shadow toward rescue team, ONE ダッ. Lower horizontal row RIGHT Rook black glove raises STEEL shield at narrowdoor / LEFT Mira guides first freed adult behind protective doorway. Ren offscreen stillbreakingremainingchains, his support not abandoned. No guardsdefeated/killed, no Noa.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ダッ"]
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-hold-exit.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/12-hold-exit.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit the attached comic, preserving exact style, color and Japanese canon dialogue. All lettering raster integrated upright Japanese 80-90px at1024px; no separators inside balloons, no new dialogue, no watermark. True framed panels and gutters. Each horizontal row reads RIGHT first then LEFT. Keep exact Rook speech この出口は、閉めさせない。 and ONE ガン at shield. Put Rook's sword COMPLETELY into its DARK SCABBARD at his waist, hilt visible, no exposed blade. Rook braces silver shield, face/silver hair/blue cape unchanged. Background Ren basic BLACK CLOTH short sleeves/red scarf; RIGHT hand BARE, LEFT forearm ONLY can retain black/cyan plates while opening another chain, NO black gloves on bare right hand, no torso armor. Keep one large panel.
```

## remake-copy-evidence.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/13-copy-evidence.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Mira copies trial recording via brass memory crystal at wall console. Exact large display text 記録保存 only; chamber and target silhouettes reflected. No huge futuristic HUD.
Exact layout, camera and mechanics: Exactly3 frames[1,2]/3: upper RIGHT Mira barefingers inserts ONE brass memorycrystal into samewallconsole slot / upper LEFT simplephysical console recordingdisplay changes to exact large HORIZONTAL 記録保存 ONLY, restblank/unlabelled. Lower larger Mira retrieves SAME crystal with TWO roomsreflection training platforms+chains, no giant futuristHUD and no English/numbers. ONE ピッ at displayconfirmation. Same teamcontinuesescaping.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ピッ"]
Exact visible prop text: [{"text": "記録保存", "kind": "prop"}]. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-e08-their-evidence.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/v6-their-evidence.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit the attached comic, preserving exact style, color and Japanese canon dialogue. All lettering raster integrated upright Japanese 80-90px at1024px; no separators inside balloons, no new dialogue, no watermark. True framed panels and gutters. Each horizontal row reads RIGHT first then LEFT. Replace EVERY purple diamond with the SAME long slender AMBER memory crystal taken from the console: transparent warm gold/amber elongated prism, brass base/holder, no purple/blue orb. Top RIGHT crystal / LEFT masked guide reaction; bottom Mira presents SAME amber crystal and says exactly あなたたちの証拠です。, freed residents behind Rook. Keep THREE panels and giant text.
```

## remake-rescue-outcome.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/15-rescue-outcome.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Freed adult resident reaches outside sunlight and touches wrist where chain was; Ren unarmored helps steady them, quiet relieved empathy, no crowd applause yet.
Exact layout, camera and mechanics: Upper wide freedADULT resident reachesoutsidesunlight, unarmoredRen BARE hand steadies shoulder and SAME old wristrestraintmarkclothednodamage. Lower horizontal row RIGHT hand touches freedwrist / LEFT adulttearsrelief exact …外だ。 largeupright2cols … / 外だ。 tailresidentmouth. Quiet empathy, NO applause/crowdcelebration orprematurenewenemyface.
Exact speech in chronological order: [{"speaker": "Resident", "text": "…外だ。", "columns": ["…外だ。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["ふぅ…"]
Exact visible prop text: []. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-old-inscription-cue.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/16-old-inscription-cue.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit the attached comic, preserving exact style, color and Japanese canon dialogue. All lettering raster integrated upright Japanese 80-90px at1024px; no separators inside balloons, no new dialogue, no watermark. True framed panels and gutters. Each horizontal row reads RIGHT first then LEFT. Change ONLY the purple/blue staff crystal in Mira's hands into the SAME slender AMBER memory crystal with a short brass base, handheld palm-sized elongated prism, not a staff or sword. Keep top Ren BARE fingers touching dusty still-hidden inscription, bottom RIGHT his sweeping hand ONE サッ then LEFT Mira holds SAME amber crystal. No readable inscription yet.
```

## remake-selection.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/17-selection.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST close exact carved inscription 救済は選別である on pale stone plinth, horizontal formal lettering large, no other words or speaker.
Exact layout, camera and mechanics: Single short close FIRST reveal EXACT carved horizontal words 救済は選別である on SAME pale stone plinth. Large darkdeepcutkanji, wholephrasefitsphonewidthreadably; ONLYthese9characters, noquote/caption/extraEnglish, no speaker. Sweptdustattopedge, solemnquietpause.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): []
Exact visible prop text: [{"text": "救済は選別である", "kind": "prop"}]. No other text.

Phone lettering override: NO ruled separator lines inside speech balloons. Actual upright Japanese glyph height 80-90px at 1024px width; use two or three columns with at most six glyphs per column, rightmost column read first. Every horizontal row reads the RIGHT panel before the LEFT panel. Each sound once at its source. Noa stays offscreen in her workshop for this chapter.
```

## remake-e08-reject-selection.png

built-in image_gen

参照：["examples/zero-break/episode-08/art/v6-reject-selection.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Edit the attached comic, preserving exact style, color and Japanese canon dialogue. All lettering raster integrated upright Japanese 80-90px at1024px; no separators inside balloons, no new dialogue, no watermark. True framed panels and gutters. Each horizontal row reads RIGHT first then LEFT. In TOP panel replace the smartphone/rectangular device in Mira's hands with the SAME long slender palm-sized AMBER memory crystal on a small brass base/holder, seen immediately previously. NO phone or screen. Keep Ren BARE black cloth/red scarf, the white marble/gold star statue, bottom Ren exact 誰が、そんなことを決めた。 huge three vertical columns. Keep two panels.
```
