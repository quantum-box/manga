# 第09話 — 採用原画の実行指示

全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・採用原画の保持を generation-log.json で区別。以前の実行記録は Git の履歴で管理。

## 01-workshop-return.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png", "../production/references/noa.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Rescue team back in warm workshop at night, freed residents rest on cots; Noa connects neutral magic meter near unarmored Ren, Mira holds trial memory crystal, Rook guards closed door.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 02-zero-again.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a11-result.png"]

採用時の指示：

```text
Edit ONLY time-of-day background and light in FIRST image. Preserve the same black crystal on silver gothic measuring pedestal, the exact large numeral 0, Ren's BARE hand, any native vertical speech, composition and all device details. This is the NIGHT brass-and-brick workshop from image2, not daytime: replace bright daylight windows with dark indigo night windows, warm amber oil-lamp light and dim brick/copper-pipe interior. No sun or bright blue sky, no character/letter changes, no armor.
```

## 03-replay.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Noa slowly replays paper/oscilloscope line: magic needle flat while cyan chest glow visible in recording. Gesture toward discrepancy, device design consistent.

Balloon 1: speech, Noa, upper right. EXACT text: 針は、動いてない。 . Columns RIGHT to LEFT: 針は、 / 動いてない。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## v6-other-axis.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-09/art/04-other-axis.png", "sha256": "fb8ca4c4447e4c28151f22ac385a5a865705109440adc128ad2ac4982217924d"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira draws TWO clear simple graph axes on paper, one flat, one rises during rescuing; exact large horizontal labels 魔力 and 救助負荷 . Ren leans in, not instantly master explanation.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira calm explaining face in SAME warm amber workshop AT NIGHT; no sunshine windows.. Voice / balloon: clear composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「空じゃない。」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Physical paper with TWO graph axes: large exact horizontal labels 魔力 and 救助負荷. One flat and one rises. Ren eyes follow the difference without instant mastery.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira calm explaining face in SAME warm amber workshop AT NIGHT; no sunshine windows.. Voice / balloon: clear composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「測る箱が違う。」 (render contents only).

```

## 05-understand.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Edit ONLY background and its light in FIRST image. Preserve Ren's black ordinary short-sleeve FABRIC shirt, bare hand/arm, red scarf, small cyan point at chest, thoughtful face and EXACT native vertical speech ゼロでも、ここにはある。. Replace the bright outdoor palace setting with the SAME INSIDE brass-and-brick rescue workshop at NIGHT in image2: oil lamps, copper pipes, shelves, warm amber light and dark indigo night window. No location jump outside, no daylight, no armor, no new characters or letters.
```

## 06-siege.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Outside night alley, grey armored royal guards surround workshop main door and power pillar. Inside team not yet fighting, no graphic force.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 07-cut-power.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Guard lever cuts workshop supply cable at street fuse box, lanterns inside dim visible through window. Ordinary electrical sabotage, no future villain face.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## v6-ventilator-stops.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-09/art/08-ventilator-stops.png", "sha256": "30018f28486e75622454b213a3db2fb7061e1ab11526b04880e796d25956dbc1"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Inside simple medical alcove, OLD MAN brown vest grey beard saved in episode5 on cot uses brass bellows breathing assistance, motion slows; Mira notices distress, no death or gore.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: Inside simple medical alcove, OLD MAN brown vest grey beard saved in episode5 on cot uses brass bellows breathing assistance, motion slows; Mira notices distress, no death or gore. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira suddenly worried face in SAME NIGHT medical alcove after power cut.. Voice / balloon: urgent angular bold outer outline, continuous mouth tail.
ONLY speaker: Mira. EXACT text: 「呼吸の装置が…！」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Brass breathing bellows slowing beside SAME grey-bearded old man in brown vest on cot; no death/gore or restored breathing yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 09-check-patient.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png", "art/08-ventilator-stops.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren unarmored kneels beside same elderly man with shallow breath, checks wrist while Noa pulls isolated test circuit box from shelf. No immediate success.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## v6-isolate-circuit.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-09/art/10-isolate-circuit.png", "sha256": "34591943bfaa520f322d465421adbc2c52ec786729a440b4206734be44a13517"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Noa connects ONLY isolated rescue-core circuit to ventilator, physical copper leads and safety switch visible; no connection to city main grid or new form. Ren keeps one bare hand on terminal.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Noa focused face in SAME dim NIGHT workshop, orange goggles and gloves, not outside in sunlight.. Voice / balloon: calm practical ordinary capsule.
ONLY speaker: Noa. EXACT text: 「街の線とは、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Orange-gloved hands connect physically ISOLATED rescue-core copper circuit ONLY to ventilator. Ren BARE hand on terminal at edge. No city-grid connection or new form, device not moving yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Noa focused face in SAME dim NIGHT workshop, orange goggles and gloves, not outside in sunlight.. Voice / balloon: calm practical ordinary capsule.
ONLY speaker: Noa. EXACT text: 「切り離す。」 (render contents only).

```

## 11-give-power.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "art/08-ventilator-stops.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Ren concentrates faint CYAN energy from chest into isolated lead with BOTH arms UNARMORED, no full armor or attack. Bellows starts first small motion, he sacrifices combat output.

Balloon 1: speech, Ren, upper right. EXACT text: 戦う力は、あとでいい。 . Columns RIGHT to LEFT: 戦う力は、 / あとでいい。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## 12-rook-guard.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Rook silver armor blue cape holds steel shield against workshop door under guards' blows, protects exhausted unarmored Ren inside. No miraculous limitless power.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## 13-breath-cue.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "art/08-ventilator-stops.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Close brass ventilator bellows expands and cyan indicator starts tiny pulse, patient face still outside crop. Wait for actual breathing response, no healthy smile shown yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## v6-breath-returns.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-09/art/14-breath-returns.png", "sha256": "fd9ae266de0b6708627367363307db68fec71715591e4446313de08154b71cca"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): FIRST clear elderly man inhales, chest visibly lifts under blanket, hand relaxes; Mira relieved nearby, Ren remains at powered circuit.

Panel 1, downward order. Frame: full-width wide framed establishing shot. Reader understands: Confirm the immediate context without adding a new event.. Visible camera subject / offscreen continuity: FIRST clear elderly man inhales, chest visibly lifts under blanket, hand relaxes; Mira relieved nearby, Ren remains at powered circuit. Show the established spatial relationship, WITHOUT replaying earlier action or later results.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira relieved face in SAME NIGHT alcove, ordinary blue-white-gold dress.. Voice / balloon: gentle soft blue-grey contour.
ONLY speaker: Mira. EXACT text: 「息が、戻った。」 (render contents only).
Panel 3, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Same grey-bearded old man FIRST visibly inhales, blanket chest lifts, fingers relax. Ren STILL supplies isolated circuit offscreen, has not stopped.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 15-small-line.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Output paper recorder draws a small unmistakably rising cyan line, Noa points with oil stained orange glove, no huge numeric gain, no upgraded gadget.

Balloon 1: speech, Noa, upper right. EXACT text: ちゃんと、届いてる。 . Columns RIGHT to LEFT: ちゃんと、 / 届いてる。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## 16-signal.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Noa sees a faint stray transmission travelling out of isolated sensor toward thin separate line on city map. Do not show location label yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## 17-under-palace.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: FIRST reveal city map route goes into chamber DIRECTLY beneath royal palace white towers; map exact large label 王宮直下 . Mira traces destination, no fuel torture depiction.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## v6-location.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-09/art/18-location.png", "sha256": "e34430945c3692f1b2a214fb52f501e6a01427a2f30ddef90ccb45b7e2bb9e88"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira holds traced map while Ren still powers ventilator, eyes resolved. Rook keeps protective door, Noa watches line.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira resolved face in SAME NIGHT workshop after route revealed on map.. Voice / balloon: quiet serious blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「ここが、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Mira fingertip traces SAME map directly underneath palace, EXACT large existing label 王宮直下. Ren keeps ventilator powered offscreen, Rook guards door. No new chamber victims or villain yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira resolved face in SAME NIGHT workshop after route revealed on map.. Voice / balloon: quiet serious blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「消えた街区の行き先。」 (render contents only).

```
