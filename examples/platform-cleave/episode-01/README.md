# ホームを裂く一閃

地下駅の出口を塞ぐ槍を剣士が跳ね上げ、階段への道を開く戦闘短編。

完成版は [reader.html](reader.html) を単独で開く。画像と文字を含み、ネットワーク接続を必要としない。

## 制作と確認

採用された20コマのネームを本作画へ仕上げた短編。通常話の分量へ広げる改稿は含まない。本文の高さは390 CSS px幅で6,524.078125 CSS px、360 CSS px幅で6,022.078125 CSS px。保存解像度やDPRと区別して記録する。

7枚の生成原画を [art](art) に保存した。セリフ、吹き出し、効果音は原画内へ統合し、HTMLで重ねていない。元画像の変更はbuilt-in image_genを使用した。実行したプロンプト、生成元、ハッシュは [production](production) に記録している。

採用ネームの原画は構図参照として [review/name-preview](review/name-preview) に保持した。旧版の完成リーダーやバックアップは置かない。

```sh
python3 build_reader.py --package
node validation/capture_reader.cjs
node export_product.cjs --output /absolute/path/to/empty-delivery-directory
```

Nodeの検証と書き出しはPlaywrightを利用する。検証は完成HTMLを `page.setContent` へ読み込み、360×800と390×844、DPR1で全コマ・実スクロール位置を確認する。配信用画像は390 CSS px、DPR3で幅1170pxに書き出す。画像の切り出しと組版はブラウザが行い、生成原画のピクセルは変更しない。

[表示検証](validation/reader-captures/metrics.json) に画像読込、文字の統合、並列コマ、ずらし配置、余白、横はみ出し、表示エラーを記録した。本文内の明示的な無音余白は390px幅で715px。本文高から715pxを引いた値を、純余白を全て除いた内容高として扱わない。

公開サイトとアプリのカタログへの追加は、配信範囲の返答待ち。ローカルの完成と公開済みを区別する。
