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


text("目を開けたら、<br>処刑場だった。", "narration")
pause(3, "危機へすぐ入る")
text("雑役弟子ハン・ユン。<br>禁庫荒らしの罪で、死刑。", "speech", "right")
art("execution", 0, .587, "execution-wide")
text("最期まで、<br>目障りな目だな。", "speech", "right")
art("execution", .593, .748, "bound-wrists")
pause(7, "手から目への短い視線移動")
art("execution", .754, 1, "calm-eyes")
text("……待て。<br>この道場、見たことがある。")
pause(48, "回想への呼吸")
text("俺は武侠ゲーム『九天』を、<br>三千時間やり込んだ。", "narration")
art("previous-life")
text("最後のボスを倒した、<br>その瞬間——。", "narration", "right")
pause(58, "白い光から異世界へ移る")
text("……この世界、知ってる。")
graphic("ui-transfer")
pause(30, "最弱の身分を読んでから引き継ぎを示す")
graphic("ui-inherit")
art("awakening")
text("ああ。<br>強くてニューゲームか。", "speech")
pause(25, "自信を受け止めてから敵の攻撃")
text("死ね。", "speech", "right")
art("descending-sword")
text("こいつは、序盤の中ボス。")
text("覚えてる。<br>三十七回、倒した。", "thought", "left", "catch-cue")
pause(248, "斬撃を追う期待。止めた結果を一画面以上先で初めて見せる")
graphic("sfx-stop", "right")
art("two-fingers")
text("……は？", "speech", "right")
text("その技。<br>二段目まで遅いんだよ。", "speech")
pause(14, "止まった指の余裕")
graphic("sfx-grip", "left")
art("shatter", 0, .319, "grip-blade")
graphic("sfx-crack", "left")
art("shatter", .327, .573, "falling-shards")
graphic("sfx-break", "right")
art("shatter", .581, 1, "elder-fear")
text("俺の……<br>名剣が……", "speech", "right")
pause(20, "敵の恐怖から主人公の返答")
text("これ、返すぞ。", "speech")
pause(34, "掌打の直前")
graphic("technique")
art("one-palm")
pause(24, "一撃の余韻")
text("一発で、終わり。", "speech")
pause(34, "勝利が確定してから周囲の反応")
art("aftermath")
text("あの雑役が……<br>長老を、一撃で？", "speech", "right")
graphic("ui-reward")
pause(78, "戦利品を味わう。次の異変はまだ見せない")
text("……ん？")
pause(54, "視線を遠い禁庫へ運ぶ")
text("禁庫の奥から、<br>剣が鳴いた。", "narration")
graphic("sfx-ring", "center", "sword-cue")
pause(248, "音の発生源を探す。伝説の黒剣はこの下で初登場")
art("sword-bows")
text("天魔剣が……<br>頭を下げた？", "speech", "right")
pause(43, "目撃者の驚きから本人の答え")
text("盗んでねえよ。", "speech")
pause(26, "濡れ衣を覆す一言を独立させる")
text("向こうが、<br>俺を選んだ。", "final-line", "center")
pause(72, "臣従の余韻から隠しルートへ")
graphic("ui-route")
pause(68, "次回への余韻")

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
{''.join(BLOCKS)}<footer><p>第1話　完</p><p>次回「宗主、跪け」</p><small>天魔、二周目。 ／ ORIGINAL WEBTOON</small></footer></main></body></html>'''
(ROOT / "index.html").write_text(document, encoding="utf-8")
print(ROOT / "index.html")
