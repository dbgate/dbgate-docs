---
sourceHash: ca8ddaf0b11d2bd598a11450dfbfe01ceee7fb8493445eb920ea2829b472b4af
language: ja
title: DbGate ドキュメント
---

DbGate には、データを扱うさまざまな方法に合わせて構築された複数の製品があります。このページを参考に、最適な製品を見つけてください。

| 製品 | ホスティング | ログイン | 適した用途 |
|---|---|---|---|
| [DbGate](/ja/dbgate/) (Community / Premium / Team Premium) | デスクトップアプリ、またはセルフホストのウェブ版 (Docker、NPM、AWS、Azure) | 任意 (Team Premium) | SQL および NoSQL データベースサーバー向けのフル機能クライアント。接続やスクリプトを保存できる [DbGate Cloud](/ja/dbgate/dbgate-cloud/) オンラインストレージ付き |
| [DbGate Central](/ja/dbgate-central/) | ホスティング型、有償、ブラウザ内で動作 | 必須 | GraphQL、oData、Shopify の API をデータベースのように参照・クエリ・編集。BI レポートと AI エージェント向けの MCP サーバーを搭載 |
| [DbGate Shopify App](/ja/dbgate-shopify-app/) | ネイティブ Shopify アプリ、ストア管理画面に埋め込み | Shopify セッション | Shopify ストアのデータの一括表示・編集と、スケジュール実行される商品フィードの生成 |
| [DbGate Lite](/ja/dbgate-lite/) | ホスティング型、無償、ブラウザ内で動作 | 不要 | SQL の学習と、データファイルを使った手軽なアドホック作業 |

DbGate Lite と DbGate Central は同じグリッドおよびクエリエンジンを基盤としているため、フィルタリング、編集、参照の操作感は両者で同じです。ただし Lite は無償で、ローカルの SQLite/DuckDB データベースとファイルのみを扱えるのに対し、Central はホスティング型の API 接続、クラウドに保存されるワークスペース、チーム向け機能を追加で提供します。
