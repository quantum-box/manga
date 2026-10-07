#!/usr/bin/env python3
"""Prepare prompts from the sole adopted chapter scripts; never embed story snapshots."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMON = '''Use case: illustration-story. Asset: finished full-color smartphone Japanese vertical-scroll Webtoon, including final speech balloons, Japanese text, SFX and specified HUD. Create ONE tall native illustration, 1:3 aspect ratio, preferably 1024x3072. Polished detailed anime linework and controlled cel shading, expressive readable faces, warm metal, medieval sword-and-magic fantasy. White scroll canvas. Reference 1 is character identity only; reference 2 is the adopted series art style only. Never copy their layout or labels. Draw only characters mentioned in THIS moment; offscreen characters stay nearby, not cloned into every panel.
Kai: short tousled dark-brown hair, amber streak at his RIGHT temple, amber eyes, ivory rolled-sleeve shirt, brown leather vest, short navy shoulder cape, dark trousers, boots, ONE copper cuff LEFT forearm. BOTH HANDS BARE even though the old character sheet shows a glove. His ONE ordinary steel straight sword has square brass guard, black leather grip and ONE thin amber inset line. Sword RIGHT hand unless specified sheathed/on table. Amber line indicates slash enhancement, NEVER a flame sword or lightsaber. No spare drawn sword, no duplicate cuff. The sword has a SIMPLE narrow blade and small guard, one tiny vent by the guard, no industrial block or oversized mechanical box; a SMALL flat copper cooling plate only AFTER Episode 5 adds it. Sena: silver-blonde LOW ponytail, blue eyes, silver armor over navy cloth, long navy cape, ONE triangular silver-blue shield attached LEFT forearm; plain sword sheathed. In FRONT views her LEFT shield is on viewer RIGHT; in REAR views her LEFT shield is on viewer LEFT. Never mount it on her right arm. Iris: purple chin-length bob, green eyes, teal hood-down cloak, ivory tunic, dark skirt/leggings, ONE wood staff with ONE amber tip. Orun: older NPC smith, short gray beard, brown leather apron. Vane appears ONLY if named: tied-back ash-gray hair, silver armor, white cape. Faces and gestures express the current emotion, not the reference smile.
Speech uses exact Japanese, genuine vertical upright glyphs, top-to-bottom within columns, columns RIGHT TO LEFT; clean Japanese printed manga gothic, near 60px character height at 1024px width. Never rotate horizontal sentences. Use soft slender balloons with speaker tails for normal speech, stronger outline for urgency; thoughts use dots. Give ample inner padding; short columns at natural phrase boundaries. Do not shrink lettering to cram a long sentence. SFX are separate drawn lettering, outside balloons, follow material/motion and may cross panel frames and gutters. Specified ongoing SFX are ONE inscription continuing, not a full word repeated per panel. HUD is small translucent functional cyan, horizontal Japanese allowed, visible only to its owner; shared map pins only when specified. No unlisted text, labels, watermark, titles or panel numbers.
Compose intentionally unequal beats, varied close/medium/wide camera, staggered small close-ups for fast motion, borderless broad art for emotional results, diagonal frame boundaries only when action calls for them. Never use a uniform stacked rectangle grid. Reserve broad planned white spaces INSIDE this art; do not fill them with scenery or bonus panels. Dialogue/SFX/HUD must not obscure faces, hands, blade, shield, or clues. Follow top-to-bottom and right-to-left for any paired small inserts. Scene geometry and prop count stay causal. During combat, an active foe AHEAD must be in the foreground or offscreen in FRONT-facing party shots, never over their shoulders in the rear background. In BACK-facing party wide shots the foe may be distant ahead. Draw exactly this asset's events; withhold later replies, discoveries and future art.
'''

def prompt(ep, scene):
    state = ep['art_state']
    cast=scene.get('cast', ['Kai','Sena','Orun'] if ep['number']==2 and int(scene['id'])<10 else ['Kai','Sena','Iris'])
    if any('オルン' in p['art'] or p['speaker']=='オルン' for p in scene['panels']) and not any('Orun' in c for c in cast):
        cast=cast+['Orun']
    lines = [COMMON, 'EXCLUSIVE CAST for this asset: '+', '.join(cast)+'. Do NOT draw any other reference character. Iris is ABSENT unless explicitly listed here. RIGHT wrist/forearm has NO glove, bracelet, cuff or bracer; copper cuff ONLY LEFT forearm.', 'Current continuity: '+state,
             'Location/time: '+scene['location'], 'Scroll composition: '+scene['layout'],
             'What the reader understands: '+scene['understanding'],
             'Withhold: '+scene['withheld']]
    for i,p in enumerate(scene['panels'],1):
        lines.append(f"Beat {i}: {p['art']}")
        if p['text']:
            lines.append(f"Speaker {p['speaker']}, exact dialogue: {p['text']} Vertical columns right-to-left: {' / '.join(p['columns'])}. Voice: {p.get('voice','normal spoken')}.")
        else:
            lines.append('Dialogue: none; no speech or thought balloons in this beat.')
        for s in p.get('sounds',[]):
            lines.append(f"Originating SFX exact text {s['text']}: {s['source']}; {s['placement']}")
        for s in p.get('sound_continuations',[]):
            lines.append(f"Continue SAME SFX from {s['origin']}: {s['text']}; {s['placement']}; no new impact and no duplicate complete inscription.")
        for u in p.get('ui',[]):
            lines.append(f"HUD owner {u['owner']}, input {u['input']}, exact horizontal rows: {' | '.join(u['lines'])}. Visibility: {u['visibility']}.")
        if not any(p.get(k) for k in ['sounds','sound_continuations','ui']):
            lines.append('No additional SFX or HUD in this beat.')
    lines.append('After this asset: '+scene['pause']['purpose']+'. Outside pause at 390px width: '+str(scene['gap'])+'px. Do not draw the next reveal.')
    if scene.get('layout_en'):
        lines.append('MANDATORY LAYOUT, overrides reference compositions: '+scene['layout_en'])
    if scene.get('continuity_en'):
        lines.append('MANDATORY CURRENT STATE: '+scene['continuity_en'])
    return '\n'.join(lines)+'\n'

def prepare(number):
    folder=ROOT/f'episode-{number:02d}'
    ep=json.loads((folder/'episode.json').read_text())
    prompts=folder/'prompts'; prompts.mkdir(exist_ok=True)
    board=[f"# 第{number}話：{ep['title']}", '', ep['arc'], '', '本文の正本は episode.json。ここはそこから出力した縦ラフ。', '']
    for i,s in enumerate(ep['scenes'],1):
        value=prompt(ep,s)
        s['prompt']=value
        (prompts/f'{i:02d}.txt').write_text(value)
        board.extend([f"## {i:02d} {s['name']}", s['location'], s['layout'],
                      '読む理解：'+s['understanding'], '伏せる情報：'+s['withheld']])
        for p in s['panels']:
            board.append(f"- {p['art']}\n  {p['speaker']}「{p['text']}」" if p['text'] else '- '+p['art']+'（無言）')
            for a in p.get('sounds',[]): board.append('  発生音 '+a['text']+'：'+a['source']+'／'+a['placement'])
            for a in p.get('sound_continuations',[]): board.append('  持続音 '+a['text']+'：'+a['placement'])
            for a in p.get('ui',[]): board.append('  HUD：'+'／'.join(a['lines'])+'（'+a['owner']+'）')
        board.append(f"間：{s['gap']}px@390、{s['pause']['purpose']}。手掛かり：{s['pause']['cue']}。次に初出：{s['pause']['next']}。白地。\n")
    (folder/'episode.json').write_text(json.dumps(ep,ensure_ascii=False,indent=2)+'\n')
    (folder/'storyboard.md').write_text('\n'.join(board).rstrip()+'\n')
    (folder/'PROMPTS.md').write_text('\n\n'.join(f"## {i:02d}\n\n```text\n{s['prompt']}```" for i,s in enumerate(ep['scenes'],1))+'\n')
    print(f"Prepared {number}: {len(ep['scenes'])} assets / {sum(len(s['panels']) for s in ep['scenes'])} narrative beats")

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('episodes',type=int,nargs='+')
    for n in parser.parse_args().episodes:prepare(n)
