#!/usr/bin/env python3
"""Prepare native recomposition without changing the adopted reader."""
import copy
import hashlib
import json
from pathlib import Path
from panel_lettering import render_panel_lettering, panel_board

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'production/scroll-revision'
PLANS={
 2:dict(ratio='1:3',composition='上に幅65％の小さな現実の挿入。白へフェードした後、雲から塔の縦軸、都市、階段、手前のカイへ視点を下げる一つの長い枠なし風景。下端の左手とログイン表示は小さな独立した挿入。三つの全幅矩形にしない。',arts=[
 '上端右寄せ、幅65％・高さ15％の小さな挿入。黒髪の海斗が現実の室内で黒いVRヘッドセットを着け、両手に一つずつストラップ付きのコントローラー。普通の無地の室内。今度は俺も、という気持ち。下端を白へ溶かす。',
 '中段から下へ画像の約70％を使う一つの枠なし風景。まず雲を横切る細長い白石の塔、次にその裾の都市と運河、最後に同じ塔へ向かう階段と手前のカイの背中へ視点が下りる。塔の縦軸と道がスクロールを導く。カイは一人一度だけ。景色の外周は白い紙へ柔らかく消す。',
 '最下端左寄せ、幅65％の浅い手元の挿入。カイの左カフと素手、本人の視界にログイン完了。背景は同じ石段。中央風景と横線で分断せず、間を白に残す。']),
 4:dict(ratio='1:3',composition='上の小さな状況、右の目元と左の工具袋の近い二つの挿入、その後に余白を挟んだ長い枠なしの横道。石畳のS字の道を上から下へたどると青い布の工房の扉に着く。',arts=[
 '上端の幅80％の浅い状況。塔へ向かう数人の冒険者が奥左へ去る。カイは手前右で立ち止まり追う。背景は白石の通り。足音は遠ざかる靴のそば。大きな全身を繰り返さない。',
 '次の段の右、幅35％の短い目元だけの挿入。期待とためらい。アーチの白石を隅へ残す。無言。',
 '同じ段の左、幅55％、右の目元より少し下げた工具袋に触れる素手の接写。カイの顔を全身で繰り返さず、昨日の試作剣を思う。思考の点は接写の上にいる画面外の頭へ続く。腰に剣はない。',
 '短い白い間の後、下の半分は一つの長い枠なしの背景。白いアーチの下の道から石畳をS字でたどり、下端の青い布の木の扉へ着く。カイの後ろ姿が一人だけ敷居へ踏み込む。ハンマーの印のみ。足音は下の靴のそば。上下の背景が一つの経路としてつながる。']),
 6:dict(ratio='1:2.5',composition='窓を開く小さな手元→白い間→一本の剣と大きなHUDを一つの枠なし作業台の画面に置く。二つの説明は下の右→左の近い顔・指の挿入へ分ける。四つの全幅コマにしない。',arts=[
 '上端右寄せの小さな手元。カイの右指が左の銅カフを触れ、台の剣の詳細を開く。装備詳細の短い見出しとピッ。カイは素手。剣は台にあり、まだ誰も持たない。',
 '白い間を挟んだ中央の大きな枠なし画面。木の台に一本だけの鋼剣と四角い真鍮の鍔、細い橙の刻線。本人の視界の大きな三行のHUDが余白へ浮く。背景は薄く抑え、細部を全面へ詰めない。HUDと剣は同時に読める。',
 '下の段の右側、幅48％のカイの落ち着いた顔と刻線を示す指の近い挿入。魔石で切れ味を上げる説明。背景はほぼ白。全文の縦書き3列に十分な幅を残す。',
 '同じ段の左側、幅48％、少し下げた鍔へ戻る指とカイの口元の挿入。振る時だけ魔力を回す説明。前のコマと同じ一本の剣を別の時刻で見る。背景はほぼ白、セナは右の画面外で聞く。']),
 8:dict(ratio='1:3',composition='上に浅い場所の確認。中段の第一打と第二打は同じ段の右→左へ短く連なる接写。下へ200px相当の白い無音の間を置き、光が消えた刃とセナの顔が大きな枠なし画面として初めて現れる。',arts=[
 '上端の浅い状況コマ。同じ青い布の裏口からセナとカイが庭へ出る。左に一本の木の標的、盾は壁のベンチに置く。セナの右手に試作剣。ここなら安全、の発話。',
 '次の一段の右側、幅48％。第一打の銀の籠手と剣と木の接触だけに寄る。顔や背景全景を縮小しない。橙の一本の線は光る。縦書き一回目と、接触点近くのコン。枠の下辺と次の枠の間を斜めにする。',
 '同じ段の左側、幅48％。第二打の刃と木の接触だけに寄る。橙の線は光る。二回目、コン。読む順は右の第一打から左の第二打。',
 'その下に画像高さの約18％の白い無音の間。次に下の大きな枠なしセナの顔と持ち上げた無傷の鋼剣。刻線の光が消えている。右手で剣を止め、画面外左のカイへ見せる。ここで止まるの発話はこの下の画面にだけ置く。第三打を当てる絵やコンを追加しない。']),
 14:dict(ratio='1:2',composition='上段右の第一打、左の第二打を近い接写でつなぐ。下は排熱溝の一つの大きな枠なし接写、粒の流れを下へたどると小さなカイの目元の挿入へ着く。三打目は次の画像へ残す。',arts=[
 '上段右、幅48％の第一打の接写。カイの素手の右手、鋼剣、木の標的の接触へ寄る。細い橙の刻線は光る。コンは接触のそば。背景は簡潔。',
 '同じ段の左、幅48％の第二打。光る刃、同じ木の標的、小さな木片。コン。実際の斜めのコマ間で二つの短い動作をつなぐ。',
 '中段から下へ、一つの枠なしの大きな鍔の接写。素手のカイが剣を一度止め、清掃済みの排熱溝から細い橙の粒が抜ける。スゥ…は粒のそば。粒は下へ視線を運び、背景は白へ消える。巨大な火炎や魔法はない。',
 '下端左に幅65％の浅い目元だけの挿入。次を試す前のためらいと集中。第三打、成功HUD、セナの安堵はまだ出さない。挿入の後を白へ溶かす。']),
 15:dict(ratio='1:3',composition='右上の握る手だけの短い挿入から、斜めの大きな第三打へ。鍔とHUDの小さな挿入の後に広い白い間を置き、最後に右のセナ、左のカイの静かな顔を近くへ置く。五段の全幅矩形にはしない。',arts=[
 '上端右、幅55％の握り直す素手の右手だけの挿入。ギュッ。剣一本。下に描く打撃の前の瞬間。',
 '次の大きな斜め枠。カイの第三打が同じ木の標的へ当たる。細い橙の刻線は点灯を保つ。コンは接触点の近く。枠の実際の上下の辺を斜めにし、身体の方向と下への視線をつなぐ。余分な剣、爆発、標的の消滅はない。',
 '打撃の下、左寄せの浅い鍔の接写。無傷の溝と保たれた刃の光。一行だけ斬撃強化作動のHUD。HUDはカイ本人の視界、顔や部品を隠さない。',
 'その後に画像高さの約18％の白い無音の間。下段右、幅45％のセナの安堵の顔、出た。の柔らかな発話。背景は白へ柔らかく消す。',
 '同じ下段の左、幅50％、セナより少し下げたカイの顔と肩。肩の力が抜け、小さく笑う。よかったの独り言。右手の剣は画面外へ安全に下ろしている。二人の表情へ背景全景を入れない。']),
 16:dict(ratio='1:3',composition='上に誘いの一つの広い画面、次の段の右に修理係で？左に一緒に戦いに。短い掛け合いの後は広い白い無音の間。受け止めた目元と、自分の剣を使いたい問いは下に大きく枠なしで現れる。',arts=[
 '上の浅い幅85％の画面。セナが盾を左腕へ戻してカイへ向き直り、明日塔へ誘う。剣は素手のカイの右手にある。背景は同じ庭の青い布の扉を少しだけ。',
 '次の段の右、幅45％のカイの顔と工具袋へ下がる目。修理係で、と短く確認。白い背景、顔を大きく。',
 '同じ段の左、幅50％のセナの顔と塔の方向を指す右手。一緒に戦いに、と答える。全文を右から左の縦列で読み、同じ段は右のカイの問いから左のセナの返答へ読む。',
 '返答の下に高さ約20％の白い無音の間。下にカイの目元の浅い枠なしの挿入。受け止め、目が少し大きくなり、緊張がほどける。吹き出しなし。',
 '最下端に大きな枠なしのカイの顔と、自分の一本の剣を持つ素手の右手。初めて自分の剣で冒険へ行ける嬉しさ。相手へこの剣で行っていい、と確かめる。背景は白へフェードし、まだ塔へ移動しない。']),
 18:dict(ratio='1:3',composition='上端に幅60％の小さなセナの返事。白い余韻を挟み、雲と塔の縦軸から庭に並ぶ二人の背中へ下る、画像下部約70％の一つの枠なしの長い夕景。二つの全幅矩形にしない。',arts=[
 '上端右寄せ幅60％、セナの目と優しい小さな笑顔の浅い挿入。カイを画面外左に見てうなずく。うん待ってるの柔らかな発話。背景と輪郭の外側を白へ溶かす。',
 '白い間の後、雲と夕空から巨大な塔の縦軸、白石の街、工房の青い布、最後に庭で同じ方向へ並ぶ二人の背中へ下って読む一つの枠なし風景。下のカイの素手の右手に一本の鋼剣、セナの左腕に盾。二人は一度だけ描く。灯りは灯ったまま。カイの小さな決意の言葉は下の彼のそば、冒頭に先出ししない。余韻を残し、停電・敵・次の事件を出さない。'])
}
GAPS={1:(140,'現実の寂しさからログインへの息継ぎ'),2:(60,'塔の景色から自分の技能を見る'),3:(100,'使えるようになりたい気持ちを道へつなぐ'),4:(80,'青い布の入口から工房へ'),5:(100,'評価を聞く前に一本の剣を見る'),6:(100,'説明を受け止めてセナの評価へ'),7:(160,'不具合の問いを試験へ持ち越す'),8:(180,'止まった光を二人が受け止める'),9:(90,'確認する選択からログを見る'),10:(140,'ログで絞った場所を実物で確かめる'),11:(70,'発見した詰まりから理由を聞く'),12:(140,'再試験を選び、持つ人を変える'),13:(60,'構えから短い二打へ'),14:(620,'ためらう目元から三打目まで待たせる'),15:(240,'成功の安堵から誘いへの静かな余韻'),16:(160,'この剣で行けるか、招待を受け取る'),17:(250,'参加を自分で選んだ後、約束を受け止める'),18:(0,'静かな夕景で閉じる')}

COMMON='''Use case: illustration-story. Edit the referenced finished Japanese Webtoon into a smartphone vertical-scroll composition. The reference is the edit target and preserves character identity, costume, sword, exact story and anime linework, NOT the old full-width stacked layout. Recompose and redraw. This is a finished raster comic, with all dialogue, HUD and sound lettering integrated. No HTML-like cards, no page border, no equal rectangular rows. Use the composition below: unequal floating inserts, actual same-row pairs, large borderless art fading into white, and purposeful quiet space. A narrative moment does not require its own full-width box. White gaps belong to the comic's timing; do not fill them with scenery or extra panels. Within a pair read RIGHT then LEFT, then down. Keep short-action pairs close; separate anticipation and quiet reactions. Do not rotate Japanese glyphs.
Preserve the EXACT adopted utterances, HUD rows and sound words below. True vertical Japanese dialogue, upright black manga glyphs, columns right to left, tails to the actual speaker; thought has dots towards the actual head. Allow glyphs about 5.6 percent of total canvas width, even in narrow inserts; reserve room rather than shrinking letters. HUD is horizontal cyan/navy, only in its owner's view. Sounds are outside balloons, near the drawn source. No dialogue does not prohibit specified HUD or sounds. Do not add other text, captions, panel numbers, arrows or watermark.
Kai: brown hair with right-temple amber streak, amber eyes, ivory rolled sleeves, brown vest, indigo cape, copper cuff on LEFT forearm, bare hands, right-handed, tool pouch. Sena: silver-blonde low ponytail, blue eyes, silver armor, blue tunic and cape, silver/cobalt triangular shield on LEFT arm when specified. ONE steel sword with square brass guard, dark grip and one thin amber inset line. The sword never breaks. Kai made it; Sena tests it before the handover, Kai uses it only after the handover. Modern VR equipment only in the real room. Keep the same courtyard, wooden target, workbench and blue cloth doorway. No added plot, new characters, fire attack, duplicated limbs, black gloves on Kai or later reveals.
'''

def main():
    FOLDER.mkdir(exist_ok=True)
    ep=copy.deepcopy(json.loads((ROOT/'episode-01/episode.json').read_text()))
    if ep.get('scroll_revision'):raise SystemExit('Already adopted; do not replace executed plans.')
    ep['scroll_revision']='scroll_composition_2026_10_07'
    manifest=[];board=['# 第1話 スクロール構図の実行前計画\n\n現行の採用版は episode-01/storyboard.md。68の物語上の瞬間を維持し、各瞬間を全幅矩形へ固定しない。\n']
    for i,s in enumerate(ep['scenes'],1):
        s['gap'],s['gap_purpose']=GAPS[i]
        if i not in PLANS:continue
        plan=PLANS[i];assert len(plan['arts'])==len(s['panels'])
        source=s['file'];s['file']=f'art/r{i:02d}-scroll.png';s['ratio']=plan['ratio']
        s['scroll_layout']=dict(composition=plan['composition'],read_order='上から下。同じ段は右から左。',intent=s['purpose'])
        for q,art in zip(s['panels'],plan['arts']):q['art']=art
        prompt=COMMON+f"\nCanvas width:height {s['ratio']}. Scene {i}: {s['name']}. Location: {s['location']}. Composition takes precedence over the reference's grid: {plan['composition']}\n"
        for j,q in enumerate(s['panels'],1):prompt+=f"\nNarrative moment {j}, in the specified reading order, not a mandatory full-width panel: {q['art']}\n"+render_panel_lettering(q)
        prompt_file=f'production/scroll-revision/r{i:02d}-scroll.txt'
        (ROOT/prompt_file).write_text(prompt)
        manifest.append(dict(scene=i,source=source,source_sha256=hashlib.sha256((ROOT/'episode-01'/source).read_bytes()).hexdigest(),destination=s['file'],prompt_file=prompt_file,prompt=prompt))
        board.append(f"\n## {i:02d} {s['name']}\n\n{plan['composition']}\n\n次の間：{s['gap']}px（390幅）。{s['gap_purpose']}。\n")
        for j,q in enumerate(s['panels'],1):board.append(f"\n{j}. {q['art']}\n"+panel_board(q))
    (FOLDER/'episode.json').write_text(json.dumps(ep,ensure_ascii=False,indent=2)+'\n')
    (FOLDER/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (FOLDER/'storyboard.md').write_text(''.join(board))
    print(f'Prepared {len(manifest)} native recompositions; adopted reader unchanged.')

if __name__=='__main__':main()
