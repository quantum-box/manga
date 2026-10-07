#!/usr/bin/env python3
"""Prepare the pacing revision without replacing a reader until its art exists."""
import json
from pathlib import Path
from panel_lettering import make_panel, normalize_panel, render_panel_lettering, panel_board

ROOT = Path(__file__).resolve().parents[1]

def p(art, speaker='', text='', columns=None, voice='普通の声'):
    return make_panel(art,speaker,text,columns,voice)

def s(name, location, purpose, panels, gap=70, ratio='1:3'):
    return dict(name=name, location=location, purpose=purpose, panels=panels, gap=gap, ratio=ratio,
                withheld='停電・新しい事件・イリス・敵・報酬をまだ描かない。')

scenes = [
 s('冒険の外側', '現実の海斗の部屋、夜。机にPCとVR端末。', '役に立てる嬉しさと、自分も冒険へ行きたい気持ちを同時に見せる。', [
  p('上の中景。黒髪の海斗が机で友人から届いたゲーム内の記念画像を見る。PCの中だけに剣を掲げて喜ぶ三人の小さなアバター。海斗は画像にいない。机に修理工具と黒いVRヘッドセット。Tシャツ姿。', 'メッセージ', '剣、ありがとう！', ['剣、ありがとう！'], '画面の横書き'),
  p('中央の浅い接写。海斗の目と少し緩んだ口。友人が喜んでくれたことは嬉しい。背景はぼかした同じPC。無言。'),
  p('下の大きな余韻。海斗が椅子を引き、机のVR端末へ手を伸ばす。もう片方の手はまだ机。二本のコントローラーは机の上に静かに置かれ、余分な腕を描かない。喜びから少しだけ寂しさへ。', '海斗', '俺も、行きたかったな。', ['俺も、', '行きたかったな。'], '小さな独り言')
 ], 110),
 s('塔のある世界', '同じ部屋からVRログイン。リューメルの広場。', '遊んでいるVRゲームだと分かった上で、主人公が憧れる世界を味わう。', [
  p('上の浅いコマ。海斗が頭にVRヘッドセットを装着。両手に一つずつ黒いVRコントローラー、ストラップ付き。現実の部屋には動ける空間。', '海斗', '今度は、俺も。', ['今度は、', '俺も。'], '小さな独り言'),
  p('中央は画像の六割を使う長い枠なし風景。白石の中世都市、運河、雲へ伸びる巨大な石塔。カイの背中を手前に一度だけ描く。巨大な塔の階段と道が下へ視線を運ぶ。細かい群衆は遠景だけ。説明台詞なし。'),
  p('下に幅を絞った手元。カイの左手をかざすと小さな半透明青のHUD。服は茶色の革ベストと白シャツ、藍マント。', 'HUD', 'ログイン完了', ['ログイン完了'], '画面の横書き')
 ], 100),
 s('向かう先', '広場から工房への一つの通り。晴れたゲーム内の午後。', '塔に惹かれつつ、試用を頼んだ自分の剣が気になり工房へ戻る。歩く経路を描く。', [
  p('上の広い状況コマ。塔へ向かう冒険者たちが遠景の左奥へ歩く。カイは手前の右で立ち止まり、そちらを目で追う。彼がまだ一緒に行けていないと分かる。'),
  p('右寄せの浅い目元。期待とためらい。前の通りの白いアーチを背景の隅に残す。無言。'),
  p('左寄せの中コマ。カイが腰の工具袋に触れて、前日に試用を頼んだ剣を気にする。カイの腰には剣を描かない。', 'カイ', '昨日の剣、どうだったかな。', ['昨日の剣、', 'どうだったかな。'], '心の声'),
  p('下の大きな中景。塔へ行く道から横道へ曲がり、青い布のかかった木の扉に入るカイ。通りから同じ工房の入り口までが見える。看板は文字のないハンマーの印だけ。')
 ], 70),
 s('帰ってきた剣', '青い布の扉がある工房。木の作業台を挟み、カイは左、セナは右。', '修理を任される関係と、主人公自身の試作品であることを示す。', [
  p('上の全幅状況コマ。セナが青い布の扉から入る。左のカイが木の作業台から振り向く。セナの左腕に三角盾、右手に一振りの試作剣。彼女の普通の剣は腰の鞘。', 'セナ', 'カイ、今いい？', ['カイ、', '今いい？']),
  p('右寄せのカイの顔。相手を知っていて、戻ってきたことを喜ぶ。', 'カイ', 'セナさん。おかえり。', ['セナさん。', 'おかえり。']),
  p('左寄せの手元。セナが試作剣を作業台へ置く。四角い真鍮の鍔、革巻きの柄、刃に一本だけ細い橙の刻線。まだ光らない。', 'セナ', 'カイの剣、使ってみたよ。', ['カイの剣、', '使ってみたよ。']),
  p('下の大きなカイの表情。工具を持つ手を止め、嬉しさと評価への不安を少し見せて相手を見る。', 'カイ', '……どうだった？', ['……どうだった？'])
 ], 90),
 s('嬉しい言葉、その続き', '同じ作業台。青い布の扉と、一本だけの試作剣。', '褒められる嬉しさを受け止めてから、不具合を知る。', [
  p('右寄せの中コマ。セナの率直な笑顔、剣に置いた手。カイは画面外左にいる。', 'セナ', 'すごく振りやすい。', ['すごく', '振りやすい。']),
  p('左寄せの小さな浅いカイの顔。ほっとして、本人も抑えきれない小さな笑み。無言。'),
  p('全幅の中コマ。セナの笑みが少し困った表情へ変わり、光らない剣の刃を二人で見る。', 'セナ', 'でも、三回目が出ない。', ['でも、', '三回目が', '出ない。']),
  p('下の大きなカイの聞き手の反応。笑みが消え、剣へ目を落とす。工具袋の手が止まる。解決方法をまだ知らない。無言。')
 ], 100),
 s('三回目の前で', '工房の裏口から隣接する石の試験庭。木の標的一つ。', '何が止まるのか、修理前の挙動を読者にも見せる。', [
  p('上の広い移動コマ。セナが試作剣を手に、カイと青い布の裏口から庭へ出る。木の丸太標的が左奥。盾は壁際のベンチへ置いた状態。', 'セナ', 'ここなら、安全に試せる。', ['ここなら、', '安全に', '試せる。']),
  p('中央右の動作コマ。セナが丸太へ第一打。刃の橙の細い刻線だけが灯る。腕も剣も一本ずつ。魔法の大爆発はなし。', 'セナ', '一回目。', ['一回目。']),
  p('その下、左寄せの浅い第二打。丸太と刃の接写。橙の線はまだ光る。', 'セナ', '二回目。', ['二回目。']),
  p('下の大コマ。セナが第三打へ持ち上げた刃の光が消えている。刃は折れていない。右手を止めてカイへ剣を見せる。', 'セナ', '……ここで止まる。', ['……ここで', '止まる。'])
 ], 120),
 s('失敗を見たあと', '同じ試験庭の壁際。セナ右、カイ左。', '自分の製作品の失敗を気にするカイと、責めずに一緒に確かめるセナ。', [
  p('右寄せのカイの中景。伏せた目、下がった肩。セナに向かって正直に言う。', 'カイ', 'ごめん。', ['ごめん。'], '小さな声'),
  p('左寄せのセナの中景。試作剣を横に持ち、鋼の刃が無事であるところをカイに見せる。', 'セナ', '折れてないよ。', ['折れてないよ。']),
  p('下へ大きく続くカイの顔と空いている手。自分の失敗より使った相手への心配が出る。', 'カイ', 'でも、戦ってる時なら……。', ['でも、', '戦ってる', '時なら……。']),
  p('下の全幅、二人の中景。セナが困った剣を大事に扱い、工房の青い布の扉へ目線を向ける。', 'セナ', 'じゃあ、ここで確かめよう。', ['じゃあ、', 'ここで', '確かめよう。'])
 ], 80),
 s('どこで止まるのか', '庭から工房へ戻る。同じ台、試作剣はカイの前。', '決めつけず開けて確認する。熱と刃を区別する。', [
  p('上の全幅。カイが一本の試作剣を台に置き、セナへ小さな工具を示す。青い布の扉が背景。', 'カイ', '少し、開けてもいい？', ['少し、', '開けても', 'いい？']),
  p('右寄せのセナの浅い顔。素直にうなずき、待つ。', 'セナ', 'うん。', ['うん。']),
  p('左寄せの接写。カイが鍔のすぐ上の小さな真鍮の蓋をドライバーで外す。薄い刃は変形していない。', 'カイ', '刃じゃない……。', ['刃じゃ', 'ない……。'], '小さな声'),
  p('下の大きな部品の接写。蓋の下の一つの排熱溝に黒い付着物。工具の先がそこを示す。カイは画面外左、セナ右。', 'カイ', '熱の逃げ道が、詰まってる。', ['熱の逃げ道が、', '詰まってる。'])
 ], 80),
 s('直す理由', '同じ台と同じ一振り。台に置いた蓋と工具。', '仕組みを質問、対象、作業の順で一つずつ理解する。', [
  p('上の右寄せ小コマ。セナの眉が少し上がる。', 'セナ', '熱？', ['熱？']),
  p('左寄せの中景。カイが一本の剣の細い刻線から鍔の溝へ指を動かす。二人の全景や分解図は不要。', 'カイ', '光を出すと、ここが熱くなる。', ['光を出すと、', 'ここが', '熱くなる。']),
  p('下の浅い部品接写。黒く詰まった一つの溝を大きく見せる。', 'カイ', '逃げないと、止まる。', ['逃げないと、', '止まる。']),
  p('短い斜め枠の工具接写。細い工具で付着物を少しずつかき出す。説明台詞なし、工具と部品だけ。', '音', 'カチ', ['カチ'], '効果音'),
  p('下の大きな落ち着いた中景。蓋を元の同じ場所へ固定し、カイが顔を上げる。セナはまだ台の右で待つ。', 'カイ', 'もう一回、試そう。', ['もう一回、', '試そう。'])
 ], 100),
 s('持つ人が変わる', '同じ裏口から同じ試験庭。標的一つ、盾は同じベンチ。', '作るのは得意でも戦うのは慣れていない。仲間の助言を受けて試す。', [
  p('上の全幅。庭でセナが試作剣の柄をカイの右手へ渡す。受け取った後はカイだけが剣を持つ。', 'セナ', '今度は、カイが振って。', ['今度は、', 'カイが', '振って。']),
  p('右寄せの中コマ。カイがぎこちなく握り、少し照れて横のセナを見る。', 'カイ', '俺、うまくないけど。', ['俺、', 'うまく', 'ないけど。']),
  p('左寄せのセナの中コマ。まっすぐ急かさず見守る。', 'セナ', 'ゆっくりでいいよ。', ['ゆっくりで', 'いいよ。']),
  p('下の大きなカイの膝と肩、手。息を整え、右足を少し後ろへ置く。無言。前に一本の丸太。巨大な技や魔法は出さない。')
 ], 100),
 s('二回、そして', '同じ試験庭。カイが標的の右、セナは後ろで見守る。', '前と同じ条件で確かめ、三回目を待つ。', [
  p('上の中コマ。カイの第一打が丸太へ当たる。剣は細い橙の刻線だけ光る。', '音', 'コン', ['コン'], '効果音'),
  p('左寄せの浅い接写。第二打が同じ丸太へ当たる。小さな木片、光る刃。', '音', 'コン', ['コン'], '効果音'),
  p('右寄せの大きな手元。カイが振るのを一度止め、鍔の小さな溝から淡い橙の粒が抜けるのを見る。刃にはまだ細い光。熱の排出が修理後に働く。無言。'),
  p('下の大きなカイの目と口。まだ結果を断言せず、次の一撃に集中してためらう。無言。三打目やセナの答えを先に出さない。')
 ], 190),
 s('あと一撃が出た', '同じ標的への三打目。', '修理した仕組みが自分の行動で働き、成功を受け止める。', [
  p('上の浅い握る手。第三打へ、カイが右手の握りを確かめる。剣一本。無言。'),
  p('中央の大きな斜め枠。カイの第三打が同じ木の標的へ当たる。刃の細い橙の光は消えず、大爆発も標的の消滅もない。', '音', 'コン', ['コン'], '効果音'),
  p('小さな鍔の接写。溝から淡い光が抜け、刃の光が保たれる。部品は壊れていない。無言。'),
  p('右寄せのセナの顔。自分も結果を待っていたことが分かる安堵の笑み。', 'セナ', '出た。', ['出た。'], '柔らかな声'),
  p('下の大きなカイ。肩の力が抜けて、少しだけ笑う。剣を安全に下ろす。', 'カイ', '……よかった。', ['……よかった。'], '小さな声')
 ], 150),
 s('誘いの意味', '同じ試験庭、夕方へ。カイの手に一本の試作剣。', '修理係としてではなく、一緒に戦う人として誘われる。', [
  p('上の全幅。セナがベンチの盾を左腕へ戻し、剣を持つカイへ向き直る。', 'セナ', '明日、塔に行かない？', ['明日、', '塔に', '行かない？']),
  p('右寄せのカイの顔。思わず工具袋へ目線が向く。嬉しいが意味を確認したい。', 'カイ', '修理係で？', ['修理係で？']),
  p('左寄せのセナの中景。普通に当然のこととして、塔の方向を指す。', 'セナ', '一緒に、戦いに。', ['一緒に、', '戦いに。']),
  p('下に大きなカイの顔。相手の言葉を受け止める無言の時間。目が少し大きくなり、握った肩の緊張がほどける。新しい台詞や停電を追加しない。'),
  p('下端のカイの手と顔。初めて自分の剣を冒険に使える嬉しさを、はっきり相手へ確かめる。', 'カイ', 'この剣で、行っていい？', ['この剣で、', '行っていい？'])
 ], 170),
 s('一緒に登る約束', '試験庭、工房と塔が同じ方向に見える。夕方の暖かな光。', '約束を受け止めて終わる。別の事件で喜びを中断しない。', [
  p('上の右寄せ中コマ。セナがカイの目を見て、小さくうなずく。', 'セナ', 'うん。待ってる。', ['うん。', '待ってる。'], '柔らかな声'),
  p('下は大きな枠なし風景。庭の二人の背中、青い布の工房の扉、その向こうの白石の塔。カイの右手に修理した一本の鋼剣、セナの左腕に盾。街灯は灯ったまま。カイが初めて塔を見るときとは違い、セナと同じ方向を向いている。', 'カイ', '……うん。行く。', ['……うん。', '行く。'], '小さな声')
 ], 0, '1:2'),
]

COMMON = '''Use case: illustration-story. A finished Japanese full-color smartphone vertical-scroll Webtoon strip, including final artwork, speech balloons and exact Japanese lettering. Generate ONE portrait raster image, normally width:height 1:3. The reference sheet is ONLY for character identity, clothing, colors and anime linework. Do not copy its layout, parchment, labels or facial expression. Kai: dark brown hair with one amber streak at his right temple, amber eyes, ivory rolled-sleeve shirt, brown leather vest, short indigo cape, copper cuff left forearm, dark trousers, tool pouch; NO sword on his waist in this episode. Sena: silver-blonde low ponytail, blue eyes, silver shoulder/arm armor, blue tunic and navy cape, triangular silver shield with cobalt lines; her normal plain sword is sheathed. The ONE prototype being tested is steel, square brass guard, dark leather grip, ONE very thin orange inset line along the center of the blade, small brass vent beside the guard. It is Kai's creation, loaned to Sena for a test, NOT a lightsaber. Real-world Kaito: same young male face but natural black hair, no amber streak, charcoal T-shirt; black VR headset and TWO small motion controllers, no gamepad. Iris is not in this chapter. Modern equipment appears ONLY in the real room, medieval scenery ONLY inside the VR game.

Storytelling: calm, clear emotional progression, one principal understanding per panel. Stay in the stated place, preserve the same blue cloth on the workshop door, the workbench, the single wooden practice dummy in the adjacent stone yard. Establish people and position once, then close-ups of speaker, listener or object instead of packing everyone and an elaborate city into each small panel. Keep speaking to nearby offscreen people spatially clear. Do not invent additional plot events, extra dialogue, extra arms, duplicate characters or multiple copies of the sword. The sword NEVER breaks in this chapter.

Panel design: use the SPECIFIC unequal panel widths, heights, staggered placement, borderless landscape and occasional diagonal action frames described below. These panels are successive moments, not simultaneous duplicate people. Clear top-to-bottom flow, same-row inserts read right to left. White gutters, substantial calm breathing room between dialogue/response panels; not a uniform four-box grid and not four cramped panels inside a phone screen. Every tiny panel focuses on a hand, face or component rather than a tiny whole scene. Detailed background ONLY for orientation and the giant tower reveal. Simple backgrounds for emotion. Keep words, faces, fingers and the vent large and separate.

Lettering: true Japanese vertical speech, upright black printed manga glyphs, columns RIGHT to LEFT, each column top-to-bottom. Use LARGE glyphs roughly 5.6 percent of image width (about 20px high when shown at 360px wide). Never shrink text to fit. Exact utterance and column order follow; slash marks in instructions are separators and must not be printed. Spoken words have clean white oval/rounded vertical balloons with tails aimed at the actual speaker. Small quiet speech has softly irregular thin outlines. Internal thought uses thought dots and a softer cloud border. Screen/HUD messages may be horizontal, cyan translucent in the game; real PC message is small ordinary horizontal text. Dialogue and sound effects are independent. No dialogue means no speech/thought balloons; render any separately specified sounds. Place sound lettering near its source, outside balloons, with no tails. Do not apply dialogue column rules to sounds. Only panels explicitly specifying no sounds are quiet. No speaker labels, panel numbers, decorative captions, watermark or extra text. Reserve light blank areas for balloons and generous inset padding. All text is integrated into the raster art.
'''

def main():
    global scenes
    current=ROOT/'episode-01/episode.json'
    if current.exists():
        scenes=json.loads(current.read_text())['scenes']
    scenes=[dict(x,panels=[normalize_panel(p) for p in x['panels']]) for x in scenes]
    design_path=ROOT/'production/episode-01-sound-design.json'
    if design_path.exists():
        design=json.loads(design_path.read_text())
        for key,cues in design['panels'].items():
            i,j=map(int,key.split('-'))
            scenes[i-1]['panels'][j-1]['sounds']=cues
    ep=dict(number=1, title='この剣で、一緒に', revision='reader_context_2026_10_07',
            narrative_panel_count=sum(len(x['panels']) for x in scenes), scenes=scenes)
    prompts=['# 第1話 次回生成用の指示（未実行）\n\n参照は人物・衣装・絵柄のみ。初稿の密度とコマ割りは引き継がない。\n']
    board=['# 第1話 この剣で、一緒に\n',
           'ユーザーの指摘：密度が高い、1話が短い、展開が速く流れと共感が成立しない。\n',
           '修正の目的は長さそのものではなく、知覚→理解→選択→行動→結果→反応を読者が辿れること。停電は第2話へ送る。\n']
    for i,scene in enumerate(scenes,1):
        scene['id']=f'{i:02d}'; scene['file']=scene.get('file',f'art/r{i:02d}.png')
        kind='narrative moments (not mandatory full-width panels)' if scene.get('scroll_layout') else 'narrative panels'
        prompt=COMMON+f"\nChapter 1 revised, strip {i}. Image ratio {scene['ratio']}. Scene: {scene['name']}. Place and continuity: {scene['location']}. Purpose: {scene['purpose']}. Exactly {len(scene['panels'])} {kind}, with unequal sizes as described.\n"
        if scene.get('scroll_layout'):
            layout=scene['scroll_layout']
            prompt+=f"\nScroll composition takes precedence over the reference or default panel grid: {layout['composition']} Reading order: {layout['read_order']} Preserve borderless continuous scenery, same-row pairs and quiet white space; never turn every narrative moment into a full-width rectangle.\n"
        gap_purpose=scene.get('gap_purpose','感情の返答待ち、または場面移動の息継ぎ')
        board += [f"\n## {i:02d} {scene['name']}\n",f"場所・接続：{scene['location']}\n",f"この区間で理解すること：{scene['purpose']}\n",f"次の間：390px幅で{scene['gap']}px。{gap_purpose}。\n"]
        if scene.get('scroll_layout'):board.append('構図：'+scene['scroll_layout']['composition']+'\n')
        for j,panel in enumerate(scene['panels'],1):
            prompt+=f"\nPanel {j}, top to bottom. Artwork, camera, size and main focus: {panel['art']}\n"
            prompt+=render_panel_lettering(panel)
            board += [f"\n{j}. {panel['art']}\n",panel_board(panel),'   - 接続：同じ場所・視線と手・道具の状態を継承。画面外の相手は退場していない。文字は顔・手・排熱溝を避けた余白へ置く。\n']
        scene['prompt']=prompt
        scene['prompt_role']='prepared_next_generation_not_executed'
        prompts += [f'\n## r{i:02d}\n\n```text\n{prompt}\n```\n']
    (ROOT/'production/episode-01-next-generation.json').write_text(json.dumps(ep,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'episode-01/PROMPTS-NEXT.md').write_text(''.join(prompts))
    (ROOT/'production/episode-01-next-storyboard.md').write_text(''.join(board))
    print(f"Prepared next-generation instructions for {len(scenes)} strips, {ep['narrative_panel_count']} panels. Actual used prompts and reader unchanged.")

if __name__=='__main__': main()
