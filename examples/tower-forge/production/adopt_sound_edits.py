#!/usr/bin/env python3
"""Adopt all reviewed sound edits together and retain exact execution history."""
import hashlib
import json
from pathlib import Path
from panel_lettering import normalize_panel, panel_board

ROOT=Path(__file__).resolve().parents[1]

def write(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    d=ROOT/'episode-01'
    ep=json.loads((d/'episode.json').read_text())
    manifest=json.loads((ROOT/'production/sound-edits/manifest.json').read_text())
    design=json.loads((ROOT/'production/episode-01-sound-design.json').read_text())
    provenance=json.loads((ROOT/'production/revision-provenance.json').read_text())
    by_file={x['file']:x for x in provenance}
    adopted=json.loads((ROOT/'production/adopted-assets.json').read_text())
    for edit in manifest:
        target=d/edit['destination']
        assert target.is_file(),target
        record=by_file[edit['destination']]
        assert hashlib.sha256(target.read_bytes()).hexdigest()==record['sha256'],target
        assert record['prompt']==edit['prompt'],target
        assert record['references']==['episode-01/'+edit['source']],target
        assert ep['scenes'][edit['scene']-1]['file'] in [edit['source'],edit['destination']],edit
    for scene in ep['scenes']:
        scene['prompt_role']='executed_initial_generation_before_sound_edits'
        scene['next_generation_prompt_file']='PROMPTS-NEXT.md#r'+scene['id']
        scene['panels']=[normalize_panel(p) for p in scene['panels']]
        for panel in scene['panels']:
            panel['sounds']=[]
            panel['quiet_reason']='会話・知覚・反応に集中する静かな区間。'
    for key,cues in design['panels'].items():
        i,j=map(int,key.split('-'))
        panel=ep['scenes'][i-1]['panels'][j-1]
        panel['sounds']=cues
        panel['quiet_reason']=''
    for edit in manifest:
        i=edit['scene'];scene=ep['scenes'][i-1]
        scene['file']=edit['destination']
        scene.setdefault('executed_sound_edits',[])
        if edit['prompt_file'] not in scene['executed_sound_edits']:
            scene['executed_sound_edits'].append(edit['prompt_file'])
        adopted[f'1-{i}']=dict(file=edit['destination'],reason='無言と無音を分け、動作音を吹き出しから独立させる部分編集')
    ep['sound_revision']='dialogue_and_sfx_independent_2026_10_07'
    ep['sound_cue_count']=sum(len(p['sounds']) for s in ep['scenes'] for p in s['panels'])
    write(d/'episode.json',ep)
    episodes=json.loads((ROOT/'production/episodes.json').read_text());episodes[0]=ep
    write(ROOT/'production/episodes.json',episodes);write(ROOT/'production/adopted-assets.json',adopted)
    board=['# 第1話 この剣で、一緒に\n','55の物語コマ。発話と効果音を独立して記録。無言はセリフなし、無音は効果音もなし。停電は第2話へ送る。\n']
    for i,scene in enumerate(ep['scenes'],1):
        board += [f"\n## {i:02d} {scene['name']}\n",f"場所・接続：{scene['location']}\n",f"この区間で理解すること：{scene['purpose']}\n",f"次の間：390px幅で{scene['gap']}px。\n"]
        for j,p in enumerate(scene['panels'],1):
            board += [f"\n{j}. {p['art']}\n",panel_board(p),'   - 同じ場所、視線と道具を継承。文字は顔・手・排熱溝・接触点を避ける。\n']
    (d/'storyboard.md').write_text(''.join(board))
    for filename in ['PROMPTS.md','PROMPTS-USED.md']:
        path=d/filename;original=path.read_text()
        marker='\n## 2026-10-07 発話と効果音を分けた実行済み部分編集\n'
        original=original.split(marker)[0]
        path.write_text(original+marker+'\n前の指示は実使用履歴として保持。次回生成用の修正版は PROMPTS-NEXT.md。以下は実行済み編集のみ。\n'+''.join(f"\n### r{x['scene']:02d}-sounds\n\n```text\n{x['prompt']}\n```\n" for x in manifest))
    validation=json.loads((d/'validation.json').read_text())
    validation.update(sound_revision=ep['sound_revision'],raster_lettering_visual='pending_model_review',story_quality_approved_by_user=False)
    write(d/'validation.json',validation)
    print(f"Adopted {len(manifest)} native edits and {ep['sound_cue_count']} independent sound cues. Browser review still pending.")

if __name__=='__main__':main()
