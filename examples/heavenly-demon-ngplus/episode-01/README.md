# 天魔、二周目。 — 第1話

**処刑する相手、間違えてるぞ — 感情増補版（2026-10-06）**

[単独リーダー](reader.html) · [編集用HTML](index.html) · [縦読み完成画像](webtoon-full-390.jpg) · [構成](storyboard.md)

## 増補した時間

授業を終え、夕飯を置き、ゲームを始める前に肩を伸ばす3コマを追加。生還後には石段に座り、震える手で椀を持ち、力加減と現実の感覚を確かめる3コマを追加した。身体は最強でも、本人は知らない世界に戸惑う学生として描く。

既存の感情改稿、長老との一戦、内功120年と飛燕歩の獲得を保つ。山場は一戦に絞り、天魔剣の姿・臣従・隠しルートは第2話で初めて見せる。第1話は禁庫からの音だけで閉じる。

本文は作画12種類・23表示窓、システムと効果音を含む32画像。追加2枚は組み込みimage_genで無言の原画を制作し、既存方式のHTML文字組みで会話と内心を表示する。原画のバイトは加工せず、表示窓で場面を分ける。第2〜10話は従来どおり縦書きの会話を原画と一体生成している。

## スマホ確認

| 実際のCSS表示範囲 | 本文の最小文字 | 全長 | 祈りの末尾→指の決めゴマ |
| --- | ---: | ---: | ---: |
| 390×844 | 19.968px | 20,789px | 971.6px |
| 360×800 | 19px | 19,564px | 898.4px |

両幅で32画像の読み込み、横はみ出しなし、編集元と単独リーダーの全長一致を確認。祈りと刃を止めた結果は一画面以上離している。追加6窓の顔・手・文字と、次の場面へのつながりを目視。画像内のシステム文字をCSSのfont-sizeとして測ったとは扱わない。

今回のChromiumと同じ条件で保存版を表示した全長は390px幅で18,025px、増補後は20,789px（+15.3%）。旧検証の17,946pxは別の描画環境での値。読書時間は測定していない。[全話の比較](../pacing-comparison.json)。完成JPEGは390×20,789px。

検証記録はvalidation.json、追加窓の画面はvalidation/pacing-*-390.jpg／360.jpg。修正前の本文・完成画像と、感情・システムUIの改稿前はGitの履歴で管理する。

## 原本と生成指示

- [PACING-PROMPTS.md](PACING-PROMPTS.md)／pacing-daily-provenance.json／pacing-rest-provenance.json：日常と生還後の追加2枚。
- [EMPATHY-PROMPTS.md](EMPATHY-PROMPTS.md)／empathy-provenance.json：表情編集3枚、再攻撃・防御と戦闘後の追加2枚。
- [PROMPTS.md](PROMPTS.md)／provenance.json：最初の作画9枚。使用を見送った原画も保持。
- [HOLOGRAM-UI-PROMPTS.md](HOLOGRAM-UI-PROMPTS.md)／hologram-ui-provenance.json：現在の投影表示3枚。細いシアンの枠、透過と光のにじみ。
- [SYSTEM-UI-PROMPTS.md](SYSTEM-UI-PROMPTS.md)、[LETTERING-PROMPTS.md](LETTERING-PROMPTS.md)：以前の表示案、効果音、武技名。

build_episode.pyとepisode.jsonが原画・表示窓・文字組みの編集元。lettering.jsonが生成したシステム表示と効果音の定義。絵コンテに全文と話者を残し、画像にも日本語の代替テキストを付ける。画像内の文字を直す場合は画像生成で編集する。

## 再出力

repoルートから実行。

~~~sh
python3 examples/heavenly-demon-ngplus/episode-01/build_episode.py
python3 skills/webtoon/scripts/package_reader.py examples/heavenly-demon-ngplus/episode-01/index.html --force
python3 examples/heavenly-demon-ngplus/build_series.py
python3 examples/heavenly-demon-ngplus/validate_series.py --episode 1
python3 scripts/sync_ios_webtoons.py
python3 scripts/sync_ios_webtoons.py --check
~~~

表示確認にはPlaywrightとChromium、8765番のローカルHTTPサーバーが必要。Linuxの/usr/bin/chromium、インストール済みPlaywright Chromium、またはPLAYWRIGHT_CHROMIUM_EXECUTABLEで指定した実行ファイルを使える。

iOS同梱版は6作品／35リーダーの照合に合格。実機起動、TestFlightと本番公開はこの増補では未実施。全話の作画・配信データ・持ち出しZIPの説明は[シリーズREADME](../README.md)。
