---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: ja
title: データベースデプロイ
weight: 10
---

*デプロイ機能は今後のリリースで大幅に変更される予定です。このドキュメントは最新の BETA バージョンに関するものです*

DbGate はデータベースを自動的にデプロイする仕組みを提供します。従来の方法ではマイグレーション SQL スクリプトを使用しますが、DbGate はデフォルトで異なる方法を採用しています（マイグレーションスクリプトもサポートされています）。
テーブル構造とリストデータを記述した YAML ファイル、およびビュー・ストアドプロシージャ・関数を記述した SQL ファイルで DB モデルを定義します。このモデルはデータベースにデプロイされ、現在の構造とモデル内の構造を比較して、不足しているカラムやテーブルを作成し、ビューやプロシージャの定義を更新します。**破壊的な操作**（データ損失につながる可能性のあるもの）は一切実行されないため、モデルからカラムやテーブルを削除しても、データベース内にはそのまま残ります。モデル内でカラム名を変更した場合、新しい名前のカラムが作成され、古いカラムはデータベース内に残ります。

デプロイはコマンドライン（node スクリプトを使用）から、または DbGate GUI から実行できます。DB 比較機能を使用して、モデルと実際のデータベースの差分を視覚的に比較することもできます。

## テーブルの yaml フォーマット

```yaml
name: Album # table name 
columns:
  - name: AlbumId # column name 
    type: int # data type. is used directly in target SQL engine  
    autoIncrement: true # column is autoincrement 
    notNull: true # column is not nullable (default: is nullable) 
  - name: Title
    type: nvarchar(150)
    notNull: true
  - name: ArtistId
    type: int
    references: Artist # name of table. Is used for creating foreign key 
  - name: isDeleted
    type: bit
    notNull: true
    default: 0 # default value 
  - name: created
    type: timestamp
    default: current_timestamp
primaryKey:
  - AlbumId # list of primary key column names 
indexes:
  - name: UQ_AlbumTitleArtistId # index name 
    unique: true # whether index is unique. default=false 
    columns: # list of index columns 
      - Title
      - ArtistId
data: # static data (only for list tables) 
  - AlbumId: -1 # values for all columns, which should be filled 
    Title: Predefined static album
```

- 名前はスキーマ名なしで定義します。1 つのモデルは 1 つのスキーマを記述します
- デフォルト値は SQL 式として定義されるため、文字列を定義したい場合は 'シングルクォート' を使用する必要があります
- テーブルに静的データを定義できます

### マイグレーションスクリプトの使用
より伝統的なマイグレーションスクリプトを DbGate 固有のデプロイ管理と組み合わせることができます。より特殊なオブジェクトはマイグレーションスクリプトで作成できます。
スクリプトの種類はファイル拡張子によって決まります。ディレクトリ構成はユーザーの自由であり、DbGate はこれに影響されません。

以下のスクリプト拡張子がサポートされています:
- `*.predeploy.sql` - 各デプロイ処理の前に実行されるスクリプト
- `*.install.sql` - 前回のデプロイと異なる場合にのみ実行されるスクリプト
- `*.uninstall.sql` - このスクリプトは `.install.sql` ファイルと対になっており、新しいバージョンの `*.install.sql` ファイルが実行される前に実行されます
- `*.once.sql` - 一度だけ実行されるスクリプト
- `*.postdeploy.sql` - 各デプロイ処理の前に実行されるスクリプト

DbGate はデータベースにデプロイされたデプロイスクリプトを追跡するために `dbgate_deploy_journal` テーブルを使用します。このテーブルは、マイグレーションスクリプトを少なくとも 1 つ含むプロジェクトをデプロイした際に自動的に作成されます。


### DbGate GUI での使用

- 接続内のデータベースのコンテキストメニューで「Export DB model」を選択します（Premium のみ）。DB モデルはディレクトリまたはファイルに保存されます。デプロイ機能を使用する予定がある場合は、Data archive または Folder (YAML + SQL) を保存先として選択してください。
- アーカイブウィジェットを開くと、ダウンロードされたモデルが表示されます
- モデルのコンテキストメニューから、モデルに対していくつかの操作を実行できます:
    - Generate deploy DB SQL - 現在のデータベース（ステータスバーで確認できます）とモデルを比較し、モデルの変更を現在のデータベースにデプロイする SQL スクリプトを生成します
    - Shell: Deploy DB - DB のデプロイに使用できる JavaScript シェルを生成します
    - Compare with {current database} - 現在のデータベースとモデルをグラフィカルに比較します（Premium のみ）

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### コマンドラインからの使用
以下のスクリプトを deploy.js ファイルにコピーし、データベース設定を更新してください。また、モデルフォルダの場所に応じて modelFolder を変更する必要があります。
このスクリプトを実行するには、コンピュータに [NodeJs](https://nodejs.org/) がインストールされている必要があります。

```js
const path = require('path');
const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginPostgres = require('dbgate-plugin-postgres');
dbgateApi.registerPlugins(dbgatePluginPostgres);

async function run() {
	await dbgateApi.deployDb({
		connection: {
			server: process.env.DB_SERVER || 'localhost',
			engine: 'postgres@dbgate-plugin-postgres',
			password: process.env.DB_PASSWORD || 'test',
			user: process.env.DB_USER || 'postgres',
			port: process.env.DB_PORT || 5432,
			database: process.env.DB_NAME || 'my_database',
		},
		modelFolder: path.join(__dirname, 'database'),
	});
	await dbgateApi.finalizer.run();
	console.log('Finished job script');
}
dbgateApi.runScript(run);
```

次に、deploy.js のあるディレクトリで以下のコマンドを実行して、必要なモジュールをインストールします:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

以下のコマンドを実行してデータベースデプロイを実行します:
```sh
node deploy.js
```

このスクリプトは PostgreSQL 用です。他のデータベースエンジンではドライバーの変更が必要です。

このスクリプトは DbGate GUI から自動的に生成することもできます。アーカイブフォルダのコンテキストメニューから「Shell: Deploy DB」を使用し、生成されたスクリプトで「Copy nodejs script」を実行すると、有効なスクリプトがコピーされます。require コマンドで使用されるすべてのパッケージは、npm install でインストールする必要があります。
