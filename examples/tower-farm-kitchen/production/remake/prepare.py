#!/usr/bin/env python3
"""Prepare the adopted episode 2–10 remake; never changes episode one."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
EPISODES=json.loads((Path(__file__).parent/'episodes.json').read_text())
STYLE='''Use case: illustration-story. Finished full-color Japanese vertical-scroll Webtoon, VERY TALL PORTRAIT 1:3. Warm refined adult anime art, confident ink lines, expressive natural adult faces, earthy painted shading, warm ivory unpainted whitespace. Reference 1 defines character identities and clothes ONLY, reference 2 place and materials ONLY, reference 3 large upright vertical Japanese lettering ONLY. Never copy reference layouts. This is a flowing scroll sequence, NOT a rectangular comic page. Vary moment sizes, narrow hand closeups, broad establishing view, asymmetric reaction faces, and an occasional borderless atmospheric passage. Not a uniform grid; not all equal full-width rectangles. Reserve generous ivory breathing space for the stated pause, while keeping quick practical actions close together.
CHARACTER IDENTITIES: Kou black-haired 28-year-old adult man, brown work jacket, cream shirt, dark green waist apron, rectangular brown leather tool satchel. Elna auburn low ponytail, blue headscarf, cream blouse, brick-red skirt, off-white apron. Balt gray-haired weathered 52-year-old male farmer, brown hat, olive work shirt. Iris 27-year-old WOMAN technician, short navy hair, copper goggles on forehead, gray workwear. Leon 34-year-old silver-gray-haired male supply officer, eyebrow scar, navy cloak and brown tunic, no drawn weapon. Only characters actually specified in scene may appear. Customer is an ordinary adult auburn-haired adventurer in ochre cloak, never Leon. Clerk beige robe, never Balt. Supplier or trader is ordinary brown-clothed adult. No random cast lineup.
WORLD: garden and blue-awning diner are INSIDE the tower beneath luminous sandstone ribs, no open sky, no modern electronics or modern plastic pipes, no giant magic vegetables, no magic buffs. Four modest long vegetable beds with three small subsections each, paths between, roots and leaves reflect stated time. Never depict future events.
TEXT: Integrate every exact supplied utterance ONCE as genuine upright vertical Japanese, top-to-bottom with columns RIGHT to LEFT. Printed crisp manga gothic. Large glyphs approximately 75px per 1024px canvas width, generous white balloon padding. Spoken speech has tail to the correct mouth, quiet speech soft thin oval; thoughts cloud with dots. Reading order follows listed lines DOWNWARD, not all balloons on one panel. Never print speaker names, quotation marks, annotations, instructions, page number or title. Keep faces, hands, clues unobstructed. No extra writing on notebook, diagram, sign, menu or contract: abstract marks only. Do not squeeze a conversation into one image-sized panel. Make successive visual moments for each turn and at least one silent establishing/action/reaction moment as described.
FOOD whenever present: mouthwatering clear ingredient silhouettes, soft glazed beef and carrot cuts, fresh soft green leaves, smooth russet-brown gravy with broad restrained gloss and gentle steam; softened barley mostly submerged. Avoid dense bead fields, stippling, pits, foam, individual pearl-like shiny grains. Same vessel, recipe and utensils across cooking, serving and bite. Farm tools and unwashed leaves never on clean cooking counter. Food rules add no food unless scene requires it.'''
# Scripted rhythm decisions belong to the scene's story, not a fixed gap template.
RHYTHMS=[
'Begin with a broad establishing view of the current location and modest plant state. Follow the first speaker with a closer listening reaction, then the next choice. Brief practical gesture, larger final expression. Location first, faces after. A short warm-ivory pause before the last response, not at every turn.',
'Focus on meeting or listening. Establish who stands where, break the supplied conversation into separate unequal close shots. One silent hand/eye response AFTER the important explanation. Let ivory space hold uncertainty before the last utterance. No future answer leaked above.',
'This is hands-on observation or preparation. Two small connected hand/tool closeups form a fast local pair, then a larger face who understands the result. Use a narrow bridge of soil, stone or tabletop to preserve location. Avoid long blanks interrupting the hand action. Slow down only before the conclusion.',
'Present the comparison or record before the conclusion. First show the tool/sample/book in context; close enough to understand its state, then a quiet listening face. Leave a noticeably longer unpainted ivory interval BEFORE the conclusion is shown, carrying only the prior clue or very faint background line. Vary panel widths.',
'Follow a practical decision into a concrete hand movement and its result. Keep contact, movement and outcome adjacent, then release into a larger borderless response and a small empty breathing interval. Dialogue turns in separate successive moments, never one crowded explanation box.',
'An emotional or technical turning point: establish the object and the speaker, move to listener, then a small no-dialogue hand detail. A broad warm-ivory quiet area at the hesitation, final face or choice below. The silence has no characters or invented labels inside it. No uniform comic grid.',
'Link task to people: broad situation, then handoff/preparation closeup, then the next speaker in a separate larger frame. Keep props physically consistent. A vertical trail of steam, a path, or a faint light rib can lead through sparse ivory space where physically justified; no decorative magic.',
'Episode close: modest achieved result in a large borderless scene, a small practical detail that remains unresolved, and larger quiet faces for the final exchange. Let the last voice fade into warm ivory. Protect the next episode: no extra event, crop, contract, or magic reward. Give an actual quiet ending rather than a poster.'
]
CAST={'コウ':'Kou','エルナ':'Elna','バルト':'Balt','イリス':'Iris','レオン':'Leon'}
def prompt(ep,i,s):
 cast=[name for ja,name in CAST.items() if any(ja in who for who,_ in s[2]) or name in s[1]]
 out=[STYLE,f'ONLY MAIN CAST IN THIS SEQUENCE: {", ".join(cast)}. Others absent. Supporting cast only when explicitly required. Never paint all people in the identity reference.',f'EPISODE {ep["number"]}; current time {ep["time"]}. Continuity limits (not extra panels): {ep["state"]}',f'CURRENT SEQUENCE ONLY: {s[1]}',f'SCROLL DIRECTING: {RHYTHMS[i]}','EXACT UTTERANCES, each as a successive beat, with listening/actions from the current scene between:']
 for who,line in s[2]:
  out.append(f'Speaker {who}. Exact text: {line}. Vertical columns RIGHT to LEFT: '+ ' / '.join(line[x:x+6] for x in range(0,len(line),6)))
 if ep['number']==2 and i==4:out.append('Small simple horizontal time caption at the very TOP ONLY: 五日目. White new roots revealed after the first leaf observation; partial recovery only. Do not repeat caption.')
 if ep['number']==8 and i==5:out.append('Focus the dish in a larger appetizing near-full-width borderless reveal BEFORE the customer lifts spoon. Do not include bite reaction, which belongs to next sequence.')
 if ep['number']==8 and i==7:out.append('Tonight prepare EMPTY containers and schedule only. Food will be cooked tomorrow, never pack warm food overnight.')
 if ep['number']==9 and i==5:out.append('Order is proof BEFORE team meal. Delivery count checks sealed containers and receipt; nobody is eating yet.')
 out.append('Only natural subtle sound effects at visible physical actions if specified: footsteps コツ, seed/soil hand サラ, clear pipe stream ちょろ, clean chopping トン. Do not add all sounds, choose only the actually occurring action. No dialogue invented. Silence/reaction is not automatically soundless. Never duplicate an utterance.')
 return '\n\n'.join(out)
if __name__=='__main__':
 jobs=[]
 for ep in EPISODES:
  directory=ROOT/f'episode-{ep["number"]:02d}'
  for i,s in enumerate(ep['scenes']):
   slug=s[5].get('adoptedId',f'{i+1:02d}-{s[0]}')
   p=directory/'generation'/f'{slug}.prompt.txt'
   if not p.exists() or not (p.parent/f'{slug}.json').exists():p.write_text(prompt(ep,i,s))
   jobs.append({'episode':ep['number'],'slug':slug,'prompt':p.read_text(),'target':str(directory/'art'/f'{slug}.png')})
 Path(__file__).with_name('jobs.json').write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n')
 print(f'Prepared {len(jobs)} distinct prompts')
