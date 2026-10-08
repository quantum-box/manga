#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Persist the ten-episode screenplay, storyboard and image-generation prompts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAST = ROOT / 'reference/cast.png'

ALT_SCENES = {
1: ['進路希望の白紙と剣道部の補欠の航','母の弁当店を手伝い、灯里からゲームに誘われる','自分の部屋でヘッドセットを装着し接続する','まだ何も見えない中、草の匂いに気づく','初めて見る巨大な星環と竜、広大な谷とミルトの町','ぬかるみにはまった荷車を押すリゼとセナ','三人で車輪を持ち上げ、名前を名乗る','町の橋を渡り、セナから薬の配達を頼まれる'],
2: ['翌日、ミルトを再訪する','航が帰った夜、リゼは薬を届けていた','薬を届け、パン屋で声をかけられる','温かいパンを食べて笑う二人','精霊の風と水で動く町の風車','リゼは自分の巡回の仕事へ向かう','黒冠の守護者の討伐イベントが告知される'],
3: ['剣と盾の訓練をリゼに頼む','剣道の間合いを試すが、盾の扱いに失敗する','水路の巡回中、爪の跡を見つける','獣が飛び出し、先走った帰還者を襲う','盾で負傷兵を守り、リゼが風の剣で獣を退ける','再生成した帰還者が失った剣を嘆く','現地兵はセナの治療を受けて休む','憧れのプレイヤー、怜が航を討伐隊に誘う'],
4: ['怜の隊で自分の役割を教わる','灯里と練習し、盾と立ち位置を直す','討伐隊が使う巡回図にはリゼの署名がある','役割を果たして喜ぶ一方、配達の薬がベンチに残る','遅れて町へ戻り、配達を忘れたことを謝る','リゼから帰り道と戻る時刻の約束を求められる','日本の家で、店の手伝いと討伐の予定が重なる'],
5: ['店の手伝いと帰宅時刻を済ませて冒険へ向かう','仲間と町の門から徒歩で出発する','星環の下を、水路と山へ続く道が延びる','野営で温かい煮込みを食べる','遺構の管理印と王国の依頼を確かめる','杯の水面に振動が伝わる','まだ姿の見えない巨大な足音','音の方を見つめて次の動きを待つ'],
6: ['黒冠の守護者が遺構の奥から現れる','怜の指示を聞き、恐怖の中で一歩を踏み出す','守護者の攻撃で仲間が倒れ、追うか守るか選ぶ','盾で石片を受け、灯里が負傷者を運ぶ','灯里が腕と胸の動作の周期を記録する','守護者が腕を下げる瞬間に関節の制御環を斬る','怜が中枢を斬り、仲間は退避する','中枢が壊れ、分流弁が開いて流れが移る','勝利の後にも手の震えが残る'],
7: ['討伐から町へ帰り、リゼに声をかけられる','町の人々と温かい食卓を準備する','勝利の食卓に、香ばしいパンと煮込みが並ぶ','パンと煮込みを食べ、セナや灯里と笑う','盾の働きをリゼに認められる横で、流量計が下がる','日本へ遅く戻り、冷めた夕飯と母の声を受け止める','翌朝、灯里から復興イベントの表示を知らされる'],
8: ['日本で異変の知らせを読み再接続する','以前水が流れていたミルトの橋の下が干上がっている','パン屋の蛇口から水が出ない','診療所の患者に水が必要になる','住民と桶で水を分担する','町の道を見直して避難先へ向かう','セナが薬を包み、運ぶときの注意を伝える','患者の列が旧道から丘の集会所へ向かう'],
9: ['患者と薬を旧道から集会所へ運ぶ','獣が避難の道をふさぐ','航が盾を構えて列を守る','子どもと最後の患者を避難させる','セナが患者を守り、攻撃を受ける','セナは灯里に薬箱を託す','航の盾が割れ、接続が切断される','日本の静けさに心臓の音だけが残る','無傷の自分の腕を見て、航は再接続をためらう'],
10: ['母に事情を話し、店の仕事と戻る時刻を伝える','仕事を済ませ、自分で再生成と再訪を選ぶ','旧道を歩き、落とした剣だけを拾う','リゼから井戸の水を運ぶ仕事を受ける','桶の受け渡しを続け、患者全員の到着を知る','セナの薬箱を弟子へ渡し、治療を引き継ぐ','パンと水で今日を越え、食事を分け合う','水を戻したいと伝え、まず翌日の配達を約束する','町の灯りから、乾いた水路とまだ見ぬ旅を望む'],
}

STYLE = '''Use case: illustration-story. Asset type: finished original Japanese full-color smartphone vertical webtoon artwork with integrated final Japanese speech balloons, NOT a print manga page. Reference image establishes character faces, hair, costumes and art style ONLY; do not copy its grid or include every reference character. Clear expressive anime linework, painterly fantasy environments, cinematic light, warm human acting, natural hands. Source canvas tall approximately 1024x2560, characters in speech balloons at least 60 source pixels high, bold clean Japanese manga Gothic. Use TRUE VERTICAL JAPANESE: upright glyphs top-to-bottom, columns right-to-left. Preserve exact text, punctuation and reading order. Each described panel is a successive moment; do not duplicate characters within a moment. Vary width and height according to the described camera: wide establishing shots need room, close-ups can be shallow and staggered. Leave generous white space INSIDE this scroll asset where specified; never use a uniform rectangular grid. White/very light ivory page edges. Normal speech: simple oval or softly rounded tall white balloon with tail to the speaking mouth. Gentle tired speech: thin slightly wavering outline and narrow tail. Shouts: angular heavy jagged outline with strong tail. Thoughts: cloud outline and dots toward the thinker's head. HUD: clean translucent blue-gray horizontal display belonging only to KOH/AKARI, never a speech balloon and no ornamented gold frame. Sounds are drawn lettering near their source, not balloons. No words other than those specified. No title, episode number, panel labels, watermark, bonus panels or later events. Do not cover faces, hands, weapons or clues with text. Frame order is top to bottom; any paired close-ups read right to left. Follow the specified shot count and stop at the final described moment.
CAST identity: KOH male17 BLACK messy hair with small cowlick, warm gray eyes, slim, blue-gray tunic cream collar brown belt/boots and plain straight steel sword; Japan outfit is faded teal hoodie/white tee/charcoal trousers, school outfit navy blazer/white shirt/charcoal trousers. LIZE female18 chestnut BOB amber eyes tiny brass ear pendant moss-green courier tunic IVORY shoulder cloth brown boots round wooden shield short sword. AKARI female17 BLACK shoulder-length hair orange geometric clip; Japan navy school blazer glasses; game cinnamon-orange jacket charcoal tunic brown trousers simple wooden bow small brass communicator and no glasses. REI male21 DARK SILVER cropped hair steel practical armor short deep red cloak longsword. SENA MALE38 auburn short hair gentle light stubble oatmeal robe dark olive vest brown medicine satchel wooden medicine box. MIWA Japanese woman44 brown hair tied back ivory blouse INDIGO apron. Only draw the people named in each shot. If food appears: soft golden bread with browned crust, vegetable/meat stew with broad distinct pieces and restrained gloss/steam; Japanese bento white rice softly grouped, golden fried chicken, green vegetables, no dense bead-like dots, holes or pinpoint highlights. Keep food vessels and portions consistent. Non-graphic injuries and restrained blood only; no gore.'''

def P(scene, *lines):
    return {'scene':scene, 'lines':[{'speaker':s,'columns':[c.replace('、','').replace('。','') for c in t.split('|')],'text':t.replace('|','').replace('、','').replace('。','')} for s,t in lines]}

def A(key, location, panels, gap=70, purpose='場面の接続', reveal=False):
    return {'id':key,'location':location,'panels':panels,'gap_before_390':gap,'pacing_purpose':purpose,'reveal':reveal}

EPISODES = [
 {'number':1,'title':'補欠の空','start':'日本の放課後。航はまだゲームへ接続したことがない。','end':'ミルトでリゼとセナを知り、薬の配達を頼まれる。剣は未使用、盾は未所持。','hold':'水不足、運営の秘密、守護者、現地の死者、成長した装備を描かない。','assets':[
 A('01-school','Japan: school and kendo practice hall, late afternoon',[
  P('Wide: high-school desk, blank career choice sheet, KOH in navy school uniform staring down.',('ナレーション','進路希望の欄は、|白いままだった。')),
  P('Shallow close-up: fingers gripping a bamboo practice sword at the kendo hall, not a steel sword.',('音','ギュッ')),
  P('Medium: coach faces five selected teammates; KOH stands outside their line, kendo uniform and no helmet.',('先生','次の大会は、|この五人。')),
  P('Small close-up: KOH accepts the result, lips tight, bamboo sword lowered. No triumphant smile.',('航（心）','また、|呼ばれなかった。'))]),
 A('02-bento','Japan: the family bento shop back room, evening',[
  P('Wide: KOH now in teal hoodie stacks closed takeaway bento boxes; MIWA works behind the counter.',('美和','航、お箸も|入れてね。')),
  P('Close: KOH adds chopsticks, attentive hands and one box only.',('航','うん。')),
  P('Shallow phone close-up: a single message notification, a thumb opening it. No invented app labels.',('HUD','灯里：今日、入れる？')),
  P('Medium: KOH looks at used VR headset in plain cardboard box, hopeful but uncertain.',('航（心）','ここなら、|何かできるかな。'))],100,'日常の仕事から自分の願いへ'),
 A('03-login','Japan: KOH small bedroom, evening',[
  P('Wide: modest desk, lamp, school bag; KOH sits safely with headset in hands.',('航','……よし。')),
  P('Tight hands: KOH fits the headset, one deliberate click.',('音','カチッ')),
  P('Close POV: simple translucent interface fading into white, fingertips press the start option.',('HUD','REGALIA　接続開始'),('音','ピッ'))],90,'接続を自分で選ぶ'),
 A('04-scent','Sparse first sensation; only pale ivory and a few drifting grass seeds, no figure, no landscape, no ring, no dragon',[
  P('ONE borderless sparse composition: empty upper area, a few pale grass seeds low down; a floating vertical thought caption centered right, no person, no face, no frame.',('航（心）','……草の匂い。'))],190,'姿より先に感覚が届く'),
 A('05-first-sky','Elselia: bright grassland outside Milt, afternoon',[
  P('ONE towering borderless cinematic panorama: thin immense luminous celestial ring curves from upper sky through deep perspective into horizon; a distant huge dragon glides below it, mountain valleys and tiny windmills below; small KOH back silhouette at bottom foreground in initial blue-gray outfit. No HUD, no speech, no boxes, no inset.')],940,'感覚から初めて空の広さを発見する',True),
 A('06-cart','Same road outside Milt, same afternoon, cart wheel trapped in muddy rut',[
  P('Medium close: KOH turns toward an offscreen voice, open surprised eyes.',('リゼ（画面外）','そこ、少し|空けてもらえる？')),
  P('Wide: LIZE braces one wheel of a wooden cart while SENA supports its rear; KOH stands next to road, hands empty, steel sword still sheathed.',('リゼ','車輪が|はまっちゃって。')),
  P('Small KOH POV close-up: glance from wheel to empty quest list, translucent HUD only visible to him.',('HUD','依頼：なし'))],180,'声の発生源と位置を確かめる'),
 A('07-push','Same stuck cart, no teleport, same three people',[
  P('Medium: KOH kneels by wheel opposite LIZE, hands under the rim.',('航','こっち、|持ち上げるよ。')),
  P('Shallow action: both lift and SENA pushes; wheel climbs rut, clothing muddy.',('リゼ','せーの！'),('音','ガタン')),
  P('Small close-up: LIZE exhales, lets go of wheel, relieved smile.',('リゼ','助かった。|私はリゼ。')),
  P('Medium KOH: hands dirty, modest smile, he gestures to himself.',('航','航。|……コウでいいよ。'))],55,'短い共同作業を密に読む'),
 A('08-medicine','Milt bridge and market edge, sunset; turquoise water and pale gold supply channel visible under stone bridge',[
  P('Wide: trio walk the cart over bridge toward warm stalls; SENA offers a small tied medicine parcel.',('セナ','コウ、これも|届けてもらえる？')),
  P('Medium KOH looks at parcel, then to SENA. Hands hold ONE parcel.',('航','それも|クエスト？')),
  P('Large gentle SENA close-up, tired kind eyes, not a mysterious grin.',('セナ','今晩、|薬が要るんだよ。'))],240,'ゲームの表示と暮らしの声のずれを受け止める')]},
 {'number':2,'title':'明日のある町','start':'航は一度帰還し、翌日の放課後に再接続する。町の水は通常、セナは生存。','end':'ミルトの仕事と人を覚える。黒冠の守護者のイベント告知を読む。','hold':'水不足、守護者の真の役割、世界の実在の断定を見せない。','assets':[
 A('01-return','KOH bedroom then Milt safe arrival plaza, next day afternoon',[
 P('Medium Japan: KOH takes headset after school, school bag still on desk.',('航','昨日の薬、|どうなったかな。')),
 P('Close hand on start display, blue-white transition.',('音','ピッ')),
 P('Medium Milt: LIZE spots KOH by bridge, same green outfit.',('リゼ','コウ。|今日は早いね。'))]),
 A('02-night-work','Milt clinic porch, medicine box on shelf, afternoon',[
 P('KOH worried close-up, parcel no longer in his hands.',('航','昨日、途中で|帰っちゃって……。')),
 P('LIZE close-up normal practical smile.',('リゼ','私が届けた。|夜には間に合った。')),
 P('SENA wraps a NEW different medicine parcel, one clear action.',('セナ','今日は、|これを頼める？'))],100,'いなかった夜にも進んだ生活'),
 A('03-delivery','Milt lanes, bakery then house door, same delivery route',[
 P('Wide: KOH and LIZE carry medicine along recognizable stone lane, red tile roofs.',('リゼ','青い扉の家。|その先はパン屋。')),
 P('Close hands: KOH gives parcel to elderly resident at blue door, no duplicate parcel.',('住民','ありがとう、|コウ。')),
 P('Medium bakery: baker offers a small golden bread roll, KOH startled.',('パン屋','昨日、荷車を|押してくれたろ。'))],80,'名前と行き先が結びつく'),
 A('04-bread','Same riverside bakery bench, late afternoon',[
 P('Close: warm bread roll on cloth, browned crust soft interior and a tiny wisp of steam, no text.'),
 P('Medium: KOH bites the roll, shoulders relax.',('航','……うまい。')),
 P('Shallow LIZE face laughing with genuine warmth.',('リゼ','顔に|全部出るね。'))],140,'食事と笑いで町を好きになる'),
 A('05-wind','Milt riverside windmill with tiny luminous wind spirits, early evening',[
 P('ONE large borderless vertical scene: water leads downward from bridge to turning windmill, small wind spirits lift cloth flags, LIZE and KOH small at bottom; generous calm sky.',('航','魔法って、|暮らしにも使うんだ。'))],260,'風と水の道をたどる'),
 A('06-work','Same windmill path turning toward guard station, evening',[
 P('Medium LIZE checks a brass patrol token and changes direction.',('リゼ','ここから巡回。|私は行くね。')),
 P('Small KOH face, starts to ask but stops.',('航','……また明日。')),
 P('Wide rear shot: LIZE walks to waterway station, KOH stays at bakery path; independent work continues.',('リゼ','来るなら、|日暮れ前に。'))],100,'誘いより仕事を優先する彼女を見送る'),
 A('07-announcement','KOH POV at market; only HUD overlays for him',[
 P('Close: brass wrist menu responds to KOH touch, soft blue HUD.',('音','ピン')),
 P('Large clean translucent mission window, market blurred behind it, readable exact Japanese.',('HUD','大型イベント　黒冠の守護者　討伐隊募集')),
 P('KOH face looking up, excited possibility.',('航（心）','俺も、|行けるかな。'))],310,'日常を守る町から大きな冒険の誘いへ')]},
 {'number':3,'title':'戻れる剣、戻れない剣','start':'航は討伐に憧れるが、盾と実戦は未経験。','end':'帰還者と現地兵の治療・再生成の違いを知り、怜から誘われる。','hold':'守護者の姿と配分の真相を先に描かない。','assets':[
 A('01-lesson','Milt training yard, morning in game; LIZE left, KOH right',[
 P('Wide: KOH asks to train; wooden practice sword and small round wooden shield on bench.',('航','討伐、行きたい。|剣を教えてくれる？')),
 P('Medium LIZE hands him ONE practice shield, short sword in scabbard.',('リゼ','まず、これ。|持ってみて。')),
 P('Close: KOH awkwardly raises shield left hand and practice sword right, elbows stiff.',('航','重い……。'))]),
 A('02-distance','Same training yard and same wooden weapons',[
 P('Shallow foot close-up: KOH takes kendo stance, tries to step into range.',('航（心）','この間合いなら。')),
 P('Diagonal dynamic action: LIZE lightly shifts his shield aside with wooden sword, controls him without injury.',('音','コン')),
 P('Large KOH surprised face, shield fouls his right arm.',('リゼ（画面外）','剣だけを|見ないで。'))],60,'経験が役立つ部分と足りない部分'),
 A('03-patrol','Milt outer river path; KOH now carries steel sword and borrowed wooden shield; LIZE and one local guardsman',[
 P('Wide: patrol walks riverbank, steel blade sheathed, water plentiful.',('リゼ','盾を左。|足元も見て。')),
 P('Small close: fresh claw tracks in mud under reeds, ominous but not gore.'),
 P('Medium: impulsive red-haired PLAYER traveler runs past the patrol with flashy steel sword.',('帰還者','任せろ！'))],100,'練習から外の実戦へ位置をつなぐ'),
 A('04-beast','Same river bend',[
 P('ONE big angled action shot: lean dark riverwolf-like monster leaps from reeds at the impulsive PLAYER; KOH in foreground frightened, shield held low, LIZE already reacts. Not the black-horn guardian.',('音','ガッ'))],170,'近づく音から危険の姿を見せる',True),
 A('05-defense','Same river bend, no additional monsters',[
 P('Medium: KOH steps LEFT beside local wounded guard, raises borrowed shield, right hand grips sword.',('リゼ','その人の前に！')),
 P('Two quick close-up moments right-to-left within ONE shallow row: shield blocks claw; LIZE gathers pale wind around short sword.',('音','ガン')),
 P('Wide: LIZE pushes beast back with wind and KOH keeps injured guard behind shield.',('リゼ','今、離れて！'))],45,'防御の理由と結果を密に読む'),
 A('06-returner','Safe arrival plaza in Milt after encounter',[
 P('Wide: the red-haired PLAYER reappears in plain replacement clothes, weapon lost, KOH and AKARI nearby.',('帰還者','戻れた。|でも剣がない。')),
 P('Close KOH listens with relief, sword sheathed and shield lowered.',('航','復活、|できるんだ。')),
 P('AKARI in orange game jacket checks a readable blue HUD only for herself.',('灯里','身体を|作り直すんだって。'))],130,'再生成の仕様を知る'),
 A('07-local','Clinic porch, injured local guardsman on bench, SENA cleans a small arm wound; non-graphic',[
 P('Medium KOH looks toward the LOCAL guard, worried.',('航','この人も、|戻せないの？')),
 P('SENA calm close-up, one clean bandage in hands.',('セナ','この身体しか|ないからね。')),
 P('LIZE tightens bandage, clear difference to player; tired expression.',('リゼ','明日は休んで。|仕事は代わる。'))],260,'仕様を身体と仕事の違いで受け止める'),
 A('08-invitation','Same clinic path, golden evening',[
 P('REI in silver armor and deep red short cloak approaches KOH, sword sheathed, friendly.',('怜','さっきの盾、|よく出せたな。')),
 P('Close KOH recognizes his admired player, startled but delighted.',('航','……レイさん？')),
 P('Large REI offers an open empty hand, a genuine invitation.',('怜','討伐隊、|一緒に来るか。'))],290,'小さな役割を英雄に認められる')]},
 {'number':4,'title':'名前を呼ぶ先輩','start':'怜の誘いを受け、航は大きな集団へ参加する。','end':'町の配達を忘れ、戻る時刻を約束する。リゼの巡回図が討伐に使われる。','hold':'リゼは取水の意図を知らない。怜を悪役の表情にしない。','assets':[
 A('01-team','Milt guild training yard, afternoon',[
 P('Wide: REI directs a small mixed PLAYER group; KOH in initial tunic with wooden shield, AKARI bow lowered.',('怜','コウは左。|後衛を守って。')),
 P('Close KOH feels seen when name is called.',('航','俺で、いいの？')),
 P('REI friendly close, gestures toward vulnerable archer.',('怜','さっき、|できてただろ。'))]),
 A('02-role','Same training yard, no lethal attack',[
 P('Action medium: KOH blocks a wooden sparring blow while AKARI retreats behind him.',('音','コン')),
 P('Small AKARI face laughs, practical encouragement.',('灯里','右、空いたよ。')),
 P('Medium KOH shifts feet and shield, a useful small correction.',('航','……こっちか。'))],50,'教わって一つ良くなる'),
 A('03-map','Guild planning table, late afternoon',[
 P('Wide: REI opens one patrol map, KOH and AKARI look from sides.',('怜','上流の遺構。|ここを通る。')),
 P('Close paper: small guard-service seal, a simple route and exact handwritten signature at bottom.',('HUD','リゼ・フェルン')),
 P('KOH notices the familiar name, curious rather than suspicious.',('航','リゼの地図だ。'))],120,'巡回図の署名を手掛かりとして置く'),
 A('04-success','Same practice yard, sun lowering',[
 P('Medium: successful mock formation, KOH shield protects AKARI.',('怜','よし。|その位置でいい。')),
 P('Close KOH smile, genuinely proud.',('航（心）','俺にも、|役目がある。')),
 P('Small late-day shadow of a medicine parcel left on a bench, no label, no text.')],120,'嬉しさの後で置き忘れた約束を見せる'),
 A('05-late','Milt clinic porch at evening, LIZE and SENA finish delivery themselves',[
 P('KOH hurries to porch, medicine parcel now in SENA hand.',('航','ごめん、配達……。')),
 P('LIZE medium, tired but not raging.',('リゼ','終わった。|来ないなら言って。')),
 P('Close KOH lowered eyes, admits mistake.',('航','……うん。'))],230,'叱られた言葉を受け止める'),
 A('06-promise','Same porch, lantern just lit',[
 P('Medium LIZE rests hand on patrol map case, practical.',('リゼ','守護者は危ない。|帰り道も覚えて。')),
 P('Close KOH nods, not yet an effortless hero.',('航','戻ってくる。')),
 P('LIZE clear close-up, quiet firm line.',('リゼ','戻る時間を|言って。'))],160,'曖昧な約束を具体的にする'),
 A('07-japan','Japan bento shop back room, KOH in teal hoodie',[
 P('Medium MIWA holds shop order list, KOH takes off headset after game session.',('美和','明日の夕方、|店をお願いね。')),
 P('Close KOH glances at a small private raid reminder on phone.',('HUD','討伐隊：明日集合')),
 P('KOH answers too quickly, avoids explaining overlap.',('航','うん。|できると思う。'))],230,'二つの約束が重なる')]},
 {'number':5,'title':'出発の朝','start':'航は町への帰還予定を伝えるが、日本の約束と重なる。','end':'初めての遠征、夕方の野営、守護者の足音を聞く。守護者本体はまだ見せない。','hold':'守護者の全身、中枢の働き、水不足、未来の技術を描かない。','assets':[
 A('01-before','Japan bento shop morning; school-free weekend, KOH teal hoodie',[
 P('Close hands: KOH finishes putting chopsticks in bento bags, order list visible with no legible invented numbers.'),
 P('Medium MIWA watches KOH hurry toward stairs.',('美和','夕方は|戻ってね。')),
 P('KOH uncertain half-smile, avoids details.',('航','ゲームの大会。|終わったらすぐ。'))]),
 A('02-gate','Milt town gate in game, morning',[
 P('Wide: REI team gathers, KOH sword and borrowed wooden shield, AKARI bow, LIZE stands at gate to send them off.',('航','日が沈む前に|戻るつもり。')),
 P('LIZE close-up studies him, neither approves all nor forbids.',('リゼ','変わったら、|知らせて。')),
 P('Close KOH tightens leather shield strap, real nerves.',('航','分かった。'))],100,'出発前の約束'),
 A('03-road','Grasslands ascending to old aqueduct valley, midday',[
 P('ONE tall continuous borderless scenic passage: road snakes from near boots at top down through verdant valley, aqueduct spans and pale luminous ring high beyond mountains; tiny travel group, not a giant monster; serene sparse midsection.')],230,'道と景色をたどって遠征の距離を感じる'),
 A('04-camp','Forest camp at edge of ruined water complex, late afternoon',[
 P('Wide: REI directs safe positions; KOH rests borrowed shield against SAME tree, sword remains sheathed.',('怜','先に飯。|慌てるな。')),
 P('Close: a ceramic bowl of vegetable and chicken stew, large soft carrot pieces, gentle steam and appetizing thick broth, no speech.'),
 P('Medium AKARI and KOH share a light laugh while holding bowls.',('灯里','もう腕、|筋肉痛？'),('航','……少し。'))],130,'野営の食事と仲間の気楽さ'),
 A('05-seal','Same camp, ruined intake gate within view',[
 P('Close: AKARI raises brass recorder toward carved crown seal on intake stone, no abstract magic code labels.',('灯里','依頼の印と|同じだね。')),
 P('Medium REI answers plainly, no sinister smile.',('怜','王国の管理区画。|記録しといて。')),
 P('Small KOH looks beyond gate, moonlike ring visible in evening sky.',('航（心）','ここまで、|来たんだ。'))],160,'管理印を記録して冒険の実感へ'),
 A('06-warning','Same camp as twilight deepens; old intake behind trees',[
 P('Close ground: a cup trembles near campfire.',('音','カタ……')),
 P('Medium KOH notices ripples in stew bowl, turns head toward forest, shield still leaning on tree.',('航','今の、何？')),
 P('REI stands from campfire, alert, hand at sword hilt.',('怜','静かに。'))],70,'小さな振動から耳を澄ます'),
 A('07-footfall','Only sparse dark-blue-white forest mist, no creature silhouette, no character, no horn or eye',[
 P('ONE sparse borderless sound-only beat: broad mist and white space, dark heavy Japanese sound lettering lower center; no scenery detail that reveals the source.',('音','ズン……'))],420,'姿を見せず足音を待つ'),
 A('08-listen','Same camp path at twilight, source still outside image',[
 P('Close KOH grips shield LEFT hand from tree and keeps sword sheathed RIGHT side, breath tense.',('航（心）','こんなに、|大きい音……。')),
 P('Medium AKARI lowers recorder and peers toward gate.',('灯里','動いてる。')),
 P('REI tight close-up, eyes fixed offscreen, about to draw.',('怜','……来るぞ。'))],640,'音を聞いた人の反応で次話へ')]},
 {'number':6,'title':'黒冠の守護者','start':'夕暮れの上流遺構、守護者の足音の直後。航は左に盾、右に剣。','end':'討伐成功。守護者中枢は破壊され、供給線が王都方向へ流れる。航は生存し疲労と震えが残る。','hold':'王都の人物、水不足、守護者が善良だという後付け表情、未来の装備を描かない。','assets':[
 A('01-guardian','Ancient intake ruins in twilight',[
 P('ONE monumental borderless reveal: black STONE-AND-BRASS autonomous guardian 18 meters tall, two asymmetrical black crown-like horns, glowing turquoise circular CHEST CORE, long angular forearms and blunt feet; old aqueduct gate behind, tiny REI KOH AKARI team foreground. Awe and real threat, NO biological demon mouth, no wings, no royal person.',('音','ゴオオ……'))],120,'足音の発生源を初めて大きく見せる',True),
 A('02-formation','Same intake courtyard, guardian same horns/chest core',[
 P('Wide: REI calls positions, KOH left foreground shield LEFT sword RIGHT, AKARI behind him.',('怜','コウ、左！|後衛を守れ！')),
 P('KOH close-up sees the giant, afraid and pale, not smirking.',('航（心）','足が、|動かない。')),
 P('Hands close: KOH forces one foot forward, shield raised.',('航','……左。'))],80,'恐怖から一つの行動へ'),
 A('03-collapse','Same courtyard and formation',[
 P('Dynamic diagonal: guardian sweeps one long stone arm across front line; debris low, no gore.',('音','ガァン')),
 P('Medium: PLAYER ally falls beside AKARI, KOH sees him, REI temporarily across the sweep.',('灯里','こっち、倒れた！')),
 P('Close KOH looks from REI target to fallen ally, clear choice.',('航（心）','追ったら、|この人が残る。'))],40,'主役の一撃より目の前の役割を選ぶ'),
 A('04-shield','Same courtyard, fallen ally BEHIND KOH; no teleport',[
 P('Large angled action: KOH plants feet and blocks falling stone fragment with wooden shield LEFT arm; sword RIGHT low.',('航','後ろへ！'),('音','ドン')),
 P('Shallow close: shield develops visible THREE short cracks, left strap intact, glove clenched.'),
 P('Medium: AKARI drags ally behind intact stone block while KOH protects them.',('灯里','運べた！'))],40,'防御の動作と救えた結果をつなぐ'),
 A('05-pattern','Same courtyard, guardian chest turns between shots',[
 P('Close AKARI watches glowing chest and clicking elbow ring, communicator in one hand.',('灯里','腕の後、|胸が光る！')),
 P('Small detail: guardian crouched after striking the sloped ground, brass elbow joint pauses at human shoulder height beside a fallen stair, short turquoise pulse, no system explanation.'),
 P('KOH close-up takes breath, remembers training stance, shield still cracked.',('航（心）','剣だけを|見ない。'))],150,'観察を仲間から受け取る'),
 A('06-opening','Same guardian right forearm within reach; KOH shield LEFT sword RIGHT',[
 P('Unequal quick action shots: KOH deflects a small fragment with shield then steps under long arm, not flying.',('音','ガン')),
 P('Large slanted action frame: with the guardian CROUCHED and its long arm braced against the slope, KOH steps onto ONE low fallen stair and cuts the exposed SMALL brass elbow-control ring now at his shoulder height with his plain sword; no flight or enormous jump, he does not destroy chest core himself.',('航','今なら！'),('音','ザッ')),
 P('Wide result: guardian arm stalls briefly, chest exposed, REI positioned to attack.',('怜','コウ、離れろ！'))],40,'教わった間合いで短い隙を作る'),
 A('07-rei-strike','Same courtyard, KOH retreats, REI attacks exposed chest',[
 P('Medium: KOH pulls wounded ally farther back, clear line for REI, cracked shield held low.'),
 P('ONE large dramatic angled central shot: REI lunges with enchanted longsword into turquoise chest core; bright white-blue fracture, no extra horns.',('音','ガキィン')),
 P('Shallow close: chest core breaks, hands and REI blade readable, no dialogue.')],80,'連携の決め手を大きく読む'),
 A('08-flow','Only intake mechanisms and luminous channel; no characters, no victory window yet',[
 P('ONE tall borderless mechanical consequence: cracked core above; old gate counterweight releases; pale gold stream surges into RIGHT-BRANCH channel below, turquoise local line dims. No explanatory text, no town catastrophe, no labels.',('音','ゴウン……'))],270,'破壊のあとで変わった流れを見せる'),
 A('09-victory','Same courtyard after guardian stops, evening',[
 P('Readable simple blue HUD in KOH view, stopped guardian blurred behind.',('HUD','討伐成功　黒冠の守護者')),
 P('Wide: REI team cheers, AKARI lowers bow, KOH kneels alive among stone debris.',('仲間','やった！')),
 P('Large intimate close: KOH hides visibly trembling RIGHT hand against knee, cracked shield rests beside LEFT knee.',('航（心）','……守れた。'))],320,'勝利を身体の震えと安堵で受け止める')]},
 {'number':7,'title':'英雄の夕飯','start':'夕方の討伐成功後、町へ戻る。町の水槽には残りの水がある。','end':'祝いと日本の夕飯を経験。翌朝、灯里から復興イベントの連絡。','hold':'祝う人々を後の死を知るような表情にしない。水源の因果を説明しない。','assets':[
 A('01-homecoming','Milt gate after sunset, warm lanterns; KOH cracked shield strap bandaged by guard',[
 P('Wide: town greets returning team, LIZE sees KOH walking himself.',('リゼ','戻った。')),
 P('KOH medium tired modest smile, shield crack visible.',('航','……遅くなった。')),
 P('LIZE points toward feast rather than interrogating him.',('リゼ','話は、|座ってから。'))]),
 A('02-table','Town square shared wooden table, night, lanterns',[
 P('Wide: SENA and locals set plates, REI shares bread, AKARI sits by KOH.',('セナ','今日は、|腹いっぱい食べな。')),
 P('Close: hands set a SINGLE bowl of stew before KOH, wooden spoon at right.',('音','コト')),
 P('KOH looks grateful, no dialogue yet.')],130,'戻れた場所の食事を受け取る'),
 A('03-feast','Same meal; appetizing fantasy bread and chicken/carrot/potato stew',[
 P('ONE lush large close-up: browned torn bread revealing soft interior, thick golden stew broad tender chunks in rustic ceramic bowl, little steam, no repeated bead patterns, no text, no faces; ivory edges.')],190,'料理の披露をゆっくり受け止める'),
 A('04-laugh','Same table, same bowl, one spoonful then less in bowl',[
 P('Medium KOH finally eats a spoonful, relaxes, same armorless outfit.',('航','おいしい……。')),
 P('Small AKARI laughing with bread in hand.',('灯里','それ、昨日も|言ってた。')),
 P('SENA leans in kindly, medicine box beside his chair.',('セナ','何回でも|聞くよ。'))],100,'食べる動作から仲間の笑いへ'),
 A('05-recognition','Same feast edge, LIZE next to KOH; no romantic reward pose',[
 P('Medium LIZE notices his cracked shield, points to the repaired strap.',('リゼ','それで、|誰かを守った？')),
 P('KOH close-up, tired but proud.',('航','うん。|一人、運べた。')),
 P('Gentle LIZE smile, quiet acknowledgment.',('リゼ','なら、よかった。')),
 P('Small silent cutaway: brass flow gauge on nearby workshop wall has fallen slightly, no alarm text.')],210,'役割への承認と小さな前兆'),
 A('06-dinner-japan','Japan bento shop kitchen, late night, KOH teal hoodie no sword',[
 P('Wide MIWA waits beside cooled dinner, KOH awkward in doorway.',('美和','夕方、|お願いしたよね。')),
 P('Close KOH looks down, admits delay.',('航','……ごめん。')),
 P('Hands: MIWA slides cooled bento plate toward KOH, same fried chicken/rice/greens, no magical items.',('美和','食べてから、|明日の話をしよう。'))],260,'冒険から日本の約束へ帰る'),
 A('07-message','Japan bedroom then phone next morning; school-free weekend',[
 P('Medium KOH sits after breakfast looking at bruiseless hands, soft contentment.',('航（心）','昨日は、|できた。')),
 P('Shallow phone close: message from AKARI only.',('HUD','灯里：町の表示、見た？')),
 P('Large phone display: brief readable quest classification change, no water scene yet.',('HUD','ミルト　復興イベント開始'))],280,'祝いの余韻から新しい疑問へ')]},
 {'number':8,'title':'水のない朝','start':'翌朝、日本で町の新しいイベント分類を知り、再接続。','end':'診療所を移す準備、旧道の避難経路と役割が決まる。水源は未復旧。','hold':'航は水不足と討伐の因果をまだ確定していない。死者を描かない。','assets':[
 A('01-login','Japan small bedroom morning; KOH teal hoodie',[
 P('Phone close: simple classification window, unchanged content from previous episode.',('HUD','ミルト　復興イベント開始')),
 P('KOH looks uncertain, holds headset.',('航','もう、|次のイベント？')),
 P('Hand presses connect, blue-white glow only.',('音','ピッ'))]),
 A('02-dry-river','Milt bridge first arrival view, early morning; same bridge as episode1',[
 P('ONE large borderless panorama: formerly full turquoise river now narrow trickle under SAME stone bridge; exposed muddy banks, stopped windmill, empty water buckets; KOH tiny at foreground, LIZE farther along the bridge. Bright cold morning, no corpses, no destruction HUD.')],820,'表示の後で暮らしの変化を初めて見る',True),
 A('03-no-water','Milt bakery and public water tap, same morning',[
 P('Close: baker turns brass tap; only one drop falls into cup.',('音','ぽた')),
 P('Wide: empty bakery hearth, fewer bread loaves; local residents carry pails, no generic riot.',('パン屋','今朝から、|焼けないんだ。')),
 P('KOH tight face, recognizes this person and workplace.',('航','昨日まで、|水が……。'))],100,'記憶のある仕事が止まったことを知る'),
 A('04-event','Clinic porch; SENA treats patients, LIZE plans evacuation',[
 P('KOH medium beside clinic, uneasy dismissive suggestion, not mocking.',('航','復興イベント、|なのかな。')),
 P('SENA close, tired concerned face while taking patient pulse.',('セナ','今、この人に|水が要る。')),
 P('KOH silent reaction, HUD closed; hands reach for bucket.')],250,'分類の言葉から目の前の必要へ'),
 A('05-work','Clinic well and shaded yard, same people',[
 P('Wide: KOH and locals hand-line buckets from deep well; AKARI records stock on paper.',('灯里','こっちの井戸は|まだ使える。')),
 P('Close: one filled bucket passes KOH to waiting LOCAL worker, no duplication.',('航','診療所へ。')),
 P('Medium SENA gives a patient one cup, deliberate small success.',('患者','……ありがとう。'))],70,'働いた結果として一人へ水が届く'),
 A('06-route','Guard station map table; same town map, morning',[
 P('LIZE points out riverbank blocked by thirsty riverwolf monsters visible in SMALL map sketches, no actual battle yet.',('リゼ','川沿いは危ない。|旧道を使う。')),
 P('AKARI studies route alongside KOH.',('灯里','坂の上の、|集会所？')),
 P('LIZE nods, specifies KOH duty.',('リゼ','うん。コウは|隊列の後ろ。'))],110,'行き先と守る範囲を具体化する'),
 A('07-box','Clinic porch, packing medicine; SENA still alive',[
 P('Close: SENA arranges two cloth-wrapped glass vials in ONE wooden medicine box, leather satchel open.',('セナ','青い布は、|熱の薬。')),
 P('KOH listens and takes handles of patient cart, same borrowed patched shield slung left.',('航','覚えた。')),
 P('SENA tired gentle smile to KOH, not a deathbed expression.',('セナ','急がなくていい。|割らないでね。'))],190,'命を支える小道具の扱いを覚える'),
 A('08-column','Milt old stone road rising to hillside meeting hall, late morning',[
 P('ONE tall borderless scenic transition: evacuation column with two carts snakes up old road; clinic canopy recedes below, hillside meeting hall visible far ahead; LIZE at front, KOH at rear, AKARI midpoint, SENA by patient cart; no monster in this picture.')],250,'道と並び順を見せて次話へ')]},
 {'number':9,'title':'消えない名前','start':'旧道を登る避難列。リゼ前方、航後方、灯里中ほど、セナ患者の荷車。','end':'患者と子供は避難成功、セナ死亡、航の身体破壊。日本の本人は無傷で机へ戻る。','hold':'凄惨な損傷、セナの復活、王都の黒幕、世界の実在の確定を描かない。','assets':[
 A('01-road','Old hillside road late morning, same evacuation arrangement',[
 P('Wide: KOH pushes rear cart uphill, LIZE signals turn at front; AKARI watches right-hand reeds.',('リゼ','曲がったら、|集会所！')),
 P('Close KOH hands tired on cart shaft, patched shield LEFT shoulder.',('航','もう少し。')),
 P('Shallow reeds twitch and claw tracks cross dry bank.',('音','ガサッ'))]),
 A('02-attack','Same curve of old road, dry riverbank at right',[
 P('ONE big angled action: lean DARK riverwolf-like beast jumps from dry reeds toward rear of column, hungry and dangerous; KOH sees it, two patient carts ahead, no black-horn guardian.',('音','ガッ'))],460,'草の音から襲撃を発見する',True),
 A('03-defend','Same rear of column, nearest stone retaining wall',[
 P('KOH raises patched shield LEFT arm, draws plain sword RIGHT, holds position between beast and carts.',('航','先に行って！')),
 P('Dynamic diagonal: beast claw hits shield, existing THREE cracks widen; restrained wood splinters.',('音','ガン')),
 P('AKARI shoots arrow from midpoint and LIZE turns back toward KOH.',('灯里','リゼ、後ろ！'))],35,'攻撃と防御を密に読む'),
 A('04-escape','Same road curve, one child and a patient cart',[
 P('Wide: cart stalls at curb, frightened child at its near wheel, SENA braces cart.',('セナ','手を離さないで！')),
 P('Close: LIZE takes child by wrist and pulls toward safe stone shelter, the child moves WITH her not duplicated.'),
 P('Medium: KOH shifts shield to block beast pursuing them, leg planted by wall.',('航','こっちだ！'))],45,'患者と子供の位置を守る'),
 A('05-sena-hit','Same shelter entrance, retreating patient cart',[
 P('Wide non-graphic: SENA pushes last patient cart behind shelter while another claw blow knocks him against stone wall; clothes torn at side, small restrained dark stain only, no organs or exposed wound.',('音','ドッ')),
 P('Large KOH shocked close-up, sword still in RIGHT hand.',('航','セナさん！'))],120,'救えた隊列の後で負傷を受け止める'),
 A('06-handoff','Same stone shelter, injured SENA sitting supported, LIZE keeps passage clear',[
 P('Close SENA hands ONE wooden medicine box to AKARI, blue-wrapped vials visible inside; breath weak, no mystical glow.',('セナ','薬箱……|集会所へ。')),
 P('AKARI shaking but takes box, bow slung, both hands on box.',('灯里','分かった。')),
 P('KOH kneels near SENA, looks to LIZE, desperate ordinary speech.',('航','この人も、|運べるよね。'))],320,'引き継ぐ言葉を待つ'),
 A('07-last-shield','Shelter entrance after patients cleared; non-graphic',[
 P('LIZE checks SENA breathing, grief restrained, SENA now still with eyes closed and empty hands; no resurrection shimmer.',('リゼ','……コウ。')),
 P('KOH faces beast again to keep it from shelter; LEFT shield breaks under blow and RIGHT sword drops, no body gore.',('航','来るな！'),('音','バキッ')),
 P('Only KOH POV white-blue safety cutoff, foreground empty light, not local soul or revival.',('HUD','身体損傷　接続を終了します'))],160,'一度きりの別れと帰還者の切断'),
 A('08-heart','Sparse ivory Japanese-bedroom silence, no figure, no landscape, no monster, no medicine box',[
 P('ONE sparse borderless sound-only beat: very broad unoccupied off-white space, small dark heartbeat lettering lower center.',('音','どくん'))],230,'戦闘の音が消え自分の身体だけが残る'),
 A('09-japan','KOH bedroom Japan, afternoon, original teal hoodie and same desk',[
 P('Close: headset removed; KOH checks his real LEFT arm, entirely uninjured, breath shaking.',('航（心）','俺は、|傷もない。')),
 P('Large medium: KOH alone at desk, trembling empty hands beside headset; one reconnect button glows on display, he does not press it yet.',('HUD','再接続'))],910,'鼓動の後に日本の無傷の本人を見せる',True)]},
 {'number':10,'title':'戻る理由','start':'日本の机、航は無傷。ミルトの水源は停止、避難先へ患者と薬箱が着く。','end':'航が再生成後に再訪。診療所再開、当日の食事と水を確保。翌日の配達を具体的に約束する。','hold':'水源をまだ戻さない。死者を復活させない。大陸の真相や最終装備を見せない。','assets':[
 A('01-tell','Japan family shop kitchen, afternoon, KOH teal hoodie MIWA indigo apron',[
 P('Medium KOH approaches MIWA without headset on, scared but willing to speak.',('航','二時間、|戻りたい。')),
 P('MIWA pauses work and listens, firm ordinary mother.',('美和','何があったの。')),
 P('KOH close-up, wet eyes but no dramatic heroic speech.',('航','説明する。|店の仕事も、する。'))]),
 A('02-choice','Same Japan room then safe arrival hub in Milt',[
 P('Hands: KOH finishes one shop task, tells mother the return time before going upstairs.',('航','六時に戻る。')),
 P('Close: deliberate finger press, voluntary return.',('HUD','再生成を申請'),('音','ピッ')),
 P('Medium: new initial-body KOH appears at hub in SAME blue-gray basic tunic, empty hands NO restored sword NO restored shield.')],220,'帰還を自分で選び、身体だけ戻す'),
 A('03-walk','Milt old road to hillside meeting hall, late afternoon',[
 P('Wide: KOH walks the route from episode8 on foot, empty hands, sees discarded broken shield at sheltered curve.'),
 P('Close: he gathers the plain steel sword left by wall, keeps broken shield fragments on ground; do not magically repair shield.',('航（心）','道は、|覚えてる。')),
 P('Medium: KOH approaches meeting hall doorway where LIZE works, sword now sheathed on belt.',('航','……戻った。'))],180,'持ち物の損失と歩いて戻る道'),
 A('04-receive','Hillside meeting hall improvised clinic doorway',[
 P('LIZE close-up exhausted, not instantly happy, one clean bandage in hand.',('リゼ','水を運べる？')),
 P('KOH medium nods and takes one empty bucket.',('航','できる。|どこから？')),
 P('LIZE points toward well behind hall, simple clear duty.',('リゼ','裏の井戸。|急がなくていい。'))],250,'英雄の許しより具体的な仕事を受ける'),
 A('05-water','Same meeting hall backyard well, late afternoon',[
 P('Wide: KOH and local volunteers form bucket relay, AKARI gives notes to clinic volunteer.',('灯里','患者は、|全員ここに着いた。')),
 P('Close: KOH hands ONE filled bucket to worker, fingers shake less.',('航','……よかった。')),
 P('Medium: a LOCAL patient drinks a small cup safely, clinic shelter organized, no cure-all glow.')],70,'救えた人と暮らしの再開'),
 A('06-medicine','Inside same makeshift clinic, wooden medicine box on table',[
 P('AKARI opens SENA wooden box for local adult apprentice healer, blue-wrapped vials present.',('灯里','青い布は、|熱の薬。')),
 P('Apprentice healer nods, takes ONE vial, starts caring for patient.',('薬師の弟子','先生から、|教わってる。')),
 P('Close KOH watches box and empty place beside it, quiet grief, no ghost of SENA.')],280,'亡くなった人の仕事を引き継ぐ'),
 A('07-bread','Meeting hall porch evening, warm lantern and bowls',[
 P('Close: LIZE puts a simple golden bread roll beside KOH empty plate, no speech.',('音','コト')),
 P('KOH looks up and accepts the gesture, quiet sincere.',('航','ありがとう。')),
 P('Wide: residents eat simple meal at shelter, REI delivered plain supply crates at side; water still scarce but tonight is secure.',('ナレーション','今日を越える、|水と食事ができた。'))],320,'小さな受け入れと導入の成果'),
 A('08-promise','Same porch, twilight, KOH and LIZE seated with distance',[
 P('KOH medium speaks carefully, does not claim omniscient blame.',('航','水を戻したい。|何が起きたか、知りたい。')),
 P('LIZE close-up considers before answering, tired practical warmth.',('リゼ','その前に、|明日の配達を頼む。')),
 P('KOH slight genuine smile, specific answer.',('航','日暮れ前に。|今度は、知らせる。'))],440,'返事を待って約束をし直す'),
 A('09-new-road','Milt old waterway next dawn is FUTURE DESTINATION only: no actual repair, no new travel completed',[
 P('ONE borderless expansive final view from meeting hall hillside at twilight: town lights below, dry waterway snakes toward distant mountains and star ring; KOH and LIZE only small back silhouettes on porch, NOT already at the waterworks; no text, hopeful but unfinished journey.')],520,'今日の成果からまだ見ぬ旅へ')]}
]

def prompt_for(ep, asset):
    lettering='Final dialogue has NO Japanese comma or full stop. Use the supplied semantic column breaks. Preserve ellipses and question/exclamation marks exactly. EVERY spoken/thought glyph should have height BETWEEN 5.5% and 6.5% of canvas width (44-52px for793-wide image, 56-67px for1024-wide), including short replies and offscreen speech. NEVER exceed 7%: keep medium-bold regular manga Gothic, not heavy meme lettering. Enlarge balloons and allocate clear negative space rather than shrinking glyphs. Prioritize large readable vertical text at smartphone size. A single sparse beat must remain sparse, not be filled with a scene.'
    layout='Use a tall page for 3-4 shots, varied shallow/large/staggered panels; one shot uses its own natural portrait composition, not stretched to the same height as multi-shot pages.'
    lines=[STYLE,lettering,layout,f"Scene/backdrop: {asset['location']}",f"Episode initial context (later shots have the states specified below): {ep['start']}",f"DO NOT reveal: {ep['hold']}",
           f"Only {len(asset['panels'])} described shot(s). This asset is a {asset['pacing_purpose']} beat. The next asset is separate, so no bonus reply or later reveal."]
    for i,p in enumerate(asset['panels'],1):
        lines.append(f"SHOT {i}, successive top-to-bottom moment: {p['scene']}")
        for d in p['lines']:
            if d['speaker']=='音':
                lines.append(f"Exact originating/continuing drawn sound outside balloons: {d['text']}")
            elif d['speaker']=='HUD':
                lines.append(f"Exact in-world display or written-document text, not speech: {d['text']}")
            else:
                kind='thought, cloud and dots' if '（心）' in d['speaker'] else 'spoken, tail to speaker'
                if d['speaker']=='ナレーション':kind='vertical narration caption, no speaking tail'
                if any(s in d['text'] for s in ['！','来るな','後ろへ']):kind='spoken shout, jagged outline with tail'
                lines.append(f"{d['speaker']} ({kind}), exact full text: {d['text']}; vertical columns RIGHT to LEFT: " + ' / '.join(d['columns']))
    return '\n'.join(lines)

def main():
    assert len(EPISODES)==10 and [e['number'] for e in EPISODES]==list(range(1,11))
    manifests=[]
    prepared=[]
    for ep in EPISODES:
        directory=ROOT/f"episode-{ep['number']:02d}"
        planned=directory/'episode.json'
        if planned.exists() and ((directory/'generation.json').exists() or json.loads(planned.read_text()).get('revision_intent')):
            existing=json.loads((directory/'episode.json').read_text())
            prepared.append(existing)
            manifests.extend(existing['assets'])
            continue
        prepared.append(ep)
        (directory/'art').mkdir(parents=True,exist_ok=True)
        (directory/'review').mkdir(exist_ok=True)
        storyboard=[f"# 第{ep['number']}話 {ep['title']} — 脚本と縦の絵コンテ",'',
          f"開始状態：{ep['start']}",f"終了状態：{ep['end']}",f"伏せる情報：{ep['hold']}",'',
          '各原画は場面の意味と人物の反応を描く。場面の接続、カメラ距離、話者、読む順、小道具は以下の各ショットに記録。縦列は右から左。セリフは原画に含まれ、HTMLには重ねない。', '']
        prompts=[]
        assert len(ALT_SCENES[ep['number']]) == len(ep['assets'])
        for asset_index, a in enumerate(ep['assets']):
            a['episode']=ep['number'];a['prompt']=prompt_for(ep,a)
            a['references']=[str(CAST)]
            a['path']=str(directory/'art'/f"{a['id']}.png")
            a['alt']=ALT_SCENES[ep['number']][asset_index]+'。'+' / '.join(' '.join(f"{d['speaker']}「{d['text']}」" for d in p['lines']) for p in a['panels'] if p['lines'])
            manifests.append(a)
            storyboard.extend([f"## {a['id']}",f"場所・時刻：{a['location']}",
              f"直前の間：390px幅基準で{a['gap_before_390']}px。役割：{a['pacing_purpose']}。空間には予定にない人物や装飾を足さない。",''])
            for i,p in enumerate(a['panels'],1):
                storyboard.append(f"{i}. {p['scene']}")
                for d in p['lines']:storyboard.append(f"   {d['speaker']}：{d['text']}（縦列：{' / '.join(d['columns'])}）")
            storyboard.append('')
            prompts.extend([f"## {a['id']}",'```text',a['prompt'],'```',''])
        (directory/'storyboard.md').write_text('\n'.join(storyboard).rstrip()+'\n',encoding='utf-8')
        if not (directory/'generation.json').exists():
            (directory/'PROMPTS.md').write_text('# 実行する生成指示\n\n参照：../reference/cast.png。顔と衣装だけを共有し、コマ割りをコピーしない。修正指示は実行時に別記する。\n\n'+'\n'.join(prompts),encoding='utf-8')
        (directory/'episode.json').write_text(json.dumps(ep,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'production/episodes.json').write_text(json.dumps(prepared,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'production/assets.json').write_text(json.dumps(manifests,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"Saved 10 screenplays/storyboards: {len(manifests)} artwork assets, {sum(len(a['panels']) for a in manifests)} described shots.")

if __name__=='__main__':main()
