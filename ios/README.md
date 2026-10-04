# Manga iOS

SwiftUI製の漫画アプリ試作。iOS 17以降、外部パッケージ・API設定なし。

## 起動

1. `Manga/Manga.xcodeproj` をXcodeで開く。
2. `Manga` schemeとiPhone Simulatorを選ぶ。
3. Run（⌘R）で起動する。

実機ではSigning & Capabilitiesで自身のDevelopment Teamを指定する。

## 画面

- タイトル一覧：ピックアップ、2列の表紙、タイトル検索、ジャンル絞り込み。
- 作品詳細：あらすじ、お気に入り保存、話一覧、並び順切替。
- 話選択後：ポチ第1話は既存イラスト4枚の縦スクロール表示。ほかの3作品は画面確認用の架空サンプルで、本文は未収録。

データは `Manga/Sources/MangaApp.swift` の `Catalog` に定義。お気に入りは端末内に保存。既存イラストは `Manga/Artwork` に同梱する。課金・認証・配信APIは未実装。

## ビルド確認

```sh
xcodebuild -project ios/Manga/Manga.xcodeproj -scheme Manga \
  -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build
```
