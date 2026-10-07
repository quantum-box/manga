#!/usr/bin/env python3
"""Adopt reviewed native scroll compositions and keep actual prompts traceable."""
import hashlib
import json
from pathlib import Path
from panel_lettering import panel_board

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'production/scroll-revision'

def write(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    current=json.loads((ROOT/'episode-01/episode.json').read_text())
    if current.get('event_revision'):
        raise SystemExit('Tower incident already adopted; do not replace it with an older scroll plan.')
    ep=json.loads((FOLDER/'episode.json').read_text())
    manifest=json.loads((FOLDER/'manifest.json').read_text())
    records={x['file']:x for x in json.loads((ROOT/'production/revision-provenance.json').read_text())}
    for asset in manifest:
        assert hashlib.sha256((ROOT/'episode-01'/asset['source']).read_bytes()).hexdigest()==asset['source_sha256']
        s=ep['scenes'][asset['scene']-1]
        s['executed_scroll_edits']=[]
        for edit in [asset,*asset.get('followups',[])]:
            r=records[edit['destination']];file=ROOT/'episode-01'/edit['destination']
            assert file.read_bytes()==Path(r['source']).read_bytes(),file
            assert hashlib.sha256(file.read_bytes()).hexdigest()==r['sha256'],file
            assert r['prompt']==edit['prompt']==(ROOT/edit['prompt_file']).read_text(),file
            assert r['references']==['episode-01/'+edit['source']],file
            s['file']=edit['destination'];s['executed_scroll_edits'].append(edit['prompt_file'])
        s['prompt']=asset['prompt'];s['prompt_role']='executed_native_scroll_recomposition_before_followups'
    assert sum(len(s['panels']) for s in ep['scenes'])==ep['narrative_panel_count']==68
    write(ROOT/'episode-01/episode.json',ep)
    eps=json.loads((ROOT/'production/episodes.json').read_text());eps[0]=ep
    write(ROOT/'production/episodes.json',eps)
    adopted=json.loads((ROOT/'production/adopted-assets.json').read_text())
    for i,s in enumerate(ep['scenes'],1):adopted[f'1-{i}']=dict(file=s['file'],reason='物語とゲーム設定を保ち、枠なしの縦の背景・短い横並び・待つ余白を使い分ける採用版')
    write(ROOT/'production/adopted-assets.json',adopted)
    catalog_file=ROOT.parents[1]/'content/catalog.json'
    catalog=json.loads(catalog_file.read_text())
    for title in catalog:
        if title['id']=='tower-forge':title['cover']='episode-01/'+ep['scenes'][ep.get('cover_scene',1)-1]['file']
    write(catalog_file,catalog)
    board=[f"# 第1話 この剣で、一緒に\n\n68の物語上の瞬間、18原画。矩形コマの数ではない。スクロール構図の採用版。\n"]
    for i,s in enumerate(ep['scenes'],1):
        board.append(f"\n## {i:02d} {s['name']}\n\n場所：{s['location']}\n\n読者の理解：{s['purpose']}\n\n次の間：390幅で{s['gap']}px。{s['gap_purpose']}。\n")
        if s.get('scroll_layout'):board.append('\n構図：'+s['scroll_layout']['composition']+'\n読順：'+s['scroll_layout']['read_order']+'\n')
        for j,q in enumerate(s['panels'],1):board.append(f"\n{j}. {q['art']}\n"+panel_board(q))
    (ROOT/'episode-01/storyboard.md').write_text(''.join(board))
    marker='\n## 2026-10-07 スクロール構図の実行済み改稿\n'
    used=['\n組み込み image_gen による原画の再構成。実際に実行した指示と参照を記録。次回用指示は未実行として別保存。\n']
    for asset in manifest:
        for edit in [asset,*asset.get('followups',[])]:used.append(f"\n### {edit['destination']}\n\n参照：episode-01/{edit['source']}。方式：native_scroll_recomposition。\n\n```text\n{edit['prompt']}\n```\n")
    for name in ['PROMPTS.md','PROMPTS-USED.md']:
        f=ROOT/'episode-01'/name;f.write_text(f.read_text().split(marker)[0]+marker+''.join(used))
    review=json.loads((ROOT/'episode-01/validation.json').read_text())
    review.update(scroll_revision=ep['scroll_revision'],raster_lettering_visual='pending_model_review',story_quality_approved_by_user=False)
    write(ROOT/'episode-01/validation.json',review)
    print('Adopted 8 scroll compositions; mobile review pending.')

if __name__=='__main__':main()
