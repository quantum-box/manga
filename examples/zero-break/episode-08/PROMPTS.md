# 第08話 — 採用原画の実行指示

全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・旧版保持を generation-log.json で区別。以前の実行記録は production/feedback-v6/baseline に保持。

## 01-corridor.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Ren unarmored red scarf, Mira white blue gold gown and Rook without license walk long white certification hall. Framing statues only calves and immense shadow, white hero head not visible yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## 02-portrait.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: FIRST full huge WHITE armored ancient hero statue with GOLD chest star, no visible living face; small red-scarf Ren below looks up. Retain unknown name, no Arata caption.

Balloon 1: speech, Ren, upper right. EXACT text: 誰だ、この人。 . Columns RIGHT to LEFT: 誰だ、 / この人。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## v6-first-hero-gold.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-08/art/v6-first-hero.png", "sha256": "b8bf13bbb675de39c9ed830752b78d2584411c24e8c0f597d30d162d560c6476"}, {"path": "examples/zero-break/episode-08/art/v6-compare-star.png", "sha256": "62e0b8b75dfe115828ede818f6e4b747ed58cda937b6db6c0ed848ade2e8f49c"}]

元の生成指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Thin masked ceremony guide in grey formal robe points to white statue, neutral expression. Ren Mira listen.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Thin masked ceremony guide in grey formal robe points to white statue, neutral expression. Ren Mira listen. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY masked thin ceremony guide in GREY robe face, SAME white certification hall; Ren and Mira listen offscreen.. Voice / balloon: neutral formal rounded speech.
ONLY speaker: Guide. EXACT text: 「初代勇者です。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren looks up at SAME WHITE-armored statue with GOLD star, small view only; no living face or name アラタ.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

採用時の指示：

```text
Targeted continuity edit of image 1 ONLY. Preserve this entire three-panel vertical manga strip, all panel sizes and alignment, every character face and costume, the white marble statue, the grey masked guide and the exact Japanese dialogue 初代勇者です。 unchanged. In first and third panels, the ancient WHITE statue has a small unmistakable GOLD eight-point star centered on its chest, matching the statue chest star in image 2. Any cyan/blue star embellishment ON THE STATUE or its sword must become GOLD, not blue: Ren's living core is cyan, the statue's star is gold. The white statue stays carved marble, never a living person. Pedestal banner decoration and palace banners can stay blue-and-gold. Image 2 is continuity reference only and must not be returned or altered. No new name, label, dialogue, face or event.
```

## v6-compare-star.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-08/art/04-compare-star.png", "sha256": "7a7c215a035b40530df321142b92a903aa965f508cd3070533c21baba1f46367"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira looks from statue GOLD star to Ren's faint CYAN chest point visible at scarf shirt neckline. Close bodily clue, not equal color or new form.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira thoughtful face in SAME statue hall, looks between statue and Ren, no new danger.. Voice / balloon: quiet softly wavering blue-grey speech.
ONLY speaker: Mira. EXACT text: 「星の形が、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Compare a shallow silent detail: same GOLD statue star above, Ren faint CYAN chest point below scarf at edge. Shapes match but COLORS DIFFER. NO new form.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira thoughtful face in SAME statue hall, looks between statue and Ren, no new danger.. Voice / balloon: quiet softly wavering blue-grey speech.
ONLY speaker: Mira. EXACT text: 「同じ…。」 (render contents only).

```

## 05-trial-door.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Edit ONLY the hooded bearded door-opening man in the FIRST anime panel. He is the SAME thin young-adult CEREMONY GUIDE from reference2: dark brown hair tied low, clean shaven face, ornate SILVER half-mask covering eyes, GREY formal high-collar robe. Remove his black hood, beard, brown leather adventurer straps and gold cloak; change to the same grey ceremony robe and silver mask from reference2. Keep his gloved hand inserting key and door-opening pose. Preserve Ren, Mira, Rook, iron trial door, lighting and composition. No speech balloons or new words, no extra characters.

```

## 06-human-targets.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: FIRST trial hall reveal: living adult residents shackled upright on movable training target platforms; mechanical launchers aimed nearby. Graphic violence absent, ropes/chain clear, lives endangered. Ren shocked.

Balloon 1: speech, Ren, upper right. EXACT text: 人を、的にするのか。 . Columns RIGHT to LEFT: 人を、 / 的にするのか。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## v6-refuse.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-08/art/07-refuse.png", "sha256": "494f65123c458d60d58feb2210313c4bcbbc4daedfdb03873e09e2e766ed8b1c"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Ren turns away from offered ceremonial sword, opens empty hand toward captive adults; expression controlled outrage.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Ren turns away from offered ceremonial sword, opens empty hand toward captive adults; expression controlled outrage. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren controlled outraged face in SAME trial hall, ordinary black shirt red scarf; no armor yet.. Voice / balloon: firm ordinary oval.
ONLY speaker: Ren. EXACT text: 「こんな試験、受けない。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren BARE open hand turns away from offered ceremonial sword toward actual restrained living adults. No killing or early chain release.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 08-disqualify.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Edit ONLY the bearded older judge at the RIGHT of the FIRST anime panel: replace him with the SAME thin young-adult ceremony guide from reference2, brown hair tied low, clean-shaven, ornate SILVER half-mask over eyes, GREY high-collar formal robe. Preserve his hand pulling the bell rope and pointing toward exit, same exact vertical dialogue 失格です。 and its tail, bell sound カン, Ren, Mira, Rook, hall and all composition. No navy royal cape, no beard, no extra characters or balloons. Same person speaking in both panels.

```

## 09-turn-back.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png", "art/02-portrait.png", "art/06-human-targets.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren turns his BACK to guide and walks toward captive adult's dangling chain, bare hand already reaching. Rook and Mira prepare to assist, no full armor.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## 10-cut-chain.png

retained prior adopted image_gen output

参照：["../production/references/ren-partial.png", "../production/references/mira.png", "art/02-portrait.png", "art/06-human-targets.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Only Ren's black armored LEFT forearm with cyan seam forms to protect resident as mechanism tensions chain; he breaks one chain link with gloved hand, RIGHT bare hand steadies resident. Other residents still chained.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
Ren rescue state: ONLY his LEFT hand and LEFT forearm carry BASIC BLACK/CYAN armor, with torso and right arm ordinary BLACK FABRIC and BARE skin. The cyan core is a tiny point on the chest, no full suit, no second form, no shoulder plates. He stays beside the captives freeing chains; Rook silver shield covers the one EXIT.
```

## 11-guards-run.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png", "art/02-portrait.png", "art/06-human-targets.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Grey helmeted guards run from statue shadow toward freeing team; Rook raises shield at doorway, Mira guides freed residents behind him. Not an enemy victory image.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
Ren rescue state: ONLY his LEFT hand and LEFT forearm carry BASIC BLACK/CYAN armor, with torso and right arm ordinary BLACK FABRIC and BARE skin. The cyan core is a tiny point on the chest, no full suit, no second form, no shoulder plates. He stays beside the captives freeing chains; Rook silver shield covers the one EXIT.
```

## 12-hold-exit.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png", "art/02-portrait.png", "art/06-human-targets.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Rook blocks guards at narrow hall exit with shield and sheathed sword as barrier, no killing, Ren breaks remaining restraints behind.

Balloon 1: speech, Rook, upper right. EXACT text: この出口は、閉めさせない。 . Columns RIGHT to LEFT: この出口は、 / 閉めさせない。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
Ren rescue state: ONLY his LEFT hand and LEFT forearm carry BASIC BLACK/CYAN armor, with torso and right arm ordinary BLACK FABRIC and BARE skin. The cyan core is a tiny point on the chest, no full suit, no second form, no shoulder plates. He stays beside the captives freeing chains; Rook silver shield covers the one EXIT.
```

## 13-copy-evidence.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "art/02-portrait.png", "art/06-human-targets.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Mira copies trial recording via brass memory crystal at wall console. Exact large display text 記録保存 only; chamber and target silhouettes reflected. No huge futuristic HUD.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## v6-their-evidence.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-08/art/14-their-evidence.png", "sha256": "d89a402b14a35f4c3ef6a04b1318fba3041ad78791adfc80b217acbca6fd51c5"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira holds copied memory crystal in palm toward bewildered grey-robed guide; residents already walking safely behind Rook.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Mira holds copied memory crystal in palm toward bewildered grey-robed guide; residents already walking safely behind Rook. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira resolute face in SAME trial hall AFTER copying memory crystal, freed people already exiting safely behind Rook.. Voice / balloon: composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「あなたたちの証拠です。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Mira BARE palm offers ONE brass memory crystal toward grey-robed guide; no multiple crystals or new display text.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 15-rescue-outcome.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "art/02-portrait.png", "art/06-human-targets.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Freed adult resident reaches outside sunlight and touches wrist where chain was; Ren unarmored helps steady them, quiet relieved empathy, no crowd applause yet.

Balloon 1: speech, Resident, upper right. EXACT text: …外だ。 . Columns RIGHT to LEFT: …外だ。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## 16-old-inscription-cue.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "art/02-portrait.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: During exit, Ren notices dusty letters carved low on white statue plinth behind grass, finger sweeps dust. Text still hidden under hand and dust, no future name.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## 17-selection.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "art/02-portrait.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: FIRST close exact carved inscription 救済は選別である on pale stone plinth, horizontal formal lettering large, no other words or speaker.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Cast continuity: Noa remains at the workshop and is NOT in this scene. No orange-haired mechanic here. Ren, Mira and Rook are the visitors, plus only the specified guide, guards or captives. Ren begins in ordinary BLACK fabric, bare arms and bare hands; partial LEFT gauntlet only during the chain rescue when explicitly requested.
```

## v6-reject-selection.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-08/art/18-reject-selection.png", "sha256": "441df7b48547a78cceb5a3dafb66a18acc0b1df62d790c28e3e3726657480bc8"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Ren at statue base looks up with anger and resolve, unarmored scarf red against white hero shadow, Mira holds recording beside him.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Ren at statue base looks up with anger and resolve, unarmored scarf red against white hero shadow, Mira holds recording beside him. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren unarmored angry restrained face at SAME statue base AFTER reading the selection inscription.. Voice / balloon: low firm ordinary oval.
ONLY speaker: Ren. EXACT text: 「誰が、そんなことを決めた。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren BARE hand drops from dusty plinth; white statue shadow over red scarf, Mira holds same recording offscreen. No future enemy face or name.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```
