# Webtoon配信サーバー

Rust / workers-rsでCloudflare Workers上に配信する。画像とエピソードJSONは
Tachyon Storageの`managed: true`バケット（`MANGA` binding）に保存する。
Tachyonがバケットを払い出し、previewとproductionは分離される。

## ローカル

```sh
mise exec -- rustup target add wasm32-unknown-unknown
mise exec -- cargo install worker-build --version 0.8.7 --locked
# server/.dev.vars に ADMIN_TOKEN を設定（32文字以上、Git管理対象外）
cd server
mise exec -- npx wrangler dev --config wrangler.local.toml
```

## Tachyonへのデプロイ

1. 対象テナントを選び、32文字以上のランダムな管理トークンを準備する。
2. リポジトリへ変更をpushする。
3. リポジトリルートで適用・ビルドする。

```sh
tachyon compute apps apply -f tachyon.yml --tenant-id <tenant> --environment production
tachyon env set manga-server --secret ADMIN_TOKEN --value - --tenant-id <tenant>
# 標準入力で管理トークンを渡す（ログやGitへ保存しない）
tachyon compute builds trigger manga-server --tenant-id <tenant> --branch <pushed-branch>
tachyon compute logs manga-server --tenant-id <tenant>
```

`worker.generateConfig: true`でTachyonが実バケットとシークレットを設定する。
ローカルの`wrangler.local.toml`のバケット名を本番へ直接deployしない。
`install.sh`がRust/Wasm targetとworker-buildを用意するため初回クラウドビルドは時間がかかる。

## 公開

`episode.json`は既存試作と同じ `title` / `blocks` 形式。
画像はJSONと同じディレクトリに置く。PNG/JPEG/WebP、1画像16MiB以下。

画像を先にアップロードし、全画像の存在を確認してからJSONを公開する。
画像名は上書き不可。修正画像は新しい名前でアップロードしJSONの参照を更新する。
秘密トークンを読者やブラウザに渡さない。

### 全作品を採用版だけに更新する

`content/catalog.json`の各話の先頭版を正本として、6作品42話をまとめて反映する。
原稿HTMLと参照画像のハッシュを公開IDに含めるため、新旧の本文画像は衝突しない。
Playwright（Chromium）、Pillow、Node.jsを用意して実行する。

```sh
python3 scripts/export_latest_webtoons.py /tmp/manga-publish-output
python3 scripts/publish_latest_webtoons.py /tmp/manga-publish-output --dry-run
# MANGA_ADMIN_TOKEN は本番管理トークン。一時退避と書き出しは作業ツリー外で行う。
python3 scripts/publish_latest_webtoons.py /tmp/manga-publish-output --retire-previous
python3 scripts/publish_latest_webtoons.py /tmp/manga-publish-output --verify-only
```

書き出しは390 CSS px・1170画像px。原稿の本文部分だけを連続画像にし、表紙と読了文を別に持つ。
全話のJSON・画像SHA-256・カタログの話名と版を読み戻して確認してから、旧版を公開停止して
画像実体も削除する。別の公開更新を検出した場合は削除前に停止する。
公開処理中の一時退避は `/tmp/manga-publish-output/backup`、照合結果は同じ出力先の `published-checks.json` に保存する。リポジトリには採用版だけを残し、旧版はGitの履歴で管理する。
`--verify-only`は管理トークン不要で、公開データの読み戻しだけを行う。

## API

| Method / path | 用途 |
| --- | --- |
| GET `/` | 一覧・スマートフォン向け縦読みビューア |
| GET `/health` | Workerプロセスの疎通（Storageの正常性とは別） |
| GET `/api/episodes` | エピソードID一覧（最大1000件） |
| GET `/api/episodes/:id` | 公開エピソード |
| GET `/images/:id/:name` | 公開エピソードが参照する画像だけ配信 |
| PUT `/admin/images/:id/:name` | Bearer認証付き画像アップロード |
| PUT `/admin/episodes/:id` | Bearer認証付き公開・更新 |
| DELETE `/admin/episodes/:id` | Bearer認証付き公開解除（一覧キャッシュも更新。画像の原本は保持） |
| DELETE `/admin/images/:id` | Bearer認証付き画像実体削除。公開中は409。1回で最大1000件、`remaining: true`なら再実行 |

現段階は無料公開・単一管理者のMVP。作品グルーピング、課金、読者アカウント、
管理画面、画像変換、1000件超のページング、未公開画像の自動回収は未実装。
デプロイ後は画像アップロード→公開→読者GETの実データ照合を行い、管理者用PUTが
トークン無しで401になることを確認する。

## iOS配信API v1

`GET /api/v1/catalog`はiOSの`MangaTitle` / `Episode`と同じJSON配列を返す。
`image`と`reader`は同一HTTPS originに対する相対パス。公開エピソードをシリーズごとにまとめ、話数の昇順に並べる。公開処理で同じ話の旧版を削除し、採用済みの最新版だけを表示する。
作品名・話タイトルは制作カタログを使う。各話のrevisionとシリーズ全体のrevisionを返す。
Storageの公開JSONが正本で、公開時のgeneration変更で一覧索引を無効化する。
通常の一覧取得は全話のJSONを再取得せず、generationと保存済み索引だけを読む。
索引キーにはコードと制作カタログのハッシュを含め、デプロイ後も古い表記を再利用しない。
iOSはURLSessionで一覧、AsyncImageで表紙、WKWebViewで本文を取得する。管理者認証は不要。

表紙は任意の`cover`画像名で指定できる。本文画像と同様に先に管理APIへアップロードする。表紙に本文全体の画像を使わず、小さなJPEGを推奨する。

ブラウザーの既読は最初の画像の読み込み成功時に localStorage へ保存します。話一覧に既読・未読と未読へ戻す操作を表示し、未読の最初の話へ進めます。同じ話の別版は既読を共有します。端末・ブラウザー間の同期は行いません。

本文の配信には390px幅の確認用画像を使わず、元の `reader.html` を390 CSS px・3倍密度（1170px幅）で書き出します。`scripts/render_retina_reader.cjs`（Playwright）で分割PNGを生成し、`scripts/optimize_retina_images.py`（Pillow）でPNGまたは高画質WebPへ圧縮します。解像度を保持してハッシュ付きファイル名でアップロードし、全画像の存在と内容を確認してから本文JSONを差し替えます。
