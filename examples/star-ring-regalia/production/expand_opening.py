#!/usr/bin/env python3
"""Revise the opening through embodied encounters, preserving executed artwork."""
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

def write(ep):
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
           '参照した演出：context-and-dialogueの大小8コマ、cross-panel-soundsの390/360比較と連続3窓、scroll-pacing、whitespace-example。名前→反応→仕事を分け、羽音は姿より先に枠と人物のない余白へ通す。水音は橋から手洗いへ一続きにし、帰宅の静けさより前に終える。通常会話の字は画面幅比で保ち、場面の位置と持ち物を継ぐ。','',
           '生成済みの既存8素材は採用原画を保持。追加素材は下記の独立した瞬間を描く。縦列は右から左、横並びの接写も右から左。上下のショットは別の瞬間。余白は生成内とHTML外の合計をスマホ実表示で確認する。','']
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
    write(episode_one())
