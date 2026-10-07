#!/usr/bin/env python3
"""Prepare storyboards/prompts and package adopted raster-lettered Webtoon art."""
from pathlib import Path
import hashlib
import html
import json
import re
import struct
import subprocess
import sys

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
EPISODES = json.loads((BASE / 'production/episodes.json').read_text())
CHARACTERS = 'production/references/characters.png'
WORLD = 'production/references/world.png'
STYLE = '''Use case: illustration-story. Asset: finished full-color Japanese vertical-scroll Webtoon scene, including all exact dialogue and speech balloons. Create a tall portrait image, approximately 1:2 aspect ratio, suitable for full-width phone reading. Refined adult anime drawing, confident ink lines, natural proportions, warm earthy painted shading, appetizing food and precise practical tools. Pale warm ivory gutters. Do NOT draw a poster, a character lineup, a comic cover, or a uniform grid. Different panel sizes, wide situation views, narrow hand closeups and larger emotional panels as specified. Reference 1 defines only character identities and clothing; Reference 2 defines garden/diner architecture, materials and palette. Reference 3 is TYPOGRAPHY ONLY: match its large crisp vertical Japanese glyphs and generous balloon padding, never copy its scene, characters or panel arrangement. Do NOT copy reference layouts or draw every person in reference. Draw only people required by this scene. Kou is black-haired adult male farmer, brown jacket and dark green waist apron; Elna is red-brown-haired adult female cook, low ponytail, blue headscarf, cream blouse, brick-red skirt and off-white cooking apron; Balt is weathered older male farmer, gray hair, brown hat, olive work shirt; Iris is adult female technician, short navy hair, copper goggles on head, gray workwear; Leon is adult male supply officer, silver-gray hair, right eyebrow scar, navy cloak. Preserve practical clothing and distinct faces. No modern electronics, plastic irrigation tape, giant magic vegetables, gore, watermarks, invented labels or future events.
TEXT: Render ONLY the exact Japanese text specified below, integrated into the art. All spoken dialogue uses genuine vertical Japanese manga typesetting: upright glyphs top to bottom, columns read RIGHT TO LEFT, never rotate a horizontal sentence. Large clean black printed manga gothic, match Reference 3: actual glyph height about 75–85px per 1024px image width (roughly 26–30px at phone width). Text must visibly be this large, not nominal font metadata. Short dialogue uses large balloons with only two or three vertical columns, not tiny dense columns. Enlarge balloon and adjust composition rather than shrinking text. Generous white inner padding. Normal voice: thin clean oval or softly rounded rectangular balloon with tail toward the correct speaker's mouth. Gentle voice: soft slightly irregular outline and thin tail. Thought: cloud with small dots toward thinker, no speech tail. Distinct sequential shots, not duplicate simultaneous characters. Balloon order follows the stated dialogue order DOWNWARD, with right-to-left ordering only within one horizontal panel row. Faces, hands and clues stay visible. Do not display speaker names, column labels, quotation marks, extra explanations or repeated dialogue. Effect sounds alone can be shaped freely beside their physical source. Any plain notebook, diagram, menu or contract in scene has abstract marks only unless explicit text is provided. The garden is inside a tower with glowing ceiling ribs, NOT under an open sky. Plant size, damaged sections, tools and dishes must match the stated time and condition.'''

def columns(text):
    # Verbatim text is authoritative; these columns describe reading order.
    return [text[i:i+7] for i in range(0, len(text), 7)]

def prompt_for(episode, scene):
    ident, description, dialogue, layout, pause = scene[:5]
    options = scene[5] if len(scene) > 5 else {}
    positive = re.sub(r'not (Kou|Elna|Balt|Iris|Leon)', '', description)
    speakers = {'コウ':'Kou','コウ心':'Kou','コウ・心':'Kou','エルナ':'Elna','バルト':'Balt','イリス':'Iris','レオン':'Leon'}
    voiced = {speakers.get(speaker) for speaker,line in dialogue}
    cast = [name for name in ('Kou','Elna','Balt','Iris','Leon') if name in voiced or re.search(r'\b'+name+r'\b',positive)]
    absent = [name for name in ('Kou','Elna','Balt','Iris','Leon') if name not in cast]
    parts = [STYLE, f'EPISODE TIME AND STATE: {episode["time"]}. {episode["state"]}',
             'CAST LOCK: The ONLY main-reference characters allowed in this image are: '+', '.join(cast)+'. '+
             'Do NOT depict these absent reference characters anywhere, including background: '+', '.join(absent)+'. '+
             'Other people appear only if this scene explicitly describes an ordinary clerk, customer, trader or squad. Never add a supporting cast group because it appears in the identity reference.',
             f'SCENE: {description}', 'EXACT TEXT IN READING ORDER:']
    for speaker, line in dialogue:
        voice = 'thought, cloud with dots' if '心' in speaker else 'spoken, tail to speaker'
        if speaker == '効果音':
            parts.append(f'Physical sound only, exact text: {line}. Near the outlet where air and water move; no speech balloon.')
        else:
            parts.append(f'Speaker {speaker} ({voice}). Exact full text: {line}\nVertical columns from RIGHT to LEFT: ' + ' / '.join(columns(line)))
    parts.append('Do not depict any event outside this scene. Prior and future events are continuity constraints only, not additional panels.')
    for sound in options.get('soundEffects', []):
        parts.append(f'Exact sound effect: {sound["text"]}. Physical source: {sound["source"]}. Placement and drawn style: {sound["placement"]}. No speech balloon or speaker tail. Keep hands, faces and spoken text visible.')
    if not dialogue:
        parts.append('No dialogue or thought balloons. Render the specified sound effects only; a scene without dialogue is not automatically soundless.')
    return '\n\n'.join(parts)

def prepare():
    opening = ['# 導入10話 — 畑と帰還食堂', '',
       '全体200話以上、初期設計240話。導入は約六週間。各話の場面数は画像枚数であり、コマ数を固定する指定ではない。', '',
       '## 各話の因果と満足', '', '| 話 | 時間 | 変化・今回の成果 | 次へ渡すもの |', '| --- | --- | --- | --- |']
    for ep in EPISODES:
        number = ep['number']; directory = BASE / f'episode-{number:02d}'
        (directory / 'art').mkdir(parents=True, exist_ok=True)
        (directory / 'generation').mkdir(exist_ok=True)
        previous = json.loads((directory/'manifest.json').read_text()) if (directory/'manifest.json').exists() else {'scenes':[]}
        adopted = {s['id']:s['art'] for s in previous['scenes'] if (directory/s['art']).exists()}
        previous_by_slug = {s['id'].split('-', 1)[1]:s for s in previous['scenes']}
        storyboard = [f'# 第{number}話：{ep["title"]}', '', f'時間：{ep["time"]}',
                      f'開始・終了の変化：{ep["change"]}', f'状態：{ep["state"]}', '',
                      '共通参照：[人物](../production/references/characters.png)、[場所](../production/references/world.png)、[文字基準](../production/references/lettering.png)。',
                      '会話は画像内へ縦書きで統合。セリフ全文、話者、列順は下記を正本とする。', '']
        prompts = [f'# 第{number}話 — 実際に画像生成へ渡す指示', '',
                   '方式：組み込み image_gen。原画、吹き出し、日本語の縦書き会話を一体生成。',
                   '参照は人物の同一性・衣装と場所・絵柄用。参照画の配置は引き継がない。', '']
        manifest = []
        for index, scene in enumerate(ep['scenes'], 1):
            ident, desc, dialogue, layout, pause = scene[:5]
            options = scene[5] if len(scene) > 5 else {}
            prior_scene = previous_by_slug.get(ident, {})
            name = prior_scene.get('id', f'{index:02d}-{ident}')
            prompt = prompt_for(ep, scene)
            prompt_path=directory/prior_scene.get('prompt',f'generation/{name}.prompt.txt')
            if name in adopted and prompt_path.exists():
                prompt=prompt_path.read_text()
            else:
                prompt_path.write_text(prompt)
            storyboard += [f'## {index:02d}：{ident}', '', f'見せる情報・カメラ・接続：{desc}',
                f'画面構成：{layout}。画面内に描く人物は上記場面の指定に従う。ほかの人物を退場扱いしない。',
                f'間：次へ{pause}px相当（390px表示を基準とする組版初期値。完成後に通読して調整）。',
                '伏せる情報：この場面より後の出来事。未収穫の作物、未合意の契約、未来の設備を先に描かない。', '',
                '| 順 | 話者 | 全文 | 縦列：右→左 |', '| --- | --- | --- | --- |']
            for order, (speaker, line) in enumerate(dialogue, 1):
                storyboard.append(f'| {order} | {speaker} | {line} | {" / ".join(columns(line))} |')
            storyboard += ['', '原画採用・日本語・顔・手・道具・前後の状態・両スマホ幅の確認は `validation.json` と生成記録へ残す。', '']
            if prior_scene.get('narration'):
                storyboard += ['画像内の時刻表示：'+'、'.join(prior_scene['narration']), '']
            if options:
                storyboard += [f'表示幅：{options.get("canvasWidthPercent", 100)}%、位置：{options.get("alignment", "center")}。',
                    'スクロールの役割：'+options.get('scrollPurpose', ''),
                    '効果音：'+' / '.join(f'{s["text"]}（{s["source"]}）' for s in options.get('soundEffects', [])), '']
            prompts += [f'## {name}', '', '```text', prompt, '```', '']
            manifest.append({**prior_scene,**options,'id':name,'art':adopted.get(name,f'art/{name}.png'),'dialogue':dialogue,'layout':layout,
                'pauseAt390':pause,'prompt':str(prompt_path.relative_to(directory)),'description':desc})
        primary_prompts = {s['prompt'] for s in manifest}
        for record_file in sorted((directory/'generation').glob('*.json')):
            record = json.loads(record_file.read_text())
            relative_prompt = record.get('prompt_file')
            if relative_prompt and relative_prompt not in primary_prompts:
                actual_prompt = directory/relative_prompt
                if actual_prompt.exists():
                    prompts += [f'## 実際の追加生成：{record_file.stem}', '', '```text', actual_prompt.read_text(), '```', '']
        (directory / 'storyboard.md').write_text('\n'.join(storyboard))
        (directory / 'PROMPTS.md').write_text('\n'.join(prompts))
        (directory / 'manifest.json').write_text(json.dumps({'number':number,'title':ep['title'],
             'time':ep['time'],'state':ep['state'],'scenes':manifest},ensure_ascii=False,indent=2)+'\n')
        opening.append(f'| [{number}話：{ep["title"]}](../episode-{number:02d}/storyboard.md) | {ep["time"]} | {ep["change"]} | {ep["state"]} |')
    opening += ['', '## 導入の局地的な決着', '',
       '第10話で、排水・作付け・給水・仕入れ・献立・小口納品の経験をつなぎ、16食の営業枠と共同経営を成立させる。全48m²の年間安定供給、七階での栽培、町全体への補給はまだ達成しない。', '',
       '## 開示と伏線', '',
       'T01（根と排水）は1〜2話、T02（塔内の調達・輸送）は3・6・9話、T04（店の継続）は3〜10話で仕事から開示する。T03（環境制御）の真相は伏せ、光の場所差と栽培の遅れを7話へ置く。', '',
       '三階の光や水の違いには日常の条件もある。7話の生育差だけで環境装置の異変を断定しない。', '',
       '## 連続性', '',
       '最初の播種は7日目。35日目に育った二区画8m²を収穫し、遅い一区画は残す。36日目の12食は三階集結所への一便。42日目の営業枠16食は自給と仕入れを合わせる。図表の栽培28日や収量は創作上の仮値として扱う。']
    (BASE/'series/opening-arc.md').write_text('\n'.join(opening)+'\n')
    print(f'Prepared {len(EPISODES)} storyboards and {sum(len(e["scenes"]) for e in EPISODES)} scene prompts')

def package(number):
    directory = BASE / f'episode-{number:02d}'
    ep = EPISODES[number-1]
    manifest = json.loads((directory/'manifest.json').read_text())
    scenes = []
    for scene in manifest['scenes']:
        path = directory / scene['art']
        if not path.exists():
            raise FileNotFoundError(path)
        header=path.read_bytes()[:24]
        assert header[:8]==b'\x89PNG\r\n\x1a\n'
        width,height=struct.unpack('>II',header[16:24])
        scene['width']=width;scene['height']=height
        scene['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        alt=scene['description']+' '+' '.join(f'{speaker}「{line}」' for speaker,line in scene['dialogue'])
        if scene.get('narration'):
            alt+=' 時刻表示：'+'、'.join(scene['narration'])
        alt+=' '+' '.join(f'効果音「{s["text"]}」：{s["source"]}' for s in scene.get('soundEffects', []))
        display_width=scene.get('canvasWidthPercent',100)
        alignment=scene.get('alignment','center')
        scenes.append(f'<figure class="scene {scene["layout"]} align-{alignment}" id="{scene["id"]}" style="--scene-width:{display_width}%;--pause:{scene["pauseAt390"]/390*100:.2f}cqw"><img src="{scene["art"]}" width="{width}" height="{height}" alt="{html.escape(alt,quote=True)}"></figure>')
    css='''*{box-sizing:border-box}html{background:#e9e2d6;color:#312d26;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN",sans-serif}body{margin:0}main{max-width:720px;margin:auto;background:#fffaf0;container-type:inline-size}header{padding:80px 24px 70px;text-align:center}header h1{font-size:clamp(25px,7cqw,42px);line-height:1.5;margin:14px 0}header p{font-size:18px;line-height:1.7}.series-title{font-size:16px;color:#62684b}figure{margin:0 0 var(--pause);padding:0}figure img{display:block;width:100%;height:auto}footer{text-align:center;padding:60px 24px 80px;font-size:18px;line-height:2}a{color:#3a5d41}nav{display:flex;justify-content:center;gap:24px;flex-wrap:wrap}small{display:block;font-size:15px;color:#6f705d}'''
    css+='figure{width:var(--scene-width,100%)}.align-center{margin-left:auto;margin-right:auto}.align-right{margin-left:auto;margin-right:0}.align-left{margin-left:0;margin-right:auto}'
    (directory/'reader.css').write_text(css+'\n')
    prev=f'<a href="../episode-{number-1:02d}/index.html">前の話</a>' if number>1 else ''
    nxt=f'<a href="../episode-{number+1:02d}/index.html">次の話</a>' if number<10 else ''
    # Every episode remains standalone for offline bundling; navigation uses JS
    # links rather than external assets, which the bundler does not crawl.
    title=html.escape(ep['title'])
    doc=f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第{number}話 {title}｜塔の農夫は、英雄を食わせる</title><link rel="stylesheet" href="reader.css"></head><body><main><header><span class="series-title">塔の農夫は、英雄を食わせる</span><p>第{number}話</p><h1>{title}</h1><small>{html.escape(ep["time"])}</small></header>{''.join(scenes)}<footer><p>第{number}話 おわり</p><nav>{prev}<a class="series-index" href="../chapters.html">話一覧</a>{nxt}</nav></footer></main><script>if(window.webkit?.messageHandlers?.mangaReader)document.querySelector('.series-index')?.remove();</script></body></html>'''
    (directory/'index.html').write_text(doc)
    (directory/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    subprocess.run([sys.executable,str(ROOT/'skills/webtoon/scripts/package_reader.py'),str(directory/'index.html'),'--output',str(directory/'reader.html'),'--force'],check=True)
    if (directory/'reader.html').stat().st_size >= 100*1024*1024:
        from compact_reader import compact
        compact(directory/'reader.html')
    (directory/'README.md').write_text(f'# 第{number}話：{ep["title"]}\n\n[読む](index.html) / [単独リーダー](reader.html) / [絵コンテ](storyboard.md) / [生成指示](PROMPTS.md)\n\n原画、吹き出し、日本語の縦書き会話を組み込みimage_genで一体生成。確認範囲と未確認事項は[validation.json](validation.json)へ記録。\n')
    print(f'Packaged episode {number}')

if __name__=='__main__':
    if len(sys.argv)==1 or sys.argv[1]=='prepare':prepare()
    else:
        for arg in sys.argv[1:]:package(int(arg))
