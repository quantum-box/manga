"""ZIP each self-contained reader unchanged and verify its extracted bytes."""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
numbers = list(map(int, sys.argv[1:])) or list(range(2, 11))
for number in numbers:
    directory = root / f"episode-{number:02d}"
    reader = (directory / "reader.html").read_bytes()
    manifest = json.loads((directory / "manifest.json").read_text())
    if reader.count(b"data:image/png;base64,") != len(manifest["shots"]):
        raise ValueError(f"Episode {number} reader is incomplete")
    archive = directory / "reader.zip"
    info = zipfile.ZipInfo("reader.html", date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as target:
        target.writestr(info, reader, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(archive) as source:
        if source.testzip() is not None or source.read("reader.html") != reader:
            raise ValueError("ZIP extraction differs from the completed reader")
    if archive.stat().st_size >= 100 * 1024**2:
        raise ValueError("Split delivery before tracking an archive over 100 MiB")
    result = {"episode": number, "status": "passed", "archiveEntries": ["reader.html"],
              "readerBytes": len(reader), "archiveBytes": archive.stat().st_size,
              "readerSha256": hashlib.sha256(reader).hexdigest(),
              "archiveSha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
              "archiveExtractMatchesReader": True, "sourceArtworkModified": False,
              "embeddedImages": len(manifest["shots"])}
    (directory / "delivery-validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({"episode": number, "archiveBytes": result["archiveBytes"], "status": "passed"}))
