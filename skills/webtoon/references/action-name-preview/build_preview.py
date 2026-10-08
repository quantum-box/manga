#!/usr/bin/env python3
"""Rebuild this partial action name with the shared composer and local edge styles.

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
# Slanted visual edges act as gutters. Lettering remains upright outside the crop.
# The small cuts affect native blank/background margins rather than faces or blades.
style = '''
<style id="action-name-edge-styles">
body { color: #161616; }
.voice-copy { color: #263944; }
[data-beat-id="p05"] .crop-window { clip-path: polygon(0 0,100% 4%,100% 100%,0 96%); }
[data-beat-id="p17"] .crop-window { clip-path: polygon(0 4%,100% 0,100% 96%,0 100%); }
[data-beat-id="p20"] .crop-window { clip-path: polygon(0 0,100% 4%,100% 100%,0 96%); }
[data-beat-id="p20"] .sfx { font-size: clamp(25px,9cqw,38px); color: #111; transform: translate(-50%,-50%) rotate(-12deg); }
[data-beat-id="p17"] .sfx { font-size: clamp(23px,8cqw,34px); }
</style>
'''
html = html.replace('</head>', style + '</head>')
html = html.replace('390px基準 / 360pxでも確認できる構成 preview',
                    '戦闘一場面・24コマの部分試作 / 一話全体の分量判定は対象外')
output.write_text(html)
print(output)
