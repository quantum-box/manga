# 天魔、二周目。

武侠ゲーム『九天』を三千時間やり込んだ学生が、冤罪で処刑される雑役弟子ハン・ユンに転生。身体はレベル999でも、痛みと死は怖い。生きて帰るために選んだ行動が、ゲームで悪役だった人々の運命を変える。

[第1〜10話を読む](serial.html)

## 全10話

| 話 | タイトル | 勝利と獲得 |
| --- | --- | --- |
| 1 | [処刑する相手、間違えてるぞ](episode-01/index.html) | 生還、内功120年、飛燕歩 |
| 2 | [その剣は、俺を知っている](episode-02/index.html) | 天魔剣と隠しルート |
| 3 | [隠し宝庫、全部もらう](episode-03/index.html) | 天魔の宝庫と鍛造素材 |
| 4 | [その天才、俺が買う](episode-04/index.html) | 鍛冶師の仲間と天魔剣の共鳴 |
| 5 | [百人まとめて、来い](episode-05/index.html) | 百人戦の優勝と帰還門の鍵 |
| 6 | [ラスボスは、まだ死ねない](episode-06/index.html) | 白燼の解放と帰還門の地図 |
| 7 | [正派の正体、見せてやる](episode-07/index.html) | 奪われた記録と三人の協力 |
| 8 | [百人分の盾になれ](episode-08/index.html) | 統率者の護陣と町の生還 |
| 9 | [帰る条件は、殺すこと？](episode-09/index.html) | 帰還門の裏口と自分で選ぶ決意 |
| 10 | [二周目は、俺が決める](episode-10/index.html) | 呉天策の無力化と自由に行き来する帰還権 |

第1話は採用済みの感情改稿版。第2〜10話は、同じ人物と鮮明なアニメのセル塗りを引き継ぐ新作。各話3場面、12コマ。恐怖・確認・選択・結果への反応を残し、弱体化や修行で話を引き延ばさない。10話で帰還を実際に叶え、最初の章を閉じる。

## 作画と読書ファイル

第2〜10話は組み込み image_gen で、絵・吹き出し・日本語の縦書きセリフを一緒に生成した27点の原画を使用。原本のバイトを変更せず各話の art に保存。会話をHTMLへ重ねて二重表示しない。

各話の index.html は画像と余白を組む編集元、reader.html は画像・CSSを内包した単独リーダー。原画の文字を直すには画像生成で編集する。storyboard.md に全文と話者、scene-script.json に場面と状態、PROMPTS.md と provenance に生成指示と参照元を残す。webtoon-full-390.jpg は組版後の縦読み完成画像。

## 確認と再出力

390×844と360×800 CSS pxで、編集元と単独リーダーの表示、全画像の読み込み、横はみ出し、余白、末尾までの読み進めを確認。記録は各話の validation.json と全体の mobile-checks.json。画像内の文字をCSSの文字サイズとして計測したとは扱わない。iOS同梱版は同期・照合するが、実機起動は別の確認。

~~~sh
python3 examples/heavenly-demon-ngplus/build_series.py
python3 examples/heavenly-demon-ngplus/validate_series.py
python3 scripts/sync_ios_webtoons.py
python3 scripts/sync_ios_webtoons.py --check
~~~

表示確認はローカルHTTPサーバーを8765番で起動して実行する。[連載構成](series-plan.md)と[人物・作画の共通仕様](production-spec.json)。

[第2〜10話の生成指示一覧](PROMPTS.md)

全話を単独HTMLで持ち出すZIPは次のコマンドで再作成する。ZIP自体はGitへ収録しない。

~~~sh
python3 examples/heavenly-demon-ngplus/package_series.py
~~~

本番サーバー向けの配信画像・JSONは `server-export` に保存。
[公開・照合の手順](../../server/README.md#天魔二周目第110話の反映)を参照。
