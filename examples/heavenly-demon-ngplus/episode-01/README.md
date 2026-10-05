# 天魔、二周目。 — 第1話

**処刑する相手、間違えてるぞ — 感情改稿版**

[単独リーダー](reader.html) · [編集用HTML](index.html) · [縦読み完成画像](webtoon-full-390.jpg) · [構成](storyboard.md)

## 主人公と展開の改稿

身体は最強でも、本人は異世界を知らない学生。名前を呼ばれて戸惑う、縄の痛みで現実を疑う、普通の日常に帰りたいと願う、表示を信じる前に指先で縄を切って確かめる。剣が止まると本人も驚き、話を求めるが長老は再び襲う。反射で出した掌の力に戸惑い、相手の生存を確かめてから安堵する。

表情の編集3枚と、再攻撃・防御／戦闘後の反応の新規作画2枚。現行は作画10種類を17の表示窓で使用。原画の画像バイトを変更せず、動作の短い部分だけCSSの表示窓に分けた。会話と地の文はHTMLで編集できる。

第1話の山場を一戦に絞り、天魔剣の姿・臣従・隠しルートは第2話へ移した。今回は禁庫からの音で閉じる。最初の目的は「まずは、生きる。帰り道は、俺が探す」。以前の版は `revisions/before-empathy/`。

吹き出しは滑らかな楕円。ステータス3点・効果音5点・武技名1点は、文字を含む透明背景の生成画像を使う。ステータスは2026-10-05の指摘を反映し、細いシアンの枠・ゴシック体・整列したデータ行のシステムウィンドウへ更新。転生先の処刑タイマーだけ赤、レベルと報酬は白とシアンで情報を強調する。 追加の指摘に合わせて、3枚とも文字と枠の輪郭をにじませ、透過と拡散光を持つ視界内の投影へ編集。日本語と配置は維持。全画像に日本語の代替テキストを持たせている。

## スマホ表示

|実際のCSS表示範囲|本文の最小文字|全長|祈りの末尾→指の決めゴマ|
|---|---:|---:|---:|
|390×844|19.968px|17,946px|971.6px|
|360×800|19px|16,907px|898.4px|

両幅で26画像を表示、横はみ出しなし。本文の最小文字はHTMLの測定値。生成画像内の文字は画面で目視した。刃を止めたいという祈りと実際の結果は、一画面を超える距離で保護。剣の破砕は近い小コマ、主人公の理解や安堵は顔と手、短い無言の間で読む速度を変える。

ブラウザの実効倍率は80%。viewport設定と実際のCSS表示範囲を別に測り、書き出し範囲を補正。完成JPEGは390×17,945px（CSS全長との差は丸めによる1px）。冒頭、力の発見、剣の停止、再攻撃、防御、戦闘後、ラストを確認した。測定値は [validation.json](validation.json)、感情改稿の画面は `validation/empathy-*.jpg`、システムUIの画面は `validation/system-ui-*.jpg`、投影への修正は `validation/hologram-ui-*.jpg`。輪郭が鮮明な前版は `revisions/before-hologram-ui/`、金装飾版は `revisions/before-system-ui/`。

## 原本と生成指示

- [EMPATHY-PROMPTS.md](EMPATHY-PROMPTS.md)／`empathy-provenance.json`：今回の表情編集と追加作画5枚。
- [PROMPTS.md](PROMPTS.md)／`provenance.json`：最初の作画9枚。未使用になった原画も保持。
- [HOLOGRAM-UI-PROMPTS.md](HOLOGRAM-UI-PROMPTS.md)／`hologram-ui-provenance.json`：現在の3点。輪郭・光・透過の編集。
- [SYSTEM-UI-PROMPTS.md](SYSTEM-UI-PROMPTS.md)／`system-ui-provenance.json`：今回のシステムウィンドウ3点。転生先を基準に、引き継ぎと報酬の枠・書体を揃えた。
- [LETTERING-PROMPTS.md](LETTERING-PROMPTS.md)／`lettering-provenance.json`：初回の表示・効果音・武技名。UIの旧案も保持。
- `build_episode.py`／`episode.json`／`lettering.json`：組版の再現、原画と表示窓、生成表示の定義。
- `reader.html`：全画像を内包。`webtoon-full-390.jpg`／`mobile-keyframe.jpg`：文字付き全長と戦闘後のプレビュー。

## 再出力

repoルートで実行する。

```sh
python3 examples/heavenly-demon-ngplus/episode-01/build_episode.py
python3 /Users/takanorifukuyama/.codex/skills/webtoon/scripts/package_reader.py examples/heavenly-demon-ngplus/episode-01/index.html --output examples/heavenly-demon-ngplus/episode-01/reader.html --force
python3 scripts/sync_ios_webtoons.py
python3 scripts/sync_ios_webtoons.py --check
```

iOS同梱カタログは5作品／16リーダー。新規Swift・Rustコードの変更なし。同梱チェックは実施。iOS実機の読書、TestFlight、配信サイトへの投稿は未実施。
