# カラー縦読みWebtoon試作

[縦読みページを開く](index.html)。転生、姫の依頼、魔王との対面、「おて」の結末を4枚の縦長イラストと余白で構成した。

画像生成にはこのチャットの組み込み画像生成機能を使用。外部APIキーは不要。キャラクターの色設定は [カラー参照シート](pochis-color-sheet.png)、生成指示の全文は [PROMPTS.md](PROMPTS.md) に保存した。

セリフと余白は [episode.json](episode.json) に保持し、画像に焼き込まない。内容を変えたら、リポジトリのルートで次を実行して `index.html` を再生成する。

```sh
python3 scripts/build_webtoon.py examples/pochis-handshake/webtoon/episode.json
```

画像は各場面ごとに差し替えられる。今回の出力は静的な縦読みページで、画像生成の自動実行とブラウザ上でのセリフ編集はまだ実装していない。

この版はWebtoonの演出としては不十分。4枚の完成イラストに均一な余白を足した構成になっており、コマごとの画角・反応・オチの間が不足している。[再調査と作り直し案](../../../docs/webtoon-research.md)を参照。
