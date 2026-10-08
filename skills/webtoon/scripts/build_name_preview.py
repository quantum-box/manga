#!/usr/bin/env python3
"""Build a self-contained, phone-width name preview from rough supplied art.

The preview is deliberately separate from the finished reader.  It embeds the
rough images referenced by the manifest and adds editable HTML overlays for
dialogue and sounds; it never edits or rasterizes the image files.
"""

import argparse
import base64
import hashlib
import html
import json
import math
from pathlib import Path
import sys


SCHEMA = "webtoon-name-preview/v1"
DEFAULT_REFERENCE_WIDTH = 390
SUPPORTED_MIME = {
    ".avif": "image/avif",
    ".gif": "image/gif",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}
ALIGNS = {"left", "center", "right"}
BEAT_TYPES = {"panel", "pause", "voice", "sound"}
COMPOSITION_MEMBER_TYPES = {"panel", "voice", "sound"}
FRAME_STYLES = {"none", "thin"}
DIALOGUE_KINDS = {"spoken", "thought"}
TAIL_DIRECTIONS = {"left", "right", "down", "down-left"}


class PreviewError(ValueError):
    """Raised when a name-preview manifest cannot be rendered safely."""


def _path_error(path, message):
    raise PreviewError(f"{path}: {message}")


def _mapping(value, path):
    if not isinstance(value, dict):
        _path_error(path, "expected an object")
    return value


def _list(value, path):
    if not isinstance(value, list):
        _path_error(path, "expected an array")
    return value


def _text(value, path, required=True):
    if not isinstance(value, str):
        _path_error(path, "expected text")
    if required and not value.strip():
        _path_error(path, "must not be empty")
    return value


def _number(value, path, minimum=None, maximum=None, strict_minimum=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        _path_error(path, "expected a finite number")
    value = float(value)
    if not math.isfinite(value):
        _path_error(path, "expected a finite number")
    if minimum is not None and (value <= minimum if strict_minimum else value < minimum):
        _path_error(path, f"must be {'greater than' if strict_minimum else 'at least'} {minimum}")
    if maximum is not None and value > maximum:
        _path_error(path, f"must be at most {maximum}")
    return value


def _id(value, path):
    value = _text(value, path)
    if len(value) > 160:
        _path_error(path, "is too long")
    return value


def _image_size(value, path):
    values = _list(value, path)
    if len(values) != 2:
        _path_error(path, "must contain [width, height]")
    return (
        _number(values[0], f"{path}[0]", minimum=0, strict_minimum=True),
        _number(values[1], f"{path}[1]", minimum=0, strict_minimum=True),
    )


def _png_size(raw):
    if raw.startswith(b"\x89PNG\r\n\x1a\n") and len(raw) >= 24:
        return int.from_bytes(raw[16:20], "big"), int.from_bytes(raw[20:24], "big")
    return None


def _gif_size(raw):
    if raw[:6] in (b"GIF87a", b"GIF89a") and len(raw) >= 10:
        return int.from_bytes(raw[6:8], "little"), int.from_bytes(raw[8:10], "little")
    return None


def _webp_size(raw):
    if raw[:4] != b"RIFF" or raw[8:12] != b"WEBP" or len(raw) < 30:
        return None
    kind = raw[12:16]
    if kind == b"VP8X" and len(raw) >= 30:
        width = 1 + int.from_bytes(raw[24:27], "little")
        height = 1 + int.from_bytes(raw[27:30], "little")
        return width, height
    return None


def _jpeg_size(raw):
    if raw[:2] != b"\xff\xd8":
        return None
    index = 2
    sof_markers = set(range(0xC0, 0xC4)) | set(range(0xC5, 0xC8)) | set(range(0xC9, 0xCC)) | set(range(0xCD, 0xD0))
    while index + 9 <= len(raw):
        while index < len(raw) and raw[index] != 0xFF:
            index += 1
        while index < len(raw) and raw[index] == 0xFF:
            index += 1
        if index >= len(raw):
            break
        marker = raw[index]
        index += 1
        if marker in (0xD8, 0xD9):
            continue
        if index + 2 > len(raw):
            break
        length = int.from_bytes(raw[index:index + 2], "big")
        if length < 2 or index + length > len(raw):
            break
        if marker in sof_markers and length >= 7:
            height = int.from_bytes(raw[index + 3:index + 5], "big")
            width = int.from_bytes(raw[index + 5:index + 7], "big")
            return width, height
        index += length
    return None


def _detected_image_size(raw):
    return _png_size(raw) or _gif_size(raw) or _webp_size(raw) or _jpeg_size(raw)


def _resolve_image(root, reference, path):
    reference = _text(reference, path)
    if "\\" in reference or reference.startswith(("/", "\\")):
        _path_error(path, "must be a relative local image path")
    if "://" in reference or reference.startswith(("data:", "file:")):
        _path_error(path, "external or data URLs are not supported")
    try:
        candidate = (root / reference).resolve()
    except (OSError, RuntimeError, ValueError) as error:
        _path_error(path, f"invalid local image path: {error}")
    try:
        candidate.relative_to(root)
    except ValueError:
        _path_error(path, "must stay inside the manifest directory")
    try:
        exists = candidate.is_file()
    except (OSError, ValueError) as error:
        _path_error(path, f"invalid local image path: {error}")
    if not exists:
        _path_error(path, f"image does not exist: {reference}")
    mime = SUPPORTED_MIME.get(candidate.suffix.lower())
    if mime is None:
        _path_error(path, f"unsupported image type: {candidate.suffix or '(none)'}")
    try:
        raw = candidate.read_bytes()
    except (OSError, ValueError) as error:
        _path_error(path, f"cannot read image: {error}")
    if not raw:
        _path_error(path, "image is empty")
    return candidate, mime, raw


def _validate_crop(panel, image_bytes, path):
    crop_value = panel.get("crop")
    supplied_size = panel.get("imageSize")
    if supplied_size is not None:
        supplied_size = _image_size(supplied_size, f"{path}.imageSize")
    detected_size = _detected_image_size(image_bytes)
    if supplied_size is not None and detected_size is not None and supplied_size != detected_size:
        _path_error(f"{path}.imageSize", f"does not match the image dimensions {detected_size}")
    if crop_value is None:
        return None, supplied_size or detected_size
    values = _list(crop_value, f"{path}.crop")
    if len(values) != 4:
        _path_error(f"{path}.crop", "must contain normalized [x, y, width, height]")
    crop = tuple(_number(value, f"{path}.crop[{index}]", minimum=0, maximum=1)
                 for index, value in enumerate(values))
    x, y, width, height = crop
    if width <= 0 or height <= 0:
        _path_error(f"{path}.crop", "width and height must be greater than zero")
    if x + width > 1 or y + height > 1:
        _path_error(f"{path}.crop", "must stay inside the source image")
    source_size = supplied_size or detected_size
    if source_size is None:
        _path_error(f"{path}.imageSize", "is required when crop is supplied for this image type")
    return crop, source_size


def _annotation_position(item, path, default_x, default_y, default_width):
    x = _number(item.get("x", default_x), f"{path}.x", minimum=0, maximum=100)
    y = _number(item.get("y", default_y), f"{path}.y", minimum=0, maximum=100)
    width = _number(item.get("width", default_width), f"{path}.width", minimum=0, maximum=100, strict_minimum=True)
    if x + width > 100:
        _path_error(path, "x plus width must be at most 100")
    return x, y, width


def _vertical_segments(text):
    """Preserve authored vertical-text breaks without guessing at word boundaries."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = normalized.strip()
    explicit = [part.strip() for part in normalized.split("\n") if part.strip()]
    return explicit or [""]


def _vertical_html(text):
    return "<br>".join(f"<span>{html.escape(segment)}</span>"
                       for segment in _vertical_segments(text))


def _style_number(value):
    return f"{value:.6f}".rstrip("0").rstrip(".")


def _validate_annotations(panel, path):
    dialogue = []
    for index, raw in enumerate(_list(panel.get("dialogue", []), f"{path}.dialogue")):
        item = _mapping(raw, f"{path}.dialogue[{index}]")
        text = _text(item.get("text"), f"{path}.dialogue[{index}].text")
        speaker = _text(item.get("speaker", ""), f"{path}.dialogue[{index}].speaker", required=False)
        kind = item.get("kind", "spoken")
        if not isinstance(kind, str) or kind not in DIALOGUE_KINDS:
            _path_error(f"{path}.dialogue[{index}].kind", "must be spoken or thought")
        tail = item.get("tail", item.get("tailDirection", "down-left"))
        if not isinstance(tail, str) or tail not in TAIL_DIRECTIONS:
            _path_error(f"{path}.dialogue[{index}].tail", "must be left, right, down, or down-left")
        x, y, width = _annotation_position(item, f"{path}.dialogue[{index}]", 68 - index * 28, 8, 24)
        dialogue.append({"speaker": speaker, "text": text, "kind": kind,
                         "x": x, "y": y, "width": width, "tail": tail})
    sounds = []
    for index, raw in enumerate(_list(panel.get("sounds", []), f"{path}.sounds")):
        item = _mapping(raw, f"{path}.sounds[{index}]")
        text = _text(item.get("text"), f"{path}.sounds[{index}].text")
        x, y, _ = _annotation_position(item, f"{path}.sounds[{index}]", 68, 74, 30)
        sounds.append({"text": text, "x": x, "y": y})
    return dialogue, sounds


def _placement_fields(beat, path):
    composition = None
    if "composition" in beat:
        composition = _text(beat.get("composition"), f"{path}.composition")
    offset_x = _number(beat.get("offsetX", 0), f"{path}.offsetX",
                       minimum=0, maximum=100)
    offset_y = _number(beat.get("offsetY", 0), f"{path}.offsetY",
                       minimum=0, maximum=5000)
    return composition, offset_x, offset_y


def _panel_natural_height(panel, path):
    source_size = panel.get("imageSize")
    if source_size is None:
        _path_error(f"{path}.imageSize",
                    "is required when panel participates in a composition")
    source_width, source_height = source_size
    rendered_width = DEFAULT_REFERENCE_WIDTH * panel["widthPercent"] / 100
    if panel["crop"] is None:
        return rendered_width * source_height / source_width
    _, _, crop_width, crop_height = panel["crop"]
    return rendered_width * (crop_height * source_height) / (crop_width * source_width)


def _validate_manifest(data, source):
    data = _mapping(data, "manifest")
    if data.get("schema") != SCHEMA:
        _path_error("manifest.schema", f"must be {SCHEMA}")
    title = _text(data.get("title"), "manifest.title")
    reference_width = _number(data.get("referenceWidth", DEFAULT_REFERENCE_WIDTH),
                              "manifest.referenceWidth", minimum=0, strict_minimum=True)
    beats = _list(data.get("beats"), "manifest.beats")
    if not beats:
        _path_error("manifest.beats", "must not be empty")
    root = source.parent.resolve()
    normalized = []
    ids = set()
    for index, raw in enumerate(beats):
        path = f"manifest.beats[{index}]"
        beat = _mapping(raw, path)
        beat_id = _id(beat.get("id"), f"{path}.id")
        if beat_id in ids:
            _path_error(f"{path}.id", f"duplicate id: {beat_id}")
        ids.add(beat_id)
        beat_type = beat.get("type")
        if not isinstance(beat_type, str) or beat_type not in BEAT_TYPES:
            _path_error(f"{path}.type", "must be panel, pause, voice, or sound")
        purpose = _text(beat.get("purpose", ""), f"{path}.purpose", required=False)
        item = {"id": beat_id, "type": beat_type, "purpose": purpose}
        if beat_type == "panel":
            image, mime, raw_image = _resolve_image(root, beat.get("image"), f"{path}.image")
            alt = _text(beat.get("alt"), f"{path}.alt")
            width_percent = _number(beat.get("widthPercent", 100), f"{path}.widthPercent",
                                   minimum=0, maximum=100, strict_minimum=True)
            align = beat.get("align", "center")
            if not isinstance(align, str) or align not in ALIGNS:
                _path_error(f"{path}.align", "must be left, center, or right")
            crop, source_size = _validate_crop(beat, raw_image, path)
            dialogue, sounds = _validate_annotations(beat, path)
            composition, offset_x, offset_y = _placement_fields(beat, path)
            frame = beat.get("frame", "none")
            if not isinstance(frame, str) or frame not in FRAME_STYLES:
                _path_error(f"{path}.frame", "must be none or thin")
            row = beat.get("row")
            if row is not None:
                if isinstance(row, (dict, list)) or not str(row).strip():
                    _path_error(f"{path}.row", "must be a non-empty scalar when supplied")
                row = str(row)
            item.update({"image": image, "mime": mime, "raw_image": raw_image, "alt": alt,
                         "widthPercent": width_percent, "align": align, "crop": crop,
                         "imageSize": source_size, "dialogue": dialogue, "sounds": sounds,
                         "row": row, "composition": composition, "offsetX": offset_x,
                         "offsetY": offset_y, "frame": frame})
            if composition is not None:
                item["naturalHeight"] = _panel_natural_height(item, path)
        elif beat_type == "pause":
            if "composition" in beat:
                _path_error(f"{path}.composition", "pause cannot have composition")
            item["height"] = _number(beat.get("height"), f"{path}.height", minimum=0,
                                     maximum=5000)
            item["purpose"] = _text(beat.get("purpose"), f"{path}.purpose")
        else:
            item["text"] = _text(beat.get("text"), f"{path}.text")
            item["height"] = _number(beat.get("height"), f"{path}.height", minimum=0,
                                     maximum=5000, strict_minimum=True)
            item["x"] = _number(beat.get("x", 50), f"{path}.x", minimum=0, maximum=100)
            item["y"] = _number(beat.get("y", 50), f"{path}.y", minimum=0, maximum=100)
            item["speaker"] = _text(beat.get("speaker", ""), f"{path}.speaker", required=False)
            width_percent = _number(beat.get("widthPercent", 100), f"{path}.widthPercent",
                                    minimum=0, maximum=100, strict_minimum=True)
            composition, offset_x, offset_y = _placement_fields(beat, path)
            if "frame" in beat:
                _path_error(f"{path}.frame", "frame is only supported on panels")
            item.update({"widthPercent": width_percent, "composition": composition,
                         "offsetX": offset_x, "offsetY": offset_y})
            if composition is not None:
                item["naturalHeight"] = item["height"]
        normalized.append(item)

    seen_compositions = set()
    current_composition = None
    for index, beat in enumerate(normalized):
        composition = beat.get("composition")
        if composition is None:
            current_composition = None
            continue
        path = f"manifest.beats[{index}]"
        if beat.get("row") is not None:
            _path_error(f"{path}.composition", "cannot be combined with row")
        if beat["offsetX"] + beat["widthPercent"] > 100:
            _path_error(f"{path}.offsetX", "offsetX plus widthPercent must be at most 100")
        if composition != current_composition:
            if composition in seen_compositions:
                _path_error(f"{path}.composition", "composition groups must not reappear")
            seen_compositions.add(composition)
            current_composition = composition

    open_rows = set()
    current_row = None
    current_width = 0.0
    for index, beat in enumerate(normalized):
        row = beat.get("row") if beat["type"] == "panel" else None
        if row is None:
            if current_row is not None:
                open_rows.add(current_row)
                current_row = None
                current_width = 0.0
            continue
        if row != current_row:
            if row in open_rows:
                _path_error(f"manifest.beats[{index}].row", "row groups must be contiguous")
            if current_row is not None:
                open_rows.add(current_row)
            current_row = row
            current_width = 0.0
        current_width += beat["widthPercent"]
        if current_width > 100.000001:
            _path_error(f"manifest.beats[{index}].widthPercent", "row widths must total at most 100")
    assets = {}
    asset_ids = {}
    for beat in normalized:
        if beat["type"] != "panel":
            continue
        key = (beat["mime"], hashlib.sha256(beat["raw_image"]).hexdigest())
        asset_id = asset_ids.get(key)
        if asset_id is None:
            asset_id = f"asset-{len(assets)}"
            asset_ids[key] = asset_id
            assets[asset_id] = _data_uri(beat["mime"], beat["raw_image"])
        beat["assetId"] = asset_id
    return {"schema": SCHEMA, "title": title, "referenceWidth": reference_width,
            "beats": normalized, "assets": assets}


def _data_uri(mime, raw):
    return f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"


def _panel_html(panel, composition_member=False):
    style = f"--panel-width:{_style_number(panel['widthPercent'])}%;"
    classes = ["panel", f"align-{panel['align']}"]
    if composition_member:
        classes.append("composition-member")
        style += (f"left:{_style_number(panel['offsetX'])}%;"
                  f"top:{_style_number(panel['offsetY'] / DEFAULT_REFERENCE_WIDTH * 100)}cqw;")
    if panel.get("frame", "none") == "thin":
        classes.append("frame-thin")
    if panel["crop"] is not None:
        x, y, width, height = panel["crop"]
        source_width, source_height = panel["imageSize"]
        ratio = (width * source_width) / (height * source_height)
        style += (f"--crop-x:{_style_number(x)};--crop-y:{_style_number(y)};"
                  f"--crop-w:{_style_number(width)};--crop-h:{_style_number(height)};"
                  f"--crop-ratio:{_style_number(ratio)};"
                  f"--crop-image-width:{_style_number(100 / width)}%;"
                  f"--crop-left:{_style_number(-100 * x / width)}%;"
                  f"--crop-top:{_style_number(-100 * y / height)}%;")
        classes.append("cropped")
        image = (f'<div class="crop-window"><img data-asset="{html.escape(panel["assetId"], quote=True)}" '
                 f'alt="{html.escape(panel["alt"], quote=True)}"')
        if panel["imageSize"]:
            image += f' width="{_style_number(source_width)}" height="{_style_number(source_height)}"'
        image += "></div>"
    else:
        image = (f'<img data-asset="{html.escape(panel["assetId"], quote=True)}" '
                 f'alt="{html.escape(panel["alt"], quote=True)}"')
        if panel["imageSize"]:
            source_width, source_height = panel["imageSize"]
            image += f' width="{_style_number(source_width)}" height="{_style_number(source_height)}"'
        image += ">"
    overlays = []
    for dialogue in panel["dialogue"]:
        segments = _vertical_segments(dialogue["text"])
        max_chars = max(len(segment) for segment in segments)
        style_dialogue = (f"--x:{_style_number(dialogue['x'])}%;--y:{_style_number(dialogue['y'])}%;"
                          f"--dialogue-width:{_style_number(dialogue['width'])}%;"
                          f"--dialogue-height:{_style_number(max(5.5, max_chars * 1.45))}em;")
        speaker = (f'<span class="dialogue-speaker">{html.escape(dialogue["speaker"])}</span>'
                   if dialogue["speaker"] else "")
        overlays.append(
            f'<div class="dialogue {dialogue["kind"]} tail-{dialogue["tail"]}" style="{style_dialogue}" '
            f'aria-label="{html.escape(dialogue["text"], quote=True)}">'
            f'<div class="balloon">{speaker}<span class="dialogue-text">{_vertical_html(dialogue["text"])}</span></div>'
            "</div>"
        )
    for sound in panel["sounds"]:
        style_sound = f"--x:{_style_number(sound['x'])}%;--y:{_style_number(sound['y'])}%;"
        label = html.escape(sound["text"], quote=True)
        overlays.append(
            f'<span class="sfx" style="{style_sound}" aria-label="効果音 {label}">'
            f'{html.escape(sound["text"])}</span>'
        )
    return (f'<figure class="{" ".join(classes)}" data-beat-id="{html.escape(panel["id"], quote=True)}" '
            f'style="{style}">{image}{"".join(overlays)}</figure>')


def _text_beat_html(beat, reference_width, composition_member=False):
    height_reference = DEFAULT_REFERENCE_WIDTH if composition_member else reference_width
    height = _style_number(beat["height"] / height_reference * 100)
    copy_position = f"left:{_style_number(beat['x'])}%;top:{_style_number(beat['y'])}%;"
    classes = ["text-beat", beat["type"]]
    section_style = f"--beat-height:{height}cqw;"
    if composition_member:
        classes.append("composition-member")
        section_style += (f"--member-width:{_style_number(beat['widthPercent'])}%;"
                          f"left:{_style_number(beat['offsetX'])}%;"
                          f"top:{_style_number(beat['offsetY'] / DEFAULT_REFERENCE_WIDTH * 100)}cqw;")
    speaker = (f'<span class="floating-speaker">{html.escape(beat["speaker"])}</span>'
               if beat["speaker"] else "")
    if beat["type"] == "voice":
        body = f'{speaker}<span class="voice-copy">{_vertical_html(beat["text"])}</span>'
    else:
        body = f'{speaker}<span class="sound-copy">{html.escape(beat["text"])}</span>'
    return (f'<section class="{" ".join(classes)}" data-beat-id="{html.escape(beat["id"], quote=True)}" '
            f'style="{section_style}"><div class="floating-copy" style="{copy_position}">{body}</div></section>')


def _composition_html(composition, members, reference_width):
    height = max(beat["offsetY"] + beat["naturalHeight"] for beat in members)
    style = f"--composition-height:{_style_number(height / DEFAULT_REFERENCE_WIDTH * 100)}cqw;"
    rendered = []
    for beat in members:
        if beat["type"] == "panel":
            rendered.append(_panel_html(beat, composition_member=True))
        else:
            rendered.append(_text_beat_html(beat, reference_width, composition_member=True))
    return (f'<section class="composition" data-composition="{html.escape(composition, quote=True)}" '
            f'style="{style}">{"".join(rendered)}</section>')


def _purpose_notes(beats):
    entries = [beat["purpose"] for beat in beats if beat.get("purpose")]
    if not entries:
        return ""
    return '<details class="notes"><summary>構成メモ</summary><ol>' + "".join(
        f"<li>{html.escape(entry)}</li>" for entry in entries
    ) + "</ol></details>"


def _safe_json_script(value):
    """Serialize JSON for an inert script element without allowing markup escape."""
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"))
            .replace("&", "\\u0026")
            .replace("<", "\\u003c")
            .replace(">", "\\u003e")
            .replace("\u2028", "\\u2028")
            .replace("\u2029", "\\u2029"))


CSS = r"""
:root { color-scheme: light; font-family: -apple-system, BlinkMacSystemFont,
  "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif; }
* { box-sizing: border-box; }
html { background: #fff; }
body { margin: 0; background: #fff; color: #20242a; }
.reader { width: 100%; max-width: var(--reference-width, 390px); min-height: 100vh; margin: 0 auto;
  background: #fff; container-type: inline-size; }
.draft-bar { padding: 10px 16px 11px;
  color: #f8fbff; background: #263746; border-bottom: 3px solid #efb46a; }
.draft-badge { display: inline-block; padding: 3px 7px; border: 1px solid #efb46a;
  border-radius: 999px; color: #ffdca8; font-size: 11px; letter-spacing: .08em; }
.draft-bar h1 { margin: 7px 0 0; font-size: 20px; line-height: 1.4; }
.draft-meta { margin-top: 3px; color: #c4d4de; font-size: 11px; }
.notes { margin: 10px 14px; color: #58636b; font-size: 12px; line-height: 1.7; }
.notes summary { cursor: pointer; color: #334b5b; font-weight: 700; }
.notes ol { margin: 5px 0 0; padding-left: 22px; }
.beat { position: relative; }
.panel { width: var(--panel-width); margin: 0; position: relative; }
.panel.align-left { margin-right: auto; }
.panel.align-center { margin-left: auto; margin-right: auto; }
.panel.align-right { margin-left: auto; }
.composition { position: relative; width: 100%; height: var(--composition-height); }
.composition > .composition-member { position: absolute; margin: 0; }
.composition > .text-beat.composition-member { width: var(--member-width); }
.panel.frame-thin.cropped .crop-window { border: 1px solid #35454e; }
.panel > img { display: block; width: 100%; height: auto; }
.panel.cropped .crop-window { position: relative; width: 100%; overflow: hidden;
  aspect-ratio: var(--crop-ratio); }
.panel.cropped .crop-window img { position: absolute; display: block; width: var(--crop-image-width);
  max-width: none; height: auto; left: var(--crop-left); top: var(--crop-top); }
.panel-row { display: flex; flex-direction: row-reverse; width: 100%; align-items: flex-start; }
.panel-row .panel { flex: 0 0 auto; margin: 0; }
.dialogue { position: absolute; z-index: 2; left: var(--x); top: var(--y); width: var(--dialogue-width);
  pointer-events: none; }
.balloon { position: relative; display: flex; align-items: center; justify-content: center;
  min-height: var(--dialogue-height); padding: 7px 6px; color: #17232b; background: #fffefb;
  border: 2px solid #35454e; border-radius: 48% / 34%; box-shadow: 0 2px 0 #17232b22; }
.spoken .balloon::after { content: ""; position: absolute; left: 16%; bottom: -13px;
  width: 16px; height: 16px; background: #fffefb; border-right: 2px solid #35454e;
  border-bottom: 2px solid #35454e; transform: rotate(35deg) skew(-10deg); }
.spoken.tail-left .balloon::after { left: -10px; bottom: 28%; transform: rotate(135deg) skew(-10deg); }
.spoken.tail-right .balloon::after { left: auto; right: -10px; bottom: 28%; transform: rotate(-45deg) skew(-10deg); }
.spoken.tail-down .balloon::after { left: 50%; bottom: -13px; transform: translateX(-50%) rotate(35deg) skew(-10deg); }
.thought .balloon { border-style: dashed; border-radius: 42%; }
.thought .balloon::after { content: "••"; position: absolute; left: 13%; bottom: -21px;
  color: #35454e; font-size: 18px; letter-spacing: 4px; transform: rotate(20deg); }
.dialogue-text { display: inline-block; writing-mode: vertical-rl; text-orientation: mixed;
  white-space: nowrap; font-size: clamp(19px, 5.4cqw, 22px); line-height: 1.35; font-weight: 700; }
.dialogue-text br { display: block; }
.dialogue-speaker, .floating-speaker { display: block; color: #60717b; font-size: 10px;
  line-height: 1.2; text-align: center; writing-mode: horizontal-tb; }
.sfx { position: absolute; z-index: 3; left: var(--x); top: var(--y); transform: translate(-50%, -50%) rotate(-8deg);
  color: #263944; font-size: clamp(15px, 6cqw, 27px); font-weight: 900; letter-spacing: .08em;
  text-shadow: 1px 1px 0 #fff, -1px -1px 0 #fff; white-space: nowrap; }
.pause { width: 100%; height: var(--beat-height); background: #fff; }
.text-beat { position: relative; width: 100%; height: var(--beat-height); background: #fff; }
.floating-copy { position: absolute; transform: translate(-50%, -50%); max-width: 82%; text-align: center; }
.voice-copy { display: inline-block; writing-mode: vertical-rl; text-orientation: mixed; color: #185e79;
  font-size: clamp(19px, 5.4cqw, 22px); line-height: 1.3; font-weight: 700; }
.sound-copy { display: block; color: #263944; font-size: clamp(19px, 7cqw, 34px); font-weight: 900;
  letter-spacing: .09em; white-space: nowrap; transform: rotate(-7deg); }
.text-beat .floating-speaker { margin-bottom: 5px; }
.end-note { padding: 30px 16px 55px; text-align: center; color: #68747b; font-size: 12px; }
.measurement { position: static; display: block; margin: 10px 14px 0; max-width: 100%;
  color: #25333c; background: #fffefb; border: 1px solid #9aaab1; border-radius: 8px;
  box-shadow: 0 3px 14px #17232b33; font-size: 11px; }
.measurement summary { cursor: pointer; padding: 6px 9px; color: #334b5b; font-weight: 700; }
.measurement-body { padding: 0 9px 8px; }
.measurement dl { display: grid; grid-template-columns: auto auto; gap: 3px 10px; margin: 0; }
.measurement dt { color: #60717b; }
.measurement dd { margin: 0; text-align: right; font-variant-numeric: tabular-nums; }
.measurement-note, .measurement-width-note { margin: 7px 0 0; color: #68747b; line-height: 1.45; }
.measurement-width-note { color: #99531a; font-weight: 700; }
"""


MEASUREMENT_HTML = '''<details class="measurement" id="preview-measurement">
<summary>構成計測</summary>
<div class="measurement-body" aria-live="polite">
<dl>
<dt>読書領域幅</dt><dd data-measure="reader-width">—</dd>
<dt>本編高</dt><dd data-measure="flow-height">—</dd>
<dt>明示した余白</dt><dd data-measure="pause-height">—</dd>
<dt>明示した余白だけを除いた高</dt><dd data-measure="non-pause-height">—</dd>
<dt>表示カット数（有効コマではない）</dt><dd data-measure="panel-count">—</dd>
<dt>DPR</dt><dd data-measure="dpr">—</dd>
<dt>画像失敗数</dt><dd data-measure="image-failures">—</dd>
</dl>
<p class="measurement-width-note" data-measure="width-note" hidden>390px幅で確認してください。</p>
<p class="measurement-note">指定した空白区間だけを差し引いた値です。画像内の空白など、他の空白は除外していません。</p>
</div>
</details>'''


MEASUREMENT_SCRIPT = r'''(() => {
  const flow = document.getElementById("preview-flow");
  const reader = document.querySelector(".reader");
  const measurement = document.getElementById("preview-measurement");
  if (!flow || !reader || !measurement) return;

  const value = (name) => measurement.querySelector("[data-measure=\"" + name + "\"]");
  const set = (name, text) => {
    const node = value(name);
    if (node) node.textContent = text;
  };
  const pixels = (number) => Math.round(number) + " CSS px";

  const measure = () => {
    const flowBox = flow.getBoundingClientRect();
    const flowHeight = Number.isFinite(flowBox.height) ? flowBox.height : 0;
    const pauseHeight = Array.from(flow.querySelectorAll(".pause"))
      .reduce((total, node) => total + node.getBoundingClientRect().height, 0);
    const readerWidth = reader.getBoundingClientRect().width;
    const failedImages = Array.from(flow.querySelectorAll("img"))
      .filter((image) => image.complete && image.naturalWidth === 0).length;
    const metrics = {
      readerWidthCssPx: readerWidth,
      bodyHeightCssPx: flowHeight,
      explicitPauseHeightCssPx: pauseHeight,
      nonPauseHeightCssPx: Math.max(0, flowHeight - pauseHeight),
      renderedPanelCount: flow.querySelectorAll("figure.panel").length,
      devicePixelRatio: window.devicePixelRatio || 1,
      imageFailureCount: failedImages
    };
    measurement.dataset.metrics = JSON.stringify(metrics);
    set("reader-width", pixels(readerWidth));
    set("flow-height", pixels(flowHeight));
    set("pause-height", pixels(pauseHeight));
    set("non-pause-height", pixels(metrics.nonPauseHeightCssPx));
    set("panel-count", metrics.renderedPanelCount + " カット");
    set("dpr", String(metrics.devicePixelRatio));
    set("image-failures", String(metrics.imageFailureCount));
    const widthNote = value("width-note");
    if (widthNote) widthNote.hidden = Math.abs(readerWidth - 390) < 0.5;
  };

  const waitForImage = async (image) => {
    if (!image.complete) await new Promise((resolve) => {
      const finish = () => resolve();
      image.addEventListener("load", finish, {once: true});
      image.addEventListener("error", finish, {once: true});
    });
    if (typeof image.decode === "function") {
      try {
        await image.decode();
      } catch (_) {
        // The failure count is collected after the browser settles the image.
      }
    }
  };

  const waitForLayout = async () => {
    await Promise.all(Array.from(flow.querySelectorAll("img")).map(waitForImage));
    if (document.fonts && document.fonts.ready) {
      await document.fonts.ready.catch(() => {});
    }
    await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    measure();
  };

  window.addEventListener("resize", measure, {passive: true});
  if (typeof ResizeObserver === "function") {
    new ResizeObserver(measure).observe(reader);
  }
  measure();
  waitForLayout();
})();'''


def _render_document(manifest):
    beats = manifest["beats"]
    rendered = []
    index = 0
    while index < len(beats):
        beat = beats[index]
        if (beat["type"] in COMPOSITION_MEMBER_TYPES
                and beat.get("composition") is not None):
            composition = beat["composition"]
            members = []
            while (index < len(beats)
                   and beats[index]["type"] in COMPOSITION_MEMBER_TYPES
                   and beats[index].get("composition") == composition):
                members.append(beats[index])
                index += 1
            rendered.append(_composition_html(composition, members, manifest["referenceWidth"]))
            continue
        if beat["type"] == "panel" and beat.get("row") is not None:
            row = beat["row"]
            panels = []
            while index < len(beats) and beats[index]["type"] == "panel" and beats[index].get("row") == row:
                panels.append(_panel_html(beats[index]))
                index += 1
            rendered.append(f'<div class="panel-row" data-row="{html.escape(row, quote=True)}">{"".join(panels)}</div>')
            continue
        if beat["type"] == "panel":
            rendered.append(_panel_html(beat))
        elif beat["type"] == "pause":
            height = _style_number(beat["height"] / manifest["referenceWidth"] * 100)
            rendered.append(f'<div class="pause" data-beat-id="{html.escape(beat["id"], quote=True)}" '
                            f'aria-hidden="true" style="--beat-height:{height}cqw"></div>')
        else:
            rendered.append(_text_beat_html(beat, manifest["referenceWidth"]))
        index += 1
    notes = _purpose_notes(beats)
    title = html.escape(manifest["title"], quote=True)
    reference_width = _style_number(manifest["referenceWidth"])
    asset_json = _safe_json_script(manifest["assets"])
    return f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — ネーム確認用</title><style>{CSS}</style></head>
<body><main class="reader" style="--reference-width:{reference_width}px" aria-label="{title} ネーム確認用">
<header class="draft-bar"><span class="draft-badge">ネーム確認用・下書き</span>
<h1>{title}</h1><div class="draft-meta">{reference_width}px基準 / 360pxでも確認できる構成 preview</div></header>
{notes}
<div id="preview-flow">
{''.join(rendered)}
</div>
<footer class="end-note">構成確認用の下書きです。完成原稿・公開版ではありません。</footer>
{MEASUREMENT_HTML}
</main>
<script type="application/json" id="name-preview-assets">{asset_json}</script>
<script>
(() => {{
  const assets = JSON.parse(document.getElementById("name-preview-assets").textContent);
  document.querySelectorAll("img[data-asset]").forEach((image) => {{
    const source = assets[image.dataset.asset];
    if (source) image.src = source;
  }});
}})();
</script>
<script>{MEASUREMENT_SCRIPT}</script>
</body></html>
'''


def build_preview(manifest_path, output_path=None, force=False):
    source = Path(manifest_path).resolve()
    if not source.is_file():
        raise PreviewError(f"manifest does not exist: {source}")
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise PreviewError(f"invalid JSON at line {error.lineno}, column {error.colno}") from error
    manifest = _validate_manifest(data, source)
    output = Path(output_path).resolve() if output_path is not None else source.with_name("name-preview.html")
    if output == source:
        raise PreviewError("output must differ from the manifest")
    referenced_images = {
        beat["image"] for beat in manifest["beats"] if beat["type"] == "panel"
    }
    if output in referenced_images:
        raise PreviewError("output must differ from every referenced image")
    if output.exists() and not force:
        raise FileExistsError(f"output exists: {output}; use --force to replace it")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(_render_document(manifest), encoding="utf-8")
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="webtoon-name-preview/v1 JSON manifest")
    parser.add_argument(
        "--output", type=Path,
        help="self-contained HTML output (default: name-preview.html beside manifest)",
    )
    parser.add_argument("--force", action="store_true", help="replace an existing HTML output")
    args = parser.parse_args(argv)
    try:
        output = build_preview(args.manifest, args.output, args.force)
    except (OSError, PreviewError) as error:
        print(f"Cannot build name preview: {error}", file=sys.stderr)
        return 1
    print(f"Saved {output} (draft preview; supplied rough artwork bytes embedded unchanged)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
