import json,sys,hashlib
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[5];ep=root/'examples/star-ring-regalia/episode-03';d=ep/'review/name-preview';plan=json.loads((d/'plan.json').read_text());panels=[b for b in plan['beats'] if b['type']=='panel'];dec={b['id']:b for b in json.loads((d/'layout-decisions.json').read_text())}
intro='''# 第3話「戻れる剣、戻れない剣」構成ネーム

状態：2026-10-11の第2話最新版から続く新しい構成。**未採用・本作画未着手**。旧第3話への2026-10-09の承認を、この変更の承認として扱わない。旧完成原稿の配布・公開データは、このネームの採用と完成版の検証が終わるまで差し替えない。

## 構成

| 区間 | 変化 | 絵のID |
| --- | --- | --- |
| 土曜の朝と再訪 | 日本の無傷の手から、ミルトで残る擦り傷と銅貨二枚へ。昨日の自分の行動をリゼに話す | 00-japan〜01-choice |
| 稽古 | 剣道の両手握りが盾を邪魔する。肘と足を修正して一度受け、限界と休憩を覚える | 01-lesson〜02-rest |
| 借り物と巡回 | 木剣を返して鋼剣を安全に納める。予備の木盾を借りて、返す場所を確認して川へ歩く | 02-change〜03-listen |
| 川辺の獣 | 別の赤髪の帰還者が先走り身体を失う。航は兵士を盾で守り、航だけに魔力の筋が見え 自分の一閃で獣を退ける リゼも驚く | 04-beast〜05-recover |
| 戻れる身体と戻らない仕事 | 帰還者の再生成には用意が必要。装備は戻らず、兵士の右前腕は治療と休養が必要 | 06-returner〜07-clinic |
| 結果と誘い | 盾の傷を隠さず持ち主へ見せ、棚へ返す。次の稽古を頼んだ航へ、怜が討伐隊に誘う | 07-promise〜08-invitation |

冒頭の問いは「昨日 抜いたあとに何ができたのか」。今回の成果は航の特別な一閃で獣を退け、負傷兵を生きたまま休める場所へ運ぶこと。昨日の加害者との決着は先へ残す。怜は本当に親切な先輩として登場する。参加の返答と討伐隊の詳細は第4話へ残す。

## 第2話からの連続性

基点はPR #93のmain bf149ef8c0a0b3f5de0233e54d307e598794d967。第1話の最新完成稿と、第2話の採用ネーム・adoption.json・layout-decisions.json・layout-revision.md、seriesのbible/world/characters/opening-arc/roadmap/continuityを確認。

- 日本の航の身体には傷を移さない。ミルトでの右手掌の擦り傷は残す。手首と手の甲の負傷へ変えない。旧ラフの細部に傷が省略されるカットも、状態が回復した意味にはしない。本作画では見える掌へ同じ傷を引き継ぐ。
- 銅貨二枚は使わず小袋へ戻す。日本への持出し、パンの購入、補給品の支払いに流用しない。
- 第2話の荷運び人の右手首は未治癒。加害者への対応を勝手に決着させない。第3話の赤髪の帰還者は第2話の金髪の加害者とは別人。
- 航の剣は右手、鞘は左腰。木剣を返してから鋼剣へ持ち替える。予備の木盾は左。リゼは短剣と風。航は稽古で魔法を習得したのではなく、救助中に星環共鳴が初めて発現する。訓練は痛みを隠さず途中で止められる条件から始める。
- 再生成は帰還者の身体だけ。無限の供給や自動の装備回収を足さない。現地兵の右前腕をセナが治療し、仕事の代役も決める。町の川は正常。水不足・守護者の姿と役割・独立した世界の真相は先出ししない。

## 分量とレイアウト

全話104の異なる動作・理解・選択・結果を計上。声・音・純余白を有効コマへ足さない。目標は390 CSS pxの本編34,000〜60,000px、内容24,000px以上、80〜120有効コマ。実量はvalidation.jsonを正本とする。2026-10-11の主人公の特別さを加えた再計測を参照。

72発話を白地に独立、4発話を身体動作や短い反応の絵へ。17原画の使える訓練・救護ラフを無加工で参照し、接続と稽古前の告白・共鳴の一閃を3原画で追加。原画の枚数とコマ数を混同しない。読みやすい縦列で句読点を使わず、自然な問いと制止には？と！を残す。

5か所で大きな絵と脇の小さな接写・白地の返答を同じ場面の空間へ置く。単純な全幅のカード列に揃えない。右側の小カットから始める横並びは、この話では無理に追加せず、JSONの順と縦の位置で読順を指定。主動作は広く、手・足の理解は小さく、救助後は密度を落とす。

純余白20か所にはplan.json/pureGapsのID、前後、役割、高さを対応。獣の直前は草の音→航の反応→リゼの停止→足場を選ぶ→900pxの無音の間→姿。ガサ…は原画内に一度あり、同じ言葉をHTMLに重ねない。続く点は同じ音の減衰で、二度目の草の音にはしない。

## 演出参照と適用

webtoonスキルのname-preview、episode-length、approved-example、scroll-pacing、whitespace-example、emotion-and-causality、speech-balloons、action-directionを読了。approved-webtoon、spacious-before/after、zero-breakの全長と音→通知→光→出現の390px連続窓、橋上の一歩の薙ぎ→跳躍→反撃後、空を踏むの肘打ちと跳躍の強化後を画像で確認。

使った判断：短い稽古の失敗と修正は近く読む。質問の返答、獣の発見、救護後の理解と盾の返却には違う長さの間を置く。独立した声が先に届き表情が後に現れる順、主動作の起点→接触→撤退の結果、人物を描かない沈黙を選ぶ。作例の内容や枚数は転用しない。

## コマごとの判断

改行は縦書きの列区切り。音の発生と継続は別に記録。無言を無音と同義にしない。

'''
sections=[]
for i,p in enumerate(panels):
 id=p['id'];choice=dec[id];scene=id.split(':')[0]
 if scene.startswith('00-japan'):state='日本 土曜の朝 パーカーと白いシャツ ヘッドセット以外の異世界の道具なし 身体は無傷'
 elif scene.startswith('00-yard') or scene.startswith('01-choice'):state='ミルト 訓練場に徒歩で到着 右掌の擦り傷 銅貨二枚 初期剣は左腰に納刀 盾まだなし'
 elif scene.startswith(('01','02-distance','02-retry','02-rest')):state='同じ訓練場 航は左木盾 右木剣 自分の鋼剣は左腰に納刀 右掌の傷をかばい 魔法なし'
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
 sections.append(f"### {i+1:03d} {id}\n\n- 絵・新しい理解：{p['alt']}\n- 接続：{previous}の結果を受ける。{state}\n- 幅と配置：{p['widthPercent']}% {p['align']} 枠={p['frame']} 表示窓={p['crop']}"+(f" 場面空間={p['composition']} x={p['offsetX']} y={p['offsetY']}" if 'composition' in p else '')+f"\n- 音：{sound}\n- 余白：{gap}\n- 感情・意図：{emotion}\n- 声の輪郭：白地は人物・尾なしで話者と順を接続。絵の通常声は細い楕円、制止は太い縁、心の声は点で区別。無彩色。\n{ds}\n")
text=intro+'\n'.join(sections)
(d/'storyboard.md').write_text(text);(ep/'storyboard.md').write_text(text)
