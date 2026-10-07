#!/usr/bin/env python3
"""Prepare next-generation prompts from the adopted chapter without a body snapshot."""
import json
from pathlib import Path
from panel_lettering import normalize_panel, render_panel_lettering

ROOT = Path(__file__).resolve().parents[1]

COMMON = '''Use case: illustration-story. A finished Japanese full-color smartphone vertical-scroll Webtoon strip, including final artwork, speech balloons and exact Japanese lettering. Generate ONE portrait raster image, normally width:height 1:3. The reference sheet is ONLY for character identity, clothing, colors and anime linework. Do not copy its layout, parchment, labels or facial expression. Kai: dark brown hair with one amber streak at his right temple, amber eyes, ivory rolled-sleeve shirt, brown leather vest, short indigo cape, copper cuff left forearm, dark trousers, tool pouch; NO sword on his waist in this episode. Sena: silver-blonde low ponytail, blue eyes, silver shoulder/arm armor, blue tunic and navy cape, triangular silver shield with cobalt lines; her normal plain sword is sheathed. The ONE prototype being tested is steel, square brass guard, dark leather grip, ONE very thin orange inset line along the center of the blade, small brass vent beside the guard. It is Kai's creation, loaned to Sena for a test, NOT a lightsaber. Real-world Kaito: same young male face but natural black hair, no amber streak, charcoal T-shirt; black VR headset and TWO small motion controllers, no gamepad. Iris is not in this chapter. Modern equipment appears ONLY in the real room, medieval scenery ONLY inside the VR game.

Storytelling: follow the stated emotional progression, one principal understanding per panel. The party promise is earned and received before the specified tower incident. Stay in the stated place, preserve the same blue cloth on the workshop door, the workbench, the single wooden practice dummy in the adjacent stone yard. Establish people and position once, then close-ups of speaker, listener or object instead of packing everyone and an elaborate city into each small panel. Keep speaking to nearby offscreen people spatially clear. Draw only the specified plot events; no extra dialogue, arms, duplicate characters or multiple copies of the sword. The sword NEVER breaks or causes the tower incident in this chapter.

Panel design: use the SPECIFIC unequal panel widths, heights, staggered placement, borderless landscape and occasional diagonal action frames described below. These panels are successive moments, not simultaneous duplicate people. Clear top-to-bottom flow, same-row inserts read right to left. White gutters, substantial calm breathing room between dialogue/response panels; not a uniform four-box grid and not four cramped panels inside a phone screen. Every tiny panel focuses on a hand, face or component rather than a tiny whole scene. Detailed background ONLY for orientation and the giant tower reveal. Simple backgrounds for emotion. Keep words, faces, fingers and the vent large and separate.

Lettering: true Japanese vertical speech, upright black printed manga glyphs, columns RIGHT to LEFT, each column top-to-bottom. Use LARGE glyphs roughly 5.6 percent of image width (about 20px high when shown at 360px wide). Never shrink text to fit. Exact utterance and column order follow; slash marks in instructions are separators and must not be printed. Spoken words have clean white oval/rounded vertical balloons with tails aimed at the actual speaker. Small quiet speech has softly irregular thin outlines. Internal thought uses thought dots and a softer cloud border. Screen/HUD messages may be horizontal, cyan translucent in the game; real PC message is small ordinary horizontal text. Dialogue and sound effects are independent. No dialogue means no speech/thought balloons; render any separately specified sounds. Place sound lettering near its source, outside balloons, with no tails. Do not apply dialogue column rules to sounds. Only panels explicitly specifying no sounds are quiet. No speaker labels, panel numbers, decorative captions, watermark or extra text. Reserve light blank areas for balloons and generous inset padding. All text is integrated into the raster art.
'''

def main():
    current=ROOT/'episode-01/episode.json'
    scenes=json.loads(current.read_text())['scenes']
    scenes=[dict(x,panels=[normalize_panel(p) for p in x['panels']]) for x in scenes]
    design_path=ROOT/'production/episode-01-sound-design.json'
    if design_path.exists():
        design=json.loads(design_path.read_text())
        for key,cues in design['panels'].items():
            i,j=map(int,key.split('-'))
            scenes[i-1]['panels'][j-1]['sounds']=cues
    moment_count=sum(len(x['panels']) for x in scenes)
    prompts=['# 第1話 次回生成用の指示（未実行）\n\n参照は人物・衣装・絵柄のみ。初稿の密度とコマ割りは引き継がない。\n']
    for i,scene in enumerate(scenes,1):
        scene['id']=f'{i:02d}'; scene['file']=scene.get('file',f'art/r{i:02d}.png')
        kind='narrative moments (not mandatory full-width panels)' if scene.get('scroll_layout') else 'narrative panels'
        prompt=COMMON+f"\nChapter 1 revised, strip {i}. Image ratio {scene['ratio']}. Scene: {scene['name']}. Place and continuity: {scene['location']}. Purpose: {scene['purpose']}. Exactly {len(scene['panels'])} {kind}, with unequal sizes as described.\n"
        if scene.get('scroll_layout'):
            layout=scene['scroll_layout']
            prompt+=f"\nScroll composition takes precedence over the reference or default panel grid: {layout['composition']} Reading order: {layout['read_order']} Preserve borderless continuous scenery, same-row pairs and quiet white space; never turn every narrative moment into a full-width rectangle.\n"
        for j,panel in enumerate(scene['panels'],1):
            prompt+=f"\nPanel {j}, top to bottom. Artwork, camera, size and main focus: {panel['art']}\n"
            prompt+=render_panel_lettering(panel)
        scene['prompt']=prompt
        scene['prompt_role']='prepared_next_generation_not_executed'
        prompts += [f'\n## r{i:02d}\n\n```text\n{prompt}\n```\n']
    (ROOT/'episode-01/PROMPTS-NEXT.md').write_text(''.join(prompts))
    print(f"Prepared next-generation instructions for {len(scenes)} strips, {moment_count} panels. Actual used prompts and reader unchanged.")

if __name__=='__main__': main()
