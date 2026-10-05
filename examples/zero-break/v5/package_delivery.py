"""Package the standalone reader without changing any source artwork."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile


root = Path(__file__).resolve().parent
repository = root.parents[2]
subprocess.run([
    sys.executable,
    str(repository / "skills/webtoon/scripts/package_reader.py"),
    str(root / "index.html"), "--output", str(root / "reader.html"), "--force",
], check=True)
reader = (root / "reader.html").read_bytes()
archive = root / "reader.zip"
entry = zipfile.ZipInfo("reader.html", date_time=(1980, 1, 1, 0, 0, 0))
entry.compress_type = zipfile.ZIP_DEFLATED
entry.external_attr = 0o644 << 16
with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as target:
    target.writestr(entry, reader, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
with zipfile.ZipFile(archive) as source:
    if source.testzip() is not None or source.read("reader.html") != reader:
        raise ValueError("Standalone reader archive does not match its source")
    archive_names = source.namelist()
record = {
    "status": "passed",
    "format": "ZIP containing the unmodified self-contained reader.html",
    "archiveEntries": archive_names,
    "readerBytes": len(reader),
    "archiveBytes": archive.stat().st_size,
    "readerSha256": hashlib.sha256(reader).hexdigest(),
    "archiveSha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
    "archiveExtractMatchesReader": True,
    "embeddedImages": reader.count(b"data:image/png;base64,"),
    "sourceArtworkModified": False,
}
(root / "delivery-validation.json").write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(record, ensure_ascii=False))
