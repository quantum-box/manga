#!/usr/bin/env python3
"""Build a local, mobile-friendly webtoon from an episode JSON file."""

import argparse
import html
import json
from pathlib import Path


STYLE = """
:root { color-scheme: light; font-family: -apple-system, BlinkMacSystemFont,
  'Hiragino Kaku Gothic ProN', 'Yu Gothic', sans-serif; }
* { box-sizing: border-box; }
body { margin: 0; background: #15121a; color: #29232b; }
main { max-width: 720px; margin: auto; background: #fffaf4;
  box-shadow: 0 0 60px #0008; overflow: hidden; }
header { min-height: 48vh; display: grid; align-content: center; text-align: center;
  padding: 5rem 1.5rem; background: linear-gradient(#fff8ed, #e8d9ca); }
header h1 { font-size: clamp(2rem, 8vw, 3.5rem); line-height: 1.35; margin: 0 0 1rem; }
header p { font-size: 1.1rem; margin: 0; letter-spacing: .13em; }
figure { margin: 0; }
figure img { display: block; width: 100%; height: auto; }
.beat { display: grid; place-items: center; padding: 5rem 1.5rem;
  text-align: center; min-height: 220px; }
.caption { background: #fffaf4; font-size: clamp(1.2rem, 4.7vw, 1.65rem);
  font-weight: 700; line-height: 1.8; }
.speech { min-height: 180px; background: #fffaf4; }
.bubble { max-width: 86%; background: white; border: 2px solid #392d3b;
  border-radius: 48% / 32%; padding: 1.4rem 2rem;
  box-shadow: 0 10px 28px #392d3b17; }
.speaker { display: block; color: #786b74; font-size: .85rem; margin-bottom: .4rem; }
.line { display: block; font-size: clamp(1.2rem, 5vw, 1.8rem); font-weight: 800; line-height: 1.5; }
.spacer { background: #fffaf4; }
.spacer.short { height: 100px; }
.spacer.long { height: min(42vh, 340px); }
.ending { min-height: 300px; background: linear-gradient(#fffaf4, #ffe7b8);
  color: #533326; font-size: clamp(1.5rem, 6vw, 2.4rem); font-weight: 900; }
footer { text-align: center; padding: 2.5rem; color: #786b74; font-size: .8rem; }
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}
"""


def render_block(block: dict, root: Path) -> str:
    kind = block["type"]
    if kind == "image":
        name = block["src"]
        if Path(name).name != name or not (root / name).is_file():
            raise ValueError(f"Image must exist beside episode.json: {name}")
        return (f'<figure><img src="{html.escape(name, quote=True)}" '
                f'alt="{html.escape(block["alt"], quote=True)}" '
                'loading="lazy" width="1024" height="1536"></figure>')
    if kind == "spacer":
        size = block["size"]
        if size not in {"short", "long"}:
            raise ValueError(f"Unknown spacer size: {size}")
        return f'<div class="spacer {size}" aria-hidden="true"></div>'
    content = html.escape(block["text"])
    if kind == "caption":
        return f'<section class="beat caption"><p>{content}</p></section>'
    if kind == "speech":
        speaker = html.escape(block["speaker"])
        return (f'<section class="beat speech"><div class="bubble">'
                f'<span class="speaker">{speaker}</span><span class="line">{content}</span>'
                '</div></section>')
    if kind == "ending":
        return f'<section class="beat ending"><p>{content}</p></section>'
    raise ValueError(f"Unknown block type: {kind}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episode", type=Path, help="Path to episode.json")
    args = parser.parse_args()
    source = args.episode.resolve()
    data = json.loads(source.read_text(encoding="utf-8"))
    blocks = "\n".join(render_block(block, source.parent) for block in data["blocks"])
    title = html.escape(data["title"])
    subtitle = html.escape(data.get("subtitle", ""))
    document = f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><style>{STYLE}</style></head>
<body><main><header><h1>{title}</h1><p>{subtitle}</p></header>
{blocks}
<footer>おわり</footer></main></body></html>
'''
    output = source.with_name("index.html")
    output.write_text(document, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
