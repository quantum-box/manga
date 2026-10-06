# 第01話 — 採用原画の実行指示

全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・旧版保持を generation-log.json で区別。以前の実行記録は production/feedback-v6/baseline に保持。

## 01-memory.png

retained prior adopted image_gen output

参照：[]

採用時の指示：

```text
See ../production/feedback-v6/baseline/prompts-episode-01.md for the original executed prompt.
```

## v6-waking.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/02-arrival.png", "sha256": "a15849a76923d2ef7ae428d9d0c5d1ec1382a377b1c1d8f319d19268932509cf"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading, WHITE outer gutters; explicitly UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

Exact continuity/setting (not a request to put everything in every panel): Ren wakes seated on a stone stair in a white fantasy plaza and looks up at floating white towers, blue sky and hanging blue banners. Unarmored black short sleeves, charcoal trousers, crimson scarf, bare hands. Establish his confusion and the new world. Preserve the clear establishing view, large enough face.

Panel 1, downward order. Frame: right-aligned 80% width, medium-height framed close-up. Reader understands: Ren opens his eyes in an unfamiliar place.. Visible camera subject / offscreen continuity: ONLY seated Ren face, eyes opening; white stair and a blue banner establish the same landing.. Voice / balloon: bewildered thought, cloud and dots.
ONLY speaker: Ren thought. EXACT text: 「……ここ、どこだ。」 (render contents only).
Panel 2, downward order. Frame: large full-width BORDERLESS vertical upward view, enough height to understand geography. Reader understands: The place really floats in the sky.. Visible camera subject / offscreen continuity: His upward eyeline leads to floating white towers and islands; only location box EXACT 空都リュミエル, no other words.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: left-aligned90% width, medium-height framed face. Reader understands: He links this place to his last memory, without knowing why.. Visible camera subject / offscreen continuity: ONLY Ren seated shoulders/face, one bare hand touching his crimson scarf; same intact stairs. No corpse or child flashback.. Voice / balloon: uncertain thought, cloud with dots.
ONLY speaker: Ren thought. EXACT text: 「俺、事故に遭ったはずじゃ……。」 (render contents only).

```

## a01-footsteps.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x768.
Scene: Low close shot of Rook's silver armored boots stepping on intact white stone stairs. Blue cape edge and daylight shadow lead toward Ren offscreen. FIRST approach cue. No faces, crystal, or future events.


No dialogue, thoughts, narration, captions or readout text.
Draw once outside balloons, upright Japanese effect: カツ….
```

## a02-knight-arrives.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x1280.
Scene: SAME arrival stone stair plaza. Ren seated lower left; Rook walks toward him from upper right EIGHT METRES away. Show actual distance and descending stairs, both recognizable. Rook is not beside Ren yet. No crystal.


No dialogue, thoughts, narration, captions or readout text.
No sound-effect lettering.
```

## v6-greeting.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/a03-greeting.png", "sha256": "d35123d57fb388361074edd3438c91b914e7c164a8857857e0188075b6bf34b2"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading, WHITE outer gutters; explicitly UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

Exact continuity/setting (not a request to put everything in every panel): Rook now arrived ONE metre to right of still seated Ren. Rook bends slightly, offers a black-gloved hand, professionally reserved. Ren looks up and raises a BARE hand toward him, no touch yet. Faces and hands clear. No crystal.

Panel 1, downward order. Frame: right-aligned82% width, medium framed close. Reader understands: The approaching knight addresses seated Ren.. Visible camera subject / offscreen continuity: ONLY Rook face bent slightly down; Ren remains seated offscreen left. Same white stone stairs.. Voice / balloon: reserved ordinary thin-black oval.
ONLY speaker: Rook. EXACT text: 「立てるか？」 (render contents only).
Panel 2, downward order. Frame: left-aligned66% width, shallow hand insert. Reader understands: Help is offered, not yet accepted.. Visible camera subject / offscreen continuity: Rook black-gloved open hand extended toward Ren bare hand. No crystal, no contact yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: left-aligned90% width, medium close-up. Reader understands: Ren answers while still getting his bearings.. Visible camera subject / offscreen continuity: ONLY Ren seated face looking up right, same scarf and shirt.. Voice / balloon: quiet shaky spoken voice, continuous tail.
ONLY speaker: Ren. EXACT text: 「ああ……。」 (render contents only).
Panel 4, downward order. Frame: full-width tall framed movement. Reader understands: He asks his first question.. Visible camera subject / offscreen continuity: Ren bare hand takes Rook gloved hand and Ren rises a little; tight upper-body shot, not an unexplained new location.. Voice / balloon: ordinary questioning oval.
ONLY speaker: Ren. EXACT text: 「ここは？」 (render contents only).

```

## v6-rook-name.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/a03-greeting.png", "sha256": "d35123d57fb388361074edd3438c91b914e7c164a8857857e0188075b6bf34b2"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Immediately AFTER Rook helps seated Ren rise: both now STAND at same intact stair landing; they have not walked to the measuring station. Rook introduces his name and job. No Mira, crystal, armor or future0 result.

Panel 1, downward order. Frame: right-aligned92% width, medium framed speaker. Reader understands: The knight tells Ren who he is before explaining the country.. Visible camera subject / offscreen continuity: ONLY Rook face and silver armor/blue cape; immediately AFTER helping Ren stand, SAME intact white stair landing. Ren stands offscreen left.. Voice / balloon: reserved ordinary rounded speech.
ONLY speaker: Rook. EXACT text: 「私はルーク。この街の騎士だ。」 (render contents only).
Panel 2, downward order. Frame: full-width wide quiet shared location. Reader understands: Ren has accepted help and knows whose explanation he is hearing.. Visible camera subject / offscreen continuity: One standing Ren and one standing Rook on SAME stair landing, medium upper bodies, Ren small grateful nod. No crystal or future magic result.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## v6-orientation.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/a04-orientation.png", "sha256": "0c477f2e441d29e38b2f9a171b223e360bd4fdd4342346dea5598256c607f25d"}, {"path": "examples/zero-break/v5/art/a05-registration.png", "sha256": "baea0b39c1566147b39b11df58f5e5a03d0aef5f66b18f6bb833f6475d26e1b3"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Ren NOW STANDS on same landing beside Rook. Rook gestures toward floating white towers. Ren follows his gaze, stunned eyes and parted lips. Same city. Single medium scene of understanding the setting, no crystal or giant. Close conversation on stair landing with both standing. Rook RIGHT examines Ren's unfamiliar short black sleeve and red scarf, eyebrow raised, subtly points toward his clothes without touching. Ren LEFT confused, hand on scarf. No crystal yet.

Panel 1, downward order. Frame: right-aligned86% width, medium framed. Reader understands: Rook gives one fact about this country.. Visible camera subject / offscreen continuity: ONLY standing Rook face and pointing glove; Ren now stands beside him offscreen left.. Voice / balloon: matter-of-fact rounded speech.
ONLY speaker: Rook. EXACT text: 「ここは、空に浮かぶ国だ。」 (render contents only).
Panel 2, downward order. Frame: full-width wide borderless geographic view. Reader understands: Ren really looks at the impossible landscape.. Visible camera subject / offscreen continuity: White towers suspended beyond intact landing; lower corner shows only red scarf and Ren eye following them.. Voice / balloon: quiet astonished speech, soft outline.
ONLY speaker: Ren. EXACT text: 「空に……？」 (render contents only).
Panel 3, downward order. Frame: left-aligned78% width, shallow detail. Reader understands: The knight notices unfamiliar clothes.. Visible camera subject / offscreen continuity: Rook gloved finger gestures toward Ren black FABRIC sleeve/red scarf; no grabbing.. Voice / balloon: ordinary thin oval.
ONLY speaker: Rook. EXACT text: 「見慣れない服だな。」 (render contents only).
Panel 4, downward order. Frame: right-aligned83% width, medium framed. Reader understands: A new word is introduced separately.. Visible camera subject / offscreen continuity: ONLY Rook close face, calm guarded eyes; Ren remains offscreen left.. Voice / balloon: composed speech.
ONLY speaker: Rook. EXACT text: 「転生者か。」 (render contents only).
Panel 5, downward order. Frame: full-width large close-up. Reader understands: Ren has to process that word.. Visible camera subject / offscreen continuity: ONLY Ren face with widened blue eyes; scarf visible, SAME landing. No crystal or armor.. Voice / balloon: hesitant spoken voice, mildly wavering outline.
ONLY speaker: Ren. EXACT text: 「……転生？俺が？」 (render contents only).

```

## v6-instruction.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/a06-walk-to-station.png", "sha256": "74d2b63d8e64fde86d63ac9857dd756c8936e7e854ab7c08272da6c75258a54e"}, {"path": "examples/zero-break/v5/art/a07-instruction.png", "sha256": "db8d5ed1b133469d85040c94a9c9dc6a39f982ab9f80ad2afa06175bfac67523"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Rook leads Ren ON FOOT across SAME intact lower balcony plaza. Side/three-quarter view of ONE Ren and ONE Rook walking the same direction; knight half a pace ahead right points forward. Ahead is ornate pointed silver stone pedestal and large BLACK faceted crystal, identical design to reference2. Add a SMALL NARROW FLAT METAL readout INSET on pedestal front, totally BLANK. High bridge in background, cargo awnings below rail. No results, giant, blue power. Ren LEFT and Rook RIGHT beside SAME assessment crystal. Rook's BLACK GLOVED finger points to top of black crystal. Ren's BARE hands stay lowered, NO TOUCH yet. Crystal in foreground center bottom. Narrow flat inset readout front totally blank, neutral daylight reflections no emitted glow. Both faces and hands clear.

Panel 1, downward order. Frame: right-aligned90% width, medium framed. Reader understands: Rook names the procedure before walking.. Visible camera subject / offscreen continuity: ONLY Rook shoulders and pointing hand; same landing, Ren offscreen left.. Voice / balloon: calm explanatory rounded capsule.
ONLY speaker: Rook. EXACT text: 「異世界から来た者は、まず魔力を測る。」 (render contents only).
Panel 2, downward order. Frame: full-width broad geography and walking shot. Reader understands: Ren follows him physically.. Visible camera subject / offscreen continuity: One Rook half a pace ahead and one Ren walk toward distant SAME black crystal on SILVER gothic pedestal across intact plaza.. Voice / balloon: ordinary oval.
ONLY speaker: Rook. EXACT text: 「こっちだ。」 (render contents only).
Panel 3, downward order. Frame: left-aligned86% width, medium prop close-up. Reader understands: Ren reaches the apparatus but has not touched it.. Visible camera subject / offscreen continuity: Close BLACK crystal and Rook BLACK glove pointing at its top. Ren BARE hand lowered at edge. Readout blank.. Voice / balloon: ordinary instruction.
ONLY speaker: Rook. EXACT text: 「水晶に手を置け。」 (render contents only).
Panel 4, downward order. Frame: right-aligned92% width, medium-height framed reaction. Reader understands: The purpose of touching is explained.. Visible camera subject / offscreen continuity: ONLY Ren listening face; black crystal edge at bottom, bare hand still lowered. Rook stays offscreen right.. Voice / balloon: calm offscreen speech, tail exits toward Rook on right, no dots.
ONLY speaker: Rook offscreen. EXACT text: 「使える魔力の量がわかる。」 (render contents only).

```

## a08-hesitation.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png", "art/a06-walk-to-station.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x1280.
Scene: Close Ren unsure face, eyes between Rook offscreen and crystal bottom. His BARE RIGHT hand hovers FOUR centimetres ABOVE black crystal, tense fingers, NOT touched. Soft black sleeves and red scarf. Modest hopeful anxiety, no swagger. No readout result or blue glow.

Item 1: thought; speaker Ren thought; position upper left with dots to Ren hair.
Exact complete text: 俺にも、そんな力が……？
Columns RIGHT to LEFT: 1: 俺にも、 | 2: そんな力が | 3: ……？. Do NOT print numbers or labels.
Exactly 1 specified speech/thought/readout items.
No sound-effect lettering.
Reference3 locks the NEW assessment station established in the walking shot: the same dark black crystal, ornate pointed silver pedestal, SMALL NARROW FLAT METAL inset readout, and intact lower balcony. Do not copy its walking pose or captions. Keep the readout BLANK until the result shot. Lock scale and design; this device is NOT the hero power.
```

## a09-touch.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png", "art/a06-walk-to-station.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x768.
Scene: Extreme close-up: Ren's BARE RIGHT PALM makes FIRST contact on TOP of same black faceted crystal. Exactly five relaxed fingers, soft short black sleeve, red scarf blurred behind. Same ornate pointed silver pedestal bottom. Narrow flat inset readout still BLANK. Neutral white reflections no magic. Single contact moment, no faces, text or numbers.


No dialogue, thoughts, narration, captions or readout text.
No sound-effect lettering.
Reference3 locks the NEW assessment station established in the walking shot: the same dark black crystal, ornate pointed silver pedestal, SMALL NARROW FLAT METAL inset readout, and intact lower balcony. Do not copy its walking pose or captions. Keep the readout BLANK until the result shot. Lock scale and design; this device is NOT the hero power.
```

## v6-waiting.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/a10-waiting.png", "sha256": "5e03edd8ca82b6ce5a80d1c3f9e75cdc4361e3da850859ad50e4bf1ded316e85"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Ren LEFT and Rook RIGHT at same station AFTER touch. Ren's BARE RIGHT palm stays flat ON TOP of crystal. He looks to Rook, who patiently watches narrow flat inset readout BELOW crystal; display still blank. Crystal stays unlit. Faces, palm and apparatus visible. No disaster. Moment is WAITING, not a result.

Panel 1, downward order. Frame: left-aligned92% width, medium framed. Reader understands: Ren keeps his palm on the crystal and checks the procedure.. Visible camera subject / offscreen continuity: ONLY Ren face with same BARE RIGHT palm visible below on BLACK crystal. NO results or glowing power.. Voice / balloon: uncertain ordinary speech.
ONLY speaker: Ren. EXACT text: 「……これで、いいのか？」 (render contents only).
Panel 2, downward order. Frame: right-aligned80% width, medium framed. Reader understands: The knight tells him to wait.. Visible camera subject / offscreen continuity: ONLY Rook close face watching blank narrow metal inset readout; Ren offscreen left.. Voice / balloon: controlled ordinary oval.
ONLY speaker: Rook. EXACT text: 「そのまま、待て。」 (render contents only).
Panel 3, downward order. Frame: left-aligned68% width, shallow silent hand insert. Reader understands: A short real wait before the readout.. Visible camera subject / offscreen continuity: BARE palm resting still on BLACK crystal; empty readout partly visible, no0.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## a11-result.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png", "art/a06-walk-to-station.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x1280.
Scene: Close on SAME black faceted crystal and ornate pointed silver pedestal. Ren's BARE RIGHT hand stays on top and is visible. The SMALL NARROW FLAT METAL readout INSET into pedestal FRONT shows FIRST reading in clean pale ivory vertical lettering: RIGHT column 魔力量, LEFT column ０. Zero large at 360px. Instrument in scene, not floating caption or gold hologram. Crystal remains dark. No faces or other letters.

Item 1: system; speaker measurement device; position INSET readout on pedestal, not a floating box.
Exact complete text: 魔力量０
Columns RIGHT to LEFT: 1: 魔力量 | 2: ０. Do NOT print numbers or labels.
Exactly 1 specified speech/thought/readout items.
No sound-effect lettering.
Reference3 locks the NEW assessment station established in the walking shot: the same dark black crystal, ornate pointed silver pedestal, SMALL NARROW FLAT METAL inset readout, and intact lower balcony. Do not copy its walking pose or captions. Keep the readout BLANK until the result shot. Lock scale and design; this device is NOT the hero power.
```

## v6-confirmation.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/a12-confirmation.png", "sha256": "e3f6c4ad2eaaa1306f784104688a92235697aa517d5882edeb761a3451b2f56e"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Closer TWO faces at same station. Rook RIGHT looks down at result, brows disappointed. Ren LEFT eyes widen in quiet shock, BARE RIGHT palm STILL touches crystal below. Keep readout out of frame. No disaster, armor, magic or smile.

Panel 1, downward order. Frame: right-aligned84% width, medium framed. Reader understands: Rook reads the disappointing result.. Visible camera subject / offscreen continuity: ONLY Rook face looking down left, disappointed but quiet, Ren offscreen left. No new display.. Voice / balloon: cool ordinary thin oval.
ONLY speaker: Rook. EXACT text: 「魔力、ゼロ。」 (render contents only).
Panel 2, downward order. Frame: left-aligned69% width, very shallow eye insert. Reader understands: Ren hears before he answers.. Visible camera subject / offscreen continuity: ONLY Ren blue eyes, widening; BARE RIGHT hand still on crystal outside crop.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width large framed face. Reader understands: The word finally reaches him.. Visible camera subject / offscreen continuity: ONLY Ren face, red scarf, palm STILL touches crystal at bottom; same station.. Voice / balloon: small uncertain SPOKEN wavy speech tail, not thought dots.
ONLY speaker: Ren. EXACT text: 「……ゼロ？」 (render contents only).

```

## a13-stakes.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png", "art/a06-walk-to-station.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x1280.
Scene: Same station. Rook right explains coldly, head toward Ren. Ren left listens, now WITHDRAWN his BARE RIGHT hand from crystal, holds palm near chest in bafflement. Dark crystal below. Same intact city, no giant or blue power. Face and hand show disappointment.

Item 1: speech; speaker Rook; position upper right, tail to Rook.
Exact complete text: この国では、魔力がない者は戦えない。
Columns RIGHT to LEFT: 1: この国では、 | 2: 魔力がない | 3: 者は | 4: 戦えない。. Do NOT print numbers or labels.
Exactly 1 specified speech/thought/readout items.
No sound-effect lettering.
Reference3 locks the NEW assessment station established in the walking shot: the same dark black crystal, ornate pointed silver pedestal, SMALL NARROW FLAT METAL inset readout, and intact lower balcony. Do not copy its walking pose or captions. Keep the readout BLANK until the result shot. Lock scale and design; this device is NOT the hero power.
This moment is AFTER the zero result: any visible front readout must remain dark with ONE pale ivory ０ inside the SAME small HORIZONTAL plaque. It must not become blank again or change shape. You may frame the readout fully outside the picture. Preserve all faces, right bare hand, and Japanese dialogue.
```

## a14-rejection.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png", "art/a06-walk-to-station.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x1280.
Scene: Rook takes TWO steps AWAY from same crystal station along balcony; BLUE cape back in right middle, dismissive glance over shoulder toward Ren left foreground. Ren STANDING by crystal, shoulders slump, BARE hands lowered. Show separation. Same silver armor and black gloves. No crystal-hand touch or giant.

Item 1: speech; speaker Rook; position upper right with tail to Rook mouth.
Exact complete text: ハズレの転生者か。
Columns RIGHT to LEFT: 1: ハズレの | 2: 転生者か。. Do NOT print numbers or labels.
Exactly 1 specified speech/thought/readout items.
No sound-effect lettering.
Reference3 locks the NEW assessment station established in the walking shot: the same dark black crystal, ornate pointed silver pedestal, SMALL NARROW FLAT METAL inset readout, and intact lower balcony. Do not copy its walking pose or captions. Keep the readout BLANK until the result shot. Lock scale and design; this device is NOT the hero power.
This moment is AFTER the zero result: any visible front readout must remain dark with ONE pale ivory ０ inside the SAME small HORIZONTAL plaque. It must not become blank again or change shape. You may frame the readout fully outside the picture. Preserve all faces, right bare hand, and Japanese dialogue.
```

## a15-zero-reaction.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png", "art/a06-walk-to-station.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x1280.
Scene: Solitary medium close-up Ren at same station, Rook has LEFT. Ren looks at his own BARE RIGHT palm held low, brows drawn, quiet hurt and loss. Black short sleeves red scarf. Black crystal blurred behind. No heroic pose, magic or armor. Intact quiet city.

Item 1: thought; speaker Ren thought; position upper left dots ending at Ren head.
Exact complete text: ……ここでも、何もできないのか。
Columns RIGHT to LEFT: 1: ……ここでも、 | 2: 何もできない | 3: のか。. Do NOT print numbers or labels.
Exactly 1 specified speech/thought/readout items.
No sound-effect lettering.
Reference3 locks the NEW assessment station established in the walking shot: the same dark black crystal, ornate pointed silver pedestal, SMALL NARROW FLAT METAL inset readout, and intact lower balcony. Do not copy its walking pose or captions. Keep the readout BLANK until the result shot. Lock scale and design; this device is NOT the hero power.
This moment is AFTER the zero result: any visible front readout must remain dark with ONE pale ivory ０ inside the SAME small HORIZONTAL plaque. It must not become blank again or change shape. You may frame the readout fully outside the picture. Preserve all faces, right bare hand, and Japanese dialogue.
```

## a16-tremor.png

retained prior adopted image_gen output

参照：["../v4/art/02-arrival.png", "../v4/art/03-guide.png", "art/a06-walk-to-station.png"]

採用時の指示：

```text
Use case: illustration-story. Asset: finished anime Webtoon art WITH integrated Japanese upright vertical lettering.
Reference1: Ren identity and intact arrival stair/plaza. Reference2: Rook identity, black crystal and silver pedestal design. Do NOT copy their captions or poses and do NOT skip ahead to measurement.
Ren: adult19 black spiky hair, blue eyes, crimson scarf, soft BLACK SHORT-SLEEVE shirt with narrow brown straps, charcoal trousers, ordinary dark boots, BARE hands. Absolutely no armor, glowing star or blue power. Rook: adult22 silver hair blue eyes, silver engraved armor and BLUE cape, BLACK leather gloves, silver armored boots.
Same white floating city, sunshine, blue/gold banners. No other major characters. High-quality Japanese anime, crisp expressive faces and cel shaded detail, same visual style. Correct hands. ONE moment, not montage, grid or duplicated sequence.
Japanese: upright glyphs TOP TO BOTTOM, columns RIGHT TO LEFT, never sideways. Exact wording and punctuation only. Bold manga gothic, actual glyphs64–74px at1024px art width, readable at360px. Reshape balloons rather than shrink text. White smooth speech balloons with tails toward correct mouths, thought clouds with dots to Ren. No labels/English/watermark. Do not cover faces, hands or crystal. Clean thin dark comic outline. Varied close shots and full scenes, avoid giant unused margins.

Preferred output aspect 1024x768.
Scene: Low close shot of Ren's ordinary dark BOOT and charcoal cuff on SAME white stone balcony floor. Red scarf edge above. Small loose pebbles and dust JOLT at first distant tremor. Intact floor. No giant, princess, crack, falling figure or later destruction. Short horizontal insert before guardian reveal.


No dialogue, thoughts, narration, captions or readout text.
Draw once outside balloons, upright Japanese effect: ズ……ン。.
Reference3 locks the NEW assessment station established in the walking shot: the same dark black crystal, ornate pointed silver pedestal, SMALL NARROW FLAT METAL inset readout, and intact lower balcony. Do not copy its walking pose or captions. Keep the readout BLANK until the result shot. Lock scale and design; this device is NOT the hero power.
```

## v6-danger-geography.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/v6-danger.png", "sha256": "8c573ede762a2411ce912bc08a86d23f7cea8730332ed256c7595536d5404735"}, {"path": "examples/zero-break/v5/art/02-arrival.png", "sha256": "a15849a76923d2ef7ae428d9d0c5d1ec1382a377b1c1d8f319d19268932509cf"}]

元の生成指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): The SAME giant black stone guardian, armored stone limbs, violet fissures and a violet diamond-shaped chest core, goes berserk and breaks a high stone bridge. Princess Mira small but identifiable ON bridge, before falling. Establish high bridge above a lower balcony (Ren's assessment level) above a broad cargo canvas awning and soft cargo on a lower plaza. Two warning voices from small background guards or offscreen; no extra main characters. Giant fills upper background.

Panel 1, downward order. Frame: right-aligned86% width, medium framed warning. Reader understands: The vibration comes from a runaway guardian.. Visible camera subject / offscreen continuity: Distant warning guard shouting from lower plaza, looking up; Ren offscreen near measuring station.. Voice / balloon: urgent SHOUT, bold jagged outer edge.
ONLY speaker: warning guard A. EXACT text: 「警備巨兵が暴走した！」 (render contents only).
Panel 2, downward order. Frame: full-width LARGE tall borderless geographic view. Reader understands: Show the full dangerous spatial relationship BEFORE anybody falls.. Visible camera subject / offscreen continuity: Large continuous view: SAME black stone guardian violet diamond chest core beside HIGH stone bridge, Mira on bridge, Ren much LOWER balcony, canvas cargo awning BELOW Ren. Violet cracks only on guardian. Bridge beginning to crack, Mira still on bridge.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: left-aligned90% width, medium framed shout. Reader understands: The rescue target is identified.. Visible camera subject / offscreen continuity: SECOND warning guard face only, pointing up beyond top; Mira is NOT falling in this strip yet.. Voice / balloon: urgent bold jagged shout.
ONLY speaker: warning guard B. EXACT text: 「姫様が、橋にいる！」 (render contents only).

```

採用時の指示：

```text
Edit the FIRST image, preserving its THREE panel sequence, both shouting guards and their exact Japanese balloons completely. Change ONLY the MIDDLE large borderless geography image. It must clearly show THREE vertically separated levels: (1) Mira remains ON the cracking HIGH bridge at upper-right, not falling yet; (2) add a LOWER intact white STONE BALCONY sticking from the left wall at middle-left, significantly BELOW Mira's bridge; ONE unarmored Ren from image2 stands ON that lower balcony, BLACK fabric short-sleeve shirt, red scarf, messy black hair and blue eyes, both BARE hands, looking up to Mira. Show his whole upper body and one boot on stone so the balcony is unmistakable, not inside a tent. (3) keep the tan cargo canvas AWNING BELOW Ren's balcony with soft cargo beneath. Visible empty-air fall path from Mira, past Ren's lower balcony, down to awning. The giant black stone guardian and violet diamond chest core stay exactly the same. Do not put Ren on Mira's bridge, the ground, the canvas or in armor. Do not add lettering, future core power, any additional Ren or new event. Keep the FIRST and THIRD frames and balloon text pixel-consistent as much as possible. This is a geography clarification BEFORE fall, not a second rescue scene.
```

## 07-fall.png

retained prior adopted image_gen output

参照：[]

採用時の指示：

```text
See ../production/feedback-v6/baseline/prompts-episode-01.md for the original executed prompt.
```

## 08-leap.png

retained prior adopted image_gen output

参照：[]

採用時の指示：

```text
See ../production/feedback-v6/baseline/prompts-episode-01.md for the original executed prompt.
```

## v6-catch.png

reused skill reference (original built-in image_gen)

参照：[{"path": "skills/webtoon/references/zero-break/balloon-shout.png", "sha256": "b1e3efc1a8356b4b72005066acc515d7948c8ccafe10f0ccc7deb92a71fa419b"}]

採用時の指示：

```text
Use case: precise-object-edit / emphatic speech-balloon outline.
Image1 is the EXACT target: Ren catching Mira in midair. Image2 is a PHOTO supplied ONLY as a reference for the DENSE thick outward jagged/brush rim on the loud balloon. Do not copy its dialogue, characters, photo or layout.
Change ONLY Ren's existing shout balloon at upper right. Preserve all artwork, faces, bare hands, the supported Mira, clothing, red scarf, setting, framing and composition. Same roughly 4:5 portrait aspect. Keep the exact Japanese つかまって！ in ONE upright top-to-bottom vertical column, large legible printed manga gothic.
Replace its thin simple starburst with an emphatic white shout balloon surrounded by a bold dark charcoal dense outward tapered jagged/brush rim, like stressed loud comic speech. Variation of thick and thin strokes around the perimeter, roughly 12-20px visual rim at 1024px-wide art, WHITE inner area and generous text inset. A clear pointed sharp speech tail connects toward REN'S OPEN MOUTH, no dots. The outline communicates a loud urgent safety instruction during a rescue, not a villain aura or interior thought.
Fit the rim into the existing balloon area; do not cover hair, face or hand, and do not enlarge it over Mira. Avoid glow, red fill, blood, extra text, labels, new balloons or watermark. The original black panel frame stays unchanged. Everything outside this balloon is an invariant.

```

## 10-landing.png

retained prior adopted image_gen output

参照：[]

採用時の指示：

```text
See ../production/feedback-v6/baseline/prompts-episode-01.md for the original executed prompt.
```

## v6-safe-01.png

reused skill reference (original built-in image_gen)

参照：[{"path": "skills/webtoon/references/zero-break/balloons-01.png", "sha256": "647470d3b13e82694c7373f125057c20713db171024a87722f6c52c8cffc4e44"}]

採用時の指示：

```text
Use case: precise-object-edit / Japanese speech-balloon contour revision.
Input image1 is the EXACT edit target. Input image2 is a user-provided PHOTO of example balloon outlines only: use it solely to understand how thin colored contours and expressive thick rims vary by vocal intent. Do not reproduce its words, characters, screen, photograph or layout.
Change ONLY the specified speech-balloon contours, line weight/color and tail design in image1. Preserve ALL existing manga artwork, frame widths/heights/positions, white gutters, borderless portions, character faces and anatomy, clothes, scene lighting, expressions and Japanese dialogue. Maintain original tall 3:1 aspect. Do NOT recompose, crop, zoom, reorder panels or add any speech to silent panels.
Text remains exact, LARGE upright Japanese, top-to-bottom columns and RIGHT-to-LEFT column order, same legibility and placements. Keep generous white inner padding and black printed manga gothic. Tails connect to correct actual speaker; keep faces and hands unobscured. No extra symbols, hearts, captions, labels, English or watermark. Distinguish quiet spoken voice with a CONNECTED pointed/curved tail from thought with dots. No thought dots here: EVERY existing line in this target is SPOKEN. Do not add a shout effect to a calm scene.
Panel1 safety establishing view: leave completely unchanged, no balloons.
Panel2 Mira gratitude: exact ありがとう。 Replace the generic oval with a softly organic rounded contour, 2-3 gentle uneven curves but NOT a thought cloud. Fine subdued blue-gray outline, slender gently curved CONTINUOUS SPEECH TAIL pointing into Mira's mouth. Warm and tender normal voice; not a jagged shout. Shape must visibly differ from a perfect ellipse while remaining quiet and readable.
Panel3 eye reaction: leave completely unchanged, silent, no new balloon.
Panel4 Mira introduction: exact 私はミラ。 Replace the oval with a tall clean ROUNDED-RECTANGLE/rounded capsule, restrained slightly stronger same blue-gray outline, a small tapering pointed tail toward Mira mouth. Formal composed self-introduction, corners generously rounded. It must visibly differ from panel2 organic gratitude. Preserve her face, hand and exact panel dimensions. No electronic UI, filled colored box or thought dots.

```

## v6-safe-02.png

reused skill reference (original built-in image_gen)

参照：[{"path": "skills/webtoon/references/zero-break/balloons-02.png", "sha256": "3a01d48eb489e7e615e481d489b13cb60ce907b549a8422997b256f4d7c071c9"}]

採用時の指示：

```text
Use case: precise-object-edit / Japanese speech-balloon contour revision.
Input image1 is the EXACT edit target. Input image2 is a user-provided PHOTO of example balloon outlines only: use it solely to understand how thin colored contours and expressive thick rims vary by vocal intent. Do not reproduce its words, characters, screen, photograph or layout.
Change ONLY the specified speech-balloon contours, line weight/color and tail design in image1. Preserve ALL existing manga artwork, frame widths/heights/positions, white gutters, borderless portions, character faces and anatomy, clothes, scene lighting, expressions and Japanese dialogue. Maintain original tall 3:1 aspect. Do NOT recompose, crop, zoom, reorder panels or add any speech to silent panels.
Text remains exact, LARGE upright Japanese, top-to-bottom columns and RIGHT-to-LEFT column order, same legibility and placements. Keep generous white inner padding and black printed manga gothic. Tails connect to correct actual speaker; keep faces and hands unobscured. No extra symbols, hearts, captions, labels, English or watermark. Distinguish quiet spoken voice with a CONNECTED pointed/curved tail from thought with dots. No thought dots here: EVERY existing line in this target is SPOKEN. Do not add a shout effect to a calm scene.
Panel1 cropped Mira hand information: exact この国の王女よ。 Two columns RIGHT TO LEFT: この国の | 王女よ。 Use a clean tall rounded-rectangle/rounded capsule, fine subdued blue-gray outline matching Mira's composed self-introduction. Small tapered tail toward her OFFSCREEN MOUTH ABOVE RIGHT, never toward the jewel or hand. This is spoken dialogue, no thought dots and no electronic UI.
Panel2 Ren eye reaction: unchanged, SILENT, no new balloon.
Panel3 Ren introduction: exact レンだ。 Keep a simple ordinary upright oval, restrained dark charcoal line and short direct speech tail toward Ren mouth. Plain steady voice. Same legible text size.
Panel4 borderless Ren relieved response: exact 無事なら、それで。 Two columns RIGHT TO LEFT: 無事なら、 | それで。 Replace generic round ellipse with a slightly elongated SOFTLY WAVERING outline, irregular but closed fine charcoal line, thinner than his normal speech; connected small weak wavering speech tail points toward Ren mouth. Audible tired breath after rescue, not fear, crying, shouting or interior thought. No dotted tail, no fluffy thought cloud, no speech without tail. Preserve the LARGE borderless last portrait exactly. The difference should communicate an exhausted soft voice, not random decoration.

```

## v6-approach.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/12-approach.png", "sha256": "db367919c758c5797eaa9f3626408e06025f4cdb815ab24179433b41b7aef8c1"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): SAME black stone guardian with violet diamond chest core and violet cracks now approaches on the lower SOLID plaza. Ren still unarmored black short sleeves and red scarf, BARE hands out to shield standing Mira behind him. Torn canvas and cargo remain behind them. Giant, both people and ground show clear depth. Ren looks alarmed then resolute, no armor/glow.

Panel 1, downward order. Frame: full-width medium framed shared location. Reader understands: Ren stands up after the quiet rescue conversation; the same guardian approaches.. Visible camera subject / offscreen continuity: Ren rising from kneeling on solid lower cargo plaza, Mira standing safely right; torn canvas/rope gives same-location marker. SAME black guardian with VIOLET DIAMOND core is clearly visible approaching in distant upper-right background on the SOLID lower plaza, not the high bridge. No new crest or power.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: left-aligned84% width, medium close. Reader understands: The same danger has followed them down.. Visible camera subject / offscreen continuity: ONLY Ren tight face looking past Mira at offscreen approaching SAME guardian, still unarmored.. Voice / balloon: worried cloud thought with dots.
ONLY speaker: Ren thought. EXACT text: 「まだ、来るのか。」 (render contents only).
Panel 3, downward order. Frame: right-aligned92% width, medium framed. Reader understands: He puts Mira behind him.. Visible camera subject / offscreen continuity: Ren BARE open hand directs Mira back toward cargo wall; ordinary shirt, no armor yet. Focus only gesture and her safe backward step.. Voice / balloon: firm ordinary speech.
ONLY speaker: Ren. EXACT text: 「ミラ、下がって。」 (render contents only).
Panel 4, downward order. Frame: full-width large borderless emotional close. Reader understands: His choice comes before the power.. Visible camera subject / offscreen continuity: ONLY Ren large determined face/chest, soft shirt and red scarf, Mira safely offscreen behind; no visible blue star or armor yet.. Voice / balloon: resolute rounded oval, no shout decoration.
ONLY speaker: Ren. EXACT text: 「今度は俺が止める。」 (render contents only).

```

## v6-core.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/13-core.png", "sha256": "39c4515e03a3799e1fa6a21f26f96b5c1e9fbc2f04032bb5412d8f20f694834e"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): A close shot of Ren's BARE hand and his still SOFT BLACK SHIRT at the chest as a cyan star-like core first glows through the fabric. Not full armor; no transformed silhouette anywhere. Dark blue mood, cyan illumination. One small white vertical thought balloon and two vertical rectangular cyan system notices integrated in sequence. Preserve hand anatomy and shirt. System notices are opaque dark cyan rectangles with readable pale cyan upright Japanese lettering, not a speech tail.

Panel 1, downward order. Frame: full-width medium framed prop close. Reader understands: A strange light appears in fabric for the first time.. Visible camera subject / offscreen continuity: Close BARE hand at still-soft BLACK shirt chest as first tiny CYAN star glows through cloth. No full armor silhouette. Dark navy scene.. Voice / balloon: cloud and thought dots.
ONLY speaker: Ren thought. EXACT text: 「これは……？」 (render contents only).
Panel 2, downward order. Frame: right-aligned94% width, shallow functional system frame. Reader understands: The system reports the cause before the equipment name.. Visible camera subject / offscreen continuity: Cyan translucent functional rectangle in dark background; small edge of shirt, no armored limbs. EXACT system words in upright Japanese: 救命行動を確認。救済核、起動。. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: full-width broad framed dark system view. Reader understands: The armor name appears separately, but the body reveal waits below.. Visible camera subject / offscreen continuity: CYAN system label only in plain functional frame: EXACT 装甲名：ゼロ・ブレイク. Soft shirt silhouette only, no transformed body or hands.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.

```

## 14-hero.png

retained prior adopted image_gen output

参照：[]

採用時の指示：

```text
See ../production/feedback-v6/baseline/prompts-episode-01.md for the original executed prompt.
```

## 15-punch.png

retained prior adopted image_gen output

参照：[]

採用時の指示：

```text
See ../production/feedback-v6/baseline/prompts-episode-01.md for the original executed prompt.
```

## v6-relief.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/16-relief.png", "sha256": "ee18f68d4ad0ce7e6ad638fbe3747c2b21f75bce7bcf17f938d60c10b84246df"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): On the same safe solid plaza AFTER the giant stopped, Ren in black armor and red scarf and Mira in white/blue/gold dress smile in relief. Both stand safely, gentle eye contact. Broken stone in background, not an attacking giant. Ren armor includes cyan star core and armored gloves. Two vertical speech balloons arranged as Mira first then Ren.

Panel 1, downward order. Frame: right-aligned87% width, medium framed. Reader understands: Mira looks at the stopped guardian and living Ren.. Visible camera subject / offscreen continuity: Mira face alone, safe lower solid plaza, violet-black wreckage blurred; Ren STILL basic black armor offscreen left.. Voice / balloon: warm questioning soft blue-grey outline.
ONLY speaker: Mira. EXACT text: 「あなた、本当に魔力ゼロなの？」 (render contents only).
Panel 2, downward order. Frame: left-aligned82% width, medium close. Reader understands: Ren gives a short answer.. Visible camera subject / offscreen continuity: Ren armored shoulders and relieved face, red scarf.. Voice / balloon: gentle ordinary speech.
ONLY speaker: Ren. EXACT text: 「みたいだ。」 (render contents only).
Panel 3, downward order. Frame: left-aligned68% width, shallow silent hand insert. Reader understands: He takes in that somebody really is safe.. Visible camera subject / offscreen continuity: ONLY Ren black armored hand relaxes from a fist; SAME wreckage, no crest or new person.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 4, downward order. Frame: full-width large BORDERLESS emotional close. Reader understands: His relief is bigger than the numerical verdict.. Visible camera subject / offscreen continuity: ONLY Ren wide relieved face, slightly wet eyes, blue chest star and red scarf; Mira safely offscreen right.. Voice / balloon: breathless soft wavering thin contour.
ONLY speaker: Ren. EXACT text: 「けど、役立たずじゃなかった。」 (render contents only).

```

## v6-fragment.png

built-in image_gen

参照：[{"path": "examples/zero-break/v5/art/17-fragment.png", "sha256": "1cff91216d59187b144db2b5dbbde5670350708845c0199901a9d7a728d796b2"}, {"path": "skills/webtoon/references/zero-break/varied-01.png", "sha256": "207182b5e679ed4ec4b42761adc149f4ad98039d823ed903cb2a1a6f5319b68e"}]

採用時の指示：

```text
Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.

The LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.
Exact continuity/setting (not a request to put everything in every panel): Macro shot of Ren's BLACK ARMORED GLOVE holding a purple-black broken guardian core fragment with an UNMISTAKABLE SMALL CROWN CREST engraved on it. This is FIRST crown-crest reveal. White city ground out of focus. Mira speaks from offscreen right and Ren replies from offscreen left; balloon tails point toward their offscreen positions, never pretend the stone speaks. Keep the entire glove/thumb, fragment and crown visible. Single clue close-up.

Panel 1, downward order. Frame: left-aligned78% width, shallow hand insert. Reader understands: Ren lifts a single piece from the defeated guardian.. Visible camera subject / offscreen continuity: BLACK armored glove picks up SAME violet-black core shard from safe plaza, crown side turned away, NO crest visible yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 2, downward order. Frame: full-width medium framed reveal. Reader understands: The mark is shown FIRST HERE.. Visible camera subject / offscreen continuity: Macro same single shard in black glove with unmistakable SMALL CROWN engraved on violet-black stone. No workshop number on reverse yet.. Voice / balloon: 無言.
SILENT: no balloons or text unless an exact prop inscription is explicitly specified.
Panel 3, downward order. Frame: right-aligned90% width, medium-height framed. Reader understands: Mira recognizes the clue.. Visible camera subject / offscreen continuity: ONLY Mira concerned face looking at shard offscreen left, not smiling; same plaza.. Voice / balloon: serious composed blue-grey rounded capsule.
ONLY speaker: Mira. EXACT text: 「その紋章……王家の工房のものよ。」 (render contents only).
Panel 4, downward order. Frame: full-width large close-up. Reader understands: Ren asks what the clue means, without naming the later enemy.. Visible camera subject / offscreen continuity: ONLY Ren basic armored shoulders/red scarf and worried face facing Mira offscreen right.. Voice / balloon: quiet troubled ordinary oval.
ONLY speaker: Ren. EXACT text: 「じゃあ、なんで俺たちを襲った？」 (render contents only).

```
