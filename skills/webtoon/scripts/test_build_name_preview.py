import base64
import importlib.util
import json
from pathlib import Path
import struct
import tempfile
import unittest
import zlib


SCRIPT = Path(__file__).with_name("build_name_preview.py")
SPEC = importlib.util.spec_from_file_location("build_name_preview", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def png_bytes(rgb):
    width = height = 2
    row = b"\x00" + bytes(rgb) * width
    raw = row * height

    def chunk(kind, payload):
        return (struct.pack(">I", len(payload)) + kind + payload +
                struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff))

    return (b"\x89PNG\r\n\x1a\n" +
            chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)) +
            chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


class BuildNamePreviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "rough").mkdir()
        (self.root / "rough" / "first.png").write_bytes(png_bytes((220, 80, 80)))
        (self.root / "rough" / "second.png").write_bytes(png_bytes((80, 120, 220)))
        (self.root / "rough" / "first.txt").write_text("not an image", encoding="utf-8")
        self.manifest = self.root / "preview.json"
        self.output = self.root / "preview.html"

    def tearDown(self):
        self.temp.cleanup()

    def write_manifest(self, data):
        self.manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def base_manifest(self, beats=None):
        return {
            "schema": "webtoon-name-preview/v1",
            "title": "扉の前",
            "referenceWidth": 390,
            "beats": beats or [
                {"type": "panel", "id": "opening", "image": "rough/first.png",
                 "alt": "主人公が閉じた扉を見る", "widthPercent": 100, "align": "center",
                 "dialogue": [{"speaker": "レン", "text": "まだ\n開けない", "x": 66, "y": 12,
                                "width": 27, "kind": "spoken", "tail": "left"}],
                 "sounds": [{"text": "カタ…", "x": 68, "y": 78}]},
                {"type": "pause", "id": "wait", "height": 120, "purpose": "返事を待つ"},
                {"type": "voice", "id": "answer", "text": "中にいる", "height": 180,
                 "speaker": "声", "purpose": "姿を見せず声だけ先に届かせる"},
                {"type": "panel", "id": "reaction", "image": "rough/second.png",
                 "alt": "主人公が息を止める", "widthPercent": 72, "align": "right"},
            ],
        }

    def test_embeds_supplied_art_in_reading_order_and_keeps_overlay_text_editable(self):
        data = self.base_manifest()
        data["beats"][0]["dialogue"][0]["text"] = "まだ\n<開けない>"
        data["beats"].append({"type": "panel", "id": "repeat", "image": "rough/first.png",
                              "alt": "同じラフをもう一度見る", "widthPercent": 50, "align": "left"})
        self.write_manifest(data)
        MODULE.build_preview(self.manifest, self.output)
        document = self.output.read_text(encoding="utf-8")
        first_uri = "data:image/png;base64," + base64.b64encode((self.root / "rough/first.png").read_bytes()).decode()
        second_uri = "data:image/png;base64," + base64.b64encode((self.root / "rough/second.png").read_bytes()).decode()
        self.assertEqual(document.count(first_uri), 1, "reused image bytes should be emitted once")
        self.assertEqual(document.count(second_uri), 1)
        self.assertLess(document.index('data-beat-id="opening"'), document.index('data-beat-id="wait"'))
        self.assertLess(document.index('data-beat-id="wait"'), document.index('data-beat-id="answer"'))
        self.assertIn("ネーム確認用・下書き", document)
        self.assertIn("writing-mode: vertical-rl", document)
        self.assertIn("dialogue spoken tail-left", document)
        self.assertIn("<br>", document)
        self.assertIn("&lt;開けない&gt;", document)
        self.assertNotIn("<開けない>", document)
        self.assertNotIn("rough/first.png", document)
        self.assertIn('<script type="application/json" id="name-preview-assets">', document)
        self.assertIn('document.querySelectorAll("img[data-asset]")', document)
        self.assertIn("font-size: clamp(19px, 5.4cqw, 22px)", document)
        self.assertNotIn("overflow: hidden; }\n.draft-bar", document)

    def test_vertical_text_keeps_words_together_and_only_honors_explicit_breaks(self):
        data = self.base_manifest([{
            "type": "panel", "id": "words", "image": "rough/first.png", "alt": "長いセリフ",
            "dialogue": [{"text": "あいうえおかきくけこ", "x": 50, "y": 5, "width": 30}],
        }])
        self.write_manifest(data)
        MODULE.build_preview(self.manifest, self.output)
        document = self.output.read_text(encoding="utf-8")
        self.assertIn("あいうえおかきくけこ", document)
        self.assertNotIn("あいうえおかき<br>", document)
        self.assertIn("dialogue spoken tail-down-left", document)

        data["beats"][0]["dialogue"][0]["text"] = "あいうえお\nかきくけこ"
        self.write_manifest(data)
        MODULE.build_preview(self.manifest, self.output, force=True)
        document = self.output.read_text(encoding="utf-8")
        self.assertIn("<span>あいうえお</span><br><span>かきくけこ</span>", document)

        data["beats"][0]["dialogue"][0]["text"] = "New York\nそうなんだ"
        self.write_manifest(data)
        MODULE.build_preview(self.manifest, self.output, force=True)
        document = self.output.read_text(encoding="utf-8")
        self.assertIn("<span>New York</span><br><span>そうなんだ</span>", document)

    def test_crop_uses_a_view_window_and_does_not_rewrite_source_bytes(self):
        data = self.base_manifest([{
            "type": "panel", "id": "crop", "image": "rough/first.png", "alt": "部分を見る",
            "widthPercent": 80, "align": "left", "crop": [0.25, 0.0, 0.5, 1.0],
            "imageSize": [2, 2],
            "dialogue": [{"text": "見る", "kind": "thought", "x": 4, "y": 8, "width": 24}],
        }])
        original = (self.root / "rough/first.png").read_bytes()
        self.write_manifest(data)
        MODULE.build_preview(self.manifest, self.output)
        document = self.output.read_text(encoding="utf-8")
        self.assertIn("class=\"crop-window\"", document)
        self.assertIn("--crop-x:0.25", document)
        self.assertIn("--crop-w:0.5", document)
        self.assertIn("dialogue thought", document)
        self.assertIn("border-style: dashed", document)
        self.assertEqual(original, (self.root / "rough/first.png").read_bytes())

    def test_row_groups_render_in_right_to_left_visual_order(self):
        data = self.base_manifest([
            {"type": "panel", "id": "right", "row": "intro", "image": "rough/first.png",
             "alt": "右側", "widthPercent": 50, "align": "right"},
            {"type": "panel", "id": "left", "row": "intro", "image": "rough/second.png",
             "alt": "左側", "widthPercent": 50, "align": "left"},
        ])
        self.write_manifest(data)
        MODULE.build_preview(self.manifest, self.output)
        document = self.output.read_text(encoding="utf-8")
        self.assertIn("flex-direction: row-reverse", document)
        self.assertIn('class="panel-row" data-row="intro"', document)
        self.assertLess(document.index('data-beat-id="right"'), document.index('data-beat-id="left"'))

    def test_rejects_unsafe_references_duplicate_ids_and_invalid_bounds(self):
        cases = [
            (lambda d: d["beats"][0].update(image="../outside.png"), "manifest.beats[0].image"),
            (lambda d: d["beats"][0].update(image="rough/first.txt"), "unsupported image type"),
            (lambda d: d["beats"][0].update(crop=[0.8, 0, 0.5, 1], imageSize=[2, 2]), "manifest.beats[0].crop"),
            (lambda d: d["beats"][0].update(
                dialogue=[{"text": "重なる", "x": 90, "y": 0, "width": 20}]
            ), "manifest.beats[0].dialogue[0]"),
            (lambda d: d["beats"].append(dict(d["beats"][0])), "duplicate id"),
        ]
        for mutate, expected in cases:
            with self.subTest(expected=expected):
                data = self.base_manifest()
                mutate(data)
                self.write_manifest(data)
                with self.assertRaises(MODULE.PreviewError) as error:
                    MODULE.build_preview(self.manifest, self.output)
                self.assertIn(expected, str(error.exception))

    def test_rejects_overwrite_without_force_and_allows_explicit_force(self):
        self.write_manifest(self.base_manifest())
        MODULE.build_preview(self.manifest, self.output)
        original = self.output.read_text(encoding="utf-8")
        with self.assertRaises(FileExistsError):
            MODULE.build_preview(self.manifest, self.output)
        self.write_manifest(dict(self.base_manifest(), title="別の構成"))
        MODULE.build_preview(self.manifest, self.output, force=True)
        self.assertNotEqual(original, self.output.read_text(encoding="utf-8"))

    def test_rejects_overwriting_referenced_image_even_through_symlink(self):
        self.write_manifest(self.base_manifest())
        original = (self.root / "rough" / "first.png").read_bytes()

        with self.assertRaises(MODULE.PreviewError):
            MODULE.build_preview(self.manifest, self.root / "rough" / "first.png", force=True)
        self.assertEqual(original, (self.root / "rough" / "first.png").read_bytes())

        image_link = self.root / "rough" / "first-link.png"
        image_link.symlink_to(self.root / "rough" / "first.png")
        with self.assertRaises(MODULE.PreviewError):
            MODULE.build_preview(self.manifest, image_link, force=True)
        self.assertEqual(original, (self.root / "rough" / "first.png").read_bytes())


if __name__ == "__main__":
    unittest.main()
