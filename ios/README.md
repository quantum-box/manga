# AI Manga iOS

SwiftUI製のWebtoonアプリ。iOS 17以降。配信APIから作品一覧・表紙・本文を読み込む。オフラインへ切り替えると同梱4作品を通信なしで読める。外部パッケージは不要。

## 起動

1. `ios/Manga/Manga.xcodeproj`をXcodeで開く。
2. `Manga` schemeとiPhone Simulatorを選ぶ。
3. Run（⌘R）で起動する。

実機ではSigning & Capabilitiesで自身のDevelopment Teamを指定する。

## 画面

- タイトル一覧：ピックアップ、2列の表紙、タイトル検索、SF・武侠などのジャンル絞り込み。
- 作品詳細：あらすじ、お気に入り保存、話一覧、並び順切替。
- 話選択：完成したWebtoonをWKWebViewで縦スクロール。日本語、吹き出し、広い余白、背景色を保持。
- 武侠第1話は「知らない手」（白背景・ゆっくり版）を既定で開く。白背景の初稿と夜色の初稿も別版として選択できる。第2〜10話を収録し、同じ第1話の別版を重複加算せず10話と表示する。本文下部の「次の話」「前の話」で移動し、話の先頭から開く。

お気に入りは端末内に保存。配信APIは`GET /api/v1/catalog`。読者の課金・認証は未実装。管理者トークンはアプリに含めない。

接続先はXcode Build Settingの`MANGA_API_BASE_URL`（HTTPS）。現在はPR #5のpreview Workerを指定している。本番URLが確定したらDebug/Release両方を更新する。カタログ更新は起動・読み込み元切替・下へ引っ張って更新で行う。通信失敗はエラーとして表示し、オフラインを明示的に選べる。

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
swiftc ios/Manga/Sources/Catalog.swift scripts/test_ios_catalog.swift -o /tmp/manga-catalog-tests
/tmp/manga-catalog-tests
xcodebuild -project ios/Manga/Manga.xcodeproj -scheme Manga \
  -destination 'generic/platform=iOS Simulator' \
  -derivedDataPath /tmp/manga-build CODE_SIGNING_ALLOWED=NO build
```

mainへの反映はソース更新。TestFlight配布の完了とは別に確認する。

カタログのSwiftテストはmacOSで実行する。実機と同様に実在する`/private/var`のファイルを用意し、以前のパス比較がカタログを拒否することと、修正後に4作品・全15版・武侠10話を読み込めることを確認する。画像と本文にも同じパス解決を使う。読み込み失敗は空の検索結果と区別し、本文の読み込み中も表示する。

配布アーカイブの内容を同じテストで確認する場合は、実際の`Manga.app`ディレクトリをテスト実行時の第1引数に指定する。GitHub ActionsではPythonによる収録整合性とmacOSでの実機パス回帰テストを実行する。

## 配信作品をオフラインへ保存

配信作品を開くと、作品の全話・画像・表紙を端末内へ自動保存する。
一覧の「オフライン」に保存済み作品と同梱作品を表示する。保存中の話数と失敗を表示し、
全ファイルが揃った作品だけ公開する。途中失敗時は再試行できる。
Application Support/MangaDownloadsへ保存し、iCloudバックアップから除外する。
保存済み作品は再ダウンロードせず再利用する。設定（一覧右上の歯車）で自動保存をオフにできる。
保存済み作品ごとの「削除」から確認後に端末のデータを削除できる。同梱作品は対象外。
削除と保存完了が競合しても保存データは復活しない。再び配信作品を開くと再保存するため、
保存を止めたい場合は自動保存をオフにする。更新版への置き換えは未実装。
保存中はアプリを開いておく（バックグラウンドダウンロードは未対応）。
