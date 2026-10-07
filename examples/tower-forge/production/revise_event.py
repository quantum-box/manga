#!/usr/bin/env python3
"""Prepare and adopt the tower incident after the earned party promise."""
import argparse
import hashlib
import json
from pathlib import Path
from panel_lettering import make_panel, panel_board, render_panel_lettering

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'production/event-revision'
REVISION = 'tower_incident_2026_10_07'
REFERENCES = ['episode-01/art/r18-scroll.png', 'episode-01/art/r03-status.png']

COMMON = '''Use case: illustration-story. Create ONE new finished Japanese Webtoon raster strip adjoining the supplied comic. Reference 1 gives the same white stone Gothic tower, medieval city, workshop blue cloth, sunset and the characters' costumes/props. Reference 2 gives Kai's face and functional cyan game HUD. These are identity, environment and painting-style references ONLY, not panel-layout templates. Match the refined full-color anime linework and expressive faces. Kai: young man, tousled dark brown hair with one amber streak at his RIGHT temple, amber eyes, ivory rolled-sleeve shirt, brown leather vest, short navy cape, copper LEFT forearm cuff, bare hands, tool pouch; holds ONE ordinary steel straight prototype sword in his RIGHT hand, square brass guard, black grip, one fine amber blade inset, no flames. Sena: silver-blonde LOW ponytail, blue eyes, silver shoulder and arm armor over blue tunic, navy cape, ONE triangular silver/cobalt shield on LEFT arm; ordinary plain sword sheathed. Kai's sword has already been handed back to him. No extra limbs, no duplicate people or weapons. No gloves on Kai. No new named character, enemy, dragon, reward, chosen-one power or game death trap. The incident is an authored multiplayer game world event independent of Kai's repaired sword. Normal logout remains available. Never draw the sword causing the tower event.
Native smartphone vertical-scroll comic: unequal floating inserts, actual borderless long scenery, large meaningful negative space. Do NOT make an equal-height grid or fill every white gap. The giant incident gets one continuous full-width image, not a tiled page of action rectangles. Japanese speech is upright VERTICAL manga gothic, columns RIGHT to LEFT; words in white balloons with tails aimed at the named speaker. Glyph height about 5.6 percent of the strip width, readable at 360px. Speech and sound effects are independent. SFX outside balloons by their source, no tails. Game HUD is HORIZONTAL: short exact lines, thin cyan translucent functional rectangle in the player's viewpoint; no gold ornamental plaque or UI dialogue bubble. No unlisted text, captions, speaker labels, numbers, watermarks or duplicate words. All lettering integrated into the raster image. Faces, hands, blade, clues and text must stay readable and separate.
'''

def sound(text, cause, placement, design):
    return dict(text=text, cause=cause, placement=placement, design=design)

def scene(number, name, location, purpose, panels, ratio, gap, gap_purpose, composition, withheld):
    return dict(id=f'{number:02d}', name=name, location=location, purpose=purpose,
                panels=panels, ratio=ratio, gap=gap, gap_purpose=gap_purpose,
                file=f'art/r{number:02d}-event.png', withheld=withheld,
                scroll_layout=dict(composition=composition, read_order='上から下。手掛かり→知覚→次の情報。'))

def planned_scenes():
    p = make_panel
    return [
        scene(19, '約束の後の前兆', '同じ試験庭。約束の直後、夕空から薄暮へ。塔はまだ画面外。',
              '安心した直後、周囲の異変を二人の感覚から知る。原因の姿は次のスクロールへ残す。', [
                  p('上右寄せの幅65％の浅い接写。同じ青い工房布の隣、橙の魔導灯が一瞬だけちらつく。塔も人もまだ描かない。', sounds=[sound('パチ…','灯りの明滅に伴うゲーム内の小さな放電音','灯具の横','小さく細い灰黒の描き文字')]),
                  p('離れた中央左の幅60％の浅い枠なし接写。カイの目が振動に気づいて少し見開く。遠くの低い音だけが来る。剣と塔は画面外。', sounds=[sound('ゴゴ…','画面外の塔の駆動部から届く低い振動音','目を避けた余白、下へ少し伸ばす','重く低い灰色の描き文字。次の轟音より控えめ')]),
                  p('下端の広い中景。セナが右手で上を指し、隣のカイも顔を上げる。左腕に盾、カイの素手の右手に剣を安全に下ろす。青い布と庭の標的を残し、塔の光環は描かない。', 'セナ', 'カイ、上！', ['カイ、','上！'], '切迫した声')
              ], '1:2', 620, '音と上を見る視線を先に届け、塔の大きな姿をスクロール後へ残す',
              '上の灯具、離れた目の接写、下の二人の視線。間に白い空間を残す。三段の均等な箱へしない。', '光環・閉じる門・停電結果・事件の原因は次の場面へ'),
        scene(20, '塔が空を揺らす', '同じ庭から見上げる塔と薄暮の街。一回の魔力放出。',
              '穏やかな世界を変える巨大な出来事を、塔と街の尺度で体感する。', [
                  p('一つの枠なし連続画面。上の暗青の空をほぼ横幅いっぱいの巨大な橙金色の光環が横切る。既存の白石ゴシック塔の上部から光柱が噴き、輪状の魔導設備が過負荷で輝く。石塔は崩壊せず、光が膨れ街へ走る一瞬。塔の縦軸と光の曲線を下へたどると白石の街並み、最下部に庭のカイとセナの小さな背中が一度だけ現れる。カイ右手の普通の鋼剣は下ろしたまま、セナ左腕に盾。服と青い布だけが衝撃の風で揺れる。顔の会話コマ・別の門・説明UI・怪物・剣から出る光を追加しない。上下端は薄い光から白へ自然に溶かす。', sounds=[sound('ゴオオオ','塔の大規模な魔力放出の轟音','上から中央の空いた空。塔の形と二人を隠さない','大胆な長い墨黒の描き文字、細い白縁。文字を光の曲線に沿わせる')])
              ], '1:3', 100, '大きな異変を受け止めてから街への影響を見る',
              '全長を使う一枚の枠なし風景。空の光環→塔の縦軸→街→小さな二人。枠と文字で分断しない。', '原因・復旧期限・回収部品・敵はまだ説明しない'),
        scene(21, '閉ざされた行き先', '庭から見える東門。その後、同じ工房の扉とカイの視界。薄暮。',
              '明日向かう門が閉じ、剣を作った工房街が停電した。ゲームの区域イベントとして確認する。', [
                  p('上の幅いっぱいの斜め枠。庭から通りの向こうに見えていた塔の東門の鉄格子が激しく落ちる。門の前の少数の冒険者が立ち止まり見上げる。二人は庭で画面外。誰も潰されず、建物も崩れない。塔の巨大な光はもう収まる。', sounds=[sound('ガァン','東門の鉄格子が石の下枠へ止まる','門の接地部を避けた空き','重い角張った描き文字、白の細縁')]),
                  p('中央左寄せの幅65％の静かな接写。前の場面と同じ青い布と真鍮灯。橙の魔導灯が消え、布が暗青になる。遠い主都市の灯りは残る。', sounds=[sound('フッ','魔導灯が消える瞬間のゲーム内の短い音','消えた灯具のそば','小さく柔らかな灰白色、轟音との強弱をつける')]),
                  p('下の大きなカイの肩越し。カイは左カフを少し上げ、自動着信した区域通知を見る。右手の剣は下ろしたまま。窓は本人のHUD。顔と剣を避け広く3行。背景に青い布と暗い工房入口。セナは庭で近くにいるが画面外。', sounds=[sound('ピン','区域イベントの通知が届く電子音','HUD左上の空き','短く小さなシアンの電子音')], ui=[dict(owner='カイ', action='区域のイベント通知を受信して読む。操作で発生させた事件ではない', placement='空いた背景を使う大きな窓。手と剣を隠さない', lines=['街区イベント発生','工房街・灯炉停止','塔東門・一時封鎖'])])
              ], '1:3', 210, '事実を知った後、カイがどう動くかを待つ',
              '上の広い門の衝撃、間を置いた小さな消灯、下の広い本人視点HUD。均等な三箱へしない。', '原因の診断・期限・部品名・解決策は第2話以降へ'),
        scene(22, '工房へ戻る', '同じ庭から青い布の工房入口へ。日没後の暗い街区。',
              'カイは明日の冒険を奪う問題を見過ごさず、自分で確かめに戻る。修理の成功は約束しない。', [
                  p('上右寄せ幅60％、セナの顔の静かな接写。光の収まった暗い空、カイは画面外左。聞く表情で問いかける。', 'セナ', 'どうする？', ['どうする？']),
                  p('広い白い無音の間の後、中央左の小さな接写。カイの目が驚きから考える表情へ変わり、灯りの消えた工房へ視線を動かす。HUDは閉じ、能力の覚醒や謎の数値を描かない。', quiet_reason='驚きを受け止め、自分で行動を選ぶ時間。'),
                  p('下の大きな枠なし中景。カイが一歩踏み出し、庭から同じ青い布の工房へ向き直る。一本の剣を素手の右手で安全に低く持つ。セナが隣で左腕の盾を保ちついて行く。遠い中央都市は灯るが、この扉の魔導灯は消えている。カイの決意は彼のそばの大きな縦の白い吹き出しに置く。工房の中はまだ見せない。', 'カイ', '工房に戻ろう。', ['工房に','戻ろう。'], sounds=[sound('コツ','カイが工房へ最初の一歩を踏み出す','石畳の足元','小さく硬い灰黒の描き文字')])
              ], '1:2', 0, '第2話で同じ夜の工房へつなぐ',
              '小さな問い→白い無音の間→目の判断→大きな枠なしの一歩。決断と場所の接続を最後へ残す。', 'オルンの診断・イリス・依頼と報酬をまだ描かない')
    ]

def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def prepare():
    ep_path = ROOT/'episode-01/episode.json'
    ep = json.loads(ep_path.read_text())
    if ep.get('event_revision'):
        raise SystemExit('Incident already adopted; do not replace its reviewed revision.')
    FOLDER.mkdir(exist_ok=True)
    scenes = planned_scenes()
    for s in scenes:
        prompt = COMMON + f"\nScene {s['id']}: {s['name']}. Portrait ratio {s['ratio']}. Place: {s['location']}. Purpose: {s['purpose']}.\nComposition: {s['scroll_layout']['composition']}\n"
        for i, panel in enumerate(s['panels'], 1):
            prompt += f"\nNarrative moment {i}: {panel['art']}\n" + render_panel_lettering(panel)
        prompt += '\nWithhold: ' + s['withheld'] + '\n'
        s['prompt'] = prompt
        s['prompt_role'] = 'executed_new_incident_scene'
        s['prompt_file'] = f"production/event-revision/r{s['id']}.txt"
        (ROOT/s['prompt_file']).write_text(prompt)
    write(FOLDER/'plan.json', dict(revision=REVISION, source_sha256=hashlib.sha256(ep_path.read_bytes()).hexdigest(), references=REFERENCES, scenes=scenes))
    print('Prepared 4 new strips / 10 narrative moments after the 68 retained moments.')

def adopt():
    plan = json.loads((FOLDER/'plan.json').read_text())
    ep_path = ROOT/'episode-01/episode.json'
    assert hashlib.sha256(ep_path.read_bytes()).hexdigest() == plan['source_sha256']
    ep = json.loads(ep_path.read_text())
    records = {x['file']:x for x in json.loads((ROOT/'production/revision-provenance.json').read_text())}
    for s in plan['scenes']:
        edits = [dict(file=s.get('source_file',s['file']), prompt=s['prompt'],
                      prompt_file=s['prompt_file'], references=REFERENCES), *s.get('followups',[])]
        for edit in edits:
            r = records[edit['file']]
            data = (ROOT/'episode-01'/edit['file']).read_bytes()
            assert data == Path(r['source']).read_bytes()
            assert hashlib.sha256(data).hexdigest() == r['sha256']
            assert r['prompt'] == edit['prompt'] == (ROOT/edit['prompt_file']).read_text()
            assert r['references'] == edit['references']
        s['executed_event_edits'] = [edit['prompt_file'] for edit in edits]
    ep['scenes'][17]['purpose'] = '一緒に登る約束を受け止める。前兆は喜びの余韻の後に始める。'
    ep['scenes'][17]['gap'] = 180
    ep['scenes'][17]['gap_purpose'] = '約束の喜びを受け止めた後に、日常の小さな違和感へ移る'
    ep['scenes'][17]['withheld'] = 'この場面では灯りと喜びを保つ。塔の異変は次の場面から。'
    ep['scenes'].extend(plan['scenes'])
    ep['event_revision'] = REVISION
    ep['narrative_panel_count'] = sum(len(s['panels']) for s in ep['scenes'])
    ep['sound_cue_count'] = sum(len(p.get('sounds',[])) for s in ep['scenes'] for p in s['panels'])
    assert ep['narrative_panel_count'] == 78 and ep['sound_cue_count'] == 25
    eps_path = ROOT/'production/episodes.json'
    eps = json.loads(eps_path.read_text()); eps[0] = ep
    eps[1]['opening_caption'] = '塔の異変から、少し後。同じ夜の工房街。'
    eps[1]['scenes'][0]['location'] = '塔の異変から少し後、同じ夜の工房街。カイとセナが戻る街路'
    route=eps[1]['scenes'][3]
    route_file='art/r04-route.png'
    route_prompt_file='production/event-revision/episode-02-route.txt'
    route_prompt=(ROOT/route_prompt_file).read_text()
    route_records=[x for x in json.loads((ROOT/'production/revision-provenance.json').read_text()) if x['episode']==2 and x['file']==route_file]
    assert len(route_records)==1
    r=route_records[0]
    assert (ROOT/'episode-02'/route_file).read_bytes()==Path(r['source']).read_bytes()
    assert r['prompt']==route_prompt and r['references']==['episode-02/art/04.png']
    route.update(file=route_file, location='翌日のログイン。工房街側の旧水路保守入口、昼',
                 opening_caption='翌日のログイン。工房街側の旧水路保守入口。',
                 prompt=route_prompt, prompt_role='executed_route_and_hand_continuity_edit', executed_event_edits=[route_prompt_file])
    route['panels'][3]['art']='長い枠なし。三人の後ろ姿、工房街側の運河にある旧水路の小さな保守入口へ歩く。保守口は開いている。塔は遠景に見えるが、封鎖された東門は開かない。カイは素手、銅カフは左腕だけ。'
    write(ep_path, ep)
    write(ROOT/'episode-02/episode.json', eps[1]); write(eps_path, eps)
    adopted_path = ROOT/'production/adopted-assets.json'
    adopted = json.loads(adopted_path.read_text())
    for s in plan['scenes']:
        adopted[f"1-{int(s['id'])}"] = dict(file=s['file'], reason='約束の余韻の後、前兆・塔の異変・門と街区への影響・主人公の選択を描く')
    adopted['2-4']=dict(file=route_file,reason='東門の封鎖を維持し、翌日の遠征を街側の旧水路保守口へつなぐ')
    write(adopted_path, adopted)
    design_path = ROOT/'production/episode-01-sound-design.json'
    design = json.loads(design_path.read_text())
    for s in plan['scenes']:
        for j, p in enumerate(s['panels'], 1):
            if p['sounds']: design['panels'][f"{int(s['id'])}-{j}"] = p['sounds']
    design['scope'] = 'Game actions and tower incident; dialogue, UI and sounds independent'
    write(design_path, design)
    board = ['# 第1話 この剣で、一緒に\n\n78の物語上の瞬間、22原画。矩形コマの数ではない。約束の後に塔の異変を描く採用版。\n']
    for i, s in enumerate(ep['scenes'], 1):
        board.append(f"\n## {i:02d} {s['name']}\n\n場所：{s['location']}\n\n読者の理解：{s['purpose']}\n\n次の間：390幅で{s['gap']}px。{s['gap_purpose']}。\n")
        if s.get('scroll_layout'): board.append('\n構図：'+s['scroll_layout']['composition']+'\n読順：'+s['scroll_layout']['read_order']+'\n')
        for j, p in enumerate(s['panels'], 1): board.append(f"\n{j}. {p['art']}\n"+panel_board(p))
    (ROOT/'episode-01/storyboard.md').write_text(''.join(board))
    marker = '\n## 2026-10-07 約束の後の塔の異変・実行済み追加\n'
    used = ['\n組み込み image_gen。既存18原画は保持。新しい4原画へ会話・HUD・効果音を統合。\n']
    for s in plan['scenes']:
        edits=[dict(file=s.get('source_file',s['file']), prompt=s['prompt'], references=REFERENCES), *s.get('followups',[])]
        for edit in edits:
            used.append(f"\n### {edit['file']}\n\n参照：{'、'.join(edit['references'])}。\n\n```text\n{edit['prompt']}\n```\n")
    for name in ['PROMPTS.md','PROMPTS-USED.md']:
        path=ROOT/'episode-01'/name
        path.write_text(path.read_text()+marker+''.join(used))
    route_used=f'\n## 2026-10-07 東門封鎖後の経路・実行済み局所編集\n\n採用：{route_file}。参照：art/04.png。組み込み image_gen。出発は翌日のログイン。開いた東門へ入る絵を街側の旧水路保守口へ修正。本文全体の改稿は未完。\n\n```text\n{route_prompt}\n```\n'
    for name in ['PROMPTS.md','PROMPTS-USED.md']:
        path=ROOT/'episode-02'/name
        path.write_text(path.read_text()+route_used)
    (ROOT/'episode-02/storyboard.md').write_text('# 第2話 灯りの消えた街\n\n塔の異変から少し後、同じ夜の工房街。最終場面は翌日のログイン、街側の旧水路保守入口へ。本文全体は初稿・改稿待ち。\n'+''.join(f"\n## {i:02d} {s['name']}\n\n場所：{s['location']}\n"+''.join(f"\n{j}. {p['art']}\n"+panel_board(p) for j,p in enumerate(s['panels'],1)) for i,s in enumerate(eps[1]['scenes'],1)))
    review_path=ROOT/'episode-01/validation.json'
    review=json.loads(review_path.read_text())
    review.update(revision=REVISION, event_revision=REVISION, raster_lettering_visual='pending_model_review', story_quality_approved_by_user=False)
    write(review_path,review)
    print('Adopted 22 native strips / 78 narrative moments / 25 sound cues; phone review pending.')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('mode', choices=['prepare','adopt'])
    args=parser.parse_args()
    prepare() if args.mode=='prepare' else adopt()
