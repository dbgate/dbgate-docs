---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: ja
title: DbGate
weight: 5
---

## DbGate とは？

DbGate はデータベースマネージャーで、サポートされているデータベースに接続して作業できます。デスクトップアプリとしても Web アプリとしても利用できます。高速で使いやすいように設計されています。

ブラウザベースおよびホスティング型の製品（DbGate Lite、Central、Shopify App）については、[製品概要](/ja/)をご覧ください。

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## サポートされているデータベース

| データベース | {{< center "Community" >}} | {{< center "Premium" >}} | 追加機能 |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | バックアップ、リストア |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | バックアップ、リストア |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | バックアップ、リストア |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## サポートされているプラットフォーム

- デスクトップ
  - Windows
  - MacOS（ARM および Intel プロセッサの両方）
  - Linux
- Web バージョン
  - Docker
  - NPM
  - Azure
  - AWS

## エディション

DbGate には 3 つのエディションがあります。

| エディション | 提供形態 | 主な機能 |
|---|---|---|
| Community | デスクトップアプリ、またはセルフホスト型 Web（Docker/NPM）、無料 | 標準的な SQL および NoSQL データベースへの接続と閲覧・編集、Redis GUI、DbGate Cloud の接続/ファイルを最大 5 件まで |
| Premium | デスクトップアプリ（シングルユーザー） | Community のすべての機能に加えて、[クエリデザイナー](sql-and-queries/query-designer)、[チャート](working-with-data/charts)、[編集可能なクエリ結果とビュー](sql-and-queries/sql-editor)、[マスター/詳細ビュー](working-with-data/data-browser)、[AI ツール](working-with-data/ai-features)（DB チャット、エラー解説、テーマアシスタント）、DB モデルの比較とデプロイ、高度な/バッチのエクスポート・インポート、[データデプロイヤー](working-with-data/advanced-data-tools/data-deployer)、[API 接続](developer/api-connections)（GraphQL/oData/OpenAPI）、追加のデータベースエンジン（libSQL、CosmosDB、Amazon Redshift、Firestore、Amazon DynamoDB）、無制限の DbGate Cloud ストレージ |
| Team Premium | デスクトップアプリ + セルフホスト型 Web（Docker/NPM/AWS/Azure） | Premium のすべての機能に加えて、Web アプリケーション、[管理 UI](admin)、ユーザー/ロール/権限、外部 ID プロバイダー（OAuth/OIDC）、設定不要のネイティブバックアップとリストア |

## このセクションの内容

* [はじめに](getting-started) - DbGate をインストールして最初のデータベースに接続する
* [データの操作](working-with-data) - データの閲覧、編集、フィルタリング、チャート化、マップ表示、エクスポート、アーカイブ
* [SQL とクエリ](sql-and-queries) - SQL エディター、ビジュアルクエリデザイナー、ER 図
* [データベース操作](database-operations) - スキーマの編集、モデルの比較とデプロイ、バックアップとリストア
* [カスタマイズ](customization) - 外観と実行時設定の構成
* [管理](admin) - ユーザー、ロール、権限の管理（Team Premium）
* [開発者向け機能と自動化](developer) - スクリプト、API 接続、プラグイン
* [DbGate Cloud](dbgate-cloud) - 接続、SQL スクリプト、共有フォルダーのオンラインストレージ
