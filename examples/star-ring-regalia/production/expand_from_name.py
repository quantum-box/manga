#!/usr/bin/env python3
"""Prepare Episode 3 final artwork only from its adopted, verified full name."""
import copy
import json
from collections import OrderedDict
from prepare import ROOT, CAST, STYLE, prompt_for
from expand_opening import write
from narrative_alt import narrative_alt_text


def episode_three():
    directory = ROOT / 'episode-03'
    name = directory / 'review/name-preview'
    validation = json.loads((name / 'validation.json').read_text())
    assert validation['status'] == 'passed'
    assert validation['adoption']['status'] == 'adopted'
    assert validation['adoption']['scope'] == 'episode_03_name_only'
    source = json.loads((name / 'effective-panels.json').read_text())['panels']
    descriptions = json.loads((ROOT / 'production/episode-03-descriptions.json').read_text())
    assert len(source) == 96
    by_scene = OrderedDict()
    for panel in source:
        by_scene.setdefault(panel['id'].split(':')[0], []).append(panel)
    # One full shot in each odd-length scene keeps every two-shot unit consecutive.
    singles = {'00-japan': 0, '00-yard': 0, '01-lesson': 4, '01-grip': 0,
               '03-patrol': 0, '04-beast': 0, '04-find': 0, '05-defense': 2,
               '05-recover': 6, '06-supply': 4, '07-local': 0,
               '07-clinic': 0, '07-promise': 4, '08-invitation': 4}
    old_adoption = json.loads((directory / 'adoption.json').read_text())
    old_ep = json.loads((directory / 'episode.json').read_text())
    reference_by_scene = {key: old_adoption.get(key, key + '.png') for key in by_scene}
    ep = copy.deepcopy(old_ep)
    ep['revision_intent'] = ('96コマの全話ネームを2026-10-09の「続けて」で採用。'
                            '旧53の瞬間から、稽古の原因・修正・限界、借り物の責任、'
                            '救護の引き継ぎ、有限の再生成と装備の損失、現地兵の回復と仕事を深める。'
                            '56枚の原画へ96の異なる瞬間を一度ずつ割り当て、本作画で実量を再確認する。')
    ep['name_adoption'] = validation['adoption']
    ep['effective_panel_count'] = 96
    ep['regular_episode_requirements'] = {'reference_width_css_px': 390,
        'body_height_css_px': [34000, 60000], 'minimum_content_height_css_px': 24000,
        'effective_panels': [80, 120]}
    ep['assets'] = []
    ordinal = 0
    for key, panels in by_scene.items():
        groups = []
        cursor = 0
        while cursor < len(panels):
            is_single = singles.get(key) == cursor or (key == '02-rest' and cursor < 2)
            group = panels[cursor:cursor + (1 if is_single else 2)]
            groups.append(group)
            cursor += len(group)
        for group in groups:
            ordinal += 1
            asset_id = f'n{ordinal:02d}-{key}'
            asset = {'id': asset_id, 'episode': 3, 'location': group[0]['location'],
                     'gap_before_390': group[0]['gapBefore'],
                     'pacing_purpose': group[0]['newUnderstanding'],
                     'reveal': group[0]['id'] == '04-beast:1',
                     'name_panel_ids': [p['id'] for p in group],
                     'panels': [], 'path': str(directory / 'art' / (asset_id + '.png'))}
            for i, panel in enumerate(group):
                p = copy.deepcopy(panel)
                p['name_panel_id'] = p.pop('id')
                p['gap_inside_390'] = panel['gapBefore'] if i else 0
                if panel['id'] == '03-listen:2':
                    p['sound_continuations'] = [{'origin': '03-listen:1', 'text': 'ガサ…',
                        'placement': 'The single rustling inscription starts by reeds above; only its fading dots pass the gutter into the eye reaction. Never print a second ガサ.'}]
                if panel['id'] == '03-listen:2-added-1':
                    p['sound_continuations'] = [{'origin': '03-listen:1', 'text': '…',
                        'placement': 'Only a few pale trailing dots of the SAME earlier rustle beside the stop gesture; no new rustle inscription.'}]
                asset['panels'].append(p)
            asset['references'] = [str(CAST), str(directory / 'art' / reference_by_scene[key])]
            asset['narrative_description'] = descriptions[asset_id]
            asset['alt'] = narrative_alt_text(asset['narrative_description'], group)
            # Replace the earlier 3–4-shot canvas rule, not any dialogue or acting.
            prompt = prompt_for(ep, asset)
            prompt = prompt.replace('Source canvas tall approximately 1024x2560, characters in speech balloons at least 60 source pixels high, bold clean Japanese manga Gothic.',
                'Natural tall finished scroll canvas approximately 1024x1792 for TWO moments, or approximately 1024x1280 for ONE expressive scene. Medium-bold Japanese manga Gothic. Choose natural proportions for the specified acting, never pad the image to reach a length target.')
            prompt = prompt.replace('Use a tall page for 3-4 shots, varied shallow/large/staggered panels; one shot uses its own natural portrait composition, not stretched to the same height as multi-shot pages.',
                'Exactly the specified ONE or TWO successive moments. Two moments have generous acting space, alternate broad environmental views with offset closer panels, separated by a quiet irregular white gutter. Never a contact sheet or equal grid. A one-moment asset is a single composition, no extra reaction inset. Face, hand, boot and prop details remain readable.')
            prompt += ('\nReference 1 establishes identities and costume colors ONLY. Reference 2 is the adopted earlier finished style and location reference ONLY; do not copy its panel count, lettering, carried props or old actions. Draw only the named people in the specified moment. '
                'KOH own steel scabbard is at his anatomical LEFT hip, steel or wooden practice blade in anatomical RIGHT hand; the ONE borrowed wooden shield on anatomical LEFT arm only when the shot specifies it. No duplicated hilt, no shield in Japan, no second shield. LIZE carries NO shield in this episode; the only visible shield is her spare borrowed by KOH, or that same spare on the bench when he rests or returns it. '
                'The shield OUTSIDE face has plain wooden boards, a small metal boss and narrow metal rim. The INNER face has leather forearm strap and wooden hand grip, NO outside metal boss; never place straps across the exterior metal boss. Show INNER face when checking or teaching the straps. No glowing runes or cracks; after the wolf fight only one small rim scrape. '
                'In a BACK view KOH anatomical LEFT hip is on the viewer LEFT side; never draw the steel scabbard and hilt on the visible anatomical RIGHT hip. Hide the steel gear if its correct LEFT side lies outside the camera framing. '
                'LOCAL guard: gray hair, dark goatee, dull steel helmet, sand scarf, brown leather armor, cream sleeves. Injury is anatomical RIGHT forearm only; healthy LEFT hand and polearm. '
                'RED PLAYER: short red hair, bronze gear before defeat; plain beige replacement tunic and no sword/armor after regeneration. Gear stays in river mud. '
                'SENA is male38, auburn short hair and gentle stubble, oatmeal robe and olive vest. AKARI wears orange game jacket, orange hairclip, bow and brass communicator, no glasses. REI is honestly friendly, silver armor and deep red short cloak. '
                'Bright Saturday morning at the yard, midday river and supply stall, early afternoon clinic and final invitation; no sunset. No drought, guardian appearance, hidden real-world explanation or later event.')
            for p in asset['panels']:
                if p['gap_inside_390']:
                    prompt += f"\nBefore the following moment {p['name_panel_id']}, include a short natural white gutter corresponding to about {p['gap_inside_390']} CSS pixels at 390px reader width; keep speech tails and fading sounds connected to their source."
                for s in p.get('sound_continuations', []):
                    prompt += '\nContinuing sound: ' + s['placement']
            if any(p['name_panel_id'] == '00-japan:1' for p in asset['panels']):
                prompt += '\nPhone display exact HORIZONTAL words: 黒冠の守護者 / 討伐隊募集. Generic dark castle silhouette only; no visible guardian monster. No other readable phone/interface/background text.'
            asset['prompt'] = prompt
            ep['assets'].append(asset)
    assert len(ep['assets']) == 56
    assert set(descriptions) == {a['id'] for a in ep['assets']}
    assigned = [p['name_panel_id'] for a in ep['assets'] for p in a['panels']]
    assert assigned == [p['id'] for p in source] and len(set(assigned)) == 96
    return ep


if __name__ == '__main__':
    ep = episode_three()
    write(ep, scroll_notes='採用ネーム96コマの順序を守る。草のガサは一度だけ鳴り、目・停止・足の反応へ薄い点として続く。880pxの純余白の先で初めて獣を見せる。稽古の接触と実戦の接触は別の一回。',
          art_notes='通常話の実量を満たす本作画を56枚作る。前の原画は実際に使用する制作参照として保存し、公開の採用原画は今回の56枚に切り替える。ネームの検証と本作画の検証は別に記録する。')
    root = ROOT / 'episode-03'
    (root / 'review/name-preview/final-art-assignment.json').write_text(json.dumps([
        {'assetId': a['id'], 'panelIds': a['name_panel_ids'], 'gapBefore390': a['gap_before_390']}
        for a in ep['assets']], ensure_ascii=False, indent=2) + '\n')
