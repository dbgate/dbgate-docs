---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: zh
title: 数据库部署
weight: 10
---

*部署功能将在即将发布的版本中发生重大变化，本文档针对最新的 BETA 版本*

DbGate 提供了自动部署数据库的机制。传统方式通常使用迁移 SQL 脚本来实现这一点，而 DbGate 默认采用不同的方式（同时也支持迁移脚本）。
您使用 YAML 文件定义数据库模型，描述表结构和列表数据，并使用 SQL 文件描述视图、存储过程和函数。该模型会被部署到数据库中，比较当前结构与模型中的结构，创建缺失的列和表，并更新视图与存储过程的定义。**不会执行任何破坏性操作**（可能导致数据丢失的操作），因此当您从模型中删除列或表时，它仍会保留在数据库中。如果您在模型中重命名某个列，则会创建一个使用新名称的新列，而旧列仍保留在数据库中。

部署可以从命令行调用（使用 node 脚本），也可以从 DbGate GUI 中调用。您还可以使用数据库比较功能，以可视化方式比较模型与实际数据库之间的差异。

## 表的 yaml 格式

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

- 名称的定义不包含架构名，一个模型描述一个架构
- 默认值以 SQL 表达式的形式定义，因此如果要定义字符串，必须使用 '单引号'
- 您可以为表定义静态数据

### 使用迁移脚本
您可以将较为传统的迁移脚本与 DbGate 特有的部署管理结合使用，某些更特殊的对象可以通过迁移脚本创建。
脚本类型由文件扩展名决定，目录结构由用户自行选择，DbGate 不受其影响。

支持以下脚本扩展名：
- `*.predeploy.sql` - 在每次部署过程之前运行的脚本
- `*.install.sql` - 仅在与上次部署不同时才执行的脚本
- `*.uninstall.sql` - 此脚本与 `.install.sql` 文件配对，在执行新版本的 `*.install.sql` 文件之前执行
- `*.once.sql` - 仅执行一次的脚本
- `*.postdeploy.sql` - 在每次部署过程之前运行的脚本

DbGate 使用 `dbgate_deploy_journal` 表来跟踪已部署到数据库的部署脚本。当您部署任何至少包含一个迁移脚本的项目时，该表会自动创建。


### 在 DbGate GUI 中使用

- 在连接中的数据库右键菜单中，选择 "Export DB model"（仅限 Premium）。数据库模型会保存到目录或文件中。如果您打算使用部署功能，请选择 Data archive 或 Folder (YAML + SQL) 作为目标。
- 打开 archives 小部件，您应该能看到已下载的模型
- 在模型的右键菜单中，您可以对模型执行一些操作：
    - Generate deploy DB SQL - 比较当前数据库（可在状态栏中查看）并生成 SQL 脚本，该脚本会将模型中的变更部署到当前数据库
    - Shell: Deploy DB - 生成可用于部署数据库的 JavaScript shell
    - Compare with {current database} - 以图形方式比较当前数据库与模型（仅限 Premium）

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### 从命令行使用
将以下脚本复制到 deploy.js 文件中并更新数据库配置。您还应根据模型文件夹的位置修改 modelFolder。
运行此脚本需要在您的计算机上安装 [NodeJs](https://nodejs.org/)。

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

然后，在包含 deploy.js 的目录中运行以下命令，安装所需的模块：
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

运行以下命令执行数据库部署：
```sh
node deploy.js
```

此脚本适用于 PostgreSQL，其他数据库引擎需要更改驱动程序。

此脚本也可以从 DbGate GUI 中自动生成，在 archive 文件夹的右键菜单中使用 "Shell: Deploy DB"，然后在生成的脚本上点击 "Copy nodejs script" 即可复制出可用的脚本。require 命令中使用的所有包都必须通过 npm install 安装。
