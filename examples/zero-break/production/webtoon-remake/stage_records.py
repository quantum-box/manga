"""Write observed panel order, independently of the original requested layout."""
import argparse
import json
from pathlib import Path

STATE = Path(__file__).resolve().parent

def stage(number):
    plan = json.loads((STATE/f'episode-{number:02d}-plan.json').read_text())
    observed = json.loads((STATE/f'episode-{number:02d}-staging.json').read_text())
    assert set(observed) == {j['shotId'] for j in plan['jobs']}
    for job in plan['jobs']:
        path = STATE/'records'/f'{job["id"]}.json'
        record = json.loads(path.read_text())
        item = observed[job['shotId']]
        assert [p for row in item['rows'] for p in row] == list(range(1,len(item['beats'])+1))
        assert len(item['beats']) == record['actualPanelCount']
        assert len(item['speech']) == len(job['beforeShot']['lines'])
        panels = []
        for i,beat in enumerate(item['beats'],1):
            row_index,row = next((k,row) for k,row in enumerate(item['rows'],1) if i in row)
            frame = f'row {row_index}; '+('full-width panel' if len(row)==1 else f'horizontal row, right-to-left position {row.index(i)+1}/{len(row)}')
            panel = dict(beat=beat,view=beat,frame=frame,voice='無言')
            if i in item['speech']:
                line = job['beforeShot']['lines'][item['speech'].index(i)]
                panel['line'] = line
                panel['voice'] = 'thought cloud with dots' if line.get('type')=='thought' else 'spoken balloon with tail to mouth'
            panels.append(panel)
        record['panels'] = panels
        record['layout'] = dict(readingDirection='right-to-left, then downward',rowsInReadingOrder=item['rows'],
                                direction=job['layoutDirection'],observedPanelBeats=item['beats'])
        if item.get('geometryNote'):
            record['layout']['observedGeometry'] = item['geometryNote']
        path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')

if __name__ == '__main__':
    p = argparse.ArgumentParser();p.add_argument('episode',type=int)
    stage(p.parse_args().episode)
