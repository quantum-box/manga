import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('regalia_narrative_alt',
    Path(__file__).resolve().parents[1] / 'examples/star-ring-regalia/production/narrative_alt.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class NarrativeDescriptionTests(unittest.TestCase):
    def test_screen_reader_gets_story_and_dialogue_without_generation_directions(self):
        panels = [{'scene': 'KOH anatomical LEFT, no HUD, medium camera',
                   'lines': [{'speaker': '航', 'text': 'もう一回いい？'},
                             {'speaker': '音', 'text': 'コン'},
                             {'speaker': 'HUD', 'text': '討伐隊募集'}]}]
        self.assertEqual(module.narrative_alt_text('航が構え直す。', panels),
                         '航が構え直す。　航「もう一回いい？」 / 音「コン」 / 画面「討伐隊募集」')

    def test_missing_narrative_description_fails_instead_of_falling_back_to_prompt(self):
        for description in [None, '', '   ']:
            with self.subTest(description=description):
                with self.assertRaisesRegex(ValueError, 'narrative'):
                    module.narrative_alt_text(description, [{'scene': 'Generation directions', 'lines': []}])


if __name__ == '__main__':
    unittest.main()
