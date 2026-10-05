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
mise exec -- npx wrangler dev
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
ローカルの`wrangler.toml`のバケット名を本番へ直接deployしない。
`install.sh`がRust/Wasm targetとworker-buildを用意するため初回クラウドビルドは時間がかかる。

## 公開

`episode.json`は既存試作と同じ `title` / `blocks` 形式。
画像はJSONと同じディレクトリに置く。PNG/JPEG/WebP、1画像16MiB以下。

```sh
# MANGA_ADMIN_TOKEN にデプロイ済み ADMIN_TOKEN と同じ値を設定
python3 scripts/publish_episode.py https://<worker-host> pochis-handshake \
  examples/pochis-handshake/webtoon/episode.json
```

画像を先にアップロードし、全画像の存在を確認してからJSONを公開する。
画像名は上書き不可。修正画像は新しい名前でアップロードしJSONの参照を更新する。
途中失敗後は同じコマンドを再実行できる。既存画像を管理者APIで読み戻し、バイト一致を確認する。
放棄された未公開画像の回収は現段階では管理者によるバケット操作が必要。
秘密トークンを読者やブラウザに渡さない。

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

現段階は無料公開・単一管理者のMVP。作品グルーピング、課金、読者アカウント、
管理画面、画像変換、1000件超のページング、未公開画像の自動回収は未実装。
デプロイ後は画像アップロード→公開→読者GETの実データ照合を行い、管理者用PUTが
トークン無しで401になることを確認する。
