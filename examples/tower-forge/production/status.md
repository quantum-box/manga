# 制作・公開状態

2026-10-08。完成した話を一話ずつ PR、CI・レビュー、main マージ、サーバー公開、公開確認の順で届ける。

| 話 | 制作・表示確認 | 公開手順 |
| --- | --- | --- |
| 1 | 採用済み22原画・78の物語上の瞬間 | main 採用版を公開済み。全36画像をバイト照合。360px・390pxで43画像ブロックの読み込みと横はみ出し無しを確認。[公開第1話](https://manga-server.txcloud.app/?episode=tower-forge-episode-01-r63d24a1e972f) |
| 2 | 改稿20原画・60の物語上の瞬間。全360px原画と390px代表場面を目視。両幅で実ブラウザー全編撮影 | [PR #45](https://github.com/quantum-box/manga/pull/45) は CI・レビュー対応後 main に取り込み済み。全35画像をバイト照合。360px・390pxで40画像ブロックの読み込みと横はみ出し無しを確認。[公開第2話](https://manga-server.txcloud.app/?episode=tower-forge-episode-02-rf4a7732306b5)。既存54話を維持 |
| 3 | 改稿19原画・57の物語上の瞬間。全360px原画と390px代表場面を目視。両幅で全編実ブラウザー撮影。本文・原画ハッシュへ紐づけて validation.json に記録 | この話だけの PR。CI・レビュー、main 取り込み後に第3話だけをアップロードして公開確認する |
| 4〜10 | この PR に含めない。先行制作物は制作作業ツリーに保持 | 各話の完成後に個別 PR・公開 |

第3話は水路へ降り、帰還点を記録し、初めての実戦でセナに守られながら動きの周期を観察する。イリスから一回だけ供給を受ける相談、盾で空けた道、一撃、勝利の反応、停止を確かめた後の観察を順につなぐ。水音・守護機の擦過音・盾の衝撃と白い間の強弱を点検した。剣は右手、カフは左腕、セナの盾は左腕。倒した小型機は暗く停止し、先の通路へ新しい敵を出さない。旧稿の水路原画 art/01.png は後続の現行画像が参照する共有素材として残し、元の実行指示を production/source-material/episode-03-aqueduct-PROMPT.md に保持する。第3話の本文へ旧稿は収録しない。

物理スマートフォン・ユーザーによる改稿後の評価・TestFlight 配布は未確認。表示確認を読者の理解の保証とは扱わない。

公開は production/export.py --episode N で一話だけを新しい空の出力先へ書き出す。publish_latest_webtoons.py は manifest の seriesIds と chapterNumbers を検証し、対象以外の話や作品を維持する。第2話以降は一つ前の採用話の公開を先に確認する。元の生成 PNG を再圧縮せず、画像のアップロード後に本文 JSON を公開する。

第2・3話の reader.html は index.html と同一の画像参照式本文。画像内包 HTML は package_reader.py で作業ツリー外へ生成できる。実行済み指示は各話の PROMPTS-USED.md と revision-provenance.json、今後の制作指示は PROMPTS.md に区別して記録する。
