#!/usr/bin/env python3
"""Rebuild this partial action name with the shared composer and local impact lettering.

Only display windows and CSS are changed. Generated PNG bytes stay unchanged.
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHARED = HERE.parents[1] / 'scripts' / 'build_name_preview.py'
spec = importlib.util.spec_from_file_location('webtoon_name_preview', SHARED)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
output = HERE / 'index.html'
module.build_preview(HERE / 'plan.json', output, force=True)
html = output.read_text()
# The action assets contain their own inner frame and protruding silhouettes.
# Showing the whole source preserves that protrusion; no CSS polygon masks are used.
style = '''
<style id="action-name-impact-styles">
body { color: #161616; }
.voice-copy { color: #263944; }
[data-beat-id="p05"] .sfx,
[data-beat-id="p17"] .sfx,
[data-beat-id="p20"] .sfx {
 color: #111; font-weight: 900; font-style: italic; letter-spacing: -.035em;
 -webkit-text-stroke: 1px #111;
 text-shadow: 3px 0 #fff,-3px 0 #fff,0 3px #fff,0 -3px #fff;
 transform: translate(-50%,-50%) rotate(-10deg) skew(-8deg);
}
[data-beat-id="p05"] .sfx { font-size: 13cqw; }
[data-beat-id="p17"] .sfx { font-size: 12cqw; }
[data-beat-id="p20"] .sfx { font-size: 14cqw; }
</style>
'''
html = html.replace('</head>', style + '</head>')
html = html.replace('390px基準 / 360pxでも確認できる構成 preview',
                    '戦闘一場面・24コマの部分試作 / 一話全体の分量判定は対象外')
output.write_text(html)
print(output)
