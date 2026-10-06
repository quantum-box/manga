# 第2〜10話の制作スクリプト

採用済みの各話 `manifest.json` と保存原画からリーダーを再構築する。画像のセリフをHTMLへ重ねず、PNGのバイトを変更しない。

1. `python3 production/build.py` で編集用index.html、原画を埋め込んだreader.html、話の一覧、生成指示を再構築。
2. `node production/check.cjs` で390×844と360×800の表示、画像のバイト一致、順序、横はみ出し、見せ順と全話PNGの画素一致を検査。
3. `review/contact-360-*.png` の全場面と390px幅の連続画面を読んで、セリフの全文・話者、人物・衣服、手・小道具、因果と安全な場所を確認。確認できた内容だけvalidation.jsonのvisualReviewへ記録する。
4. `python3 production/package_delivery.py` で各話の単体ZIPを作り、CRC・展開後のバイト一致を検査。
5. `python3 series/build_scripts.py` で目視確認済みの作画範囲を脚本目次へ反映。iOS同梱版はrepoルートの `python3 scripts/sync_ios_webtoons.py` で同期。

各コマンドには話番号を渡せる（例：`python3 production/build.py 10`）。check.cjsはPlaywrightとpngjsを使用。Chromeの実行ファイルはCHROMIUM_EXECUTABLE_PATHで指定でき、MacのGoogle Chromeを既定候補にする。確認はブラウザのスマホ幅で行い、実機検証とは区別する。

`plan.py` は初期企画データであり、既存manifestがある場合は終了する。採用後の余白、話者、人物、修正指示を初期値へ戻さない。

`save_asset.py` は組み込み画像生成のPNGを変更せず保存し、正確なプロンプト・参照・SHA-256を記録する。`repair_asset.py` は対象の原画を目視した後の編集結果を採用し、編集前のPNG・ハッシュと編集指示を記録する。`references/` はノアとミラの人物参照。画像の生成と編集は組み込みimage_genで実行する。
