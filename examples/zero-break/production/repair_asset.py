"""Adopt a targeted image_gen edit, retaining its prior PNG and exact prompt."""
from pathlib import Path
import hashlib
import json
import sys

root = Path(__file__).resolve().parents[1] / f"episode-{int(sys.argv[2]):02d}"
filename, previous, prompt_file = sys.argv[3:6]
data = Path(sys.argv[1]).read_bytes()
if not data.startswith(b"\x89PNG\r\n\x1a\n") or not data.endswith(b"IEND\xaeB\x60\x82"):
    raise ValueError("Edited PNG is incomplete")
log = root / "generation" / (Path(filename).stem + ".json")
record = json.loads(log.read_text())
prompt = (root / prompt_file).read_text()
record.setdefault("originalPrompt", record["prompt"])
record.setdefault("repairs", []).append({
    "prompt": prompt, "editTargetSavedAt": previous,
    "references": json.loads(sys.argv[6]), "previousSha256": record["sha256"],
    "finalArt": "art/" + filename, "sha256": hashlib.sha256(data).hexdigest(),
})
(root / "art" / filename).write_bytes(data)
record.update(prompt=prompt, sha256=hashlib.sha256(data).hexdigest(), bytes=len(data), visualReview="pending")
log.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"file": filename, "repairSaved": True, "sha256": record["sha256"]}))
