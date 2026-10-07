#!/usr/bin/env python3
# coding: utf-8
"""Keep production labels out of reader-facing catalog metadata."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_LABEL = re.compile(
    r"日本語縦書き|原画統合|改稿版|再制作版|増補版|初稿|"
    r"ロードマップ|作画済み|完成作画|スマホ確認|改稿待ち|場面脚本|仮構成|公開準備中|各(?:話)?(?:約)?\d+(?:枚|コマ)|"
    r"(?:^|[\s・·（(])v\d+(?:$|[\s・·）)])"
)


def check(catalog):
    for series in catalog:
        for field in ("title", "tagline", "synopsis"):
            if PRODUCTION_LABEL.search(series.get(field, "")):
                raise ValueError(f"Production label in {series['id']}/{field}")
        for episode in series["episodes"]:
            if episode.get("edition", ""):
                raise ValueError(f"Public edition label in {series['id']}/{episode['id']}")
            if PRODUCTION_LABEL.search(episode["title"]):
                raise ValueError(f"Production label in chapter title: {episode['id']}")


class VisibleCopy(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.hidden_depth -= 1

    def handle_data(self, data):
        if not self.hidden_depth and PRODUCTION_LABEL.search(data):
            raise ValueError(f"Production label in public chapter list: {data.strip()}")


def check_readme(text):
    """Only the reader's work list is public copy; production sections are notes."""
    in_work_list = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_work_list = line == "## 読める作品"
        if in_work_list and line.startswith("| ["):
            description = line.split("|")[-2]
            if PRODUCTION_LABEL.search(description):
                raise ValueError(f"Production label in public work list: {description.strip()}")


if __name__ == "__main__":
    check_readme((ROOT / "README.md").read_text(encoding="utf-8"))
    print("Customer copy verified: README.md work list")
    for path in (ROOT / "content/catalog.json", ROOT / "ios/Manga/Webtoons/catalog.json"):
        catalog = json.loads(path.read_text(encoding="utf-8"))
        check(catalog)
        print(f"Customer copy verified: {path.relative_to(ROOT)}")
    for path in (ROOT / "examples").rglob("chapters.html"):
        VisibleCopy().feed(path.read_text(encoding="utf-8"))
        print(f"Customer copy verified: {path.relative_to(ROOT)}")
