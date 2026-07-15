---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: ja
title: Docker 上の Team Premium
weight: 30
---

一般的な Team Premium のインストールは、次の 2 つのコンポーネントで構成されます。
- DbGate サーバーの docker コンテナ
- データベースサーバー（MS SQL、MySQL、PostgreSQL、Oracle）- 接続、ユーザー、ロールを保存する内部ストレージデータベース。既存のデータベースサーバーを使用することも、新しくインストールすることもできます。

## DbGate サーバーの Docker コンテナ
Docker Hub の [DbGate Team Premium イメージ](https://hub.docker.com/r/dbgate/dbgate-premium) を使用します。
```
docker pull dbgate/dbgate-premium
```

DbGate Team Premium コンテナでは、いくつかの環境変数を設定する必要があります。
- `STORAGE_SERVER`、`STORAGE_DATABASE`、`STORAGE_USER`、`STORAGE_PASSWORD`、`STORAGE_ENGINE` - 内部ストレージデータベースへの接続を定義します

利用可能な環境変数の詳細については、[環境変数のドキュメント](/ja/dbgate/customization/env-variables/#team-premium-edition-configuration) を参照してください。

## リソース要件

実際のところ、DbGate Team Premium のリソース消費は非常に少ないですが、最適なパフォーマンスのためには次の構成を推奨します（同時接続ユーザー 10 名の場合）。
- CPU 2 コア
- 4 GB RAM（MySQL または PostgreSQL の内部ストレージデータベースの RAM 消費を含む）
- 10 GB の空きディスク容量（docker のインストール、ストレージデータベース、一時ファイル、クエリ結果などのため。実際のディスク消費量は使用状況によって異なります）

ユーザー数が少ない場合は、より低いリソース制限（1 GB RAM、CPU 1 コア）を使用できます。  
小規模なインストールでリソース消費を最小限に抑える必要がある場合は、内部ストレージとして MySQL/MariaDB を使用することを推奨します。  

## docker の構成

ユーザーファイル（クエリ結果のエクスポートなど）の保存にディスクファイルを使用したい場合は、コンテナ内の `/root/.dbgate` パスをマッピングする必要があります。

以下は、内部ストレージデータベースとして PostgreSQL を使用する DbGate Team Premium コンテナを定義する `docker-compose.yml` ファイルの例です。
- `DBGATE_LICENSE` 環境変数を定義してライセンスキーを設定できます。設定されていない場合、DbGate は初回起動時にライセンスキーを要求します。
-  'ADMIN_PASSWORD' 環境変数を定義して admin ユーザーのパスワードを設定できます。設定されていない場合、DbGate は初回起動時に admin のパスワードを要求します。

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## ステートレス/ステートフル
DbGate コンテナはステートフルです。

以下のデータがコンテナ内に保存されます。
* ログイン中のユーザーセッション
* クエリ実行の状態
* 一時ファイル（結果など）
* 開いているデータベーストランザクション
* 開いているデータベース接続

上記のデータはコンテナ間で共有されないため、ロードバランサーの背後で複数の DbGate コンテナを正しく実行することはできません。

## NPM からの DbGate サーバー
インフラストラクチャが Docker をサポートしていない場合は、[DbGate Team Premium NPM パッケージ](https://www.npmjs.com/package/dbgate-serve-premium) を使用できます。
```
npm install -g dbgate-serve-premium
```
 
## プロセス分離
DbGate Team Premium はデータベース接続レベルでプロセス分離を使用するため、複数のユーザーが干渉することなく同じデータベースサーバーを使用できます。DbGate からフォークされるプロセスはアクティブなユーザー数と接続数に応じて増加するため、サーバーに十分なリソースがあることを確認してください。
以下のエンティティは新しいプロセスに分離されます。
* サーバー接続
* データベース接続
* クエリセッション
* エクスポート/インポートジョブの実行
* SSH トンネリング
