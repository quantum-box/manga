# iOS収録確認

確認日: 2026-10-04。Xcode 27.0 / iPhone 18 Pro Simulator（iOS 27.0）。

## 確認結果

- Simulator向け`xcodebuild`成功。追加後の4作品・5版を同梱。
- 同期スクリプトの4テスト成功。HTMLの文字・余白と画像のバイト保存、JSONで作るコマ、画像欠落時の既存同梱物の保持、外部依存・作品外参照の拒否、同梱物の差分検知を確認。
- 実際の`.app/Webtoons`内のカタログ・HTML・画像が生成した同梱物と一致。
- ネイティブUIからSF・ファンタジー・日常・武侠の絞り込みと本文表示を確認。すべての作品で日本語と作画を表示。
- 武侠の2版はどちらも第1話と表示。「第1話から読む」は白背景版を開き、縦スクロールで末尾に到達。初稿も別に選択できる。

## 画面証拠

| 画面 | スクリーンショット |
| --- | --- |
| 4作品の一覧、表紙と紹介文 | [catalog.png](catalog.png) |
| ポチ最新版の日本語と画像 | [pochi-reader.png](pochi-reader.png) |
| 落とし物係の日本語と画像 | [lost-property-reader.png](lost-property-reader.png) |
| 白背景版の読了画面 | [white-reader-end.png](white-reader-end.png) |

各作品の390×844・360×800での構成検証は`examples`内の記録を参照。この確認はSimulator上のアプリとソース収録の検証であり、TestFlight配布や実機での検証は含まない。
