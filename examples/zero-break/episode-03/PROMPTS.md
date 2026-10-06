# 第03話 — 採用原画の実行指示

採用原画の実行指示と参照ハッシュを generation-log.json に記録。以前の公開版・実行記録は Git の履歴で管理。

今回のWebtoonスキルによる再作画：18素材。大小・横並び・斜め枠・動作音・人物と小道具の連続性を原画ごとに再設計。実行指示と参照ハッシュは production/webtoon-remake/records。

## remake-morning.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-morning-before-correction.png"]

採用時の指示：

```text
Edit this existing Zero Break morning Webtoon strip. Remove the entire bottom panel that shows Ren and Mira meeting the rescued mother and boy: that reunion occurs later after the accident and MUST NOT appear here. Keep the top market geography panel with Ren, Mira and Rook, and below it ONE horizontal row read RIGHT to LEFT: Rook at right, Ren and Mira eating bread at center, the bread hand at left. End after that row with clean white bottom margin. Exactly 4 total panels. Preserve same characters, clothing and gentle morning light; Ren has ordinary short black shirt, bare hands and red scarf, no armor. Keep one サク… near the bread, remove any other text. Actually redraw the shortened strip composition, do not leave a blank bottom panel. Preserve the existing fine manga art and large upright Japanese lettering; no HTML overlays.
```

## remake-e03-challenge-r2.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/remake-e03-challenge.png"]

採用時の指示：

```text
Edit this existing Webtoon strip specifically for 360px PHONE reading: the current dialogue is too small. Preserve every panel frame, action, anatomy, prop, and character identity, and all quiet/action sounds exactly once as now. Reflow ONLY the following exact dialogue into larger balloon(s), actual upright Japanese glyph height 75-85px at1024px output width; font weight clear and dark, roomy3columns as specified. Increase white balloon area by using background space; do not cover eyes, hands, or key props. It is okay to expand the speech panel vertically to preserve art and large type. FULL EXACT wording, no missing or added syllables, punctuation correct: 私に勝てば免許をやる。 / upright vertical RIGHT column 私に勝てば / LEFT column 免許をやる。 ; Rook speaks, calm oval tail reaches his mouth. Same total number of panels. Unarmored Ren ordinary soft black shirt, red scarf, BARE hands, no new events or extra family members. No tiny text or caption labels, no HTML overlays.
```

## remake-fist.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/03-fist.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Close Ren's bare fist clenches, black shirt sleeve and red scarf, chest totally dark; attempting armor for competition and failing.
Exact layout, camera and mechanics: One short horizontal row RIGHT Ren BARE fist clenches / LEFT unchanged soft black shirt chest. No cyan glow, plates or system window anywhere. Empty power response is the point.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ギュ…"]
Exact visible prop text: []. No other text.

Episode3 continuity: the same rescued mother has brown hair, brown shawl over white blouse (hood may be lowered in morning); same young boy has dark brown hair and olive-green shirt. Noa is not present in this episode; do not keep an orange-haired background child from earlier draft. Barrel stays same intact wood/barrel metal hoops from failure through stopping.

```

## remake-e03-no-answer-r2.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/remake-e03-no-answer.png"]

採用時の指示：

```text
Edit this existing Webtoon strip specifically for 360px PHONE reading: the current dialogue is too small. Preserve every panel frame, action, anatomy, prop, and character identity, and all quiet/action sounds exactly once as now. Reflow ONLY the following exact dialogue into larger balloon(s), actual upright Japanese glyph height 75-85px at1024px output width; font weight clear and dark, roomy3columns as specified. Increase white balloon area by using background space; do not cover eyes, hands, or key props. It is okay to expand the speech panel vertically to preserve art and large type. FULL EXACT wording, no missing or added syllables, punctuation correct: さっきの力、もう消えたのか。 / RIGHT さっきの / CENTER 力、もう / LEFT 消えたのか。 ; Ren THINKS, cloud contour and thought dots to temple, no speech tail. Same total number of panels. Unarmored Ren ordinary soft black shirt, red scarf, BARE hands, no new events or extra family members. No tiny text or caption labels, no HTML overlays.
```

## remake-laughter.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-laughter-before-correction.png"]

採用時の指示：

```text
Edit this two-panel Webtoon image only to correct the repeated sound effect. Keep the RIGHT panel of two snickering adult bystanders and LEFT panel of Ren reacting, same art, clothing and horizontal right-to-left reading. Keep exactly ONE クス… beside the male bystander on the far right. Remove the second クス… beside the female bystander and restore the plain background beneath that removed text. No extra text, no dialogue, no new panel or people. Ren remains unarmored with bare hands.
```

## remake-practice.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/06-practice.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Rook makes one slow practice sword approach toward Ren's bare hand in training area; Ren steps back safely, no armor, not a wound or real fatal attack.
Exact layout, camera and mechanics: One wide diagonal framed action: Rook makes ONE slow controlled blunt sword approach, ordinary-shirt Ren retreats one safe step. Sword remains away from skin; no cut or armor. Rook's exact line large with tail to his mouth.
Exact speech in chronological order: [{"speaker": "Rook", "text": "その程度か。", "columns": ["その程度か。"], "type": "speech"}]
Exact effects (each once, near physical cause): ["ヒュッ"]
Exact visible prop text: []. No other text.

Episode3 continuity: the same rescued mother has brown hair, brown shawl over white blouse (hood may be lowered in morning); same young boy has dark brown hair and olive-green shirt. Noa is not present in this episode; do not keep an orange-haired background child from earlier draft. Barrel stays same intact wood/barrel metal hoops from failure through stopping.

```

## remake-axle.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-axle-before-correction.png"]

採用時の指示：

```text
Edit this existing two-panel diagonal Webtoon strip only to fix duplicate sound effects. Keep exactly ONE バキッ adjacent to the cracking wooden cart axle in the upper panel. Remove the second バキッ from the lower panel and restore that region's art/background. Preserve both panel frames, the same damaged axle and loaded intact wooden barrel with metal hoops, Ren and Mira by the cart, the distant dark-haired olive-green-shirt boy on the stairs. The barrel has NOT rolled downhill yet. No other text, no armored Ren, no extra event.
```

## remake-barrel.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/08-barrel.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Large barrel rolls down sloped white market steps toward SAME small boy green shirt from prior rescue, mother reaches from side too far. Show actual barrel, child and Ren distance. No impact yet.
Exact layout, camera and mechanics: Large tall geographic scene: SAME intact barrel rolls DOWN sloped white market steps toward SAME small olive-green-shirt boy. Mother in brown shawl reaches from side too far, exact urgent warning in jagged balloon. Ren several steps away. No collision/rescue outcome yet.
Exact speech in chronological order: [{"speaker": "Mother", "text": "危ない！", "columns": ["危ない！"], "type": "speech"}]
Exact effects (each once, near physical cause): ["ゴロロ"]
Exact visible prop text: []. No other text.

Episode3 continuity: the same rescued mother has brown hair, brown shawl over white blouse (hood may be lowered in morning); same young boy has dark brown hair and olive-green shirt. Noa is not present in this episode; do not keep an orange-haired background child from earlier draft. Barrel stays same intact wood/barrel metal hoops from failure through stopping.

```

## remake-move.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/09-move.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren discards bread bag safely and runs toward child with bare hand extended, decisive urgency. No giant leap, no armor until protection moment.
Exact layout, camera and mechanics: Upper SHORT horizontal row RIGHT bare hand lets bread bag fall safely aside / LEFT ordinary boot pushes off stone. Lower large diagonal movement of ONE unarmored Ren running toward offscreen child. No armor or giant leap yet.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["タッ"]
Exact visible prop text: []. No other text.

Episode3 continuity: the same rescued mother has brown hair, brown shawl over white blouse (hood may be lowered in morning); same young boy has dark brown hair and olive-green shirt. Noa is not present in this episode; do not keep an orange-haired background child from earlier draft. Barrel stays same intact wood/barrel metal hoops from failure through stopping.

```

## remake-shield-arm.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-shield-arm-before-correction.png"]

採用時の指示：

```text
Redraw this strip as exactly THREE panels. Upper short horizontal row read RIGHT to LEFT: RIGHT a close-up of Ren's LEFT forearm STILL BARE with faint cyan lattice. LEFT the SAME left forearm black faceted basic armor plates lock into place with exactly one カチッ. Lower large panel: Ren kneels between the olive-green-shirt dark-haired young boy and approaching INTACT wooden barrel, now his LEFT forearm and glove are black-cyan armored, OTHER arm and hand BARE, torso ordinary SOFT black cloth with tiny faint cyan point, red scarf. His left armored palm faces the approaching barrel. The barrel is NOT touching him yet: a clear space remains between barrel and palm; no flying splinters, breaking barrel, sparks, or stopped motion yet. Boy entirely on safe side behind his arm. Same white-stone market steps, mother brown shawl white blouse, Mira/Rook distant. No extra speech or text. Large gutters, actual horizontal frame division. Retain detailed manga style.
```

## remake-stop.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-stop-before-correction.png"]

採用時の指示：

```text
Correct this SINGLE diagonal rescue panel. The wooden barrel MUST stay completely INTACT: continuous curved wooden staves and both metal hoops, resting against Ren's LEFT black-cyan armored forearm/palm. Remove ALL shattered wood, flying splinters, bursting debris, and explosion streaks. Ren braces to stop it on market steps, BOTH ORDINARY BROWN BOOTS firmly touch stair stone, torso ordinary soft black short sleeve shirt and red scarf, right arm/hand BARE. Dark-haired olive-green-shirt boy safely BEHIND left forearm, brown-haired mother brown shawl/white blouse reaches boy on same landing. Make physical contact readable, no punching. Exactly ONE ドン at contact, no other text. Keep same characters and richly detailed style, do not add extra panels or armor on torso.
```

## remake-realization.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/12-realization.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Ren looks at armored forearm in astonishment, Rook lowers practice sword safely in background; stopped barrel beside feet, child and mother together.
Exact layout, camera and mechanics: Large upper Ren startled face with exact spoken question. Lower horizontal row RIGHT his one armored forearm / LEFT Rook silently lowers blunt practice sword. Intact stopped barrel at feet, family already together on safe side. Other hand bare, torso cloth.
Exact speech in chronological order: [{"speaker": "Ren", "text": "勝つためには、動かない？", "columns": ["勝つためには、", "動かない？"], "type": "speech"}]
Exact effects (each once, near physical cause): []
Exact visible prop text: []. No other text.

Episode3 continuity: the same rescued mother has brown hair, brown shawl over white blouse (hood may be lowered in morning); same young boy has dark brown hair and olive-green shirt. Noa is not present in this episode; do not keep an orange-haired background child from earlier draft. Barrel stays same intact wood/barrel metal hoops from failure through stopping.

```

## remake-reunion.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-reunion-before-correction.png"]

採用時の指示：

```text
Correct the upper panel of this two-panel reunion strip: Ren's armor must dissolve from the SAME LEFT forearm that stopped the barrel, not his opposite right arm. To remove the wrong-limb confusion, remove BOTH Ren's currently visible left-edge body/right-arm and Rook's right-edge body from the upper panel. Restore plain market landing background behind them. Keep mother brown shawl/white blouse embracing olive-green-shirt dark-haired boy at center unchanged, exactly one ぎゅ…. At EXTREME RIGHT EDGE add ONLY Ren's LEFT forearm and LEFT hand extending from offscreen, black faceted armor dissolving into bare skin with small cyan fragments and exactly one シュゥ…. Ren body stays OUTSIDE frame so there is one unmistakable dissolving arm, no other armored limb and no Rook. Lower boy close-up and exact upright vertical ありがとう。 with tail to mouth stays unchanged. Exactly two panels, no added dialogue, no extra people, no threatening barrel.
```

## remake-e03-rule-r2.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/remake-e03-rule.png"]

採用時の指示：

```text
Edit this existing Webtoon strip specifically for 360px PHONE reading: the current dialogue is too small. Preserve every panel frame, action, anatomy, prop, and character identity, and all quiet/action sounds exactly once as now. Reflow ONLY the following exact dialogue into larger balloon(s), actual upright Japanese glyph height 75-85px at1024px output width; font weight clear and dark, roomy3columns as specified. Increase white balloon area by using background space; do not cover eyes, hands, or key props. It is okay to expand the speech panel vertically to preserve art and large type. FULL EXACT wording, no missing or added syllables, punctuation correct: Panel1 Mira speaks 助けるときだけ、 / RIGHT 助ける / CENTER とき / LEFT だけ、 ; panel3 Mira speaks 応えている。 / RIGHT 応えて / LEFT いる。 ; two calm ovals with tails reaching Mira mouth, no Ren speaking. Same total number of panels. Unarmored Ren ordinary soft black shirt, red scarf, BARE hands, no new events or extra family members. No tiny text or caption labels, no HTML overlays.
```

## remake-e03-permit-r2.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/remake-e03-permit.png"]

採用時の指示：

```text
Edit this existing Webtoon strip specifically for 360px PHONE reading: the current dialogue is too small. Preserve every panel frame, action, anatomy, prop, and character identity, and all quiet/action sounds exactly once as now. Reflow ONLY the following exact dialogue into larger balloon(s), actual upright Japanese glyph height 75-85px at1024px output width; font weight clear and dark, roomy3columns as specified. Increase white balloon area by using background space; do not cover eyes, hands, or key props. It is okay to expand the speech panel vertically to preserve art and large type. FULL EXACT wording, no missing or added syllables, punctuation correct: Panel2 Ren speaks じゃあ、勝つより先に助ける。 / RIGHT じゃあ、 / CENTER 勝つより / LEFT 先に助ける。 ; calm oval tail reaches Ren mouth. Same total number of panels. Unarmored Ren ordinary soft black shirt, red scarf, BARE hands, no new events or extra family members. No tiny text or caption labels, no HTML overlays.
```

## remake-mechanical-bird.png

built-in image_gen

参照：["examples/zero-break/episode-03/art/16-mechanical-bird.png", "skills/webtoon/references/zero-break/layout-sequence-390.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished full-colour Japanese smartphone Webtoon comic artwork WITH integrated Japanese balloons and sounds. Recompose this existing scene with the specified purposeful panel layout. Reference 1 is the EDIT TARGET for its story, exact characters, costumes and place; retain its plot meaning, not its old panel stack. Reference 2, if present, is a layout/lettering quality reference only, not characters or plot.
Polished Zero Break anime/cel shading. Ren19 black tousled hair/blue eyes/red scarf/ordinary BLACK short sleeves and narrow brown straps/charcoal trousers/bare hands unless BASIC black faceted armor with CYAN seams and cyan star is explicitly present. No helmet, new form, changed scarf colour or body duplication. Mira19 blonde braid/blue eyes/white-blue-gold dress. Rook22 short SILVER hair/blue eyes/silver engraved armor/BLUE cape/BLACK gloves. Place/time and handedness must connect. Do not preview later outcomes or later identities.
Japanese dialogue: exact supplied wording and punctuation, UPRIGHT vertical glyphs top-to-bottom, columns right-to-left. Clear bold manga gothic, actual glyph height ~68px on1024px width; do not shrink long lines; use 2-4 short columns and a larger speech panel as needed. Read horizontal rows RIGHT to LEFT then downward. Each speech tail points to the mouth, thought clouds have dots. Spoken lines never have thought dots. Sounds sit near the specified physical cause and leave faces, hands and dialogue clear. No dialogue duplication, labels, English, watermark or invented system readings. White gutters, variable camera distance and frame area; meaningful horizontal rows and diagonal panel borders, not a decorative montage. One person may reappear only in genuinely sequential separate panels. Preferred width1024, height2048-3072 depending on panel count; a single geography can be 1024x1536. Maintain the current colour palette and exact role of the scene.


Noa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.
IMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.

Existing moment and strict continuity: Small silver brass mechanical bird secretly watches FROM market roof, cyan camera lens aimed toward Ren far below. No enemy face or display text yet.
Exact layout, camera and mechanics: Upper short horizontal row RIGHT silver/brass mechanical bird camera lens rotates / LEFT market-roof claw brace. Lower wide roof-to-market view of ONE small bird watching distant tiny Ren. No monitor message or enemy face yet.
Exact speech in chronological order: []
Exact effects (each once, near physical cause): ["ウィン…"]
Exact visible prop text: []. No other text.

Episode3 continuity: the same rescued mother has brown hair, brown shawl over white blouse (hood may be lowered in morning); same young boy has dark brown hair and olive-green shirt. Noa is not present in this episode; do not keep an orange-haired background child from earlier draft. Barrel stays same intact wood/barrel metal hoops from failure through stopping.

```

## remake-monitor.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-monitor-before-correction.png"]

採用時の指示：

```text
Redraw this ONE-panel dark remote monitor reveal. Cyan translucent monitor records Ren's ORDINARY BLACK CLOTH shirt chest with ONE tiny cyan star point, brown narrow shoulder straps, red scarf edge; the recorded torso is soft fabric, NOT faceted armor, no armored chest. The only readable monitor text is exact LARGE HORIZONTAL 未登録救済核 centered below recorded shirt. All other UI uses simple unlabelled faint line graphs and geometric marks, NO small invented letters, numbers or paragraphs. Dark blue-black remote stone room, no people faces, no body silhouette, no name, no white hero armor. Keep quiet dramatic single frame and beautiful manga linework.
```

## remake-watcher.png

built-in image_gen

参照：["examples/zero-break/production/webtoon-remake/references/e03-watcher-before-correction.png"]

採用時の指示：

```text
Edit this single watcher frame. Keep ONLY black-gloved hand, dark gold-embroidered sleeve edge on desk, face entirely OUTSIDE frame, exact soft spoken vertical ようやく来たか。 in large upright 2 columns with tail pointing offscreen LEFT to unseen speaker. Exactly one コト… at hand. Replace the BRIGHT daylight palace/window/background with the same DARK BLUE-BLACK REMOTE STONE ROOM as preceding monitor; no sunlight, no bright sky. Beside hand cyan monitor EDGE only with unlabelled abstract thin diagrams, remove all tiny invented letters, paragraphs and symbols resembling text. No white armor, no name, no new panel or extra event. Preserve hand anatomy and high quality art.
```
