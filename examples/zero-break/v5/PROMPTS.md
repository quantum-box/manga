# 第01話 — 採用原画の実行指示

全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・採用原画の保持を generation-log.json で区別。以前の実行記録は Git の履歴で管理。

この話の追加改稿：既存11素材の効果音編集・3素材の装着過程追加。元画像・修正前画像・実行指示は production/episode-01-sfx に保持。

その後のコマ割り改稿：4素材を横並び・斜め枠へ再構成。読順・元画像・指示は production/episode-01-layout に保持。

## sfx-01-memory.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/01-memory.png", "sha256": "76769d9ab0904a5d0e0fd061878b12b554a064fd845b79e37c0bf73eccdc3c65"}]

元の生成指示：

```text
See the preserved adopted edition prompt in ../baseline/PROMPTS.md.
```

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 full-color Japanese Webtoon artwork. Input image is the EXACT EDIT TARGET. Add or revise only the specified integrated raster Japanese sound-effect lettering and the tiny related motion accents explicitly allowed below. Keep the original canvas aspect ratio, panel arrangement, gutters, cropping, composition, camera, every character identity, anatomy, costume, prop, background, pose, expression, exact dialogue and speech/thought balloons unchanged. Preserve vertical Japanese dialogue, upright glyphs and right-to-left column reading. Do NOT redraw or reinterpret the scene. Sounds sit directly in the picture outside dialogue balloons and support the pictured cause/action. Sound lettering may angle with motion; all Japanese words must be spelled exactly. Ensure the added effect reads at 360px phone width, but protect faces, hands, existing text and narrative clues. No English, added dialogue, watermark, captions, new people, panels or premature reveals.

TARGETED EDIT:
Add EXACT ザァァ… once in slender slightly wavering cool pale-blue Japanese hand-lettered rain effect, with subtle navy shadow for legibility, vertically down the open lower-right wet-road area. Its gentle scale and rhythm should establish rain before the scene changes, noticeably quieter than later combat. Preserve the entire reaching bare hand, crimson scarf and the exact narration box. Do not add crash sound, vehicle contact, an injured person or extra story information.

Verbatim new sound lettering: ザァァ…
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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png"]

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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png"]

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

## layout-greeting.png

built-in image_gen panel layout recomposition

参照：[{"path": "examples/zero-break/v5/art/sfx-v6-greeting.png", "sha256": "fad0bef74ce69d0dc5744975b5af885eebc9416872908f0e0e22ef67f90e1835"}]

元の生成指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 Japanese full-color Webtoon artwork. Input is the EXACT EDIT TARGET. Add ONLY specified integrated raster Japanese sound lettering and tiny motion accents. Preserve canvas dimensions/aspect ratio, panel arrangement and gutters, faces, anatomy, hands, poses, clothes, props, setting, every existing Japanese word and speech/thought balloon. Preserve upright vertical dialogue and all reading order. Sound lettering outside balloons may angle with the physical motion, but must be exact and legible at 360px display width. Protect the pictured cause/action, faces, hands and text. No added dialogue, English, panels, powers, armor, watermark, later reveal or newly invented action.

In panel 2 (Rook offers his black-gloved hand), add small thin スッ beside the open wrist, without covering either hand. In the last panel where Ren's bare hand takes Rook's glove, add medium rounded ギュッ alongside the joined hands, keeping fingers entirely clear. The two sounds should feel like a quiet offering followed by a firm accepting grip; no effects in the face-dialogue panels.
Exact new sound words: スッ / ギュッ
```

採用時の指示：

```text
Use case: illustration-story / existing Japanese Webtoon panel-layout recomposition. The input is the adopted artwork for THIS scene: preserve its exact story events, identities, costume, props, location, speaker, all Japanese dialogue, all sound words, and causal reading order. RE-DRAW the panel arrangement as specified below; do not preserve the old simple vertical stack. Full-color polished anime/cel shading matching the input. White page, thin black frames, clean white gutters. Japanese dialogue is LARGE printed gothic with UPRIGHT glyphs, top-to-bottom and right-to-left columns, target glyph height65-75px on a1024px-wide canvas so it reads at360px width. Never shrink lettering to fit a small frame: use true close-ups and short text. Do not rotate Japanese text even inside angled frames. Speech tails point to the correct actual mouth; thought uses dots toward the head. Sound lettering stays outside dialogue balloons and near its physical cause. Protect faces, hands and all existing exact words. No captions, panel numbers, arrows, English, watermark, duplicate people within one panel, new events, advance reveal, or additional dialogue. READ ORDER for a row is RIGHT panel then LEFT panel; rows proceed TOP to BOTTOM. The output must contain actual side-by-side or angled frames where requested, not just images whose subjects look sideways. Each small panel is a newly composed detail/face crop, not a compressed whole scene.

SPECIFIC LAYOUT AND EXACT CONTENT:
Canvas1024x2304 approximately. EXACTLY FOUR panels in THREE rows. Top row/full width (~28% height): Rook silver short hair, blue eyes, silver gold-detailed armor, royal-blue cape bends toward seated Ren and says EXACT 立てるか？ in thin ordinary oval. Middle row (~24% height) has TWO DISTINCT SIDE-BY-SIDE panels with a24px white vertical gutter: RIGHT panel (~46% canvas width) macro of Rook's black-gloved open hand offered toward Ren's approaching BARE hand, NOT touching yet, exact small スッ near wrist; LEFT panel (~50% width) CLOSE Ren's black-haired blue-eyed face looking UP RIGHT toward offscreen Rook, black soft shirt/red scarf, EXACT quiet spoken ああ……。 with continuous tail to Ren's mouth. Bottom/full-width taller row (~44% height): Ren's BARE hand firmly accepts the BLACK glove and he rises a little, same white stone steps and blue/gold flags, EXACT spoken ここは？ near Ren with tail to his mouth, exact ギュッ beside joined hands. Ren remains unarmored, no core, no crystal. Preserve hands as two distinct anatomically normal hands and keep text clear of grip. Never stack middle-right and middle-left as separate full-width rows.
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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png", "art/a06-walk-to-station.png"]

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

## sfx-a09-touch.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/a09-touch.png", "sha256": "87293897433c808cab7f97eadda236dd974c552c35cc450d23af8924499950c5"}]

元の生成指示：

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

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 Japanese full-color Webtoon artwork. Input is the EXACT EDIT TARGET. Add ONLY specified integrated raster Japanese sound lettering and tiny motion accents. Preserve canvas dimensions/aspect ratio, panel arrangement and gutters, faces, anatomy, hands, poses, clothes, props, setting, every existing Japanese word and speech/thought balloon. Preserve upright vertical dialogue and all reading order. Sound lettering outside balloons may angle with the physical motion, but must be exact and legible at 360px display width. Protect the pictured cause/action, faces, hands and text. No added dialogue, English, panels, powers, armor, watermark, later reveal or newly invented action.

Add ぺた once in small soft rounded dark lettering with a clean narrow white border beside the hand-crystal contact, in the open area just to the right of the fingertips. This is a quiet bare palm touching a smooth crystal, not an impact. No light burst, magic energy, vibration or readout yet. Keep the full hand/fingers, crystal facets and blank display visible.
Exact new sound words: ぺた
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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png", "art/a06-walk-to-station.png"]

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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png", "art/a06-walk-to-station.png"]

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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png", "art/a06-walk-to-station.png"]

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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png", "art/a06-walk-to-station.png"]

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

参照：["../production/references/02-arrival.png", "../production/references/03-guide.png", "art/a06-walk-to-station.png"]

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

## sfx-v6-danger-geography.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/v6-danger-geography.png", "sha256": "641bbe8bb4d91f98d85de78289ab9d9e0a015fa0066218ce7fd6b964c4f6a8a4"}]

元の生成指示：

```text
Edit the FIRST image, preserving its THREE panel sequence, both shouting guards and their exact Japanese balloons completely. Change ONLY the MIDDLE large borderless geography image. It must clearly show THREE vertically separated levels: (1) Mira remains ON the cracking HIGH bridge at upper-right, not falling yet; (2) add a LOWER intact white STONE BALCONY sticking from the left wall at middle-left, significantly BELOW Mira's bridge; ONE unarmored Ren from image2 stands ON that lower balcony, BLACK fabric short-sleeve shirt, red scarf, messy black hair and blue eyes, both BARE hands, looking up to Mira. Show his whole upper body and one boot on stone so the balcony is unmistakable, not inside a tent. (3) keep the tan cargo canvas AWNING BELOW Ren's balcony with soft cargo beneath. Visible empty-air fall path from Mira, past Ren's lower balcony, down to awning. The giant black stone guardian and violet diamond chest core stay exactly the same. Do not put Ren on Mira's bridge, the ground, the canvas or in armor. Do not add lettering, future core power, any additional Ren or new event. Keep the FIRST and THIRD frames and balloon text pixel-consistent as much as possible. This is a geography clarification BEFORE fall, not a second rescue scene.
```

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 full-color Japanese Webtoon artwork. Input image is the EXACT EDIT TARGET. Add or revise only the specified integrated raster Japanese sound-effect lettering and the tiny related motion accents explicitly allowed below. Keep the original canvas aspect ratio, panel arrangement, gutters, cropping, composition, camera, every character identity, anatomy, costume, prop, background, pose, expression, exact dialogue and speech/thought balloons unchanged. Preserve vertical Japanese dialogue, upright glyphs and right-to-left column reading. Do NOT redraw or reinterpret the scene. Sounds sit directly in the picture outside dialogue balloons and support the pictured cause/action. Sound lettering may angle with motion; all Japanese words must be spelled exactly. Ensure the added effect reads at 360px phone width, but protect faces, hands, existing text and narrative clues. No English, added dialogue, watermark, captions, new people, panels or premature reveals.

TARGETED EDIT:
In the large middle geographical panel ONLY, add ゴゴゴ… as heavy dark-violet/black outlined, slightly irregular stone-rumble lettering along the upper-left sky beside the guardian shoulder. Add バキバキッ！ in sharp fractured black lettering with white outline next to the breaking bridge, farther down the middle-right, following the falling masonry. Both sound effects must be large enough at 360px width, while preserving an uninterrupted view of the giant fist, Mira's face and body, Ren on the lower-left balcony, and canvas cargo awnings below. Do not put sound effects inside the guard speech panels.

Verbatim new sound lettering: ゴゴゴ… / バキバキッ！
```

## sfx-07-fall.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/07-fall.png", "sha256": "5f4c80051660c866219a3c68555e228507332bd5bbc8f3129b5f337adc91ea49"}]

元の生成指示：

```text
See the preserved adopted edition prompt in ../baseline/PROMPTS.md.
```

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 full-color Japanese Webtoon artwork. Input image is the EXACT EDIT TARGET. Add or revise only the specified integrated raster Japanese sound-effect lettering and the tiny related motion accents explicitly allowed below. Keep the original canvas aspect ratio, panel arrangement, gutters, cropping, composition, camera, every character identity, anatomy, costume, prop, background, pose, expression, exact dialogue and speech/thought balloons unchanged. Preserve vertical Japanese dialogue, upright glyphs and right-to-left column reading. Do NOT redraw or reinterpret the scene. Sounds sit directly in the picture outside dialogue balloons and support the pictured cause/action. Sound lettering may angle with motion; all Japanese words must be spelled exactly. Ensure the added effect reads at 360px phone width, but protect faces, hands, existing text and narrative clues. No English, added dialogue, watermark, captions, new people, panels or premature reveals.

TARGETED EDIT:
Add EXACT ヒュウウッ once as tapered flowing dark-navy lettering with white outline in the open sky BELOW Mira and to the right of center, vertically descending alongside the existing fall path. Gentle curved strokes and a couple restrained wind streaks can emphasize speed without implying a magic power. Keep Mira's whole reaching hand, frightened face, hair and dress clear; keep the lower cargo awnings and exact shouted dialogue visible. Preserve the same perspective, fall position and clear source-to-destination geography.

Verbatim new sound lettering: ヒュウウッ
```

## sfx-08-leap.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/08-leap.png", "sha256": "f2a963e797c6584a68913ab29b354b94f184c38f43c27ec4dea819901f6ac507"}]

元の生成指示：

```text
See the preserved adopted edition prompt in ../baseline/PROMPTS.md.
```

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 full-color Japanese Webtoon artwork. Input image is the EXACT EDIT TARGET. Add or revise only the specified integrated raster Japanese sound-effect lettering and the tiny related motion accents explicitly allowed below. Keep the original canvas aspect ratio, panel arrangement, gutters, cropping, composition, camera, every character identity, anatomy, costume, prop, background, pose, expression, exact dialogue and speech/thought balloons unchanged. Preserve vertical Japanese dialogue, upright glyphs and right-to-left column reading. Do NOT redraw or reinterpret the scene. Sounds sit directly in the picture outside dialogue balloons and support the pictured cause/action. Sound lettering may angle with motion; all Japanese words must be spelled exactly. Ensure the added effect reads at 360px phone width, but protect faces, hands, existing text and narrative clues. No English, added dialogue, watermark, captions, new people, panels or premature reveals.

TARGETED EDIT:
Add EXACT バッ！ once as compact sharp BLACK brush lettering with clean white outline beside the lower-left broken ledge where Ren has just pushed off. Angle its short energetic strokes in the leap direction, with two restrained motion accents beside that ledge. Keep his reaching bare hand and face unobscured, red scarf, entire body/legs and landing awnings unchanged. Do not add glowing energy, armor or superhuman power here. Preserve the exact vertical thought balloon.

Verbatim new sound lettering: バッ！
```

## layout-catch.png

built-in image_gen panel layout recomposition

参照：[{"path": "examples/zero-break/v5/art/sfx-v6-catch.png", "sha256": "8356849e99ccd8192b0f6b3a9bc88a142f2a272d1bf889788d2b55fdceaf7dcd"}]

元の生成指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 Japanese full-color Webtoon artwork. Input is the EXACT EDIT TARGET. Add ONLY specified integrated raster Japanese sound lettering and tiny motion accents. Preserve canvas dimensions/aspect ratio, panel arrangement and gutters, faces, anatomy, hands, poses, clothes, props, setting, every existing Japanese word and speech/thought balloon. Preserve upright vertical dialogue and all reading order. Sound lettering outside balloons may angle with the physical motion, but must be exact and legible at 360px display width. Protect the pictured cause/action, faces, hands and text. No added dialogue, English, panels, powers, armor, watermark, later reveal or newly invented action.

Add medium bold ギュッ！ beside Mira's bare hand gripping Ren's shirt at the center-right, clear of all fingers, faces and the existing つかまって！ balloon. Add flowing lighter バサァッ in the lower-left open background alongside the whipping fabric/scarf direction. Sound of holding on is primary; cloth flutter is secondary. Keep Ren unarmored, carrying Mira above the cargo awning, all limbs and their grip, exact pose and location; do not show a new landing or tear.
Exact new sound words: ギュッ！ / バサァッ
```

採用時の指示：

```text
Use case: illustration-story / existing Japanese Webtoon panel-layout recomposition. The input is the adopted artwork for THIS scene: preserve its exact story events, identities, costume, props, location, speaker, all Japanese dialogue, all sound words, and causal reading order. RE-DRAW the panel arrangement as specified below; do not preserve the old simple vertical stack. Full-color polished anime/cel shading matching the input. White page, thin black frames, clean white gutters. Japanese dialogue is LARGE printed gothic with UPRIGHT glyphs, top-to-bottom and right-to-left columns, target glyph height65-75px on a1024px-wide canvas so it reads at360px width. Never shrink lettering to fit a small frame: use true close-ups and short text. Do not rotate Japanese text even inside angled frames. Speech tails point to the correct actual mouth; thought uses dots toward the head. Sound lettering stays outside dialogue balloons and near its physical cause. Protect faces, hands and all existing exact words. No captions, panel numbers, arrows, English, watermark, duplicate people within one panel, new events, advance reveal, or additional dialogue. READ ORDER for a row is RIGHT panel then LEFT panel; rows proceed TOP to BOTTOM. The output must contain actual side-by-side or angled frames where requested, not just images whose subjects look sideways. Each small panel is a newly composed detail/face crop, not a compressed whole scene.

SPECIFIC LAYOUT AND EXACT CONTENT:
Canvas approximately1024x1408. EXACTLY ONE large rescue panel. Its actual OUTER FRAME must be an oblique quadrilateral inside a white page: top border from(x20,y20) to(x1004,y145), bottom border from(x20,y1260) to(x1004,y1385), upright outer sides. Thus two clear white triangular wedges remain OUTSIDE the picture at upper-right and lower-left. Do NOT merely tilt a conventional rectangle or rotate all the artwork/text. Recompose the midair catch inside this sloping action frame: unarmored Ren's bare arms support Mira's back and knees, both recognizable faces clear, his red scarf and her white/blue/gold dress streaming with downward momentum. He shouts EXACT つかまって！ in upright vertical Japanese inside a bold jagged balloon with tail to HIS mouth, positioned in upper clear space safely INSIDE the sloping top edge. Exact ギュッ！ next to Mira's bare hand grasping Ren's soft black shirt, exact flowing バサァッ by whipping lower-left fabric inside the frame. Protect all fingers, faces, neck and modest intact dress. Same cream cargo awning/blue-gold city flags and white stone towers, canopy BELOW and behind them. They are still above the awning BEFORE landing; no feet contacting ground, no completed landing, no armor, no core, no added people. Retain the same midair moment and grip. Frame slope and scarf/fabric guide the eye toward the next landing image below; text stays upright and uncropped.
```

## 10-landing.png

retained prior adopted image_gen output

参照：[]

採用時の指示：

```text
See git:81a4a9a80c9c6782bac7592142750c324a1b42eb:examples/zero-break/production/feedback-v6/baseline/prompts-episode-01.md for the original executed prompt.
```

## layout-safe-01.png

built-in image_gen panel layout recomposition

参照：[{"path": "examples/zero-break/v5/art/v6-safe-01.png", "sha256": "647470d3b13e82694c7373f125057c20713db171024a87722f6c52c8cffc4e44"}]

元の生成指示：

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

採用時の指示：

```text
Use case: illustration-story / existing Japanese Webtoon panel-layout recomposition. The input is the adopted artwork for THIS scene: preserve its exact story events, identities, costume, props, location, speaker, all Japanese dialogue, all sound words, and causal reading order. RE-DRAW the panel arrangement as specified below; do not preserve the old simple vertical stack. Full-color polished anime/cel shading matching the input. White page, thin black frames, clean white gutters. Japanese dialogue is LARGE printed gothic with UPRIGHT glyphs, top-to-bottom and right-to-left columns, target glyph height65-75px on a1024px-wide canvas so it reads at360px width. Never shrink lettering to fit a small frame: use true close-ups and short text. Do not rotate Japanese text even inside angled frames. Speech tails point to the correct actual mouth; thought uses dots toward the head. Sound lettering stays outside dialogue balloons and near its physical cause. Protect faces, hands and all existing exact words. No captions, panel numbers, arrows, English, watermark, duplicate people within one panel, new events, advance reveal, or additional dialogue. READ ORDER for a row is RIGHT panel then LEFT panel; rows proceed TOP to BOTTOM. The output must contain actual side-by-side or angled frames where requested, not just images whose subjects look sideways. Each small panel is a newly composed detail/face crop, not a compressed whole scene.

SPECIFIC LAYOUT AND EXACT CONTENT:
Canvas1024x2304 approximately. EXACTLY FOUR panels in THREE rows. Top (~34% height) wide shared location: Ren19 black hair/blue eyes/red scarf/soft black short sleeves/charcoal trousers/brown straps/BARE hands kneels LEFT on solid cargo plaza; Mira19 long blonde braid/blue eyes/white royal-blue gold dress/blue-gold flower hair ornament stands RIGHT safely under same torn cream canvas awning. Ren's small prior scratches remain, no armor or cyan core. SILENT, no dialogue. Middle row (~25% height): RIGHT58% width medium Mira face looking down-left, EXACT spoken ありがとう。 with soft organic blue-grey speech outline and connected tail to mouth; LEFT38% width much shallower close-up ONLY Ren's blue eyes relieved while looking up-right, SILENT. Put Ren eyes at the LOWER part of the SAME row, bottoms aligned; keep WHITE space above the shallow left insert,24px gutter between side-by-side frames. This is one right-to-left gratitude/reaction pair, not four vertically stacked rectangles. Bottom (~36% height) full-width larger Mira upper body with her hand naturally at chest, EXACT 私はミラ。 in composed rounded capsule with blue-grey continuous mouth tail. Keep her hand, necklace, flowers, braid, exact dress; same torn canvas and cargo backdrop. No crown crest, identity lore, new event, guardian close-up, sound effects, or extra text. All dialogue spoken, no thought dots.
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

## sfx-v6-approach.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/v6-approach.png", "sha256": "188e2c24ca02b0f6fd5cb42f6dc137bbbd10d3503db82845f1b5410d7a3814c1"}]

元の生成指示：

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

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 Japanese full-color Webtoon artwork. Input is the EXACT EDIT TARGET. Add ONLY specified integrated raster Japanese sound lettering and tiny motion accents. Preserve canvas dimensions/aspect ratio, panel arrangement and gutters, faces, anatomy, hands, poses, clothes, props, setting, every existing Japanese word and speech/thought balloon. Preserve upright vertical dialogue and all reading order. Sound lettering outside balloons may angle with the physical motion, but must be exact and legible at 360px display width. Protect the pictured cause/action, faces, hands and text. No added dialogue, English, panels, powers, armor, watermark, later reveal or newly invented action.

In the first wide scene panel add heavy charcoal/violet ズン… ズン… in two descending beats near the giant's lower body/ground, without covering its core or either protagonist. Communicate footsteps of the approaching SAME giant. In the third shielding-gesture panel add compact ザッ in the lower-left ground-side margin alongside Mira's backward movement, clear of Ren's large bare hand. Leave the two close-up thought/speech panels uncluttered. No early armor or cyan glow.
Exact new sound words: ズン… ズン… / ザッ
```

## sfx-v6-core.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/v6-core.png", "sha256": "494da4641bd999b732d615a53cadc53b25787ad6d58bebe29148e2fa3adc47b7"}]

元の生成指示：

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

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 full-color Japanese Webtoon artwork. Input image is the EXACT EDIT TARGET. Add or revise only the specified integrated raster Japanese sound-effect lettering and the tiny related motion accents explicitly allowed below. Keep the original canvas aspect ratio, panel arrangement, gutters, cropping, composition, camera, every character identity, anatomy, costume, prop, background, pose, expression, exact dialogue and speech/thought balloons unchanged. Preserve vertical Japanese dialogue, upright glyphs and right-to-left column reading. Do NOT redraw or reinterpret the scene. Sounds sit directly in the picture outside dialogue balloons and support the pictured cause/action. Sound lettering may angle with motion; all Japanese words must be spelled exactly. Ensure the added effect reads at 360px phone width, but protect faces, hands, existing text and narrative clues. No English, added dialogue, watermark, captions, new people, panels or premature reveals.

TARGETED EDIT:
In the FIRST, upper chest-close-up panel ONLY, add EXACT キィィン… once in slender luminous pale-cyan sound-effect strokes with dark-blue outline on the left of the first glowing star, in the open dark shirt area between scarf and hand. A small controlled cyan bloom can harmonize with the core glow; every Japanese glyph must remain identifiable at 360px. Preserve the bare hand, SOFT unarmored black fabric, face/scarf, exact thought text and BOTH lower system windows including their exact wording and typography. No armor silhouette, no new panels or labels, no sound effects in the system windows.

Verbatim new sound lettering: キィィン…
```

## armor-route.png

built-in image_gen armor assembly insertion

参照：[{"path": "examples/zero-break/v5/art/sfx-v6-core.png", "sha256": "ea88f815854233497ff443c1852f3277e37f3b218520fe5a599086e1be75321c"}, {"path": "examples/zero-break/v5/art/sfx-14-hero.png", "sha256": "06b3480a33e9250958be8f59cfe3d9528bd5ecfa928221728efc2ab8e56c87d9"}]

採用時の指示：

```text
Use case: illustration-story. Recompose the input core/armor artwork into the NEXT sequential transformation insert in the SAME adopted Zero Break episode 1. Image 1 is the starting-state/visual-style target; Image 2 is the finished armor design and Ren identity reference ONLY. Preserve the Japanese anime/cel-shaded rendering and same lower solid cargo plaza, torn cream canvas awning, blue-gold city flags in soft background. Ren19: black tousled hair, blue eyes, crimson scarf, soft black short sleeves, charcoal trousers, brown straps before assembly. Finished armor is BLACK angular faceted plates with CYAN seams and a cyan STAR chest core, black segmented gauntlets and boots; NEVER a helmet. Mira remains safe offscreen behind, same black stone giant with violet core remains offscreen ahead. No newly invented characters, weapons, icons, forms, crown or lore. This is not a collage of simultaneous duplicate people. Show sequential close-up steps, UNEQUAL panels, white narrow gutters, top-to-bottom reading. Exact Japanese text and sound effects integrated in raster artwork. Dialogue/thought glyphs are upright, vertical top-to-bottom/right-to-left, bold gothic readable at360px; sounds may angle with action. Cyan system panes are compact functional translucent navy/cyan projections with restrained glow; no ornate plaques or English. Do NOT reveal a completed full-body armored silhouette: that comes in the existing hero panel below. Aim 1024x2048, portrait ratio1:2; make small panels true detail shots, not shrunken full scenes.

Panel 1 is larger: chest-to-bare-forearm close-up shows the SINGLE cyan chest star driving luminous paths OUTWARD through cloth over shoulder and arm. Arm still bare, human fingers unchanged. A compact restrained cyan system rectangle reads EXACT 装甲展開、開始。 in upright vertical Japanese. Panel 2 is a smaller, left-aligned wrist close-up: a delicate cyan angular lattice outlines a future wrist guard above the still-bare hand, with exact slender シュウウ… nearby. No black armor yet, no floating body, no additional labels.
```

## layout-armor-assemble.png

built-in image_gen panel layout recomposition

参照：[{"path": "examples/zero-break/v5/art/armor-assemble.png", "sha256": "4b02f12584966ff2c3c88b87336ba42d22229be7f839603962116aa19990b891"}]

元の生成指示：

```text
Use case: illustration-story. Recompose the input core/armor artwork into the NEXT sequential transformation insert in the SAME adopted Zero Break episode 1. Image 1 is the starting-state/visual-style target; Image 2 is the finished armor design and Ren identity reference ONLY. Preserve the Japanese anime/cel-shaded rendering and same lower solid cargo plaza, torn cream canvas awning, blue-gold city flags in soft background. Ren19: black tousled hair, blue eyes, crimson scarf, soft black short sleeves, charcoal trousers, brown straps before assembly. Finished armor is BLACK angular faceted plates with CYAN seams and a cyan STAR chest core, black segmented gauntlets and boots; NEVER a helmet. Mira remains safe offscreen behind, same black stone giant with violet core remains offscreen ahead. No newly invented characters, weapons, icons, forms, crown or lore. This is not a collage of simultaneous duplicate people. Show sequential close-up steps, UNEQUAL panels, white narrow gutters, top-to-bottom reading. Exact Japanese text and sound effects integrated in raster artwork. Dialogue/thought glyphs are upright, vertical top-to-bottom/right-to-left, bold gothic readable at360px; sounds may angle with action. Cyan system panes are compact functional translucent navy/cyan projections with restrained glow; no ornate plaques or English. Do NOT reveal a completed full-body armored silhouette: that comes in the existing hero panel below. Aim 1024x2048, portrait ratio1:2; make small panels true detail shots, not shrunken full scenes.

THREE UNEQUAL ordered panels. Panel 1 smaller right-aligned forearm: matte/glossy BLACK faceted wrist guard plates emerge from the cyan lattice, tiny cyan join lines, one pair of plate edges almost meeting then clicking; exact カチッ in compact crisp letters. Human fingertips still bare, do not finish the whole glove here. Panel 2 broader lower-leg/boot view: black angular shin/boot plates slide together over dark trousers/ordinary boot, grounded on the same cracked solid plaza; sound ガシャッ in medium angular letters. Panel 3 the largest close-up of chest ONLY: black chest plates interlock around a SINGLE cyan star core, scarf remains red above, all armor cyan seams match reference. Exact larger metallic sound ガキンッ and a compact system pane EXACT 装甲固定。 No full suit pose, no helmet, no cape instead of scarf.
```

採用時の指示：

```text
Use case: illustration-story / existing Japanese Webtoon panel-layout recomposition. The input is the adopted artwork for THIS scene: preserve its exact story events, identities, costume, props, location, speaker, all Japanese dialogue, all sound words, and causal reading order. RE-DRAW the panel arrangement as specified below; do not preserve the old simple vertical stack. Full-color polished anime/cel shading matching the input. White page, thin black frames, clean white gutters. Japanese dialogue is LARGE printed gothic with UPRIGHT glyphs, top-to-bottom and right-to-left columns, target glyph height65-75px on a1024px-wide canvas so it reads at360px width. Never shrink lettering to fit a small frame: use true close-ups and short text. Do not rotate Japanese text even inside angled frames. Speech tails point to the correct actual mouth; thought uses dots toward the head. Sound lettering stays outside dialogue balloons and near its physical cause. Protect faces, hands and all existing exact words. No captions, panel numbers, arrows, English, watermark, duplicate people within one panel, new events, advance reveal, or additional dialogue. READ ORDER for a row is RIGHT panel then LEFT panel; rows proceed TOP to BOTTOM. The output must contain actual side-by-side or angled frames where requested, not just images whose subjects look sideways. Each small panel is a newly composed detail/face crop, not a compressed whole scene.

SPECIFIC LAYOUT AND EXACT CONTENT:
Canvas1024x1800 approximately. EXACTLY THREE panels in TWO rows. TOP ~46% height is a TWO-PANEL SIDE-BY-SIDE assembly row separated by a strong clean DIAGONAL WHITE GUTTER, not a horizontal separator. Divide runs from around canvas x50% at TOP to x60% at row BOTTOM: RIGHT panel is a distinct trapezoid, LEFT panel complementary trapezoid. Keep outer edges within canvas. READ RIGHT FIRST: close-up of Ren's black faceted forearm/wrist plates forming around cyan join-lines, fingertips still BARE, exact カチッ in compact crisp letters at clear top-right. THEN LEFT: close-up of grounded black faceted boot/shin plates fitting over charcoal trousers, ordinary solid cracked cargo-plaza floor, exact ガシャッ in medium sharp letters. Do not show a full person or duplicate upper limbs. Bottom ~50% height is one broad large CHEST close-up: black angular plates interlock around a SINGLE cyan STAR; red scarf above, lower face only, EXACT larger metallic ガキンッ on left and compact cyan system notice EXACT 装甲固定。 on right. System text upright vertical, restrained navy/cyan functional projection. Each sound entirely inside its own panel without covering wrist/fingers/boot joins/star or system glyphs. Same black armor/cyan seams design, face uncovered, no helmet. Do not show completed whole-body pose; later existing hero panel reveals it. The diagonal split should give two mechanical steps a brisk rhythm, while the chest closure is visibly broader and settles below.
```

## armor-check.png

built-in image_gen armor assembly insertion with thought-tail repair

参照：[{"path": "examples/zero-break/v5/art/sfx-v6-core.png", "sha256": "ea88f815854233497ff443c1852f3277e37f3b218520fe5a599086e1be75321c"}, {"path": "examples/zero-break/v5/art/sfx-14-hero.png", "sha256": "06b3480a33e9250958be8f59cfe3d9528bd5ecfa928221728efc2ab8e56c87d9"}, {"path": "examples/zero-break/v5/art/armor-check-before-thought-tail.png", "sha256": "122ab59d38b28733a14913cedf61953a0b7bdcdff75ad7fb31d40e628007c7ae"}]

元の生成指示：

```text
Use case: illustration-story. Recompose the input core/armor artwork into the NEXT sequential transformation insert in the SAME adopted Zero Break episode 1. Image 1 is the starting-state/visual-style target; Image 2 is the finished armor design and Ren identity reference ONLY. Preserve the Japanese anime/cel-shaded rendering and same lower solid cargo plaza, torn cream canvas awning, blue-gold city flags in soft background. Ren19: black tousled hair, blue eyes, crimson scarf, soft black short sleeves, charcoal trousers, brown straps before assembly. Finished armor is BLACK angular faceted plates with CYAN seams and a cyan STAR chest core, black segmented gauntlets and boots; NEVER a helmet. Mira remains safe offscreen behind, same black stone giant with violet core remains offscreen ahead. No newly invented characters, weapons, icons, forms, crown or lore. This is not a collage of simultaneous duplicate people. Show sequential close-up steps, UNEQUAL panels, white narrow gutters, top-to-bottom reading. Exact Japanese text and sound effects integrated in raster artwork. Dialogue/thought glyphs are upright, vertical top-to-bottom/right-to-left, bold gothic readable at360px; sounds may angle with action. Cyan system panes are compact functional translucent navy/cyan projections with restrained glow; no ornate plaques or English. Do NOT reveal a completed full-body armored silhouette: that comes in the existing hero panel below. Aim 1024x2048, portrait ratio1:2; make small panels true detail shots, not shrunken full scenes.

TWO ordered panels. Top panel is a medium close-up ONLY of Ren's newly BLACK segmented armored hand forming ONE clenched fist naturally (normal five-finger anatomy), cyan seams and faint red scarf edge. Place exact thought ……動かせる。 in one white cloud balloon with dots leading offscreen toward his head, not spoken by the glove. Add compact exact ギュッ beside the fist without hiding knuckles. Lower panel is a shallow close-up of a readable translucent navy/cyan functional HUD over blurred black chest/ground. EXACT header 救済核残量 is horizontal Japanese above a reserve bar of SIX uniform rectangles: FOUR cyan lit and TWO dark. EXACT separate confirmation 接続完了。 below. This communicates finite stored energy only; no percentages, time limit, numeric costs, magic readout, recharge rules, foreign origin, future forms or source identity. No full-body armor reveal, victory, or enemy attack.
```

採用時の指示：

```text
Use case: precise-object-edit. Edit ONLY the dotted thought-balloon trail in the TOP panel. Keep all artwork, canvas, panels, entire armored hand/fist, exact Japanese thought ……動かせる。, sound ギュッ, lower system notice 救済核残量 / 接続完了。 and the six reserve segments (four lit, two dark) exactly as shown. The thinker is Ren, whose HEAD is OFFSCREEN ABOVE the top panel. REMOVE the current thought dots at the balloon's LOWER-LEFT that point to the glove. Put a short trail of TWO or THREE small thought dots above the balloon at its UPPER-RIGHT, travelling UP toward the top image edge and offscreen Ren's head. Keep dots within the image, do not connect them toward any glove/arm/hand. Preserve the balloon position/text/size and all other pixels as closely as possible. No added labels, no other edits.
```

## sfx-14-hero.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/14-hero.png", "sha256": "1ec3bf124f07724dd319caa5d1c164b18f4de168452f60fdba26e0119845cbf3"}]

元の生成指示：

```text
See the preserved adopted edition prompt in ../baseline/PROMPTS.md.
```

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 full-color Japanese Webtoon artwork. Input image is the EXACT EDIT TARGET. Add or revise only the specified integrated raster Japanese sound-effect lettering and the tiny related motion accents explicitly allowed below. Keep the original canvas aspect ratio, panel arrangement, gutters, cropping, composition, camera, every character identity, anatomy, costume, prop, background, pose, expression, exact dialogue and speech/thought balloons unchanged. Preserve vertical Japanese dialogue, upright glyphs and right-to-left column reading. Do NOT redraw or reinterpret the scene. Sounds sit directly in the picture outside dialogue balloons and support the pictured cause/action. Sound lettering may angle with motion; all Japanese words must be spelled exactly. Ensure the added effect reads at 360px phone width, but protect faces, hands, existing text and narrative clues. No English, added dialogue, watermark, captions, new people, panels or premature reveals.

TARGETED EDIT:
Add EXACT ガキンッ！ once as angular metallic assembly sound lettering in black/navy with crisp white outline and a restrained cyan highlight, in the upper-left clear sky beside Ren's shoulder/head without covering his hair/face. The lettering should communicate the final armor locking into place, medium strength between the slender core tone and the huge following punch. Preserve his full-length black faceted suit, cyan star/seams, red scarf, calm ready stance, Mira standing safely behind at right, white floating city and exact speech balloon. Do not add new armor pieces, a transformation montage or a punch.

Verbatim new sound lettering: ガキンッ！
```

## sfx-15-punch.png

built-in image_gen targeted raster sound-effect edit

参照：[{"path": "examples/zero-break/v5/art/15-punch.png", "sha256": "8628adaf6b9c98c42bce8e482947d79ae29cd884a43165f58e88255a9ce4accb"}]

元の生成指示：

```text
See the preserved adopted edition prompt in ../baseline/PROMPTS.md.
```

採用時の指示：

```text
Use case: precise-object-edit. Asset: existing adopted Zero Break episode 1 full-color Japanese Webtoon artwork. Input image is the EXACT EDIT TARGET. Add or revise only the specified integrated raster Japanese sound-effect lettering and the tiny related motion accents explicitly allowed below. Keep the original canvas aspect ratio, panel arrangement, gutters, cropping, composition, camera, every character identity, anatomy, costume, prop, background, pose, expression, exact dialogue and speech/thought balloons unchanged. Preserve vertical Japanese dialogue, upright glyphs and right-to-left column reading. Do NOT redraw or reinterpret the scene. Sounds sit directly in the picture outside dialogue balloons and support the pictured cause/action. Sound lettering may angle with motion; all Japanese words must be spelled exactly. Ensure the added effect reads at 360px phone width, but protect faces, hands, existing text and narrative clues. No English, added dialogue, watermark, captions, new people, panels or premature reveals.

TARGETED EDIT:
Replace ONLY the existing red/black lower-left ドンッ impact effect with much larger, more legible ドゴォンッ！ in energetic black brush letters with a clean thick white separation outline and restrained cyan edge. Sweep it diagonally upward toward the fist-core contact. Add smaller angular ガシャァッ！ among the flying upper-left fragments to communicate stone shattering. Preserve the exact punch contact, wrist/fist, cyan impact burst, purple guardian core fragments, Ren's face/red scarf and Mira safe behind him. The primary ドゴォンッ！ must be visibly stronger than ガシャァッ！ and legible at phone width. Avoid muddy illegible red texture.

Verbatim new sound lettering: ドゴォンッ！ / ガシャァッ！
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
