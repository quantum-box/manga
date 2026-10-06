#!/usr/bin/env python3
"""Adopt the pacing revision only after every new scene exists."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def write(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    ep=json.loads((ROOT/'production/episode-01-revision.json').read_text())
    d=ROOT/'episode-01'
    ep['scenes'][0]['file']='art/r01-monitor.png'
    ep['scenes'][0]['panels'][0]['art']=ep['scenes'][0]['panels'][0]['art'].replace('三人の小さなアバター','二人の匿名の兜姿のアバター')
    ep['scenes'][3]['file']='art/r04-created.png'
    ep['scenes'][3]['panels'][2]['text']='カイが作った剣、使ってみたよ。'
    ep['scenes'][3]['panels'][2]['columns']=['カイが作った剣、','使ってみたよ。']
    ep['cover_scene']=2
    for scene in ep['scenes']:
        assert (d/scene['file']).is_file(),scene['file']
    records=json.loads((ROOT/'production/revision-provenance.json').read_text())
    by_file={r['file']:r for r in records}
    for scene in ep['scenes']:
        path=d/scene['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==by_file[scene['file']]['sha256']
    episodes=json.loads((ROOT/'production/episodes.json').read_text())
    episodes[0]=ep
    episodes[1]['opening_caption']='翌日のログイン。約束の工房へ。'
    episodes[1]['scenes'][0]['location']='翌日のログイン、工房へ向かう同じ街路。灯りの消えた夜'
    write(ROOT/'production/episodes.json',episodes)
    write(d/'episode.json',ep)
    write(ROOT/'episode-02/episode.json',episodes[1])
    board=(ROOT/'production/episode-01-revised-storyboard.md').read_text().replace('三人の小さなアバター','二人の匿名の兜姿のアバター')
    board=board.replace('カイの剣、使ってみたよ。','カイが作った剣、使ってみたよ。').replace('カイの剣、 / 使ってみたよ。','カイが作った剣、 / 使ってみたよ。')
    (d/'storyboard.md').write_text(board)
    prompts=(d/'PROMPTS-REVISION.md').read_text()
    prompts+='\n## r01-monitor の局所修正\n\n```text\n'+(ROOT/'production/repair-monitor.txt').read_text()+'\n```\n'
    prompts+='\n## r04-created の局所修正\n\n```text\n'+(ROOT/'production/repair-created-sword.txt').read_text()+'\n```\n'
    (d/'PROMPTS.md').write_text(prompts)
    (d/'PROMPTS-USED.md').write_text(prompts)
    adopted=json.loads((ROOT/'production/adopted-assets.json').read_text())
    adopted={k:v for k,v in adopted.items() if not k.startswith('1-')}
    for i,scene in enumerate(ep['scenes'],1):
        adopted[f'1-{i}']=dict(file=scene['file'],reason='読者の指摘に対応した状況・感情の改稿')
    write(ROOT/'production/adopted-assets.json',adopted)
    catalog=ROOT.parents[1]/'content/catalog.json'
    titles=json.loads(catalog.read_text())
    title=next(x for x in titles if x['id']=='tower-forge')
    title['cover']='episode-01/art/r02.png'
    title['synopsis']='VRMMORPG《星環の塔 ONLINE》。自分が作った剣で、仲間と一緒に塔を登りたいカイ。装備の試作と剣と魔法の冒険を描く。240話の仮構成。第1話は状況と感情を補う改稿、第2〜10話は初稿・改稿待ち。'
    for entry in title['episodes']:
        if entry['number']==1:
            entry['title']=ep['title'];entry['edition']='状況と感情を補う改稿'
        else:entry['edition']='初稿・改稿待ち'
    write(catalog,titles)
    review=dict(episode=1,revision=ep['revision'],raster_lettering_visual='pending_model_review',
                story_quality_approved_by_user=False,physical_device_tested=False)
    write(d/'validation.json',review)
    print(f"Adopted chapter 1, {len(ep['scenes'])} raster strips, {ep['narrative_panel_count']} planned narrative panels.")

if __name__=='__main__':main()
