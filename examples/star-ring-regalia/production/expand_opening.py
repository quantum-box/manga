#!/usr/bin/env python3
"""Revise the opening through embodied encounters, preserving executed artwork."""
import argparse
import copy
import json
from pathlib import Path
from prepare import ROOT, CAST, P, A, STYLE, prompt_for

REFERENCE = ROOT/'episode-01/art/07-push-final.png'
STYLE = STYLE.replace('Source canvas tall approximately 1024x2560, characters in speech balloons at least 60 source pixels high, bold clean Japanese manga Gothic.', 'Use a natural tall canvas approximately 900x1900 for three moments, 900x2200 for four. Sparse sound beats have their own proportions. Clear medium-bold Japanese manga Gothic.')

def finish(ep, asset, alt):
    asset.update(episode=ep['number'], references=[str(CAST), str(REFERENCE)],
                 path=str(ROOT/f"episode-{ep['number']:02d}"/'art'/f"{asset['id']}.png"))
    asset['alt'] = alt + '。' + ' / '.join(' '.join(f"{d['speaker']}「{d['text']}」" for d in p['lines']) for p in asset['panels'] if p['lines'])
    # Keep scene-specific instructions and the semantic vertical columns, replace
    # only the old canvas rule which conflicted with the lettering width rule.
    prompt=prompt_for(ep, asset)
    prompt=STYLE+'\nFinal dialogue'+prompt.split('Final dialogue',1)[1]
    asset['prompt']=prompt+'\nInput 1 defines faces and costumes. Input 2 defines the established drawing style and KOH/LIZE/SENA identities only. Do not copy its shot arrangement or muddy state where the scene says clean. Only the specified people appear. All dialogue glyphs approximately 5.5 to 6 percent of the full source width, regular manga weight. Preserve right-to-left column order. No bonus panel or later event.'
    for p in asset['panels']:
        for continuation in p.get('sound_continuations',[]):
            asset['prompt']+='\nContinuing the SAME sound from '+continuation['origin']+': '+continuation['text']+' — '+continuation['placement']+'. Do not repeat a second complete sound or cancel it with a no-text rule.'
    if asset['id']=='07-flow':
        asset['references'].append(str(ROOT/'episode-01/art/07-water-final.png'))
        asset['prompt']+='\nInput 3 preserves the same bridge, flowing river and little warm gold supply channel in the immediate previous moment. It does not dictate shot arrangement. This two-moment asset can be about 1024x1536, with an airy wide infrastructure view above and a focused human response below.'
    return asset

def episode_one():
    ep=copy.deepcopy(json.loads((ROOT/'episode-01/episode.json').read_text()))
    old={a['id']:a for a in ep['assets'] if a['id'] in ['01-school','02-bento','03-login','04-scent','05-first-sky','06-cart','07-push','08-medicine']}
    ep['start']='木曜の放課後。川口の高校生・航は部活の補欠。初めてREGALIAへ接続する。'
    ep['end']='ミルトで魔法と魔導器、精霊、荷運びの暮らしを体験する。薬の配達を引き受けかけるが帰宅の約束を思い出し、リゼが代わる。安全な広場から帰り、翌日の日暮れ前の再訪を約束。剣は抜いて重さを確かめただけ、戦闘と盾は未経験。'
    ep['revision_intent']='2026-10-08の「1・2話が短く没入感がない」への改稿。世界の名前、旅、身体の操作、暮らしの魔法、道具と練習の違い、精霊の意志、帰還と再訪を行動と反応で示す。余白と継続音を場面内で設計する。旧版の23の瞬間を保ち、前後に経験と理解を足す。'
    assets=[]
    def keep(key, gap=None):
        a=old[key]
        if gap is not None:a['gap_before_390']=gap
        assets.append(a)
    def add(a, alt): assets.append(finish(ep,a,alt))
    keep('01-school')
    keep('02-bento')
    add(A('02-home-rule','Same bento shop back room, Thursday evening, KOH teal hoodie MIWA indigo apron',[
        P('Wide: the used headset still in its worn cardboard box on the shop back-room shelf. KOH carefully picks it up; MIWA sees him from the same counter. Bento boxes remain CLOSED.',('美和','それが|灯里ちゃんの言ってたゲーム？')),
        P('Medium KOH looks at the headset he paid for with saved allowance, bashful ordinary smile. No magical equipment in Japan.',('航','中古なら|小遣いで足りた')),
        P('Small MIWA face then open white space at bottom, mother trusts him without overbearing anger; tail toward her mouth.',('美和','九時には|戻ってね'))
    ],90,'家での時間の約束を、接続前に交わす'),'中古のヘッドセットと、母との九時の約束')
    keep('03-login')
    keep('04-scent',180)
    add(A('04-body','Elselia beginner grassland on the same hill outside Milt; warm daylight, KOH game blue-gray tunic',[
        P('Tight right hand, palm-down into green grass. Fingers individually flex, grass bends under skin. Wrist has blue-gray game sleeve; no headset here.',('音','サワ…')),
        P('Shallow slightly staggered detail: KOH plants ONE brown leather boot into soft soil and shifts his weight. No sword swing.',('音','ザッ')),
        P('Medium seated-to-rising KOH, amused at his own moving hand, feels the breeze. The sword remains sheathed at hip and NO shield.',('航','こんなふうに|歩けるんだ'))
    ],90,'手、足、重心を順に確かめて身体を持つ'),'草と土に触れ、身体を動かす航')
    wing=A('04-wings','Same grassland hill, shadow passing across KOH, the dragon itself remains outside the frame',[
        P('Shallow right-offset eye close-up, KOH notices a broad moving shadow over the grass. Only his eyes and blue-gray shoulder edge, NO dragon NO ring NO skyline.',('音','バサァ…')),
        P('Small low-angle partial close-up: KOH lifts his chin toward an OFFSCREEN sound. His hair and collar move in the displaced breeze. Under this reaction leave a long pure-white fade of about forty percent of the canvas height. Let the same wing sound taper diagonally through the white bottom edge; no new sound, no dragon silhouette, no skyline, no revealing inset.')
    ],100,'姿より先に羽音と影が届き、音だけが下の余白へ続く')
    wing['panels'][1]['sound_continuations']=[{'origin':'04-wings:1','text':'バサァ…','placement':'One continuing inscription begins beside the eye, passes the reaction panel border, decays through the long white bottom gutter, ends before the next panorama'}]
    add(wing,'頭上を横切る影と、余白まで続く一度の羽音')
    keep('05-first-sky',400)
    add(A('05-meeting','Same grassland hill path overlooking Milt; AKARI arrives on foot, KOH game outfit sword sheathed',[
        P('Wide: AKARI in cinnamon-orange jacket and orange hair clip, wooden bow on her back, walks toward KOH from the visible footpath. KOH still looking at sky. She is the same girl from his phone message, no glasses in game.',('灯里','コウ|着いたね')),
        P('Small KOH face turns toward her, recognition and relief, not an anonymous stranger.',('航','灯里？')),
        P('Large airy side view: AKARI points gently toward the huge ring in the already revealed sky while KOH follows her finger; distant landscape open behind their shoulders.',('灯里','あれが|星環だよ'))
    ],220,'日本の友達を認め、初めて見た空の名を聞く'),'同じ道で灯里に会い、星環の名前を知る')
    add(A('05-map','Same hill, looking from KOH to his own translucent beginner map; AKARI beside him, not a teleport screen',[
        P('Over KOH shoulder: a simple soft translucent blue-gray map opened above his wrist, a modest location pin at the nearby riverside town. Exact horizontal display text only エルセリア and ミルト. River and footpath recognizable behind it, no huge technical panels.',('HUD','エルセリア　ミルト'),('灯里（画面外）','ここは|辺境の町ミルト')),
        P('Medium AKARI facing KOH at the same grass path.',('灯里','世界の名前が|エルセリア')),
        P('Shallow KOH looking past map toward the distant mountains with his body turned toward them.',('航','街の外も|歩いて行けるの？'))
    ],80,'世界と町の名前を、今いる場所と結びつける'),'地図でエルセリアとミルトを確かめる')
    add(A('05-road','Same hill and fork in the path, afternoon; iron city rail is discussed as future travel, never physically arriving here',[
        P('Medium AKARI lowers her own wrist menu while talking naturally; the local road and a small riverboat far below are visible, no railway through Milt.',('灯里','船や魔導列車も|あるんだって')),
        P('Wide rear three-quarter: KOH traces the winding physical road toward the town with his eyes, mountains and distant floating islands beyond; he imagines future travel but stands in the same grass. No copied map interface.',('航','あの空まで|行けるかな')),
        P('Medium AKARI walks down the fork toward a visible town training pennant, friendly wave, wooden bow still on her back. KOH remains at fork, going down the OTHER road; continuity not teleport.',('灯里','私は弓の訓練|先に行ってるね'))
    ],100,'先の旅への憧れと、友達自身の予定を両方見せる'),'旅の道を見渡し、灯里は自分の弓の訓練へ向かう')
    add(A('05-weight','Same downhill dirt road toward Milt, KOH alone foreground; two distant ordinary knights pass on horseback, no fight',[
        P('Tight hands and waist: KOH carefully draws his plain straight steel sword a little way out of the brown scabbard, RIGHT hand on hilt, LEFT hand holds scabbard. Metal gives restrained long highlight.',('音','スラ…')),
        P('Medium KOH cautiously holds the fully drawn sword low with BOTH hands like a bamboo sword, tip pointed to empty ground, blade now steel and visibly heavy. No shield, no spell aura, no combat.',('航','……重い')),
        P('Wide small KOH resheathes the sword as mounted knights continue past toward the city gate; he looks at their easy posture. He is not a master swordsman.',('航（心）','俺でも|使えるのかな'))
    ],100,'現実の剣道と、ここで持つ剣の感触の差を確かめる'),'剣の重さと、道を行く騎士の姿')
    keep('06-cart',160)
    keep('07-push')
    add(A('07-introduction','Immediately beside the unstuck cart, same LIZE KOH SENA with muddy forearms; sword sheathed, LIZE shield on back',[
        P('Medium SENA eases off the cart rear and introduces himself with warm eye contact; wooden medicine box secure among cargo.',('セナ','薬師のセナだよ|よろしく')),
        P('Small KOH eye close-up, surprised that a person offers him a name rather than a rewards screen. No HUD here.'),
        P('Medium LIZE wipes a muddy hand on a practical cloth, indicates the loaded cart and the road ahead.',('リゼ','荷物を運ぶのが|私の仕事')),
        P('Two-person low view: LIZE starts walking at the cart side and KOH chooses to accompany them, dirty hands lowered naturally.',('リゼ','町の見回りも|してるよ'))
    ],110,'名前の後に仕事を知り、町へ同行する理由を作る'),'セナの名前と、リゼが担っている仕事')
    water=A('07-water','Walked from cart road to Milt stone bridge, afternoon nearing sunset; water flow healthy, small gold channel underneath',[
        P('Wide establishing: all THREE walk across the same stone bridge with the wooden cart, turquoise river flowing normally below, waterwheel downstream. KOH slows to look over parapet, LIZE waits nearby, SENA beside cart.',('音','サァァァ')),
        P('Shallow right-offset: KOH washes both muddy hands in a small public basin supplied by the same flowing channel, blue-gray sleeves rolled. A few water drops, no dense dots. The SAME running-water inscription continues lightly beside the diagonal gutter; no second complete sound.'),
        P('Medium KOH looking toward the TURNING waterwheel and tiny warm gold supply channel below the bridge; LIZE beside him looks the same direction. Their hands now clean.',('航','水が|光ってる'))
    ],150,'車輪の土を洗い、水の流れを追って町へ入る')
    water['panels'][1]['sound_continuations']=[{'origin':'07-water:1','text':'サァァァ','placement':'one starting サ under the bridge, following ァ letters continue past the basin edge and white angled gutter, end before KOH dialogue'}]
    add(water,'橋を渡り、手を洗い、光を帯びた水路を追う')
    add(A('07-flow','Same stone bridge basin and waterwheel, directly after KOH notices the glowing channel. LIZE beside KOH, SENA and cart offscreen within a few steps',[
        P('Wide over KOH shoulder looking UNDER the same stone bridge: clean turquoise water flows beside a slender warm-gold channel with brass guide rings fixed by local craftspeople. No hidden giant mechanism, no valve boss, no drain or drought. LIZE points down from parapet at the flow itself, not at a HUD.',('リゼ','魔力も|この水路を通るの')),
        P('Medium KOH follows the visible branching little supply channel from bridge to waterwheel and adjoining repair stall, begins to understand a connected town. Same clean hands, muddy blue-gray tunic from cart, steel sword sheathed and no shield.',('航','街全体を|つないでるんだ'))
    ],70,'光る水への疑問に答え、橋と町の設備を一続きに見る'),'町へ魔力を運ぶ水路の働き')
    add(A('07-device','Immediately by bridge-side repair stall, Milt; same trio and parked cart, one small insulated wooden medicine cooling box',[
        P('Close: SENA opens ONE cooling box on the cart, a brass rune strip glows gently around its hinge, cold vapor barely visible, same tied small medicine vials inside. His hand points to the brass fitting, no high-tech computer.',('セナ','薬を冷やす|魔導器だよ')),
        P('Medium LIZE taps the carved brass rune with one finger, KOH listens from the opposite side of cart, no invented energy meter.',('リゼ','魔法の形を|道具に刻むの')),
        P('Shallow KOH eyes and open relaxed hand, interested practical realization rather than genius revelation.',('航','魔法が苦手でも|使えるんだ'))
    ],80,'生活の道具から、魔法と技術の違いを理解する'),'薬を冷やす魔導器の働き')
    add(A('07-spirit','Milt bridge-side waterwheel steps, close to repair stall; same KOH LIZE parked cart and SENA offscreen nearby. One small wind spirit and local adult female mill-worker in beige shirt brown apron',[
        P('Wide at waterwheel: mill-worker opens a windcloth vane and asks a tiny pale teal wind spirit hovering just above it. The spirit has a light airy face-like form and its own direction, not a robot or HUD.',('水車の職人','風向きを|変えてくれる？')),
        P('Small KOH reaction as the spirit FIRST darts off toward a bright flower by river rather than obeying; connected swooping airy trace and tiny rustle, no teleport.',('航','言うこと|聞かないんだ'),('音','ひゅっ')),
        P('Medium mill-worker laughs gently and waits with an open hand. The wind spirit pauses at the flower then looks back; same waterwheel behind, no automatic obedience.',('水車の職人','この子にも|都合があるから'))
    ],130,'精霊にも意志があり、暮らしの人が待つことを知る'),'水車の職人と、自分の都合で動く風の精霊')
    add(A('07-practice','Same bridge-side waterwheel steps; KOH and LIZE on stone walkway, wind spirit near worker in background',[
        P('Close LIZE open RIGHT palm, a little controlled breeze curls a narrow cloth strip held in LEFT hand. Small precise magic rather than giant combat glow; clean hands after washing.',('音','フワ…')),
        P('Small offset KOH copies the gesture with RIGHT palm but the cloth strip he holds in LEFT hand hangs limp. Same clothes, sword sheathed, no shield, no cheat power. His expression mildly embarrassed.',('航','……出ない')),
        P('Large LIZE reassuring without teasing, her hands lower as the small wind stops, teaches a basic fact rather than a full lesson.',('リゼ','形を覚えて|何度も練習するの'))
    ],80,'魔導器を使うことと、本人が魔法を習うことを分ける'),'小さな風の魔法と、航の最初の失敗')
    add(A('07-town','Milt outer market at the end of the SAME bridge, early sunset, after the waterwheel stop',[
        P('ONE borderless tall panorama descending from vast warm ring-lit sky to Milt crenellated stone wall and rooflines, then market canopies, lantern-worker lighting one small warm magical lamp, resting patrol knights and porters, thin riverboat mast. KOH LIZE and SENA with the cart are three small continuous figures entering in lower foreground. Healthy turquoise water and pale gold channel remain under bridge. White fade at top and bottom; no words, no HUD, no tiled reaction panels. Lived-in human-scale detail, no giant rail station, no ominous drought.')
    ],360,'仕事の接写から引き、生活が広がる町に滞在する'),'橋の向こうに広がるミルトの夕方')
    keep('08-medicine',230)
    add(A('08-choice','Same bridge market edge immediately after SENA asks about tonight medicine. KOH LIZE SENA and ONE tied parcel',[
        P('Medium KOH accepts the ONE tied parcel, eager to be useful, gentle optimistic overpromise.',('航','俺も|できると思う')),
        P('Shallow KOH wrist menu in his point of view: only a quiet reminder, exact horizontal text 日本時間 20:50. KOH looks past it toward parcel in his OTHER hand. No offscreen mother voice in Elselia.',('HUD','日本時間 20:50'),('航','ごめん|今日は帰らないと')),
        P('Large two-person view: LIZE takes that SAME parcel from KOH, explicit single handoff, not duplicated. Her smile remains practical and kind; SENA in background turns toward clinic with cart.',('リゼ','私が届ける|明日は来られる？'))
    ],190,'引き受けたい気持ちと、日本の時間を同時に自覚する'),'九時の約束を思い出し、薬をリゼに託す')
    add(A('09-safe','Milt safe arrival plaza adjoining bridge, twilight. KOH and LIZE walk a short distance from market, tied parcel now LIZE hand, SENA offscreen heading clinic',[
        P('Wide establishing: low sheltered plaza surrounded by stone benches, familiar town gate and bridge entrance visible, people leaving equipment at a staffed wooden desk. LIZE shows KOH the place; no teleport effect or imprisonment.',('リゼ','帰るなら|ここでね')),
        P('Medium KOH beside bench, one hand opens his own wrist display. Exact simple horizontal UI 安全拠点 ミルト and ログアウト. Sword still sheathed, hands empty of medicine. To LIZE he makes a specific return promise.',('HUD','安全拠点 ミルト　ログアウト'),('航','明日|日暮れ前に来る')),
        P('Small LIZE face, softly answers while holding the ONE parcel ready to go. Under her answer leave a generous white fade, no next day scene yet.',('リゼ','じゃあ|また明日'))
    ],250,'帰る場所と再訪の約束を、相手と一緒に決める'),'安全な広場で、明日また会う約束をする')
    add(A('10-japan','Japan same modest bedroom and desk as connection, Thursday 21:00, KOH real-world teal hoodie white tee, headset removed',[
        P('Shallow close-up: KOH lifts the headset from his eyes with BOTH hands, back in teal hoodie, desk lamp and school bag from login. Quiet end to fantasy environmental sounds, no objects carried from Elselia.',('音','カチ')),
        P('Medium KOH turns toward open bedroom door, MIWA offscreen downstairs. A small wall clock reads 21:00 if legible, no floating HUD. KOH relief and lingering wonder.',('美和（画面外）','おかえり'),('航','ただいま')),
        P('ONE large borderless final quiet close view: KOH clean REAL hands resting beside the headset, reflection of his slightly smiling eyes in the dark desk window. They carry no dirt, sword, parcel, magic or fantasy ring. Broad unoccupied ivory at bottom after the thought, no montage or next episode.',('航（心）','名前を|呼ばれた'))
    ],500,'環境音を終え、日本の静けさで呼ばれた名前を受け止める'),'日本へ戻り、今日呼ばれた名前を思う')
    ep['assets']=assets
    return ep

def episode_two():
    ep=copy.deepcopy(json.loads((ROOT/'episode-02/episode.json').read_text()))
    ids=['01-return','02-night-work','03-delivery','04-bread','05-wind','06-work','07-announcement']
    old={a['id']:a for a in ep['assets'] if a['id'] in ids}
    ep.update(start='金曜の放課後。航は昨日の再訪の約束を守り、正常な水路のミルトへ戻る。',
              end='薬の配達と粉袋の返却を通じ、住民の暮らしと町の道を覚える。初めて運び賃を受け取りパンを買う。リゼの巡回を見送り、討伐隊募集に心が動く。',
              revision_intent='町を背景にせず、道を教わる、迷う、音を聞く、届ける、働いた対価を使う体験で覚える。第1話で薬を明示的に託したため謝罪ではなく感謝でつなぐ。魔導器を知ったことは反復せず、正常な水と仕事のつながりを深める。')
    assets=[]
    def keep(key,gap=None):
        a=old[key]
        if gap is not None: a['gap_before_390']=gap
        a['alt']=a['alt'].split('。',1)[0]+'。'+' / '.join(' '.join(f"{d['speaker']}「{d['text']}」" for d in panel['lines']) for panel in a['panels'] if panel['lines'])
        assets.append(a)
    def add(asset,alt,extra=()):
        a=finish(ep,asset,alt)
        a['references'].extend(str(ROOT/x) for x in extra)
        if len(a['panels'])==2:
            a['prompt']+='\nTwo meaningful moments in an airy natural approximately 1024x1536 canvas, no third panel or montage.'
        for i,x in enumerate(extra,3):
            a['prompt']+=f'\nInput {i} is the immediate visual continuity reference for '+x+'. Preserve its specified people, clothing, props and local architecture, without copying its panels or text.'
        assets.append(a)
        return a
    add(A('00-school','Japan high school gate after classes on Friday, KOH navy school blazer with bag; AKARI school navy outfit, rectangular glasses and orange geometric hair clip',[
        P('Medium natural two-shot at school gate: AKARI turns toward KOH while other students walk toward town, no headset or fantasy outfit.',('灯里','今日も|行く？')),
        P('Small KOH face looking toward her, quiet but definite, no anonymous thought floating over town.',('航','また行くって|約束した')),
        P('Wide AKARI and KOH continue along the Japanese street, AKARI gestures to herself with familiar friendliness; no game HUD or magic.',('灯里','私は弓の訓練|続きやろうっと'))
    ],50,'日本の友達も自分の予定を持ち、航は再訪を選ぶ'),'下校時に灯里と、今日も接続すると話す',('episode-01/art/01-school-final.png',))
    keep('01-return',100)
    add(A('02-night-work',old['02-night-work']['location'],[
        P('KOH at the same Milt clinic porch with medicine shelves, hands empty and clean, thanks LIZE for their explicit medicine handoff yesterday. He has not lost or abandoned a parcel.',('航','昨日の薬|届けてくれてありがとう')),
        P('LIZE normal practical smile, yesterday work completed while KOH was away. She is not standing at his command.',('リゼ','夜には|間に合ったよ')),
        P('SENA at his clinic porch wooden counter wraps one NEW flat rectangular medicine parcel about 24cm across in pale brown paper with brown string. Same parcel will be delivered to EDA. One clear wrapping action, no clone parcels in KOH hands.',('セナ','今日はこれを|頼める？'))
    ],100,'昨日の引き渡しに感謝し、今日の仕事を引き受ける'),'リゼが薬を届けたことを知り、セナから今日の包みを受け取る',('episode-02/art/02-night-work.png','episode-02/art/03-delivery.png'))
    add(A('02-route-note','Same clinic porch work counter beside medicine shelves, SENA and a small folded paper street map, KOH holds ONE new 24cm medicine parcel, LIZE beside him',[
        P('Close SENA points on a small hand-drawn PAPER map showing the same bridge, a fork, a waterwheel and a little blue door mark. No printed names or HUD. KOH left arm holds the paper parcel against waist, right hand ready to take map.',('セナ','青い扉の|エダさんだよ')),
        P('Medium KOH follows SENA finger with his eyes, then looks at the visible stone bridge in the real surroundings. Package remains at waist.',('航','この橋を|渡るんだね')),
        P('Wide LIZE starts along the road with KOH following carrying the one parcel and folded map. SENA remains at his clinic porch counter to put away medicines, not teleporting with them.',('リゼ','帰りの道も|覚えておこう'))
    ],70,'地図の記号をその場の橋と結びつけ、仕事の相手を知る'),'セナからエダの家への道を教わる',('episode-02/art/03-delivery.png',))
    walk=add(A('02-walk','Milt stone lane leading from clinic past bridge toward EDA blue-door house, clear afternoon, same parcel and folded paper map',[
        P('Low shallow walking detail: KOH brown boots and LIZE brown boots continue down stone steps, parcel seen only partly at upper edge. One soft vertical コツコツ begins beside his first step and continues diagonally past the gutter with the same cadence, not a second complete inscription.',('音','コツコツ')),
        P('Airy wide lane opening: KOH and LIZE small beneath an arch, blue wooden door visible ahead among warm red-tile houses, bakery hanging pretzel sign farther along. The SAME footstep sound tapers toward white bottom; no new starting コツ or bonus conversation.')
    ],130,'教わった道を自分の足で歩き、足音を街の間へ続ける'),'橋から青い扉の家まで歩く',('episode-02/art/03-delivery.png',))
    walk['panels'][1]['sound_continuations']=[{'origin':'02-walk:1','text':'コツコツ','placement':'a single shared cadence begins by the steps and its later ツ letters taper past the arch into white, no second inscription'}]
    add(A('03-delivery','EDA blue wooden front door beside the same Milt stone lane; EDA elderly silver low-tied hair, ivory collar blouse and faded brown-plum shawl with gold trim, exactly as original delivery reference',[
        P('Medium KOH at the blue wooden door, LIZE waiting one step behind to the side. EDA opens door toward him. KOH holds the ONE 24cm flat paper parcel at waist and introduces himself before she uses his name.',('航','コウです|薬を届けに来ました')),
        P('Close hands: KOH passes that one parcel into EDA hands, unambiguous shared transfer. Her warm face beside the blue door, no duplicate parcel.',('エダ','ありがとう|コウ')),
        P('Quiet shallow interior view from doorway: the delivered paper parcel now rests on a small wooden table beside EDA ordinary cup, folded shawl and small hand-painted family portrait in a plain frame. She sets it down carefully; no immediate cure, no quest reward pop-up. KOH no longer carries medicine, both hands free.')
    ],90,'配達を一回の報酬画面で終えず、受け取った人の生活へ置く'),'青い扉のエダへ薬を手渡す',('episode-02/art/03-delivery.png',))
    add(A('03-household','Same open blue doorway, package inside on table, KOH hands empty, LIZE at roadside, EDA the same elderly woman in brown-plum shawl',[
        P('Medium EDA by open door with a small flower pot and two ordinary cups visible inside. She speaks to KOH, tired but pleased, no physical transformation.',('エダ','明日は|孫が来るの')),
        P('Medium KOH gently glances from the flowers to EDA, ordinary warm response; LIZE listens rather than explaining what an NPC is.',('航','楽しみですね'))
    ],80,'薬を受け取る相手にも明日の予定がある'),'エダの明日の予定を聞く',('episode-02/art/03-delivery.png',))
    add(A('03-bakery','Bakery farther along the same lane with pretzel sign, flour shelves and oven, baker same chestnut hair short beard ivory cloth cap white shirt brown leather apron; KOH and LIZE arrive empty-handed',[
        P('Medium baker looks up from bread shelf as KOH arrives at the counter, recognizes him rather than summoning him. Golden round bread on shelf.',('パン屋','昨日荷車を|押してくれたろ')),
        P('Shallow KOH surprise, he looks at stacked flour sacks beside oven, connects the muddy cart with bread.',('航','あれ|パン屋の荷物？')),
        P('Close baker offers ONE warm golden round bread roll on small oatmeal cloth into KOH ready hands, white fluffy break in crust and gentle steam. This is a gift for cart help, no coins yet.',('パン屋','粉が無事で|助かったよ'))
    ],120,'昨日の小さな手伝いが今日のパンにつながる'),'パン屋で荷車の粉と今日のパンのつながりを知る',('episode-02/art/03-delivery.png','episode-02/art/04-bread.png'))
    keep('04-bread',140)
    add(A('04-bread-talk','Bakery outside bench immediately after KOH eats the gifted round bread; he finishes the last piece, folds the small EMPTY oatmeal wrapper; LIZE same moss green courier outfit',[
        P('Medium LIZE naturally asks KOH sitting across a small bench table, no bread cloning; his last crumbs and wrapper remain on his side.',('リゼ','向こうでは|何してるの？')),
        P('Shallow KOH with relaxed smile, folds his empty cloth wrapper beside the table, hands clearly shown.',('航','学校と|家の弁当屋')),
        P('LIZE warm practical response, courier belt visible, not flirt pose. KOH listens and starts to feel useful.',('リゼ','荷運び|慣れてるんだね'))
    ],110,'食べ終わる間に日本の仕事と現地の仕事を結びつける'),'パンを食べながら家の弁当店を話す',('episode-02/art/04-bread.png',))
    add(A('04-errand','Back at same bakery counter, KOH has finished bread and stored empty cloth, ONE EMPTY soft folded flour sack on counter, no medicine package or bread in his hands',[
        P('Medium baker lifts a single visibly flat EMPTY beige flour sack with tied folded edge from counter toward KOH, no cargo box.',('パン屋','空の袋を|水車小屋へ頼める？')),
        P('Small KOH nodding, takes the one light empty sack with BOTH hands, clearly relieved to recognize the landmark.',('航','さっきの道だね')),
        P('Wide LIZE walks beside KOH away from bakery but half a step behind, he carries the folded empty sack under left arm and folded paper map in right.',('リゼ','今度はコウが|案内して'))
    ],80,'地図を覚えることに使い道を作る'),'空の粉袋を水車小屋へ返す仕事を引き受ける',('episode-02/art/03-delivery.png',))
    wrong=add(A('04-wrong-turn','Milt branching stone lane, KOH carrying ONE flat empty flour sack left arm and the same paper route map right hand; LIZE half a step behind; waterwheel remains offscreen',[
        P('Medium KOH turns toward the WRONG narrow side lane while comparing folded map and street. Ahead is an ordinary closed garden fence, no monster, no ring reveal, no waterwheel visible.',('航','ここを|曲がって……')),
        P('Shallow LIZE beside him calmly tilts her head toward the unseen river, a question that helps him rather than mocking.',('リゼ','水の音|聞こえる？')),
        P('Small KOH stops, lowers the paper map and turns his eyes toward offscreen sound. A single quiet flowing-water サァァ… starts near the right white side and extends toward the open lower gap. NO source wheel visible yet.',('音','サァァ…'))
    ],90,'道に迷う小さな失敗から、町の音を手掛かりにする'),'道を迷い、水の音に耳を澄ます')
    add(A('04-wheel','Return to the SAME healthy-flowing bridge-side waterwheel from episode one, reached on foot from lane; KOH and LIZE small near lower doorway, KOH holds one folded empty flour sack',[
        P('ONE large borderless airy view: clean turquoise water descends past dark wooden wheel, brass guide fittings and slender warm gold mana channel drive an old stone mill. Flour workers and one small independent wind spirit belong in the scene. The SAME distant サァァ… has already begun in previous asset: continue only its trailing ァ… lightly beside water and white edge, never write a second サ or second complete sound. No drought, valve boss or display.')
    ],700,'聞いた音の場所へ辿り着き、水と魔導技術の仕事を広く見る'),'水の音をたどり、水車小屋へ戻る',('episode-01/art/07-water-final.png','episode-01/art/07-spirit.png'))
    add(A('04-mill','Same waterwheel doorway, local adult female worker same chestnut ponytail ivory rolled-sleeve shirt dark brown long apron as episode1 wind-spirit scene; ONE empty flour sack from KOH',[
        P('Medium worker takes the one flat empty sack from KOH hands at doorway, LIZE beside him. The original medicine and bread are absent.',('水車の職人','ありがと|明日も使うから')),
        P('Quiet wide interior view behind worker: wheel shaft and modest brass engraved fitting rotate a stone grinding mill; regular sacks of grain and flour, soft clean drifting flour dust, no modern robot factory. KOH and LIZE look from doorway, not operating equipment.'),
        P('Close worker offers TWO small copper coins on open palm toward KOH, same apron cuff and clear fingers. Plain copper color, no exact engraved denomination, no unlimited pile.',('水車の職人','袋の|運び賃'))
    ],150,'持ち物を返した結果と、誰かの仕事の対価を見せる'),'粉袋を返し、銅貨二枚の運び賃を受け取る',('episode-01/art/07-spirit.png',))
    add(A('04-wage','Outside same mill doorway after handoff, KOH holds EXACTLY TWO plain copper coins, no flour sack; LIZE beside him, worker returned to her work in background',[
        P('Shallow KOH looks at two copper coins on his open palm in wonder, no level-up or game notification.',('航','運び賃……？')),
        P('Medium LIZE looks at his palm then his face, straightforward smile, modest normal wages rather than a grand reward.',('リゼ','働いたぶんだよ'))
    ],70,'手元の小さな対価に驚き、仕事の意味を受け取る'),'初めての運び賃を確かめる')
    add(A('04-buy','Same bakery reached by the now familiar lane, KOH and LIZE return on foot; same baker cloth cap white shirt brown apron; exactly TWO copper coins buy ONE small round bread roll',[
        P('Close KOH places his TWO copper coins on bakery counter, baker offers ONE smaller golden bread roll wrapped in oatmeal cloth. No other coins in KOH hand.',('航','小さいの|一つください')),
        P('Medium KOH now empty of coins offers that ONE purchased bread roll to LIZE across bakery threshold, slightly shy warm smile.',('航','リゼの分')),
        P('Shallow LIZE accepts the one bread with BOTH hands, surprised gentle smile. KOH hands empty, no second bread or currency.',('リゼ','ありがとう'))
    ],120,'覚えた道と自分の運び賃を、相手への小さな返礼に使う'),'運び賃でリゼのパンを買う',('episode-02/art/03-delivery.png','episode-02/art/04-bread.png'))
    add(A('05-wind',old['05-wind']['location'],[
        P('ONE large borderless vertical scene exactly continuing the old windmill illustration: normal flowing water, turning windmill, small independent wind spirits and cloth flags. KOH and LIZE small but dialogue stays a readable modest vertical balloon. No parcel or flour sack. LIZE has finished her small bread; no duplicated leftover.',('航','この道は|覚えた'))
    ],260,'町の道を覚えた実感を、穏やかな風景へ置く'),'風と水の道を覚え、町を見渡す',('episode-02/art/05-wind.png',))
    keep('06-work',100)
    add(A('06-town-evening','Same Milt river street toward safe square, LIZE has gone to patrol and does NOT return; KOH alone with folded paper map, sword sheathed, no shield or parcel; local workers close shops at dusk',[
        P('Shallow local lamplighter touches one modest brass-rune street lamp, warm light quietly appears above stone lane. KOH glances toward the light while walking, no spell cast by him.',('音','ポッ')),
        P('ONE large quiet borderless view: river-side Milt under dusk with normal clear water, workers folding stalls, children walking home, warm lit windows. Small KOH pauses to fold the route map into his belt pouch, learning where he is rather than waiting for LIZE. Broad white breathing room below; no mission or giant enemy yet.')
    ],280,'巡回へ行った相手を待たず、続いている町を一人で見る'),'灯りがともる町で道の略図をしまう')
    keep('07-announcement',310)
    assets[-1]['location']='KOH POV at Milt market at dusk, immediately after the town lamps are lit; only HUD overlays for him'
    ep['assets']=assets
    return ep

def write(ep, scroll_notes=None, art_notes=None):
    directory=ROOT/f"episode-{ep['number']:02d}"
    adoption_path=directory/'adoption.json'
    adoption=json.loads(adoption_path.read_text()) if adoption_path.exists() else {}
    for asset in ep['assets']:
        original=asset['id']+'.png'
        if asset['id'] not in adoption and (directory/'art'/original).is_file():
            adoption[asset['id']]=original
    adoption_path.write_text(json.dumps(adoption,ensure_ascii=False,indent=2)+'\n')
    (directory/'episode.json').write_text(json.dumps(ep,ensure_ascii=False,indent=2)+'\n')
    episodes=json.loads((ROOT/'production/episodes.json').read_text())
    episodes=[ep if row['number']==ep['number'] else row for row in episodes]
    (ROOT/'production/episodes.json').write_text(json.dumps(episodes,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'production/assets.json').write_text(json.dumps([a for row in episodes for a in row['assets']],ensure_ascii=False,indent=2)+'\n')
    lines=[f"# 第{ep['number']}話 {ep['title']} — 脚本と縦の絵コンテ",'',
           f"開始：{ep['start']}",f"終了：{ep['end']}",f"伏せる：{ep['hold']}",'',ep['revision_intent'],'',
           scroll_notes or ('第1話：羽音は姿より先に枠と人物のない余白へ通す。水音は橋から手洗いへ一続きにし、帰宅の静けさより前に終える。' if ep['number']==1 else '第2話：足音を歩行から街の間へ続け、水音は場所が見える前に始める。届いた薬と明日の予定、粉とパン、仕事と対価を別の瞬間で描く。'),'',
           '参照した演出：context-and-dialogue、cross-panel-soundsの390/360比較と連続3窓、scroll-pacing、whitespace-example。通常会話の字は画面幅比で保ち、場面の位置と持ち物を継ぐ。','',
           (art_notes or ('既存8素材の採用原画を保持。' if ep['number']==1 else '既存の採用原画を活かし、02-night-work・03-delivery・05-windは話のつながりに合わせて編集。07-announcementは直前の町と同じ夕暮れへ揃える。'))+'追加素材は下記の独立した瞬間を描く。縦列は右から左、横並びの接写も右から左。上下のショットは別の瞬間。余白は生成内とHTML外の合計をスマホ実表示で確認する。','']
    for a in ep['assets']:
        lines.extend([f"## {a['id']}",f"場所：{a['location']}",f"直前の間：390幅で{a['gap_before_390']}px。役割：{a['pacing_purpose']}",''])
        for i,p in enumerate(a['panels'],1):
            lines.append(f"{i}. {p['scene']}")
            for d in p['lines']:lines.append(f"   {d['speaker']}：{d['text']}（縦列：{' / '.join(d['columns'])}）")
            for s in p.get('sound_continuations',[]):lines.append(f"   継続音：{s['origin']}からの同じ{s['text']}。{s['placement']}")
        lines.append('')
    (directory/'storyboard.md').write_text('\n'.join(lines).rstrip()+'\n')
    print(f"Episode {ep['number']}: {len(ep['assets'])} artwork units, {sum(len(a['panels']) for a in ep['assets'])} story moments")

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--episode',type=int,choices=(1,2),default=1)
    args=parser.parse_args()
    write(episode_one() if args.episode==1 else episode_two())
