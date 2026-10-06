# 第02話 — 採用原画の実行指示

全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・旧版保持を generation-log.json で区別。以前の実行記録は production/feedback-v6/baseline に保持。

## 01-hunger.png

retained prior adopted image_gen output

参照：["../v5/art/14-hero.png", "../v5/art/16-relief.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime WEBTOON single comic moment. References establish Ren identity, Mira identity, armor design, and crisp detailed anime cel shaded style ONLY; do not copy their dialogue, pose, framing or panel layout. Adult Ren19: messy black hair, blue eyes, crimson scarf. He CURRENTLY wears complete faceted BLACK armor with thin cyan seams and a cyan star on chest, like reference1; the cyan is WEAK now, never purple. Scene: immediately after the first guardian fight, ruined white floating-city plaza in sunshine, giant broken stone fragments behind him. ONE short close shot of Ren from head to waist, hand on stomach, cheeks embarrassed, shoulders tired. His stomach growls. Mira is not in this crop yet. Do NOT show armor disappearing, invoices, new danger or future rescue. Compose wide 1024x768 with thin smooth black comic border, no giant unused margins. Render exact Japanese sound effect once near stomach, outside a balloon: ぐう… . Glyphs upright Japanese, expressive manga lettering, legible at360px; no speech balloons, narration, labels, English or other text. Preserve beautiful expressive anime face and red scarf, anatomically correct five-finger hand on stomach. Fully colored finished art, white-blue daylight background.
```

## 02-untransform.png

retained prior adopted image_gen output

参照：["../v5/art/14-hero.png", "../v5/art/a14-rejection.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Close bare Ren hand emerging as black arm armor flakes into tiny blue light; red scarf remains, black short sleeve shirt underneath. Exhaustion, no new danger.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## v6-support.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-02/art/03-support.png", "sha256": "52014ef3db1dd0df8202139e76af7b3eeea84d46647333c4170fd6e2430af059"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Unarmored Ren sways; Mira steps beside him and supports his shoulder with one hand, smiling gently among rubble. This is the first support touch.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Unarmored Ren sways; Mira steps beside him and supports his shoulder with one hand, smiling gently among rubble. This is the first support touch. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira gentle face after supporting exhausted unarmored Ren at same ruined plaza; Ren nearby offscreen left.. Voice / balloon: warm soft outline.
ONLY speaker: Mira. EXACT text: 「英雄も、お腹は空くんですね。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren hand on empty stomach, now BARE after armor has faded; Mira still supporting him.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 04-invoice.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Rook in silver armor, blue cape, black gloves offers a paper sheet across the plaza. Ren's bare hand accepts the sheet. Paper is geometric unreadable lines only, no invented numbers.

Balloon 1: speech, Rook, upper right. EXACT text: 無許可の戦闘だ。 . Columns RIGHT to LEFT: 無許可の / 戦闘だ。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## v6-debt.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-02/art/05-debt.png", "sha256": "a9f50b94815347a968d4b314cc9a299fbfde4c276832b305cb8fa01b9419744b"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Close unarmored Ren looking up from the same sheet with shocked eyebrows, chest not glowing. Mira and Rook remain beside plaza rubble.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Close unarmored Ren looking up from the same sheet with shocked eyebrows, chest not glowing. Mira and Rook remain beside plaza rubble. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY unarmored Ren face looking up from SAME invoice, shocked not angry; Rook offscreen right.. Voice / balloon: baffled slightly wavering spoken oval.
ONLY speaker: Ren. EXACT text: 「助けたら、借金？」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Invoice held in Ren BARE hand; paper abstract geometric lines, no invented amount.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 06-crack.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Close crack widening across a white aqueduct support above a gap. Water leaks downward. Only effect ミシ… . No people or rescue outcome.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 07-stranded.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Vertically establish damaged aqueduct: mother in brown shawl and small boy in green shirt stranded on tilted upper ledge; open gap below; rescuers Ren and Mira on intact LOWER opposite ledge. Clear unsafe and safe positions, no bridge yet.

Balloon 1: speech, Mother, upper right. EXACT text: 誰か…！ . Columns RIGHT to LEFT: 誰か…！.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## 08-barrier.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Precise edit reference1 ONLY. Reference2 locks the mother and boy identity and clothes while they are still stranded. In reference1, change ONLY distant boy shirt from blue-grey to OLIVE GREEN short sleeves; match same brown-haired small boy and same mother from reference2. Give mother the same BROWN hooded shawl over white blouse, hood over her brown hair, and worried expression. Both remain together on the UPPER RIGHT distant unsafe ledge, never beside Ren. Keep entire Ren and Rook foreground, cordon rope, silver armor, blue cape, black gloves, red scarf, anatomy, architecture, framing and exact existing LARGE vertical balloon 立入禁止だ。 unchanged. No new words, people, armor, rescue outcome or layout change.
```

## 09-set-down.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Precise edit of this anime comic image. Fix ONLY premature family placement and stray lettering. It is BEFORE the rescue: the mother and boy remain stranded on a DIFFERENT upper-right ledge several metres away, so they MUST NOT appear beside Ren. Remove both mother and child from the right of this image; seamlessly fill their area with matching sunny white-city stone architecture/empty sky. Keep Ren's exact black-haired blue-eyed face, unarmored black short sleeves, red scarf, anatomy, hand placing the invoice on this safe dry stone and the blue-caped Rook in background unchanged. Ren is choosing to rescue, not talking to an already rescued family. Paper should contain only abstract non-readable lines and a crown stamp, no invented readable words. Do not add speech balloons, words, new people, armor or rope bridge. Preserve wide composition, anime style and beautiful daylight colors. No parent or child anywhere in this edited frame.
```

## 10-choice.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Unarmored Ren leans toward danger, teeth set but visibly tired, Mira behind him sees his decision.

Balloon 1: speech, Ren, upper right. EXACT text: まだ、手は届く。 . Columns RIGHT to LEFT: まだ、 / 手は届く。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## v6-hold.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-02/art/11-hold.png", "sha256": "3bcda37055d4f8af4938155906677d02f6e63240569621eb6713b49692354b45"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Ren reactivates only weak complete black armor/cyan star; feet braced on intact lower ledge, both hands lift a fallen white beam so it spans the gap to the family. Beam holds position as a crossing, family not crossing yet. The family stays on UPPER RIGHT broken ledge. Ren is on LOWER LEFT intact ledge. One long stone beam runs diagonally lower-left to upper-right, FAR end rests firmly on family ledge, Ren lifts/supports NEAR end with BOTH hands and braced feet, a physically usable inclined bridge. Mother brown hooded shawl and white blouse, boy olive GREEN shirt. No family on safe ledge yet.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren BASIC black-armored strained face at same beam crossing, cyan star weak. He MAINTAINS the beam, not attacking.. Voice / balloon: strained wavering speech; continuous tail, no thought dots.
ONLY speaker: Ren. EXACT text: 「戦う燃料がないなら、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Close black-armored hands supporting SAME white beam, boots braced on solid ledge; family remains stranded at far end, has NOT crossed yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren BASIC black-armored strained face at same beam crossing, cyan star weak. He MAINTAINS the beam, not attacking.. Voice / balloon: strained wavering speech; continuous tail, no thought dots.
ONLY speaker: Ren. EXACT text: 「持ち上げるだけだ。」 (render contents only).

```

## 12-rope.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png", "art/07-stranded.png"]

採用時の指示：

```text
Edit the first manga illustration to fix rescue continuity. Preserve its polished full-color anime manga style, crisp linework, Mira's face and elegant white blue gold gown, and the exact existing speech balloon 「この縄を、支えてください。」 in true Japanese vertical columns read right to left. Recompose the scene clearly: Mira is on the SAFE LOWER-LEFT ledge, passing a coiled rope to TWO ADULT RESIDENTS (adult male workers in simple tan and grey clothes). Replace the mother and boy beside Mira with those two adult helpers. One end of the rope is tied to the intact white column on this safe ledge. The mother in brown hooded shawl and eight-year-old boy in OLIVE GREEN shirt remain SMALL AND DISTANT on the UNSAFE UPPER-RIGHT ledge, separated by a visible chasm, as in the second reference. Ren must be in BLACK FACETED BASIC HERO ARMOR, CYAN seams and CYAN STAR chest, RED scarf, black hair uncovered, matching the third reference. Ren is UNDER the NEAR END of the diagonal stone beam at LOWER LEFT, boots firmly braced on a remaining lower shelf, BOTH ARMS raised ABOVE his head supporting the underside of that beam. He cannot grip it from above or stand on it. The beam's far end rests on the upper-right family ledge. Show credible load-bearing pose. Family has not crossed yet. Mira's balloon tail points only to Mira. Portrait manga shot, no collage, no extra text.
```

## 13-cross.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png", "art/07-stranded.png"]

採用時の指示：

```text
Edit the first illustration to correct the bridge mechanics in this rescue manga, keeping the exquisite anime art, stone aqueduct, chasm, olive green shirt boy and brown hooded mother and safe-side adult rope helpers. The second reference establishes geography; the third reference establishes Ren's actual support pose. Ren MUST NOT walk on the bridge or hold the rope. Move Ren to the LOWER LEFT on a small intact stone shelf BELOW the near end of the bridge. His boots brace against the shelf, both arms raised over his head, BOTH HANDS visibly support the UNDERSIDE of the near end of the diagonal stone beam. Ren remains in BASIC BLACK FACETED armor with thin CYAN seams and a CYAN star chest, RED scarf, messy black hair uncovered. The far end of the long stone beam rests firmly on the UNSAFE UPPER-RIGHT ledge. The brown hooded mother and eight-year-old olive green shirt boy are now HALFWAY ACROSS the narrow stone beam from upper right toward lower left, walking carefully while grasping the taut safety rope. The two adult villagers on the safe lower-left platform pull the other end of that safety rope. Draw a wide enough view in this tall panel to show Ren below supporting, family above crossing, and a deep open chasm underneath. Keep the people distinct and do not fuse any hands. No speech, no text, one tall cinematic continuous panel.
```

## 14-safe.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png", "art/07-stranded.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Mother and boy now both on dry intact safe ledge, hugging each other, relieved faces. Rope slack, beam still secured, no return to dangerous position.

Balloon 1: speech, Boy, upper right. EXACT text: お母さん…！ . Columns RIGHT to LEFT: お母さん…！.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Fourth reference establishes same mother (brown hooded shawl and white blouse), same boy (olive green short sleeve shirt), same aqueduct gap: unsafe upper RIGHT ledge, safe lower LEFT ledge. The supported stone bridge slopes from upper-right down to lower-left. Preserve identity, but change safety position ONLY according to THIS exact scene.
```

## 15-exhale.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren unarmored again sitting at safe ledge edge, bare hands trembling; Mira kneels beside him with a water cup, no romantic touch. Rescued family behind safely.

Balloon 1: speech, Ren, upper right. EXACT text: よかった…。 . Columns RIGHT to LEFT: よかった…。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## v6-responsibility-paper.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-02/art/v6-responsibility.png", "sha256": "1d2b50d12e2da1d356296f4846ddd0ebce03d1dbf16617840086fcaf6148eb4e"}]

元の生成指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira stands between Rook and seated tired Ren. Holds invoice herself, authoritative concern, ruined crown-run aqueduct behind. Ren no armor.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira serious face holding invoice at SAME safe ledge, tired unarmored Ren nearby; Rook listens offscreen.. Voice / balloon: firm composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「王家の責任です。」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: ONLY Ren tired eyes look up at Mira, surprised she accepts responsibility. Rescued family stays safely offscreen.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira serious face holding invoice at SAME safe ledge, tired unarmored Ren nearby; Rook listens offscreen.. Voice / balloon: firm composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「あなた一人に払わせません。」 (render contents only).

```

採用時の指示：

```text
Edit ONLY the paper invoice surfaces in the FIRST and THIRD panels of this existing vertical manga strip. Preserve the entire image size, every panel position, faces, hands, clothes, background, Japanese balloon text and balloon shape exactly. Keep the invoice parchment outline, royal blue-and-gold crest, decorative border and abstract horizontal/table ruling. Remove ALL tiny pseudo-English words, fabricated numbers, totals, and fake legible text from both copies of this same invoice. Replace these tiny text marks with sparse neutral nonlinguistic short strokes or plain empty ruled fields, so no invented monetary amount is asserted. The exact Japanese dialogue 王家の責任です。 and あなた一人に払わせません。 stays entirely untouched. No other edits.
```

## 17-cancel.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Close Mira places royal ring over the invoice in Rook's gloved hands, cancelling the demand by gesture; Ren watches startled, paper unchanged unreadable diagrams. No new text.

Balloon 1: speech, Rook, upper right. EXACT text: …承知しました。 . Columns RIGHT to LEFT: …承知 / しました。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## 18-turn-fragment.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png", "../v5/art/06-giant.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Mira turns over the guardian fragment already found in episode1; its outer crown crest turns away; backside still hidden from camera. Ren leans closer, curiosity replaces relief. No workshop number visible yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 19-workshop-number.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png", "../v5/art/06-giant.png", "art/18-turn-fragment.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: FIRST close reveal backside guardian fragment with etched small crown plus exact horizontal plate text 王室工房　七番 . Mira's fingertips and surprised eyes behind. Only this label on metal, not a speech balloon.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## v6-inside-threat.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-02/art/20-inside-threat.png", "sha256": "f610d3e54ffb8453251eda1375704f69e133d94dfdcba6807ec6a027a782d995"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira holds revealed fragment, Ren stands beside her looking toward royal white towers with sober expression. No enemy identity shown.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Mira holds revealed fragment, Ren stands beside her looking toward royal white towers with sober expression. No enemy identity shown. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira concerned face; same single core fragment with REVERSE plate already revealed, Ren offscreen beside her.. Voice / balloon: quiet serious blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「これ、外から来た魔物じゃない。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren eyes shift from fragment toward royal towers; no new enemy or incident.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```
