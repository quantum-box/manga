import json
from pathlib import Path
import tempfile
import unittest

from export_latest_webtoons import adopted_chapters
from publish_latest_webtoons import owned_id, retire_previous, verify_catalog


class ClientFixture:
    def __init__(self, ids=(), catalog=()):
        self.ids, self.catalog, self.mutations = list(ids), list(catalog), []

    def json(self, path):
        return self.ids if path == "/api/episodes" else self.catalog

    def request(self, path, method="GET", **_kwargs):
        self.mutations.append((path, method))
        raise AssertionError("No mutation expected")


class PublicationSafetyTests(unittest.TestCase):
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
