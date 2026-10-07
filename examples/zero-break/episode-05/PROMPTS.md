# 第05話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：18素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-empty-house.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/01-empty-house.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren Mira Noa enter low-ceiling LOWER-city house at dusk: steam rises from unattended soup bowl, empty chairs, no bodies or horror. Humble brick and brass pipes contrast royal white towers.
Exact layout, camera and mechanics: Upper wide geography of the THREE entering low-city brick house at dusk, single table and two empty chairs. Lower horizontal RIGHT warm soup steam close / LEFT empty chair still pushed out. Nobody captive visible, no vanished-body magic, no armor.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["こと…"]
Exact visible prop text: []. No other text.

```

## remake-shoes-r2.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/remake-shoes.png"]

採用時の指示：

```text
Edit only Noa's own foot in UPPER panel of this existing3-panel Webtoon. At upper panel's left-bottom, the black sock/bare toes are wrong: adult orange-haired Noa is wearing a CLOSED black WORK BOOT, show thick solid boot leather toe and sole, NO bare toes or separated toes. Preserve both distinct MUDDY brown friend's boots: Noa ORANGE gloves picks up one, its mate stays by door. Keep3 frames and exact ONE スッ effect, every hand pose, soup, doorway and lighting. No new text or extra shoes.
```

## remake-e05-not-moving.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-e05-not-moving-before-correction.png"]

採用時の指示：

```text
Preserve every panel, prop, action, character, word and sound in this Webtoon. PHONE requirement: actual upright Japanese glyph height 75-85px at1024px width, bold clean black, roomy white balloon. Expand speech panel/balloon vertically if needed; never cover eyes or active hands. Panel1 Noa exact 引っ越しなら、 split RIGHT 引っ越し / LEFT なら、 . Panel3 Noa exact 靴は持っていく。 split RIGHT 靴は / LEFT 持っていく。 . Calm oval tails reach Noa mouth. Keep the same boot, Noa orange gloves, Ren bare hands/soft black shirt/red scarf. Exactly3 stacked panels. No additional text.
```

## remake-ledger.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/04-ledger.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: At small local records counter, clerk's finger points to clean blank square on registry page; Mira places folded old map beside it, Noa still has boot. No tiny fabricated text.
Exact layout, camera and mechanics: One horizontal row RIGHT grey-cloaked clerk bare finger on clean BLANK registry square / LEFT Mira slides folded old map beside page. Noa holds same worker boot. Table fixed, no small fabricated letters.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["トン"]
Exact visible prop text: []. No other text.

```

## remake-e05-denial.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/v6-denial.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Middle-aged grey-cloaked clerk shakes head behind counter, Ren and Mira visible listening angry but controlled.
Exact layout, camera and mechanics: Upper close middle-aged clerk face and first/only dialogue, thin calm speech tail to mouth, text 3 upright columns. Lower wide Ren and Mira listening controlled, Noa boot edge. No threat, weapon, or secret villain reveal.
Exact speech in chronological order: [{"speaker": "Clerk", "text": "存在しない区画です。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

```

## remake-old-map.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-old-map-before-correction.png"]

採用時の指示：

```text
Preserve every panel, prop, action, character, word and sound in this Webtoon. PHONE requirement: actual upright Japanese glyph height 75-85px at1024px width, bold clean black, roomy white balloon. Expand speech panel/balloon vertically if needed; never cover eyes or active hands. Exactly4 panels1/[2,3]/4. Final Mira speech exact この家は、ここにあります。 split RIGHT この家は、 / MIDDLE ここに / LEFT あります。 . All physical old city map lines, blank erased ledger comparison and exactly one バサッ unchanged. Tail to Mira mouth. No new text.
```

## remake-entry.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-entry-before-correction.png"]

採用時の指示：

```text
Recompose this descent scene into exactly5 clearly ordered genuine frames at1024x1536: upper full-width geography of ONE Ren leading Mira and Noa DOWN the brass-pipe service stair with ONE lantern. Second row RIGHT Noa lantern close-up / LEFT Mira cautious face. Third full-width Ren face looking down. Fourth full-width ordinary Ren boot stepping DOWN with exactly ONE コツ… . Japanese reading top to bottom, within row RIGHT to LEFT. Clear white gutters; NO tall frame spanning multiple rows at side, no duplicate lanterns or extra people, captives still hidden. Preserve unarmored character clothing/identities and tunnel lighting. No dialogue/captions.
```

## remake-voice.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-voice-before-correction.png"]

採用時の指示：

```text
Preserve every panel, prop, action, character, word and sound in this Webtoon. PHONE requirement: actual upright Japanese glyph height 75-85px at1024px width, bold clean black, roomy white balloon. Expand speech panel/balloon vertically if needed; never cover eyes or active hands. Exactly3 frames1/[2,3]. Crucial speech speaker is an UNSEEN RESIDENT behind the CLOSED pipe-wall hatch, NOT Ren. Exact …出して。 as RIGHT … / LEFT 出して。 in a pale weak oval near the hatch. Thin wavering tail ends at the closed hatch seam or extends offscreen behind wall, never toward Ren's face/hand. Ren's mouth CLOSED; he pauses with BARE hand near hatch and listens. Keep lower RIGHT rattling seam with exactly ONE カタ… / LEFT Ren blue-eye reaction. No person/captive visible yet. Same lantern, Noa behind, no extra text.
```

## remake-captives.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/09-captives.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST reveal silhouettes of living residents moving inside translucent magical transport conduit behind brass protective window. Clear distressed humans, not liquid or gore, destination hidden. Ren Mira Noa foreground aghast.
Exact layout, camera and mechanics: FIRST reveal: upper wide protective brass window and translucent transport conduit, clear LIVING human silhouettes moving inside, no liquid or gore. Lower horizontal RIGHT Ren/Mira shocked faces / LEFT Noa lantern hand lowered. Directional movement through tube, destination and individual Haru face hidden.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ゴウン…"]
Exact visible prop text: []. No other text.

```

## remake-old-man.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-old-man-before-correction.png"]

採用時の指示：

```text
Preserve every panel, prop, action, character, word and sound in this Webtoon. PHONE requirement: actual upright Japanese glyph height 75-85px at1024px width, bold clean black, roomy white balloon. Expand speech panel/balloon vertically if needed; never cover eyes or active hands. Exactly2 diagonal stacked panels. Lower Ren speaks exact 聞こえますか。 split RIGHT 聞こえ / LEFT ますか。 ; tail reaches Ren mouth. Grey bearded elderly man brown vest breathes beside OPEN inspection hatch, exactly one はぁ… near man's breathing. Ren kneels and checks his shoulder, BARE hands, no armor. Keep all composition and clothing.
```

## remake-patrol.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/11-patrol.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: A small brass patrol drone searchlight sweeps toward tunnel fork; Noa spots it, elderly survivor foreground supported by Ren. No giant attack yet.
Exact layout, camera and mechanics: Upper narrow brass patrol drone searchlight sweeps through fork BEFORE protagonists hide. Lower diagonal large tunnel geography: Noa sees approaching light, Ren physically supports SAME elderly man, Mira stays behind pipes. Only one drone, no giant attack or combat armor.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ウィーン"]
Exact visible prop text: []. No other text.

```

## remake-choose.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/12-choose.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren looks from receding transport shadows to elderly man's shaky breathing, chooses to pick him up rather than chase.
Exact layout, camera and mechanics: Upper horizontal RIGHT receding shadows in transport conduit / LEFT frail old man's shaky breathing. Lower large Ren turns from tube to survivor and exact dialogue in 3 large upright columns, softly firm speech tail. Ren BARE hands begin safely lifting man, no future rescue montage.
Exact speech in chronological order: [{"speaker": "Ren", "text": "まず、この人を外へ。", "columns": ["まず、この人を", "外へ。"], "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

```

## remake-jam-signal.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-jam-signal-before-correction.png"]

採用時の指示：

```text
Edit ONLY panel placements in this existing6-panel Webtoon. Two horizontal rows are currently in wrong chronological order for Japanese RIGHT-to-LEFT reading. In the SECOND row place the pliers REMOVING the fuse and single カチッ in the RIGHT half of canvas; place Noa holding the already removed fuse in the LEFT half. In the THIRD row place SAME brass drone with searchlight ON in the RIGHT half; place SAME drone searchlight OFF in the LEFT half. Preserve upper wide Noa/Mira working on same relay and lower wide Mira copying abstract diagram. Keep6 frames, all art style, characters, fuse, no added words/sounds. Clear white gutters. No mirrored Japanese lettering: sound カチッ remains normal readable orientation exactly once.
```

## remake-escape.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-escape-before-correction.png"]

採用時の指示：

```text
Recompose exactly4 frames1/[2,3]/4: upper full-width dynamic Ren unarmored carrying SAME grey-bearded old man brown vest safely on his BACK uphill toward workshop, both bodies/heads visible, no duplicate Ren. Middle RIGHT blonde Mira follows holding copied paper / LEFT adult orange-haired Noa follows with ONE lantern. Lower full-width close of Ren ordinary boot firmly on NEXT HIGHER stair, exactly one タッ, clear ascending stair diagonal. No tall frame spanning side rows; clear white gutters in Japanese RIGHT-to-LEFT sequence. Preserve clothing, one old man, no speech/extra labels.
```

## remake-record.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-record-before-correction.png"]

採用時の指示：

```text
Edit only one duplicated sound in this existing3-panel Webtoon. Keep ONE サラ… next to Mira's pencil in UPPER full-width panel. REMOVE the duplicated サラ… in lower RIGHT close-up of Mira and restore workshop background there. Preserve exactly the same panel layout, every character and paper, the exact prop labels 十七人 and 明朝 in each occurrence, abstract row lines only, no new words/numbers. Unarmored Ren bare hands and recovering elderly man cot remain. Do not change any lettering except duplicated lower effect.
```

## remake-e05-vow.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e05-e05-vow-before-correction.png"]

採用時の指示：

```text
Preserve every panel, prop, action, character, word and sound in this Webtoon. PHONE requirement: actual upright Japanese glyph height 75-85px at1024px width, bold clean black, roomy white balloon. Expand speech panel/balloon vertically if needed; never cover eyes or active hands. Exactly4 frames1/[2,3]/4. IMPORTANT: silver-haired silver-armored Rook is NOT PRESENT in this chapter. Replace only that Rook in middle LEFT reaction frame with adult18 orange-haired Noa green eyes brass goggles ON HEAD blue overalls black shirt ORANGE gloves. Mira remains beside Noa. Upper Ren exact 全員を戻す。 split RIGHT 全員を / LEFT 戻す。 ; lower Ren exact そのために、場所を忘れない。 split RIGHT そのために、 / CENTER 場所を / LEFT 忘れない。 . Tails to Ren mouth. Ren soft black shirt/red scarf BARE hands calmly holds copied paper beside same elderly man's cot. Preserve map, warm workshop, no new events or sounds.
```

## remake-destination.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/17-destination.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: FIRST close reveal next morning delivery docket: exact horizontal large title 英雄認定場 and small bold count 十七人 . No enemy face. Mira fingertips hold document.
Exact layout, camera and mechanics: ONE full-width close document in Mira fingertips. FIRST destination reveal exactly horizontal 英雄認定場 large bold at top and 十七人 below; rest blank abstract ruled lines. No enemy face, no imperial secret caption.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ペラ…"]
Exact visible prop text: [{"text": "英雄認定場", "type": "prop", "orientation": "horizontal"}, {"text": "十七人", "type": "prop", "orientation": "horizontal"}]. No other text.

```

## remake-e05-friend-listed.png

built-in image_gen

参照：["examples/zero-break/episode-05/art/v6-friend-listed.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Noa's gloved finger stops on handwritten name ハル in simple list; Noa's green eyes widen, Ren beside grips scarf. Just one readable name, rest abstract lines.
Exact layout, camera and mechanics: Upper Noa face first exact line, green eyes widening. Middle horizontal RIGHT orange gloved finger stops on ONE handwritten ハル / LEFT Ren blue eye and bare hand grips red scarf. Lower Noa second exact line large, no smiling reunion or captive rescue yet. Other list entries abstract lines only.
Exact speech in chronological order: [{"speaker": "Noa", "text": "ハルも、", "type": "speech"}, {"speaker": "Noa", "text": "ここにいる。", "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: [{"text": "ハル", "type": "raster label", "review": "visually confirmed in generated image"}]. No other text.

```
