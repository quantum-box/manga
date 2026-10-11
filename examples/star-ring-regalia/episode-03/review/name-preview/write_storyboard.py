# coding: utf-8
import json,sys,hashlib
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[5];ep=root/'examples/star-ring-regalia/episode-03';d=ep/'review/name-preview';plan=json.loads((d/'plan.json').read_text());panels=[b for b in plan['beats'] if b['type']=='panel'];dec={b['id']:b for b in json.loads((d/'layout-decisions.json').read_text())};balloons={b['targetPanel']:b for b in json.loads((d/'balloon-decisions.json').read_text())}
intro='# 第3話「星環の剣筋」構成ネーム\n\n状態：2026-10-11改稿。**未採用・本作画未着手**。第2話の最新版から続く。旧第3話への承認をこの改稿へ適用しない。\n\n## 構成\n\n| 区間 | 新しい動きと理解 | 絵のID |\n| --- | --- | --- |\n| 朝と再訪 | 日本の無傷の手からミルトの擦り傷と銅貨二枚へ。昨日の抜刀しかけた衝動を話す | 00-japan〜01-choice |\n| 動く稽古 | リゼが低く薙ぐ→盾が落ち足へ触れる→航が打ち返し空振り→外へ一歩を教わり受ける | 01-lesson〜01-spar |\n| 特別さの片鱗 | 弱い風に細い光が見える→異常に速く踏み込む→木剣を肩の手前で止める→リゼが驚く。再試行は普通に止められる | 02-flicker |\n| 星環 | 空の巨大な環と魔力の巡りという日常知識に触れる。降りている線を尋ねてもリゼには見えない | 02-star |\n| 巡回と実戦 | 先走った帰還者が消え、兵士が負傷。航が盾で守ると稽古の光が戻り、自分の剣で獣を退ける | 03-patrol〜05-recover |\n| 救護と次の一歩 | 身体を作り直せる帰還者と休養が必要な兵士。盾の傷を報告して返し、一閃を見た怜から討伐隊へ誘われる | 06-returner〜08-invitation |\n\n主筋は「守れなかった昨日の航が、稽古で自分だけの光を見て、実戦で一閃を決める」。道具の確認、指示と返事、救護後の供給説明の反復を削った。力は一度だけの速さと一撃で具体的に見せ、原因の説明や習得済みの魔法にはしない。怜は親切な先輩。誘いへの返答は第4話へ。\n\n## 連続性\n\n基点は第2話PR #93 / main bf149ef8。右掌の擦り傷、使わなかった銅貨二枚、抜刀を止められた経験を引き継ぐ。日本には傷や道具を移さない。赤髪の帰還者は第2話の金髪の加害者とは別人。\n\n稽古の木剣は右手、木盾は左。自分の鋼剣は左腰に納刀。木剣を返してから鋼剣を確かめて納め、予備盾を借りて巡回する。救助時は右鋼剣、左木盾。負傷兵の傷は右前腕。剣を納めてから支え、盾は拭いて訓練場の棚へ返す。原画に掌の小傷が省略された瞬間も治癒した意味にしない。\n\n星環は空全体に渡る自然の巨大な環。普通の人が知っている「魔力が巡ると言われている」という話までに留める。航だけに見える細い線は現在の魔力の流れで、未来や人の心ではない。最初の感応は稽古、初めての決定的な剣撃は救助。再現方法・起源・世界の真相・守護者の役割・水不足は明かさない。風の稽古は安全な弱い流れであり、リゼへ木剣を当てない。特別な動きの後も立って話せる。\n\n## 分量とレイアウト\n\n85有効コマ、独立した吹き出し60発話と絵に置く3発話。通常声48は尾つき、強い呼びかけ3はトゲ、心の声9は雲形と点。声・音・余白をコマへ数えない。目標は390 CSS pxの本編34,000〜60,000px、内容24,000px以上、80〜120有効コマ。実量はvalidation.jsonを参照。\n\n主動作は広く、足や視線は小さく、驚きは間を置く。稽古の接触・空振り・修正は近く読み、異常な踏み込みは100%幅、星環の空も100%幅。足跡と盾の返却は大小の接写を同じ場面空間へ組む。対話は縦の列を明示しスマホ幅で全文を読む。\n\n草の音→反応→停止→足場→無音900px→獣の姿という間を残す。ガサ…は原画に一度ありHTMLで重ねない。静けさは直前の動く稽古・巡回と対比する。\n\n## 演出参照\n\nwebtoonのaction-directionとname-preview、speech-balloonsを使用。橋上の一歩の薙ぎ・跳躍・反撃後、空を踏むの強化後の肘打ちと踏み切りを画像表示で参照。見せ場の起点→移動→接触または停止→結果を今回の稽古と救助へ移す。既存の決定打ラフを保ち、今回の稽古と星環は組み込みimage_genで3原画を追加した。PROMPT-motion.mdとgeneration.jsonへ実行指示と出所を記録。\n\n## コマごとの判断\n\n'
sections=[]
for i,p in enumerate(panels):
 id=p['id'];choice=dec[id];scene=id.split(':')[0]
 if scene.startswith('00-japan'):state='日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷'
 elif scene.startswith('00-yard') or scene.startswith('01-choice'):state='ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし'
 elif scene.startswith(('01','02-distance','02-retry','02-rest')):state='同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばう 教わった術式は未習得 星環の光へ初めて感応'
 elif scene.startswith('02-change'):state='訓練場 木剣をベンチへ返す 鋼剣の重さを確かめ納刀 予備の木盾を左で借りる'
 elif scene.startswith(('03','04','05')):state='ミルト川沿い 航は左木盾 右鋼剣/左腰の鞘 赤髪の帰還者は別人 現地兵の負傷は右前腕 川の水は正常'
 elif scene.startswith('06'):state='町の安全広場 帰還者は予備の服で再生成 失った剣は川辺の泥 灯里は弓と通信器 航の盾は借り物'
 else:state='町の診療所から訓練場へ徒歩 セナは現地兵の右前腕を治療 航の右掌の傷は残る 返却後は盾なし 自分の剣は左腰に納刀'
 ds='\n'.join(f"- {x['speaker']}／{x['kind']}／{choice['placement']}\n```\n{x['text']}\n```" for x in choice['dialogue']) or '- 発話なし'
 sounds='／'.join(x['text'] for x in p.get('sounds',[]))
 if id=='03-listen:1':sound='新しく鳴る ガサ… 草の原画に一度だけ 以後は同じ音の点へ減衰'
 elif id=='05-defense:3':sound='新しく鳴る ザンッ 刃が爪の魔力を断つ起点から斜めの軌跡へ 効果音は画像の爪や航の顔を隠さない'
 elif id.startswith('03-listen'):sound='前の草の音が続く 追加のガサを描かず 薄い点が止まるまで 警戒する目と手を優先'
 elif sounds:sound='新しく鳴る '+sounds+' 動作の接点へ置き 前の音と混同しない'
 else:sound='効果音を描かない 聞き手の表情と声または小さい動作の理解を優先 背景の音を追加しない'
 gaps=[g for g in plan['pureGaps'] if g['before']==id];gap='／'.join(f"{g['height']}px {g['purpose']} 次={g['after']}" for g in gaps) or '追加の純余白なし 動作または応酬を近く読む'
 previous=panels[i-1]['id'] if i else '第2話末尾の問い'
 emotion='発話相手へ求めること：'+p['purpose']+'。言い切れない本音は目・掌・姿勢に残し 次の返答や行動を読む。' if choice['dialogue'] else '新しい動作または反応：'+p['purpose']+'。次の行動の理由として見せる。'
 balloon=balloons.get(id)
 outline=(f"{balloon['reason']} 尾または点の方向={balloon['tail']} 対応人物={id} 無彩色" if balloon else '絵の通常声は細い楕円 制止は太い縁 心の声は点で区別 無言には追加しない 無彩色')
 sections.append(f"### {i+1:03d} {id}\n\n- 絵・新しい理解：{p['alt']}\n- 接続：{previous}の結果を受ける。{state}\n- 幅と配置：{p['widthPercent']}% {p['align']} 枠={p['frame']} 表示窓={p['crop']}"+(f" 場面空間={p['composition']} x={p['offsetX']} y={p['offsetY']}" if 'composition' in p else '')+f"\n- 音：{sound}\n- 余白：{gap}\n- 感情・意図：{emotion}\n- 声の輪郭：{outline}\n{ds}\n")
text=intro+'\n'.join(sections)
(d/'storyboard.md').write_text(text);(ep/'storyboard.md').write_text(text)
