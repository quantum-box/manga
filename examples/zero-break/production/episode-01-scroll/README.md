# 第1話全編 — 余白とスクロールの改稿

ユーザー採用の余白見本を第1話全編へ適用。セリフだけ・音だけ・演出だけの余白を出来事に応じて挟む。原作73コマ、40の原画、76の表示単位。セリフ・効果音・救出位置・起動条件・六区画中四区画点灯の残量・王冠の発見順は維持する。

新規生成・編集7枚の実行プロンプトは jobs.json。実行結果・出力名・参照ハッシュは records。採用例から3枚をバイト一致で再利用。PNGは v5/art に置き、生成キャッシュを配布物の依存先にしない。

plan.json は表示窓、幅、位置、次までの間、原作のコマ・声・音・表示への参照を記録。欠落・重複とセリフの順を検査する。横並びの反応や斜めの装着枠は一つの表示窓に残す。余白へ移した思考や音は元画像側で除去または表示窓から外す。

原画をHTMLに1回だけ埋め込み、Canvasに表示窓を描く。原画の全内容をhiddenで隠して次のコマを先に見せず、デコード後に原画プールを解放する。失敗時は再読込の案内を出す。JavaScriptが必要。ブラウザを使用せず実際のスクリプトをDOMアダプタで実行し、76窓の描画と読み込み失敗を検査した。

再構築：

1. `python3 examples/zero-break/production/episode-01-scroll/make_plan.py`
2. `python3 examples/zero-break/production/feedback_v6.py build 1`
3. `node examples/zero-break/production/export_v6.cjs 1`（@napi-rs/canvas が必要）
4. `python3 examples/zero-break/v5/package_delivery.py`
5. `python3 scripts/sync_ios_webtoons.py`

検査：`node --test scripts/test_windowed_reader.cjs`、`python3 -m unittest discover -s scripts -p 'test_*.py'`、`python3 scripts/sync_ios_webtoons.py --check`、`python3 examples/zero-break/production/verify_v6.py`。最後の検査は1〜10話のignoredな reader.html を先にpackage_reader.pyで再生成する必要がある。

360/390px幅の全表示窓と主要場面の連続窓を確認。新規原寸素材、話者、縦書き、文字の欠け、手足と装甲の連続性を目視。破片拾いのスマホ窓に次の王冠の絵が入らないことを配置寸法でも確認。原画・ZIP・iOSのバイト照合は verification.json と v5 の各検査記録。ネイティブ書き出しはブラウザの画面撮影ではない。ブラウザ・実機確認とサーバー反映は未実施。
