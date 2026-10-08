import json
from pathlib import Path
import tempfile
import tracemalloc
import unittest

from sync_ios_webtoons import bundle_catalog, sync


class OfflineBundleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.chapter = self.root / "examples/story/chapter"
        (self.chapter / "art").mkdir(parents=True)
        (self.chapter / "art/cover.png").write_bytes(b"cover-fixture")
        (self.chapter / "art/second.png").write_bytes(b"second-fixture")
        (self.root / "content").mkdir()
        self.catalog = [{
            "id": "story", "title": "試作", "genre": "SF", "tagline": "", "synopsis": "",
            "cover": "chapter/art/cover.png",
            "episodes": [{"id": "chapter", "number": 1, "title": "第1話", "edition": "",
                          "source": "examples/story/chapter/index.html", "background": "#ffffff"}],
        }]
        self.write_catalog()
        self.html = ('<!doctype html><img src="art/cover.png">'
                     '<script type="application/json">{"blocks":[{"src":"art/second.png"}]}</script>'
                     '<p style="margin-top:500px">沈黙のあと。</p>')
        (self.chapter / "index.html").write_text(self.html, encoding="utf-8")

    def write_catalog(self):
        (self.root / "content/catalog.json").write_text(json.dumps(self.catalog), encoding="utf-8")

    def bundle(self):
        destination = self.root / "bundle"
        destination.mkdir(exist_ok=True)
        return bundle_catalog(self.root, destination), destination

    def test_preserves_lettering_spacing_and_dynamic_panel_assets(self):
        catalog, destination = self.bundle()
        reader = destination / catalog[0]["episodes"][0]["reader"]
        self.assertEqual(reader.read_bytes(), (self.chapter / "index.html").read_bytes())
        self.assertEqual((reader.parent / "art/second.png").read_bytes(), b"second-fixture")
        self.assertTrue((destination / catalog[0]["image"]).is_file())

    def test_missing_image_fails_before_replacing_existing_bundle(self):
        sync(self.root)
        target = self.root / "ios/Manga/Webtoons/story/chapter/index.html"
        (self.chapter / "art/second.png").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            sync(self.root)
        self.assertEqual(target.read_text(encoding="utf-8"), self.html)

    def test_artwork_source_map_bundles_dynamic_images_and_rejects_missing_art(self):
        html = ('<!doctype html><img data-source="cover"><img data-source="second">'
                '<script type="application/json" id="artwork-sources">'
                '{"cover":"art/cover.png","second":"art/second.png"}</script>'
                '<p style="margin-top:860px">水面の向こう。</p>')
        (self.chapter / "index.html").write_text(html, encoding="utf-8")
        sync(self.root)
        target = self.root / "ios/Manga/Webtoons/story/chapter"
        self.assertEqual((target / "index.html").read_text(encoding="utf-8"), html)
        self.assertEqual((target / "art/second.png").read_bytes(), b"second-fixture")
        (self.chapter / "art/second.png").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            sync(self.root)
        self.assertEqual((target / "index.html").read_text(encoding="utf-8"), html)

    def test_remote_assets_and_directory_escape_are_rejected(self):
        for reference in ["https://example.com/image.png", "../../outside.png"]:
            with self.subTest(reference=reference):
                (self.chapter / "index.html").write_text(f'<img src="{reference}">', encoding="utf-8")
                with self.assertRaises(ValueError):
                    self.bundle()

    def test_check_detects_drift_and_editions_keep_same_chapter_number(self):
        edition = dict(self.catalog[0]["episodes"][0], id="chapter-white", edition="白背景版")
        self.catalog[0]["episodes"].insert(0, edition)
        self.catalog[0]["cover"] = "chapter-white/art/cover.png"
        self.write_catalog()
        sync(self.root)
        sync(self.root, check=True)
        output = self.root / "ios/Manga/Webtoons"
        catalog = json.loads((output / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual([episode["number"] for episode in catalog[0]["episodes"]], [1, 1])
        (output / "story/chapter-white/art/second.png").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "differ"):
            sync(self.root, check=True)

    def test_check_uses_bounded_memory_for_large_assets_and_detects_same_size_drift(self):
        asset = self.chapter / "art/second.png"
        with asset.open("wb") as stream:
            for _ in range(16):
                stream.write(b"a" * (1024 * 1024))
        sync(self.root)
        tracemalloc.start()
        try:
            sync(self.root, check=True)
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        self.assertLess(peak, 8 * 1024 * 1024)

        bundled = self.root / "ios/Manga/Webtoons/story/chapter/art/second.png"
        with bundled.open("r+b") as stream:
            stream.seek(-1, 2)
            stream.write(b"b")
        self.assertEqual(asset.stat().st_size, bundled.stat().st_size)
        with self.assertRaisesRegex(ValueError, "differ"):
            sync(self.root, check=True)

    def test_check_detects_missing_and_extra_bundle_files(self):
        sync(self.root)
        output = self.root / "ios/Manga/Webtoons/story/chapter/art"
        (output / "extra.png").write_bytes(b"extra")
        with self.assertRaisesRegex(ValueError, "differ"):
            sync(self.root, check=True)
        (output / "extra.png").unlink()
        (output / "second.png").unlink()
        with self.assertRaisesRegex(ValueError, "differ"):
            sync(self.root, check=True)


if __name__ == "__main__":
    unittest.main()
