# 第2話の採用原画

2026-10-10「いいね！GO！」で採用された96コマのネームを組み込みimage_genでカラー化した。

- 採用と生成元：[plan.json](production/final-from-name/plan.json)
- 実際の指示：[prompts](production/final-from-name/prompts/)
- 参照：人物設定、第1話の完成原画、採用ネーム
- 表示窓：[source-crops.json](production/final-from-name/source-crops.json)
- 補修：話者の尾、青い扉、銅貨二枚、靴、退場済み人物の除去

原画PNGは生成元と同一バイト。本文の日本語と吹き出しは原画に統合し、HTMLで重ねない。


## 2026-10-11 全編レイアウト補修

既存の f01〜f17, f22, f24 を編集対象とし、同じ絵の吹き出し・心の声のみ除去。新しい場面は生成しない。生成元と採用先は `production/final-from-name/layout-edit-sources.json`。組版の選択は `layout-decisions.json`。

使用した built-in image_gen の指示：

- f01: Edit target: this exact 4-cell manga sheet. Precise local lettering removal ONLY. Remove all four speech balloons and their Japanese dialogue, including tails, reconstructing the immediately underlying classroom background naturally. KEEP the blue sound effect キーン コーン in top-left cell unchanged. Preserve all four existing illustrations, exact character faces and expressions, poses, hands, bags, uniform, colors, lighting, framing, 2x2 grid and cell boundaries. Do not redraw or redesign the scene. No additional text. Output same 1024x1536 composition.
- f02–f06: Edit target: this exact 4-cell manga sheet. Precise local lettering removal ONLY: remove every speech balloon/thought balloon, its dialogue and tails/dots. Reconstruct only the immediately underlying background. KEEP sound effects, diegetic shop signs, all people and objects unchanged. Preserve exact faces, expressions, poses, hands, clothes, props, lighting, colors, camera framing, all four illustrations and 2x2 grid/cell boundaries. Do not invent scenes or change layout. No new text. This image will be cropped in HTML to match an already approved storyboard; do not recompose. Output same 1024x1536 composition.
- f07–f12: Precise local lettering-removal edit of the supplied 4-cell manga sheet. Remove all speech/thought balloons, their dialogue and tails/dots; reconstruct only the underlying background. KEEP all drawn sound effects and shop signs. Preserve every character face, expression, pose, hand, outfit, prop, setting, color and lighting. Keep original exact 2x2 grid with same four cell boundaries and framing. Do not add detail, recompose, redesign or invent. This is source cleanup for independently typeset dialogue and narrower storyboard crops, not a new illustration. Output same 1024x1536 layout.
- f13–f17, f22, f24: Precise local lettering-removal edit of this exact supplied 4-cell manga sheet. Remove speech/thought balloons and all their dialogue, tails/dots, restoring the immediately underlying background ONLY. Keep every sound effect and shop sign unchanged. Preserve all four character illustrations, exact faces, expressions, hands, poses, props, injuries, clothes, colors, light and camera framing. Preserve exact 2x2 grid and cell boundaries. Do not invent scenes or change drawing style or add detail. Output same 1024x1536 composition.
- f24のみ上記ONLY直後に追加: Also remove the glowing blue text notification rectangle from bottom-left panel (the text will be typeset in separate white space), reconstructing only the city behind it; keep the two coins and hand exactly.
