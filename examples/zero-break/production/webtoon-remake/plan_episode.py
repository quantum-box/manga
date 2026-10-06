"""Record scene-specific direction before calling built-in image_gen."""
import argparse
import json
from pathlib import Path

STATE = Path(__file__).resolve().parent
REPO = STATE.parents[3]

def plan(episode, directions):
    destination = STATE / f'episode-{episode:02d}-plan.json'
    if destination.exists():
        raise ValueError(f'Plan already exists: {destination}')
    previous = json.loads((STATE / 'episode-02-plan.json').read_text())
    common = previous['jobs'][0]['prompt'].split('Existing moment and strict continuity:')[0]
    common += '''\nNoa18 if present: ORANGE short tousled hair, GREEN eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, ORANGE work gloves. No new form or changed identity. Commander if present: mature45 short black hair greying temples, black-trim beard, navy cape and silver/gold armor; never confused with young silver-haired Rook.\nIMPORTANT PHONE LETTERING: actual glyph height60-70px on1024px-wide output, including when output is1024x1536. Reflow long dialogue to 3-4 columns of no more than6 upright glyphs per column; enlarge speech panel/balloon rather than shrink text. Preserve exact complete wording and punctuation. Calm speech thin oval/capsule; fatigue softly wavering; warning/shout jagged outside; thought cloud and dots. Only scene-specified bodies/props, no duplicates within same panel.\n'''
    manifest = json.loads((REPO / f'examples/zero-break/episode-{episode:02d}/manifest.json').read_text())
    assert set(directions) == {s['id'] for s in manifest['shots']}
    jobs = []
    for shot in manifest['shots']:
        direction = directions[shot['id']]
        references = [f'examples/zero-break/episode-{episode:02d}/art/{shot["file"]}',
                      'skills/webtoon/references/zero-break/layout-sequence-390.png']
        props = direction.get('visibleText', shot.get('visible_text', []))
        prompt = common + '\nExisting moment and strict continuity: ' + shot['scene']
        prompt += '\nExact layout, camera and mechanics: ' + direction['layout']
        prompt += '\nExact speech in chronological order: ' + json.dumps(shot['lines'], ensure_ascii=False)
        prompt += '\nExact effects (each once, near physical cause): ' + json.dumps(direction['sounds'], ensure_ascii=False)
        prompt += '\nExact visible prop text: ' + json.dumps(props, ensure_ascii=False) + '. No other text.\n'
        jobs.append(dict(id=f'e{episode:02d}-{shot["id"]}', episode=episode, shotId=shot['id'],
                         beforeShot=shot, file=f'remake-{shot["id"]}.png', references=references,
                         prompt=prompt, layoutDirection=direction['layout'], sounds=direction['sounds'],
                         visibleText=props, status='planned'))
    destination.write_text(json.dumps(dict(sourceCommit=previous['sourceCommit'], jobs=jobs), ensure_ascii=False, indent=2)+'\n')
    print(f'Planned episode {episode}: {len(jobs)} assets')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('episode', type=int)
    p.add_argument('directions', type=Path)
    args = p.parse_args()
    plan(args.episode, json.loads(args.directions.read_text()))
