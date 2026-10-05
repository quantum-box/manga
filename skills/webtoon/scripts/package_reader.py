#!/usr/bin/env python3
"""Embed a comic's local artwork and plain CSS in one HTML file (stdlib only)."""
import argparse
import base64
import html
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".gif": "image/gif",
    ".avif": "image/avif",
}


class ReaderPackager(HTMLParser):
    def __init__(self, directory):
        super().__init__(convert_charrefs=False)
        self.directory = directory.resolve()
        self.parts = []
        self.image_count = 0
        self.stylesheet_count = 0
        self.in_style = False

    @staticmethod
    def check_css(css):
        if re.search(r"@import\b|url\s*\(", css, re.IGNORECASE):
            raise ValueError("CSS url() and @import are not supported; use plain CSS")

    def local_file(self, reference):
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            raise ValueError(f"External resource is not supported: {reference}")
        path = (self.directory / unquote(url.path)).resolve()
        if not path.is_relative_to(self.directory):
            raise ValueError(f"Resource must be within the HTML directory: {reference}")
        if not path.is_file():
            raise ValueError(f"Resource does not exist: {reference}")
        return path

    @staticmethod
    def tag_text(tag, attributes, self_closing=False):
        text = "<" + tag
        for name, value in attributes:
            text += " " + name
            if value is not None:
                text += '="' + html.escape(value, quote=True) + '"'
        return text + (" />" if self_closing else ">")

    def start_tag(self, tag, attributes, self_closing=False):
        values = dict(attributes)
        self.check_css(values.get("style", ""))
        if tag == "style":
            self.in_style = True
        if tag == "img":
            if values.get("srcset"):
                raise ValueError("Use one img src per scene; srcset is not supported")
            source = values.get("src")
            if not source:
                raise ValueError("An img element has no src")
            if not source.startswith("data:image/"):
                image = self.local_file(source)
                mime = MIME_TYPES.get(image.suffix.lower())
                if mime is None:
                    raise ValueError(f"Unsupported artwork format: {source}")
                encoded = base64.b64encode(image.read_bytes()).decode("ascii")
                embedded = f"data:{mime};base64,{encoded}"
                attributes = [(name, embedded if name == "src" else value)
                              for name, value in attributes]
            self.image_count += 1
            self.parts.append(self.tag_text(tag, attributes, self_closing))
        elif tag == "link" and "stylesheet" in values.get("rel", "").lower().split():
            reference = values.get("href")
            if not reference:
                raise ValueError("A stylesheet element has no href")
            css = self.local_file(reference).read_text(encoding="utf-8")
            self.check_css(css)
            if values.get("media"):
                css = "@media " + values["media"] + " {\n" + css + "\n}"
            css = re.sub(r"</style", r"<\\/style", css, flags=re.IGNORECASE)
            self.parts.append("<style>\n" + css + "\n</style>")
            self.stylesheet_count += 1
        else:
            self.parts.append(self.get_starttag_text())

    def handle_starttag(self, tag, attributes):
        self.start_tag(tag, attributes)

    def handle_startendtag(self, tag, attributes):
        self.start_tag(tag, attributes, True)

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False
        self.parts.append("</" + tag + ">")

    def handle_data(self, data):
        if self.in_style:
            self.check_css(data)
        self.parts.append(data)

    def handle_entityref(self, name):
        self.parts.append("&" + name + ";")

    def handle_charref(self, name):
        self.parts.append("&#" + name + ";")

    def handle_comment(self, data):
        self.parts.append("<!--" + data + "-->")

    def handle_decl(self, declaration):
        self.parts.append("<!" + declaration + ">")

    def handle_pi(self, data):
        self.parts.append("<?" + data + ">")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Editable HTML source")
    parser.add_argument("--output", type=Path, help="Default: reader.html beside input")
    parser.add_argument("--force", action="store_true", help="Replace an existing output")
    args = parser.parse_args()
    source = args.input.resolve()
    output = (args.output or source.with_name("reader.html")).resolve()
    if output == source:
        parser.error("Output must differ from the editable input")
    if output.exists() and not args.force:
        parser.error("Output exists; choose another path or use --force")
    try:
        packager = ReaderPackager(source.parent)
        packager.feed(source.read_text(encoding="utf-8"))
        packager.close()
        result = "".join(packager.parts)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Cannot package reader: {error}", file=sys.stderr)
        return 1
    # Read and validate all resources before writing so failures leave no partial output.
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(result, encoding="utf-8")
    print(f"Saved {output} ({packager.image_count} images, "
          f"{packager.stylesheet_count} stylesheets embedded; artwork bytes unchanged)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
