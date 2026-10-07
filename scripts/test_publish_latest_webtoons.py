import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from export_latest_webtoons import adopted_chapters
from publish_latest_webtoons import backup_previous, load_manifest, owned_id, owned_chapter, retire_previous, sha256, verify_catalog


class ClientFixture:
    def __init__(self, ids=(), catalog=()):
        self.ids, self.catalog, self.mutations = list(ids), list(catalog), []

    def json(self, path):
        return self.ids if path == "/api/episodes" else self.catalog

    def request(self, path, method="GET", **_kwargs):
        self.mutations.append((path, method))
        raise AssertionError("No mutation expected")


class PublicationSafetyTests(unittest.TestCase):
    def test_single_chapter_release_leaves_other_chapters_live(self):
        manifest = {"seriesIds": ["tower-forge"], "chapterNumbers": [2],
                    "chapters": [{"id": "tower-forge-episode-02-rnew", "series": "tower-forge", "number": 2}]}
        client = ClientFixture(ids=["tower-forge-episode-01-rold", "tower-forge-episode-02-rnew",
                                    "tower-forge-episode-03-rold", "other-episode-02-rold"])
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            self.assertEqual(backup_previous(client, folder, manifest), [])
            self.assertEqual(retire_previous(client, folder, manifest, []), [])
            with self.assertRaisesRegex(ValueError, "unrelated edition"):
                retire_previous(client, folder, manifest, ["tower-forge-episode-01-rold"])
        self.assertEqual(client.mutations, [])

    def test_scoped_manifest_requires_every_current_chapter_without_publishing_other_series(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "content").mkdir()
            catalog = []
            for series, count in [("tower-forge", 2), ("other", 1)]:
                episodes = []
                for number in range(1, count + 1):
                    folder = root / series / str(number)
                    folder.mkdir(parents=True)
                    (folder / "index.html").write_text('<img src="art.png">')
                    (folder / "art.png").write_bytes(b"native artwork")
                    episodes.append(dict(number=number, title=f"Chapter {number}", edition="current",
                                         source=f"{series}/{number}/index.html"))
                catalog.append(dict(id=series, title=series, episodes=episodes))
            catalog_bytes = json.dumps(catalog).encode()
            (root / "content/catalog.json").write_bytes(catalog_bytes)
            output = root / "output"
            output.mkdir()
            chapters = adopted_chapters(root, ["tower-forge"])
            for chapter in chapters:
                folder = output / chapter["id"]
                folder.mkdir()
                data = b"native artwork"
                (folder / "art.png").write_bytes(data)
                chapter["assets"] = [dict(name="art.png", sha256=sha256(data), bytes=len(data))]
                payload = dict(title=chapter["title"], subtitle=chapter["subtitle"], cover="art.png",
                               blocks=[dict(type="image", src="art.png", alt="")])
                (folder / "episode.json").write_text(json.dumps(payload))
            manifest = dict(seriesIds=["tower-forge"], chapters=chapters,
                            catalogSHA256=sha256(catalog_bytes))
            def resolve(series_ids=None, chapter_numbers=None):
                return adopted_chapters(root, series_ids, chapter_numbers)
            with patch("publish_latest_webtoons.ROOT", root), patch("export_latest_webtoons.adopted_chapters", side_effect=resolve):
                path = output / "manifest.json"
                path.write_text(json.dumps(manifest))
                self.assertEqual(len(load_manifest(output)["chapters"]), 2)
                single = dict(manifest, chapterNumbers=[2], chapters=chapters[1:])
                path.write_text(json.dumps(single))
                self.assertEqual(len(load_manifest(output)["chapters"]), 1)
                self.assertTrue(owned_chapter("tower-forge-episode-02-rold", single))
                self.assertFalse(owned_chapter("tower-forge-episode-01-rold", single))
                self.assertFalse(owned_chapter("tower-forge-episode-03-rold", single))
                self.assertFalse(owned_chapter("other-episode-02-rold", single))
                for numbers in [[], [0], [True], [2, 2], [3], "2"]:
                    path.write_text(json.dumps(dict(single, chapterNumbers=numbers)))
                    with self.assertRaises(ValueError):
                        load_manifest(output)
                for invalid in [dict(manifest, chapters=chapters[:1]),
                                {k: v for k, v in manifest.items() if k != "seriesIds"},
                                dict(manifest, seriesIds=["other"])]:
                    path.write_text(json.dumps(invalid))
                    with self.assertRaisesRegex(ValueError, "every adopted chapter"):
                        load_manifest(output)
                path.write_text(json.dumps(manifest))
                (output / chapters[0]["id"] / "art.png").write_bytes(b"changed bytes")
                with self.assertRaisesRegex(ValueError, "Asset bytes differ"):
                    load_manifest(output)

    def test_series_scope_excludes_other_titles_and_rejects_invalid_scopes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "content").mkdir()
            catalog = []
            for series in ["tower-forge", "other"]:
                folder = root / series
                folder.mkdir()
                (folder / "index.html").write_text('<img src="art.png">')
                (folder / "art.png").write_bytes(b"drawing")
                catalog.append({"id": series, "title": series, "episodes": [
                    {"number": 1, "title": "Chapter", "edition": "", "source": series + "/index.html"}]})
            (root / "content/catalog.json").write_text(json.dumps(catalog))
            self.assertEqual([c["series"] for c in adopted_chapters(root, ["tower-forge"])], ["tower-forge"])
            self.assertEqual(len(adopted_chapters(root)), 2)
            for invalid in [[], ["unknown"], ["tower-forge", "tower-forge"], "tower-forge"]:
                with self.assertRaises(ValueError):
                    adopted_chapters(root, invalid)

    def test_revision_includes_referenced_image_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            chapter = root / "examples/story/chapter"
            chapter.mkdir(parents=True)
            (chapter / "index.html").write_text('<img src="art.png">')
            (chapter / "art.png").write_bytes(b"first drawing")
            (root / "content").mkdir()
            catalog = [{"id": "story", "title": "Story", "episodes": [
                {"number": 1, "title": "Chapter", "edition": "", "source": "examples/story/chapter/index.html"},
                {"number": 1, "title": "Old edition", "edition": "old", "source": "examples/story/chapter/index.html"}]}]
            (root / "content/catalog.json").write_text(json.dumps(catalog))
            first = adopted_chapters(root)
            self.assertEqual(len(first), 1)
            (chapter / "art.png").write_bytes(b"revised drawing")
            self.assertNotEqual(first[0]["id"], adopted_chapters(root)[0]["id"])

    def test_cleanup_stops_if_adopted_chapter_is_missing_or_another_publish_arrives(self):
        manifest = {"chapters": [{"id": "story-episode-01-rnew", "series": "story"}]}
        for ids in [["story-old"], ["story-old", "story-episode-01-rnew", "story-concurrent"]]:
            client = ClientFixture(ids)
            with self.assertRaisesRegex(ValueError, "concurrently"):
                retire_previous(client, Path("unused"), manifest, ["story-old"])
            self.assertEqual(client.mutations, [])

    def test_cleanup_cannot_remove_an_adopted_or_unrelated_id(self):
        manifest = {"chapters": [{"id": "story-episode-01-rnew", "series": "story"}]}
        for old in ["story-episode-01-rnew", "other-episode-01"]:
            client = ClientFixture(["story-episode-01-rnew", old])
            with self.assertRaisesRegex(ValueError, "adopted or unrelated"):
                retire_previous(client, Path("unused"), manifest, [old])
            self.assertEqual(client.mutations, [])
        self.assertFalse(owned_id("another-story-episode-01", {"story"}))

    def test_catalog_verification_rejects_wrong_chapter_title_and_retired_editions(self):
        chapter = {"id": "pochi-episode-02-rnew", "series": "pochi", "number": 2,
                   "subtitle": "New chapter", "edition": "v4"}
        episode = dict(id=chapter["id"], number=2, title="Old first chapter", edition="v4")
        client = ClientFixture(catalog=[{"id": "online-pochi", "episodes": [episode]}])
        with self.assertRaisesRegex(ValueError, "metadata"):
            verify_catalog(client, {"chapters": [chapter]})
        episode["title"] = "New chapter"
        client.catalog[0]["episodes"].append({"id": "pochi-old"})
        with self.assertRaisesRegex(ValueError, "Retired"):
            verify_catalog(client, {"chapters": [chapter]}, ["pochi-old"])


if __name__ == "__main__":
    unittest.main()
