import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


EXPORT_PATH = Path(__file__).resolve().parents[1] / "examples/tower-forge/production/export.py"
spec = importlib.util.spec_from_file_location("tower_native_export", EXPORT_PATH)
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class EpisodeExportBoundaryTests(unittest.TestCase):
    def test_multiple_or_invalid_episode_scope_cannot_create_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "release"
            for numbers in [[], [2, 3], [2, 2], [True], [0]]:
                with self.assertRaisesRegex(ValueError, "exactly one episode"):
                    exporter.export(output, numbers)
                self.assertFalse(output.exists())
            result = subprocess.run([sys.executable, str(EXPORT_PATH), str(output),
                                     "--episode", "2", "--episode", "3"], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("exactly one episode", result.stderr)
            self.assertFalse(output.exists())

    def test_stale_backup_state_cannot_be_reused_or_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            backup = output / "backup"
            backup.mkdir()
            snapshot = backup / "previous-ids.json"
            snapshot.write_text("[]\n")
            manifest = output / "manifest.json"
            manifest.write_text("old release\n")
            with self.assertRaisesRegex(ValueError, "new empty output directory"):
                exporter.export(output, [2])
            self.assertEqual(snapshot.read_text(), "[]\n")
            self.assertEqual(manifest.read_text(), "old release\n")


if __name__ == "__main__":
    unittest.main()
