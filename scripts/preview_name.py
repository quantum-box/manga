#!/usr/bin/env python3
"""Render a checked-in name and deliver it only to manga-server's PR preview."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def preview_url(pr):
    if pr <= 0:
        raise ValueError('A positive PR number is required')
    return f'https://pr{pr}--manga-server.txcloud.app'


def validate_destination(manifest, pr):
    expected = preview_url(pr)
    if manifest['baseURL'] != expected or manifest['pullRequest'] != pr:
        raise ValueError('Manifest must target this exact PR preview')
    if not manifest['episodeID'].startswith('name-'):
        raise ValueError('Only name preview IDs can be published here')
    return expected


def prepare(args):
    source = args.source.resolve()
    relative = source.relative_to(ROOT)
    plan = json.loads(source.with_name('plan.json').read_text())
    if args.output.resolve().is_relative_to(ROOT):
        raise ValueError('Use an empty output directory outside the checkout')
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Output directory must be empty')
    # A PR preview must be traceable to its committed name, never an unsaved draft.
    tracked = subprocess.check_output(['git', 'ls-files', '--error-unmatch', str(relative)], cwd=ROOT)
    dirty = subprocess.check_output(['git', 'status', '--porcelain', '--', str(relative), str(relative.with_name('plan.json'))], cwd=ROOT)
    if not tracked or dirty:
        raise ValueError('Commit the name and plan before exporting')
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    series = relative.parts[1]
    episode = relative.parts[2]
    episode_id = f'name-{series}-{episode}-{digest[:12]}'
    args.output.mkdir(parents=True, exist_ok=True)
    settings = {episode_id: {'source': str(source), 'sourceDigest': digest,
                            'subtitle': plan['title'], 'flowSelector': '#preview-flow'}}
    sources = args.output / 'sources.json'
    sources.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + '\n')
    subprocess.run(['node', str(ROOT / 'scripts/render_retina_reader.cjs'), str(sources), str(args.output)], check=True)
    folder = args.output / episode_id
    render = json.loads((folder / 'render.json').read_text())
    payload = {'title': plan['title'] + ' · ネーム', 'subtitle': '構成確認用',
               'cover': render['cover'], 'blocks': render['blocks']}
    (folder / 'episode.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    names = [b['src'] for b in render['blocks']] + [render['cover']]
    manifest = {'baseURL': preview_url(args.pr), 'pullRequest': args.pr, 'episodeID': episode_id,
                'source': str(relative), 'sourceSHA256': digest,
                'sourceCommit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
                'panels': sum(b['type'] == 'panel' for b in plan['beats']),
                'cssHeight390': render['cssHeight'], 'pixelWidth': render['pixelWidth'],
                'assets': {n: hashlib.sha256((folder / n).read_bytes()).hexdigest() for n in names}}
    (folder / 'preview-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(folder, flush=True)


def publish(args):
    folder = args.folder.resolve()
    manifest = json.loads((folder / 'preview-manifest.json').read_text())
    base = validate_destination(manifest, args.pr)
    source = ROOT / manifest['source']
    if hashlib.sha256(source.read_bytes()).hexdigest() != manifest['sourceSHA256']:
        raise ValueError('Name changed after export; prepare it again')
    for name, expected in manifest['assets'].items():
        if hashlib.sha256((folder / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Export changed: {name}')
    subprocess.run([sys.executable, str(ROOT / 'scripts/publish_episode.py'), base,
                    manifest['episodeID'], str(folder / 'episode.json')], check=True)
    # Read back every delivered byte, including the cover and the last page.
    def get(path):
        with urllib.request.urlopen(base + path, timeout=60) as response:
            return response.read()
    payload = json.loads((folder / 'episode.json').read_text())
    if json.loads(get('/api/episodes/' + manifest['episodeID'])) != payload:
        raise ValueError('Delivered episode does not match the export')
    for name, expected in manifest['assets'].items():
        data = get('/images/' + manifest['episodeID'] + '/' + name)
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f'Delivered image differs: {name}')
    manifest['verifiedURL'] = base + '/?episode=' + manifest['episodeID']
    (folder / 'preview-verified.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print('Verified:', manifest['verifiedURL'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('source', type=Path)
    prep.add_argument('output', type=Path)
    prep.add_argument('--pr', type=int, required=True)
    pub = commands.add_parser('publish')
    pub.add_argument('folder', type=Path)
    pub.add_argument('--pr', type=int, required=True)
    args = parser.parse_args()
    preview_url(args.pr)
    (prepare if args.command == 'prepare' else publish)(args)


if __name__ == '__main__':
    main()
