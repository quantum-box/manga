from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
if any((ROOT/f'episode-{n:02d}/manifest.json').exists() for n in range(2,11)):
 raise SystemExit('Initial planning only: existing episode manifests contain adopted art and pacing. Rebuild with production/build.py; do not overwrite them.')
# id | crop | pause at 390px | exact visible moment and character/prop state | speaker:text:columns (right to left);...
RAW={2:'''hunger|wide|35|Ren in full black armor, cyan chest star weak, hand on stomach, embarrassed and exhausted amid guardian rubble. Only effect ぐう… .|
untransform|wide|55|Close bare Ren hand emerging as black arm armor flakes into tiny blue light; red scarf remains, black short sleeve shirt underneath. Exhaustion, no new danger.|
support|portrait|100|Unarmored Ren sways; Mira steps beside him and supports his shoulder with one hand, smiling gently among rubble. This is the first support touch.|Mira:英雄も、お腹は空くんですね。:英雄も、/お腹は/空くんですね。
invoice|wide|45|Rook in silver armor, blue cape, black gloves offers a paper sheet across the plaza. Ren's bare hand accepts the sheet. Paper is geometric unreadable lines only, no invented numbers.|Rook:無許可の戦闘だ。:無許可の/戦闘だ。
debt|portrait|110|Close unarmored Ren looking up from the same sheet with shocked eyebrows, chest not glowing. Mira and Rook remain beside plaza rubble.|Ren:助けたら、借金？:助けたら、/借金？
crack|wide|120|Close crack widening across a white aqueduct support above a gap. Water leaks downward. Only effect ミシ… . No people or rescue outcome.|
stranded|tall|70|Vertically establish damaged aqueduct: mother in brown shawl and small boy in green shirt stranded on tilted upper ledge; open gap below; rescuers Ren and Mira on intact LOWER opposite ledge. Clear unsafe and safe positions, no bridge yet.|Mother:誰か…！:誰か…！
barrier|portrait|50|Rook's gloved palm bars Ren at a cordon on intact lower ledge; stranded parent and child on opposite distant ledge, no armor yet.|Rook:立入禁止だ。:立入禁止だ。
set-down|wide|70|Close Ren placing invoice flat onto a safe dry stone at cordon, bare fingers release paper. His gaze turns toward parent and child, no armor yet.|
choice|portrait|90|Unarmored Ren leans toward danger, teeth set but visibly tired, Mira behind him sees his decision.|Ren:まだ、手は届く。:まだ、/手は届く。
hold|tall|65|Ren reactivates only weak complete black armor/cyan star; feet braced on intact lower ledge, both hands lift a fallen white beam so it spans the gap to the family. Beam holds position as a crossing, family not crossing yet.|Ren:戦う燃料がないなら、持ち上げるだけだ。:戦う燃料が/ないなら、/持ち上げる/だけだ。
rope|portrait|50|Mira hands coiled rope to two adult residents beside safe end of beam; one end already secured to intact column, Ren holds beam in background.|Mira:この縄を、支えてください。:この縄を、/支えて/ください。
cross|tall|65|Mother and boy cautiously step along held beam, grasping taut safety rope; residents pull rope from safe side, Ren's armor cracks while holding weight. They are MIDWAY, not safe yet.|
safe|portrait|190|Mother and boy now both on dry intact safe ledge, hugging each other, relieved faces. Rope slack, beam still secured, no return to dangerous position.|Boy:お母さん…！:お母さん…！
exhale|wide|130|Ren unarmored again sitting at safe ledge edge, bare hands trembling; Mira kneels beside him with a water cup, no romantic touch. Rescued family behind safely.|Ren:よかった…。:よかった…。
responsibility|portrait|150|Mira stands between Rook and seated tired Ren. Holds invoice herself, authoritative concern, ruined crown-run aqueduct behind. Ren no armor.|Mira:王家の責任です。あなた一人に払わせません。:王家の/責任です。/あなた一人に/払わせません。
cancel|wide|120|Close Mira places royal ring over the invoice in Rook's gloved hands, cancelling the demand by gesture; Ren watches startled, paper unchanged unreadable diagrams. No new text.|Rook:…承知しました。:…承知/しました。
turn-fragment|wide|360|Mira turns over the guardian fragment already found in episode1; its outer crown crest turns away; backside still hidden from camera. Ren leans closer, curiosity replaces relief. No workshop number visible yet.|
workshop-number|portrait|170|FIRST close reveal backside guardian fragment with etched small crown plus exact horizontal plate text 王室工房　七番 . Mira's fingertips and surprised eyes behind. Only this label on metal, not a speech balloon.|
inside-threat|portrait|210|Mira holds revealed fragment, Ren stands beside her looking toward royal white towers with sober expression. No enemy identity shown.|Mira:これ、外から来た魔物じゃない。:これ、外から/来た魔物じゃ/ない。''',
3:'''morning|tall|80|Next morning bright market of white sky city, Ren unarmored red scarf carrying bread beside Mira; Rook waits at cleared training space, unsharpened training sword lowered. No power yet.|
challenge|portrait|80|Rook offers a permit envelope and points practice sword toward marked dueling space, Ren listens warily, Mira observes.|Rook:私に勝てば免許をやる。:私に勝てば/免許をやる。
fist|wide|70|Close Ren's bare fist clenches, black shirt sleeve and red scarf, chest totally dark; attempting armor for competition and failing.|
no-answer|portrait|90|Ren stares at his unchanged bare hand, worried; chest dark. Rook's practice sword held safely down, crowd amused.|Ren thought:さっきの力、もう消えたのか。:さっきの力、/もう消えた/のか。
laughter|wide|110|Two adult market spectators snicker behind an uncertain Ren foreground. No text, no aggressive mob or new armor.|
practice|portrait|55|Rook makes one slow practice sword approach toward Ren's bare hand in training area; Ren steps back safely, no armor, not a wound or real fatal attack.|Rook:その程度か。:その程度か。
axle|wide|85|Nearby laden handcart wooden axle splits under a barrel. FIRST mechanical failure, child's shadow farther down slope, no rescue or armor. Only effect バキッ .|
barrel|tall|65|Large barrel rolls down sloped white market steps toward SAME small boy green shirt from prior rescue, mother reaches from side too far. Show actual barrel, child and Ren distance. No impact yet.|Mother:危ない！:危ない！
move|wide|45|Ren discards bread bag safely and runs toward child with bare hand extended, decisive urgency. No giant leap, no armor until protection moment.|
shield-arm|portrait|50|FIRST partial transformation: only Ren's FOREARM becomes black faceted armor with cyan seam as he puts arm between boy and rolling barrel. Rest black shirt, scarf, bare other hand. Chest faint star light through shirt, no full armor.|
stop|tall|120|Ren's ONE armored forearm braces and stops the intact barrel one step from child; boots dug into slope, mother behind child reaches him. No attack on Rook, no explosion. Only effect ドン .|
realization|portrait|160|Ren looks at armored forearm in astonishment, Rook lowers practice sword safely in background; stopped barrel beside feet, child and mother together.|Ren:勝つためには、動かない？:勝つためには、/動かない？
reunion|portrait|160|Mother hugs same green-shirt boy on safe flat market landing. Ren's forearm armor fades, no barrel threatening them now.|Boy:ありがとう。:ありがとう。
rule|portrait|180|Mira approaches Ren and points gently to faint cyan chest point while Ren listens, both now unarmored. Rook silent background.|Mira:助けるときだけ、応えている。:助けるとき/だけ、/応えている。
permit|wide|130|Ren sets duel prize purse and unopened permit envelope back on training table, walks toward rescued family with Mira. No victory in duel or illegal reward.|Ren:じゃあ、勝つより先に助ける。:じゃあ、/勝つより先に/助ける。
mechanical-bird|wide|450|Small silver brass mechanical bird secretly watches FROM market roof, cyan camera lens aimed toward Ren far below. No enemy face or display text yet.|
monitor|portrait|130|Dark remote room with nobody's face, simple cyan translucent monitor displays Ren chest recording and exact label 未登録救済核 horizontally. No name of enemy, no armor portrait inside readout.|
watcher|portrait|180|Silhouette hand resting on desk beside same cyan monitor. Only sleeve edge, no face or white armor revealed.|Unknown:ようやく来たか。:ようやく/来たか。''',
4:'''back-stairs|tall|80|Mira guides unarmored Ren down palace rear spiral stairs toward closed heavy workshop door; sunshine above, warm amber light below. No prison bars.|Ren:牢屋じゃないよな。:牢屋じゃ/ないよな。
key|wide|350|Close Mira inserts a single brass key and turns it in workshop lock, bare fingers visible; door still closed, room and new character hidden.|
workshop|tall|120|FIRST reveal open oily workshop: pipes, wooden workbench, round pressure boiler at back, young adult orange-haired mechanic Noa in blue overalls and goggles on head, waving from bench. Mira and Ren enter, no danger.|Mira:私たちの工房よ。:私たちの/工房よ。
noa|portrait|70|Noa adult18 orange tousled short hair green eyes goggles on head blue mechanic overalls black undershirt orange gloves, casually offers a broken handheld meter to Ren across bench.|Noa:魔力ゼロ？こっちじゃ普通。:魔力ゼロ？/こっちじゃ/普通。
catch|wide|65|Close Ren's bare hands catch same broken handheld meter, Noa orange glove releases it, no duplicate meter. Face softening from tension.|
common|portrait|150|Ren smiles slightly at Noa, no armor. Mira gathers a copper testing lead but no new advanced power gadget.|Ren:…俺だけじゃないんだ。:…俺だけ/じゃないんだ。
fault|wide|90|Close boiler gauge needle climbing red band while clogged safety valve vibrates. Ordinary apparatus fault during a neutral observation test; nobody intentionally creates danger. No explosion outcome yet. Only effect カタカタ .|
notice|portrait|65|Noa hears vibrating valve and turns toward boiler; Ren notices hiss behind Noa, chest faint cyan. Mira holds paper pipe map still rolled.|Noa:圧力が、戻らない。:圧力が、/戻らない。
cover|portrait|60|Ren moves between Noa and leaking boiler, raises one black armored forearm; full body stays black shirt/red scarf, energy limited. Noa ducks beside control pipes.|Ren:下がって！:下がって！
valve-search|wide|70|Noa crouches along brass pipes finding jammed manual valve, orange gloves checking connections; steam directed upward away from faces. Ren maintains shield arm, no giant blast.|
pipe-map|portrait|80|Mira unfolds pipe routing paper on bench and traces safe bypass branch with finger, Noa follows gesture toward brass valve.|Mira:この弁で、圧を逃がせる。:この弁で、/圧を逃がせる。
open-valve|wide|70|Noa's orange-gloved hands turn correct brass wheel valve; pressure needle visibly falls, safe vent releases steam upward. No magic upgrade.|
last-fragment|portrait|140|One loose metal cap fragment flies; Ren's single armored forearm catches it with other bare hand holding Noa back safely. Boiler now vented, all three uninjured.|
shared-load|portrait|150|Ren exhales and lowers armored forearm, looks to smiling Noa and Mira; sparse steam clears.|Ren:全部、俺が受けなくていいのか。:全部、俺が/受けなくて/いいのか。
finite|portrait|150|Noa shows a simple graph on paper: line falls during prior strain, no illegible annotations. Ren listens; armor gone, red scarf unchanged.|Noa:有限だよ。でも、使い方は変えられる。:有限だよ。/でも、使い方は/変えられる。
team-sign|portrait|220|Mira and Noa hang small handmade wooden plaque reading 救助隊 horizontally over workshop door. Ren reaches up helping straighten it; warm small success.|
missing-wires|wide|380|Close Noa's orange-gloved finger traces blank disconnected block on city circuit map. No residents shown disappearing, no full conspiracy answer.|
friend|portrait|190|Noa beside blank block map, hand clenched, goggles pushed up, worried genuine personal face. Ren watches empathetically.|Noa:昨日まで、友達が住んでた。:昨日まで、/友達が/住んでた。''',
5:'''empty-house|tall|130|Ren Mira Noa enter low-ceiling LOWER-city house at dusk: steam rises from unattended soup bowl, empty chairs, no bodies or horror. Humble brick and brass pipes contrast royal white towers.|
shoes|wide|130|Close Noa orange-gloved hand picks up a single adult worker boot beside warm meal; match its mate by door, no blood.|
not-moving|portrait|150|Noa holds friend's boot, worried brows, Ren beside door scans empty home, unarmored.|Noa:引っ越しなら、靴は持っていく。:引っ越しなら、/靴は持っていく。
ledger|wide|80|At small local records counter, clerk's finger points to clean blank square on registry page; Mira places folded old map beside it, Noa still has boot. No tiny fabricated text.|
denial|portrait|100|Middle-aged grey-cloaked clerk shakes head behind counter, Ren and Mira visible listening angry but controlled.|Clerk:存在しない区画です。:存在しない/区画です。
old-map|portrait|160|Mira unfolds old city map aligned against new erased ledger page, same block clearly drawn on old map. Her face firm, not instantly conspiracy explained.|Mira:この家は、ここにあります。:この家は、/ここに/あります。
entry|tall|110|Three descend a service stair into blue-grey subterranean brass transport tunnel following block's pipe route. No captive silhouettes yet, keep directional stair and single lantern.|
voice|wide|410|Ren pauses with bare hand near vibrating pipe wall, Noa lantern ahead, no captives visible yet. Tiny speech balloon seems from unseen wall.|Unseen resident:…出して。:…出して。
captives|tall|120|FIRST reveal silhouettes of living residents moving inside translucent magical transport conduit behind brass protective window. Clear distressed humans, not liquid or gore, destination hidden. Ren Mira Noa foreground aghast.|
old-man|portrait|80|Grey-bearded old man in brown vest has crawled out through inspection hatch and collapsed on tunnel walkway, breathing, NOT among the later17-person car convoy. Ren kneels to check him.|Ren:聞こえますか。:聞こえますか。
patrol|wide|60|A small brass patrol drone searchlight sweeps toward tunnel fork; Noa spots it, elderly survivor foreground supported by Ren. No giant attack yet.|
choose|portrait|95|Ren looks from receding transport shadows to elderly man's shaky breathing, chooses to pick him up rather than chase.|Ren:まず、この人を外へ。:まず、この人を/外へ。
jam-signal|wide|100|Noa orange gloves remove drone relay fuse at wall access panel, searchlight dims; only hand-tool technology, no future load disperser. Mira records conduit plate.|
escape|tall|110|Ren unarmored carries grey-bearded old man uphill through service stair; Mira with copied paper and Noa lantern follows, everyone moves toward workshop safety.|
record|portrait|150|Safe workshop, old man resting on simple cot breathing. Mira copies conveyor number and time on paper; Noa compares missing friends' registry, exact big handwritten labels 十七人 and 明朝 only.|
vow|portrait|180|Ren sits beside recovering old man, holds copied route paper calmly rather than boasts; other two listen.|Ren:全員を戻す。そのために、場所を忘れない。:全員を戻す。/そのために、/場所を/忘れない。
destination|wide|380|FIRST close reveal next morning delivery docket: exact horizontal large title 英雄認定場 and small bold count 十七人 . No enemy face. Mira fingertips hold document.|
friend-listed|portrait|210|Noa's gloved finger stops on handwritten name ハル in simple list; Noa's green eyes widen, Ren beside grips scarf. Just one readable name, rest abstract lines.|Noa:ハルも、ここにいる。:ハルも、/ここにいる。''',
6:'''dawn-plan|tall|100|Dawn beside upper sky rail loading platform, Ren Mira Noa study paper roster; convoy carriage beyond closed gate. Seventeen live prisoners expected, no arbitrary extra vehicle or advanced form.|Ren:一人ずつ、確認する。:一人ずつ、/確認する。
roster|wide|110|Close Mira pencil marking a row on roster, large exact number 十七人 visible. Names depicted abstract except friend ハル. No all-rescued marks yet.|
rail-geography|tall|120|Sky-rail prisoner carriage above cloud chasm, solid maintenance catwalk with ladder to carriage on left, secure exit gate at upper platform. Establish safe rescue route before peril. No falling carriage yet.|
inspection|wide|65|Noa crawls through underside maintenance hatch using orange gloves and simple tool, orange hair/goggles consistent. Train held stationary beside catwalk.|
unlock|portrait|70|Noa unlocks prisoner compartment from service panel; inside young adult Haru dark brown short hair green workshirt grey trousers, relieved. Single door opening, no escape complete yet.|Noa:ハル、迎えに来た。:ハル、/迎えに来た。
security-wakes|tall|70|Grey stone security guardian with purple core awakens on opposite catwalk, its foot cracks rail coupling. Ren in basic black armor stands at platform, Mira prepares ladder. No enemy defeat.|
wrong-target|portrait|55|Ren starts to leap toward guardian, fist raised, but turns head toward metallic crack behind him; red scarf trailing, no speed form. Only effect ガキン .|
carriage-falls|tall|55|Carriage joint splits and ONE occupied rear compartment tilts off sky rail; residents inside visible through window, same maintenance catwalk intact at side. Ren mid-turn not catching yet.|
change-choice|wide|70|Close Ren's determined eyes look down at falling compartment rather than enemy, raised fist opens into reaching hand.|Ren:敵より、先に！:敵より、/先に！
catch-carriage|tall|110|Ren in basic black armor grabs falling compartment UNDER its floor from braced catwalk support; feet secure against support ledge, lifts weight, seventeen captives still inside. Not floating without anchor.|
armor-peeling|portrait|90|Close Ren arm armor visibly cracking and cyan star dimming while supporting compartment; strain and clenched teeth. No new form or unlimited recharge.|Ren thought:長くは、もたない。:長くは、/もたない。
ladder|portrait|85|Mira extends locked rescue ladder from catwalk to tilted doorway, adult residents receive ladder edge; Noa holds coupling. Clear both ends secured before anyone climbs.|Mira:歩ける人は、次の人を支えて。:歩ける人は、/次の人を/支えて。
help-next|tall|110|Residents climb ladder sequentially; one adult helps small brown-haired girl yellow dress; Haru still last inside. Ren holds car underneath, Mira counts arrivals, no instant group teleport.|
last-hand|portrait|150|LAST Haru reaches from doorway and Noa catches his wrist with orange glove, other evacuees already safe behind ladder. Noa tense relief.|Noa:手を、離すな！:手を、/離すな！
all-seventeen|wide|190|Close roster with seventeen clearly separated CHECKMARKS, exact prominent total 十七人、全員 . Mira's pencil adds final mark. Show actual17 checks in one vertical line, not random unreadable names.|
release|portrait|170|Ren releases now EMPTY compartment only after everyone safe, settles to knees on intact catwalk, armor fades and he smiles breathlessly. No survivors returned into car.|Ren:…全員、いるな。:…全員、/いるな。
pass|wide|380|Haru hands Mira brass admission pass found in empty carriage; exact large engraving 英雄認定場 . No unknown villain reveal yet.|
rook-blocks|portrait|190|At exit gate Rook silver armor blue cape stands with sheathed sword blocking group. Ren unarmored kneeling stands slowly, Noa and Mira shelter17 survivors behind.|Rook:王室への反逆、という扱いになる。:王室への/反逆、という/扱いになる。''',
7:'''girl-steps|wide|80|Same brown-haired small girl yellow dress from seventeen evacuees steps from Mira's side toward Rook's lowered silver training sword at exit gate, palm open; Ren behind unarmored exhausted. Rook hesitates, no violence.|Girl:この人、私たちを出してくれた。:この人、/私たちを/出してくれた。
hand-stops|portrait|120|Close Rook's blue eyes and gloved sword hand trembling, blade points safely at ground, evacuated girl at edge of shot. Internal conflict, no instant redemption speech.|
superior|portrait|90|Older stern commander age45 short black greying hair dark navy cape silver armor with square gold collar, arrives holding stamped order sheet. Rook listens.|Commander:囚人を再収容しろ。:囚人を/再収容しろ。
princess-refuses|portrait|110|Mira steps between commander and evacuees, holds admission pass, determined. Ren and Noa hold survivors near safe wall.|Mira:王女の名で、拒みます。:王女の名で、/拒みます。
suspension|wide|100|Commander snaps royal authority seal off order chain, cold look, Mira recoils in shock but remains protective.|Commander:あなたの権限は、停止された。:あなたの/権限は、/停止された。
collapse-cue|wide|90|Grey security guardian purple core advances from damaged rail, cracks under commander boots spread into corridor, no people falling yet. Only effect ミシッ .|
collapse|tall|70|Corridor floor breaks under commander and residents at near edge, guardian arm smashing beam; Rook turns toward trapped elderly man white hair navy vest among17, Mira keeps girl away. Clear safe exit above.|
discard-order|wide|70|Close Rook drops stamped order sheet from black glove; other hand grips real rescue shield. Fallen sheet not sword, no new permit here.|
shield|portrait|100|Rook silver armor and blue cape raises steel shield over evacuees to catch rubble, leads them toward intact exit.|Rook:こっちへ！頭を下げろ！:こっちへ！/頭を下げろ！
ren-holds|tall|100|Ren in BASIC full black armor braces guardian wrist against wall to stop second collapse; cyan star weak from prior rescue, feet visible on intact section. No violent victory needed.|
rook-carries|portrait|100|Rook carries same elderly evacuee white hair navy vest on back up clear corridor, Mira leads girl, Noa guides Haru. Supports body safely.|Rook:そっちは任せる。:そっちは/任せる。
ren-answer|portrait|140|Ren looks over shoulder toward escaping Rook while maintaining guardian wrist restraint, exhausted but trusting.|Ren:任せた。:任せた。
escape|tall|190|All evacuees reach open safe lower-city service yard. Rook sets elderly man on bench; Ren last unarmored enters with dusty scarf. Commander fled other route, not saved offscreen as dead.|
apology|portrait|160|Rook bends head to seated Ren without theatrical kneeling; hands empty, remorse face. Survivors in safe yard.|Rook:見ないふりをした。謝って終わらせない。:見ないふりを/した。/謝って/終わらせない。
return-license|wide|170|Rook places his OWN silver knight license badge on rescue team's wooden table, takes plain rescue rope instead. Mira and Ren watch gesture, no restored royal authority.|
accept-work|portrait|210|Ren holds rope end toward Rook, mutual practical trust rather than instant friendship; Rook accepts.|Ren:じゃあ、次の人を一緒に。:じゃあ、/次の人を/一緒に。
invitation-cue|wide|400|Noa intercepts discarded commander's communicator at desk, pulses of cyan light, Mira leans to read. No inviter identity yet.|
invitation|portrait|200|Close simple glowing invitation on transmitter with exact horizontal text 英雄認定場 and レン様 . Ren sees his already printed name, stunned.|Ren:俺を、待ってる？:俺を、/待ってる？''',
8:'''corridor|tall|95|Ren unarmored red scarf, Mira white blue gold gown and Rook without license walk long white certification hall. Framing statues only calves and immense shadow, white hero head not visible yet.|
portrait|tall|140|FIRST full huge WHITE armored ancient hero statue with GOLD chest star, no visible living face; small red-scarf Ren below looks up. Retain unknown name, no Arata caption.|Ren:誰だ、この人。:誰だ、/この人。
first-hero|portrait|110|Thin masked ceremony guide in grey formal robe points to white statue, neutral expression. Ren Mira listen.|Guide:初代勇者です。:初代勇者/です。
compare-star|wide|150|Mira looks from statue GOLD star to Ren's faint CYAN chest point visible at scarf shirt neckline. Close bodily clue, not equal color or new form.|Mira:星の形が、同じ…。:星の形が、/同じ…。
trial-door|wide|340|Guide opens iron trial door with one key, team waits behind; targets and prisoners hidden until next scene. No later evidence text yet.|
human-targets|tall|120|FIRST trial hall reveal: living adult residents shackled upright on movable training target platforms; mechanical launchers aimed nearby. Graphic violence absent, ropes/chain clear, lives endangered. Ren shocked.|Ren:人を、的にするのか。:人を、/的にするのか。
refuse|portrait|95|Ren turns away from offered ceremonial sword, opens empty hand toward captive adults; expression controlled outrage.|Ren:こんな試験、受けない。:こんな試験、/受けない。
disqualify|wide|100|Ceremony guide pulls bell rope and points to exit with judge gesture. Bell effect カン . No attack or ren armor yet.|Guide:失格です。:失格です。
turn-back|portrait|95|Ren turns his BACK to guide and walks toward captive adult's dangling chain, bare hand already reaching. Rook and Mira prepare to assist, no full armor.|
cut-chain|portrait|100|Only Ren's black armored right forearm with cyan seam forms to protect resident as mechanism tensions chain; he breaks one chain link with gloved hand, left hand steadies resident. Other residents still chained.|
guards-run|tall|100|Grey helmeted guards run from statue shadow toward freeing team; Rook raises shield at doorway, Mira guides freed residents behind him. Not an enemy victory image.|
hold-exit|portrait|130|Rook blocks guards at narrow hall exit with shield and sheathed sword as barrier, no killing, Ren breaks remaining restraints behind.|Rook:この出口は、閉めさせない。:この出口は、/閉めさせない。
copy-evidence|wide|150|Mira copies trial recording via brass memory crystal at wall console. Exact large display text 記録保存 only; chamber and target silhouettes reflected. No huge futuristic HUD.|
their-evidence|portrait|180|Mira holds copied memory crystal in palm toward bewildered grey-robed guide; residents already walking safely behind Rook.|Mira:あなたたちの証拠です。:あなたたちの/証拠です。
rescue-outcome|portrait|200|Freed adult resident reaches outside sunlight and touches wrist where chain was; Ren unarmored helps steady them, quiet relieved empathy, no crowd applause yet.|Resident:…外だ。:…外だ。
old-inscription-cue|wide|430|During exit, Ren notices dusty letters carved low on white statue plinth behind grass, finger sweeps dust. Text still hidden under hand and dust, no future name.|
selection|wide|140|FIRST close exact carved inscription 救済は選別である on pale stone plinth, horizontal formal lettering large, no other words or speaker.|
reject-selection|portrait|210|Ren at statue base looks up with anger and resolve, unarmored scarf red against white hero shadow, Mira holds recording beside him.|Ren:誰が、そんなことを決めた。:誰が、/そんなことを/決めた。''',
9:'''workshop-return|tall|100|Rescue team back in warm workshop at night, freed residents rest on cots; Noa connects neutral magic meter near unarmored Ren, Mira holds trial memory crystal, Rook guards closed door.|
zero-again|wide|90|Close original black crystal-on-silver-pedestal meter from episode1 now at workshop bench shows exact big ０ on horizontal plaque. Ren bare hand on crystal, no armor.|
replay|portrait|130|Noa slowly replays paper/oscilloscope line: magic needle flat while cyan chest glow visible in recording. Gesture toward discrepancy, device design consistent.|Noa:針は、動いてない。:針は、/動いてない。
other-axis|portrait|140|Mira draws TWO clear simple graph axes on paper, one flat, one rises during rescuing; exact large horizontal labels 魔力 and 救助負荷 . Ren leans in, not instantly master explanation.|Mira:空じゃない。測る箱が違う。:空じゃない。/測る箱が/違う。
understand|portrait|160|Ren touches bare chest over faint cyan core, eyes widen with slow relief, red scarf moved slightly but same outfit.|Ren:ゼロでも、ここにはある。:ゼロでも、/ここには/ある。
siege|tall|95|Outside night alley, grey armored royal guards surround workshop main door and power pillar. Inside team not yet fighting, no graphic force.|
cut-power|wide|100|Guard lever cuts workshop supply cable at street fuse box, lanterns inside dim visible through window. Ordinary electrical sabotage, no future villain face.|
ventilator-stops|portrait|75|Inside simple medical alcove, OLD MAN brown vest grey beard saved in episode5 on cot uses brass bellows breathing assistance, motion slows; Mira notices distress, no death or gore.|Mira:呼吸の装置が…！:呼吸の/装置が…！
check-patient|wide|75|Ren unarmored kneels beside same elderly man with shallow breath, checks wrist while Noa pulls isolated test circuit box from shelf. No immediate success.|
isolate-circuit|portrait|100|Noa connects ONLY isolated rescue-core circuit to ventilator, physical copper leads and safety switch visible; no connection to city main grid or new form. Ren keeps one bare hand on terminal.|Noa:街の線とは、切り離す。:街の線とは、/切り離す。
give-power|tall|130|Ren concentrates faint CYAN energy from chest into isolated lead with BOTH arms UNARMORED, no full armor or attack. Bellows starts first small motion, he sacrifices combat output.|Ren:戦う力は、あとでいい。:戦う力は、/あとでいい。
rook-guard|portrait|95|Rook silver armor blue cape holds steel shield against workshop door under guards' blows, protects exhausted unarmored Ren inside. No miraculous limitless power.|
breath-cue|wide|350|Close brass ventilator bellows expands and cyan indicator starts tiny pulse, patient face still outside crop. Wait for actual breathing response, no healthy smile shown yet.|
breath-returns|portrait|190|FIRST clear elderly man inhales, chest visibly lifts under blanket, hand relaxes; Mira relieved nearby, Ren remains at powered circuit.|Mira:息が、戻った。:息が、/戻った。
small-line|wide|170|Output paper recorder draws a small unmistakably rising cyan line, Noa points with oil stained orange glove, no huge numeric gain, no upgraded gadget.|Noa:ちゃんと、届いてる。:ちゃんと、/届いてる。
signal|wide|410|Noa sees a faint stray transmission travelling out of isolated sensor toward thin separate line on city map. Do not show location label yet.|
under-palace|tall|130|FIRST reveal city map route goes into chamber DIRECTLY beneath royal palace white towers; map exact large label 王宮直下 . Mira traces destination, no fuel torture depiction.|
location|portrait|210|Mira holds traced map while Ren still powers ventilator, eyes resolved. Rook keeps protective door, Noa watches line.|Mira:ここが、消えた街区の行き先。:ここが、/消えた街区の/行き先。''',
10:'''festival|tall|120|Day festival plaza in sky city, white banners, audience faces expect celebration. Noa runs brass projector, Mira near podium, Ren unarmored red scarf nearby, Rook in plain duty armor without license. No tragedy yet.|
evidence|portrait|110|Projector beam FIRST shows silhouettes in transport conduit from episode5 and humans shackled as targets from8, recognizable records, no unreadable long caption. Audience laughter ends, concerned faces foreground.|Mira:消された人には、名前があります。:消された人には、/名前が/あります。
cut-switch|wide|90|Same older commander black greying hair navy cape from7 reaches projector power switch angrily; Noa keeps projection cable out of grasp. No arrest yet.|Commander:映像を止めろ！:映像を/止めろ！
giant-arrives|tall|80|Concealment guardian GREY stone purple core approaches projection tower behind stage and raises arm. Audience at tower base, Ren turns at low rumble. No falling result yet.|
tower-hit|wide|85|Guardian fist smashes tower support, projection light falters, steel beam bends overhead; Noa drops under control booth safely. Only effect ドゴン .|
two-choices|tall|100|Ren unarmored between damaged tower's exposed memory projector ABOVE and startled spectators BELOW leaning fall path. His gaze moves down from evidence to lives, scene geographically clear. No rescue yet.|
choice|portrait|110|Close Ren grips red scarf and starts toward trapped spectators, blue eyes resolute, a real choice before full armor.|Ren:証拠は写せる。人は戻せない。:証拠は写せる。/人は/戻せない。
run|wide|55|Ren launches toward spectators as basic black armor/cyan seams forms in motion, scarf streak follows path; no new speed form before episode12.|
catch-tower|tall|105|Ren BASIC complete black armor catches falling tower crossbeam over two crouching spectators and directs it away toward EMPTY stone patch. Clear hands support beam, legs braced, no random damage to people.|
noa-copy|portrait|95|Noa under intact kiosk plugs memory crystal duplicate into SMALL separate shop relay, old main tower abandoned. Orange hair/goggles/blue overalls, no future citywide link form.|Noa:一つ消しても、終わらない。:一つ消しても、/終わらない。
distributed|tall|160|Three DIFFERENT small shop windows down street each show same transport silhouette evidence, everyday screens powered independently. One continuous streetscape, not repeated identical panels. Citizens watch stunned; no overlay words.|
name-them|portrait|150|Mira speaks into simple brass relay microphone from safe street, copied roster in hand. Exact short dialogue preserves human names over numbers.|Mira:十七人です。一人ずつ、ここにいます。:十七人です。/一人ずつ、/ここにいます。
evacuation|tall|140|Spectators now walk OUT from under crossbeam along Mira-marked safe lane, Ren holds beam; Rook guides last small child green shirt to mother. Do not show final safe group before crossing.|
set-beam|wide|180|Ren lowers tower beam onto EMPTY marked patch after all spectators safe, cyan star fades; no enemy knockout needed. Hands tremble with exhaustion.|
first-clap|portrait|210|FIRST one ordinary adult woman in rescued audience claps cautiously while others stare in silence, Ren unarmored leaning on safe beam. No mass thunderous applause before first hand clap. Only effect パチ .|
recognized|tall|230|Broad crowd now applauds rescued exhausted Ren, Mira and Noa beside him; Ren hand to chest with surprised wet eyes, not boastful. Show concrete saved families facing him.|Ren thought:…届いたんだ。:…届いたんだ。
arrest|portrait|190|Rook restrains commander's wrist with lawful metal cuffs beside copied evidence, commander alive uninjured. Rook carries no knight license; civil witnesses nearby, no revenge violence.|Rook:今度は、見ないふりをしない。:今度は、/見ないふりを/しない。
base|portrait|230|Lower-city workshop transformed into modest official rescue base with SAME handmade plaque 救助隊 . Ren Mira Noa Rook share bread at workbench; Haru and survivors outside help repairs. Clear warm first-arc achievement.|
white-armor-cue|tall|420|Deep palace shadow, LIVING ancient hero back turned: faceted WHITE armor and GOLD star partly reflected in wall, adult short pale hair obscured face. No exact identity or name yet; quiet ominous contrast to happy base.|
close-gates|tall|220|Massive palace gates all lowering toward shut stone, white armored silhouette far above, no protagonist trapped or killed. Ominous exact dialogue from unseen white hero.|Unknown:ゼロを、上げてはいけない。:ゼロを、/上げては/いけない。'''}
TITLES={2:'英雄の請求書',3:'殴れないヒーロー',4:'姫の秘密基地',5:'消える街区',6:'十七人を運べ',7:'騎士の見たもの',8:'白い英雄の肖像',9:'ゼロの外側',10:'拍手より先に'}
STYLE='''Use case: illustration-story. Asset: FINAL anime WEBTOON single comic moment WITH speech balloons and exact Japanese vertical lettering. References are character identity, costume, armor design and anime style ONLY. Never copy reference dialogue, pose, or panel sequence. ONE distinct moment, not montage, grid, contact sheet or duplicate character sequence. Beautiful expressive Japanese anime faces, crisp linework and detailed cel shaded color. Adult Ren19: messy black hair, BLUE eyes, crimson scarf, BLACK short-sleeve shirt, charcoal trousers, brown narrow straps, BARE hands when unarmored. BASIC armor ONLY when scene requests: faceted BLACK plates, narrow CYAN seams and cyan chest STAR, face and hair uncovered, red scarf persists. NO new speed/shield/link/gate form. Adult Mira19: blonde long braid with loose bangs, blue eyes, white/royalBLUE/GOLD embroidered dress, blue-gold flower hair ornament and earrings, no blue cape. Rook22: SILVER short hair, blue eyes, SILVER engraved armor, royalBLUE cape, BLACK leather gloves. Noa18 when present: ORANGE short tousled hair, green eyes, round brass goggles ON HEAD, blue mechanic overalls, black undershirt, orange work gloves. Keep characters identifiable; vary emotion and camera by the scene. Five fingers, sensible hand/prop geometry. Dialogue is PRINTED Japanese manga gothic, upright glyphs TOP to BOTTOM, columns RIGHT to LEFT. Visible glyph height about68-76px on1024px image width, bold black on white smooth speech balloons integrated into composition. Tails clearly point to speaking mouth, thought clouds use small dots. Reshape balloons rather than make tiny text; keep faces, hands and the important prop readable. Exact text only, no labels, English, watermark or decorative extra words. Unless borderless scene specified, draw a thin smooth black comic border. Match background lighting to THIS scene, not reference sunshine in indoor/night scenes. No unknown enemy face or future revelation before requested.'''
for n,raw in RAW.items():
 directory=ROOT/f'episode-{n:02d}';(directory/'art').mkdir(parents=True,exist_ok=True)
 shots=[]
 for i,row in enumerate(raw.splitlines(),1):
  sid,crop,pause,scene,words=row.split('|')
  lines=[]
  if words:
   for entry in words.split(';'):
    speaker,text,cols=entry.split(':')
    lines.append({'speaker':speaker,'text':text,'columns':cols.split('/'),'type':'thought' if 'thought' in speaker else 'speech'})
  aspect={'wide':'1024x768','portrait':'1024x1280','tall':'1024x1792'}[crop]
  shapes={'wide':'right' if i%2 else 'left','portrait':'left' if i%2 else 'right','tall':'bleed'}
  shot={'id':sid,'file':f'{i:02d}-{sid}.png','crop':crop,'shape':shapes[crop],'aspect':aspect,'pause':int(pause),'scene':scene,'lines':lines,'status':'pending','state':scene,'pacing':'short action / reaction' if int(pause)<120 else 'understanding / recovery' if int(pause)<300 else 'wait for hidden information','hidden':'Do not reveal the event of the next shot in this image.'}
  text='\n'.join(f"Balloon {k}: {line['type']}, {line['speaker']}, {'upper right' if k==1 else 'lower left'}. EXACT text: {line['text']} . Columns RIGHT to LEFT: {' / '.join(line['columns'])}." for k,line in enumerate(lines,1))
  shot['prompt']=STYLE+f'\n\nPreferred image aspect {aspect}. Composition: '+('one tall continuous single moment, borderless dramatic vertical flow; not multiple moments or panels' if crop=='tall' else 'one close readable moment, minimal extraneous margins')+'\nScene and exact state: '+scene+'\n\n'+(text+'\nExactly '+str(len(lines))+' speech/thought balloons. No other lettering except explicitly requested effect/prop text in scene.' if lines else 'No speech/thought balloons. No lettering except the exact effect or prop inscription explicitly specified in the scene.')
  shots.append(shot)
 manifest={'episode':n,'title':TITLES[n],'version':'vertical-v1','method':'built-in image_gen','shots':shots,'revealPairs':[]}
 # Waits are narrative, not every inter-panel gap; result anchors will be visually checked.
 cues={2:('turn-fragment','workshop-number'),3:('mechanical-bird','monitor'),4:('key','workshop'),5:('voice','captives'),6:('last-hand','all-seventeen'),7:('invitation-cue','invitation'),8:('old-inscription-cue','selection'),9:('breath-cue','breath-returns'),10:('white-armor-cue','close-gates')}
 manifest['revealPairs']=[{'cue':cues[n][0],'answer':cues[n][1],'mode':'emotional wait; actual text/reveal anchors inspected after generation'}]
 (directory/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 sb=[f'# 第{n:02d}話 {TITLES[n]} — 詳細絵コンテ','',f'{len(shots)}の別々の動作・反応を縦へ読む。画像の文字は生成原画に含め、HTMLへ二重に重ねない。','', '## 連続性','', '人物・有限の救済核は ../series/bible.md を参照。第12話の速度フォームより前なので新フォームを出さない。衣服、小道具の受け渡し、救助前後の位置を各場面で固定する。','']
 for s in shots:
  sb += [f"## {s['file']} — {s['id']}", '', '見せる情報・人物の理解／感情・選択・状態：'+s['scene'],'まだ見せない情報：次の場面の結果・新人物の正体。','画面の密度：'+s['crop']+'。間：'+str(s['pause'])+'px相当、役割 '+s['pacing']+'。','次へ運ぶもの：この動作が生む視線・手・音・結果への期待。','']
  for line in s['lines']:sb += [f"- {line['speaker']}（{line['type']}）：{line['text']} / 縦列は右から左：{' / '.join(line['columns'])}"]
  if not s['lines']:sb+=['会話なし。効果音・作中の表示だけを場面指定どおり生成する。']
  sb+=['']
 (directory/'storyboard.md').write_text('\n'.join(sb).rstrip()+'\n')
 (directory/'PROMPTS.md').write_text(f'# 第{n:02d}話 {TITLES[n]} — 実行予定の作画指示\n\n方式：組み込み image_gen。実際の実行結果は generation-log.json、最終原画は art/。\n\n'+'\n\n'.join('## '+s['file']+'\n\n```text\n'+s['prompt']+'\n```' for s in shots)+'\n')
print({n:len(raw.splitlines()) for n,raw in RAW.items()})
