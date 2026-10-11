import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1] / 'examples/star-ring-regalia'
SPEC = importlib.util.spec_from_file_location('regalia_prepare', ROOT / 'production/prepare.py')
prepare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prepare)


class AdoptedEpisodeRecoveryTests(unittest.TestCase):
    def test_missing_descriptor_restores_adopted_story_without_recreating_art(self):
        adopted = json.loads((ROOT / 'production/episodes.json').read_text())
        expected = next(e for e in adopted if e['number'] == 3)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'production').mkdir()
            (root / 'production/episodes.json').write_text(json.dumps(adopted))
            for episode in adopted:
                directory = root / f"episode-{episode['number']:02d}"
                directory.mkdir()
                (directory / 'generation.json').write_text('{}')
                if episode['number'] != 3:
                    (directory / 'episode.json').write_text(json.dumps(episode))
            with patch.object(prepare, 'ROOT', root):
                prepare.main()
            restored = json.loads((root / 'episode-03/episode.json').read_text())
            self.assertEqual(restored, expected)
            self.assertEqual(restored['title'], '星環の剣筋')
            self.assertEqual(json.loads((root / 'production/episodes.json').read_text()), adopted)
            self.assertFalse((root / 'episode-03/art').exists())

    def test_missing_adopted_manifest_stops_without_an_old_draft_fallback(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(prepare, 'ROOT', Path(temporary)):
            with self.assertRaises(FileNotFoundError):
                prepare.adopted_episode(3)


if __name__ == '__main__':
    unittest.main()
