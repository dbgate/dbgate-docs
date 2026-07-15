---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: ja
title: スクリプティング
weight: 40
---

DbGate は複数の [NPM パッケージ](https://www.npmjs.com/search?q=keywords%3Adbgate) で構成されており、これらは nodejs スクリプト内で使用できます

通常、以下のパッケージが必要になります:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - ユーティリティ関数を実装します
* dbgate-plugin-`engine` - コネクタープラグインのセットで、データベースへの接続および指定されたデータベースエンジン固有の操作を実装します
* dbgate-plugin-`fileformat` - CSV や XML へのエクスポートを使用する場合、これらのフォーマットプロバイダーは外部プラグインとして実装されています

[API のドキュメント](/ja/dbgate/developer/apidoc)

## DbGate からスクリプトを生成する
DbGate の多くの機能は、内部的にスクリプティングインターフェースで実装されています。そのため、エクスポートのような操作を使用する際には、どこかに「Generate Shell script」ボタンがあり、nodejs スクリプトを生成してくれます。

エクスポートに nodejs スクリプトを使用したい場合は、以下の手順で行えます:
* テーブルを右クリックし、「Export/Export advanced」を選択します
* エクスポートを設定します
* 下部のツールバーで「Generate script」を選択します。これで JS スクリプトを編集し、DbGate 内で実行できます
* 下部のツールバーで「Copy nodejs script」を選択すると、これを js ファイルに保存し、お使いのコンピューターにインストールされた [nodejs](https://nodejs.org/) で実行できます


## 例 1 - テーブルを CSV にエクスポートする
これは簡単な例で、`dbgateApi` パッケージの [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) と `dbgate-plugin-csv` の writer を使用しています。また、エンジンパラメーター `mysql@dbgate-plugin-mysql` を使用しているため、`dbgate-plugin-mysql` も必要です
```js
const dbgateApi = require('dbgate-api');
const dbgatePluginMysql = require("dbgate-plugin-mysql");
const dbgatePluginCsv = require("dbgate-plugin-csv");

dbgateApi.registerPlugins(dbgatePluginMysql);

async function run() {
  const reader = await dbgateApi.tableReader({
    connection: { server: 'localhost', engine: 'mysql@dbgate-plugin-mysql', user: 'root', password: 'xxxx', database: 'Chinook' },
    pureName: 'Customer',
  });
  const writer = await dbgatePluginCsv.shellApi.writer({ fileName: 'Customer.csv' });
  await dbgateApi.copyStream(reader, writer);

  console.log('Finished job script');
}
dbgateApi.runScript(run);
```