"""Read the immutable revision inputs from Git without retaining backup copies."""
import json
from pathlib import Path
import subprocess

REPO = Path(__file__).resolve().parents[3]
REVISION = "81a4a9a80c9c6782bac7592142750c324a1b42eb"
SNAPSHOTS = "examples/zero-break/production/feedback-v6/baseline"


def baseline_reference(filename):
    return f"git:{REVISION}:{SNAPSHOTS}/{filename}"


def load_baseline(filename):
    result = subprocess.run(
        ["git", "-C", str(REPO), "show", f"{REVISION}:{SNAPSHOTS}/{filename}"],
        capture_output=True, text=True,
    )
    if result.returncode:
        raise RuntimeError(
            f"Revision input {filename} is unavailable in Git history. "
            f"Fetch it with: git fetch origin {REVISION}"
        )
    return json.loads(result.stdout)
