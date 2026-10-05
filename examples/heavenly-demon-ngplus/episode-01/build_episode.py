#!/usr/bin/env python3
"""Typeset the original anime Webtoon without modifying generated artwork."""
from pathlib import Path
import html
import json
import struct

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "episode.json").read_text())
ASSETS = {item["id"]: item for item in DATA["artwork"]}
GRAPHICS = json.loads((ROOT / "lettering.json").read_text())["assets"]
BLOCKS = []


def text(line, kind="thought", align="left", ident=""):
    element_id = f' id="{ident}"' if ident else ""
    BLOCKS.append(f'<div class="lettering {kind} {align}"{element_id}><p>{line}</p></div>')


def pause(size, purpose):
    BLOCKS.append(f'<div class="pause" style="height:{size}cqw" data-purpose="{purpose}" aria-hidden="true"></div>')


def art(key, start=0, end=1, ident=None):
    item = ASSETS[key]
    raw = (ROOT / item["src"]).read_bytes()
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Expected original PNG: {item['src']}")
    width, height = struct.unpack(">II", raw[16:24])
    first, last = round(start * height), round(end * height)
    if not 0 <= first < last <= height:
        raise ValueError("Invalid art window")
    span = last - first
    source = html.escape(item["src"], quote=True)
    alt = html.escape(item["alt"], quote=True)
    scene_id = ident or key
    BLOCKS.append(f'<figure class="scene" id="{scene_id}" data-source="{source}" '
                  f'data-window="{first}:{last}"><div class="art-window" '
                  f'style="aspect-ratio:{width}/{span}"><img src="{source}" '
                  f'width="{width}" height="{height}" alt="{alt}" '
                  f'style="object-position:50% {(first/(height-span)*100 if height != span else 0):.6f}%" '
                  f'decoding="sync"></div></figure>')


def graphic(key, align="center", ident=""):
    item = GRAPHICS[key]
    raw = (ROOT / item["src"]).read_bytes()
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Expected original PNG graphic: {item['src']}")
    width, height = struct.unpack(">II", raw[16:24])
    element_id = ident or key
    source, alt = html.escape(item["src"], quote=True), html.escape(item["alt"], quote=True)
    BLOCKS.append(f'<figure class="graphic {item["kind"]} {align}" id="{element_id}">'
                  f'<img src="{source}" width="{width}" height="{height}" alt="{alt}" '
                  f'decoding="sync"></figure>')


text("目を開けたら、<br>知らない場所で縛られていた。", "narration")
pause(3, "読者と主人公が同じ情報量で危機へ入る")
text("雑役弟子ハン・ユン。<br>禁庫荒らしの罪で、死刑。", "speech", "right")
art("execution", 0, .587, "execution-wide")
text("ハン・ユン？<br>……誰のことだ。", ident="disorientation")
art("execution", .593, .748, "bound-wrists")
text("縄が、食い込む。<br>膝の下の石が、冷たい。")
pause(9, "身体の痛みを読んでから、恐怖の顔を見る")
art("execution", .754, 1, "frightened-eyes")
text("待って。<br>俺、何も……！", "speech")
text("最期まで、<br>見苦しい。", "speech", "right")
pause(28, "訴えが届かないことを受け止める")
text("聞いてくれない。")
pause(26, "日常の記憶への呼吸")
text("昨日まで、ただの学生だった。", "narration")
text("授業のあと、帰ってゲーム。<br>それだけの一日だった。")
art("previous-life")
text("三千時間遊んだ『九天』。<br>やっと、最後の敵を倒した。", "narration")
text("画面が、真っ白になって——。", "narration", "right")
pause(48, "記憶と現在をつなぐ。転生を即座に受け入れない")
text("夢、だよな。<br>目を閉じれば……。")
pause(22, "夢であってほしいという否認")
text("でも、手首の痛みは消えない。")
pause(28, "痛みから、生きたいという目的へ")
text("帰らなきゃ。<br>こんなところで、<br>死にたくない。", ident="want-home")
graphic("ui-transfer")
text("ハン・ユン……。<br>ゲームで、序盤に死ぬ奴だ。")
text("冤罪で処刑される。<br>俺はそれを、画面で見ていた。")
pause(20, "既知のゲームと、生身の危機が結びつく")
text("俺が、あいつに……？")
text("待て。どうして、<br>文字が見えるんだ？")
graphic("ui-inherit")
pause(18, "表示を信じる前に、自分の記録か確かめる")
text("LV.999……？<br>俺のセーブデータだ。")
art("awakening")
text("指先に、<br>少し力を入れただけだった。")
text("……縄が、切れた。", ident="strength-test")
pause(30, "自分の体の変化に戸惑う")
text("強くてニューゲーム……？")
text("そんな表示、信じていいのか。<br>こっちは本当に痛いんだぞ。")
pause(16, "理解し終わる前に刃が迫る")
text("死ね。", "speech", "right")
art("descending-sword")
text("この構え……。<br>三十七回、負けて覚えた。")
text("次は、右上から。")
text("考えるより先に、<br>手が動いた。")
text("お願いだ。<br>止まってくれ。", "thought", "left", "catch-cue")
pause(215, "止まる保証のない祈りから結果を一画面以上先へ。刃が迫る主観時間")
graphic("sfx-stop", "right")
art("two-fingers")
text("……は？", "speech", "right")
text("……止まった。")
text("指、痛くない。<br>本当に、俺の手か？", ident="catch-disbelief")
pause(22, "本人にも意外だった成功を受け止める")
text("もう、<br>やめてください。", "speech")
text("離せッ！", "speech", "right")
text("また刃が、動く。<br>離したら、首に届く。")
graphic("sfx-grip", "left")
art("shatter", 0, .319, "grip-blade")
text("離せない。")
graphic("sfx-crack", "left")
art("shatter", .327, .573, "falling-shards")
graphic("sfx-break", "right")
art("shatter", .581, 1, "elder-fear")
text("……力、入れすぎた？")
text("俺の……<br>名剣が……", "speech", "right")
pause(18, "剣が壊れたことに本人も戸惑う")
text("待って。<br>話を——", "speech")
text("黙れ、雑役！", "speech", "right")
art("counter-bridge", 0, .635, "elder-lunge")
text("武器はもう、ないのに。<br>まだ、殺す気だ。")
art("counter-bridge", .643, 1, "defensive-palm")
text("やめろ！", "speech")
text("頭じゃなく、<br>体が知っていた。", "narration")
graphic("technique")
art("one-palm")
pause(55, "力の大きさを本人と読者が受け止める")
text("……え？")
art("aftermath", 0, .726, "fallen-elder")
text("……生きて、るよな？", "speech")
text("ぐっ……<br>貴様……何者だ……。", "speech", "right")
pause(30, "返事で相手の生存が分かってから、自分の手を見る")
art("aftershock", 0, .608, "shaking-hand")
text("押し返しただけ、なのに。")
pause(28, "勝ち誇る前に、自分の力を怖がる時間")
art("aftershock", .615, 1, "relieved-face")
text("こわかった。", ident="aftershock-thought")
pause(28, "無言の表情と身体の反応で生還を感じる")
text("今になって、<br>手が震えてきた。")
text("……助かった。", "speech")
pause(35, "生きている安堵を、周囲の称賛より先に置く")
art("aftermath", .732, 1, "crowd-reaction")
text("あの雑役が……<br>長老を、一撃で？", "speech", "right")
graphic("ui-reward")
text("内功、百二十年……？<br>それって、どれくらいだ。")
pause(30, "報酬と、実際に生き残った感覚を整理する")
text("足が、まだ震える。<br>でも——生きてる。")
pause(35, "この世界を受け入れるには、まず一つの目的だけ")
text("まずは、生きる。<br>帰り道は、俺が探す。", "final-line", "center", "first-goal")
pause(55, "最初の生還の余韻を、次の謎の前に置く")
text("そのとき、<br>遠い禁庫から、音がした。", "narration")
graphic("sfx-ring", "center", "sword-cue")
pause(48, "姿は見せず、耳を澄ませる")
text("……俺を、呼んでる？")
pause(85, "第1話は生還で閉じ、剣の姿と臣従は第2話へ")

CSS = """
*{box-sizing:border-box}html{background:#eceff2;color:#17222e;color-scheme:light}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Sans','Yu Gothic',sans-serif}
.episode{width:100%;max-width:480px;margin:0 auto;background:#fff;container-type:inline-size}
header{padding:24px 8% 24px;text-align:left}
.eyebrow{font-size:11px;letter-spacing:.14em;color:#627d89;margin:0 0 8px}
h1{font-family:'Hiragino Mincho ProN','Yu Mincho',serif;font-size:clamp(36px,10.4cqw,48px);font-weight:900;line-height:1.25;margin:0 0 12px;letter-spacing:.02em}
h1 span{color:#a88130}.subtitle{font-size:13px;line-height:1.6;margin:0}.scroll-hint{font-size:11px;color:#7b8b96;margin:10px 0 0;letter-spacing:.15em}
.scene{position:relative;margin:0;width:100%}
.art-window{position:relative;width:100%;overflow:clip}
.art-window img{display:block;position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover}
.lettering{padding:18px 8%;margin:0;font-size:clamp(19px,5.12cqw,23px);line-height:1.75;letter-spacing:.02em;min-height:65px}
.lettering p{margin:0;max-width:100%}
.right{display:flex;justify-content:flex-end}.center{text-align:center}
.thought p{display:inline-block;border-left:2px solid #a8c4c9;padding:3px 0 3px 14px}
.narration{font-weight:700;padding-top:16px;padding-bottom:16px}
.speech p{display:inline-block;border:1.5px solid #273a46;border-radius:50%;padding:17px 28px;text-align:center;background:#fff;line-height:1.65;font-weight:600}
.pause{width:100%;background:#fff}
.graphic{position:relative;display:block;padding:0;text-align:initial}
.graphic img{display:block;width:100%;height:auto}
.status-art{width:94%;margin:22px 3%}
.sfx-art{width:58%;margin:10px 8%}
.sfx-art.center{margin:10px auto}.sfx-art.right{margin-left:auto}
.technique-art{width:90%;margin:12px auto 22px}
.final-line{font-family:'Hiragino Mincho ProN','Yu Mincho',serif;font-weight:900;font-size:clamp(27px,8cqw,38px);line-height:1.9;color:#17262c;padding:24px 6%}
footer{text-align:center;border-top:1px solid #e1e8e9;padding:44px 8% 65px;color:#405969}
footer p{font-size:19px;line-height:1.8;margin:0 0 13px}footer small{font-size:11px;letter-spacing:.12em}
"""
document = f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#ffffff"><title>{DATA['title']}｜{DATA['subtitle']}</title><style>{CSS}</style></head>
<body><main class="episode"><header><p class="eyebrow">異世界転生 × 武侠 × 強くてニューゲーム</p>
<h1>天魔、<br><span>二周目。</span></h1><p class="subtitle">第1話｜処刑する相手、間違えてるぞ</p><p class="scroll-hint">下へスクロール ↓</p></header>
{''.join(BLOCKS)}<footer><p>第1話　完</p><p>次回「その剣は、俺を知っている」</p><small>天魔、二周目。 ／ ORIGINAL WEBTOON</small></footer></main></body></html>'''
(ROOT / "index.html").write_text(document, encoding="utf-8")
print(ROOT / "index.html")
