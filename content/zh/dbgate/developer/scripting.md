---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: zh
title: 脚本编写
weight: 40
---

DbGate 由多个 [NPM 包](https://www.npmjs.com/search?q=keywords%3Adbgate)组成，这些包可以在 nodejs 脚本中使用

通常你会需要以下这些包：
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - 实现各种实用函数
* dbgate-plugin-`engine` - 一组连接器插件，实现与数据库的连接以及特定数据库引擎的相关操作
* dbgate-plugin-`fileformat` - 如果你使用导出为 CSV 或 XML，这些格式提供程序是作为外部插件实现的

[API 文档](/zh/dbgate/developer/apidoc)

## 从 DbGate 生成脚本
DbGate 的许多功能在内部都是通过脚本接口实现的。因此，当你使用某个类似导出的操作时，在某处会有一个 "Generate Shell script"（生成 Shell 脚本）按钮，它会为你生成 nodejs 脚本。

如果你想使用 nodejs 脚本进行导出，可以按照以下步骤操作：
* 右键点击表，选择 "Export/Export advanced"（导出/高级导出）
* 配置你的导出
* 在底部工具栏选择 "Generate script"（生成脚本）。现在你可以编辑该 JS 脚本并在 DbGate 中运行它
* 如果你在底部工具栏选择 "Copy nodejs script"（复制 nodejs 脚本），你可以将其保存到 js 文件中，并使用计算机上已安装的 [nodejs](https://nodejs.org/) 运行它


## 示例 1 - 将表导出为 CSV
这是一个简单的示例，我们使用了 `dbgateApi` 包中的 [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) 和 `dbgate-plugin-csv` 中的 writer。同时还需要 `dbgate-plugin-mysql`，因为我们使用了引擎参数 `mysql@dbgate-plugin-mysql`
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
