---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: ja
title: エクスポートとインポート
weight: 20
---

DbGate には柔軟なエクスポート/インポートシステムがあり、シンプルなワンクリックエクスポートから複雑なカスタム設定まで対応できます。

## シンプルなワンクリックエクスポート

設定が不要で、データをファイルにエクスポートするだけでよい場合は、シンプルエクスポートを使用できます。シンプルエクスポートを呼び出す方法はいくつかあります。
- テーブル/ビュー/コレクションのコンテキストメニューの「Export」
- テーブルデータの「Export」コンテキストメニューまたは {{<mdi "export" >}} ボタン。フィルターはエクスポートされるデータにも適用されます
- クエリ結果の「Export」コンテキストメニューまたは {{<mdi "export" >}} ボタン

デスクトップアプリケーションでは、エクスポートしたファイルを直接保存できます。

Web アプリでは、エクスポートしたファイルはダウンロードとして提供されます。

## 高度なエクスポート/インポート
より詳細な設定が必要な場合や、複数のテーブルを一度にエクスポートしたい場合は、「Advanced export」を使用する必要があります。  
インポートにも同じ設定ツールが使用され、ソースとターゲットの設定が入れ替わるだけです。

高度なエクスポート/インポートは次の場所から呼び出せます。
- シンプルエクスポートと同じ場所で、ファイル形式の代わりに「Export advanced...」を選択します
- データベースのコンテキストメニューで「Export」または「Import」を選択します


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} ソース設定
* ストレージタイプ - データのソースを選択します
  * Database - この場合は「Export」を設定します
    * 複数のソーステーブルを選択します
  * File (JSON, CSV, DBF...) - この場合は「Import」を設定します
    * ソースファイルを開くか、ドラッグ＆ドロップします
  * Query - ほとんどの場合これは必要ありませんが、ここで直接クエリを入力できます。このオプションは、フィルターされたテーブルデータをエクスポートする場合などに内部的に使用されます。
  * Archive - [データアーカイブ](advanced-data-tools/archives)からデータをインポート/エクスポートします

### {{<mdi "export" >}} ターゲット設定
* ストレージタイプ - ソース設定と同じですが、意味が逆になります
  * Database - 「Import」を設定します
  * File (JSON, CSV, DBF...) - 「Export」を設定します

### {{< mdi "table-multiple" >}} ソーステーブル/ファイルのマッピング
入力ファイル/テーブルが出力にどのように変換されるかをマッピングできます

### アクションボタン
  * {{< mdi "play" >}} Run - 定義したインポート/エクスポートジョブを実行します
  * {{< mdi "flash" >}} Generate script - 定義したジョブを実行する JavaScript コードを作成します。DbGate のシェルコンソールで実行することも、ファイルにエクスポートして nodejs を使ってコマンドラインから実行することもできます
  * {{< mdi "content-save" >}} Save - ジョブを後で使用できるように保存します

## インポート/エクスポートスクリプト
DbGate のすべてのインポート/エクスポートジョブは、最初にスクリプトへトランスパイルされます。以下は SQLite のテーブルを CSV にエクスポートする例です。

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

このスクリプトは DbGate なしで実行することもできます。スクリプトエディターのコンテキストメニューから「Copy nodejs script」を使用してください。次のスクリプトがコピーされます。

```js

const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginSqlite = require('dbgate-plugin-sqlite');
const dbgatePluginCsv = require('dbgate-plugin-csv');
dbgateApi.registerPlugins(dbgatePluginSqlite,dbgatePluginCsv);

require=null;
async function run() {

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);


await dbgateApi.finalizer.run();
console.log('Finished job script');
}
dbgateApi.runScript(run);
```

スクリプトのあるフォルダーに、使用されている依存関係（require() 関数で使用されているすべてのパッケージ）をインストールした後、

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

次のコマンドでこのスクリプトを実行できます。

```sh
node myExportScript.js
```
