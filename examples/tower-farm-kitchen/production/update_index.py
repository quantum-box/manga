#!/usr/bin/env python3
"""Expose only visually reviewed episodes; leave future art explicitly pending."""
from pathlib import Path
import html
import json
import re

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
EPISODES = json.loads((BASE / 'production/episodes.json').read_text())
completed = []
for ep in EPISODES:
    d = BASE / f'episode-{ep["number"]:02d}'
    v = d / 'validation.json'
    if not v.exists():
        continue
    review = json.loads(v.read_text())
    if all(str(review.get(k, '')).startswith('passed') for k in ('artworkTextReview', 'continuityReview')):
        if (d / 'reader.html').exists() and (d / 'index.html').exists():
            completed.append(ep['number'])

bible = BASE / 'series/bible.md'
bible.write_text(re.sub(r'completed_art_episodes: \[[^\n]*\]', 'completed_art_episodes: ' + str(completed), bible.read_text()))

items = []
for ep in EPISODES:
    number = ep['number']
    label = f'第{number}話　{html.escape(ep["title"])}'
    if number in completed:
        items.append(f'<li><a href="episode-{number:02d}/index.html">{label}<span>読む →</span></a></li>')
    else:
        items.append(f'<li class="pending">{label}<span>制作中</span></li>')
first=json.loads((BASE/'episode-01/manifest.json').read_text())
cover = 'episode-01/' + next(scene['art'] for scene in first['scenes'] if scene['id']=='08-first-meal')
doc = '''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>塔の農夫は、英雄を食わせる</title><style>*{box-sizing:border-box}body{margin:0;background:#eee6d7;color:#342d24;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN",sans-serif}main{max-width:640px;margin:auto;background:#fffaf0;padding-bottom:56px}header{padding:36px 24px 24px}h1{font-size:30px;line-height:1.6;margin:12px 0}p{font-size:18px;line-height:1.9}header>small{font-size:16px;color:#60704c}.cover{width:100%;height:300px;object-fit:cover;object-position:50% 25%;display:block}ol{list-style:none;margin:0;padding:0 20px}li{border-bottom:1px solid #ded5c5;font-size:18px;line-height:1.8}li a,li.pending{display:block;padding:20px 4px}a{color:#355a3c;text-decoration:none}li span{display:block;font-size:15px;color:#677559;margin-top:6px}.pending{color:#8c8374}.pending span{color:#8c8374}</style></head><body><main>'''
doc += f'<img class="cover" src="{cover}" alt="エルナが食堂で温かい一皿をコウに渡す"><header><small>剣と魔法・農業・帰還食堂</small><h1>塔の農夫は、<br>英雄を食わせる</h1><p>塔の三階に召喚された農夫。<br>畑と食堂を立て直し、冒険者の明日の一皿をつくる。</p><small>第1〜10話：畑と帰還食堂</small></header><ol>{"".join(items)}</ol></main></body></html>'
(BASE / 'chapters.html').write_text(doc + '\n')

count = len(completed)
delivery_path = BASE / 'production/delivery.json'
delivery = json.loads(delivery_path.read_text()) if delivery_path.exists() else {}
delivery_passed = count == 10 and delivery.get('localVerification') == 'passed'
first_review=json.loads((BASE/'episode-01/validation.json').read_text())
screen_counts=[round(v['scrollHeight']/v['innerHeight']) for v in first_review['viewports']]
sounds=sum(len(s.get('soundEffects',[])) for s in first['scenes'])
(BASE / 'README.md').write_text(f'''# 塔の農夫は、英雄を食わせる

[話一覧を開く](chapters.html)。200話以上の指定に対して、初期ロードマップは240話。第1〜10話の脚本・絵コンテを制作し、現在{count}話が作画とスマホ確認まで完了。

塔の三階で行き場を失った農夫が、帰還食堂の料理人と畑・作付け・水・献立・補給を組み直す。農業と設備には材料、時間、費用、失敗の条件を持たせる。

| 資料 | 内容 |
| --- | --- |
| [設定入口](series/bible.md) / [ロードマップ](series/roadmap.md) | 世界・無双の形・240話の転換 |
| [人物](series/characters.md) / [世界](series/world.md) | 農夫、料理人、農家、技師、補給官と塔の制度 |
| [農業と設備](series/agriculture.md) / [一次資料](series/sources.md) | 排水、作付け、配水、分析、食数、収支の根拠と創作の仮値 |
| [料理の作画基準](series/food-art.md) | 美味しそうな形、艶と湯気、粒の密集を避ける生成指示と確認 |
| [導入10話](series/opening-arc.md) / [連続性](series/continuity.md) | 約六週間の時間経過、開示、各話の終了状態 |
| [制作台帳](production/status.md) | 完成・制作中・未確認の区別 |

各話の`index.html`は原画を直接読むリーダー、`reader.html`は原画のバイトを内包するリーダー。第1話は容量に合わせて同じフォルダーの`reader-art-*.js`三個を一緒に使う。第2〜10話は単独HTML。会話は原画内へ日本語の縦書きで統合し、HTMLで重ねて表示しない。原画・実際の生成指示・採用と修正の記録・両スマホ幅の全長画像・確認シートを各話へ保存する。公開サーバーへの配信はまだ行っていない。

第1話は長尺・効果音に加え、場所と帰還門を知る順序、水を頼んでから仕事の依頼を受ける順序を改稿。{len(first['scenes'])}場面、スマホ約{min(screen_counts)}〜{max(screen_counts)}画面、原画内の効果音{sounds}箇所。[改稿と確認の記録](production/episode-01-review.md)。第2〜10話も全編を改稿。73枚の新原画を334の表示窓で読み、質問・判断・実作業・反応をつなぐ。[改稿と確認の記録](production/remake/review.md)。
''')

rows = []
for ep in EPISODES:
    n = ep['number']
    d = BASE / f'episode-{n:02d}'
    m = json.loads((d / 'manifest.json').read_text())
    art_count = sum((d / s['art']).exists() for s in m['scenes'])
    art = '完了' if n in completed else f'作画{art_count}/{len(m["scenes"])}・確認中' if art_count else '未着手'
    review = '完了' if n in completed else '未完了'
    package = '完了' if n in completed else '未完了'
    rows.append(f'| {n} | 完了 | 完了 | {art} | {review} | {package} |')
remaining = [e['number'] for e in EPISODES if e['number'] not in completed]
next_work = f'第{remaining[0]}話から、残りの作画・スマホ確認・包装を続ける。' if remaining else ('第11話以降は未制作。240話ロードマップの次の仕事を脚本化する。' if delivery_passed else '導入10話の通読、カタログ・iOS同期、PRの最新CIを確認する。')
(BASE / 'production/status.md').write_text('''# 制作台帳

2026-10-07の指定：200話以上。下限200話、初期ロードマップ240話、初回の完成原稿は第1〜10話。続編改稿ブランチ `codex/farmer-episodes-remake`。第2〜10話の既存完成稿を全編置き換え。

| 段階 | 状態 |
| --- | --- |
| 1. 全体設計・導入10話の脚本 | 完了 |
| 2. 共通の人物・場所・文字基準 | 完了 |
| 3. 第1話の作画と品質確認 | 完了 |
| 4. 第2〜10話の制作 | ''' + ('完了' if count == 10 else '進行中') + ''' |
| 5. 全話通読・カタログ・iOS配布物 | ''' + ('完了' if delivery_passed else '未完了') + ''' |

| 話 | 計画 | 脚本・絵コンテ | 作画・文字 | 390/360確認 | パッケージ |
| --- | --- | --- | --- | --- | --- |
''' + '\n'.join(rows) + f'\n\n次の作業：{next_work}\n\nローカル検証の結果は [delivery.json](delivery.json)。最新HEADのCI・レビューは [PR #36](https://github.com/quantum-box/manga/pull/36) を正本とする。公開サーバー配信と実機確認は未実施。mainへの取り込みは上記PRの状態を参照。\n\n完成は採用画像を両幅で読み、全文・話者・道具・時間と状態を確認した話だけに付ける。画像生成の限界、未修正の文字、未検証の表示を完了として記録しない。\n')

continuity = BASE / 'series/continuity.md'
text = continuity.read_text()
for ep in EPISODES:
    marker = f'| {ep["number"]} | {ep["time"]} | {ep["state"]} | '
    text = re.sub(r'^\| '+str(ep['number'])+r' \|[^\n]+', marker + ('完成原稿で確認済み' if ep['number'] in completed else '脚本の予定。作画未確認') + ' |', text,flags=re.MULTILINE)
continuity.write_text(text)

root_readme = ROOT / 'README.md'
text = root_readme.read_text()
text = re.sub(r'## 企画中の作品\n\n- \[塔の農夫[^\n]*\n\n', '', text)
text = re.sub(r'^\| \[塔の農夫[^\n]*\n', '', text, flags=re.M)
entry = f'| [塔の農夫は、英雄を食わせる](examples/tower-farm-kitchen/chapters.html) | 剣と魔法・塔・農業・飲食店 | 完成作画とスマホ確認{count}話。全240話のロードマップと導入10話の脚本 |\n'
text = text.replace('| --- | --- | --- |\n', '| --- | --- | --- |\n' + entry, 1)
root_readme.write_text(text)
print(f'Visible completed episodes: {completed}; next: {next_work}')
