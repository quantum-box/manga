import unittest
from preview_name import validate_destination


class PreviewDestinationTests(unittest.TestCase):
    def test_refuses_production_and_another_pr_before_upload(self):
        for url in ['https://manga-server.txcloud.app', 'https://pr93--manga-server.txcloud.app',
                    'https://pr94--manga-server.txcloud.app.evil.example']:
            with self.assertRaises(ValueError):
                validate_destination({'baseURL': url, 'pullRequest': 94, 'episodeID': 'name-episode-03'}, 94)

    def test_refuses_completed_episode_id(self):
        with self.assertRaises(ValueError):
            validate_destination({'baseURL': 'https://pr94--manga-server.txcloud.app',
                                  'pullRequest': 94, 'episodeID': 'star-ring-regalia-episode-03'}, 94)

    def test_accepts_only_matching_preview(self):
        self.assertEqual(validate_destination({'baseURL': 'https://pr94--manga-server.txcloud.app',
                                              'pullRequest': 94, 'episodeID': 'name-episode-03'}, 94),
                         'https://pr94--manga-server.txcloud.app')
