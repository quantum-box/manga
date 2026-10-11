"""Render the checked-in plan with the repository builder and episode lettering."""
from pathlib import Path
import subprocess,sys
p=Path(__file__).resolve().parent
root=p.parents[4]
subprocess.run([sys.executable,str(root/'skills/webtoon/scripts/build_name_preview.py'),str(p/'plan.json'),'--output',str(p/'index.html'),'--force'],check=True)
h=(p/'index.html').read_text()
h=h.replace('</style>', '\n[data-beat-id="03-patrol:3"] .balloon,[data-beat-id="05-defense:1"] .balloon,[data-beat-id="05-defense:3"] .balloon{border-width:3px;border-radius:17% 24% 16% 22%}\n[data-beat-id="05-recover:1"] .balloon{border-width:2px;border-radius:36%}\n</style>',1)
(p/'index.html').write_text(h)
