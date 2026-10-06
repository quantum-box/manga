#!/usr/bin/env python3
from pathlib import Path
import json
base=Path(__file__).resolve().parents[1]
directory=base/'episode-01';manifest=json.loads((directory/'manifest.json').read_text())
batch=[]
for scene in manifest['scenes']:
    if scene['id'].startswith(('06-','07-')):continue
    ident=scene['id']+'-lettered'
    exact=' / '.join(speaker+'「'+line+'」' for speaker,line in scene['dialogue'])
    prompt='''Use case: precise-object-edit. The Japanese dialogue in this existing finished vertical comic is TOO SMALL at a 360px phone width. Edit ONLY the dialogue lettering and the necessary white speech/thought balloon areas. Enlarge EVERY Japanese dialogue glyph to approximately 1.7 TIMES its current height and width; final glyph height around 7 percent of full canvas width, including any small-panel dialogue. Enlarge balloons and reflow vertical columns to fit, with generous white inset. Do NOT make letters small to keep the original balloon size. Preserve ALL exact wording, punctuation, speakers and balloon reading order. Upright vertical Japanese: top-to-bottom, columns RIGHT TO LEFT. Do not display speaker labels or quotation marks. Thought stays a cloud with dots; speech tails stay attached to the correct speaker. Keep every panel boundary, character face/expression/pose/hand/clothing, tool, plant condition, bowl, food, architecture and color unchanged except the small areas needed for bigger balloons. Do not cover faces, hands or important evidence. Preserve any existing sound effects unchanged. No added people, words or repeated dialogue. Strong clean printed manga gothic, easy to read on a phone.
EXACT DIALOGUE IN ORDER: '''+exact
    prompt_path=directory/'generation'/f'{ident}.prompt.txt';prompt_path.write_text(prompt+'\n')
    batch.append({'id':ident,'scene_id':scene['id'],'target':str(directory/'art'/f'{ident}.png'),
                  'prompt':prompt,'referencePaths':[str(directory/scene['art'])]})
print(json.dumps(batch,ensure_ascii=False))
