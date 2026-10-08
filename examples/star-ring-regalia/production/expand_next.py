#!/usr/bin/env python3
"""Deepen later episodes after the preceding episode has been published."""
import argparse
import copy
import json
from pathlib import Path
from prepare import ROOT, P, A
from expand_opening import finish, write


def episode_three():
    ep=copy.deepcopy(json.loads((ROOT/'episode-03/episode.json').read_text()))
    old={a['id']:a for a in ep['assets'] if a['id'] in (
        '01-lesson','02-distance','03-patrol','04-beast','05-defense',
        '06-returner','07-local','08-invitation')}
    ep['start']='土曜の朝。航は朝食を終えてミルトへ戻り、討伐隊に憧れて自分から剣と盾の訓練を頼む。'
    ep['end']='小さな防御で現地兵を助ける。帰還者の有限な再生成と失う装備、現地兵の休養と仕事の違いを知る。借りた盾を訓練場に返した後、土曜の早い午後に怜から誘われる。'
    ep['revision_intent']='第1・2話の増補で得た暮らしと身体の経験を継ぐ。習う理由、失敗と再試行、疲れ、装備の持ち替え、借り物の責任、襲撃の前後、治療と再生成の違いを一連の時間として描く。大陸の真実を早く明かさない。'
    assets=[]
    def keep(key,gap=None):
        a=copy.deepcopy(old[key])
        if gap is not None:a['gap_before_390']=gap
        # No empty alternative-text separators from silent moments.
        a['alt']=a['alt'].split('。',1)[0]+'。'+' / '.join(
            ' '.join(f"{d['speaker']}「{d['text']}」" for d in p['lines'])
            for p in a['panels'] if p['lines'])
        if key=='02-distance' and 'reflexively reverts' not in a['panels'][1]['scene']:
            a['panels'][1]['scene']+=' KOH reflexively reverts to his real-world TWO-HANDED kendo grip; shield hangs awkwardly from LEFT forearm and obstructs his RIGHT arm. This is the failed habit the next retry corrects, not a new correct stance.'
        if key=='04-beast':
            a['panels'][1]['scene']=a['panels'][1]['scene'].replace('his forearm','his RIGHT forearm')
        if key=='07-local' and 'adopted artwork establishes' not in a['location']:
            a['location']+='; the adopted artwork establishes injured RIGHT forearm'
        assets.append(a)
        return a
    def add(a,alt,refs=()):
        a=finish(ep,a,alt)
        a['references'] += [str(ROOT/r) for r in refs]
        if a['id'] in ('00-yard','01-grip','02-retry','02-rest','02-change','07-promise'):
            a['references'].append(str(ROOT/'episode-03/art/01-lesson.png'))
        if a['id']=='03-listen':
            a['references'].append(str(ROOT/'episode-03/art/03-patrol.png'))
        a['prompt']+='\nContinuity: KOH always holds the ONE borrowed plain wooden round shield with his LEFT hand, wooden or steel sword with his RIGHT. Shield uses the same wood boards, small metal central boss, narrow metal rim and leather inner grip as adopted 01-lesson. No glowing rune, no shield skill learned yet. Steel scabbard remains at LEFT hip for right-handed drawing. Steel sword stays sheathed during wood-sword practice; wood sword returns to shared bench before patrol. Nameless LOCAL guardsman is adult male with gray hair, short dark goatee, dull steel helmet, sand scarf, brown leather armor and polearm; the adopted originals establish injury on his RIGHT forearm, with LEFT hand available to carry polearm. The impulsive PLAYER is short red-haired, bronze armor before defeat, plain beige replacement clothes after regeneration. Only the people described appear; no guardian or administrative reset.'
        assets.append(a)
        return a
    add(A('00-japan','Japan modest bento-shop home kitchen, Saturday morning; KOH teal hoodie white shirt, MIWA indigo apron offscreen nearby',[
        P('Shallow ordinary smartphone on breakfast table: same simple REGALIA event notice about the black crown guardian, exact horizontal text 黒冠の守護者 and 討伐隊募集. KOH looks at it with eager eyes. Breakfast plate has been emptied, headset waits on shelf, no magical sword or shield in Japan.'),
        P('Medium KOH carries his own empty breakfast plate toward sink, THEN reaches toward headset on shelf. Warm everyday kitchen, open bottom white fade, no logged-in game view here.',('航（心）','今日は|剣を習いたい'))
    ],80,'冒険の前に日本の朝と自分の意志を置く'),'朝食を終え、剣を習おうと決める',('episode-01/art/02-home-rule.png',))
    add(A('00-yard','Milt same stone-lane training yard, Saturday morning, KOH initial tunic sword SHEATHED and NO shield yet; LIZE green courier outfit preparing to patrol',[
        P('Wide KOH approaches the small open training yard ON FOOT from the safe-square lane. LIZE kneels beside a bench checking a worn spare round wooden shield strap, wooden practice swords beside it. One shield is lying on bench, no borrowed shield in KOH hands yet.',('航','今日は|剣を習いに来た')),
        P('Medium LIZE looks up from the strap and smiles practically, hand remains on spare shield, her own short sword sheathed.',('リゼ','巡回の前なら|少しできるよ'))
    ],200,'相手の仕事の前に訓練の時間を頼む'),'巡回前のリゼへ訓練を頼む')
    keep('01-lesson',80)
    add(A('01-grip','Same yard and ONE borrowed round wooden shield, KOH LEFT shield RIGHT wooden practice sword; LIZE demonstrates with empty hands',[
        P('Shallow rear of shield close-up: KOH LEFT fingers go around inner wooden grip and forearm under leather strap. Correct wrist anatomy, only ONE grip and shield.',('リゼ（画面外）','肘を|固めないで')),
        P('Medium KOH bends LEFT elbow slightly and lowers shield rim so his RIGHT wooden sword can move freely. LIZE points toward his elbow without pulling his arm.',('航','こう？')),
        P('Shallow boots on stone dust then shoulders: KOH feet a little staggered, shield left, wooden sword right, eyes look across top rim at LIZE.',('リゼ','相手と足元|両方見るの'))
    ],70,'持ち方を手と肘と足へ分ける'),'盾の取っ手、肘、足を順に確かめる')
    keep('02-distance',70)
    add(A('02-retry','Same yard immediately after first failed practice, nonviolent controlled wood-sword contact only',[
        P('Medium KOH breathes out, deliberately lowers the LEFT shield a little and places RIGHT wooden sword outside shield edge; embarrassed but determined.',('航','もう一回|いい？')),
        P('Large diagonal controlled contact: LIZE wooden practice sword gently touches KOH shield rim, KOH shifts LEFT boot half a step back, shield not fused with right hand, no explosive magic.',('音','コン')),
        P('Shallow LIZE approving face, her wooden sword lowered after one successful touch. KOH remains a novice, no grand victory.',('リゼ','今の感じ'))
    ],70,'直前の失敗を一回だけやり直す'),'盾と足をやり直し、一度だけ受ける')
    add(A('02-rest','Same yard bench, morning, KOH left forearm tired, ONE shield and ONE wooden sword set on bench; initial steel sword still SHEATHED',[
        P('Close KOH LEFT hand trembles mildly as he lowers borrowed shield onto bench. Not a severe injury. Sweat at temple, shoulders relax.',('航','腕が|震える……')),
        P('Medium KOH sits and drinks from ONE plain water flask; LIZE rests beside bench rather than pushes him immediately back to combat.',('リゼ','休むのも|練習'))
    ],210,'疲れと休む時間を身体へ残す'),'盾を下ろし、水を飲んで休む')
    add(A('02-change','Same bench after short rest; KOH initial plain steel sword in his own brown scabbard; borrowed plain wood shield belongs to LIZE as spare',[
        P('Shallow KOH returns ONE wooden practice sword to shared bench beside the other spare practice tools, not holding steel yet. Shield rests at bench edge.'),
        P('Medium KOH uses RIGHT hand to draw his OWN plain straight steel sword briefly from brown scabbard, LEFT holds scabbard, recognizes heavier weight. No shield in hands during this check.',('航','こっちは|もっと重い')),
        P('Medium KOH has resheathed steel sword and picks the ONE spare wooden shield up with LEFT hand for patrol. LIZE points to this specific bench, explains ownership and return place.',('リゼ','盾は私の予備|帰ったらここへ'))
    ],100,'木剣を返し、実際の装備と借り主を確かめる'),'木剣から自分の鋼剣へ持ち替え、盾の返す場所を聞く')
    keep('03-patrol',180)
    listen=add(A('03-listen','Same healthy riverbank bend under reeds, nameless local guardsman beside LIZE, impulsive red-haired PLAYER ahead; NO beast shown',[
        P('Shallow empty reeds shiver near muddy path, only grass and moving leaves. A SINGLE ガサ… inscription starts at right side of reeds and extends toward panel border. No eyes or claws or creature silhouette yet.',('音','ガサ…')),
        P('Small KOH eye-and-left-shield close-up reacts to the offscreen rustle as he slips the borrowed shield from its walking sling onto LEFT forearm; red-haired bronze-armored traveler back only in farther edge, turning ahead. Continue the same sound with faint trailing … into large white bottom fade, no second complete inscription. No visible beast.')
    ],100,'獣の姿より先に草の音を届ける'),'草の音を聞き、盾を持つ手が止まる')
    listen['panels'][1]['sound_continuations']=[{'origin':'03-listen:1','text':'…','placement':'Only the faint dots of the ONE previous ガサ… trail through the white fade; do not repeat ガサ'}]
    listen['prompt']+='\nOnly ONE ガサ… begins in shot 1; its faint remaining dots cross shot 2 and the open bottom fade. No second complete sound.'
    keep('04-beast',880)
    add(A('04-find','Same river bend directly after red-player body dissolves; one dropped steel sword in mud, local guard wounded RIGHT forearm, riverwolf offscreen a few steps ahead',[
        P('Shallow dropped red-player steel sword lies on mud near reeds, not vanished and not automatically returned. A boot of the injured LOCAL guard braces beside it; his RIGHT forearm held close, blood only a tiny restrained mark.'),
        P('Medium KOH sees the LOCAL guard crouching ahead, raises ONE shield with LEFT hand and steps between guard and OFFSCREEN threat. RIGHT hand takes his own steel sword hilt, two swords distinct: his own versus lost one in mud. LIZE moving toward flank, no guardian.')
    ],50,'消えた身体、残った物、痛む人を同じ場所に置く'),'泥の剣と負傷した現地兵に気づく',('episode-03/art/04-beast.png',))
    keep('05-defense',50)
    add(A('05-recover','Same river bend after LIZE wind drives ONE riverwolf away; daylight, no new monsters, nameless guard injured RIGHT forearm',[
        P('Wide wolf retreats physically into reeds on LEFT far bank edge, same dark lean animal with tail, visible direction and diminishing distance. LIZE sword down but alert, no creature dissolved or respawned.',('リゼ','追わないで')),
        P('Medium LOCAL guard uses healthy LEFT hand to press cloth against wounded RIGHT forearm. Polearm rests upright against a tree during this pause. KOH left shield low and own sword resheathed stands beside him.',('航','歩けますか')),
        P('Wide three walk back toward visible Milt gate at same river path. KOH matches LOCAL guard pace, LIZE walks outer side keeping watch. Dropped red-player sword remains behind in mud near reeds, not magically collected.')
    ],120,'逃げた敵を追わず、助けた人と帰る'),'獣を追わず、現地兵の歩調で町へ帰る',('episode-03/art/04-beast.png',))
    keep('06-returner',240)
    add(A('06-supply','Same Milt safe arrival plaza after red-haired player regeneration; KOH sword sheathed left shield, AKARI game orange jacket no glasses, one local supply clerk',[
        P('Medium local supply clerk points to a modest waiting bench and almost empty replacement-clothes shelf; gives plain spare boot pair to regenerated PLAYER in beige clothes, not his lost armor or sword.',('係の人','次の身体も|用意がいる')),
        P('Shallow regenerated red-haired PLAYER looks at empty hands and plain clothes, remembers his weapon still physically at riverbank.',('帰還者','剣は川に|落ちたままだ')),
        P('Medium AKARI lowers her own brass communicator, speaks to KOH with relief for person in Japan, her wooden bow remains on back.',('灯里','日本の身体は|無事だって'))
    ],100,'再生成と物品の損失を分け、供給の限りを置く'),'予備の供給と、戻らない装備、日本の本人の無事を聞く',('episode-03/art/06-returner.png',))
    keep('07-local',280)
    add(A('07-clinic','Same clinic porch immediately after nameless guard RIGHT forearm bandaged, Saturday midday; SENA male38 medicine box, LIZE patrol token board, KOH nearby',[
        P('Shallow LIZE moves ONE patrol token from tomorrow active row to a reserve peg beside the clinic board. No readable unexplained bureaucratic chart, no giant UI, no promise to heal instantly.'),
        P('Medium SENA closes ONE wooden medicine box gently beside seated LOCAL guard, addresses KOH with practical thanks. Guard rests right bandaged arm on lap, same gray hair and goatee.',('セナ','休ませる場所まで|運んでくれて助かった'))
    ],130,'手当てに合わせて明日の仕事を代える'),'巡回の担当を代え、セナが運んだ仕事をねぎらう',('episode-03/art/07-local.png',))
    add(A('07-promise','Same training yard spare bench reached by KOH and LIZE on foot after clinic, Saturday early afternoon; ONE borrowed spare wooden shield, no combat',[
        P('Close KOH uses plain cloth to wipe mud from ONE wooden shield rim on bench, shield detached from LEFT arm, his own steel sword stays sheathed at belt. No magically repaired cracks.'),
        P('Medium KOH looks up from cleaned shield toward LIZE, asks rather than silently claims borrowed property.',('航','明日も|借りていい？')),
        P('Wide LIZE points toward spare shield shelf right above the same bench. KOH places ONE cleaned shield there and removes hand, now shieldless.',('リゼ','ここに置いて|次も一緒に練習しよう'))
    ],160,'借りた道具を返し、次の練習を相手と決める'),'借りた盾を拭いて返し、次の練習を約束する')
    invitation=keep('08-invitation',240)
    invitation['location']='Same clinic path revisited from nearby training yard, Saturday EARLY AFTERNOON, warm clear daylight; KOH has returned borrowed shield, own sword remains sheathed'
    shield_state=' KOH hands empty, NO shield, own steel sword remains sheathed.'
    invitation['panels'][1]['scene']=invitation['panels'][1]['scene'].split(shield_state)[0]+shield_state
    time_note='This follows shield returned to training bench. KOH has NO shield in any shot; own sword remains sheathed. Warm early afternoon daylight, not sunset or night. REI genuinely offers an invitation, no villain pose. Preserve all exact dialogue.'
    invitation['prompt']=invitation['prompt'].replace('golden evening','early afternoon daylight').split('\n'+time_note)[0]+'\n'+time_note
    ep['assets']=assets
    return ep


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--episode',type=int,choices=(3,),default=3)
    args=parser.parse_args()
    write(episode_three(),
          scroll_notes='第3話：草の音は獣の姿より先に始め、白い間へ続ける。失敗、再試行、休憩、実戦、帰還後の手当てと道具の返却を省略しない。',
          art_notes='既存原画を活かす。現地兵の負傷は採用原画どおり右前腕。02-distanceの両手の剣道握りは失敗の瞬間として扱う。08-invitationは土曜の早い午後へ光を揃える。')
