# 剣聖、仇の弟子に転生する — 第1〜10話

[連続して読む](serial.html#1) · [新作の第2話から](serial.html#2)

白背景の武侠転生譚。第1話は採用済みのゆっくり版を維持し、第2〜10話を追加した。仇への疑いを解かず、食事・呼吸・階段・稽古・手当てを通して、身体と相手の見え方を少しずつ変える。

| 話 | タイトル | その話の変化 |
| --- | --- | --- |
| 1 | [知らない手](episode-01-white-v3/index.html) | 仇が師匠と分かる |
| 2 | [掴めない手](episode-02-white/index.html) | 手の代わりに袖を掴む |
| 3 | [一椀の粥](episode-03-white/index.html) | 毒を疑いながら食べる |
| 4 | [息をほどく](episode-04-white/index.html) | 弱い身体で半歩を覚える |
| 5 | [石段の下](episode-05-white/index.html) | 仇の手に落下を止められる |
| 6 | [門の外の風](episode-06-white/index.html) | この身体の過去と印の謎 |
| 7 | [斬らない剣](episode-07-white/index.html) | 古い剣の癖を見られる |
| 8 | [名のない墓](episode-08-white/index.html) | 仇が誰かを悼む姿を見る |
| 9 | [雨の針](episode-09-white/index.html) | 襲撃から仇に庇われる |
| 10 | [守る手](episode-10-white/index.html) | 初めて仇の腕を支える |

## 制作と編集

- `series-plan.json`：人物設定と全9話の脚本。`serial-plan.py`は初期構成の記録。最終稿は各話の`scene-script.json`。
- 各話の`storyboard.md` / `PROMPTS.md` / `provenance-*.json`：演出の目的、セリフ、実際の生成プロンプトと参照原画。
- 各話の`art`：built-in image_genで作った原画像。63場面を生成し、器と木剣の2場面を修正した。v2が採用版。採用版の再制作に使う原画・修正時の参照素材を保持。
- `art-windows.json`：原画を目視して決めた非重複の表示窓。連続する道は切らず、短い動作は別々に見せる。誤った紋章の再登場は表示窓から外した。
- 各話の`index.html`：編集用。`reader.html`：原画像を一度ずつ内包した単独HTML。`full-mobile.jpg`：本文全長。`mobile-hero.jpg`：登場後の画面。

```sh
python3 examples/swordsaint-enemy-disciple/build_serial.py
python3 scripts/sync_ios_webtoons.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/sync_ios_webtoons.py --check
```

repoルートで実行する。表示窓の未レビュー、画像の欠落、窓の重複はエラーになる。生成APIはアプリ実行時に不要。

## 確認した条件

新作9話すべてで360×800 / 390×844 CSS pxを確認。横はみ出し0、文字19px以上、全画像読込済み。390pxでは1話約24,457〜25,396 CSS px（約29〜30画面）。問いから大ゴマまで950px、360pxでは約877pxで、同時に見えない間を確保した。

ブラウザのスクリーンショットはCSS幅と保存画像のピクセル寸法が異なるため、実測は`mobile-checks.json`に記録。全長JPEGの保存幅は488px。4〜6分は制作目標であり、読了時間は未計測。

## アプリ

作品詳細は10話として表示。各話は採用済みの最新版のみ収録し、旧版はGitの履歴で管理する。「次の話」「前の話」で本文を作り直し、先頭から読む。第2話から戻ると採用版の第1話を開く。第10話で次へ進むボタンを無効にする。
