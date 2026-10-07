import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


spec = importlib.util.spec_from_file_location(
    "tower_verify", Path(__file__).resolve().parents[1] / "examples/tower-forge/production/verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class CurrentGenerationInputs(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "production").mkdir()
        self.write_json("production/adopted-assets.json", {})
        self.write_json("production/repairs.json", [])
        self.write_json("production/revision-provenance.json", [])
        self.add_image("episode-01/art/current.png", b"current artwork")
        self.add_image("episode-02/art/shared.png", b"shared generation input")
        self.write_json("episode-01/episode.json", dict(number=1, scenes=[dict(file="art/current.png")]))
        self.records = [self.record("episode-01/art/current.png", ["episode-02/art/shared.png"]),
                        self.record("episode-02/art/shared.png", [])]

    def write_json(self, name, data):
        (self.root / name).write_text(json.dumps(data))

    def add_image(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def record(self, name, references):
        return dict(adopted=name, sha256=hashlib.sha256((self.root / name).read_bytes()).hexdigest(),
                    references=references)

    def check(self):
        self.write_json("production/asset-provenance.json", self.records)
        return verify.check_source_references(self.root)

    def test_cross_episode_shared_input_remains_reachable(self):
        self.assertEqual(self.check(), {"episode-01/art/current.png", "episode-02/art/shared.png"})

    def test_deleting_shared_input_fails_before_publication(self):
        (self.root / "episode-02/art/shared.png").unlink()
        with self.assertRaisesRegex(ValueError, "Missing current generation input"):
            self.check()

    def test_replacing_input_bytes_invalidates_record(self):
        (self.root / "episode-02/art/shared.png").write_bytes(b"different artwork")
        with self.assertRaisesRegex(ValueError, "Generation input bytes differ"):
            self.check()

    def test_cycles_do_not_hide_missing_nested_input(self):
        self.records[1]["references"] = ["episode-01/art/current.png", "reference/missing.png"]
        with self.assertRaisesRegex(ValueError, "reference/missing.png"):
            self.check()

    def test_unreachable_old_record_does_not_require_obsolete_art(self):
        self.records.append(dict(adopted="episode-01/art/obsolete.png", sha256="old", references=[]))
        self.assertNotIn("episode-01/art/obsolete.png", self.check())

    def make_repaired_override(self):
        self.add_image("episode-01/art/repaired.png", b"repaired artwork")
        self.write_json("production/adopted-assets.json", {"1-1": dict(file="art/repaired.png")})
        self.write_json("production/repairs.json", [dict(
            episode=1, scene=1, adopted="art/repaired.png", edit_source="art/current.png",
            sha256=hashlib.sha256(b"repaired artwork").hexdigest())])

    def test_repair_only_provenance_checks_missing_edit_source(self):
        self.make_repaired_override()
        (self.root / "episode-01/art/current.png").unlink()
        with self.assertRaisesRegex(ValueError, "Missing current generation input: episode-01/art/current.png"):
            self.check()

    def test_repair_only_provenance_checks_changed_edit_source(self):
        self.make_repaired_override()
        (self.root / "episode-01/art/current.png").write_bytes(b"changed edit source")
        with self.assertRaisesRegex(ValueError, "Generation input bytes differ: episode-01/art/current.png"):
            self.check()


class AdoptedRepositoryInputs(unittest.TestCase):
    def test_all_current_generation_inputs_exist_with_recorded_bytes(self):
        self.assertTrue(verify.check_source_references())


if __name__ == "__main__":
    unittest.main()
