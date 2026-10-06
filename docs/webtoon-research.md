# Webtoon再調査と試作の見直し

調査日: 2026-09-29。対象は [ポチのカラー縦読み試作](https://github.com/quantum-box/manga/blob/81a4a9a80c9c6782bac7592142750c324a1b42eb/examples/pochis-handshake/webtoon/README.md)。以下の「今回の判断」は資料と試作を照らした推論であり、プラットフォームの公式要件ではない。

## Webtoonを成立させる要素

1. **スクロールに合わせて見せる順番を設計する。** 縦長の原稿をスマートフォンで読み、コマ、人物、セリフを上下方向へ配置する。余白の長さは休止、時間経過、場面転換に使える。単に縦長の絵を並べるだけでは、この時間操作は生まれない。[Clip Studio: 縦スクロールWebtoonの制作ガイド](https://www.clipstudio.net/how-to-draw/archives/157055)
2. **画角を変えて情報を刻む。** 場所を示す引きの絵、表情の寄り、重要な物のクローズアップを使い分ける。動作は予兆、実行、反応に分けると時間の流れが読める。[Clip Studio: Sequential Visual Narration](https://www.clipstudio.net/en/comics-manga/design-tips/)
3. **スマートフォンで読む単位を確かめる。** 文字・絵・次のコマの見え方を画面内で確認しながら余白を調整する。制作ツールにもWebtoonの画面領域プレビューがある。[Clip Studio: On-screen area](https://tips.clip-studio.com/en-us/articles/4001)
4. **描き込み量と文字量を制御する。** 小さな画面では単純な背景と短い文字のほうが人物や表情を追いやすい。色や背景色は回想、緊張、場面転換にも使える。[Clip Studio: 縦スクロールWebtoonの制作ガイド](https://www.clipstudio.net/how-to-draw/archives/157055)
5. **余白は一律にしない。** WEBTOON上の作家による教材「Comics Tips」には、連続動作、ビートの減速、場面転換、劇的な遅延ごとにコマ間の余白を扱う別々の回がある。[Comics Tips](https://www.webtoons.com/en/canvas/comics-tips/list?page=6&title_no=892865)

2026年の[Webtoonの縦長コマに関する研究](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003332306)は、長いコマの使い方を「空間の拡張」「時間の制御」「感情のリズム」「情報の統合」に分類している。作品分析から得た分類であり、余白を長くすれば必ず面白くなるという因果実験ではない。

投稿時の画像幅・容量はサービスと時期で変わりうる。[WEBTOON CANVASの2021年の告知](https://m.webtoons.com/en/notice/detail?noticeNo=1766)は当時の自動分割仕様を説明しているが、今後の公開用制約として固定しない。

## 見比べる公開事例

- [The Horizon 第1話](https://www.webtoons.com/en/drama/the-horizon/episode-1/viewer?episode_no=1&title_no=3141): 余白の後に寄りの絵や暗い画面を見せる構成。スクロールの先をすぐ見せない演出を観察する。
- [Lore Olympus 第1話](https://www.webtoons.com/en/romance/lore-olympus/episode-1/viewer?episode_no=1&title_no=1320): 静かな導入と色の強い場面の切り替え。背景色・人物色・画面の密度を観察する。
- [Comics Tips: Large Gutters for Scene to Scene](https://www.webtoons.com/en/canvas/comics-tips/layout-large-gutters-for-scene-to-scene/viewer?episode_no=10&title_no=892865): WEBTOON CANVAS上の作家によるコマ間隔の教材。実際にスクロールして、絵の途中と場面転換の空白を見比べる。
- [Traceless Knight](https://tapas.io/episode/3576178): [Tapasの公式ガイド](https://help.tapas.io/hc/en-us/articles/360018577074-Tapas-Recommended-Formatting-for-Comics)が、ページ漫画から縦読みへ移行した参考作品として挙げる。

[WEBTOONのCreator's Resource Handbook](https://webtoons-static.pstatic.net/creator101/en/pdf/Creators-Resource-Handbook-Updated.pdf?dt=2024011501)は、同場面でのコマ間200px以上、場面転換で600〜1000px、1画面にコマは最大2つ、1コマの吹き出しは3つ以下等を制作の目安として示す。これは作品のジャンルや演出を超えて守る必須規則ではない。対して[Tapasの公式案内](https://help.tapas.io/hc/en-us/articles/360052093053-Series-Basics-How-to-find-your-audience)は、週1更新の目安として7〜15コマ、読みやすいフォントで18px以上を推奨する。エピソードの長さに共通の正解はない。今回の短いギャグなら、コマ数は作品のオチを見せるための必要量で決める。

## 今回の試作が弱かった理由

| 観察 | 読者への影響 | 次版で変えること |
| --- | --- | --- |
| 4枚とも同じ寸法の完成イラスト | 全場面が同じ重さになり、速い動きや小さな反応が見えない | 1つの場面を複数の画角・大きさのコマに分ける |
| セリフが絵の外の独立したカード | 誰の発言かを絵と同時に読みづらい | 脚本時に吹き出し位置を決め、人物に近い位置へ配置する |
| 余白が `short` / `long` の機械的な二択 | 緊張、場面転換、オチ前の沈黙を区別しにくい | 余白の意味とスマホ画面内の見え方で調整する |
| 魔王との対面から握手完成までの中間がない | 「おて」が通じた瞬間の驚きと笑いが短い | 魔王の目、差し出す手、接触を別ビートにする |
| 背景の描き込みが4場面すべて多い | 小さな画面でポチの表情と前脚が埋もれやすい | 要所の引き絵だけ詳細にし、寄りの背景は簡潔にする |

さらに、現在の `index.html` はWebで縦読みする試作品。WEBTOONやTapasへ投稿するには、文字・余白を画像に組み込んだエクスポートと、投稿先の現行仕様に合わせた分割・容量確認が必要。

## ポチの話をWebtoonとして描き直す仮のビート表

| 順 | 読者に見せるもの | 役割 |
| --- | --- | --- |
| 1 | 人間の記憶が光になって消える | 転生を始める |
| 2 | 小さな肉球のアップ、ポチの驚いた目 | 柴犬になったと気付かせる |
| 3 | 異世界の森と城の引き絵 | 新しい世界を示す |
| 4 | 姫の「勇者さま！」、ポチが首をかしげる | 依頼とキャラの反応 |
| 5 | 魔王の足元から角まで、スクロールで少しずつ見せる | 体格差と緊張を作る |
| 6 | ポチの前脚だけを寄りで見せ、「おて。」 | 予想外の行動を提示 |
| 7 | 魔王の目、降りてくる手 | 沈黙と反応を作る |
| 8 | 肉球と籠手が触れるアップ | オチ直前の確認 |
| 9 | 魔王が笑って握手する引き絵、姫の驚き | オチを解放する |

これは新しい画像を生成する前の絵コンテ案。長い空白は5→6または6→7の一か所に集中し、各コマをスマホの画面枠で確認して調整する。

## AI制作への含意

生成単位は「縦長の完成イラスト」ではなく、上の各ビートの**小さなコマ画像**にする。全コマでポチの参照シートと色設定を共有し、魔王・姫も参照を持つ。コマの役割、画角、人物の表情、吹き出し位置、次コマに何を隠すかを脚本データに保存する。表情の連続性は生成後の選択・修正も必要で、[NeurIPS 2025の作家向けAI漫画ワークフロー研究](https://proceedings.neurips.cc/paper_files/paper/2025/file/a3386597cce5ce1b2fe0f5c5c5a531db-Paper-Creative_AI_Track.pdf)も、コマごとの表情調整を独立した工程として扱う。

次版の評価は絵の美しさに加え、スマホ幅で「転生と分かるか」「誰が話しているか」「『おて』から握手までの間が効くか」「オチが事前に見えないか」を実際にスクロールして確認する。
