#!/usr/bin/env python3
"""Bundle finished Webtoon readers unchanged for the offline iOS app."""

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path("ios/Manga/Webtoons")


class ReaderReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = set()
        self.json_depth = False
        self.json_text = []
        self.json_asset_map = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"img", "script", "source"} and attrs.get("src"):
            self.references.add(attrs["src"])
        if tag == "link" and attrs.get("href"):
            self.references.add(attrs["href"])
        if tag == "script" and attrs.get("type") == "application/json":
            self.json_depth = True
            self.json_text = []
            self.json_asset_map = attrs.get("id") == "artwork-sources"

    def handle_data(self, data):
        if self.json_depth:
            self.json_text.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.json_depth:
            payload = json.loads("".join(self.json_text))
            if self.json_asset_map:
                if not isinstance(payload, dict) or not all(isinstance(value, str) for value in payload.values()):
                    raise ValueError("artwork-sources must map artwork names to resource paths")
                self.references.update(payload.values())
            else:
                self.references.update(json_references(payload))
            self.json_depth = False


def json_references(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "src" and isinstance(child, str):
                yield child
            else:
                yield from json_references(child)
    elif isinstance(value, list):
        for child in value:
            yield from json_references(child)


def local_reference(reference, directory, boundary):
    parts = urlsplit(reference)
    if parts.scheme == "data" or not parts.path:
        return None
    if parts.scheme or parts.netloc or parts.path.startswith("/"):
        raise ValueError(f"Offline reader cannot depend on: {reference}")
    path = (directory / unquote(parts.path)).resolve()
    if not path.is_relative_to(boundary) or not path.is_file():
        raise ValueError(f"Missing or out-of-episode asset: {reference}")
    return path


def reader_files(source):
    boundary = source.parent.resolve()
    pending = [source.resolve()]
    visited = set()
    while pending:
        path = pending.pop()
        if path in visited:
            continue
        visited.add(path)
        references = set()
        if path.suffix in {".html", ".css"}:
            contents = path.read_text(encoding="utf-8")
            references.update(re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", contents))
            if path.suffix == ".html":
                parser = ReaderReferences()
                parser.feed(contents)
                references.update(parser.references)
        for reference in references:
            asset = local_reference(reference, path.parent, boundary)
            if asset:
                pending.append(asset)
    return visited


def safe_id(value):
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", value):
        raise ValueError(f"Invalid bundle id: {value}")
    return value


def bundle_catalog(root, destination):
    root = root.resolve()
    catalog = json.loads((root / "content/catalog.json").read_text(encoding="utf-8"))
    title_ids = set()
    for title in catalog:
        title_id = safe_id(title["id"])
        if title_id in title_ids or not title["episodes"]:
            raise ValueError(f"Duplicate or empty title: {title_id}")
        title_ids.add(title_id)
        episode_ids = set()
        for episode in title["episodes"]:
            episode_id = safe_id(episode["id"])
            if episode_id in episode_ids or episode["number"] < 1:
                raise ValueError(f"Invalid episode: {title_id}/{episode_id}")
            episode_ids.add(episode_id)
            if not re.fullmatch(r"#[0-9a-fA-F]{6}", episode["background"]):
                raise ValueError(f"Invalid background: {episode['background']}")
            source = (root / episode.pop("source")).resolve()
            if not source.is_relative_to(root / "examples") or not source.is_file():
                raise ValueError(f"Missing episode source: {source}")
            chapter = destination / title_id / episode_id
            for asset in reader_files(source):
                relative = asset.relative_to(source.parent)
                target = chapter / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(asset, target)
            episode["reader"] = str(PurePosixPath(title_id, episode_id, source.name))
        cover = PurePosixPath(title_id, title.pop("cover"))
        if ".." in cover.parts or cover.is_absolute() or not (destination / str(cover)).is_file():
            raise ValueError(f"Missing cover: {cover}")
        title["image"] = str(cover)
    (destination / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return catalog


def same_file_contents(expected, actual):
    if expected.stat().st_size != actual.stat().st_size:
        return False
    with expected.open("rb") as expected_file, actual.open("rb") as actual_file:
        while True:
            expected_chunk = expected_file.read(1024 * 1024)
            actual_chunk = actual_file.read(1024 * 1024)
            if expected_chunk != actual_chunk:
                return False
            if not expected_chunk:
                return True


def sync(root=ROOT, check=False):
    root = root.resolve()
    target = root / OUTPUT
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="webtoon-bundle-") as temporary:
        staged = Path(temporary)
        catalog = bundle_catalog(root, staged)
        if check:
            expected = {path.relative_to(staged) for path in staged.rglob("*") if path.is_file()}
            actual = {path.relative_to(target) for path in target.rglob("*") if path.is_file()}
            if expected != actual or any(
                not same_file_contents(staged / path, target / path) for path in expected
            ):
                raise ValueError("Bundled readers differ. Run scripts/sync_ios_webtoons.py")
        else:
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(staged, target)
    episodes = sum(len(title["episodes"]) for title in catalog)
    print(f"{'Verified' if check else 'Bundled'} {len(catalog)} titles / {episodes} readers")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify committed resources match the sources")
    args = parser.parse_args()
    sync(check=args.check)
