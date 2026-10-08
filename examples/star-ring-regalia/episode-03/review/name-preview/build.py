#!/usr/bin/env python3
"""Rebuild the adopted name from its plan and separate rough lettering CSS."""
import argparse,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--helper',type=Path,default=Path.home()/'.codex/skills/webtoon/scripts/build_name_preview.py')
a=p.parse_args(); root=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(a.helper),str(root/'plan.json'),'--output',str(root/'index.html'),'--force'],check=True)
text=(root/'index.html').read_text().replace('</style>',(root/'layout.css').read_text()+'</style>',1)
(root/'index.html').write_text(text)
