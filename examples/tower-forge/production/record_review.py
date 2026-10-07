#!/usr/bin/env python3
"""Record an explicit model review against the current adopted art and browser evidence."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def record(number, scenes390, notes):
    folder = ROOT / f"episode-{number:02d}"
    episode = json.loads((folder / "episode.json").read_text())
    assets = json.loads((folder / "assets.json").read_text())
    count = len(episode["scenes"])
    if len(assets) != count or not scenes390 or any(i < 1 or i > count for i in scenes390):
        raise ValueError("Review does not match the current episode")
    metrics = []
    for width in (390, 360):
        metric = json.loads((folder / f"validation/browser-{width}.json").read_text())
        if metric["loaded"] != count or metric["sceneCount"] != count or metric["pageWidth"] != width:
            raise ValueError("Browser evidence is incomplete or has horizontal overflow")
        metrics.append(metric)
    review = dict(date=datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat(), episode=number, revision=episode.get("revision"),
                  sceneCount=count, narrative_panel_count=episode["narrative_panel_count"],
                  adopted_sha256=[a["sha256"] for a in assets],
                  reader_sha256=hashlib.sha256((folder / "index.html").read_bytes()).hexdigest(),
                  viewports=metrics,
                  full_reader_captures=[dict(width=m["width"],pageHeight=m["pageHeight"],parts=m["parts"]) for m in metrics],
                  raster_lettering_visual="reviewed_at_both_widths", physical_device_tested=False,
                  story_quality_approved_by_user=False,
                  method="Model visual review at native phone scale; actual CUA browser captures of the complete reader at both widths",
                  visual_review=dict(reviewer="model", reviewed_scenes_360=list(range(1,count+1)),
                                     reviewed_scenes_390=scenes390, notes=notes,
                                     scope="Every adopted scene at 360px; listed representative scenes at 390px; complete browser captures and load/overflow measurements at both widths"),
                  limitations="No physical device test or user read-through approval. Structural checks do not prove comprehension or empathy.")
    (folder / "validation.json").write_text(json.dumps(review,ensure_ascii=False,indent=2)+"\n")
    print(f"Recorded episode {number} review against {count} current images")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episode",type=int)
    parser.add_argument("--scenes-390",type=int,nargs="+",required=True)
    parser.add_argument("--notes",required=True)
    args = parser.parse_args()
    record(args.episode,args.scenes_390,args.notes)
