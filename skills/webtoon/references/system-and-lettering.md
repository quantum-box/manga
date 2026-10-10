# 生成文字と作中のシステム表示

称号、報酬、武技名、効果音、吹き出しの形、視界に浮かぶシステム表示を作る・直すときに読む。実際のアプリ画面のUIを作るための指示ではない。

## 文字も演出として作画する

生成文字では、句読点を使わない正確な全文、意味に沿った改行、括弧、数字、表示する順序を先に確定する。略語の点など、意味を持つ記号を文の句点と混同して削らない。用語や字の見た目はその作品へ合わせる。

透明素材として単独生成する場合は、文字、飾り、光が画像の中に収まる余裕を指示する。実際に白いページや絵の上へ置き、端の切れ、背景の残り、縮小後の読める大きさを確認する。画像に含めた文字をHTMLでも重ねない。全文は絵コンテと代替テキストにも残す。

## 吹き出しの左右端まで確認する

滑らかな輪郭、文字と輪郭の余裕、話者へ向く尾を360pxと390pxで確認する。語尾が一文字だけ孤立する改行を避ける。

原画に組み込む会話は、縦書き、吹き出し、尾、人物を一緒に生成する既定を保つ。HTMLで会話を組んだ既存作品の部分修正では、その採用方式を維持する。

## システム表示は機能と見え方を分ける

最初に、その表示が何を知らせ、誰のどの視点に見えるかを決める。情報の優先順位、見出し、ラベルと値の整列、簡潔な枠を設計する。豪華な金装飾、筆文字、剣の紋章、粒子を加えるだけでシステムウィンドウらしさを出そうとしない。勲章や巻物として見せる話なら、その道具に合う意匠を選ぶ。

読者のための文字の確認と、登場人物の視界として自然かの確認を分ける。視界に浮かぶ表示では、文字の輪郭のにじみ、光、窓の透過を作中の見え方に合わせる。文字だけくっきりしたまま、枠だけ発光させる仕上がりでは、同じ投影に見えにくい。

ぼかす場合も、誤字や欠けを演出として見逃さない。理解に必要な情報が読めることを確認する。全ての文字や全ての作品をぼかす規則にはしない。

「文字そんなはっきり映らんでしょ」のような指摘は、読みにくいので鮮明にしてほしいという意味と、作中の投影として鮮明すぎるという意味があり得る。文脈と現在の画面で判断し、両方が残るなら、一度だけ方向を聞く。逆方向へ作り直さない。

## 関連する窓を一組として揃える

一枚を共通仕様の基準にし、他の窓は「窓の形と書体の参照」と「変更する内容」を分けて生成できる。光学表現を直すときは、各窓を編集対象として使い、文言、行配置、比率を維持する。前版が失敗した装飾や構図を引き継がないよう、参照の役割を明示する。

編集の指示例:

```text
Use case: precise-object-edit.
Asset type: a system notification floating in the protagonist's field of vision in an anime Webtoon.
Input image: the edit target, not a reference for new wording.
Edit only the optical appearance of the existing lettering and window.
Keep the exact Japanese text, row arrangement, font style, canvas ratio and functional window geometry.
Give glyphs and borders gently diffused contours, restrained cyan-white bloom, and a faint optical ghost where appropriate. Make the window field genuinely translucent and fade its exterior softly to transparent.
Judge the effect at the final phone display width. Preserve identifiable word shapes while making the contours visibly less crisp.
Avoid extra words, duplicate characters, distorted glyphs, checkerboards, new ornament, uncontrolled particles and clipped glow.
Exact text to preserve: [full content in reading order].
```

## 生成指示と実際の画像を区別する

透明背景を指定しても、窓の内部が透けることまで保証されない。RGBAの存在、外側の透明、内部のalpha、背景と合成した表示を必要に応じて確認する。

組み込み image_gen で編集し、生成したPNGは無加工で `art/` へコピーする。指示、編集元、採用ファイルを記録し、旧版はGitの履歴で管理する。バイト一致やハッシュは原本維持の確認、目視は文字と演出の確認として扱う。

## スマホ幅で仕上げる

360pxと390pxで、縮小後の文字、光、周囲の会話とのつながりを確認する。原画の拡大表示だけで合否を決めない。
