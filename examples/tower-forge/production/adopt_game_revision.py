#!/usr/bin/env python3
"""Adopt the complete reviewed game revision with original native provenance."""
import hashlib
import json
from pathlib import Path
from panel_lettering import panel_board

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'production/game-revision'

def write(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    ep=json.loads((FOLDER/'episode.json').read_text())
    manifest=json.loads((FOLDER/'manifest.json').read_text())
    provenance=json.loads((ROOT/'production/revision-provenance.json').read_text())
    records={r['file']:r for r in provenance}
    for asset in manifest:
        file=ROOT/'episode-01'/asset['destination']
        record=records[asset['destination']]
        assert file.is_file() and hashlib.sha256(file.read_bytes()).hexdigest()==record['sha256'],file
        assert record['prompt']==asset['prompt'],file
        assert record['references']==['episode-01/'+asset['source']],file
        scene=ep['scenes'][asset['scene']-1]
        scene['executed_game_edits']=[asset['prompt_file']]+asset.get('followup_prompt_files',[])
        for followup in asset.get('followups',[]):
            final=ROOT/'episode-01'/followup['destination']
            r=records[followup['destination']]
            assert hashlib.sha256(final.read_bytes()).hexdigest()==r['sha256'],final
            assert r['prompt']==followup['prompt'],final
            assert r['references']==['episode-01/'+followup['source']],final
            scene['file']=followup['destination']
        if asset['mode']=='new_adjacent_strip':
            scene['prompt']=asset['prompt']
            scene['prompt_role']='executed_new_game_scene_before_followup_edits'
    ep['sound_cue_count']=sum(len(p.get('sounds',[])) for s in ep['scenes'] for p in s['panels'])
    for s in ep['scenes']:s['next_generation_prompt_file']='PROMPTS-NEXT.md#r'+s['id']
    write(ROOT/'episode-01/episode.json',ep)
    episodes=json.loads((ROOT/'production/episodes.json').read_text())
    episodes[0]=ep
    write(ROOT/'production/episodes.json',episodes)
    adopted=json.loads((ROOT/'production/adopted-assets.json').read_text())
    adopted={key:value for key,value in adopted.items() if not key.startswith('1-')}
    for i,s in enumerate(ep['scenes'],1):adopted[f'1-{i}']=dict(file=s['file'],reason='ゲーム操作、灯刃の効果と熱、回路設計の得意分野を段階的に見せる改稿')
    write(ROOT/'production/adopted-assets.json',adopted)
    design=dict(date='2026-10-07',scope='Current game revision; dialogue, UI and sounds independent',panels={f'{i}-{j}':p['sounds'] for i,s in enumerate(ep['scenes'],1) for j,p in enumerate(s['panels'],1) if p.get('sounds')},quiet='Unlisted panels retain quiet; system actions use only specified brief electronic sounds.')
    write(ROOT/'production/episode-01-sound-design.json',design)
    board=[f"# 第1話 この剣で、一緒に\n\n{ep['narrative_panel_count']}コマ、{len(ep['scenes'])}原画。発話・HUD・効果音は別々に設計。\n"]
    for i,s in enumerate(ep['scenes'],1):
        board.append(f"\n## {i:02d} {s['name']}\n\n場所：{s['location']}\n\n読者の理解：{s['purpose']}\n\n次の間：390px幅で{s['gap']}px。\n")
        for j,p in enumerate(s['panels'],1):board.append(f"\n{j}. {p['art']}\n"+panel_board(p))
    (ROOT/'episode-01/storyboard.md').write_text(''.join(board))
    marker='\n## 2026-10-07 ゲーム操作・剣の働き・得意分野の実行済み改稿\n'
    executed=[]
    for a in manifest:
        executed.append(f"\n### {a['destination']}\n\n参照：episode-01/{a['source']}。方式：{a['mode']}。\n\n```text\n{a['prompt']}\n```\n")
        for f in a.get('followups',[]):executed.append(f"\n### {f['destination']}\n\n参照：episode-01/{f['source']}。方式：native_targeted_edit。\n\n```text\n{f['prompt']}\n```\n")
    for name in ['PROMPTS.md','PROMPTS-USED.md']:
        p=ROOT/'episode-01'/name
        p.write_text(p.read_text().split(marker)[0]+marker+'\n以下は組み込み image_gen で実行した指示。過去の実使用履歴を保持。未実行の次回用指示は PROMPTS-NEXT.md。\n'+''.join(executed))
    review=json.loads((ROOT/'episode-01/validation.json').read_text())
    review.update(game_revision=ep['game_revision'],raster_lettering_visual='pending_model_review',story_quality_approved_by_user=False)
    write(ROOT/'episode-01/validation.json',review)
    print(f"Adopted {len(ep['scenes'])} strips / {ep['narrative_panel_count']} panels. Browser review pending.")

if __name__=='__main__':main()
