"""Place generated source cells into the authored reading order without editing PNGs."""
import importlib.util
import json
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = ROOT.parents[4] / 'skills/webtoon'
notes = json.loads((ROOT / 'plan-notes.json').read_text())
panels = notes['panels']
cell_windows = json.loads((ROOT / 'cell-windows.json').read_text())['sheets']
assert len(panels) == 108
panel_by_id = {p['id']: p for p in panels}
assert sorted(panel_by_id) == [f'p{i:03}' for i in range(1, 109)]
assert [p['id'] for p in panels] == notes['readingOrder']

def image_size(path):
    raw = path.read_bytes()
    assert raw[:8] == b'\x89PNG\r\n\x1a\n'
    return list(struct.unpack('>II', raw[16:24]))

def caption(text, speaker, kind='spoken', x=60, y=5, width=38):
    return dict(text=text, speaker=speaker, kind=kind, x=x, y=y, width=width, tail='down-left')

# Main scene drawings and their smaller acting/prop cuts share an authored space.
# Values are positions at 390 CSS px, not transformations of the source artwork.
groups = {
    'school-selection': [(3, 0, 0, 96), (4, 50, 400, 50)],
    'family-work': [(8, 0, 0, 90), (9, 42, 390, 58)],
    'friend-greeting': [(29, 0, 0, 92), (30, 48, 400, 52)],
    'cart-warning': [(52, 0, 0, 90), (53, 42, 430, 58)],
    'cart-jolt': [(55, 0, 0, 62), (56, 38, 285, 62)],
    'first-magic': [(75, 0, 0, 90), (76, 45, 405, 55), (77, 0, 700, 86)],
    'medicine-handoff': [(85, 0, 0, 88), (86, 48, 430, 52), (87, 0, 730, 94)],
    'real-hands': [(94, 40, 0, 60), (95, 0, 325, 74), (96, 42, 695, 58)],
}
placements = {number: dict(composition=name, offsetX=x, offsetY=y, widthPercent=width)
    for name, members in groups.items() for number, x, y, width in members}
floating = {
    4: (0, 465, 44, 225),
    9: (0, 455, 38, 220),
    30: (0, 450, 45, 170),
    76: (0, 455, 38, 220),
    96: (0, 770, 38, 240),
}
# These voices belong in the space around the drawing: the source cells do not
# reserve a balloon area, and their faces, spirit, hands and parcel carry meaning.
before_voice = {
    3: 240, 13: 320, 14: 260,
    52: 250, 54: 200, 57: 200, 58: 150, 59: 290, 60: 310, 62: 300,
    63: 260, 70: 280, 72: 250, 73: 240,
    74: 280, 79: 300, 82: 240, 84: 300, 85: 320,
    97: 180, 99: 280, 100: 180, 101: 250, 102: 220, 103: 240, 104: 180, 108: 200,
}
gaps = {
    4: (110, '選抜を受けた航の沈黙から チームが先へ行く背中へ移る'),
    6: (180, '道場を出た結果から 家の弁当店へ場所をつなぐ'),
    12: (90, '中古の機器への期待を受け止め 母へ自分の選択を話す'),
    16: (220, '九時の約束を持って 部屋で自分から接続する'),
    19: (70, '接続操作からすぐ視界の変化へ入り 期待の勢いを保つ'),
    97: (40, '部屋の光片から接続の大きな光流へ一気につなぐ'),
    98: (200, '光流の終わりを受けて初回の歓迎へ落ち着く'),
    99: (40, '名前の案内へ本人がすぐ返す'),
    100: (45, '名の選択から初めて動かす手へ移る'),
    101: (30, '案内から握る動作へ応答を近く置く'),
    102: (60, '身体の応答を喜んで世界へ入る準備へ進む'),
    103: (45, '本人の指の選択から次の光が開く'),
    104: (180, '強い光が草と風に変わり匂いが先に届く'),
    105: (50, '風と近くの花から目を落として水の光を見る'),
    106: (70, '足元の水から遠くの川と暮らしへ視線を伸ばす'),
    107: (80, '遠景を見た航の喜びを受け止める'),
    108: (150, '世界に見とれる航へ友人の声が届く'),
    23: (80, '身体の確認を終え 頭上の影へ気づく'),
    25: (360, '羽音を聞いて見上げたあと 空の最初の光をまだ見せない'),
    26: (720, '瞳の小さな星環の手掛かりから 全景の竜と空を待つ'),
    27: (170, '空の大きさを受け止める航の反応へ戻る'),
    28: (120, '空を見た余韻の中へ 友人の声が届く'),
    33: (90, '空を見た表情から 手元の小さな地図へ焦点を移す'),
    40: (140, '灯里の訓練へ行く選択を受け 航が自分の道を選ぶ'),
    41: (180, '別れた道から 町へ向かう道の全景へつなぐ'),
    48: (100, '剣を収めて歩くところへ 人の声が先に届く'),
    59: (210, '薬箱を安全な道へ戻したあと 息が落ち着くまで待って礼と名前を聞く'),
    64: (160, '町へ同行する足取りから 同じ橋の水へ目を落とす'),
    71: (170, '使える道具への理解から 精霊の意志がある暮らしへ移る'),
    74: (120, '待つ職人の姿から 航自身が形を試す場面へつなぐ'),
    77: (380, '小さな練習を終え 町全体へ視線を開く'),
    81: (150, '今晩の必要を受け止め 役に立ちたい航が引き受ける'),
    83: (150, '日本の時刻を見た航が 断る言葉を選ぶために待つ'),
    91: (660, '明日の返答を受け 異世界の音を終え日本へ帰る'),
    93: (130, 'ただいまの返事のあと 九時に戻った結果を確認する'),
}

beats = []
layout_notes = []
def voice(beat_id, text, speaker, height, purpose, **position):
    beats.append(dict(id=beat_id, type='voice', text=text, speaker=speaker,
        height=height, purpose=purpose, **position))

for panel_index, p in enumerate(panels):
    number = int(p['id'][1:])
    sheet = ROOT / 'rough' / f"sheet-{p['sheet']:02}.png"
    width, height = image_size(sheet)
    col = (p['slot'] - 1) % 3
    row = (p['slot'] - 1) // 3
    windows = cell_windows[str(p['sheet'])]
    x0, x1 = (windows['columnsByRow'][row] if 'columnsByRow' in windows else windows['columns'])[col]
    y0, y1 = windows['rows'][row]
    assert 0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height
    source = p['propState']
    dialogue = []
    sounds = []
    for d in p['dialogue']:
        if d['kind'] == 'sound':
            sounds.append(dict(text=d['text'], x=27, y=74))
        elif d['kind'] == 'speech-pair':
            voice('mother-welcome', 'おかえり', '美和（階下）', 230,
                '日本へ戻った航へ母の声だけが届き ただいまの返事を下へ残す')
            dialogue.append(caption('ただいま', '航', x=63, width=33))
        else:
            text = d['text']
            if number == 13:
                text = 'それが\n灯里ちゃんの言ってた\nゲーム？'
            if d['kind'] == 'display':
                if number == 34:
                    text = 'エルセリア\nミルト'
                if number == 83:
                    text = '日本時間\n20:50'
                if number == 90:
                    text = '安全拠点 ミルト\nログアウト'
            kind = 'thought' if d['kind'] in ('thought', 'display', 'narration') else 'spoken'
            dialogue.append(caption(text, d['speaker'], kind))
    for s in p['sounds']:
        if s.get('mode') == 'continuation':
            continue
        if s['text'] and s['text'] not in [x['text'] for x in sounds]:
            sounds.append(dict(text=s['text'], x=25, y=78))
    if number == 24:
        sounds = [dict(text='バサ', x=24, y=66)]
    if number == 65:
        sounds = [dict(text='サァ', x=23, y=71)]
    if number == 20:
        voice('first-scent', '……草の匂い', '航（心）', 310,
            '姿より先に草の匂いを受け 草の手触りを下へ残す')
        dialogue = []
    if number == 49:
        voice('cart-call', 'そこ少し\n空けてもらえる？', '道の先から声', 230,
            '荷車もリゼの姿も出す前に声を届け 航の振り向きを下へ残す')
        dialogue = []
    if number in before_voice:
        for index, d in enumerate(dialogue):
            voice(f'{p["id"]}-voice-{index}', d['text'], d['speaker'], before_voice[number],
                p['purpose'] + '。声を上へ出し、直下の顔・手・精霊・薬を守る')
        dialogue = []
    shape = p['widthShape']
    panel_width = {'full': 96, 'wide': 96, 'medium': 88, 'narrow': 68}.get(shape.get('width'), 90)
    if dialogue:
        panel_width = max(panel_width, 92)
    # Only short eye/prop reactions use a narrow standalone crop.
    if number in (26, 43, 46, 51):
        panel_width = 68 if dialogue else 58
        if number == 51:
            dialogue[0].update(x=26, width=70, y=4)
    panel = dict(id=p['id'], type='panel', image=f'rough/{sheet.name}',
        alt=p['purpose'] + '。' + ' / '.join(d['speaker'] + '：' + d['text'].replace('\n', ' ') for d in p['dialogue']),
        crop=[x0 / width, y0 / height, (x1 - x0) / width, (y1 - y0) / height],
        imageSize=[width, height], widthPercent=panel_width,
        align=shape.get('placement') if shape.get('placement') in ('left', 'right', 'center') else 'center',
        frame='none', purpose=p['purpose'], dialogue=dialogue, sounds=sounds)
    if number == 27:
        panel.update(image='rough/sky-discovery.png', imageSize=image_size(ROOT / 'rough/sky-discovery.png'),
            crop=None, widthPercent=100, align='center')
    if number == 98:
        panel.update(image='rough/connection-dive.png', imageSize=image_size(ROOT / 'rough/connection-dive.png'),
            crop=None, widthPercent=100, align='center', sounds=[dict(text='シュアアア', x=43, y=83)])
    if number in (97, 104, 105, 107):
        panel.update(widthPercent=100, align='center')
    if number in (100, 101, 102, 106, 108):
        panel.update(widthPercent=74 if number == 101 else 82, align='left' if number in (100, 106) else 'right')
    if number == 105:
        panel['sounds'] = [dict(text='そよ…', x=55, y=76)]
    if number == 106:
        panel['sounds'] = [dict(text='パシャ', x=58, y=68)]
    if number == 58:
        panel.update(widthPercent=100, align='center')
        panel['sounds'] = [dict(text='ガシッ', x=68, y=75)]
    if number == 55:
        panel['sounds'] = [dict(text='ガタン！', x=48, y=79)]
    if number == 56:
        panel['sounds'] = [dict(text='ブツッ', x=60, y=30)]
    if number == 59:
        panel['sounds'] = [dict(text='ズッ', x=24, y=82)]
    if number in placements:
        panel.update(placements[number])
    if number == 30:
        panel['dialogue'][0].update(x=22, width=75, y=3)
    if number in floating:
        panel['dialogue'] = []
    if number == 61:
        panel.update(composition='name-after-work', offsetX=0, offsetY=0, widthPercent=88, dialogue=[])
    if number == 77:
        panel['dialogue'] = []
    if number == 90:
        voice('return-promise', '明日\n日暮れ前に来る！', '航', 250,
            '時計を確かめた航が来る時刻を自分で決め リゼの聞く表情を下へ残す')
        panel['dialogue'] = []
    beats.append(panel)
    if number in floating:
        x, y, w, h = floating[number]
        for index, d in enumerate(dialogue):
            voice(f'{p["id"]}-thought-{index}', d['text'], d['speaker'], h, p['purpose'],
                composition=panel['composition'], offsetX=x, offsetY=y, widthPercent=w, x=50, y=50)
    if number == 61:
        for index, d in enumerate(dialogue):
            voice(f'p061-name-{index}', d['text'], d['speaker'], 280, p['purpose'],
                composition='name-after-work', offsetX=62, offsetY=455, widthPercent=36)
    if number == 77:
        for index, d in enumerate(dialogue):
            voice(f'p077-practice-{index}', d['text'], d['speaker'], 290, p['purpose'],
                composition='first-magic', offsetX=50, offsetY=1100, widthPercent=50)
    if number == 25:
        beats.append(dict(id='wing-tail', type='sound', text='ァ…', speaker='', height=250,
            x=34, y=43, purpose='p024のバサから続く同じ一つの羽音の末尾 空の全景はまだ出さない'))
    if number == 66:
        beats.append(dict(id='water-tail', type='sound', text='ァ…', speaker='', height=300,
            x=26, y=35, purpose='p065のサァから同じ水音を橋と洗った手の外へ続け 次の会話の前で終える'))
    if number == 90:
        voice('safe-logout-ui', '安全拠点 ミルト\nログアウト', '航だけに見える表示', 260,
            '帰る場所と操作を確認する 直後のリゼの返答を先に見せない')
    if number in gaps:
        gap_height, reason = gaps[number]
        beats.append(dict(id=f'pause-{p["id"]}', type='pause', height=gap_height, purpose=reason))
    elif panel_index < len(panels) - 1 and number not in placements and number not in (19, 25, 66):
        if panels[panel_index + 1]['scene'] == p['scene']:
            gap_height = 45 if p['dialogue'] else 24
            beats.append(dict(id=f'breath-{p["id"]}', type='pause', height=gap_height,
                purpose='同じ場所の短い動作と応答を近くで読み 次の対象へ視線を渡す'))
    layout_notes.append(dict(id=p['id'], source=panel['image'], slot=p['slot'], crop=panel['crop'],
        sourcePixelWindow=None if number in (27, 98) else [x0, y0, x1, y1],
        placement={k: panel[k] for k in ('widthPercent', 'align', 'frame', 'composition', 'offsetX', 'offsetY') if k in panel},
        propState=source, newInformation=p['purpose']))

manifest = dict(schema='webtoon-name-preview/v1', title='星環のレガリア 第1話 補欠の空',
    referenceWidth=390, beats=beats)
(ROOT / 'plan.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'source-layout.json').write_text(json.dumps(layout_notes, ensure_ascii=False, indent=2) + '\n')
spec = importlib.util.spec_from_file_location('name_preview', SKILL / 'scripts/build_name_preview.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.build_preview(ROOT / 'plan.json', ROOT / 'index.html', force=True)
# Give the rough name expressive balloons without altering the generated PNGs.
def tone_for(beat):
    number = re.match(r'p(\d{3})', beat['id'])
    source = panel_by_id.get('p' + number[1]) if number else None
    if beat['id'] in ('first-scent',):
        return 'thought'
    if beat['id'] == 'cart-call':
        return 'normal'
    if beat['id'] == 'safe-logout-ui':
        return 'interface'
    if beat['id'] == 'return-promise':
        return 'bright'
    if beat['id'] == 'mother-welcome':
        return 'warm'
    if source:
        for d in source['dialogue']:
            if d['kind'] != 'sound':
                return d.get('tone', 'normal')
    return 'normal'

extra = '''<style>
.dialogue-speaker,.floating-speaker {display:none}
[data-balloon-tone] {--ink:#404040;--paper:#ffffff;--edge:1.7px}
.voice-copy {color:#292929;position:relative;z-index:2;white-space:nowrap}
.dialogue-text {position:relative;z-index:2;color:#292929}
.balloon {background:var(--paper);border:var(--edge) solid var(--ink);box-shadow:none}
.spoken .balloon::after {background:var(--paper);border-color:var(--ink)}
.voice[data-balloon-tone] .floating-copy {padding:17px 19px;background:var(--paper);
  border:var(--edge) solid var(--ink);border-radius:48% / 34%;isolation:isolate}
.voice[data-balloon-tone] .floating-copy::after {content:"";position:absolute;
  width:13px;height:15px;bottom:-10px;left:30%;background:var(--paper);
  border-right:var(--edge) solid var(--ink);border-bottom:var(--edge) solid var(--ink);
  transform:rotate(35deg) skew(-10deg);z-index:-1}
[data-balloon-tone="warm"],[data-balloon-tone="relief"] {--paper:#f3f3f3;--ink:#7d7d7d;--edge:1.4px}
[data-balloon-tone="warm"] .balloon,[data-balloon-tone="relief"] .balloon,
.voice[data-balloon-tone="warm"] .floating-copy,.voice[data-balloon-tone="relief"] .floating-copy
  {border-radius:44% 53% 41% 48% / 40% 36% 45% 41%}
[data-balloon-tone="bright"] {--paper:#f6f6f6;--ink:#757575}
[data-balloon-tone="curious"] {--paper:#f5f5f5;--ink:#6c6c6c}
[data-balloon-tone="curious"] .balloon,.voice[data-balloon-tone="curious"] .floating-copy
  {border-radius:25px 31px 26px 28px}
[data-balloon-tone="thought"] {--paper:#f1f1f1;--ink:#686868;--edge:1.4px}
[data-balloon-tone="thought"] .balloon,.voice[data-balloon-tone="thought"] .floating-copy
  {border-style:dashed;border-radius:42% 39% 44% 40% / 39% 47% 37% 46%}
[data-balloon-tone="thought"] .balloon::after,.voice[data-balloon-tone="thought"] .floating-copy::after
  {content:"• •";width:auto;height:auto;bottom:-27px;left:20%;background:none;
   border:none;color:var(--ink);font-size:18px;transform:rotate(25deg);z-index:0}
[data-balloon-tone="alarm"],[data-balloon-tone="rally"],[data-balloon-tone="strain"]
  {--paper:#f3f3f3;--ink:#545454;--edge:2.5px}
[data-balloon-tone="rally"] {--paper:#f2f2f2;--ink:#707070}
[data-balloon-tone="alarm"] .balloon,[data-balloon-tone="rally"] .balloon,[data-balloon-tone="strain"] .balloon,
.voice[data-balloon-tone="alarm"] .floating-copy,.voice[data-balloon-tone="rally"] .floating-copy,
.voice[data-balloon-tone="strain"] .floating-copy
  {border:0;background:none;padding:26px 28px;border-radius:0;isolation:isolate}
[data-balloon-tone="alarm"] .balloon::before,[data-balloon-tone="rally"] .balloon::before,[data-balloon-tone="strain"] .balloon::before,
.voice[data-balloon-tone="alarm"] .floating-copy::before,.voice[data-balloon-tone="rally"] .floating-copy::before,
.voice[data-balloon-tone="strain"] .floating-copy::before,
[data-balloon-tone="alarm"] .balloon::after,[data-balloon-tone="rally"] .balloon::after,[data-balloon-tone="strain"] .balloon::after,
.voice[data-balloon-tone="alarm"] .floating-copy::after,.voice[data-balloon-tone="rally"] .floating-copy::after,
.voice[data-balloon-tone="strain"] .floating-copy::after
  {content:"";position:absolute;inset:0;width:auto;height:auto;border:0;transform:none;
   border-radius:0;z-index:-1;background:var(--ink);
   clip-path:polygon(50% 0,58% 8%,69% 2%,72% 13%,85% 9%,84% 22%,97% 22%,91% 35%,100% 43%,93% 51%,100% 61%,88% 66%,93% 80%,80% 81%,82% 94%,67% 89%,61% 100%,50% 93%,38% 100%,32% 89%,18% 95%,19% 81%,6% 81%,12% 66%,0 61%,8% 50%,0 40%,10% 34%,3% 22%,17% 21%,15% 9%,29% 13%,33% 2%,42% 8%)}
[data-balloon-tone="alarm"] .balloon::after,[data-balloon-tone="rally"] .balloon::after,[data-balloon-tone="strain"] .balloon::after,
.voice[data-balloon-tone="alarm"] .floating-copy::after,.voice[data-balloon-tone="rally"] .floating-copy::after,
.voice[data-balloon-tone="strain"] .floating-copy::after {inset:3px;background:var(--paper)}
[data-balloon-tone="interface"] .balloon,.voice[data-balloon-tone="interface"] .floating-copy
  {border-radius:6px;border:1px solid #7f7f7f;background:#f8f8f8}
[data-balloon-tone="interface"] .balloon::after,.voice[data-balloon-tone="interface"] .floating-copy::after,
[data-balloon-tone="narration"] .balloon::after,.voice[data-balloon-tone="narration"] .floating-copy::after {display:none}
[data-balloon-tone="narration"] .balloon,.voice[data-balloon-tone="narration"] .floating-copy
  {border:0;border-radius:0;background:white}
.sfx {color:#222222}
#preview-flow {filter:grayscale(1)}
</style>'''
html = (ROOT / 'index.html').read_text()
for beat in beats:
    if beat['type'] in ('panel', 'voice'):
        old = f'data-beat-id="{beat["id"]}"'
        html = html.replace(old, old + f' data-balloon-tone="{tone_for(beat)}"')
(ROOT / 'index.html').write_text(html.replace('</head>', extra + '</head>'))
print(f'Wrote standalone preview with {len(panels)} source cuts and {len(beats)} reading elements')
