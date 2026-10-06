import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


MODULE = Path(__file__).resolve().parents[1] / "examples/zero-break/production/history.py"
SPEC = importlib.util.spec_from_file_location("zero_break_history", MODULE)
history = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(history)


class RevisionHistoryTests(unittest.TestCase):
    def test_rebuild_uses_committed_inputs_without_recreating_deleted_backup(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True)
            snapshot = root / history.SNAPSHOTS / "episode-01.json"
            snapshot.parent.mkdir(parents=True)
            original = {"shots": [{"id": "original", "file": "original.png"}]}
            snapshot.write_text(json.dumps(original))
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            subprocess.run([
                "git", "-C", str(root), "-c", "user.name=Test",
                "-c", "user.email=test@example.invalid", "-c", "commit.gpgsign=false",
                "commit", "--quiet", "-m", "Record historical inputs",
            ], check=True)
            revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"]).decode().strip()
            snapshot.unlink()
            snapshot.parent.rmdir()
            with patch.object(history, "REPO", root), patch.object(history, "REVISION", revision):
                self.assertEqual(history.load_baseline("episode-01.json"), original)
                self.assertIn(revision, history.baseline_reference("episode-01.json"))
            self.assertFalse(snapshot.parent.exists())

    def test_missing_history_reports_the_commit_to_fetch(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True)
            with patch.object(history, "REPO", root):
                with self.assertRaisesRegex(RuntimeError, f"git fetch origin {history.REVISION}"):
                    history.load_baseline("episode-01.json")


if __name__ == "__main__":
    unittest.main()
