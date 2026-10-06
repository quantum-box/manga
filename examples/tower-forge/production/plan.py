#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Persist the exact opening-arc lettering and scene-specific image prompts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def p(art, speaker='', text='', columns=None, voice='普通の声'):
    return dict(art=art, speaker=speaker, text=text, columns=columns or ([text] if text else []), voice=voice)

def s(name, location, panels, gap=60, withheld='未登場の敵・後の報酬を描かない'):
    return dict(name=name, location=location, panels=panels, gap=gap, withheld=withheld)

EPISODES = [
 dict(number=1,title='あと一撃を打てる剣',scenes=[
  s('ログインの先', '現実の海斗の部屋から、ゲーム内リューメルの工房へ', [
   p('浅い上コマ。現実の黒髪の海斗が机の前でVRヘッドセットをかぶる。両手に小さなコントローラー。現実はTシャツ。', '海斗', '今日は、俺も登る。', ['今日は、','俺も登る。']),
   p('長めの枠なし全景。白石の中世都市、巨大な石塔が雲まで伸びる。画面手前にゲーム内の藍マントのカイ。', '', ''),
   p('右寄せの中コマ。カイの手に小さな半透明HUD。ゲーム内であることを短い表示で示す。', 'HUD', 'ログイン完了', ['ログイン完了'], '表示'),
   p('下の大きなコマ。工房の木の扉の前でセナがカイに古い予備魔導剣を差し出す。自分の普通の剣は鞘。', 'セナ', '先に、これ見て。', ['先に、','これ見て。'])], gap=35),
  s('止まる剣', '同じ工房の作業台、扉に青い布、夕方', [
   p('全幅の状況コマ。セナが右、カイが左。作業台に予備魔導剣一本。二人が刃の橙の刻線を見る。', 'セナ', '二回振ると、止まる。', ['二回振ると、','止まる。']),
   p('小さな手の接写。カイが鍔の近くの弁を開き、詰まった黒い付着物を見つける。', 'カイ', '逃がし弁が詰まってる。', ['逃がし弁が','詰まってる。']),
   p('横に並ぶ小接写を右から左。細い工具で付着物を落とす→小さな弁が開く。セリフはなし。', '', ''),
   p('大きなカイの表情コマ。断言せず剣を持ち上げて窓の光を見る。', 'カイ', '試してから、渡す。', ['試してから、','渡す。'])],gap=45),
  s('あと一撃', '工房に続く石の試験庭、木製の試験標的', [
   p('全幅の庭。カイが修理剣を持つ。セナは離れて見守る。木製標的は正面、一つ。', 'セナ', '前で戦いたいの？', ['前で','戦いたいの？']),
   p('右寄せの胸の寄り。カイが剣を構え、少し照れて真剣にセナを見る。', 'カイ', '自分の剣で、登りたい。', ['自分の剣で、','登りたい。']),
   p('斜め枠の二連動作。橙の細い光を沿わせた鋼剣で二回試す。文字は効果音のみ。', '音', 'ブン', ['ブン'], '効果音'),
   p('広い下コマ。三回目の一撃が木の標的へ当たる。弁から小さな光が抜け、剣は壊れない。', 'セナ', '三回目、出た。', ['三回目、','出た。'])],gap=100),
  s('消えた灯り', '試験庭から同じ工房の街路、夕方が夜へ', [
   p('中コマ。カイが修理剣をセナへ返す。セナだけが受け取る。', 'セナ', 'じゃあ、前衛で来て。', ['じゃあ、','前衛で来て。']),
   p('小さなカイの目元。嬉しさが顔に出て、すぐごまかさない。', 'カイ', '……うん。', ['……うん。']),
   p('浅い上の街路接写。橙の魔導灯が一つ消える。小さな煙はなし。', '音', 'ふっ', ['ふっ'], '効果音'),
   p('長い枠なしの下。工房街の灯りが順に消え、カイとセナが同じ扉から街を見ている。', 'セナ', '街まで、止まった？', ['街まで、','止まった？'])],gap=0)
 ]),
 dict(number=2,title='灯りの消えた街',scenes=[
  s('工房街の夜', '前話と同じ街路、灯りの消えた夜', [
   p('長い全景。三角屋根の工房街、魔導灯は暗く、主都市の遠い明かりだけ残る。カイとセナが見回す。', 'カイ', 'こっちの通りだけだ。', ['こっちの','通りだけだ。']),
   p('中コマ。革エプロンの灰ひげ鍛冶師オルンが扉から出てくる。', 'オルン', '灯炉が止まった。', ['灯炉が','止まった。']),
   p('手の接写。オルンが工房の製作台の暗い石を指す。', 'オルン', '製作台も動かん。', ['製作台も','動かん。']),
   p('下のカイの寄り。自分が使おうと思っていた台を見て心配する。', 'カイ', '直せるの？', ['直せるの？'])]),
  s('残す部品', '同じ工房の入口、オルンの木の机', [
   p('全幅。机へ紙の地図を広げる。オルンが旧水路を指し、カイとセナが聞く。', 'オルン', '旧水路に、蓄積環がある。', ['旧水路に、','蓄積環が','ある。']),
   p('小さな地図と部品図の接写。一つの金属環の絵。', 'オルン', '壊さず持ち帰れ。', ['壊さず','持ち帰れ。']),
   p('左寄せのセナの表情。目的を確認する視線、口は落ち着いている。', 'セナ', '倒すだけじゃ、だめか。', ['倒すだけじゃ、','だめか。']),
   p('下のHUDの寄り。期限を本人の視界に表示、NPCは読まない。', 'HUD', '復旧期限　３日', ['復旧期限','３日'], '表示')],gap=80),
  s('魔法使いの参加', '同じ机、イリスは扉から入る', [
   p('中コマ。紫のボブのイリスが杖を片手に近づき、机に小さな魔石を置く。', 'イリス', '私も、手伝う。', ['私も、','手伝う。']),
   p('小さなカイの顔。旧ゲームの知人の来訪に肩の力が抜ける。', 'カイ', 'イリス、来てたんだ。', ['イリス、','来てたんだ。']),
   p('右寄せイリスの手元。魔石と小さな記録紙。', 'イリス', '魔力の記録は任せて。', ['魔力の記録は','任せて。']),
   p('下の三人の状況コマ。机の地図を中心に、セナ右、カイ中央、イリス左。', 'セナ', '三人で、試してみよう。', ['三人で、','試してみよう。'])]),
  s('最初の遠征', '街の塔の入口、翌ログイン。昼', [
   p('手の二小コマを右から左。回収袋→二本の回復薬を腰に固定。物の数を増やさない。', '', ''),
   p('中コマ。カイが自分の鋼の魔導剣を鞘へ。修理を頼まれた予備剣は街へ残した。', 'カイ', '俺の剣で行く。', ['俺の剣で','行く。']),
   p('小さなセナの顔、期待と少しの緊張。', 'セナ', '無理は、言ってね。', ['無理は、','言ってね。']),
   p('長い枠なし。三人の後ろ姿、巨大な塔の足元の門へ歩く。門は開いている。', 'カイ', '……わかった。', ['……わかった。'])],gap=0)
 ]),
 dict(number=3,title='剣を振る前に',scenes=[
  s('水路への階段','第一層の旧水路、昼の光は上の入口だけ',[p('全幅上コマ。三人が石階段を降りる。セナ前、カイ中、イリス後。水音が下から届く。','音','ざあ…',['ざあ…'],'効果音'),p('長い枠なしの水路。青緑の水と銅の管、下へ向かう階段の動線。敵はまだ見えない。'),p('小さなセナの目元。物陰の音へ目を向ける。','セナ','止まって。',['止まって。']),p('下の中コマ。水路の曲がり角から人ほどの高さの石の守護機が一体出る。橙の刻線。','カイ','来る。',['来る。'])],gap=35),
  s('前で受ける','同じ曲がり角。銅の縦管が位置の目印',[p('斜め枠。小型守護機が突進。セナが盾で受け、カイは斜め後ろ。','セナ','私が受ける！',['私が受ける！'],'叫び'),p('浅い接写。石の腕が盾へ当たる。盾が浅く擦れる。','音','ガン',['ガン'],'効果音'),p('小さなカイの視点。敵の橙の刻線が明るくなり、少し暗く戻る。','カイ','光が、弱くなる。',['光が、','弱くなる。']),p('下のイリスの寄り。敵の周期を見て杖の先を低く構える。','イリス','今は、ためてる。',['今は、','ためてる。'])]),
  s('三人の一撃','同じ守護機との戦い',[p('上の中コマ。セナが敵の腕を盾で外へずらす。','セナ','右、空ける！',['右、空ける！'],'叫び'),p('右寄せの手の接写。イリスの杖から短い火の魔法がカイの剣の刻線へ届く。','イリス','一回分だけ。',['一回分だけ。']),p('斜めの広いアクション。カイが右手の鋼剣で敵の側面を斬る。刃と刻線の火は小さく、間合いを保つ。','カイ','ここだ！',['ここだ！'],'叫び'),p('大きな下コマ。小型機は停止して倒れる。三人が息をつく。水路の位置は同じ。','カイ','……倒せた。',['……倒せた。'])],gap=120),
  s('同じ刻線','同じ場所、戦闘終了後',[p('接写。カイが停止した小型機に膝をつき、動かない刻線を工具で触らず目で調べる。','カイ','剣と、似てる。',['剣と、','似てる。']),p('短いイリスの反応。記録紙に目を落とす。','イリス','魔力の道、だね。',['魔力の道、','だね。']),p('小さな手元。壊れていない小部品を袋へ入れる。大きな環はまだない。'),p('長い下コマ。三人が奥の閉じた格子門を見る。配管の橙の光が向こうへ続く。','セナ','奥まで、つながってる。',['奥まで、','つながってる。'])],gap=0)
 ]),
 dict(number=4,title='強くしたら、壊れた',scenes=[
  s('もう少しだけ','旧水路の格子門前、安全な石の踊り場',[p('全幅。三人が水路の踊り場で短い休憩。カイは剣、イリスは地図、セナは前方を確認。','カイ','もう少し、出せる。',['もう少し、','出せる。']),p('右寄せの接写。カイが剣の小さな弁を締める。これは初めての変更。','カイ','逃がす分を、減らせば。',['逃がす分を、','減らせば。'],'心の声'),p('小さなイリスの顔。変更に気づいて見る。','イリス','試験は？',['試験は？']),p('下のカイの寄り。胸を張り切らず、急いで答える。','カイ','次の一撃だけ。',['次の一撃だけ。'])]),
  s('熱の戻り','同じ水路の門を抜けた先、小型守護機が一体',[p('中コマ。セナが新しい小型機を受け、カイが脇へ走る。敵は前話の倒した個体ではない。','セナ','行ける？',['行ける？']),p('斜め枠。剣が強く橙に光って命中するが、小型機は止まらない。'),p('手と鍔の接写。閉じた弁の周囲で刻線が赤くなり、火花が散る。','音','パチッ',['パチッ'],'効果音'),p('大きなカイの顔と停止した剣。驚きと焦り。剣は刃自体が折れず、回路だけ焼けて暗い。','カイ','止まった……！',['止まった……！'],'叫び')],gap=35),
  s('帰る判断','同じ場所から帰還門へ後退',[p('大きなセナの盾。カイの前へ入り、まだ動く敵の攻撃を受ける。','セナ','剣を下げて！',['剣を下げて！'],'叫び'),p('浅いイリスの手。風の魔法で敵の足元だけを押し、退路を作る。','イリス','退路、開ける！',['退路、','開ける！'],'叫び'),p('全幅。三人で後退、カイも自分の足で走る。倒していない敵は遠くに残る。'),p('下の寄り。帰還門の安全な側でカイが暗い剣を見つめる。顔は落ち込んでいる。','カイ','……俺が、変えた。',['……俺が、','変えた。'])],gap=140),
  s('隠さない','安全な帰還門の踊り場、同じ遠征の終わり',[p('浅い手の接写。カイが閉じた弁を二人に見せる。','カイ','出力を、上げたかった。',['出力を、','上げたかった。']),p('右寄せのセナの表情。怒鳴らず、盾を下ろす。','セナ','次は、先に聞かせて。',['次は、','先に聞かせて。']),p('小さなカイの反応。目を上げ、二人を見る。','カイ','……ごめん。',['……ごめん。']),p('下の中コマ。イリスが剣の状態を紙へ記録する。カイの剣はまだ壊れたまま。','イリス','持ち帰って、調べよう。',['持ち帰って、','調べよう。'])],gap=0)
 ]),
 dict(number=5,title='捨てない設計図',scenes=[
  s('分解する朝','街のオルンの工房、次のログインの昼',[p('全幅。机に焼けた剣、工具、三人とNPCオルン。失敗した剣は同じ形。','オルン','よく、戻ってきた。',['よく、','戻ってきた。']),p('中寄り。カイが自分で工具を取り、オルンに鍔を見せる。','カイ','ここを締めた。',['ここを締めた。']),p('小さな断面の接写。詰まりではなく熱で黒くなった刻線。オルンの太い指が近くにある。','オルン','逃がす道が、ない。',['逃がす道が、','ない。']),p('下のカイの顔。分かった瞬間でも嬉しそうにしない。','カイ','熱も、ためたのか。',['熱も、','ためたのか。'])]),
  s('記録を合わせる','同じ机。魔石と紙の記録',[p('右寄せイリス。記録紙をカイへ向ける。','イリス','私の魔法も、強すぎた。',['私の魔法も、','強すぎた。']),p('浅いセナの顔。カイとイリスの間を見て言う。','セナ','弱くても、続けばいい。',['弱くても、','続けばいい。']),p('手の接写二つを右から左。紙へ流路を描く→弁を開く。紙の図は線だけ、細かい文字なし。'),p('大きなカイの表情。三人へ顔を向けて新案を説明する。','カイ','一撃ごとに、冷やそう。',['一撃ごとに、','冷やそう。'])],gap=70),
  s('作り直す','同じ工房の作業台',[p('上の接写。焼けた導線の細い部分を外す。剣の鋼刃はそのまま。'),p('斜め小コマ。新しい細い導線を溝へ埋め、鍔の近くへ薄い銅の放熱板を取り付ける。','音','カチ',['カチ'],'効果音'),p('右寄せの中コマ。オルンが見守り、カイが仕上げる。','オルン','試験を、忘れるな。',['試験を、','忘れるな。']),p('下の広いコマ。カイが改修剣を両手で水平に持ち、仲間に見せる。','カイ','見てて。',['見てて。'])]),
  s('同じ間隔','工房の石の試験庭、前話の木製標的とは別の健全な標的',[p('全幅。セナが時計のHUDを見て合図。カイが剣を構え、イリスが後ろで魔石を持つ。','セナ','一回、待って。',['一回、','待って。']),p('浅い二連動作。カイが一撃→弁から橙の光が小さく抜け、間を置く。','音','しゅう',['しゅう'],'効果音'),p('斜めの広い下コマ。二撃目でも三撃目でも刻線が暗赤に焼けず、薄い橙を保つ。'),p('小さな三人の顔。イリスが少し笑い、カイが安堵する。','イリス','同じ出力、保てた。',['同じ出力、','保てた。'])],gap=0)
 ]),
 dict(number=6,title='三人で一本の剣',scenes=[
  s('再び水路へ','同じ第一層旧水路、次の遠征',[p('全幅。三人が前と同じ銅の縦管の曲がり角へ戻る。セナの盾の擦り傷は残る。','セナ','同じ場所、だね。',['同じ場所、','だね。']),p('右寄せカイ。改修剣の鍔の銅板を指で確認する。','カイ','今度は、間を守る。',['今度は、','間を守る。']),p('小さなイリスの顔。杖を短く構え、合図を待つ。','イリス','一回分ずつ、送る。',['一回分ずつ、','送る。']),p('下の中コマ。前回退いた門の先で小型機が動き出す。')]),
  s('受けて、待つ','同じ小型機の戦闘',[p('斜め枠。セナが盾で受けて敵の姿勢を止める。','セナ','一、受ける！',['一、受ける！'],'叫び'),p('浅い杖の接写。イリスが小さい火を剣の刻線へ送る。','イリス','二、送る。',['二、送る。']),p('広い攻撃コマ。カイが敵の横へ一撃。剣は細い橙。','カイ','三、斬る！',['三、斬る！'],'叫び'),p('下の静かな小コマ。カイがすぐ次を振らず、弁から熱を逃がす。','カイ','……待つ。',['……待つ。'])],gap=80),
  s('前回の先へ','同じ戦闘から奥の門前へ',[p('浅い接写。敵の刻線が暗くなる時、カイの剣はまだ使える。'),p('斜めの決着。二撃目で敵が停止する。セナの盾は一枚。','音','ガッ',['ガッ'],'効果音'),p('中コマ。三人が立ち止まり、カイが嬉しさと安堵で笑う。','カイ','続けて、戦えた。',['続けて、','戦えた。']),p('小さなセナの反応。親指を立てて笑う。','セナ','三人で、一本だね。',['三人で、','一本だね。'])],gap=100),
  s('大きな脈動','旧水路の奥、大きな扉の前',[p('上の水面接写。橙の光が周期的に水へ映る。','音','どくん',['どくん'],'効果音'),p('長い枠なし。水流と配管をたどり、上から下へ大きな扉へ至る。守護者の姿は上半分へ出さない。'),p('中コマ。扉越しのイリスが聞き耳を立てる。','イリス','同じ周期。でも、大きい。',['同じ周期。','でも、大きい。']),p('大きな下コマ。開いた扉の向こう、石と銅でできた灯炉守護者の全身。胸はまだ閉じている。','セナ','あれが、守ってる。',['あれが、','守ってる。'])],gap=0,withheld='胸部の蓄積環とコアはまだ見せない')
 ]),
 dict(number=7,title='壊していいもの、だめなもの',scenes=[
  s('先に来た攻略者','守護者の部屋の手前、安全な観察台',[p('全幅。カイたちが物陰で観察。白銀の鎧と白いマント、灰髪を結んだヴェインが別の階段から現れる。','ヴェイン','回収の依頼か。',['回収の','依頼か。']),p('右寄せのカイ。警戒しながら、空の回収袋を見せる。','カイ','蓄積環が、必要なんだ。',['蓄積環が、','必要なんだ。']),p('中コマ。ヴェインは敵の位置を示す短い共有ピンを指す。','ヴェイン','胸を割れば、すぐ終わる。',['胸を割れば、','すぐ終わる。']),p('小さいセナの表情。胸の条件を思い出し、首を振る。','セナ','それじゃ、残らない。',['それじゃ、','残らない。'])]),
  s('違う目的','同じ観察台、石柱が位置の目印',[p('右寄せヴェイン。嘲笑せず時間のHUDをちらりと見る。','ヴェイン','俺の隊は、先で待ってる。',['俺の隊は、','先で待ってる。']),p('小さなカイの顔。相手の腕前を分かっていても目的を言う。','カイ','俺たちは、持ち帰りたい。',['俺たちは、','持ち帰りたい。']),p('全幅。ヴェインが脇道へ去る。三人は部屋の手前に残る。','ヴェイン','なら、別でやろう。',['なら、','別でやろう。']),p('下の三人の寄り。カイは少し緊張がほどけ、セナが笑う。','セナ','決まったね。',['決まったね。'])],gap=90),
  s('固定具を探す','観察台から守護者を望む。まだ戦闘は始めない',[p('中コマ。イリスが遠くの胸の扉の周りを指す。','イリス','開く瞬間が、ある。',['開く瞬間が、','ある。']),p('小さな観察の接写。胸の外扉が少しだけ動き、周りの固定金具が見える。コアは見えない。'),p('右寄せカイ。紙へ金具の位置だけ描く。','カイ','固定具だけ、切ろう。',['固定具だけ、','切ろう。']),p('左寄せセナ。盾の角度を変えて考える。','セナ','倒れたら、私が支える。',['倒れたら、','私が支える。'])]),
  s('条件をそろえる','同じ観察台の出口',[p('接写。イリスが水流の止まった銅管を見る。','イリス','水路も、戻したい。',['水路も、','戻したい。']),p('中コマ。カイが弁が開いているか確認し、剣を構える。','カイ','熱が下がったら、行く。',['熱が下がったら、','行く。']),p('小さなセナの足元。大きな盾を持って一歩前へ。'),p('大きな下コマ。三人が守護者の部屋へ進む。敵は両足を地へ置いている。','セナ','始めよう。',['始めよう。'])],gap=0,withheld='胸のコアをまだ露出させない、勝利を先に描かない')
 ]),
 dict(number=8,title='灯炉の守護者',scenes=[
  s('大きな腕','灯炉守護者の広い部屋。左に止まった水路、奥に胸を閉じた敵',[p('全幅。大きな石の腕が三人へ迫る。セナが前で盾を構え、カイは右、イリスは左後方。','セナ','私の後ろへ！',['私の後ろへ！'],'叫び'),p('斜めの浅い衝撃コマ。盾と石腕がぶつかり、セナが膝を曲げる。','音','ドン',['ドン'],'効果音'),p('小さなカイの目。敵の胸に光がたまるのを見て足を止める。','カイ','まだ、ためてる。',['まだ、','ためてる。']),p('下のイリス。杖を下げて水路を指す。','イリス','流れが、止まってる。',['流れが、','止まってる。'])]),
  s('水を通す','同じ部屋、左の流路',[p('上の状況コマ。敵の片足が流路を塞いでいる。位置が分かる見下ろし。'),p('中コマ。セナが左へ移動し、盾の角度で敵の腕を誘導。','セナ','こっちを、見て！',['こっちを、','見て！'],'叫び'),p('斜めアクション。敵が向きを変え片足を持ち上げる。カイは攻撃せず避ける。'),p('大きな下コマ。イリスが短い風で流路の瓦礫を払い、水が通る。','イリス','今、流す！',['今、流す！'],'叫び')],gap=90),
  s('重ねない魔法','同じ部屋、流路が動き始めた',[p('接写。戻った水が銅管を通り、敵の胸の明るさが弱まる。','音','ざああ',['ざああ'],'効果音'),p('右寄せカイ。イリスに向けて手で小さな合図を出す。','カイ','一回分だけ、お願い。',['一回分だけ、','お願い。']),p('浅いイリスの寄り。汗の演出は少し、杖の先の魔石も暗くなっている。','イリス','わかった。',['わかった。']),p('全幅。カイの鋼剣の刻線へ細い火が届き、セナが敵の腕を外へ押す。')]),
  s('踏み込む時','同じ守護者の正面',[p('小さなセナの顔。盾の向こうでカイを見る。','セナ','右、空いた！',['右、空いた！'],'叫び'),p('長めの接写。敵の胸の外扉が開く。中に一本の金属環、中央に魔石。ここが初露出。'),p('右寄せカイの目。魔石ではなく外側の固定金具を見る。','カイ','そこだけだ。',['そこだけだ。'],'心の声'),p('大きな斜め下コマ。カイが踏み込み、右手に剣を振りかぶる。斬った結果は次話へ残す。')],gap=0,withheld='固定具を切った結果、停止した敵、回収した環はまだ描かない')
 ]),
 dict(number=9,title='刃を止める勇気',scenes=[
  s('狙う場所','前話と同じ守護者の胸の前、一撃の続き',[p('上の目線の接写。カイが一瞬だけ中央の魔石へ目を向ける。','カイ','真ん中なら、倒せる。',['真ん中なら、','倒せる。'],'心の声'),p('小さなセナの盾と腕。敵の体重を受け止める。','セナ','支える！',['支える！'],'叫び'),p('斜めの大きな攻撃。カイの鋼剣が中央魔石を避け、外側の固定具だけを断つ。','カイ','こっちだ！',['こっちだ！'],'叫び'),p('浅い手元。切れた固定具が外れ、金属環は無傷で残る。','音','カン',['カン'],'効果音')],gap=60),
  s('止まった腕','同じ部屋、固定具が外れた直後',[p('全幅。敵が崩れそうになり、セナが盾を足場に傾きを抑える。カイは胸の環へ手を伸ばす。','セナ','今、外して！',['今、外して！'],'叫び'),p('小接写。イリスの短い風が腕の落下を横へそらす。','イリス','腕、ずらす！',['腕、ずらす！'],'叫び'),p('大きな手元。カイが金属環を両手で引き抜く。環は一つ。中央魔石も一つで環とともに外れる。'),p('下の広い静かなコマ。守護者は座るように停止、三人は離れて立つ。水は流れたまま。')],gap=140),
  s('持ち帰れるもの','戦闘終了した同じ部屋',[p('小さなカイの手。環を抱え、震えが止まる。身体に現実の怪我はない。','カイ','……壊してない。',['……壊してない。']),p('右寄せイリス。無傷の環を確認して笑う。','イリス','持ち帰れる。',['持ち帰れる。']),p('中コマ。セナが盾を置き、短く息を吐く。','セナ','三人とも、戻れるね。',['三人とも、','戻れるね。']),p('下のカイ。二人へ嬉しそうに顔を上げる。','カイ','ありがとう。',['ありがとう。'],'柔らかい声')]),
  s('帰り道の光','部屋から旧水路の帰還門へ',[p('接写。イリスが回収袋の口を開き、カイが一つの環を入れる。環は袋だけにある。'),p('小さなHUD。目的達成の短い表示だけ。レベル大量上昇や最強称号を足さない。','HUD','蓄積環　回収', ['蓄積環','回収'],'表示'),p('中コマ。セナが帰還門を示す。','セナ','街へ、帰ろう。',['街へ、','帰ろう。']),p('長い枠なしの下。水に映る門の明かりと三人の後ろ姿。静かに歩く。')],gap=0)
 ]),
 dict(number=10,title='次のログインで',scenes=[
  s('環を渡す','リューメルの停止した灯炉、夜',[p('全幅。オルン、三人、巨大すぎない銅の灯炉。イリスが袋を開き、カイが環をオルンへ渡す。','オルン','無傷で、戻したか。',['無傷で、','戻したか。']),p('小さなカイの顔。誇るだけでなく仲間へ視線を向ける。','カイ','三人で、外した。',['三人で、','外した。']),p('手の接写。オルンとカイが環を灯炉の溝へ固定。環は炉にだけある。','音','カチ',['カチ'],'効果音'),p('中コマ。イリスが魔力を少しだけ供給、セナが隣で待つ。','イリス','少しずつ、試すね。',['少しずつ、','試すね。'])]),
  s('街に戻る灯り','同じ灯炉から工房街へ',[p('浅い接写。環の魔石から橙の光が刻線へ届く。'),p('長い枠なし。光が銅管をたどり、下へスクロールすると一つ目の魔導灯が点く。','音','ぽっ',['ぽっ'],'効果音'),p('大きな工房街。橙の灯りが並び、露店のプレイヤーとNPCが少人数で笑う。三人は手前で見上げる。','セナ','戻った。',['戻った。'],'柔らかい声'),p('小さなカイの表情。自分の手から街へ目を上げ、言葉なしで笑う。')],gap=110),
  s('三人の工房','同じ街区の小さな空き工房',[p('全幅。オルンが三人に小さな工房の扉を開ける。木の作業台、棚、橙の一灯。','オルン','ここを、使っていい。',['ここを、','使っていい。']),p('右寄せのイリス。紙を台へ置き、椅子を引く。','イリス','次の剣も、ここで。',['次の剣も、','ここで。']),p('浅いセナの手。三人の共同所有を短いHUDで確定。','HUD','共同工房　登録', ['共同工房','登録'],'表示'),p('下のカイが鋼剣を作業台へ置く。銅板と開いた弁は残る。','カイ','次は、上へ行こう。',['次は、','上へ行こう。'])],gap=100),
  s('現実へ、また冒険へ','工房の別れ→現実の海斗の部屋→塔の遠景',[p('中コマ。セナがログアウト前に手を振り、三人が次の予定を決める。','セナ','明日、九時に。',['明日、','九時に。']),p('浅いカイの顔。明確にうなずく。','カイ','次のログインで。',['次のログインで。']),p('全幅。現実の海斗がVRヘッドセットを外す。机にコントローラー、Tシャツ。窓は夜。ほっとした嬉しい顔。'),p('長い枠なしの最後。ゲームの石塔が星空へ続く。まだ登っていない高い環状門。大きな竜や未来の成長装備を出さない。')],gap=0)
 ])
]

COMMON = '''Use case: illustration-story. Finished full-color Japanese smartphone vertical-scroll Webtoon. ONE portrait illustration around 1024x2048 or 1024x2304, with four deliberately UNEQUAL panels or beats ordered from top to bottom. Reference image establishes character identity, clothes, tools, palette, anime style ONLY; do not copy the reference sheet's layout, labels, portraits, parchment backdrop, or bring every character into every panel. Clean detailed anime linework, readable expressive faces, controlled cel shading, grounded high fantasy, warm natural metals, white page gutters. Medieval sword and magic VRMMORPG; actual world scenery looks like a fantasy adventure, only small HUDs imply gameplay. No futuristic city.
Draw exact Japanese speech as part of the raster artwork. Genuine vertical lettering with upright characters, top-to-bottom within a column, columns RIGHT TO LEFT. Clean printed Japanese manga gothic, near 60px glyph height on a 1024px-wide original, readable at 360px display width; never shrink long dialogue. Each utterance below gives columns in right-to-left order, with / only as a separator in this instruction, never printed. Normal speech: slender oval or rounded tall bubble, tail to speaker. Quiet speech: softly irregular thin outline with tail. Shouts: bold spiky bubble and clear pointed tail. Thoughts: cloud-like shape with dots toward the thinker, no speech tail. HUD is translucent cyan, compact horizontal Japanese is allowed for HUD, not ornamental gold panel. Sound effects are material-appropriate drawn text and may be horizontal. Never duplicate an utterance, add extra visible writing, translate Japanese, show speaker labels, or overlay unnecessary HUD.
Panel layout: shallow establishing/context panel when appropriate, staggered medium conversation or action, narrow object/eye insert, larger lower reaction or result. Use unequal heights and widths, some borderless long scenery; action may have slanted frame borders but keep the lettering upright. Small panels show ONLY close-up subjects, not tiny whole bodies. Dialogue must not cover faces, hands, sword, shield, or clue. Keep clear right-to-left order inside any same-row split. Use varied camera distances for understanding, no uniform four-box grid. Use a white bottom edge/gutter. Characters remain in the same location even if offscreen. Keep actions causal and exact prop state.
Kai: dark-brown short hair, one amber streak at his right temple, amber eyes, ivory rolled-sleeve shirt, brown leather vest, short indigo cape, dark trousers, leather boots, copper cuff left forearm, steel one-handed sword in right hand with square brass guard and one thin orange fuller inset; not a lightsaber. After episode 5 sword has small copper cooling plate beside guard. Sena: silver-blonde LOW ponytail, blue eyes, silver armor over deep blue tunic, navy cape, one triangular silver shield with cobalt line in left hand, straight steel sword on belt when not specified. Iris: plum bob hair, green eyes, teal hood-down cloak, ivory tunic, wooden staff with ONE amber crystal and copper ring. Do not swap their colors, genders, or props. Orun: older male NPC smith with short gray beard and brown apron. Vane: male player, tied-back ash-gray hair, silver armor, white cape. Never introduce unmentioned characters, duplicate hands/limbs/props or show a future reveal early. No watermark.'''

def make_prompt(ep, scene, idx):
    common = COMMON
    if ep['number'] >= 5:
        common = common.replace('1024x2048 or 1024x2304', '1024x3072, a tall 1:3 canvas')
        common = common.replace('near 60px glyph height', 'near 75px glyph height')
        common = common.replace('never shrink long dialogue.', 'never shrink long dialogue. PRIORITIZE large readable lettering; expand the balloons and panel height instead. Maintain around 22-26px visible Japanese glyphs after 360px downscaling.')
    context = ''
    if ep['number'] in [3,4,6,7,8,9]:
        context = ' EVERY fantasy panel is inside the SAME dim underground old aqueduct: damp gray stone VAULTED arches, moss, copper vertical pipes, blue-green shallow flowing water, dry stone walkways, restrained cool lighting. No outdoor city streets, blue heraldic banners, sky, castle, sunshine except a narrow entrance shaft in episode 3 strip 1. Reference 2, when supplied, is aqueduct/guardian identity reference ONLY; do not copy its lettering or layout. Normal guardians are human-height chunky gray stone automatons with orange engraved channels, two arms, two legs, one small round orange chest indicator. Boss guardian is the SAME ancient construction language but three times larger, with a square plated outer chest door covering the removable storage assembly. Never add a second chest core, extra arms, or expose its interior until episode 8 strip 4.'
    if ep['number']==2 and idx<4:
        context = ' SAME NIGHT as the blackout, throughout all panels. Outside windows: DARK blue night, no sun, no daytime sky. Interior light from warm candles only; magical lamps remain off. Maintain Orun as the older gray-bearded brown-apron smith from the previous street panel.'
    if ep['number']==10 and idx<4:
        context = ' SAME NIGHT throughout the restored lamp district and workshop, dark blue night through windows, warm orange lamps only, no sunlight.'
    out=[common + context, f'Episode {ep["number"]}, strip {idx}, scene: {scene["name"]}. Location continuity: {scene["location"]}.']
    for n, panel in enumerate(scene['panels'],1):
        out.append(f'BEAT {n} top-to-bottom. Artwork/camera/focus: {panel["art"].replace("膝の高さの", "人ほどの高さの")}')
        if panel['text']:
            out.append(f'Exactly one utterance by {panel["speaker"]}; voice/shape: {panel["voice"]}. Exact text: {panel["text"]}. Vertical columns RIGHT to LEFT: '+ ' / '.join(panel['columns']))
        else: out.append('Silent beat: no speech bubble, no extra text.')
    out.append('Withheld information: '+scene['withheld'])
    if ep['number'] in [7,8,9]:
        out.append('Encounter continuity: EXACTLY ONE boss guardian in this room. Never add small guardians or a patrol in the background. Reference 3, if supplied, establishes the SAME boss silhouette and CLOSED square metal chest door, not its panel layout. Its orange engraved channels are exterior conduits, not an exposed core. Until episode 8 strip 4, the door is CLOSED, or open only a hairline with interior completely obscured. Only episode 8 strip 4 and episode 9 may reveal the ONE removable brass storage ring with ONE amber crystal at its center; outer clips hold it in place. Keep the ring and core intact until removal, then the empty chest is visibly empty.')
    if (ep['number']==8 and idx==4) or ep['number']==9:
        out.append('Storage assembly continuity: the OPEN square chest door swings to the side with its flat round orange exterior indicator attached to the door, distinct from the inner core. Inside the chest is ONE portable brass ring about 30cm in diameter, holding ONE faceted amber crystal about 8cm tall at its center on short metal bridges. Four outer clips secure this assembly. The amber crystal is a faceted gem, not the flat exterior status indicator. Never multiply the ring, crystal, or recovered assembly. Reference 4, when supplied in episode 9, establishes the revealed ring assembly from episode 8, not a future victory or a repeated panel.')
    if ep['number']==10:
        out.append('Prop continuity: reference 2 establishes Orun as the same older gray-bearded smith in a brown apron, not an extra visitor or the setting. Reference 3, if supplied, establishes the recovered ONE portable brass ring with ONE faceted amber crystal and short metal bridges. Do not copy the aqueduct background or speech. In strip 1 the ring is handed from Kai to Orun and then installed into the copper furnace. After installation the ring remains ONLY inside the furnace; the recovery bag is empty and nobody carries another ring. In strips 3 and 4 no ring is visible. Iris retains her separate amber-tipped wooden staff.')
    return '\n'.join(out)

def main():
    current_path=ROOT/'production/episodes.json'
    if current_path.exists():
        current=json.loads(current_path.read_text())
        for idx,ep in enumerate(current):
            if ep.get('revision'):EPISODES[idx]=ep
    for ep in EPISODES:
        if ep.get('revision'):
            continue  # Preserve the separately revised script and exact used prompts.
        d=ROOT/f'episode-{ep["number"]:02d}'
        (d/'art').mkdir(parents=True,exist_ok=True)
        prompts=[]
        board=[f'# 第{ep["number"]}話 {ep["title"]}', '', 'セリフは原画に縦書きで一体生成。列は右から左。画像は場面単位で、各場面内の4つの理解・行動を大小のコマへ分ける。', '']
        for idx,scene in enumerate(ep['scenes'],1):
            scene['id']=f'{idx:02d}'
            scene['file']=f'art/{idx:02d}.png'
            scene['prompt']=make_prompt(ep,scene,idx)
            prompts.append(f'## {idx:02d} {scene["name"]}\n\n```text\n{scene["prompt"]}\n```')
            board.extend([f'## {idx:02d} {scene["name"]}',f'- 場所と接続：{scene["location"]}',f'- 次の場面までの白い間：{scene["gap"]} CSS px（390px幅時）。短い動作は密、結果を受け止める場面は長め。',f'- 伏せる：{scene["withheld"]}', ''])
            for n,panel in enumerate(scene['panels'],1):
                board.append(f'{n}. **読者が理解すること／絵・カメラ・焦点**：{panel["art"]}')
                if panel['text']:
                    board.extend([f'   - 発話者：{panel["speaker"]}。全文：{panel["text"]}。声：{panel["voice"]}。',f'   - 縦列（右→左）：'+ ' / '.join(panel['columns']), '   - 顔・手・重要な部品を避けた上側へ吹き出し。尾は話者へ。HUD・音以外は縦書き。'])
                else: board.append('   - 無言。文字領域は不要。反応と視線で次へつなぐ。')
                board.append('   - 画面外の仲間は同じ場所にいる。所在・所持品の変更は記載の動作に限る。')
            board.append('')
        (d/'storyboard.md').write_text('\n'.join(board).rstrip()+'\n',encoding='utf-8')
        (d/'PROMPTS.md').write_text('# 作画指示\n\n方式：組み込み image_gen。参照：../reference/party.png。\n\n'+'\n\n'.join(prompts)+'\n',encoding='utf-8')
        (d/'episode.json').write_text(json.dumps(ep,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'production/episodes.json').write_text(json.dumps(EPISODES,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if not (ROOT/'reference/PROMPTS.md').exists():
        (ROOT/'reference/PROMPTS.md').write_text('# 共通の人物参照\n\n組み込み image_gen で生成した三人の全身と顔の参照。原本を加工せず party.png へコピー。\n\nカイ：茶髪と琥珀の一房、藍の短いマント、白シャツ、革ベスト、鋼の片手剣。\nセナ：銀金の低いポニーテール、青い布と銀鎧、三角盾。\nイリス：紫ボブ、青緑のマント、琥珀石一つの木の杖。\n\n用途：同一性と画風の基準。コマの構成や同時に描く人物数の基準にはしない。\n',encoding='utf-8')
    print(f"{len(EPISODES)} episode plans, {sum(len(ep['scenes']) for ep in EPISODES)} image scenes saved. Existing revised scripts preserved.")

if __name__=='__main__':main()
