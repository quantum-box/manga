import unittest
import hashlib
import json
from pathlib import Path
import tempfile
from preview_name import validate_destination, validated_payload


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

    def test_descriptor_changes_are_rejected_before_upload(self):
        payload = {'title': '採用ネーム', 'cover': 'cover.jpg',
                   'blocks': [{'type': 'image', 'src': 'first.png'},
                              {'type': 'image', 'src': 'last.png'}]}
        raw = json.dumps(payload, ensure_ascii=False).encode()
        manifest = {'episodeSHA256': hashlib.sha256(raw).hexdigest()}
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            descriptor = folder / 'episode.json'
            descriptor.write_bytes(raw)
            self.assertEqual(validated_payload(folder, manifest), raw)
            for changed in [{**payload, 'title': '別の本文'},
                            {**payload, 'blocks': list(reversed(payload['blocks']))},
                            {**payload, 'cover': 'different.jpg'}]:
                descriptor.write_text(json.dumps(changed), encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'descriptor changed'):
                    validated_payload(folder, manifest)
            descriptor.write_bytes(raw)
            with self.assertRaisesRegex(ValueError, 'prepare it again'):
                validated_payload(folder, {})
