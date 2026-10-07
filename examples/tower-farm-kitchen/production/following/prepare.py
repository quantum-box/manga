#!/usr/bin/env python3
"""Prepare one continuation chapter; keep previously executed prompts intact."""
import json
from pathlib import Path
import runpy
import re
import sys

BASE = Path(__file__).resolve().parents[2]
HERE = Path(__file__).parent
STYLE = runpy.run_path(str(HERE.parent / 'remake/prepare.py'))['STYLE']
STYLE = STYLE.replace('no magic buffs', 'only explicitly established conditional magical food effects')
STYLE = STYLE.replace('Customer is an ordinary adult auburn-haired adventurer in ochre cloak, never Leon.', 'Unnamed customers have distinct ordinary faces and brown traveling clothes. Never substitute Row, Sera, Rodel or Leon for an anonymous traveler.')
STYLE += '''
NEW LETTERING: omit Japanese commas and full stops. Ignore punctuation in the old lettering references. Supplied line breaks become vertical columns at meaningful phrase boundaries. Do not split words or strand particles. Sound effects are action lettering outside speech balloons.
Reference 4 supplies new identities only: left Row (ロウ), center Sera (セラ), right Rodel (ロデル). Do not draw anyone from this sheet unless explicitly required in THIS sequence. Row has an ochre cloak and rust-auburn short hair; Sera has a teal cloak, black low braid and wooden blue-stone staff; Rodel has a moss-green coat, silver temple streak and trimmed beard. Do not replace anonymous supporting travelers with these named characters.
No invented inscriptions, titles, episode numbers, production labels, or extra dialogue. Future story events in the continuity notes are not extra panels.
'''


def prepare(number):
    episode = next(e for e in json.loads((HERE / 'episodes.json').read_text()) if e['number'] == number)
    directory = BASE / f'episode-{number:02d}'
    (directory / 'generation').mkdir(parents=True, exist_ok=True)
    jobs = []
    for scene in episode['scenes']:
        slug, description, dialogue, layout, pause, details = scene
        adopted = details.get('adoptedId', slug)
        prompt_path = directory / 'generation' / f'{adopted}.prompt.txt'
        if not prompt_path.exists():
            names=details['visibleCast']
            cast='VISIBLE NAMED CAST: '+(', '.join(names) if names else 'none')+'. Do not introduce any other named character from reference sheets. Anonymous extras are only those specified in the sequence.'
            parts = [STYLE, cast, f'Current time: {episode["time"]}.',
                     f'CURRENT SEQUENCE ONLY: {description}',
                     f'Scroll purpose: {details["scrollPurpose"]}',
                     'Draw successive unequal visual moments. Fast gestures may form a small right-to-left pair; the stated reveal can be borderless. Reserve readable balloons and safe ivory gutters between actual narrative beats. Portrait about 1:3. Do not compress waiting and payoff into one moment.']
            for speaker, words in dialogue:
                parts.append(f'Speaker {speaker}: exact text and upright vertical columns RIGHT to LEFT: ' +
                             ' / '.join(words.splitlines()) + '. Slash separators are instructions, never printed.')
            for sound in details.get('soundEffects', []):
                parts.append('Exact sound outside balloons at its physical source: ' + ' '.join(sound.splitlines()))
            prompt_path.write_text('\n\n'.join(parts) + '\n')
        jobs.append({'episode': number, 'slug': adopted, 'prompt': prompt_path.read_text(),
                     'target': str(directory / 'art' / f'{adopted}.png')})
    (HERE / f'jobs-{number:02d}.json').write_text(json.dumps(jobs, ensure_ascii=False, indent=2) + '\n')
    print(f'Prepared episode {number}: {len(jobs)} distinct sequences')


if __name__ == '__main__':
    for number in sys.argv[1:]:
        prepare(int(number))
