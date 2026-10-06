#!/usr/bin/env python3
"""Prepare targeted native sound edits; never rewrite actual-used prompts."""
import json
from pathlib import Path
from panel_lettering import normalize_panel

ROOT=Path(__file__).resolve().parents[1]

def cue(text,cause,placement,design):
    return dict(text=text,cause=cause,placement=placement,design=design)

PANELS={
 '3-1':[cue('コツ コツ','冒険者の靴が石畳へ接地する','上の広いコマ、奥の歩く一団の足元の石畳。カイの腕や塔を避ける','小さな硬い灰黒色の描き文字。二拍の間を少し空ける')],
 '3-4':[cue('コツ','カイの靴が工房の石の敷居へ接地する','最下段、後ろ姿の靴に近い空いた石段','小さく硬い灰黒色の描き文字。靴と足の輪郭を隠さない')],
 '4-3':[cue('コト','セナが一本の試作剣を木の台へ置く','第三段、鍔・柄と台の接触に近い空いた木目。左のセリフと右の手を避ける','控えめな丸みのある黒の描き文字、細い淡色縁')],
 '6-2':[cue('コン','第一打の鋼の刃が木の標的へ当たる','第二段、左の刃と木の接触点の近く。刃・木片・顔・一回目のセリフを避ける','中程度の角張った黒い描き文字、淡色の細い縁。大爆発の音にしない')],
 '6-3':[cue('コン','第二打の鋼の刃が同じ木の標的へ当たる','第三段、左の木と刃の接触付近の空き。二回目のセリフを避ける','第一打と同じ重さの角張った描き文字、淡色の細い縁')],
 '8-3':[cue('カチッ','工具で小さな真鍮の蓋の固定が外れる','第三段、上の蓋と工具に近い暗い空き。刃じゃないのセリフ、指、工具、開口部を避ける','小さく硬い金属音の描き文字、黒に薄い明色縁')],
 '9-4':[cue('カリカリ','細い工具が溝の付着物をかき出す','細い斜めの工具接写、既存のカチの位置だけ。手・工具先・溝を避ける','小さく細いざらついた描き文字、二拍。既存のカチを置換')],
 '9-5':[cue('カチッ','カイが真鍮の蓋を元の場所へ固定する','最下段、押さえた蓋に近い作業台の空き。もう一回試そうのセリフと指を避ける','小さく硬い金属音、細い淡色縁')],
 '11-1':[cue('コン','カイの第一打が木の標的へ当たる','上の段、既存の白いコンの楕円を除去し、その近くの刃と標的の接触を示す空きへ','楕円・尾を除いた角張った黒の描き文字、細い白縁。自然に絵へなじませる')],
 '11-2':[cue('コン','カイの第二打が同じ木の標的へ当たる','第二段、既存の白いコンの楕円を除去し、同じ接触のそばの空きへ','第一打と同じ描き文字、細い白縁。吹き出しを付けない')],
 '11-3':[cue('スゥ…','修理後の鍔の溝から魔力の熱を逃がす淡い粒が抜ける','第三段、真鍮の溝と橙の粒の近くの暗い空き。握った手と溝を避ける','打撃より小さく細い柔らかな橙灰の描き文字、淡い縁。煙や炎を追加しない')],
 '12-1':[cue('ギュッ','カイが第三打の前に剣の柄を握り直す','最上段、握る手に近い暗い空き。指と柄と刃を避ける','小さく締まった黒い描き文字、淡い細縁')],
 '12-2':[cue('コン','三打目の刃が同じ木の標的へ当たる','第二段の既存のコンをそのまま保持','既存の描き文字を保持。新たなコンを重複させない')],
}

def main():
    ep=json.loads((ROOT/'episode-01/episode.json').read_text())
    if ep.get('sound_revision'):
        raise SystemExit('Sound edits already adopted. Preserve the executed manifest; use PROMPTS-NEXT.md for a new generation.')
    folder=ROOT/'production/sound-edits';folder.mkdir(exist_ok=True)
    manifest=[]
    scenes=sorted({int(key.split('-')[0]) for key in PANELS})
    for i in scenes:
        scene=ep['scenes'][i-1]
        spoken=[]
        for j,p in enumerate(scene['panels'],1):
            p=normalize_panel(p)
            if p['text']:spoken.append(f"Narrative panel {j}: {p['speaker']} — {p['text']}")
        prompt='''Use case: precise-object-edit. Edit the supplied CURRENT finished Japanese Webtoon strip. Change ONLY the specified drawn sound effects. Preserve the canvas aspect ratio, all panel frames and gutters, every face, expression, body, clothing, hand/fingers, weapon, vent, tools, props, colors, lighting, backgrounds, speech/thought balloons and their EXACT existing Japanese text. Do not regenerate or recompose the scene. Sound effects are drawn lettering near their source, outside speech/thought balloons; NO oval, cloud, tail, speaker label or new narration. Dialogue is vertically lettered, but sound orientation follows the action. Keep sounds modest and readable at 360px. Protect faces, fingers, the vent, contact points and existing words. No new action, sound source, smoke, explosion or extra sword. Keep every unlisted panel quiet, especially the listener reactions and relief.\n'''
        prompt+=f'Edit target: episode-01/{scene["file"]}. Scene: {scene["name"]}. There are {len(scene["panels"])} narrative panels; a same-row inset still has its own narrative index.\n'
        for j,p in enumerate(scene['panels'],1):
            for sound in PANELS.get(f'{i}-{j}',[]):
                prompt+=f"Narrative panel {j}. EXACT SFX: {sound['text']}. Cause: {sound['cause']}. Placement: {sound['placement']}. Style: {sound['design']}.\n"
        if i==11:prompt+='Remove ONLY the two white sound ovals around コン and reconstruct their small former background areas before drawing those two sounds unboxed. The fourth face panel must remain completely quiet.\n'
        if i==9:prompt+='Replace ONLY the existing scraping sound カチ with カリカリ; do not retain both. Add the separate カチッ only beside the final closed cover, never in the scraping panel.\n'
        if spoken:prompt+='Preserve exact existing dialogue/display text without any changes:\n'+'\n'.join(spoken)+'\n'
        file=folder/f'r{i:02d}.txt';file.write_text(prompt)
        manifest.append(dict(scene=i,source=scene['file'],destination=f'art/r{i:02d}-sounds.png',prompt_file=str(file.relative_to(ROOT)),prompt=prompt))
    design=dict(date='2026-10-07',scope='episode 1; dialogue and sound effects designed independently',panels=PANELS,quiet='Unlisted panels retain no drawn sounds; reaction, doubt, invitation and relief retain quiet.')
    (ROOT/'production/episode-01-sound-design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2)+'\n')
    (folder/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'Prepared {len(manifest)} targeted native edits, {sum(map(len,PANELS.values()))} sound cues. Reader unchanged.')

if __name__=='__main__':main()
