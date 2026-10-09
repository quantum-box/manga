"""Place generated source cells into the authored reading order without editing PNGs."""
import importlib.util
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = Path.home() / '.codex/skills/webtoon'
notes = json.loads((ROOT / 'plan-notes.json').read_text())
panels = notes['panels']
assert len(panels) == 96
assert [p['id'] for p in panels] == [f'p{i:03}' for i in range(1, 97)]

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
    'cart-second-attempt': [(52, 0, 0, 90), (53, 18, 430, 82),
        (54, 0, 795, 100), (55, 0, 1230, 62), (56, 28, 1530, 72)],
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
    52: 250, 57: 220, 63: 260, 70: 280, 72: 250, 73: 240,
    74: 280, 79: 300, 82: 240, 84: 300, 85: 320,
}
gaps = {
    4: (110, '選抜を受けた航の沈黙から チームが先へ行く背中へ移る'),
    6: (180, '道場を出た結果から 家の弁当店へ場所をつなぐ'),
    12: (90, '中古の機器への期待を受け止め 母へ自分の選択を話す'),
    16: (220, '九時の約束を持って 部屋で自分から接続する'),
    19: (310, '接続操作のあとに 部屋が消える静けさを置く'),
    23: (80, '身体の確認を終え 頭上の影へ気づく'),
    25: (360, '羽音を聞いて見上げたあと 空の最初の光をまだ見せない'),
    26: (720, '瞳の小さな星環の手掛かりから 全景の竜と空を待つ'),
    27: (170, '空の大きさを受け止める航の反応へ戻る'),
    28: (120, '空を見た余韻の中へ 友人の声が届く'),
    33: (90, '空を見た表情から 手元の小さな地図へ焦点を移す'),
    40: (140, '灯里の訓練へ行く選択を受け 航が自分の道を選ぶ'),
    41: (180, '別れた道から 町へ向かう道の全景へつなぐ'),
    48: (100, '剣を収めて歩くところへ 人の声が先に届く'),
    59: (160, '荷車が落ち着いたあと 助かった相手の息と名乗りを受ける'),
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

for p in panels:
    number = int(p['id'][1:])
    sheet = ROOT / 'rough' / f"sheet-{p['sheet']:02}.png"
    width, height = image_size(sheet)
    col = (p['slot'] - 1) % 3
    row = (p['slot'] - 1) // 3
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
        crop=[col / 3 + .0045, row / 4 + .0045, 1 / 3 - .009, 1 / 4 - .009],
        imageSize=[width, height], widthPercent=panel_width,
        align=shape.get('placement') if shape.get('placement') in ('left', 'right', 'center') else 'center',
        frame='none', purpose=p['purpose'], dialogue=dialogue, sounds=sounds)
    if number == 27:
        panel.update(image='rough/sky-discovery.png', imageSize=image_size(ROOT / 'rough/sky-discovery.png'),
            crop=None, widthPercent=100, align='center')
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
        voice('return-promise', '明日\n日暮れ前に来る', '航', 250,
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
    elif number < 96 and number not in placements and number not in (19, 25, 66):
        if panels[number]['scene'] == p['scene']:
            gap_height = 45 if p['dialogue'] else 24
            beats.append(dict(id=f'breath-{p["id"]}', type='pause', height=gap_height,
                purpose='同じ場所の短い動作と応答を近くで読み 次の対象へ視線を渡す'))
    layout_notes.append(dict(id=p['id'], source=panel['image'], slot=p['slot'], crop=panel['crop'],
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
# Scope-specific styling only: expose speaker through semantics, spare balloon width for words.
extra = '''<style>
.dialogue-speaker {display:none}
.voice-copy {color:#27333a}
.balloon {background:#fff;box-shadow:none}
[data-beat-id="p001"] .balloon,[data-beat-id="p011"] .balloon,
[data-beat-id="p019"] .balloon,[data-beat-id="p034"] .balloon,
[data-beat-id="p051"] .balloon,[data-beat-id="p083"] .balloon {border-radius:5px;border:1px solid #50616a}
[data-beat-id="p001"] .balloon::after,[data-beat-id="p011"] .balloon::after,
[data-beat-id="p019"] .balloon::after,[data-beat-id="p034"] .balloon::after,
[data-beat-id="p051"] .balloon::after,[data-beat-id="p083"] .balloon::after {display:none}
.sfx {color:#222}
</style>'''
html = (ROOT / 'index.html').read_text()
(ROOT / 'index.html').write_text(html.replace('</head>', extra + '</head>'))
print(f'Wrote standalone preview with {len(panels)} source cuts and {len(beats)} reading elements')
