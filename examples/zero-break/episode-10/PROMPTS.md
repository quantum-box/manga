# 第10話 — 採用原画の実行指示

全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・旧版保持を generation-log.json で区別。以前の実行記録は production/feedback-v6/baseline に保持。

## 01-festival.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png", "../production/references/noa.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Day festival plaza in sky city, white banners, audience faces expect celebration. Noa runs brass projector, Mira near podium, Ren unarmored red scarf nearby, Rook in plain duty armor without license. No tragedy yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
```

## v6-evidence.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-10/art/02-evidence.png", "sha256": "7f68f3f75d69de713553f916033306e96701a3edb712ae1b1df29be492c3749a"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Projector beam FIRST shows silhouettes in transport conduit from episode5 and humans shackled as targets from8, recognizable records, no unreadable long caption. Audience laughter ends, concerned faces foreground. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira solemn face at DAY festival podium, brass microphone; first public evidence projection behind is blurred.. Voice / balloon: firm composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「消された人には、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Audience one listener face stops laughing; physical recording shows transport silhouettes, no new victims or illegible captions. Ren unarmored offscreen.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira solemn face at DAY festival podium, brass microphone; first public evidence projection behind is blurred.. Voice / balloon: firm composed blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「名前があります。」 (render contents only).

```

## 03-cut-switch.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png", "../episode-07/art/03-superior.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Same older commander black greying hair navy cape from7 reaches projector power switch angrily; Noa keeps projection cable out of grasp. No arrest yet.

Balloon 1: speech, Commander, upper right. EXACT text: 映像を止めろ！ . Columns RIGHT to LEFT: 映像を / 止めろ！.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso. Match commander in episode7 scene03 EXACTLY: short black hair greying at temples, neatly trimmed BLACK beard and moustache, navy cape, ornate SILVER/GOLD armor. Same mature face, no younger silver-haired substitute.
```

## 04-giant-arrives.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/06-giant.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Concealment guardian GREY stone purple core approaches projection tower behind stage and raises arm. Audience at tower base, Ren turns at low rumble. No falling result yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
```

## 05-tower-hit.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png", "../v5/art/06-giant.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Guardian fist smashes tower support, projection light falters, steel beam bends overhead; Noa drops under control booth safely. Only effect ドゴン .

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
```

## 06-two-choices.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Ren unarmored between damaged tower's exposed memory projector ABOVE and startled spectators BELOW leaning fall path. His gaze moves down from evidence to lives, scene geographically clear. No rescue yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
```

## v6-choice.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-10/art/07-choice.png", "sha256": "a14e34618011ad5585da63c6b4bda87d6f02f11b7f2b0c9c62b5ecc07389d8f5"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Close Ren grips red scarf and starts toward trapped spectators, blue eyes resolute, a real choice before full armor. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren unarmored determined face BETWEEN damaged tower/projector above and trapped spectators below. Same black cloth shirt, no armor until he runs.. Voice / balloon: low resolute ordinary oval.
ONLY speaker: Ren. EXACT text: 「証拠は写せる。」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Ren BARE fist releases scarf and opens toward endangered spectators; intact evidence projector higher at edge. Actual choice of lives before records, no saved group yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Ren unarmored determined face BETWEEN damaged tower/projector above and trapped spectators below. Same black cloth shirt, no armor until he runs.. Voice / balloon: low resolute ordinary oval.
ONLY speaker: Ren. EXACT text: 「人は戻せない。」 (render contents only).

```

## 08-run.png

retained prior adopted image_gen output

参照：["../v5/art/14-hero.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren launches toward spectators as basic black armor/cyan seams forms in motion, scarf streak follows path; no new speed form before episode12.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: ONLY established BASIC BLACK faceted armor with thin CYAN seams and CYAN star forms; no new speed form, white armor, gold armor, helmet or face mask.
```

## 09-catch-tower.png

retained prior adopted image_gen output

参照：["../v5/art/14-hero.png", "../production/references/mira.png"]

採用時の指示：

```text
Targeted edit to FIRST image: preserve Ren FULL BASIC BLACK faceted armor, CYAN seams/star, red scarf, BOTH hands holding the huge STONE tower crossbeam, both braced boots on intact stone ground, beam position/perspective, debris and all architecture. Replace ONLY the crouching Mira and silver-haired Rook immediately behind Ren at lower LEFT with the SAME ordinary mother and young boy from SECOND image: mother brown hair/blue eyes, BROWN hooded shawl over WHITE blouse; boy8 brown hair/blue eyes, OLIVE GREEN short sleeve shirt, brown breeches, brown boots. They are frightened free festival spectators sheltered UNDER the held beam, crouching with mother protecting son. Add two generic crouching spectators farther behind them if space permits, without covering Ren or beam. Mira and Rook are off camera helping evacuate the plaza and MUST NOT be under the beam in this image. No additional hero, no prisoners/bars, no words. High quality anime comic.
```

## v6-noa-copy.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-10/art/10-noa-copy.png", "sha256": "deb1ab5971d810d08b9fa346c703796b0375672a169717acf10eb209f08eea9d"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Noa under intact kiosk plugs memory crystal duplicate into SMALL separate shop relay, old main tower abandoned. Orange hair/goggles/blue overalls, no future citywide link form. Do NOT draw Ren anywhere in this frame. He remains OFF CAMERA in full black-cyan basic armor continuously holding the fallen beam up until every spectator is clear. No duplicate hero helping Noa/Mira here.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Noa determined face under SAME intact kiosk after MAIN tower damaged; daytime. Ren still holds beam offscreen.. Voice / balloon: ordinary practical rounded speech.
ONLY speaker: Noa. EXACT text: 「一つ消しても、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Noa orange gloves plug ONE duplicate memory crystal into SMALL independent shop relay. No advanced LINK-form gadget, no Ren in frame.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Noa determined face under SAME intact kiosk after MAIN tower damaged; daytime. Ren still holds beam offscreen.. Voice / balloon: ordinary practical rounded speech.
ONLY speaker: Noa. EXACT text: 「終わらない。」 (render contents only).

```

## 11-distributed.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png"]

採用時の指示：

```text
Edit ONLY the pictures INSIDE the three existing shop-mounted brass projection screens in the FIRST target image. The screens currently incorrectly show scenic floating palace city landscapes. Replace all THREE screen contents with the SAME copied evidence of living detained residents seen in the SECOND reference episode10 scene02: blue-tinted holographic still images of people being conveyed behind magical conduit partitions and people chained upright as targets. These are evidence recordings, not actual captives inside this street. Match the episode02 evidence imagery, clearly readable human silhouettes, iron shackles, strained living faces without graphic injury. NO skyline or floating castle postcard visible on any screen. Preserve the three separate attached shop screens, brass brackets and wires, warm festival plaza, Mira blonde blue-eyed white-blue-gold dress and Noa orange hair green eyes freckles head goggles blue overalls orange gloves looking at the broadcast. Keep all remaining pixels/content/composition/style as close as possible. Do NOT add Ren; he is continuously holding stone beam off camera. NO dialogue or extra text. Crisp anime webtoon rendering.

```

## v6-name-them.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-10/art/12-name-them.png", "sha256": "c0cd76d3a119b5ef8c0ac59b28b4b371a753cfdc24ba7eea28de88000094826b"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Mira speaks into simple brass relay microphone from safe street, copied roster in hand. Exact short dialogue preserves human names over numbers. Do NOT draw Ren anywhere in this frame. He remains OFF CAMERA in full black-cyan basic armor continuously holding the fallen beam up until every spectator is clear. No duplicate hero helping Noa/Mira here.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira face speaks into SAME brass relay microphone from safe street, copied roster held; not on damaged tower.. Voice / balloon: firm empathetic blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「十七人です。」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Copied roster in her fingers and listening street resident at edge; names abstract, no count changing. Ren remains supporting beam offscreen, no early release.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Mira face speaks into SAME brass relay microphone from safe street, copied roster held; not on damaged tower.. Voice / balloon: firm empathetic blue-grey capsule.
ONLY speaker: Mira. EXACT text: 「一人ずつ、ここにいます。」 (render contents only).

```

## 13-evacuation.png

retained prior adopted image_gen output

参照：["../v5/art/14-hero.png", "../production/references/mira.png", "../v5/art/a14-rejection.png", "art/09-catch-tower.png", "../episode-02/art/14-safe.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Spectators now walk OUT from under crossbeam along Mira-marked safe lane, Ren holds beam; Rook guides last small child green shirt to mother. Do not show final safe group before crossing.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Ren wears the established FULL BASIC BLACK faceted armor, thin CYAN seams, CYAN chest star, BOTH armored hands continuously supporting this SAME tower beam. Red scarf, exposed face and black hair. Both boots planted on broad intact STONE GROUND, knees braced, no balancing on railing. No teleporting between holds. Rook guides the same family from episode2: 8-year-old brown-haired blue-eyed boy in OLIVE GREEN short-sleeve shirt and brown breeches, mother in BROWN hooded shawl and WHITE blouse. The boy crosses toward mother; both must end safely outside beam path.
LOAD CONTINUITY: SAME thick STONE tower crossbeam as scene09; retain its cracked masonry texture and heavy rectangular section. No steel/wood substitute.
```

## 14-set-beam.png

retained prior adopted image_gen output

参照：["../v5/art/14-hero.png", "../production/references/mira.png", "art/09-catch-tower.png"]

採用時の指示：

```text
Edit the FIRST target image into the decisive END of lowering the SAME fallen stone tower crossbeam shown in second reference, after ALL spectators have escaped. This is one wide anime comic moment, no montage. Critical action change: the enormous thick stone crossbeam is NOW RESTING ON THE EMPTY PLAZA GROUND in the FOREGROUND at a LOW diagonal, one heavy chipped edge making firm visible ground contact with settling dust and small rubble. It MUST NOT remain above Ren's head or over any person. Show clear load bearing contact between stone block and flat stone plaza, no floating gap. Ren, messy BLACK hair BLUE eyes RED scarf, established BASIC BLACK faceted armor thin CYAN seams cyan chest STAR, crouches or kneels BESIDE the grounded beam, BOTH armored hands at waist/low chest height on its SIDE/upper edge, guiding the last inches until weight is settled. His feet/knee firmly on ground. Exhausted expression, armor begins subtle cyan flecks/cracks; no new form, no white/gold armor. Preserve material, carved ridge, cracks, massive crossbeam identity from second reference; it is not a wooden plank, metal carriage, statue or new building. Remaining plaza behind is EMPTY with same white fantasy city buildings blue-gold banners sunshine. No Mira/Rook/Noa/civilians under or beside beam, everyone evacuated OFF CAMERA. No dialogue/effects/labels. Crisp detailed cel shaded Japanese anime Webtoon, sensible fingers and heavy weight geometry. Keep wide 4:3 single panel with thin border, legible clear motion outcome. Stone is down and stable; Ren is no longer holding anything overhead.

```

## 15-first-clap.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: FIRST one ordinary adult woman in rescued audience claps cautiously while others stare in silence, Ren unarmored leaning on safe beam. No mass thunderous applause before first hand clap. Only effect パチ .

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
LOAD CONTINUITY: SAME thick STONE tower crossbeam as scene09; retain its cracked masonry texture and heavy rectangular section. No steel/wood substitute.
```

## 16-recognized.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../production/references/noa.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Broad crowd now applauds rescued exhausted Ren, Mira and Noa beside him; Ren hand to chest with surprised wet eyes, not boastful. Show concrete saved families facing him.

Balloon 1: thought, Ren thought, upper right. EXACT text: …届いたんだ。 . Columns RIGHT to LEFT: …届いたんだ。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
```

## v6-arrest.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-10/art/17-arrest.png", "sha256": "f37438c95f128cb0d82f65f41d42d5bc930e4e11be66e20080a1c0ffa26e4461"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Rook restrains commander's wrist with lawful metal cuffs beside copied evidence, commander alive uninjured. Rook carries no knight license; civil witnesses nearby, no revenge violence. Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso. Match commander in episode7 scene03 EXACTLY: short black hair greying at temples, neatly trimmed BLACK beard and moustache, navy cape, ornate SILVER/GOLD armor. Same mature face, no younger silver-haired substitute.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Rook resolved face in SAME safe DAY plaza after applause, no knight license, blue cape and silver armor.. Voice / balloon: quiet firm ordinary oval.
ONLY speaker: Rook. EXACT text: 「今度は、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Rook BLACK glove closes lawful cuff over SAME45 commander wrist beside copied evidence; commander ALIVE uninjured, no revenge violence.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: ONLY Rook resolved face in SAME safe DAY plaza after applause, no knight license, blue cape and silver armor.. Voice / balloon: quiet firm ordinary oval.
ONLY speaker: Rook. EXACT text: 「見ないふりをしない。」 (render contents only).

```

## 18-base.png

retained prior adopted image_gen output

参照：["../episode-03/art/03-fist.png", "../production/references/mira.png", "../v5/art/a14-rejection.png", "../production/references/noa.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Lower-city workshop transformed into modest official rescue base with SAME handmade plaque 救助隊 . Ren Mira Noa Rook share bread at workbench; Haru and survivors outside help repairs. Clear warm first-arc achievement.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Ren, if visible, is UNARMORED in ordinary BLACK short-sleeve FABRIC shirt with narrow brown straps, charcoal trousers, brown boots and red scarf; both forearms and hands BARE. No black gauntlets, no armored torso.
```

## 19-white-armor-cue.png

retained prior adopted image_gen output

参照：["../episode-08/art/02-portrait.png", "../episode-08/art/01-corridor.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Deep palace shadow, LIVING ancient hero back turned: faceted WHITE armor and GOLD star partly reflected in wall, adult short pale hair obscured face. No exact identity or name yet; quiet ominous contrast to happy base.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
FINAL CONTINUITY REQUIREMENT: Draw ONLY the living ancient white armored hero seen FROM BEHIND and palace architecture. NO Ren, NO Mira, NO Rook, NO Noa, no red scarf, no cyan chest star. Short pale hair, WHITE faceted armor with a GOLD star on its back or reflection. FACE fully hidden; name not revealed. No duplicate living hero in front.
```

## v6-close-gates.png

built-in image_gen

参照：[{"path": "examples/zero-break/episode-10/art/20-close-gates.png", "sha256": "eb1154bce3dfe446206cf8bd375dda21d725a81f0fa0ebd11da0273ccfb38700"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Massive palace gates all lowering toward shut stone, white armored silhouette far above, no protagonist trapped or killed. Ominous exact dialogue from unseen white hero. Draw ONLY the living ancient white armored hero seen FROM BEHIND and palace architecture. NO Ren, NO Mira, NO Rook, NO Noa, no red scarf, no cyan chest star. Short pale hair, WHITE faceted armor with a GOLD star on its back or reflection. FACE fully hidden; name not revealed. No duplicate living hero in front.

Panel 1, downward order. Frame: right-aligned90% width, medium framed speaker close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: Only palace WHITE-armored living unknown hero BACK silhouette high above lowering gates; no face, name or Ren.. Voice / balloon: cold unseen voice in strong angular rounded frame; tail exits toward unseen mouth, no thought dots.
ONLY speaker: Unknown. EXACT text: 「ゼロを、」 (render contents only).
Panel 2, downward order. Frame: left-aligned72% width, shallow silent detail/reaction insert. Reader understands: The listener or the relevant object holds the same scene while the words settle.. Visible camera subject / offscreen continuity: Massive SAME palace gates descend, last thin gap of daylight at bottom. No protagonist trapped or new plot outcome.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width LARGE borderless emotional close-up. Reader understands: The reader receives one part of the explanation, before a response.. Visible camera subject / offscreen continuity: Only palace WHITE-armored living unknown hero BACK silhouette high above lowering gates; no face, name or Ren.. Voice / balloon: cold unseen voice in strong angular rounded frame; tail exits toward unseen mouth, no thought dots.
ONLY speaker: Unknown. EXACT text: 「上げてはいけない。」 (render contents only).

```
