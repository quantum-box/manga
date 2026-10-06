"""Persist and assemble the context/dialogue revision from actual image_gen outputs.

This script never generates or edits artwork and never drives a browser.
All generated PNGs are copied unchanged, with executed prompts and input hashes.
"""
from pathlib import Path
from struct import unpack
import argparse
import copy
import hashlib
import html
import json
import shutil
import subprocess
import sys
from history import baseline_reference, load_baseline

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
STATE = ROOT / 'production/feedback-v6'

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def directory(number):
    return ROOT / ('v5' if number == 1 else f'episode-{number:02d}')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_plan():
    return json.loads((STATE / 'plan.json').read_text())

def initialize():
    for number in range(1, 11):
        load_baseline(f'episode-{number:02d}.json')
    report()

def save(job_id, source, method='built-in image_gen'):
    job = next(j for j in load_plan()['jobs'] if j['id'] == job_id)
    source = Path(source).resolve()
    target = directory(job['episode']) / 'art' / job['file']
    record_path = STATE / 'records' / (job_id + '.json')
    if record_path.exists():
        raise ValueError(f'Already saved: {job_id}; create a separately named repair')
    raw = source.read_bytes()
    if raw[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('Expected unmodified PNG output')
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    width, height = unpack('>II', raw[16:24])
    dump(record_path, {
        'id': job_id, 'episode': job['episode'], 'file': job['file'],
        'method': 'reused skill reference (original built-in image_gen)' if job.get('reuse_source') else method, 'original_output': str(source),
        'sha256': digest(target), 'width': width, 'height': height,
        'prompt': job['prompt'], 'references': [
            {'path': p, 'sha256': digest(REPO / p)} for p in job['references']
        ], 'replaces': job['replaces'], 'panels': job['panels'],
        'visual_review': 'pending', 'mobile_browser_review': 'pending',
    })
    report()
    print(f'Saved {job_id}: {width}x{height}')

def repair(spec_path, source):
    spec = json.loads(Path(spec_path).read_text())
    record_path = STATE/'records'/(spec['id']+'.json')
    record = json.loads(record_path.read_text())
    previous = directory(record['episode'])/'art'/record['file']
    assert digest(previous) == record['sha256']
    target = directory(record['episode'])/'art'/spec['file']
    if target.exists():
        raise ValueError(f'Repair already exists: {target}')
    source = Path(source).resolve()
    raw = source.read_bytes()
    assert raw[:8] == b'\x89PNG\r\n\x1a\n'
    record.setdefault('repair_history', []).append(copy.deepcopy(record))
    record.setdefault('originalPrompt', record['prompt'])
    record.setdefault('originalReferences', record['references'])
    record['repairBefore'] = {'file':record['file'], 'sha256':record['sha256']}
    shutil.copyfile(source,target)
    width,height=unpack('>II',raw[16:24])
    record.update(file=spec['file'],sha256=digest(target),width=width,height=height,
                  prompt=spec['prompt'],original_output=str(source),
                  references=[{'path':p,'sha256':digest(REPO/p)} for p in spec['references']],
                  visual_review='pending',mobile_browser_review='pending')
    dump(record_path,record)
    print(f'Repaired {spec["id"]}; previous artwork preserved')

CSS = """*{box-sizing:border-box}body{margin:0;background:#18202b;color:#203045;font-family:'Hiragino Kaku Gothic ProN','Yu Gothic',sans-serif}.episode{width:100%;max-width:480px;margin:auto;container-type:inline-size;background:var(--paper)}header{padding:44px 24px 38px;background:#111a29;color:#eef8ff}header small{font-size:12px;color:#acd7ee}h1{font-size:clamp(29px,8cqw,39px);line-height:1.4;margin:14px 0}header p{font-size:15px;line-height:1.8;margin:0}.scene{position:relative;margin:0;width:var(--width,100%)}.scene img{display:block;width:100%;height:auto}.left{margin-right:auto}.right{margin-left:auto}.wide{margin-left:auto;margin-right:auto}.pause{height:var(--pause);background:var(--gap-paper,var(--paper))}.chapter-anchor{height:0}footer{padding:42px 22px 65px;text-align:center;font-size:15px;line-height:2}footer a{color:#365f8a;display:inline-block;margin:8px 12px}"""

def build(number):
    plan = load_plan()
    jobs = [j for j in plan['jobs'] if j['episode'] == number]
    missing = [j['id'] for j in jobs if not (STATE/'records'/(j['id']+'.json')).exists()]
    if missing:
        raise ValueError(f'Chapter remains on original edition; missing: {missing}')
    baseline = load_baseline(f'episode-{number:02d}.json')
    manifest = copy.deepcopy(baseline)
    for shot in manifest['shots']:
        if 'references' in shot:
            shot['references'] = [ref.replace('../v4/art/', '../production/references/')
                                  for ref in shot['references']]
    original = manifest['shots']
    positions = {s['id']: i for i, s in enumerate(original)}
    first = {}
    consumed = set()
    for job in jobs:
        indices = [positions[x] for x in job['replaces']]
        assert indices == list(range(indices[0], indices[-1]+1)), job['id']
        if consumed.intersection(job['replaces']):
            assert job.get('continuation_part') and job['replaces'][0] in first, job['id']
        consumed.update(job['replaces'])
        first.setdefault(job['replaces'][0], []).append(job)
    shots = []
    for old in original:
        if old['id'] in first:
            for job in first[old['id']]:
                record = json.loads((STATE/'records'/(job['id']+'.json')).read_text())
                target = directory(number)/'art'/record['file']
                assert digest(target) == record['sha256']
                shots.append({
                    'id':job['id'], 'file':record['file'], 'shape':'bleed',
                    'pause':job.get('pause',70), 'widthPercent':100,
                    'scene':job['context'], 'lines':[p['line'] for p in record['panels'] if p.get('line')],
                    'panels':record['panels'], 'visible_text':record.get('visible_text',[]),
                    'added_context_dialogue':job.get('added_context_dialogue',False),
                    'status':'generated', 'generated':True,
                    'prompt':record['prompt'], 'references':[r['path'] for r in record['references']],
                    'sha256':record['sha256'], 'provenance':'context-dialogue-v6',
                    'replaces':job['replaces'], 'visual_review':record['visual_review'],
                })
        elif old['id'] not in consumed:
            old['file'] += '.png' if number == 1 else ''
            original_path = directory(number)/'art'/old['file']
            assert digest(original_path) == old['baseline_sha256']
            old['widthPercent'] = plan.get('layout',{}).get(str(number),{}).get(old['id'],100)
            old['provenance_v6'] = 'retained adopted art; frame placement reviewed separately'
            shots.append(old)
    # Keep later, targeted sound edits when rebuilding the adopted story layout.
    sound_records = ROOT / 'production' / f'episode-{number:02d}-sfx' / 'records'
    for shot in shots:
        revision_path = sound_records / (shot['id'] + '.json')
        if not revision_path.exists():
            continue
        revision = json.loads(revision_path.read_text())
        assert revision['preservedLines'] == shot['lines']
        assert revision['preservedVisibleText'] == shot.get('visible_text', [])
        assert revision['panels'] == shot.get('panels', [])
        assert digest(directory(number)/'art'/revision['file']) == revision['sha256']
        before = revision['repairBefore']
        assert digest(directory(number)/'art'/before['file']) == before['sha256']
        shot.update(file=revision['file'], sounds=revision['sounds'],
                    sha256=revision['sha256'], prompt=revision['prompt'],
                    references=[r['path'] for r in revision['references']],
                    provenance='targeted raster sound-effect edit',
                    revisionRecord=str(revision_path.relative_to(REPO)),
                    visual_review=revision['visual_review'])
    insertion_plan = sound_records.parent / 'inserts.json'
    if insertion_plan.exists():
        additions = json.loads(insertion_plan.read_text())
        for addition in additions['inserts']:
            record_path = REPO / addition['record']
            record = json.loads(record_path.read_text())
            assert not any(s['id'] == record['shot']['id'] for s in shots)
            assert digest(directory(number)/'art'/record['shot']['file']) == record['sha256']
            for reference in record['references']:
                assert digest(REPO/reference['path']) == reference['sha256']
            position = next(i for i,s in enumerate(shots) if s['id'] == addition['after'])
            shot = copy.deepcopy(record['shot'])
            shot.update(prompt=record['prompt'], sha256=record['sha256'],
                        references=[r['path'] for r in record['references']],
                        insertionRecord=str(record_path.relative_to(REPO)), replaces=[],
                        provenance='armor assembly insert', generated=True,
                        visual_review=record['visual_review'])
            shots.insert(position+1, shot)
        for shot in shots:
            if shot['id'] in additions.get('pauseOverrides', {}):
                shot['pause'] = additions['pauseOverrides'][shot['id']]
    layout_records = ROOT / 'production' / f'episode-{number:02d}-layout' / 'records'
    for shot in shots:
        record_path = layout_records / (shot['id'] + '.json')
        if not record_path.exists():
            continue
        record = json.loads(record_path.read_text())
        before = record['beforeShot']
        for key in ('id','file','lines','panels','sounds','visible_text','pause','widthPercent','shape','sha256','prompt','replaces'):
            assert before.get(key) == shot.get(key), (shot['id'], key)
        assert digest(directory(number)/'art'/before['file']) == before['sha256']
        assert digest(directory(number)/'art'/record['file']) == record['sha256']
        assert len(record['panels']) == len(before['panels'])
        for old, new in zip(before['panels'], record['panels']):
            assert {k:v for k,v in old.items() if k!='frame'} == {k:v for k,v in new.items() if k!='frame'}
        for reference in record['references']:
            assert digest(REPO/reference['path']) == reference['sha256']
        shot.update(file=record['file'], panels=record['panels'],
                    prompt=record['prompt'], sha256=record['sha256'],
                    references=[r['path'] for r in record['references']],
                    layoutRevisionRecord=str(record_path.relative_to(REPO)),
                    layout=record['layout'], provenance='panel layout recomposition',
                    visual_review=record['visual_review'])
    manifest.update(version='context-dialogue-v6', shots=shots,
                    panel_count=sum(len(s.get('panels',[s])) for s in shots),
                    baseline=baseline_reference(f'episode-{number:02d}.json'))
    dump(directory(number)/'manifest.json',manifest)
    title = manifest.get('title','最弱判定、最強の一歩。')
    paper = '#fffaf3' if number in (4,9) else '#f6f7f8' if number == 5 else '#ffffff'
    out = [f'<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ゼロ・ブレイク 第{number}話</title><style>{CSS}</style><main class="episode" style="--paper:{paper}">',f'<header><small>異世界転生 × スーパーヒーロー / 第{number}話</small><h1>ゼロ・ブレイク</h1><p>{html.escape(title)}</p></header>']
    storyboard = [f'# 第{number:02d}話 {title} — 会話と状況の改稿','',
                  'セリフは原画に収録。HTMLへ二重に重ねない。旧構成は Git の履歴で管理。','']
    for shot in shots:
        path = directory(number)/'art'/shot['file']
        width,height = unpack('>II',path.read_bytes()[16:24])
        alt = shot.get('alt_ja',shot['scene']) + ' ' + ' '.join(l['speaker']+'『'+l['text']+'』' for l in shot['lines'])
        alt += ' ' + ' '.join(t['text'] for t in shot.get('visible_text',[]))
        alt += ' ' + ' '.join('効果音『'+sound+'』' for sound in shot.get('sounds',[]))
        out.append(f'<figure class="scene {shot["shape"]}" id="{shot["id"]}" style="--width:{shot["widthPercent"]}%"><img src="art/{shot["file"]}" width="{width}" height="{height}" alt="{html.escape(alt,quote=True)}"></figure>')
        out.append(f'<div class="pause" aria-hidden="true" style="--pause:{shot["pause"]/390*100:.2f}cqw"></div>')
        storyboard += [f'## {shot["id"]}', '', shot['scene'], '', f'表示幅：{shot["widthPercent"]}%。次までの間：390px幅で{shot["pause"]}px相当。', '']
        for i,panel in enumerate(shot.get('panels',[]),1):
            storyboard += [f'### コマ{i}', '',panel['beat'],'',f'注目と接続：{panel["view"]}',f'大きさと枠：{panel["frame"]}',f'声：{panel.get("voice","無言")}', '']
        storyboard += [l['speaker']+'：'+l['text'] for l in shot['lines']] + ['']
        storyboard += [f'画面内表示：{t["text"]}' for t in shot.get('visible_text',[])] + ['']
        storyboard += [f'効果音：{sound}' for sound in shot.get('sounds',[])] + ['']
    prev = '../v5/index.html' if number == 2 else f'../episode-{number-1:02d}/index.html'
    nav = '<a href="../chapters.html">話一覧</a>'
    if number > 1: nav += f'<a href="{prev}">前の話</a>'
    if number < 10: nav += f'<a href="../episode-{number+1:02d}/index.html">次の話</a>'
    out.append(f'<footer>第{number}話 おわり<br>{nav}</footer></main></html>')
    (directory(number)/'index.html').write_text(''.join(out))
    (directory(number)/'storyboard.md').write_text('\n'.join(storyboard).rstrip()+'\n')
    archive=baseline_reference(f'generation-episode-{number:02d}.json')
    old_log=directory(number)/'generation-log.json'
    execution=[]
    for shot in shots:
        record_path=STATE/'records'/(shot['id']+'.json')
        if shot.get('layoutRevisionRecord'):
            record_path = REPO / shot['layoutRevisionRecord']
        elif shot.get('revisionRecord'):
            record_path = REPO / shot['revisionRecord']
        elif shot.get('insertionRecord'):
            record_path = REPO / shot['insertionRecord']
        record=json.loads(record_path.read_text()) if record_path.exists() else {
            'id':shot['id'],'file':shot['file'],'sha256':digest(directory(number)/'art'/shot['file']),
            'method':'retained prior adopted image_gen output',
            'prompt':shot.get('prompt',f'See {baseline_reference(f"prompts-episode-{number:02d}.md")} for the original executed prompt.'),
            'references':shot.get('references',[]),
            'provenance_record':archive,
        }
        execution.append(record)
    dump(old_log,{'edition':'context-dialogue-v6','adopted':execution,
                 'prior_generation_record':archive})
    prompt_lines=[f'# 第{number:02d}話 — 採用原画の実行指示','',
                  '全10話の改稿は新規54素材・承認見本の再利用3素材。再利用・修正・採用原画の保持を generation-log.json で区別。以前の実行記録は Git の履歴で管理。','']
    sound_count = sum(bool(s.get('revisionRecord')) for s in shots)
    insert_count = sum(bool(s.get('insertionRecord')) for s in shots)
    layout_count = sum(bool(s.get('layoutRevisionRecord')) for s in shots)
    if sound_count or insert_count:
        prompt_lines += [f'この話の追加改稿：既存{sound_count}素材の効果音編集・{insert_count}素材の装着過程追加。元画像・修正前画像・実行指示は production/episode-{number:02d}-sfx に保持。','']
    if layout_count:
        prompt_lines += [f'その後のコマ割り改稿：{layout_count}素材を横並び・斜め枠へ再構成。読順・元画像・指示は production/episode-{number:02d}-layout に保持。','']
    for r in execution:
        prompt_lines += ['## '+r['file'],'',r['method'],'',
                         '参照：'+json.dumps(r.get('references',[]),ensure_ascii=False),'']
        if r.get('originalPrompt'):prompt_lines += ['元の生成指示：','','```text',r['originalPrompt'],'```','']
        prompt_lines += ['採用時の指示：','','```text',r.get('prompt',''),'```','']
    (directory(number)/'PROMPTS.md').write_text('\n'.join(prompt_lines))
    subprocess.run([sys.executable,str(REPO/'skills/webtoon/scripts/package_reader.py'),str(directory(number)/'index.html'),'--output',str(directory(number)/'reader.html'),'--force'],check=True)
    validation_path=directory(number)/'validation.json'
    current_hash=digest(directory(number)/'index.html')
    prior_validation=json.loads(validation_path.read_text()) if validation_path.exists() else {}
    if prior_validation.get('readerSourceSha256')==current_hash:
        report()
        print(f'Built chapter {number}: unchanged reviewed reader')
        return
    dump(validation_path,{
        'edition':'context-dialogue-v6', 'panels':manifest['panel_count'],
        'readerSourceSha256':current_hash,
        'source_assets_verified':True,'visualReview':{'status':'pending'},
        'mobileBrowserReview':{'status':'pending','note':'Prior edition review does not apply to revised art.'},
        'physicalDeviceTested':False,
    })
    report()
    print(f'Built chapter {number}: {len(shots)} assets, {manifest["panel_count"]} panels')

def report():
    plan_path = STATE/'plan.json'
    jobs = load_plan()['jobs'] if plan_path.exists() else []
    saved = [j for j in jobs if (STATE/'records'/(j['id']+'.json')).exists()]
    rows = []
    for n in range(1,11):
        chapter_jobs = [j for j in jobs if j['episode'] == n]
        done = [j for j in saved if j['episode'] == n]
        current = json.loads((directory(n)/'manifest.json').read_text())
        validation=json.loads((directory(n)/'validation.json').read_text())
        rows.append({'episode':n,'planned_assets':len(chapter_jobs),'saved_assets':len(done),
                     'reader_revision_built':current.get('version')=='context-dialogue-v6',
                     'panels':current.get('panel_count'),
                     'native_visual_review':validation.get('visualReview',{}).get('status','pending'),
                     'browser_review':validation.get('mobileBrowserReview',{}).get('status','pending')})
    dump(STATE/'status.json',{'scope':'Illustrated episodes 1-10; panel staging for all 50 scripts; episodes 11-50 have no artwork',
                           'planned_assets':len(jobs),'saved_assets':len(saved),'episodes':rows,
                           'next_asset':next((j['id'] for j in jobs if j not in saved),None)})
    lines = ['# ゼロブレイク・フィードバック反映の進行台帳','',
             '第1〜10話の既存原画を保持して改稿。全50話のコマ別脚本を更新。第11〜50話の作画は未制作。', '',
             f'改稿素材：{len(saved)}/{len(jobs)}を保存（新規生成54・承認見本再利用3）。', '',
             '|話|改稿素材|コマ|画像目視|ブラウザ|', '|---|---:|---:|---|---|']
    lines += [f'|{r["episode"]}|{r["saved_assets"]}/{r["planned_assets"]}|{r["panels"]}|{r["native_visual_review"]}|{r["browser_review"]}|' for r in rows]
    lines += ['', '次の作画：'+next((j['id'] for j in jobs if j not in saved),'作画素材は保存済み'), '',
              '各画像の実行プロンプト・参照とハッシュ：feedback-v6/records。未生成・未確認は完成としない。','']
    (ROOT/'production/status.md').write_text('\n'.join(lines))

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['init','save','repair','build','report'])
    parser.add_argument('value',nargs='?')
    parser.add_argument('source',nargs='?')
    args=parser.parse_args()
    if args.action=='init': initialize()
    elif args.action=='save': save(args.value,args.source)
    elif args.action=='repair': repair(args.value,args.source)
    elif args.action=='build': build(int(args.value))
    else: report()
