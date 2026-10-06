# ゼロ・ブレイク

**[第1〜10話を縦読みで読む](chapters.html)**

異世界転生 × スーパーヒーロー。全50話で完結する物語。第1〜10話は全196場面の作画が完成。第11〜50話は場面脚本が完成し、作画は未制作。

セリフと吹き出しをアニメ風の絵と一緒に生成し、日本語の縦書きで収録。接近、説明、手順、選択、実行、反応を別々の場面に分ける。白や淡い背景の余白で間を作り、結果や次の事件は一段下で見せる。

| 話 | 読む | 場面数 | 制作資料・単体ZIP |
|---|---|---:|---|
| 1 | [最弱判定、最強の一歩。](v5/index.html) | 30 | [資料](v5/README.md) / [ZIP](v5/reader.zip) |
| 2 | [英雄の請求書](episode-02/index.html) | 20 | [資料](episode-02/README.md) / [ZIP](episode-02/reader.zip) |
| 3 | [殴れないヒーロー](episode-03/index.html) | 18 | [資料](episode-03/README.md) / [ZIP](episode-03/reader.zip) |
| 4 | [姫の秘密基地](episode-04/index.html) | 18 | [資料](episode-04/README.md) / [ZIP](episode-04/reader.zip) |
| 5 | [消える街区](episode-05/index.html) | 18 | [資料](episode-05/README.md) / [ZIP](episode-05/reader.zip) |
| 6 | [十七人を運べ](episode-06/index.html) | 18 | [資料](episode-06/README.md) / [ZIP](episode-06/reader.zip) |
| 7 | [騎士の見たもの](episode-07/index.html) | 18 | [資料](episode-07/README.md) / [ZIP](episode-07/reader.zip) |
| 8 | [白い英雄の肖像](episode-08/index.html) | 18 | [資料](episode-08/README.md) / [ZIP](episode-08/reader.zip) |
| 9 | [ゼロの外側](episode-09/index.html) | 18 | [資料](episode-09/README.md) / [ZIP](episode-09/reader.zip) |
| 10 | [拍手より先に](episode-10/index.html) | 20 | [資料](episode-10/README.md) / [ZIP](episode-10/reader.zip) |

第1話は騎士の足音から声かけ、装置への誘導、測定のためらい、接触、待機、ゼロ表示と落胆を段階的に描く。第2話以降も、縄を渡してから渡る、梯子を固定してから一人ずつ避難する、17人を確認してから空の車両を放す、全員が逃げてから瓦礫を下ろす、という流れを保つ。レンの救済核には有限の負荷があり、対決だけでは起動せず、人を守る選択に応える。

## 脚本と原画

- [全50話の脚本](series/index.html) / [脚本目次](series/README.md)：全300の大場面。第1〜10話には詳細絵コンテへのリンクを収録。
- [設定・能力の制約・伏線台帳](series/bible.md)。
- 各話の `art/` は採用原画、`source/` は修正前の原画。`generation/` と `generation-log.json` に実際の生成・編集指示、参照、SHA-256を保存。

原画は組み込み画像生成を使用し、保存時のPNGを縮小・加工せず保持する。文字の変更は対象画像の再生成・編集で行い、HTMLは配置とスクロールの余白を調整する。各ZIPはその話を単体で読むための埋め込み画像付き `reader.html`。連続して読む場合は話の一覧かiOS同梱版を使う。

## 表示確認と再構築

390×844 / 360×800のブラウザ表示で、全196枚の読み込み、横はみ出し、順序、文字の二重表示を検査。縦書き全文・話者・手・人物・小道具と救助前後の位置を目視確認。各話の `complete-390.png` / `complete-360.png` は通常のスクロール画面の画素をそのまま繋いだ全話画像。原画と埋め込み画像の一致、全話画像と画面の一致、ZIPのCRCと展開後の一致を検証する。実機での検証は未実施。

第2〜10話の再構築はこのディレクトリで実行する。

```sh
python3 production/build.py
python3 production/package_delivery.py
node production/check.cjs
python3 series/build_scripts.py
```

`check.cjs` はPlaywrightとpngjsを使用し、目視確認の状態をpendingへ戻す。検査後は全場面をスマホ幅で読み直し、確認内容を `validation.json` へ記録する。詳しい手順は [制作用スクリプト](production/README.md)、第1話の再構築は [v5](v5/README.md) を参照。
