---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: zh
title: 导出与导入
weight: 20
---

DbGate 拥有灵活的导出/导入系统，既支持简单的一键导出，也支持复杂的自定义设置。

## 简单的一键导出

如果你不需要任何配置，只是想把数据导出到文件，可以使用简单导出。有多种方式可以调用简单导出：
- 表/视图/集合的右键菜单，导出
- 表数据，"Export" 右键菜单或 {{<mdi "export" >}} 按钮。筛选条件同样会应用到导出的数据
- 查询结果，"Export" 右键菜单或 {{<mdi "export" >}} 按钮

在桌面应用中，你可以直接保存导出的文件。

在 Web 应用中，导出的文件会以下载的形式提供。

## 高级导出/导入
如果你需要配置更多细节，或者一次性导出多个表，就需要使用"高级导出"。  
导入使用的是同一个配置工具，只是源和目标的配置互换了。

高级导出/导入可以从以下位置调用：
- 与简单导出相同的位置，只是在文件格式处选择 "Export advanced..."
- 数据库右键菜单，选择 "Export" 或 "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} 源配置
* Storage type - 选择数据来源
  * Database - 此时你配置的是"导出"
    * 选择多个源表
  * File (JSON, CSV, DBF...) - 此时你配置的是"导入"
    * 打开或拖放源文件
  * Query - 大多数情况下你不需要它，但你可以在这里直接输入查询。当你导出例如经过筛选的表数据时，内部会使用此选项。
  * Archive - 从[数据归档](advanced-data-tools/archives)导入/导出数据

### {{<mdi "export" >}} 目标配置
* Storage type - 与源配置相同，但含义相反
  * Database - 你配置的是"导入"
  * File (JSON, CSV, DBF...) - 你配置的是"导出"

### {{< mdi "table-multiple" >}} 映射源表/文件
你可以映射输入文件/表如何转换为输出

### 操作按钮
  * {{< mdi "play" >}} Run - 运行定义好的导入/导出作业
  * {{< mdi "flash" >}} Generate script - 创建运行该作业的 JavaScript 代码。你可以在 DbGate shell 控制台中运行它，也可以将其导出到文件并使用 nodejs 从命令行运行
  * {{< mdi "content-save" >}} Save - 保存作业以备后用

## 导入/导出脚本
DbGate 中的所有导入/导出作业首先都会被转译成脚本。以下是将 SQLite 表导出为 CSV 的示例。

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

你也可以在没有 DbGate 的情况下运行此脚本。在脚本编辑器中使用右键菜单 "Copy nodejs script"，它会复制以下脚本：

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

在脚本所在文件夹中安装所用的依赖（require() 函数中使用的所有包）之后：

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

你可以使用以下命令运行此脚本：

```sh
node myExportScript.js
```
