# HTMLで仕上げるとき

## 編集できる形を保つ

作画は `art/`、文字と配置は `index.html`、必要なら `reader.css` に分ける。各場面を `<figure class="scene">` とし、画像を幅100%、高さ自動で置く。セリフ・音・看板は別要素にする。

[reader.css](../assets/reader.css) は基本の組版だけを提供する。コピーしてから色、字形、余白、吹き出し、画像端のつなぎ方を物語へ合わせる。画像枚数や見せ順は含んでいない。

```html
<main class="episode">
  <figure class="scene" id="descent">
    <img src="art/descent.png" width="724" height="2172" alt="視点が下へ移る場面">
    <p class="sound" id="cue" style="top:21%;right:14%;writing-mode:vertical-rl">ちりん</p>
  </figure>
  <figure class="scene" id="answer">
    <img src="art/answer.png" width="1122" height="1402" alt="音の発生源が現れる">
  </figure>
</main>
```

寸法と文字は例。画像の実際の寸法を指定する。横幅に応じた文字サイズには `cqw` を使える。縦書きの効果音に `cqi` を使うと意図した幅基準から変わることがあるため、実測する。

## 見せ順の測定

作品が「問いを見せてから答えを隠して待たせる」と決めた箇所だけ、先に見る要素の下端と、答えが見え始める位置の距離を確認する。二つの場面の上端だけを比べない。

たとえば問いの下端が3150px、答えの始まりが4010pxなら距離は860px。表示高844pxでは同時に見えない。別の端末の表示高が長ければ同時に見えることがあるため、確認した範囲だけを報告する。背景や視線をたどる間と、無言の余白で待つ間のどちらが合うかを選ぶ。音や問いを先に出し、そのあと広い余白を読む構成も使える。

距離の条件を満たしたあと、実際に読んで待つ時間を確認する。同時に見えないことと、発見への期待や余韻を感じることは別の確認事項。必要なら距離を表示高で割った画面数も記録する。具体的な調整は[間とスクロールの実例](scroll-pacing.md)を参照する。

UIを操作するブラウザツールのドキュメントを読み、スクロールと観察はそのツールで行う。DOMの読み取りが利用できる場合の確認例:

```javascript
() => {
  const cue = document.querySelector('#cue').getBoundingClientRect();
  const answer = document.querySelector('#answer').getBoundingClientRect();
  return {
    width: innerWidth,
    height: innerHeight,
    pageWidth: document.documentElement.scrollWidth,
    imagesLoaded: [...document.images].every(i => i.complete && i.naturalWidth > 0),
    revealDistance: answer.top - cue.bottom,
    fonts: [...document.querySelectorAll('.line,.bubble')]
      .map(e => getComputedStyle(e).fontSize)
  };
}
```

距離はDOMの画面内座標同士ならスクロール位置によらない。文字や小道具を隠す `overflow:hidden` で問題をごまかさず、要素の左右端と見た目も確認する。すべての場面が別画面になることを要求しない。

## 包装と書き出し

`scripts/package_reader.py` はローカルの `<img src="…">` と `<link rel="stylesheet" href="…">` をHTMLへ埋め込む。画像バイトは変更しない。入力ディレクトリ内のPNG/JPEG/WebP/GIF/AVIF、画像を参照しないCSSを対象にする。ネット上の資源やCSSの `url()` / `@import` は取得しないため、この小さな漫画リーダーでは外部依存を使わない。

包装後の `reader.html` を実際に開き、画像と文字が表示されることを確認する。ブラウザが作業後も残せるなら、完成した読書画面を成果物として残す。

完成画像は文字組み後のブラウザ全体をキャプチャする。スクロールして読むための画像なので、長い出力を一画面へ縮小して品質判断しない。ブラウザの拡大率や端末倍率が設定と違う場合は、CSSの表示範囲と保存画像のピクセル寸法を別々に確認する。現在のブラウザで問題がなければ補正を固定値で入れない。
