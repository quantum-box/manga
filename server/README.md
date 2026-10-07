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

### 一話ずつ公開する

連載は各話のPR・CI・レビュー・mainマージを終えてから、その話だけを公開する。
塔を灯す剣は、Pillowが使えるPythonで採用PNGを無加工で書き出し、白い間を比例画像として保持する。
初回は採用済みの第1話を先に公開し、全画像・カタログの読み戻しと公開リーダーの表示を確認する。
第2話以降の公開処理は、一つ前の採用話が公開カタログに無ければアップロード前に停止する。
各リリースに新しい空の出力先を使う。以前の書き出しや `backup` を使い回さない。

```sh
chapter_output=$(mktemp -d /tmp/tower-forge-episode-01-XXXXXX)
python3 examples/tower-forge/production/export.py "$chapter_output" --episode 1
python3 scripts/publish_latest_webtoons.py "$chapter_output" --dry-run
# MANGA_ADMIN_TOKEN は本番管理トークン。ブラウザやGitへ渡さない。
python3 scripts/publish_latest_webtoons.py "$chapter_output" --retire-previous
python3 scripts/publish_latest_webtoons.py "$chapter_output" --verify-only
# 第1話を公開リーダーでも確認してから第2話へ進む。
chapter_output=$(mktemp -d /tmp/tower-forge-episode-02-XXXXXX)
python3 examples/tower-forge/production/export.py "$chapter_output" --episode 2
python3 scripts/publish_latest_webtoons.py "$chapter_output" --dry-run
python3 scripts/publish_latest_webtoons.py "$chapter_output" --retire-previous
python3 scripts/publish_latest_webtoons.py "$chapter_output" --verify-only
```

manifestの `seriesIds` と `chapterNumbers` で対象を検証する。各回は一話だけを公開・旧版整理し、他の話や作品には触れない。`--episode` の複数指定は拒否する。画像を先に保存し、本文JSONを公開して全画像のSHA-256とカタログ情報を読み戻す。

### 公開処理の記録

`content/catalog.json`の各話の先頭版を正本として、作品・話ごとに採用版を反映する。
原稿HTMLと参照画像のハッシュを公開IDに含めるため、新旧の本文画像は衝突しない。
対象話のJSON・画像SHA-256・カタログの話名を読み戻して確認してから、同じ話の旧版を公開停止して
画像実体も削除する。別の公開更新を検出した場合は削除前に停止する。
公開処理中の一時退避は各出力先の `backup`、照合結果は同じ出力先の `published-checks.json` に保存する。出力先は作業ツリー外に置く。リポジトリには採用版だけを残し、旧版はGitの履歴で管理する。
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

現段階は無料公開・単一管理者のMVP。課金、読者アカウント、
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

### 星環のレガリアを一話ずつ公開する

一話の採用原稿・表示確認をPRでマージしてから、その話だけを準備・アップロードする。
次話の作画は公開版の確認後に進める。公開IDは採用HTML・画像のハッシュを含む。

```sh
python3 examples/star-ring-regalia/production/prepare_publish.py --episode 1
# 上のコマンドが表示した episode.json と、その親ディレクトリ名を使う。
python3 scripts/publish_episode.py https://manga-server.txcloud.app <公開ID> <episode.json>
```

`MANGA_ADMIN_TOKEN`を設定して実行する。生成した`publish-output/`はGit管理対象外。
採用PNGを変更せず配信し、余白は`spacer`の`size: "phone-940"`のように390px幅での高さを指定する。
公開リーダーは画面幅に比例して間を保つ。従来の`long`などの指定も使用できる。
JSONの一致、全画像のSHA-256、カタログ、390pxと360pxでの表示を読み戻して確認する。
