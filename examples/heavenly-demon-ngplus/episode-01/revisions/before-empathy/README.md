この文書は改稿前の制作記録です。旧版の閲覧には画像を内包した `reader.html` または `webtoon-full-390.jpg` を使ってください。`index.html` は組版ソースの記録です。共通資料へのリンクは現行の制作フォルダーを参照します。

# 天魔、二周目。 — 第1話

**処刑する相手、間違えてるぞ**

[単独リーダー](reader.html) · [編集用HTML](index.html) · [縦読み完成画像](webtoon-full-390.jpg) · [構成](storyboard.md) · [作画の生成指示](../../PROMPTS.md) · [表示・効果音の生成指示](../../LETTERING-PROMPTS.md)

組み込みimage_genでアニメ風の原画9枚を生成。顔・衣装・髪・目・昼の広場は最初の作画を参照して統一した。原画の画像バイトを変更せず、短い動作の部分だけCSSの表示窓に分けて全13コマに組版。会話と地の文はHTMLで編集できる。

ブラウザの指摘を反映して、吹き出しの左右が滑らかな楕円になるよう修正。ステータス4点・効果音5点・武技名1点は、文字も含む透明背景の画像として生成した。計11回の生成のうち10点を採用。報酬表示は技名を2行にした第2稿を使い、360px幅でも文字を読める大きさにした。

## スマホ表示

|実際のCSS表示範囲|本文の最小文字|全長|斬撃の心の声→指の決めゴマ|剣の音→天魔剣の初登場|
|---|---:|---:|---:|---:|
|390×844|19.968px|15,208px|1,100.3px|977.2px|
|360×800|19px|14,219px|1,017.2px|902.8px|

両方で画像23表示、横はみ出しなし。本文の最小文字サイズはHTMLの測定値で、生成画像内の文字は両サイズの画面で目視した。上記の二つの見せ順は、確認した画面高で先の文字と次の絵が同時に見えない距離を確保した。全コマを等間隔にせず、手と破片の短いショットは近づけ、逆転と最後の音には長い間を置いた。

ブラウザに実効80%の倍率があるため、viewport設定値と実際のinnerWidth／innerHeightを別々に検証。書き出し範囲を補正して、390×15,208pxの完成JPEGを保存した。修正後の吹き出し・報酬・剣の音と全長画像を目視した。測定値は [validation.json](validation.json)、今回の確認画面は `validation/comments-*.jpg`。修正前の全長と測定値は `validation/before-comments/`。

## 保存ファイル

- `art/`：作画原本9枚。`art/lettering/`：生成した表示・効果音・武技名の原本。`provenance.json`／`lettering-provenance.json`：生成方式・参照・保存元と確認メモ。
- `build_episode.py`／`episode.json`／`lettering.json`：組版の再現と、原画・表示画像・見せ順の定義。
- `index.html`：作画と別組み文字。`reader.html`：全画像を内包し単独で開ける本文。
- `webtoon-full-390.jpg`／`mobile-keyframe.jpg`／`validation/`：文字付きの全長と表示確認用の画像。

## 再出力

repoルートで実行する。

```sh
python3 examples/heavenly-demon-ngplus/episode-01/build_episode.py
python3 /Users/takanorifukuyama/.codex/skills/webtoon/scripts/package_reader.py examples/heavenly-demon-ngplus/episode-01/index.html --output examples/heavenly-demon-ngplus/episode-01/reader.html --force
python3 scripts/sync_ios_webtoons.py
python3 scripts/sync_ios_webtoons.py --check
```

iOS同梱カタログは5作品／16リーダー。既存の同梱チェックと5件のPythonテストに合格した。新規SwiftコードやRustコードは変更していない。iOS実機での読書、TestFlight、漫画配信サイトへの投稿は未実施。
