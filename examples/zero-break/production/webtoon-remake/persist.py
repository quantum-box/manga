"""Save unmodified built-in image_gen output and its actual execution provenance."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path
from struct import unpack

STATE = Path(__file__).resolve().parent
REPO = STATE.parents[3]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def save(episode, shot_id, source, count):
    plan_path = STATE / f'episode-{episode:02d}-plan.json'
    plan = json.loads(plan_path.read_text())
    job = next(j for j in plan['jobs'] if j['shotId'] == shot_id)
    record_path = STATE / 'records' / f'{job["id"]}.json'
    if record_path.exists():
        raise ValueError(f'Already recorded: {record_path}')
    target = REPO / f'examples/zero-break/episode-{episode:02d}/art' / job['file']
    source = Path(source).resolve()
    raw = source.read_bytes()
    assert raw[:8] == b'\x89PNG\r\n\x1a\n'
    shutil.copyfile(source, target)
    width, height = unpack('>II', raw[16:24])
    record = dict(job, output=str(target.relative_to(REPO)), sha256=sha(target),
                  generatedOutput=str(source), width=width, height=height,
                  actualPanelCount=count, nativeFullSizeReview='passed',
                  mobileImageReview='pending', browserReview='pending',
                  method='built-in image_gen', referenceHashes=[
                      dict(path=p, sha256=sha(REPO / p)) for p in job['references']])
    dump(record_path, record)
    job['status'] = 'generated_full_size_review_passed'
    dump(plan_path, plan)
    print(f'Saved {job["id"]}: {width}x{height}, {count} panels')

def repair(episode, shot_id, source, prompt, before_source, count):
    plan_path = STATE / f'episode-{episode:02d}-plan.json'
    plan = json.loads(plan_path.read_text())
    job = next(j for j in plan['jobs'] if j['shotId'] == shot_id)
    record_path = STATE / 'records' / f'{job["id"]}.json'
    if record_path.exists():
        record = json.loads(record_path.read_text())
        history = dict(record)
        history.pop('repairHistory', None)
        record.setdefault('repairHistory', []).append(history)
        before = REPO / record['output']
        assert sha(before) == record['sha256']
        target = before.with_name(before.stem + '-r2.png')
    else:
        before = STATE / 'references' / f'{job["id"]}-before-correction.png'
        before.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(before_source, before)
        save(episode, shot_id, source, count)
        record = json.loads(record_path.read_text())
        target = REPO / record['output']
    if Path(source).resolve() != target.resolve():
        shutil.copyfile(source, target)
    raw = target.read_bytes()
    assert raw[:8] == b'\x89PNG\r\n\x1a\n'
    width, height = unpack('>II', raw[16:24])
    record.update(file=target.name, output=str(target.relative_to(REPO)),
                  sha256=sha(target), generatedOutput=str(Path(source).resolve()),
                  width=width, height=height, actualPanelCount=count,
                  executedRepairPrompt=prompt, nativeFullSizeReview='passed',
                  mobileImageReview='pending', browserReview='pending',
                  repairBefore=dict(path=str(before.relative_to(REPO)),sha256=sha(before)))
    dump(record_path,record)
    job['status'] = 'generated_full_size_review_passed'
    dump(plan_path,plan)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('episode', type=int)
    parser.add_argument('shot_id')
    parser.add_argument('source')
    parser.add_argument('count', type=int)
    args = parser.parse_args()
    save(args.episode, args.shot_id, args.source, args.count)
