# 終電後の落とし物係 — 第3稿

`reader.html` をブラウザで開き、下へスクロールする。画像をすべて内包しているため、サーバーや外部通信は不要。

## この版の構成

バッグ、ポケット、空の手は近い三つのコマ。音の後は一つの長い雨の背景を下り、猫を発見する。鍵の受け渡しを小さな場面で見せた後、足跡と駅の明かりを縦にたどる。窓口の猫が最後に正体を明かす。

一律のコマ寸法や間隔ではなく、動作の密度、雨だれ、足跡、問いと答えの距離で読む速さと視線を組んだ。画像6枚を組み込み image_gen で新規生成し、文字・吹き出し・看板をHTML/CSSで別に配置した。生成画像の原本は `art/`、実際の生成指示は `PROMPTS.md` に保存。

## ファイル

- `reader.html`: 単独で開ける完成版。
- `index.html` + `art/`: 編集用の組版と作画。
- `webtoon-390.jpg`: スマホ幅390pxの完成版をブラウザで書き出した画像。
- `storyboard.md` / `PROMPTS.md`: 構成と生成指示。
- `validation.json`: 表示確認の数値と目視確認事項。

## 表示確認

2026-10-04、ブラウザのCSS表示幅390px・高さ844pxと、幅360px・高さ800pxで確認。すべての画像が表示され、横方向にはみ出さない。セリフは最小19px。音の末尾から猫の場面まで、および問いの末尾から最後の場面までの距離は、それぞれの表示高を超える。帽子は最後だけ。受け渡し後に猫の口へ鍵は残らない。看板の日本語は別組版で正確に配置した。

画像書き出しはブラウザのスクリーンショットで行った。ブラウザに残っていた80%の拡大率を考慮して、CSS表示幅と保存画像の幅を別々に確認した。

## 編集後の保存

`index.html` または `art/` を変更したら、このディレクトリで `python3 build_reader.py` を実行する。これは画像データをHTMLに埋め込むだけで、画像自体を加工しない。JPEGの書き出しは自動更新されない。

## 参照した制作資料

- [CLIP STUDIO TIPS — Webtoon composition](https://tips.clip-studio.com/en-us/articles/4143)
- [CLIP STUDIO TIPS — Vertical comic techniques](https://tips.clip-studio.com/en-us/articles/4093)
- [CLIP STUDIO TIPS — Panel size and pacing](https://tips.clip-studio.com/en-us/articles/9422)

このチャットの前の調査で、資料内の作例画像を含めて確認した。
