"""Preserve a generated PNG and one independent execution record."""
import hashlib
import json
from pathlib import Path
import sys
import time

root = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1])
episode = int(sys.argv[2])
filename = sys.argv[3]
references = json.loads(sys.argv[4])
directory = root / f"episode-{episode:02d}" if episode else root / "production"
destination = directory / ("art" if episode else "references") / filename
for attempt in range(30):
    data = source.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and data.endswith(b"IEND\xaeB\x60\x82"):
        break
    time.sleep(0.25)
else:
    raise ValueError("Generated PNG has not finished saving")
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_bytes(data)
if episode:
    manifest = json.loads((directory / "manifest.json").read_text())
    shot = next(s for s in manifest["shots"] if s["file"] == filename)
    prompt = shot["prompt"]
else:
    prompt = (directory / (Path(filename).stem + "-prompt.txt")).read_text()
record = {"file": filename, "method": "built-in image_gen", "prompt": prompt,
          "references": references, "sha256": hashlib.sha256(data).hexdigest(),
          "bytes": len(data), "status": "generated", "visualReview": "pending"}
records = directory / "generation"
records.mkdir(exist_ok=True)
(records / (Path(filename).stem + ".json")).write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps({"file": str(destination.relative_to(root)), "sha256": record["sha256"]}))
