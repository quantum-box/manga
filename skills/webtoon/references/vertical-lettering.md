# 承認された実例：縦書きのセリフと吹き出しを絵と一緒に生成

2026-10-05、ユーザーが日本語のセリフと吹き出しを含めた画像生成を試し、さらに縦書きへ変更した版を「いいね！」と評価した。以後の作画の基準として採用され、スキルへの反映を依頼された。

同梱の [縦書き原画](approved-vertical-lettering.png) と [360px表示](approved-vertical-lettering-360.png) を画像表示ツールで見る。人物や世界観を新作へコピーする素材ではなく、文字・吹き出し・構図が一体になった仕上げの参照。元の作品フォルダがなくても使える。

## 採用した方式

会話のセリフ全文、発話者、吹き出しの順序、各縦列の内容を画像生成へ渡す。原画に絵と吹き出しと日本語を一緒に描く。吹き出しは人物の近くに置き、尾で話者を示す。顔・手・重要な小道具を覆わない。

縦書きの一列は上から下。列は右から左。文字を横倒しに回転する方法は使わない。吹き出し同士の読む順はそのコマの会話と縦スクロールの流れから決める。この実例では右上のミラが話し、少し下の左のレンが答える。

## この場面で使った列指定

|話者|セリフ全文|縦列の内容（右から左）|
|---|---|---|
|ミラ|ありがとう。私はミラ。この国の王女よ。|ありがとう。 / 私はミラ。 / この国の / 王女よ。|
|レン|レンだ。無事なら、それで。|レンだ。 / 無事なら、 / それで。|

列の指示は次のように書ける。別のコマでは発話者と全文、必要な列数を変える。

```text
Render the exact Japanese dialogue inside the speech balloons as part of the image.
Use genuine vertical Japanese: upright glyphs, each column top-to-bottom, columns right-to-left.
Mira's exact dialogue: ありがとう。私はミラ。この国の王女よ。
Her rightmost column: ありがとう。
Next column to the left: 私はミラ。
Next column to the left: この国の
Leftmost column: 王女よ。
No visible column labels, quotation marks, extra text, or duplicate balloons.
Use clean Japanese manga gothic, readable after smartphone downscaling.
Reshape the balloons to fit without covering faces or hands; tails point to the speakers.
```

## 実物で確認したこと

最初の横書き試作は、スマホに縮小すると字が小さかった。人物と背景を維持したまま、文字・吹き出しだけを画像生成で拡大してから縦書きへ変更した。原画は1024×1536px。360pxと390pxの表示を作り、360pxの画像で全文と列順、読みやすさを目視した。HTMLのフォント値で原画内の文字サイズを検証したとは扱わない。

新しいコマでも、指示に字の大きさを書くだけで済ませず、生成結果を確認する。誤字や小さな字があれば、問題の原画を参照して文字と吹き出しに絞って編集し、旧版を残す。長いセリフを小さい文字で詰め込まず、言葉・列数・コマの構図から調整する。

## 指定に応じて変える部分

このユーザーの日本語の会話は縦書きと一体生成を既定にする。ユーザーが横書き・別言語・文字の個別編集を選んだときは、その指定に合わせる。会話以外のナレーション、効果音、看板、通知へ縦書きを一律に適用しない。二人、二つの吹き出し、ファンタジーの絵柄、1024×1536pxを全作品の固定形式にしない。
