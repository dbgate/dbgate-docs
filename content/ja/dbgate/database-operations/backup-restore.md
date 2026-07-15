---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: ja
title: バックアップとリストア
weight: 20
---

DbGate は、データベースのバックアップとリストアにネイティブツールを使用します。この機能は Premium エディション専用です。

サポートされているツール:

- PostgreSQL
  - `pg_dump` と `psql`
- MySQL+MariaDB
  - `mysqldump` と `mysql`

## これらのツールのインストール方法
Team Premium エディションの Docker、AWS、Azure バージョンを使用している場合は、この作業は不要です。これらのパッケージには、必要なツールがすべて同梱されています。

最も簡単な方法は、データベースエンジン全体をデスクトップにインストールすることです。
ただし、ほとんどのプラットフォームとデータベースでは、クライアントのみをインストールすることも可能です:

- PostgreSQL
  - Windows - https://www.enterprisedb.com/download-postgresql-binaries からクライアントをダウンロードして展開します
  - Mac: homebrew でクライアントをインストールします: `brew install libpq`
- MySQL:
  - Windows - https://dev.mysql.com/downloads/mysql/ から ZIP をダウンロードして展開します
  - Mac: brew install mysql-client
