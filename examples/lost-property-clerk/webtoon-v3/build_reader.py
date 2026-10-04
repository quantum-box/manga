"""Embed the untouched artwork in one portable HTML reader (stdlib only)."""
from pathlib import Path
import base64
import re

directory = Path(__file__).resolve().parent
source = (directory / "index.html").read_text(encoding="utf-8")


def embed(match):
    data = (directory / match.group(1)).read_bytes()
    return 'src="data:image/png;base64,' + base64.b64encode(data).decode("ascii") + '"'


reader = re.sub(r'src="(art/[^\"]+\.png)"', embed, source)
(directory / "reader.html").write_text(reader, encoding="utf-8")
print("Saved reader.html — artwork embedded without changing the images")
