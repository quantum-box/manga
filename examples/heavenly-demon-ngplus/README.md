# 天魔、二周目。

[第1〜10話を読む](serial.html)。最強の身体でも死ぬのは怖い。ゲームで聞かなかった声を聞く二周目。

全十話の脚本・作画・台詞・スクロール構成を作り直し、一話ずつ採用する。第1〜1話の全面改稿がこのツリーの採用版。後続話は制作ブランチに準備済みで、順番に差し替える。

| 話 | 読む | 採用状態 |
|---|---|---|
| 1 | [死にたくない](episode-01/index.html) | 全面改稿を採用 |
| 2 | [その剣は、俺を知っている](episode-02/index.html) | 置換前の採用版 |
| 3 | [隠し宝庫、全部もらう](episode-03/index.html) | 置換前の採用版 |
| 4 | [その天才、俺が買う](episode-04/index.html) | 置換前の採用版 |
| 5 | [百人まとめて、来い](episode-05/index.html) | 置換前の採用版 |
| 6 | [ラスボスは、まだ死ねない](episode-06/index.html) | 置換前の採用版 |
| 7 | [正派の正体、見せてやる](episode-07/index.html) | 置換前の採用版 |
| 8 | [百人分の盾になれ](episode-08/index.html) | 置換前の採用版 |
| 9 | [帰る条件は、殺すこと？](episode-09/index.html) | 置換前の採用版 |
| 10 | [二周目は、俺が決める](episode-10/index.html) | 置換前の採用版 |

## 原稿と制作資料

組み込みimage_genで絵・吹き出し・日本語縦書きを一体で生成。採用PNGは無加工で配置し、台詞をHTMLで重ねない。画像内の文字修正はimage_genによる編集で行う。index.htmlとreader.cssが組版元、reader.htmlが画像を内包する単体HTML、webtoon-full-390.jpgがブラウザ書き出しの完成画像。各話storyboard.mdに全文・話者・縦列・状態、PROMPTS.mdに実使用指示を保存する。

[設定](series/bible.md)・[全話設計](production/scripts.json)・[生成指示](PROMPTS.md)・[通読](production/mobile-review.md)・[進行](production/status.md)。採用話の旧原稿・配布物は同じ変更で削除し、旧内容はGit履歴に残す。最新版が使う編集入力と人物参照はproductionに保持する。

## 再出力と公開

Python、Pillow、PlaywrightとChromiumを使う。build_series.pyとvalidate_series.pyは採用済みの改稿話だけを既定で扱い、--episodeで対象を絞れる。scripts/sync_ios_webtoons.pyで同梱を同期し、--checkで照合する。

390×844と360×800で確認。原画の目視、縦スクロール、機械確認、iOS同梱、iPhone実機を区別する。実機は未確認。公開は対象話のPRがmainへ入った後、共通の一話公開手順で画像→JSON→読み戻し→同じ話の旧版削除を行う。他作品・他の話の公開状態を維持する。ZIPは必要な場合だけpackage_series.pyで作り、Gitには残さない。
