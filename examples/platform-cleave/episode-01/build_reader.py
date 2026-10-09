#!/usr/bin/env python3
"""Build the finished, raster-lettered phone reader from the approved name plan.

The reader keeps one hidden image element per source artwork and renders each
approved crop into a canvas.  Packaging with skills/webtoon/scripts/
package_reader.py therefore embeds each source once instead of duplicating a
composite image for every panel.  The canvases contain only raster artwork;
dialogue and sound text remains in accessibility captions and is never drawn
as an HTML overlay.
"""

from __future__ import annotations

import argparse
import html
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LAYOUT = ROOT / "production" / "layout.json"
CSS = ROOT / "reader.css"
INDEX = ROOT / "index.html"
READER = ROOT / "reader.html"
PACKAGE = ROOT.parent.parent.parent / "skills" / "webtoon" / "scripts" / "package_reader.py"


class BuildError(ValueError):
    pass


def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise BuildError(f"cannot read {path}: {error}") from error


def _relative_url(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _style_number(value: float) -> str:
    return f"{value:.6f}".rstrip("0").rstrip(".")


def _caption(beat: dict) -> str:
    parts = [str(beat.get("alt", "")).strip()]
    for dialogue in beat.get("dialogue", []):
        speaker = dialogue.get("speaker", "")
        text = str(dialogue.get("text", "")).replace("\n", " ").strip()
        if text:
            parts.append(f"{speaker}『{text}』" if speaker else f"『{text}』")
    for sound in beat.get("sounds", []):
        text = str(sound.get("text", "")).strip()
        if text:
            parts.append(f"効果音『{text}』")
    if beat.get("type") == "sound" and beat.get("text"):
        parts.append(f"効果音『{beat['text']}』")
    return "  ".join(part for part in parts if part)


def _source_for_beat(beat_id: str, source_assets: dict) -> str:
    matches = [key for key, asset in source_assets.items()
               if beat_id in asset.get("panels", [])]
    if len(matches) != 1:
        raise BuildError(f"beat {beat_id!r} maps to {len(matches)} source assets")
    return matches[0]


def _offset_style(beat: dict, reference_width: float) -> str:
    if not beat.get("composition"):
        return ""
    x = float(beat.get("offsetX", 0))
    y = float(beat.get("offsetY", 0)) / reference_width * 100
    return f"left:{_style_number(x)}%;top:{_style_number(y)}cqw"


def _scene_html(beat: dict, source_key: str, reference_width: float) -> str:
    beat_id = html.escape(str(beat["id"]), quote=True)
    source = html.escape(source_key, quote=True)
    caption = html.escape(_caption(beat), quote=True)
    beat_type = beat.get("type")

    if beat_type == "sound":
        crop = beat.get("sourceCrop")
        if crop is None:
            raise BuildError(f"sound beat {beat['id']} has no sourceCrop")
        slot = beat.get("slotHeight")
        if slot is None:
            raise BuildError(f"sound beat {beat['id']} has no slotHeight")
        align = beat.get("align", "right")
        style = (
            f"--panel-width:100%;--slot-height:{_style_number(float(slot) / reference_width * 100)}cqw;"
            f"--slot-height-px:{_style_number(float(slot))}px"
        )
        return (
            f'<figure class="scene sound-beat align-{html.escape(align, quote=True)}" '
            f'id="beat-{beat_id}" data-beat-id="{beat_id}" data-kind="sound" '
            f'style="{style}" aria-label="{caption}">'
            f'<canvas data-asset="{source}" data-source="{source}" data-crop="{html.escape(json.dumps(crop, separators=(",", ":")), quote=True)}" '
            f'role="img" aria-label="{caption}"></canvas>'
            f'<figcaption class="sr-only">{caption}</figcaption></figure>'
        )

    width = float(beat.get("widthPercent", 100))
    align = html.escape(str(beat.get("align", "center")), quote=True)
    member = " composition-member" if beat.get("composition") else ""
    crop = beat.get("crop") or [0, 0, 1, 1]
    style = f"--panel-width:{_style_number(width)}%"
    offset_style = _offset_style(beat, reference_width)
    if offset_style:
        style += ";" + offset_style
    return (
        f'<figure class="scene align-{align}{member}" id="beat-{beat_id}" '
        f'data-beat-id="{beat_id}" data-kind="panel" style="{style}" '
        f'aria-label="{caption}">'
        f'<canvas data-asset="{source}" data-source="{source}" data-crop="{html.escape(json.dumps(crop, separators=(",", ":")), quote=True)}" '
        f'role="img" aria-label="{caption}"></canvas>'
        f'<figcaption class="sr-only">{caption}</figcaption></figure>'
    )


def _pause_html(beat: dict, reference_width: float) -> str:
    ratio = float(beat["height"]) / reference_width * 100
    purpose = html.escape(str(beat.get("purpose", "")), quote=True)
    beat_id = html.escape(str(beat["id"]), quote=True)
    return (
        f'<div class="pause" id="beat-{beat_id}" data-beat-id="{beat_id}" '
        f'data-kind="pause" data-pacing-purpose="{purpose}" '
        f'style="--pause-ratio:{_style_number(ratio)}" aria-hidden="true"></div>'
    )


def _script() -> str:
    # Kept inline so package_reader.py can produce a single offline HTML file.
    return r'''<script>
(() => {
  const pool = new Map([...document.querySelectorAll("#asset-pool img")]
    .map((img) => [img.dataset.assetId, img]));
  const canvases = [...document.querySelectorAll("canvas[data-asset]")];
  const errors = [];

  function waitForImage(img) {
    if (!img.complete) {
      return new Promise((resolve, reject) => {
        img.addEventListener("load", resolve, {once: true});
        img.addEventListener("error", () => reject(new Error(`image failed: ${img.dataset.assetId}`)), {once: true});
      });
    }
    if (!img.naturalWidth || !img.naturalHeight) {
      return Promise.reject(new Error(`image failed: ${img.dataset.assetId}`));
    }
    return img.decode ? img.decode().catch(() => {}) : Promise.resolve();
  }

  function draw(canvas) {
    const img = pool.get(canvas.dataset.asset);
    if (!img || !img.naturalWidth || !img.naturalHeight) {
      throw new Error(`missing asset ${canvas.dataset.asset}`);
    }
    const crop = JSON.parse(canvas.dataset.crop);
    const [x, y, width, height] = crop;
    const scene = canvas.closest(".scene");
    const cssWidth = scene.getBoundingClientRect().width;
    const sourceWidth = img.naturalWidth * width;
    const sourceHeight = img.naturalHeight * height;
    const slotHeight = scene.dataset.kind === "sound"
      ? scene.getBoundingClientRect().height
      : cssWidth * sourceHeight / sourceWidth;
    const dpr = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, Math.round(cssWidth * dpr));
    canvas.height = Math.max(1, Math.round(slotHeight * dpr));
    canvas.style.height = `${slotHeight}px`;
    const context = canvas.getContext("2d", {alpha: false});
    context.imageSmoothingEnabled = true;
    context.imageSmoothingQuality = "high";
    context.fillStyle = "#fff";
    context.fillRect(0, 0, canvas.width, canvas.height);
    context.drawImage(
      img,
      img.naturalWidth * x,
      img.naturalHeight * y,
      sourceWidth,
      sourceHeight,
      0,
      0,
      canvas.width,
      canvas.height,
    );
    canvas.dataset.drawn = "true";
  }

  async function render() {
    errors.length = 0;
    await Promise.all([...pool.values()].map((img) => waitForImage(img).catch((error) => {
      errors.push(error.message);
    })));
    for (const canvas of canvases) {
      try { draw(canvas); } catch (error) {
        errors.push(error.message);
      }
    }
    window.__readerReady = {
      assets: pool.size,
      canvases: canvases.length,
      drawn: canvases.filter((canvas) => canvas.dataset.drawn === "true").length,
      errors: [...errors],
    };
    document.documentElement.dataset.readerReady = errors.length ? "error" : "true";
    document.dispatchEvent(new CustomEvent("reader-ready"));
  }

  let resizeTimer;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => render(), 80);
  });
  window.__renderReader = render;
  render();
})();
</script>'''


def build_index(plan: dict, layout: dict, missing: list[Path]) -> None:
    reference_width = float(layout.get("referenceWidth", plan.get("referenceWidth", 390)))
    source_assets = layout["sourceAssets"]
    source_tags = []
    for key, asset in source_assets.items():
        path = (ROOT / asset["path"]).resolve()
        size = asset.get("size", [1024, 1536])
        source_tags.append(
            f'<img data-asset-id="{html.escape(key, quote=True)}" '
            f'src="{html.escape(_relative_url(path), quote=True)}" '
            f'width="{int(size[0])}" height="{int(size[1])}" alt="" aria-hidden="true" loading="eager" decoding="async">'
        )

    beats = []
    open_group = None
    group_members = []

    def close_group():
        nonlocal open_group, group_members
        if open_group is None:
            return
        kind, name = open_group
        safe_name = html.escape(str(name), quote=True)
        if kind == "row":
            beats.append(f'<div class="panel-row" data-row="{safe_name}">'
                         + "".join(markup for _, markup in group_members) + '</div>')
        else:
            bottoms = []
            for member, _ in group_members:
                crop = member.get("crop") or [0, 0, 1, 1]
                source_width, source_height = member["imageSize"]
                ratio = source_height * crop[3] / (source_width * crop[2])
                height = float(member.get("widthPercent", 100)) * ratio
                top = float(member.get("offsetY", 0)) / reference_width * 100
                bottoms.append(top + height)
            total_height = _style_number(max(bottoms))
            beats.append(f'<section class="composition" data-composition="{safe_name}" '
                         f'style="--composition-height:{total_height}cqw">'
                         + "".join(markup for _, markup in group_members) + '</section>')
        open_group = None
        group_members = []

    for raw in plan["beats"]:
        beat = dict(raw)
        beat_id = beat["id"]
        if beat.get("type") == "sound":
            crop = layout.get("soundSourceCrops", {}).get(beat_id)
            slot = layout.get("soundSlots", {}).get(beat_id, {})
            if crop is None:
                raise BuildError(f"no sound crop for {beat_id}")
            beat["sourceCrop"] = crop
            beat["slotHeight"] = slot.get("height", beat.get("height"))
            beat["align"] = slot.get("align", "right")
        source_key = _source_for_beat(beat_id, source_assets) if beat.get("type") in {"panel", "sound"} else None
        group = (("composition", beat["composition"]) if beat.get("composition") else
                 ("row", beat["row"]) if beat.get("row") else None)
        if group != open_group:
            close_group()
            open_group = group
        if beat.get("type") == "pause":
            markup = _pause_html(beat, reference_width)
        elif source_key:
            markup = _scene_html(beat, source_key, reference_width)
        else:
            raise BuildError(f"unsupported beat {beat_id}")
        if group:
            group_members.append((beat, markup))
        else:
            beats.append(markup)
    close_group()

    missing_note = "" if not missing else (
        "<!-- Artwork pending: " + ", ".join(_relative_url(path) for path in missing) + " -->"
    )
    title = html.escape(layout.get("title", plan.get("title", "Webtoon")), quote=True)
    document = """<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="reader.css">
</head>
<body>
  <div id="asset-pool" aria-hidden="true">{assets}</div>
  <main class="episode" aria-label="{title}">
    <header class="episode-header"><h1>{title}</h1></header>
    <div class="episode-body">
    {beats}
    </div>
    <footer class="episode-footer"><p>おわり</p></footer>
  </main>
{missing_note}
  {script}
</body>
</html>
""".format(title=title, assets="".join(source_tags), beats="\n    ".join(beats),
           missing_note=missing_note, script=_script())
    INDEX.write_text(document, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-missing", action="store_true",
                        help="write index.html while final artwork is still being generated")
    parser.add_argument("--package", action="store_true",
                        help="also create standalone reader.html with package_reader.py")
    args = parser.parse_args()

    try:
        layout = _read_json(LAYOUT)
        plan_path = (LAYOUT.parent / layout.get("approvedPlan", "../review/name-preview/plan.json")).resolve()
        if not plan_path.is_file():
            raise BuildError(f"approved plan does not exist: {plan_path}")
        plan = _read_json(plan_path)
        missing = []
        for asset in layout["sourceAssets"].values():
            path = (ROOT / asset["path"]).resolve()
            if not path.is_file():
                missing.append(path)
        if missing and not args.allow_missing:
            paths = ", ".join(_relative_url(path) for path in missing)
            raise BuildError(f"finished artwork is missing: {paths}; use --allow-missing only for scaffolding")
        build_index(plan, layout, missing)
        print(f"Saved {INDEX} ({len(plan['beats'])} beats, {len(layout['sourceAssets'])} unique source assets)")
        if missing:
            print("Packaging skipped: " + ", ".join(_relative_url(path) for path in missing))
        elif args.package:
            result = subprocess.run([
                sys.executable, str(PACKAGE), str(INDEX), "--output", str(READER), "--force"
            ], check=False)
            if result.returncode:
                return result.returncode
        return 0
    except (BuildError, OSError, subprocess.SubprocessError) as error:
        print(f"build_reader.py: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
