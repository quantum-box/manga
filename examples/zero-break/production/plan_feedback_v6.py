"""Editable panel direction for the Zero Break context/dialogue revision."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
STATE=ROOT/'production/feedback-v6'

COMMON='''Use case: illustration-story.
Asset: finished full-color Japanese smartphone Webtoon strip with integrated raster speech balloons. Preferred canvas 1024x3072 (width:height 1:3).
Recompose the existing episode into the exact sequential panels below. Input images establish identity, costume, props and anime rendering ONLY. Do not reproduce their dense multi-speaker layout or later events. Several sequential appearances of the same person are allowed only in separate explicitly ordered panels.
Match the polished expressive anime/cel-shaded Zero Break art. Ren19: black tousled hair, blue eyes, crimson scarf, soft BLACK short-sleeve shirt, charcoal trousers, narrow brown straps, BARE hands until explicitly transformed. Basic armor only when specified: BLACK faceted plates, CYAN seams and cyan star, face uncovered, red scarf. Mira19: blonde long braid, blue eyes, white/royalBLUE/GOLD detailed dress, blue-gold flower hair ornament; no armor. Rook22: SILVER short hair, blue eyes, SILVER armor, royalBLUE cape, BLACK gloves. Noa18: ORANGE tousled hair, green eyes, brass round goggles on head, blue overalls, black undershirt, orange gloves. Draw only the people requested for each panel. People offscreen stay nearby.
Printed bold Japanese manga gothic: UPRIGHT glyphs TOP TO BOTTOM, columns RIGHT TO LEFT. Render only verbatim dialogue supplied for that panel, with no quotation marks, labels or extra captions. Aim for actual glyph height 65-76px on a1024px-wide strip (23-27px at360px). Do not shrink lettering to fit. Keep ample white inset, faces and hands visible. Speech tails point continuously to the speaking MOUTH; thoughts use cloud outlines and DOTS to head. Balloon contour follows THIS voice: ordinary thin-black oval; Mira's composed voice thin blue-grey rounded capsule; warm voice soft organic outline; breathless voice slightly wavering contour; urgent shouted warnings heavy jagged outer contour. No shouting decorations on a calm utterance, no thought dots on spoken words.
Top-to-bottom reading on a WHITE canvas. Right-aligned82% means a visible WHITE blank margin of18% at LEFT of that panel, not merely put the face on the right inside a full-width picture. Left-aligned68% means32% of the canvas at RIGHT is completely WHITE. Draw complete thin black rectangular frames INSIDE the canvas at the requested unequal widths. Leave30-60px WHITE gutters between frames. UNEQUAL panel heights and widths, occasional shallow inserts and borderless emotional or geographic full-width panels. Real re-composed close-ups in the smaller panels, never squeeze down a whole crowd scene. No equal-size stack, decorative collage, English, watermark, panel numbers or advance reveal. Maintain cause, posture, handedness, props and actual time/location through the strip. The next episode's incident must not appear.
'''

def p(beat,view,frame,speaker=None,text=None,voice='無言'):
    item={'beat':beat,'view':view,'frame':frame,'voice':voice}
    if text:
        item['line']={'speaker':speaker,'text':text,'type':'thought' if 'thought' in speaker else 'speech'}
    return item

jobs=[]
def add(n,key,replaces,panels,pause=85,context_override=None):
    d=ROOT/('v5' if n==1 else f'episode-{n:02d}')
    baseline=json.loads((STATE/'baseline'/f'episode-{n:02d}.json').read_text())
    selected=[s for s in baseline['shots'] if s['id'] in replaces]
    references=[str((d/'art'/(s['file']+('.png' if n==1 else ''))).relative_to(REPO)) for s in selected]
    references=references[:3]+['skills/webtoon/references/zero-break/varied-01.png']
    context=context_override or ' '.join(s['scene'] for s in selected)
    prompt=COMMON+'\nThe LAST input image is ONLY the adopted example of unequal FRAME WIDTHS, white negative space, and shallow eye inserts. Do not copy Mira or her rescue dialogue from it. Earlier images establish THIS scene.\nExact continuity/setting (not a request to put everything in every panel): '+context+'\n\n'
    for i,panel in enumerate(panels,1):
        prompt+=f'Panel {i}, downward order. Frame: {panel["frame"]}. Reader understands: {panel["beat"]}. Visible camera subject / offscreen continuity: {panel["view"]}. Voice / balloon: {panel["voice"]}.\n'
        if panel.get('line'):
            prompt+=f'ONLY speaker: {panel["line"]["speaker"]}. EXACT text: 「{panel["line"]["text"]}」 (render contents only).\n'
        else: prompt+='SILENT: no balloons or text unless an exact prop inscription is explicitly specified.\n'
    jobs.append({'id':f'e{n:02d}-{key}','episode':n,'file':f'v6-{key}.png','replaces':replaces,'context':context,'panels':panels,'references':references,'prompt':prompt,'pause':pause})

add(1,'waking',['waking'],[
 p('Ren opens his eyes in an unfamiliar place.','ONLY seated Ren face, eyes opening; white stair and a blue banner establish the same landing.','right-aligned 80% width, medium-height framed close-up','Ren thought','……ここ、どこだ。','bewildered thought, cloud and dots'),
 p('The place really floats in the sky.','His upward eyeline leads to floating white towers and islands; only location box EXACT 空都リュミエル, no other words.','large full-width BORDERLESS vertical upward view, enough height to understand geography'),
 p('He links this place to his last memory, without knowing why.','ONLY Ren seated shoulders/face, one bare hand touching his crimson scarf; same intact stairs. No corpse or child flashback.','left-aligned90% width, medium-height framed face','Ren thought','俺、事故に遭ったはずじゃ……。','uncertain thought, cloud with dots')],130)

add(1,'greeting',['greeting'],[
 p('The approaching knight addresses seated Ren.','ONLY Rook face bent slightly down; Ren remains seated offscreen left. Same white stone stairs.','right-aligned82% width, medium framed close','Rook','立てるか？','reserved ordinary thin-black oval'),
 p('Help is offered, not yet accepted.','Rook black-gloved open hand extended toward Ren bare hand. No crystal, no contact yet.','left-aligned66% width, shallow hand insert'),
 p('Ren answers while still getting his bearings.','ONLY Ren seated face looking up right, same scarf and shirt.','left-aligned90% width, medium close-up','Ren','ああ……。','quiet shaky spoken voice, continuous tail'),
 p('He asks his first question.','Ren bare hand takes Rook gloved hand and Ren rises a little; tight upper-body shot, not an unexplained new location.','full-width tall framed movement','Ren','ここは？','ordinary questioning oval')],90)

add(1,'orientation',['orientation','registration'],[
 p('Rook gives one fact about this country.','ONLY standing Rook face and pointing glove; Ren now stands beside him offscreen left.','right-aligned86% width, medium framed','Rook','ここは、空に浮かぶ国だ。','matter-of-fact rounded speech'),
 p('Ren really looks at the impossible landscape.','White towers suspended beyond intact landing; lower corner shows only red scarf and Ren eye following them.','full-width wide borderless geographic view','Ren','空に……？','quiet astonished speech, soft outline'),
 p('The knight notices unfamiliar clothes.','Rook gloved finger gestures toward Ren black FABRIC sleeve/red scarf; no grabbing.','left-aligned78% width, shallow detail','Rook','見慣れない服だな。','ordinary thin oval'),
 p('A new word is introduced separately.','ONLY Rook close face, calm guarded eyes; Ren remains offscreen left.','right-aligned83% width, medium framed','Rook','転生者か。','composed speech'),
 p('Ren has to process that word.','ONLY Ren face with widened blue eyes; scarf visible, SAME landing. No crystal or armor.','full-width large close-up','Ren','……転生？俺が？','hesitant spoken voice, mildly wavering outline')],130)

add(1,'instruction',['walk_to_station','instruction'],[
 p('Rook names the procedure before walking.','ONLY Rook shoulders and pointing hand; same landing, Ren offscreen left.','right-aligned90% width, medium framed','Rook','異世界から来た者は、まず魔力を測る。','calm explanatory rounded capsule'),
 p('Ren follows him physically.','One Rook half a pace ahead and one Ren walk toward distant SAME black crystal on SILVER gothic pedestal across intact plaza.','full-width broad geography and walking shot','Rook','こっちだ。','ordinary oval'),
 p('Ren reaches the apparatus but has not touched it.','Close BLACK crystal and Rook BLACK glove pointing at its top. Ren BARE hand lowered at edge. Readout blank.','left-aligned86% width, medium prop close-up','Rook','水晶に手を置け。','ordinary instruction'),
 p('The purpose of touching is explained.','ONLY Ren listening face; black crystal edge at bottom, bare hand still lowered. Rook stays offscreen right.','right-aligned92% width, medium-height framed reaction','Rook offscreen','使える魔力の量がわかる。','calm offscreen speech, tail exits toward Rook on right, no dots')],100)

add(1,'waiting',['waiting'],[
 p('Ren keeps his palm on the crystal and checks the procedure.','ONLY Ren face with same BARE RIGHT palm visible below on BLACK crystal. NO results or glowing power.','left-aligned92% width, medium framed','Ren','……これで、いいのか？','uncertain ordinary speech'),
 p('The knight tells him to wait.','ONLY Rook close face watching blank narrow metal inset readout; Ren offscreen left.','right-aligned80% width, medium framed','Rook','そのまま、待て。','controlled ordinary oval'),
 p('A short real wait before the readout.','BARE palm resting still on BLACK crystal; empty readout partly visible, no0.','left-aligned68% width, shallow silent hand insert')],170)

add(1,'confirmation',['confirmation'],[
 p('Rook reads the disappointing result.','ONLY Rook face looking down left, disappointed but quiet, Ren offscreen left. No new display.','right-aligned84% width, medium framed','Rook','魔力、ゼロ。','cool ordinary thin oval'),
 p('Ren hears before he answers.','ONLY Ren blue eyes, widening; BARE RIGHT hand still on crystal outside crop.','left-aligned69% width, very shallow eye insert'),
 p('The word finally reaches him.','ONLY Ren face, red scarf, palm STILL touches crystal at bottom; same station.','full-width large framed face','Ren','……ゼロ？','small uncertain SPOKEN wavy speech tail, not thought dots')],145)

add(1,'danger',['giant'],[
 p('The vibration comes from a runaway guardian.','Distant warning guard shouting from lower plaza, looking up; Ren offscreen near measuring station.','right-aligned86% width, medium framed warning','warning guard A','警備巨兵が暴走した！','urgent SHOUT, bold jagged outer edge'),
 p('Show the full dangerous spatial relationship BEFORE anybody falls.','Large continuous view: SAME black stone guardian violet diamond chest core beside HIGH stone bridge, Mira on bridge, Ren much LOWER balcony, canvas cargo awning BELOW Ren. Violet cracks only on guardian. Bridge beginning to crack, Mira still on bridge.','full-width LARGE tall borderless geographic view'),
 p('The rescue target is identified.','SECOND warning guard face only, pointing up beyond top; Mira is NOT falling in this strip yet.','left-aligned90% width, medium framed shout','warning guard B','姫様が、橋にいる！','urgent bold jagged shout')],100)

add(1,'approach',['approach'],[
 p('Ren stands up after the quiet rescue conversation; the same guardian approaches.','Ren rising from kneeling on solid lower cargo plaza, Mira standing safely right; torn canvas/rope gives same-location marker. SAME black guardian with VIOLET DIAMOND core is clearly visible approaching in distant upper-right background on the SOLID lower plaza, not the high bridge. No new crest or power.','full-width medium framed shared location'),
 p('The same danger has followed them down.','ONLY Ren tight face looking past Mira at offscreen approaching SAME guardian, still unarmored.','left-aligned84% width, medium close','Ren thought','まだ、来るのか。','worried cloud thought with dots'),
 p('He puts Mira behind him.','Ren BARE open hand directs Mira back toward cargo wall; ordinary shirt, no armor yet. Focus only gesture and her safe backward step.','right-aligned92% width, medium framed','Ren','ミラ、下がって。','firm ordinary speech'),
 p('His choice comes before the power.','ONLY Ren large determined face/chest, soft shirt and red scarf, Mira safely offscreen behind; no visible blue star or armor yet.','full-width large borderless emotional close','Ren','今度は俺が止める。','resolute rounded oval, no shout decoration')],90)

add(1,'core',['core'],[
 p('A strange light appears in fabric for the first time.','Close BARE hand at still-soft BLACK shirt chest as first tiny CYAN star glows through cloth. No full armor silhouette. Dark navy scene.','full-width medium framed prop close','Ren thought','これは……？','cloud and thought dots'),
 p('The system reports the cause before the equipment name.','Cyan translucent functional rectangle in dark background; small edge of shirt, no armored limbs. EXACT system words in upright Japanese: 救命行動を確認。救済核、起動。','right-aligned94% width, shallow functional system frame'),
 p('The armor name appears separately, but the body reveal waits below.','CYAN system label only in plain functional frame: EXACT 装甲名：ゼロ・ブレイク. Soft shirt silhouette only, no transformed body or hands.','full-width broad framed dark system view')],250)

add(1,'relief',['relief'],[
 p('Mira looks at the stopped guardian and living Ren.','Mira face alone, safe lower solid plaza, violet-black wreckage blurred; Ren STILL basic black armor offscreen left.','right-aligned87% width, medium framed','Mira','あなた、本当に魔力ゼロなの？','warm questioning soft blue-grey outline'),
 p('Ren gives a short answer.','Ren armored shoulders and relieved face, red scarf.','left-aligned82% width, medium close','Ren','みたいだ。','gentle ordinary speech'),
 p('He takes in that somebody really is safe.','ONLY Ren black armored hand relaxes from a fist; SAME wreckage, no crest or new person.','left-aligned68% width, shallow silent hand insert'),
 p('His relief is bigger than the numerical verdict.','ONLY Ren wide relieved face, slightly wet eyes, blue chest star and red scarf; Mira safely offscreen right.','full-width large BORDERLESS emotional close','Ren','けど、役立たずじゃなかった。','breathless soft wavering thin contour')],160)

add(1,'fragment',['fragment'],[
 p('Ren lifts a single piece from the defeated guardian.','BLACK armored glove picks up SAME violet-black core shard from safe plaza, crown side turned away, NO crest visible yet.','left-aligned78% width, shallow hand insert'),
 p('The mark is shown FIRST HERE.','Macro same single shard in black glove with unmistakable SMALL CROWN engraved on violet-black stone. No workshop number on reverse yet.','full-width medium framed reveal'),
 p('Mira recognizes the clue.','ONLY Mira concerned face looking at shard offscreen left, not smiling; same plaza.','right-aligned90% width, medium-height framed','Mira','その紋章……王家の工房のものよ。','serious composed blue-grey rounded capsule'),
 p('Ren asks what the clue means, without naming the later enemy.','ONLY Ren basic armored shoulders/red scarf and worried face facing Mira offscreen right.','full-width large close-up','Ren','じゃあ、なんで俺たちを襲った？','quiet troubled ordinary oval')],190)

def reuse(key,replaces,source,prompt_file,panels,continuation=False):
    jobs.append({'id':'e01-'+key,'episode':1,'file':'v6-'+key+'.png','replaces':replaces,
                 'context':'Same lower cargo plaza after Mira is caught and landed safely; Ren kneels, Mira stands. No armor, no crown crest yet.' if 'safe' in key else 'Ren catches Mira in midair with bare arms before landing.',
                 'panels':panels,'references':[source],
                 'prompt':(REPO/prompt_file).read_text().strip(),'reuse_source':source,
                 'continuation_part':continuation,'pause':35 if key=='safe-01' else 100})

reuse('safe-01',['safe'],'skills/webtoon/references/zero-break/balloons-01.png','skills/webtoon/references/zero-break/prompt-balloons-01.txt',[
 p('Both are safe after landing.','Ren kneels left; Mira stands right on the SAME solid cargo plaza under torn awning.','large full-width framed shared location'),
 p('Mira thanks him.','ONLY Mira face; Ren remains beside her offscreen left.','right-aligned narrow medium frame','Mira','ありがとう。','gentle soft blue-grey contour'),
 p('Ren takes in the thanks.','ONLY Ren blue eyes, unarmored.','left-aligned shallow eye insert'),
 p('Mira tells him her name.','ONLY Mira upper body, hand at chest; same torn cargo awning.','large wide framed portrait','Mira','私はミラ。','composed blue-grey rounded capsule')])
reuse('safe-02',['safe'],'skills/webtoon/references/zero-break/balloons-02.png','skills/webtoon/references/zero-break/prompt-balloons-02.txt',[
 p('Her role is one new fact.','ONLY Mira dress/hand at chest. No guardian crest.','medium-height hand/detail frame','Mira','この国の王女よ。','composed blue-grey rounded capsule'),
 p('Ren hears that she is a princess.','ONLY Ren eyes. Same kneeling pose.','small shallow left eye insert'),
 p('He gives his name.','ONLY Ren face, BARE hand touches scarf.','right-aligned medium framed face','Ren','レンだ。','ordinary black oval'),
 p('He says that her safety is what matters.','ONLY Ren relieved face, kneeling under torn awning; no armor.','large full-width borderless emotional portrait','Ren','無事なら、それで。','breathless wavering outline with continuous speech tail')],True)
reuse('catch',['catch'],'skills/webtoon/references/zero-break/balloon-shout.png','skills/webtoon/references/zero-break/prompt-balloon-shout.txt',[
 p('Ren catches Mira before they reach the canvas.','Ren BARE arms support Mira back and knees in midair, red scarf streams, awning below.','medium full-width action frame','Ren','つかまって！','thick jagged urgent shout with tail to mouth')])

def revise(n,key,parts,focus,reaction,voice='composed ordinary speech',pause=120):
    d=json.loads((STATE/'baseline'/f'episode-{n:02d}.json').read_text())
    shot=next(s for s in d['shots'] if s['id']==key)
    speaker=shot['lines'][0]['speaker']
    panels=[]
    for i,text in enumerate(parts):
        panels.append(p('The reader receives one part of the explanation, before a response.',focus,'right-aligned90% width, medium framed speaker close-up' if i==0 else 'full-width LARGE borderless emotional close-up',speaker,text,voice))
        if i==0:
            panels.append(p('The listener or the relevant object holds the same scene while the words settle.',reaction,'left-aligned72% width, shallow silent detail/reaction insert'))
    if len(parts)==1:
        panels.insert(0,p('Confirm the immediate context without adding a new event.',shot['scene']+' Show the established spatial relationship, WITHOUT replaying earlier action or later results.','full-width wide framed establishing shot'))
    add(n,key,[key],panels,pause)

# Each topic keeps its existing plot and exact words; the panels slow the crucial inference.
revise(2,'support',['英雄も、お腹は空くんですね。'],'ONLY Mira gentle face after supporting exhausted unarmored Ren at same ruined plaza; Ren nearby offscreen left.','Ren hand on empty stomach, now BARE after armor has faded; Mira still supporting him.','warm soft outline')
revise(2,'debt',['助けたら、借金？'],'ONLY unarmored Ren face looking up from SAME invoice, shocked not angry; Rook offscreen right.','Invoice held in Ren BARE hand; paper abstract geometric lines, no invented amount.','baffled slightly wavering spoken oval')
revise(2,'hold',['戦う燃料がないなら、','持ち上げるだけだ。'],'ONLY Ren BASIC black-armored strained face at same beam crossing, cyan star weak. He MAINTAINS the beam, not attacking.','Close black-armored hands supporting SAME white beam, boots braced on solid ledge; family remains stranded at far end, has NOT crossed yet.','strained wavering speech; continuous tail, no thought dots',95)
revise(2,'responsibility',['王家の責任です。','あなた一人に払わせません。'],'ONLY Mira serious face holding invoice at SAME safe ledge, tired unarmored Ren nearby; Rook listens offscreen.','ONLY Ren tired eyes look up at Mira, surprised she accepts responsibility. Rescued family stays safely offscreen.','firm composed blue-grey capsule',170)
revise(2,'inside-threat',['これ、外から来た魔物じゃない。'],'ONLY Mira concerned face; same single core fragment with REVERSE plate already revealed, Ren offscreen beside her.','Ren eyes shift from fragment toward royal towers; no new enemy or incident.','quiet serious blue-grey capsule',210)

revise(3,'challenge',['私に勝てば免許をやる。'],'ONLY Rook confident face in SAME morning market training space, practice sword lowered safely. Ren remains unarmored offscreen left.','Rook glove holding unopened permit envelope; Ren BARE fingers hesitate, no acceptance and no armor.','reserved ordinary oval')
revise(3,'no-answer',['さっきの力、もう消えたのか。'],'ONLY Ren face, uncertain after failing to transform for a duel, same training space.','ONLY Ren BARE open hand, sleeve ordinary BLACK cloth; chest dark, no power.','thought cloud with dots, never a speech tail')
revise(3,'rule',['助けるときだけ、','応えている。'],'ONLY Mira calm thoughtful face in SAME market after barrel stopped; child already with mother offscreen.','Ren looks down at now BARE forearm; the partial armor has already faded during the reunion. Both hands BARE, no armor. Faint cyan point remains at fabric chest. He compares the completed rescue with failed duel.','gentle composed blue-grey capsule',190)
revise(3,'permit',['じゃあ、勝つより先に助ける。'],'ONLY Ren face, quietly resolved beside training table AFTER child safe, unarmored red scarf.','Ren BARE hand puts unopened permit and prize purse BACK on table. No duel victory or license reward.','calm ordinary oval',145)

add(4,'noa',['noa'],[
 p('Mira introduces the person, not only the room.','ONLY Mira face inside SAME warm amber workshop just entered. Noa already visible in previous workshop establishing frame, Ren offscreen beside her.','right-aligned90% width, medium framed face','Mira','整備士のノアよ。','composed thin blue-grey capsule'),
 p('Noa checks what he heard.','ONLY Noa adult orange hair/green eyes, goggles ON head, friendly face, SAME blue overalls and warm workshop.','left-aligned84% width, medium close','Noa','魔力ゼロ？','friendly rounded speech with thin warm brown line'),
 p('Ren waits to hear whether he will be rejected again.','ONLY Ren uncertain BLUE eyes. Noa orange glove still offers ONE broken handheld meter at bottom edge; NOT yet released into Ren hands.','left-aligned70% width, shallow eye/hand insert'),
 p('Here the same number has a different social meaning.','ONLY Noa smiling face, Ren remains nearby offscreen; SAME workshop and meter.','full-width large borderless welcoming portrait','Noa','こっちじゃ普通。','gentle rounded speech with thin warm brown line')],150)
revise(4,'pipe-map',['この弁で、','圧を逃がせる。'],'ONLY Mira face angled down to SAME physical pipe map in warm workshop; steam behind, no new device.','Mira finger traces bypass branch on unfolded map. Noa orange glove follows route, valve has NOT been turned yet.','clear composed blue-grey speech',95)
revise(4,'finite',['有限だよ。','でも、使い方は変えられる。'],'ONLY Noa thoughtful face AFTER boiler vented, all alive. Ren armor faded; same warm workshop.','Falling line on physical paper chart in Noa orange gloves; Ren BARE hand lowers, listening. No tiny fabricated labels.','ordinary friendly rounded speech',180)
revise(4,'friend',['昨日まで、','友達が住んでた。'],'ONLY Noa worried face, goggles lifted on head, SAME safe workshop; not another house.','Noa orange-gloved finger rests on SAME blank/disconnected district on city map. No vanished residents or enemy depicted.','quiet vulnerable soft contour',210)

revise(5,'not-moving',['引っ越しなら、','靴は持っていく。'],'ONLY Noa troubled face inside SAME empty lower-city home at dusk. Holds friend single boot.','Single worker boot in orange gloves; its mate sits by door, warm soup on table nearby. No gore or corpse.','quiet troubled soft contour',165)
revise(5,'denial',['存在しない区画です。'],'ONLY middle-aged GREY-cloaked clerk face at SAME records counter, formal evasive manner. Ren and Mira remain on public side offscreen.','Mira finger holds folded OLD map beside blank registry square. Preserve prop ownership; clerk does not erase it in front of them.','cold formal rounded rectangle',130)
revise(5,'vow',['全員を戻す。','そのために、場所を忘れない。'],'ONLY unarmored Ren calm determined face at SAME safe workshop beside RECOVERING grey-bearded old man; not on conveyor again.','Ren BARE hand holds SAME copied route paper; old man rests breathing safely, Noa listens offscreen.','quiet determined ordinary oval',180)
revise(5,'friend-listed',['ハルも、','ここにいる。'],'ONLY Noa widening green eyes at same dawn-route paper in workshop.','Orange-gloved fingertip on EXACT handwritten name ハル on SAME list; other names abstract lines, no Haru bodily appearance yet.','hope and worry, slightly wavering speech',210)

revise(6,'unlock',['ハル、迎えに来た。'],'ONLY Noa relieved face just outside opened prisoner compartment; Noa has JUST unlocked door, Haru still inside.','Close Haru adult brown hair green workshirt sees Noa through SAME open doorway, hopeful eyes; no escape complete.','warm soft rounded speech',100)
revise(6,'ladder',['歩ける人は、','次の人を支えて。'],'ONLY Mira focused face beside SAME secured ladder, dangerous tilted carriage behind.','Both ends of ladder locked to SOLID catwalk and tilted door; Noa glove secures coupling. NO evacuee crossing before the ladder is fixed. Ren still holding carriage underfloor offscreen.','firm clear blue-grey speech',90)
revise(6,'release',['…全員、いるな。'],'ONLY Ren exhausted face as BASIC black armor fades after seventeen people counted OUTSIDE. SAME intact catwalk.','Mira pencil over roster with17 checkmarks; EMPTY carriage below now being released. No person back inside.','breathless slightly wavering continuous speech tail',200)
revise(6,'rook-blocks',['王室への反逆、','という扱いになる。'],'ONLY Rook guarded face at SAME exit gate, sword SHEATHED; not a new attack.','Ren tired unarmored eyes looking up; seventeen evacuees stay sheltered safely behind Mira and Noa offscreen.','grave restrained ordinary oval',190)

revise(7,'girl-steps',['この人、私たちを出してくれた。'],'ONLY small brown-haired GIRL in YELLOW dress face at SAME exit gate, scared but speaks toward Rook.','ONLY Rook gloved sword hand loosens, blade safely downward. Ren exhausted unarmored nearby offscreen, same seventeen survivors.','small earnest soft speech',140)
revise(7,'suspension',['あなたの権限は、','停止された。'],'ONLY older45 commander dark greying hair, navy cape and silver armor face. SAME exit gate AFTER Mira refuses recapture.','ONLY Mira shocked eyes; royal authority seal broken from command order chain at edge. She stays protective, no restored powers.','cold heavy rounded rectangular speech',145)
revise(7,'shield',['こっちへ！','頭を下げろ！'],'ONLY Rook urgent face as he holds STEEL SHIELD over evacuees in SAME collapsing corridor; same blue cape.','Cowering evacuees duck underneath shield as rubble is stopped. NO one already in service yard.','urgent SHOUT with thick jagged outer edge',80)
revise(7,'apology',['見ないふりをした。','謝って終わらせない。'],'ONLY Rook remorseful lowered face in SAME safe service yard AFTER everybody escaped. Hands empty, no theatrical kneeling.','ONLY seated unarmored Ren eyes listen, tired but attentive. SAME survivors resting safely nearby offscreen.','low serious ordinary capsule',180)
revise(7,'accept-work',['じゃあ、次の人を一緒に。'],'ONLY unarmored Ren quietly accepting face at SAME rescue table AFTER Rook set down his license.','Ren BARE hand offers plain rope end and Rook BLACK glove accepts. OWN license stays on table, no official restoration.','warm soft ordinary oval',150)

revise(8,'first-hero',['初代勇者です。'],'ONLY masked thin ceremony guide in GREY robe face, SAME white certification hall; Ren and Mira listen offscreen.','Ren looks up at SAME WHITE-armored statue with GOLD star, small view only; no living face or name アラタ.','neutral formal rounded speech',130)
revise(8,'compare-star',['星の形が、','同じ…。'],'ONLY Mira thoughtful face in SAME statue hall, looks between statue and Ren, no new danger.','Compare a shallow silent detail: same GOLD statue star above, Ren faint CYAN chest point below scarf at edge. Shapes match but COLORS DIFFER. NO new form.','quiet softly wavering blue-grey speech',190)
revise(8,'refuse',['こんな試験、受けない。'],'ONLY Ren controlled outraged face in SAME trial hall, ordinary black shirt red scarf; no armor yet.','Ren BARE open hand turns away from offered ceremonial sword toward actual restrained living adults. No killing or early chain release.','firm ordinary oval',120)
revise(8,'their-evidence',['あなたたちの証拠です。'],'ONLY Mira resolute face in SAME trial hall AFTER copying memory crystal, freed people already exiting safely behind Rook.','Mira BARE palm offers ONE brass memory crystal toward grey-robed guide; no multiple crystals or new display text.','composed blue-grey capsule',170)
revise(8,'reject-selection',['誰が、そんなことを決めた。'],'ONLY Ren unarmored angry restrained face at SAME statue base AFTER reading the selection inscription.','Ren BARE hand drops from dusty plinth; white statue shadow over red scarf, Mira holds same recording offscreen. No future enemy face or name.','low firm ordinary oval',210)

revise(9,'other-axis',['空じゃない。','測る箱が違う。'],'ONLY Mira calm explaining face in SAME warm amber workshop AT NIGHT; no sunshine windows.','Physical paper with TWO graph axes: large exact horizontal labels 魔力 and 救助負荷. One flat and one rises. Ren eyes follow the difference without instant mastery.','clear composed blue-grey capsule',170)
revise(9,'ventilator-stops',['呼吸の装置が…！'],'ONLY Mira suddenly worried face in SAME NIGHT medical alcove after power cut.','Brass breathing bellows slowing beside SAME grey-bearded old man in brown vest on cot; no death/gore or restored breathing yet.','urgent angular bold outer outline, continuous mouth tail',90)
revise(9,'isolate-circuit',['街の線とは、','切り離す。'],'ONLY Noa focused face in SAME dim NIGHT workshop, orange goggles and gloves, not outside in sunlight.','Orange-gloved hands connect physically ISOLATED rescue-core copper circuit ONLY to ventilator. Ren BARE hand on terminal at edge. No city-grid connection or new form, device not moving yet.','calm practical ordinary capsule',110)
revise(9,'breath-returns',['息が、戻った。'],'ONLY Mira relieved face in SAME NIGHT alcove, ordinary blue-white-gold dress.','Same grey-bearded old man FIRST visibly inhales, blanket chest lifts, fingers relax. Ren STILL supplies isolated circuit offscreen, has not stopped.','gentle soft blue-grey contour',210)
revise(9,'location',['ここが、','消えた街区の行き先。'],'ONLY Mira resolved face in SAME NIGHT workshop after route revealed on map.','Mira fingertip traces SAME map directly underneath palace, EXACT large existing label 王宮直下. Ren keeps ventilator powered offscreen, Rook guards door. No new chamber victims or villain yet.','quiet serious blue-grey capsule',210)

revise(10,'evidence',['消された人には、','名前があります。'],'ONLY Mira solemn face at DAY festival podium, brass microphone; first public evidence projection behind is blurred.','Audience one listener face stops laughing; physical recording shows transport silhouettes, no new victims or illegible captions. Ren unarmored offscreen.','firm composed blue-grey capsule',170)
revise(10,'choice',['証拠は写せる。','人は戻せない。'],'ONLY Ren unarmored determined face BETWEEN damaged tower/projector above and trapped spectators below. Same black cloth shirt, no armor until he runs.','Ren BARE fist releases scarf and opens toward endangered spectators; intact evidence projector higher at edge. Actual choice of lives before records, no saved group yet.','low resolute ordinary oval',135)
revise(10,'noa-copy',['一つ消しても、','終わらない。'],'ONLY Noa determined face under SAME intact kiosk after MAIN tower damaged; daytime. Ren still holds beam offscreen.','Noa orange gloves plug ONE duplicate memory crystal into SMALL independent shop relay. No advanced LINK-form gadget, no Ren in frame.','ordinary practical rounded speech',125)
revise(10,'name-them',['十七人です。','一人ずつ、ここにいます。'],'ONLY Mira face speaks into SAME brass relay microphone from safe street, copied roster held; not on damaged tower.','Copied roster in her fingers and listening street resident at edge; names abstract, no count changing. Ren remains supporting beam offscreen, no early release.','firm empathetic blue-grey capsule',170)
revise(10,'arrest',['今度は、','見ないふりをしない。'],'ONLY Rook resolved face in SAME safe DAY plaza after applause, no knight license, blue cape and silver armor.','Rook BLACK glove closes lawful cuff over SAME45 commander wrist beside copied evidence; commander ALIVE uninjured, no revenge violence.','quiet firm ordinary oval',180)
revise(10,'close-gates',['ゼロを、','上げてはいけない。'],'Only palace WHITE-armored living unknown hero BACK silhouette high above lowering gates; no face, name or Ren.','Massive SAME palace gates descend, last thin gap of daylight at bottom. No protagonist trapped or new plot outcome.','cold unseen voice in strong angular rounded frame; tail exits toward unseen mouth, no thought dots',230)

layout={'1':{'memory':100,'footsteps':76,'knight_arrives':100,'touch':78,'result':88,'zero_reaction':100,'tremor':72,'hero':100,'fall':100,'leap':94,'landing':100,'punch':100},
        '2':{'hunger':86,'untransform':76,'crack':78,'set-down':76,'turn-fragment':84,'workshop-number':96},
        '3':{'fist':72,'laughter':84,'axle':76,'move':90,'mechanical-bird':82,'monitor':100},
        '4':{'key':76,'catch':78,'fault':78,'valve-search':82,'open-valve':76,'missing-wires':84},
        '5':{'shoes':74,'ledger':86,'record':92,'destination':96},
        '6':{'roster':84,'inspection':82,'wrong-target':90,'all-seventeen':100,'pass':78},
        '7':{'hand-stops':76,'collapse-cue':78,'discard-order':76,'return-license':80,'invitation-cue':84,'invitation':100},
        '8':{'trial-door':84,'turn-back':92,'cut-chain':90,'copy-evidence':86,'old-inscription-cue':80,'selection':100},
        '9':{'zero-again':90,'cut-power':78,'check-patient':92,'breath-cue':80,'signal':82},
        '10':{'tower-hit':90,'run':96,'set-beam':92,'first-clap':86,'base':100}}
add(1,'rook-name',['greeting'],[
 p('The knight tells Ren who he is before explaining the country.','ONLY Rook face and silver armor/blue cape; immediately AFTER helping Ren stand, SAME intact white stair landing. Ren stands offscreen left.','right-aligned92% width, medium framed speaker','Rook','私はルーク。この街の騎士だ。','reserved ordinary rounded speech'),
 p('Ren has accepted help and knows whose explanation he is hearing.','One standing Ren and one standing Rook on SAME stair landing, medium upper bodies, Ren small grateful nod. No crystal or future magic result.','full-width wide quiet shared location')],80,context_override='Immediately AFTER Rook helps seated Ren rise: both now STAND at same intact stair landing; they have not walked to the measuring station. Rook introduces his name and job. No Mira, crystal, armor or future0 result.')
jobs[-1]['continuation_part']=True
jobs[-1]['added_context_dialogue']=True
next(j for j in jobs if j['id']=='e04-noa')['added_context_dialogue']=True
plan={'edition':'context-dialogue-v6','scope':'Illustrated episodes1-10; scripts1-50','jobs':jobs,'layout':layout}
(STATE/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(f'Planned {len(jobs)} generated strips')
