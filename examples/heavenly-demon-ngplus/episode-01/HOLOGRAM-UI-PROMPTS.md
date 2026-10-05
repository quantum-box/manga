# システム表示：視界内の投影へ

2026-10-05。『作中の表示として鮮明すぎるので、もっとぼかしてほしい』という指摘に合わせた光学表現の編集。現在の日本語・配置を保ち、文字と枠の拡散光、残像、透過を変更。組み込み image_gen で編集し、原本のPNGバイトを保存する。

## ui-transfer

編集元：`art/lettering/ui-transfer-system-v1.png`

保存先：`art/lettering/ui-transfer-system-v2.png`

```text
Use case: precise-object-edit.
Asset type: Japanese anime Webtoon, a subjective system window floating inside the protagonist's field of vision.
Edit ONLY the optical appearance of this existing image. Keep the exact Japanese text, wording, font arrangement, row positions, dimensions and navy/cyan window geometry.
The user says the text is too crisply displayed for a projection seen inside the story. Make the window visibly soft and translucent: gently defocus the lettering contours, with a soft cyan-white bloom and a very faint displaced optical ghost. All text should have the same projected-light softness as the border. Use pale translucent glyphs rather than solid opaque white glyphs. The visual effect must be apparent when this entire image is reduced to about 350px wide. The central shapes remain identifiable for reading, but the edges should not look like a crisp screenshot or printed font. Aim for around 4px of soft optical diffusion at the original 1672px width, with an additional weak 9px glow, not heavy illegible smearing.
Make the navy field genuinely semi-transparent (roughly 55-65% alpha) and gently fading near edges. Cyan frame is translucent and subtly diffused too. Keep the outside completely transparent. Generate actual alpha transparency inside and outside, not a checkerboard or white background.
Avoid sparkles, flare streaks, grain, ornaments, gold, extra words, duplicate letters, distorted Japanese glyphs, big solid opaque glows, and new imagery. The source is the edit target.
Exact text to preserve: SYSTEM / 転生先 / 雑役弟子 ハン・ユン / 身分： / 最下級 / 処刑まで / 10秒. Keep the timer red but softly projected.
```

## ui-inherit

編集元：`art/lettering/ui-inherit-system-v1.png`

保存先：`art/lettering/ui-inherit-system-v2.png`

```text
Use case: precise-object-edit.
Asset type: Japanese anime Webtoon, a subjective system window floating inside the protagonist's field of vision.
Edit ONLY the optical appearance of this existing image. Keep the exact Japanese text, wording, font arrangement, row positions, dimensions and navy/cyan window geometry.
The user says the text is too crisply displayed for a projection seen inside the story. Make the window visibly soft and translucent: gently defocus the lettering contours, with a soft cyan-white bloom and a very faint displaced optical ghost. All text should have the same projected-light softness as the border. Use pale translucent glyphs rather than solid opaque white glyphs. The visual effect must be apparent when this entire image is reduced to about 350px wide. The central shapes remain identifiable for reading, but the edges should not look like a crisp screenshot or printed font. Aim for around 4px of soft optical diffusion at the original 1672px width, with an additional weak 9px glow, not heavy illegible smearing.
Make the navy field genuinely semi-transparent (roughly 55-65% alpha) and gently fading near edges. Cyan frame is translucent and subtly diffused too. Keep the outside completely transparent. Generate actual alpha transparency inside and outside, not a checkerboard or white background.
Avoid sparkles, flare streaks, grain, ornaments, gold, extra words, duplicate letters, distorted Japanese glyphs, big solid opaque glows, and new imagery. The source is the edit target.
Exact text to preserve: SYSTEM / 引き継ぎ完了 / LV.999 / 内功・武技 全解放. Keep the cyan check mark.
```

## ui-reward

編集元：`art/lettering/ui-reward-system-v1.png`

保存先：`art/lettering/ui-reward-system-v2.png`

```text
Use case: precise-object-edit.
Asset type: Japanese anime Webtoon, a subjective system window floating inside the protagonist's field of vision.
Edit ONLY the optical appearance of this existing image. Keep the exact Japanese text, wording, font arrangement, row positions, dimensions and navy/cyan window geometry.
The user says the text is too crisply displayed for a projection seen inside the story. Make the window visibly soft and translucent: gently defocus the lettering contours, with a soft cyan-white bloom and a very faint displaced optical ghost. All text should have the same projected-light softness as the border. Use pale translucent glyphs rather than solid opaque white glyphs. The visual effect must be apparent when this entire image is reduced to about 350px wide. The central shapes remain identifiable for reading, but the edges should not look like a crisp screenshot or printed font. Aim for around 4px of soft optical diffusion at the original 1672px width, with an additional weak 9px glow, not heavy illegible smearing.
Make the navy field genuinely semi-transparent (roughly 55-65% alpha) and gently fading near edges. Cyan frame is translucent and subtly diffused too. Keep the outside completely transparent. Generate actual alpha transparency inside and outside, not a checkerboard or white background.
Avoid sparkles, flare streaks, grain, ornaments, gold, extra words, duplicate letters, distorted Japanese glyphs, big solid opaque glows, and new imagery. The source is the edit target.
Exact text to preserve: SYSTEM / 上位者撃破 / 内功 / +120年 / 固有武技 / 『飛燕歩』獲得. Keep the cyan check mark.
```
