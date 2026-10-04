# AI Manga iOS

SwiftUI製のWebtoonアプリ。iOS 17以降。4作品の完成したHTMLと画像を同梱し、通信なしで読む。外部パッケージ・API設定は不要。

## 起動

1. `ios/Manga/Manga.xcodeproj`をXcodeで開く。
2. `Manga` schemeとiPhone Simulatorを選ぶ。
3. Run（⌘R）で起動する。

実機ではSigning & Capabilitiesで自身のDevelopment Teamを指定する。

## 画面

- タイトル一覧：ピックアップ、2列の表紙、タイトル検索、SF・武侠などのジャンル絞り込み。
- 作品詳細：あらすじ、お気に入り保存、話一覧、並び順切替。
- 話選択：完成したWebtoonをWKWebViewで縦スクロール。日本語、吹き出し、広い余白、背景色を保持。
- 武侠第1話は「知らない手」（白背景・ゆっくり版）を既定で開く。白背景の初稿と夜色の初稿も別版として選択でき、話数は1話。

お気に入りは端末内に保存。課金・認証・配信APIは未実装。

## 作品を追加・修正する

作品の正本は`examples`内の`index.html`と参照画像。カタログの正本は`content/catalog.json`。`episodes`の先頭が「第1話から読む」の既定版であり、`number`が話数、`edition`が同じ話の版名。

```sh
python3 scripts/sync_ios_webtoons.py
python3 scripts/sync_ios_webtoons.py --check
```

同期スクリプトはHTMLと参照画像を変更せず`ios/Manga/Webtoons`へコピーする。HTML内の画像、CSS、ポチのインラインJSONにある画像、`artwork-sources`の画像マップも対象。画像欠落・外部依存・作品外参照を検出した場合は、既存の同梱物を置き換えない。

生成した`Webtoons`はコミットする。Xcodeのフォルダ参照でそのまま同梱するため、Xcode Cloudでも生成ツールの追加設定は不要。GitHub Actionsでは正本と同梱物の一致を確認する。

## ビルド確認

repoルートで実行する。

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
xcodebuild -project ios/Manga/Manga.xcodeproj -scheme Manga \
  -destination 'generic/platform=iOS Simulator' \
  -derivedDataPath /tmp/manga-build CODE_SIGNING_ALLOWED=NO build
```

mainへの反映はソース更新。TestFlight配布の完了とは別に確認する。
