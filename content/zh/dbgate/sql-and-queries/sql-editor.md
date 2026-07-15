---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: zh
title: SQL 编辑器
weight: 10
---

SQL 编辑器是您针对连接编写和运行 SQL 脚本的地方。可以通过工具栏中的 {{< mdi "flash" >}} “新建查询”按钮打开它，也可以从连接或数据库的上下文菜单中打开。

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## 运行 SQL

* **执行脚本** - 使用 {{< mdi "play" >}} 执行按钮（或 F5）运行整个脚本。
* **执行当前语句** - 仅运行光标所在的语句。
* **运行选中内容** - 如果您选中了脚本的一部分，则只会执行选中的文本。
* 结果显示在编辑器下方的结果网格中。多个结果集会显示在各自独立的选项卡中。
* 消息、行数和错误显示在 **Messages** 选项卡中。

## 编辑辅助功能

* **SQL 代码格式化工具** - 重新格式化当前脚本，使缩进和大小写保持一致。
* **代码补全** - 基于已连接数据库架构的表、列和关键字建议。
* **联接助手** - “Add SQL join”工具可根据外键生成 `LEFT`/`INNER`/`RIGHT JOIN` 子句，因此您无需手动输入联接条件。

## 使用结果

结果网格使用与[数据浏览器](/zh/dbgate/working-with-data/data-browser/)相同的引擎，因此您可以[筛选和排序](/zh/dbgate/working-with-data/data-filtering/)、以各种格式复制单元格，并[导出](/zh/dbgate/working-with-data/export-import/)结果。

### 编辑查询结果和视图 *(Premium)*

当 DbGate 能够将结果映射回单个表或可更新视图时，查询结果即可编辑。您可以直接在结果网格中编辑单元格，查看生成的变更脚本，并将其保存回数据库 - 这与[数据浏览器](/zh/dbgate/working-with-data/data-browser/)中的暂存变更工作流程相同。同样支持编辑视图。

> 可编辑的查询结果和可编辑的视图是在 DbGate 7.2 中引入的。

## 事务控制

您可以从编辑器中控制事务 - 在显式事务中执行，并提交或回滚变更，这在测试修改数据的脚本时非常有用。

## 其他编辑器

* **Mongo JavaScript 编辑器** - 对于 MongoDB 连接，使用 NodeJS 语法编写和执行 Mongo 脚本。
* **Redis** - 浏览 Redis 键树，从选定的键生成脚本并运行 Redis 脚本。
