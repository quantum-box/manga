#!/usr/bin/env python3
"""Adopt only fully drawn continuation episodes; never list a script as a reader."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    continuation = json.loads((BASE / 'production/continuation-plan.json').read_text())
    records = json.loads((BASE / 'production/generation-records.json').read_text())
    for folder in ('continuation-generation-records', 'continuation-edits'):
        for path in sorted((BASE / 'production' / folder).glob('*.json')):
            record = json.loads(path.read_text())
            if not any(r.get('source') == record.get('source') for r in records):
                records.append(record)
            if record.get('edit_source') and not record.get('rejected'):
                for episode in continuation:
                    if episode['number'] == record['episode']:
                        for scene in episode['scenes']:
                            if scene['id'] == record['scene']:
                                scene['filename'] = record['adopted']
    write(BASE / 'production/generation-records.json', records)
    write(BASE / 'production/continuation-plan.json', continuation)
    drawn = [e for e in continuation if all((BASE / f'episode-{e["number"]:02}' / s['filename']).is_file() for s in e['scenes'])]
    missing = [(e['number'], s['id']) for e in drawn for s in e['scenes'] if not any(r['episode'] == e['number'] and r['scene'] == s['id'] and not r.get('edit_source') for r in records)]
    # A running generator saves artwork immediately before its sidecar record.
    # Leave that episode pending until both writes have completed.
    pending_records = {number for number, scene in missing}
    drawn = [e for e in drawn if e['number'] not in pending_records]
    old = json.loads((BASE / 'production/plan.json').read_text())
    merged = {e['number']: e for e in old}
    merged.update({e['number']: e for e in drawn})
    write(BASE / 'production/plan.json', [merged[n] for n in sorted(merged)])
    print(json.dumps({'fullyDrawn': [e['number'] for e in drawn], 'remaining': [e['number'] for e in continuation if e not in drawn], 'pendingRecords': missing}))

if __name__ == '__main__':
    main()
