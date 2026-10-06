#!/usr/bin/env python3
"""Package ten independent offline readers with their chapter navigation."""
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parent
output=ROOT/"heavenly-demon-ngplus-episodes-01-10.zip"
with zipfile.ZipFile(output,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 z.write(ROOT/"serial.html","heavenly-demon-ngplus/serial.html")
 for n in range(1,11):
  source=ROOT/f"episode-{n:02d}/reader.html"
  if not source.is_file():raise FileNotFoundError(source)
  z.write(source,f"heavenly-demon-ngplus/episode-{n:02d}/index.html")
 z.writestr("heavenly-demon-ngplus/読む前に.txt","天魔、二周目。 第1〜10話\n\nZIPを展開し、serial.htmlをブラウザで開いてください。\n各話の画像とCSSはHTMLに含まれています。インターネット接続は不要です。\n第2〜10話は本文末のリンクで前後の話へ移動できます。\n")
print(f"{output} ({output.stat().st_size/1024/1024:.1f} MiB)")
