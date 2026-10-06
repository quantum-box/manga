# 第09話 ゼロの外側 — 作画指示と実行記録

方式：組み込み image_gen。採用原画のハッシュと参照は generation-log.json。

## 01-workshop-return.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../v5/art/a14-rejection.png, ../production/references/noa.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Rescue team back in warm workshop at night, freed residents rest on cots; Noa connects neutral magic meter near unarmored Ren, Mira holds trial memory crystal, Rook guards closed door.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 02-zero-again.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../v5/art/a11-result.png

```text
Original generation prompt:
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Close original black crystal-on-silver-pedestal meter from episode1 now at workshop bench shows exact big ０ on horizontal plaque. Ren bare hand on crystal, no armor.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.

Adopted targeted edit prompt:
Edit ONLY time-of-day background and light in FIRST image. Preserve the same black crystal on silver gothic measuring pedestal, the exact large numeral 0, Ren's BARE hand, any native vertical speech, composition and all device details. This is the NIGHT brass-and-brick workshop from image2, not daytime: replace bright daylight windows with dark indigo night windows, warm amber oil-lamp light and dim brick/copper-pipe interior. No sun or bright blue sky, no character/letter changes, no armor.
```

## 03-replay.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../production/references/noa.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Noa slowly replays paper/oscilloscope line: magic needle flat while cyan chest glow visible in recording. Gesture toward discrepancy, device design consistent.

Balloon 1: speech, Noa, upper right. EXACT text: 針は、動いてない。 . Columns RIGHT to LEFT: 針は、 / 動いてない。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## 04-other-axis.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png

```text
Original generation prompt:
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Mira draws TWO clear simple graph axes on paper, one flat, one rises during rescuing; exact large horizontal labels 魔力 and 救助負荷 . Ren leans in, not instantly master explanation.

Balloon 1: speech, Mira, upper right. EXACT text: 空じゃない。測る箱が違う。 . Columns RIGHT to LEFT: 空じゃない。 / 測る箱が / 違う。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.

Adopted targeted edit prompt:
Edit ONLY background time and environmental lighting in FIRST image. Preserve Mira, Ren and Noa, both graphs and ALL exact readable lettering 魔力 / 救助負荷 and 空じゃない。測る箱が違う。 unchanged. Same brass-and-brick workshop at NIGHT as image2, dark indigo windows and warm amber lamps. Replace any bright daytime sky or sunlit exterior with dark night workshop wall/window. Do not alter measurements, faces, clothes, speech bubble shape, drawing quality or layout.
```

## 05-understand.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png

```text
Original generation prompt:
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren touches bare chest over faint cyan core, eyes widen with slow relief, red scarf moved slightly but same outfit.

Balloon 1: speech, Ren, upper right. EXACT text: ゼロでも、ここにはある。 . Columns RIGHT to LEFT: ゼロでも、 / ここには / ある。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.

Adopted targeted edit prompt:
Edit ONLY background and its light in FIRST image. Preserve Ren's black ordinary short-sleeve FABRIC shirt, bare hand/arm, red scarf, small cyan point at chest, thoughtful face and EXACT native vertical speech ゼロでも、ここにはある。. Replace the bright outdoor palace setting with the SAME INSIDE brass-and-brick rescue workshop at NIGHT in image2: oil lamps, copper pipes, shelves, warm amber light and dark indigo night window. No location jump outside, no daylight, no armor, no new characters or letters.
```

## 06-siege.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Outside night alley, grey armored royal guards surround workshop main door and power pillar. Inside team not yet fighting, no graphic force.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 07-cut-power.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Guard lever cuts workshop supply cable at street fuse box, lanterns inside dim visible through window. Ordinary electrical sabotage, no future villain face.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
```

## 08-ventilator-stops.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../episode-05/art/10-old-man.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Inside simple medical alcove, OLD MAN brown vest grey beard saved in episode5 on cot uses brass bellows breathing assistance, motion slows; Mira notices distress, no death or gore.

Balloon 1: speech, Mira, upper right. EXACT text: 呼吸の装置が…！ . Columns RIGHT to LEFT: 呼吸の / 装置が…！.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
```

## 09-check-patient.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../production/references/noa.png, art/08-ventilator-stops.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Ren unarmored kneels beside same elderly man with shallow breath, checks wrist while Noa pulls isolated test circuit box from shelf. No immediate success.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## 10-isolate-circuit.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../production/references/noa.png, art/08-ventilator-stops.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Noa connects ONLY isolated rescue-core circuit to ventilator, physical copper leads and safety switch visible; no connection to city main grid or new form. Ren keeps one bare hand on terminal.

Balloon 1: speech, Noa, upper right. EXACT text: 街の線とは、切り離す。 . Columns RIGHT to LEFT: 街の線とは、 / 切り離す。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## 11-give-power.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, art/08-ventilator-stops.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: Ren concentrates faint CYAN energy from chest into isolated lead with BOTH arms UNARMORED, no full armor or attack. Bellows starts first small motion, he sacrifices combat output.

Balloon 1: speech, Ren, upper right. EXACT text: 戦う力は、あとでいい。 . Columns RIGHT to LEFT: 戦う力は、 / あとでいい。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## 12-rook-guard.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../v5/art/a14-rejection.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Rook silver armor blue cape holds steel shield against workshop door under guards' blows, protects exhausted unarmored Ren inside. No miraculous limitless power.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## 13-breath-cue.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, art/08-ventilator-stops.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Close brass ventilator bellows expands and cyan indicator starts tiny pulse, patient face still outside crop. Wait for actual breathing response, no healthy smile shown yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## 14-breath-returns.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, art/08-ventilator-stops.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: FIRST clear elderly man inhales, chest visibly lifts under blanket, hand relaxes; Mira relieved nearby, Ren remains at powered circuit.

Balloon 1: speech, Mira, upper right. EXACT text: 息が、戻った。 . Columns RIGHT to LEFT: 息が、 / 戻った。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```

## 15-small-line.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../production/references/noa.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Output paper recorder draws a small unmistakably rising cyan line, Noa points with oil stained orange glove, no huge numeric gain, no upgraded gadget.

Balloon 1: speech, Noa, upper right. EXACT text: ちゃんと、届いてる。 . Columns RIGHT to LEFT: ちゃんと、 / 届いてる。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## 16-signal.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../production/references/noa.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x768. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Noa sees a faint stray transmission travelling out of isolated sensor toward thin separate line on city map. Do not show location label yet.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## 17-under-palace.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1792. Composition: one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels
Scene and exact state: FIRST reveal city map route goes into chamber DIRECTLY beneath royal palace white towers; map exact large label 王宮直下 . Mira traces destination, no fuel torture depiction.

No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form.
```

## 18-location.png

状態：generated

参照：../episode-03/art/03-fist.png, ../production/references/mira.png, ../v5/art/a14-rejection.png, ../production/references/noa.png, art/08-ventilator-stops.png

```text
Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.

Preferred image aspect 1024x1280. Composition: one close readable moment, minimal extraneous margins
Scene and exact state: Mira holds traced map while Ren still powers ventilator, eyes resolved. Rook keeps protective door, Noa watches line.

Balloon 1: speech, Mira, upper right. EXACT text: ここが、消えた街区の行き先。 . Columns RIGHT to LEFT: ここが、 / 消えた街区の / 行き先。.
Exactly 1 speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.
Strict continuity: it is NIGHT in the same brass workshop, dim amber lanterns and indigo dark exterior if a window is visible. Never bright sunlight, blue daytime city, palace or outdoor plaza. Ren stays in ordinary BLACK FABRIC shirt, red scarf, BARE arms and hands throughout this entire episode. No armor on him, no attack or new form. The elderly survivor and breathing device match art/08-ventilator-stops.png: GREY beard and BROWN vest, lying on the same cot, brass mouth mask and BROWN LEATHER bellows connected by one hose. Keep the physical connection from isolated copper lead through a brass actuator to the bellows. No change of patient or ventilator design. Ren provides sustained power at the adjacent terminal; he cannot simultaneously be somewhere else.
```
