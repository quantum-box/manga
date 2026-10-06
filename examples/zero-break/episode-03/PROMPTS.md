# 第03話 — 採用原画の実行指示

全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・旧版保持を generation-log.json で区別。以前の実行記録は production/feedback-v6/baseline に保持。

## 01-morning.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Next morning bright market of white sky city, Ren unarmored red scarf carrying bread beside Mira; Rook waits at cleared training space, unsharpened training sword lowered. No power yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## v6-challenge.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-03/art/02-challenge.png", "sha256": "605cdc865dbaff17a363b399594490210afc918a5dede03d84b7d649ce8cab95"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Rook offers a permit envelope and points practice sword toward marked dueling space, Ren listens warily, Mira observes.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Rook offers a permit envelope and points practice sword toward marked dueling space, Ren listens warily, Mira observes. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Rook confident face in SAME morning market training space, practice sword lowered safely. Ren remains unarmored offscreen left.. Voice / balloon: reserved ordinary oval.
ONLY speaker: Rook. EXACT text: 「私に勝てば免許をやる。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Rook glove holding unopened permit envelope; Ren BARE fingers hesitate, no acceptance and no armor.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 03-fist.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Edit this single manga panel to remove every trace of transformation. KEEP Ren's face, clenched BARE fist pose, red scarf, brown narrow shoulder straps, composition, background, crisp anime linework and daylight. Replace ALL black metal armor plates, all floating shards, ALL cyan glowing seams and ALL cyan chest lights with his ordinary plain BLACK SHORT-SLEEVE fabric shirt and exposed bare forearm skin. Chest is totally DARK cloth. He tries to summon power for a duel but NOTHING HAPPENS: no armor, no particles, no glow, no system messages. The fist must remain natural bare skin, five fingers folded correctly. No text, no dialogue. Refer to second image for ordinary shirt and uncovered arms. Preserve the thin black panel border.
```

## v6-no-answer.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-03/art/04-no-answer.png", "sha256": "c0ea65488d91696d2a822ea30fdec8b875b56f7557672cfdf9ec3c1ef301a962"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Ren stares at his unchanged bare hand, worried; chest dark. Rook's practice sword held safely down, crowd amused.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Ren stares at his unchanged bare hand, worried; chest dark. Rook's practice sword held safely down, crowd amused. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren face, uncertain after failing to transform for a duel, same training space.. Voice / balloon: thought cloud with dots, never a speech tail.
ONLY speaker: Ren thought. EXACT text: 「さっきの力、もう消えたのか。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: ONLY Ren BARE open hand, sleeve ordinary BLACK cloth; chest dark, no power.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 05-laughter.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Two adult market spectators snicker behind an uncertain Ren foreground. No text, no aggressive mob or new armor.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 06-practice.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Rook makes one slow practice sword approach toward Ren's bare hand in training area; Ren steps back safely, no armor, not a wound or real fatal attack.

Balloon 1: speech, Rook, upper right. EXACT text: その程度か。 . Columns RIGHT to LEFT: その程度か。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## 07-axle.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png", "../episode-02/art/14-safe.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Nearby laden handcart wooden axle splits under a barrel. FIRST mechanical failure, child's shadow farther down slope, no rescue or armor. Only effect バキッ .

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 08-barrel.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/14-hero.png", "../episode-02/art/14-safe.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Large barrel rolls down sloped white market steps toward SAME small boy green shirt from prior rescue, mother reaches from side too far. Show actual barrel, child and Ren distance. No impact yet.

Balloon 1: speech, Mother, upper right. EXACT text: 危ない！ . Columns RIGHT to LEFT: 危ない！.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## 09-move.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../v5/art/06-giant.png", "../episode-02/art/14-safe.png", "art/08-barrel.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren discards bread bag safely and runs toward child with bare hand extended, decisive urgency. No giant leap, no armor until protection moment.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 10-shield-arm.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../episode-02/art/14-safe.png", "art/08-barrel.png"]

採用時の指示：

```text
Edit ONLY the small orange-haired goggle-wearing figure at upper left of this panel. That character has not been introduced yet and must not appear here. Replace him with an ordinary ADULT MARKET VENDOR, short brown hair, beige linen shirt, NO goggles, NO mechanic blue overalls, surprised but unharmed. Preserve EVERY other element: Ren with LEFT forearm black cyan armor and black fabric torso, red scarf, rescued green-shirt boy, Mira, Rook, barrel, composition and anime style. No text or balloons. Do not change Ren's protective action or add armor anywhere else.
```

## 11-stop.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../episode-02/art/14-safe.png", "art/08-barrel.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Ren's ONE armored forearm braces and stops the intact barrel one step from child; boots dug into slope, mother behind child reaches him. No attack on Rook, no explosion. Only effect ドン .

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Continuity: ONLY Ren's LEFT forearm and left hand are covered in black faceted cyan-seamed basic armor. RIGHT hand and both upper arms remain bare; torso stays ordinary black fabric shirt with brown straps; legs ordinary charcoal trousers. No armor on shoulders, torso, right arm, or legs. This is partial activation, not full transformation.
```

## 12-realization.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../episode-02/art/14-safe.png", "art/08-barrel.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren looks at armored forearm in astonishment, Rook lowers practice sword safely in background; stopped barrel beside feet, child and mother together.

Balloon 1: speech, Ren, upper right. EXACT text: 勝つためには、動かない？ . Columns RIGHT to LEFT: 勝つためには、 / 動かない？.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Continuity: ONLY Ren's LEFT forearm and left hand are covered in black faceted cyan-seamed basic armor. RIGHT hand and both upper arms remain bare; torso stays ordinary black fabric shirt with brown straps; legs ordinary charcoal trousers. No armor on shoulders, torso, right arm, or legs. This is partial activation, not full transformation.
```

## 13-reunion.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png", "../episode-02/art/14-safe.png", "art/08-barrel.png"]

採用時の指示：

```text
Edit ONLY Ren's visible armored forearm and hand at lower left of the first panel. The rescue has ended and his partial armor has now disappeared. Replace ALL plates and cyan light on that arm with his natural BARE SKIN forearm and bare relaxed hand; preserve plain black short sleeve and trousers, red scarf and shoulder straps. Keep the mother and olive green shirt boy hugging, Mira and Rook, all faces and poses, the panel layout, and the EXACT balloon 「ありがとう。」 with upright Japanese vertical glyphs and its tail toward the boy. No remaining armor or star on Ren's hand. Everything else unchanged.
```

## v6-rule.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-03/art/14-rule.png", "sha256": "8df5e24cacfbdb50c141f98115f3a25e8d489c7dba66131a84ff2d9521214a01"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira approaches Ren and points gently to faint cyan chest point while Ren listens, both now unarmored. Rook silent background.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira calm thoughtful face in SAME market after barrel stopped; child already with mother offscreen.. Voice / balloon: gentle composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「助けるときだけ、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren looks down at now BARE forearm; the partial armor has already faded during the reunion. Both hands BARE, no armor. Faint cyan point remains at fabric chest. He compares the completed rescue with failed duel.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira calm thoughtful face in SAME market after barrel stopped; child already with mother offscreen.. Voice / balloon: gentle composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「応えている。」 (render contents only).

```

## v6-permit.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-03/art/15-permit.png", "sha256": "4c165ab80f0815d851f888559c63a640a3a57a4f377e02fee4002e7eef3741c5"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Ren sets duel prize purse and unopened permit envelope back on training table, walks toward rescued family with Mira. No victory in duel or illegal reward.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Ren sets duel prize purse and unopened permit envelope back on training table, walks toward rescued family with Mira. No victory in duel or illegal reward. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren face, quietly resolved beside training table AFTER child safe, unarmored red scarf.. Voice / balloon: calm ordinary oval.
ONLY speaker: Ren. EXACT text: 「じゃあ、勝つより先に助ける。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren BARE hand puts unopened permit and prize purse BACK on table. No duel victory or license reward.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 16-mechanical-bird.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Small silver brass mechanical bird secretly watches FROM market roof, cyan camera lens aimed toward Ren far below. No enemy face or display text yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 17-monitor.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png"]

採用時の指示：

```text
Edit this manga panel to correct WHO is in the secret monitoring room. REMOVE THE LIVING REN figure completely from the left side: he is still in the market and cannot be in this room. Replace his entire body, face, hair, scarf and hands with dark empty room, shadowed stone arches and bookshelves. Make the cyan translucent monitor the main composition, preserving the recorded anatomical chest/core image and exact large horizontal label 「未登録救済核」. No people, no face, no scarf anywhere. This is a remote unknown enemy's surveillance screen showing only a DATA RECORDING of Ren's rescue core, not Ren physically standing beside it. Keep desk and cool dark lighting, crisp detailed anime linework and thin manga border. No dialogue or extra readable words.
```

## 18-watcher.png

retained prior adopted image_gen output

参照：["../v5/art/a14-rejection.png", "../v5/art/16-relief.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Silhouette hand resting on desk beside same cyan monitor. Only sleeve edge, no face or white armor revealed.

Balloon 1: speech, Unknown, upper right. EXACT text: ようやく来たか。 . Columns RIGHT to LEFT: ようやく / 来たか。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```
