#!/usr/bin/env python3
"""Run the production SwiftUI reader's layout regression on an iPhone simulator."""

import argparse
import json
import os
from pathlib import Path
import platform
import plistlib
import subprocess
import tempfile
import time


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_ID = "com.quantumbox.manga.reader-scroll-test"


def run(*args, timeout=180):
    return subprocess.check_output(args, text=True, timeout=timeout).strip()


def create_simulator():
    runtimes = json.loads(run("xcrun", "simctl", "list", "--json", "runtimes"))["runtimes"]
    available = [r for r in runtimes if r["isAvailable"] and ".iOS-" in r["identifier"]]
    if not available:
        raise RuntimeError("Install an iOS simulator runtime in Xcode before running this check")
    runtime = max(available, key=lambda r: tuple(map(int, r["version"].split("."))))
    devices = runtime.get("supportedDeviceTypes") or json.loads(
        run("xcrun", "simctl", "list", "--json", "devicetypes")
    )["devicetypes"]
    device = next(d for d in devices if d["name"].startswith("iPhone"))
    return run("xcrun", "simctl", "create", f"Manga reader scroll test {os.getpid()}",
               device["identifier"], runtime["identifier"])


def build_app(directory, source_ref):
    app = directory / "ReaderScrollTest.app"
    chapter = app / "Webtoons/scroll-test"
    chapter.mkdir(parents=True)
    panels = "".join('<div class="panel" id="marker"></div>' if i == 12 else '<div class="panel"></div>'
                     for i in range(24))
    (chapter / "index.html").write_text(
        '<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<style>body{margin:0}.panel{height:400px;background:linear-gradient(white,orange);'
        'border-bottom:10px solid black}</style>' + panels, encoding="utf-8")
    info = {"CFBundleExecutable": "ReaderScrollTest", "CFBundleIdentifier": BUNDLE_ID,
            "CFBundleName": "ReaderScrollTest", "CFBundlePackageType": "APPL",
            "CFBundleVersion": "1", "CFBundleShortVersionString": "1.0",
            "LSRequiresIPhoneOS": True, "UILaunchScreen": {},
            "UIApplicationSceneManifest": {"UIApplicationSupportsMultipleScenes": False,
                                           "UISceneConfigurations": {}}}
    (app / "Info.plist").write_bytes(plistlib.dumps(info))
    sources = []
    for name in ("MangaApp.swift", "Catalog.swift"):
        relative = f"ios/Manga/Sources/{name}"
        source = run("git", "-C", str(ROOT), "show", f"{source_ref}:{relative}") if source_ref else (
            ROOT / relative).read_text(encoding="utf-8")
        if name == "MangaApp.swift":
            entry = "@main\nstruct MangaApp:"
            if source.count(entry) != 1:
                raise RuntimeError("Cannot locate the production app entry point")
            # Only replace the entry point; compile the complete production views unchanged.
            source = source.replace(entry, "struct MangaApp:", 1)
        target = directory / name
        target.write_text(source, encoding="utf-8")
        sources.append(str(target))
    sdk = run("xcrun", "--sdk", "iphonesimulator", "--show-sdk-path")
    architecture = platform.machine()
    run("xcrun", "--sdk", "iphonesimulator", "swiftc", "-sdk", sdk,
        "-target", f"{architecture}-apple-ios17.0-simulator", "-parse-as-library",
        *sources, str(ROOT / "scripts/test_reader_scroll.swift"), "-o", str(app / "ReaderScrollTest"))
    run("codesign", "--force", "--sign", "-", str(app))
    return app


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--simulator-udid", help="Use an existing simulator instead of creating a temporary one")
    parser.add_argument("--source-ref", help="Compile production sources from a Git ref for regression verification")
    args = parser.parse_args()
    simulator = None
    try:
        with tempfile.TemporaryDirectory(prefix="manga-reader-scroll-") as temporary:
            print("Building the production reader scroll test", flush=True)
            app = build_app(Path(temporary), args.source_ref)
            simulator = args.simulator_udid or create_simulator()
            devices = json.loads(run("xcrun", "simctl", "list", "--json", "devices"))["devices"]
            device = next(d for group in devices.values() for d in group if d["udid"] == simulator)
            if device["state"] != "Booted":
                run("xcrun", "simctl", "boot", simulator)
            print(f"Booting {device['name']} and checking top, middle, bottom", flush=True)
            run("xcrun", "simctl", "bootstatus", simulator, "-b")
            run("xcrun", "simctl", "install", simulator, str(app))
            container = Path(run("xcrun", "simctl", "get_app_container", simulator, BUNDLE_ID, "data"))
            result_file = container / "Documents/reader-scroll-result.json"
            result_file.unlink(missing_ok=True)
            run("xcrun", "simctl", "launch", simulator, BUNDLE_ID)
            deadline = time.monotonic() + 45
            while not result_file.exists():
                if time.monotonic() >= deadline:
                    raise RuntimeError("Reader scroll test exited or timed out without a result")
                time.sleep(0.5)
            result = json.loads(result_file.read_text(encoding="utf-8"))
            if not result["passed"]:
                raise RuntimeError(result["error"])
            print(f"PASS: {result['measurements']} layout samples across 18 bar transitions; "
                  f"maximum movement {result['maximumDelta']}pt on iOS {result['systemVersion']}", flush=True)
    finally:
        if simulator:
            if args.simulator_udid:
                subprocess.run(["xcrun", "simctl", "terminate", simulator, BUNDLE_ID], capture_output=True)
            else:
                subprocess.run(["xcrun", "simctl", "shutdown", simulator], capture_output=True)
                subprocess.run(["xcrun", "simctl", "delete", simulator], capture_output=True)


if __name__ == "__main__":
    main()
