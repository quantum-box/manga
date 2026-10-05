"""Build Zero Break episode readers from saved, unmodified generated artwork."""
from pathlib import Path
import hashlib
import html
import json
from struct import unpack
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = ROOT.parents[1]

def execution_prompt(shot, record):
    original = record.get('originalPrompt')
    if not original: return shot['prompt']
    return 'Original generation prompt:\n' + original + '\n\nAdopted targeted edit prompt:\n' + record['prompt']

CSS = """*{box-sizing:border-box}body{margin:0;background:#18202b;color:#25364b;font-family:'Hiragino Kaku Gothic ProN','Yu Gothic',sans-serif}.episode{width:100%;max-width:480px;margin:auto;container-type:inline-size;background:var(--paper)}header{padding:42px 24px 40px;background:#111a29;color:#edf8ff}header small{font-size:12px;letter-spacing:.1em;color:#a3d8ec}h1{font-size:clamp(29px,8cqw,39px);line-height:1.4;margin:15px 0 10px}header p{font-size:15px;line-height:1.8;margin:0}.scene{margin:0;position:relative}.scene img{display:block;width:100%;height:auto}.left,.right{width:96%}.left{margin-right:auto}.right{margin-left:auto}.bleed{width:100%}.pause{height:var(--pause)}footer{padding:42px 24px 65px;text-align:center;font-size:15px;line-height:2.2}footer a{color:#365f8a;display:inline-block;margin:8px 12px}.pending{padding:30px;background:#f9e8dc}.catalog{max-width:720px;margin:auto;padding:30px 20px;color:#eef8ff}.catalog h1{font-size:32px}.catalog p{line-height:1.9}.catalog nav{display:grid;gap:12px}.catalog nav a{display:block;background:#233b52;border:1px solid #456981;padding:18px 20px;border-radius:8px;color:#fff;text-decoration:none}.catalog small{display:block;color:#a4cddc;font-size:13px;margin-top:8px}.catalog>a{color:#abdfff}"""


def build_episode(number):
    directory = ROOT / f"episode-{number:02d}"
    manifest = json.loads((directory / "manifest.json").read_text())
    records = []
    for shot in manifest["shots"]:
        saved = directory / "generation" / (Path(shot["file"]).stem + ".json")
        image = directory / "art" / shot["file"]
        if image.is_file() and saved.is_file():
            record = json.loads(saved.read_text())
            if hashlib.sha256(image.read_bytes()).hexdigest() != record["sha256"]:
                raise ValueError(f"Artwork differs from saved generation record: {image}")
            shot.update(status="generated", sha256=record["sha256"],
                        references=record["references"], prompt=record["prompt"])
            records.append(dict(record, id=shot["id"]))
    (directory / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    (directory / "generation-log.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    recorded = {record["file"]: record for record in records}
    (directory / "PROMPTS.md").write_text(
        f"# 第{number:02d}話 {manifest['title']} — 作画指示と実行記録\n\n"
        "方式：組み込み image_gen。採用原画のハッシュと参照は generation-log.json。\n\n"
        + "\n\n".join(
            "## " + s["file"] + "\n\n状態：" + s["status"] + "\n\n参照："
            + ", ".join(s.get("references", [])) + "\n\n```text\n" + execution_prompt(s, recorded.get(s["file"], {})) + "\n```"
            for s in manifest["shots"]
        ) + "\n"
    )
    paper = "#fffaf3" if number in (4, 9) else "#f6f7f8" if number == 5 else "#f7fbff"
    out = [f'<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ゼロ・ブレイク 第{number}話 {html.escape(manifest["title"])}</title><style>{CSS}</style><main class="episode" style="--paper:{paper}">',
           f'<header><small>異世界転生 × スーパーヒーロー / 第{number}話</small><h1>ゼロ・ブレイク</h1><p>{html.escape(manifest["title"])}</p></header>']
    pending = []
    for shot in manifest["shots"]:
        image = directory / "art" / shot["file"]
        if not image.is_file():
            pending.append(shot["id"])
            out.append(f'<div class="pending">制作中：{html.escape(shot["id"])}</div>')
            continue
        width, height = unpack(">II", image.read_bytes()[16:24])
        alt = shot["scene"] + " " + " ".join(l["speaker"] + "『" + l["text"] + "』" for l in shot["lines"])
        out.append(f'<figure class="scene {shot["shape"]}" id="{shot["id"]}"><img src="art/{shot["file"]}" width="{width}" height="{height}" alt="{html.escape(alt, quote=True)}"></figure>')
        out.append(f'<div class="pause" aria-hidden="true" style="--pause:{round(shot["pause"] / 390 * 100, 2)}cqw"></div>')
    previous = f"../episode-{number-1:02d}/index.html"
    navigation = f'<a href="{previous}">前の話</a>'
    if number < 10:
        navigation += f'<a href="../episode-{number+1:02d}/index.html">第{number+1}話へ</a>'
    out.append(f'<footer>第{number}話 おわり<br>{navigation}</footer></main></html>')
    (directory / "index.html").write_text("".join(out))
    if not pending:
        subprocess.run([sys.executable, str(REPOSITORY / "skills/webtoon/scripts/package_reader.py"),
                        str(directory / "index.html"), "--output", str(directory / "reader.html"), "--force"], check=True)
    print(f"Episode {number}: {len(manifest['shots'])-len(pending)}/{len(manifest['shots'])} artwork saved")
    return manifest


numbers = list(map(int, sys.argv[1:])) or list(range(2, 11))
for number in numbers:
    build_episode(number)
links = ['<a href="v5/index.html">第1話　最弱判定、最強の一歩。<small>完成版・縦書き30場面</small></a>']
for number in range(2, 11):
    directory = ROOT / f"episode-{number:02d}"
    manifest = json.loads((directory / "manifest.json").read_text())
    validation = directory / "validation.json"
    complete = validation.is_file() and json.loads(validation.read_text()).get("visualReview", {}).get("status") == "passed"
    status = f'完成版・縦書き{len(manifest["shots"])}場面' if complete else "制作中"
    links.append(f'<a href="episode-{number:02d}/index.html">第{number}話　{html.escape(manifest["title"])}<small>{status}</small></a>')
(ROOT / "chapters.html").write_text(
    f'<!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ゼロ・ブレイク 第1〜10話</title><style>{CSS}</style><main class="catalog"><h1>ゼロ・ブレイク</h1><p>異世界転生 × スーパーヒーロー<br>全50話の物語、最初の10話。</p><nav>'
    + "".join(links) + '</nav><p><a href="series/index.html" style="color:#abdfff">全50話の場面脚本を読む</a></p></main></html>'
)
