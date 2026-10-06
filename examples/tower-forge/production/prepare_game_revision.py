#!/usr/bin/env python3
"""Prepare game actions, the named sword and Kai's demonstrated specialty."""
import copy
import json
from pathlib import Path
from panel_lettering import make_panel, normalize_panel, render_panel_lettering, panel_board

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'production/game-revision'

def window(lines,action,placement='コマの空いた背景。顔・手・刃を避ける',owner='カイ'):
    return dict(lines=lines,owner=owner,action=action,placement=placement)

def ping(cause,placement):
    return dict(text='ピッ',cause=cause,placement=placement,design='小さく短いシアンの電子音。吹き出しなし')

def scene(name,location,purpose,panels,gap=70):
    return dict(name=name,location=location,purpose=purpose,panels=panels,gap=gap,ratio='1:3',withheld='未登場の人物・後の事件は描かない')

COMMON='''Use case: illustration-story. Create a NEW adjacent Japanese Webtoon strip, portrait ratio 1:3. The supplied image is a CHARACTER, COSTUME, PROP and PAINTING-STYLE reference, not an edit target or panel-layout template. Match the established polished anime fantasy linework, warm light, white gutters and readable manga expressions. Kai: dark brown tousled hair, amber eyes, white shirt, brown leather vest, short navy shoulder cape, copper LEFT forearm cuff, tool pouch. Sena: silver-blonde low ponytail, blue eyes, silver armor over navy, one triangular silver shield with blue lines. The SAME prototype sword: ordinary steel one-handed straight blade, square brass guard, black leather grip, ONE fine amber engraved line. No legendary sword or flame blade. Only registered game equipment, no hacking or supernatural vision.
Unequal panel heights and focus, clear top-to-bottom reading. Same-row insets read right to left. One principal understanding per panel; do not cram all exchanges into one shot. Japanese dialogue is upright vertical gothic, columns RIGHT to LEFT, large readable glyphs and white balloons with tails pointing to actual speakers. UI is horizontal, thin cyan translucent functional windows in the named player's viewpoint, not floating ornamental plaques visible to everyone. Keep UI wording short and large, with gently diffused luminous edges. Sound effects are outside balloons by their source. Dialogue, UI and sounds are independently specified. No unlisted words, random numbers, labels, captions, signatures or watermarks. No extra hands or weapons. Draw text inside the raster art.
'''

def main():
    current=json.loads((ROOT/'episode-01/episode.json').read_text())
    if current.get('game_revision'):
        raise SystemExit('Game revision already adopted. Preserve the execution manifest.')
    ep=copy.deepcopy(current)
    old=ep['scenes']
    status=scene('得意と、これから','ログインしたリューメルの同じ石段。セナはまだいない。','自分でステータスを開く。回路設計は既に高く、剣の実戦はこれから。',[
        make_panel('上の浅い手元。カイが右の人差し指で左腕の銅カフを二度触れ、本人の視界にメニューを開く。背後は前の石段。剣は持たない。',ui=[window(['ステータス'],'左カフを二度触って開く')],sounds=[ping('メニューを開く電子音','カフ近くの空き')]),
        make_panel('中央の大きなカイの肩越しの視界。三行だけのステータスを読み、石の階段と塔の裾が窓の奥に透ける。窓がコマ幅の約8割、字が主役。',ui=[window(['カイ','剣術 12','魔導回路設計 68'],'技能一覧を確認する','窓を中央へ大きく、3行をゆったり整列')]),
        make_panel('下の大きなカイの顔と左手。窓を閉じ、塔の道へ視線を上げる。得意の設計に加えて、自分でも剣を使いたい。嬉しい期待と少しのためらい。','カイ','剣も、使えるようになりたい。',['剣も、','使えるように','なりたい。'],voice='心の声'),
    ])
    weapon=scene('灯刃の働き','返された一本の剣が工房の木の台にある。カイ左、セナ右。','剣の名前・斬撃強化・消費を、装備詳細の操作と手元で伝える。',[
        make_panel('上の浅いカイの左カフと右指。作業台の一本の試作剣を選び、装備詳細を開く。剣は台の上のまま、二人とも手に持たない。',ui=[window(['装備詳細'],'台の剣を選択して詳細を開く')],sounds=[ping('装備詳細を開く電子音','カフ近くの空き')]),
        make_panel('中央の大きなカイ本人の視界。台に置いた鋼剣を下に残し、余白に三行だけの装備詳細。文字を大きく、普通の鋼と真鍮の剣だと同時に分かる。',ui=[window(['灯刃・試作','斬撃強化 ＋30％','消費MP 2／打'],'効果と消費を見る','横書き3行の窓をコマの上側へ大きく。一本の剣は下に見える')]),
        make_panel('その下のカイと剣の中景。窓は閉じ、刃の橙の細い刻線を指で示す。顔・指・一本の刃を見やすく。熱、火、爆発の絵は出さない。','カイ','魔石の力で、刃の切れ味を上げる。',['魔石の力で、','刃の切れ味を','上げる。']),
        make_panel('下のカイの手と落ち着いた顔。刻線から鍔へ指を戻し、魔力の流すタイミングを自分で設計したことを短く伝える。セナは右の画面外で聞いている。','カイ','振る時だけ、刃に魔力を回す。',['振る時だけ、','刃に魔力を','回す。']),
    ])
    log=scene('数字と、消えた光','失敗を見た同じ試験庭。セナが剣を保持、カイの手は空く。','魔力の残量と出力停止を区別し、回路を調べる理由を持つ。',[
        make_panel('上の浅い手元。カイが右指で左の銅カフを触り、今の剣の試験ログを開く。セナの剣先は安全に下を向き、刃の光は消えている。',ui=[window(['試験ログ'],'直前の試験結果を開く')],sounds=[ping('試験ログを開く電子音','カフと指の近くの空き')]),
        make_panel('中央はカイの肩越しの大きな視界。残量と出力の二つを、3行の窓として読む。背景のセナは本人のログを読まない。窓は読者が理解できる大きさ。',ui=[window(['灯刃・試作','魔石MP 62／100','魔導出力 停止'],'残量があることと出力停止を見比べる','大きな窓。残量はシアン、停止の語だけ淡い橙')]),
        make_panel('下はカイの目と口を大きく。窓を閉じ、無傷の鋼の刃と光の消えた刻線へ目を動かす。原因を断言せず、確認する場所を絞る。','カイ','魔力切れじゃない。強化だけが止まってる。',['魔力切れ','じゃない。','強化だけが','止まってる。']),
    ])
    party=scene('参加を選ぶ','夕方の同じ試験庭。カイは右手に試作剣、セナは左腕に盾。','誘いに実際のゲーム操作で応じ、一緒に遊ぶ相手になる。',[
        make_panel('上はセナの右指と左腕の手元。左腕の盾はそのまま、右指で自分の短いHUDの送信を押す。彼女本人の視点。剣はカイの手にある。',ui=[window(['カイを招待','送信'],'パーティ招待を送信する',owner='セナ')],sounds=[ping('招待を送信する電子音','セナの指の近く')]),
        make_panel('中央はカイの肩越しの視界。セナから招待が届き、参加ボタンにまだ触れていない。右手の剣は下を向け、左手を窓へ近づける。',ui=[window(['セナから招待','参加'],'届いた招待を読む','顔を避け、窓を大きく、参加ボタンに十分な余白')]),
        make_panel('下の大きな中景。カイが左の人差し指で参加ボタンを押す。窓が参加完了の2行へ変わる。剣は右手で安全に下ろし、隣のセナへ小さく笑う。まだ塔へ歩き出さない。',ui=[window(['パーティに参加','カイ・セナ'],'参加を押して完了を確認する')],sounds=[ping('参加を確定する電子音','カイの左指のそば')]),
    ],gap=110)
    # Keep the original response panels and continuity, editing only identified deficiencies.
    old[4]['panels'][0].update(text='同じ威力で、魔力は半分。',columns=['同じ威力で、','魔力は半分。'])
    old[4]['panels'][0]['art']+='標準市販型は同じ30％強化にMP4、灯刃はMP2という実際の差に驚く。'
    old[8]['panels'][1].update(text='刃を強化すると、回路に熱が残る。',columns=['刃を強化すると、','回路に熱が','残る。'])
    old[8]['panels'][2].update(text='熱が溜まると、安全装置が強化を止める。',columns=['熱が溜まると、','安全装置が','強化を止める。'])
    old[11]['panels'][2]['ui']=[window(['斬撃強化 作動'],'同条件の三打目でも強化が出たことを確認する','鍔接写の空いた背景へ短い1行。溝・刃・手を隠さない')]
    inserts={1:status,3:weapon,6:log,12:party}
    new=[]
    for i,s in enumerate(old):
        new.append(s)
        if i in inserts:new.append(inserts[i])
    ep['scenes']=new
    for i,s in enumerate(new,1):
        s['id']=f'{i:02d}'
        s['panels']=[normalize_panel(p) for p in s['panels']]
    ep.update(game_revision='game_actions_and_sword_identity_2026_10_07',narrative_panel_count=sum(len(s['panels']) for s in new))
    FOLDER.mkdir(exist_ok=True)
    targets=[(3,'status','art/r02.png'),(6,'weapon','art/r04-sounds.png'),(10,'log','art/r07.png'),(17,'party','art/r13.png'),(7,'identity','art/r05.png'),(12,'heat','art/r09-sounds.png'),(15,'test','art/r12-sounds.png')]
    manifest=[]
    for i,tag,source in targets:
        s=new[i-1]
        destination=f'art/r{i:02d}-{tag}.png'
        s['file']=destination
        if tag in ['status','weapon','log','party']:
            prompt=COMMON+f"\nScene {s['name']}. Place: {s['location']}. Purpose: {s['purpose']}. Exactly {len(s['panels'])} panels.\n"
            for j,p in enumerate(s['panels'],1):prompt+=f"\nPanel {j}, top to bottom: {p['art']}\n"+render_panel_lettering(p)
        else:
            prompt='Use case: text-localization. Edit ONLY the specified lettering/interface in the supplied CURRENT Japanese Webtoon strip. Preserve the exact 1:3 canvas, every panel/frame/gutter, faces, expressions, anatomy, costumes, poses, hands, the SAME single sword, all backgrounds, colors and lighting. Preserve every unmentioned word and every sound effect. Do not recompose or add action. Japanese dialogue is upright vertical manga lettering, columns RIGHT to LEFT. New HUD is horizontal in the named player perspective, thin cyan translucent functional panel, no ornament, no balloon or tail. Keep letters readable at 360px and avoid faces, hands and the vent.\n'
            if tag=='identity':
                prompt+='In the TOP Sena speech balloon ONLY replace すごく振りやすい。 with EXACT 同じ威力で、魔力は半分。 Columns RIGHT to LEFT: 同じ威力で、 / 魔力は半分。 Keep the original balloon/tail, enlarging only its local blank area if needed. Preserve でも、三回目が出ない。 and all silent reactions. No HUD in this strip.\n'
            elif tag=='heat':
                prompt+='Replace ONLY Kai\'s explanation balloon next to his face: 光を出すと、ここが熱くなる。 becomes EXACT 刃を強化すると、回路に熱が残る。 Columns RIGHT to LEFT: 刃を強化すると、 / 回路に熱が / 残る。 The vent explanation balloon 逃げないと、止まる。 becomes EXACT 熱が溜まると、安全装置が強化を止める。 Columns: 熱が溜まると、 / 安全装置が / 強化を止める。 Preserve Sena\'s 熱？, Kai\'s もう一回、試そう。, scraping カリカリ and final closing カチッ. No new flame, smoke or heat effect.\n'
            else:
                prompt+='Add ONLY one small-but-readable horizontal cyan HUD line EXACT 斬撃強化 作動 into the empty background of the THIRD brass-guard/vent closeup panel. It is Kai\'s view of the successful third-strike output, NOT heat doing damage. Keep the vent opening visible, the amber blade line on, all existing ギュッ and コン, Sena\'s 出た。, Kai\'s ……よかった。, and both relief faces. No UI or sounds in the last two reaction panels.\n'
        prompt_file=FOLDER/f'r{i:02d}-{tag}.txt'
        prompt_file.write_text(prompt)
        manifest.append(dict(scene=i,tag=tag,source=source,destination=destination,prompt_file=str(prompt_file.relative_to(ROOT)),prompt=prompt,mode='new_adjacent_strip' if tag in ['status','weapon','log','party'] else 'native_targeted_edit'))
    # Unchanged files retain their source and all historical actual-used instructions.
    for s in new:
        if 'file' not in s:raise AssertionError(s['name'])
    (FOLDER/'episode.json').write_text(json.dumps(ep,ensure_ascii=False,indent=2)+'\n')
    (FOLDER/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    board=['# 第1話 ゲーム操作・剣の働き・カイの得意分野の改稿案\n',f"{ep['narrative_panel_count']}コマ、{len(new)}画像。採用前の制作案。\n"]
    for i,s in enumerate(new,1):
        board.append(f"\n## {i:02d} {s['name']}\n\n場所：{s['location']}\n\n読者の理解：{s['purpose']}\n")
        for j,p in enumerate(s['panels'],1):board.append(f"\n{j}. {p['art']}\n"+panel_board(p))
    (FOLDER/'storyboard.md').write_text(''.join(board))
    print(f'Prepared {len(manifest)} native assets, {len(new)} strips / {ep["narrative_panel_count"]} panels. Current reader unchanged.')

if __name__=='__main__':main()
