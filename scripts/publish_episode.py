#!/usr/bin/env python3
"""Upload images, verify existing images on retry, then publish episode JSON."""
import argparse
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('base_url')
parser.add_argument('episode_id')
parser.add_argument('episode_json', type=Path)
args = parser.parse_args()
if not args.base_url.startswith('https://') and not args.base_url.startswith('http://localhost:'):
    parser.error('Use HTTPS (or localhost for development)')
if not re.fullmatch(r'[A-Za-z0-9_-]{1,80}', args.episode_id):
    parser.error('Invalid episode ID')
token = os.environ.get('MANGA_ADMIN_TOKEN', '')
if len(token) < 32:
    parser.error('Set MANGA_ADMIN_TOKEN (at least 32 characters)')
episode = json.loads(args.episode_json.read_text())
base = args.base_url.rstrip('/')

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

opener = urllib.request.build_opener(NoRedirect)
def request(path, data=None, mime=None):
    headers = {}
    if path.startswith("/admin/"):
        headers = {'Authorization': 'Bearer ' + token, 'Content-Type': mime or 'application/octet-stream'}
    req = urllib.request.Request(base + path, data=data, headers=headers, method='PUT' if data is not None else 'GET')
    with opener.open(req, timeout=60) as response:
        return response.read()

for block in episode['blocks']:
    if block['type'] != 'image':
        continue
    name = block['src']
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,80}\.(png|jpg|webp)', name):
        parser.error('Invalid image filename')
    content = (args.episode_json.parent / name).read_bytes()
    mime = {'png': 'image/png', 'jpg': 'image/jpeg', 'webp': 'image/webp'}[name.rsplit('.', 1)[1]]
    try:
        request(f'/admin/images/{args.episode_id}/{name}', content, mime)
    except urllib.error.HTTPError as error:
        # Never silently accept a conflicting immutable object.
        if error.code == 409:
            existing = request(f'/admin/images/{args.episode_id}/{name}')
            if existing != content:
                raise SystemExit(f'{name} contains different bytes. Use a new filename.') from None
            print('Verified existing:', name)
            continue
        raise SystemExit(f'Image upload failed: HTTP {error.code}') from None
    print('Uploaded:', name)
request('/admin/episodes/' + args.episode_id, json.dumps(episode, ensure_ascii=False).encode(), 'application/json')
print('Published:', base + '/?episode=' + args.episode_id)
