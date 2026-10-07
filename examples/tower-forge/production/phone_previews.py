#!/usr/bin/env python3
"""Crop scene inspection images from the saved, actual phone-width browser captures."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def crop(number):
    from PIL import Image
    folder = ROOT / f"episode-{number:02d}"
    for width in (390, 360):
        metric = json.loads((folder / f"validation/browser-{width}.json").read_text())
        if metric["width"] != width or metric["pageWidth"] != width:
            raise ValueError("Wrong browser width or horizontal overflow")
        if metric["loaded"] != metric["sceneCount"]:
            raise ValueError("Unloaded art")
        canvas = Image.new("RGB", (width, metric["pageHeight"]), "white")
        cursor = 0
        for part in metric["parts"]:
            image = Image.open(folder / part["file"]).convert("RGB")
            if part["y"] != cursor or image.width != width or abs(image.height - part["height"]) > 1:
                raise ValueError("Non-contiguous browser evidence or wrong capture dimensions")
            canvas.paste(image, (0, cursor))
            cursor += part["height"]
        if cursor != metric["pageHeight"]:
            raise ValueError("Incomplete page capture")
        for scene in metric["scenes"]:
            top = round(scene["y"])
            bottom = round(scene["y"] + scene["height"])
            image = canvas.crop((0, top, width, bottom))
            image.save(folder / f"validation/{scene['id']}-{width}.jpg", quality=94)
    print(f"Episode {number}: scene previews cropped from both actual browser widths")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episodes", type=int, nargs="+")
    for number in parser.parse_args().episodes:
        crop(number)
