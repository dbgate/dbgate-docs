---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: zh
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) 是一款免费的浏览器内数据处理工具 —— 无需安装，也无需登录。它基于与 [DbGate Central](../dbgate-central/) 相同的网格、筛选和查询引擎构建，因此两者的浏览、筛选和编辑体验完全一致。

## 学习和教授 SQL

DbGate Lite 使用 WebAssembly，完全在浏览器中运行 **SQLite 和 DuckDB**：

* 在熟悉的 DbGate 网格中针对示例数据库编写并运行 SQL 查询。
* 通过 ER 图直观呈现表之间的关系。
* 无需安装，无需登录 —— 打开网站即可开始工作。

## 临时处理数据文件

在 DbGate Lite 中打开文件，即可像使用数据库一样操作：

* **导入** CSV、JSON 和 Excel 文件，并使用 SQL 查询或编辑它们。
* 清理和重塑数据，然后将结果**导出**回 CSV、JSON 或 Excel。

## 通过链接分享数据库或查询

在 URL 中使用特定的 hash 参数打开 DbGate Lite 时，会自动初始化一个临时数据库：

* `initdbtype` —— 数据库类型，`sqlite` 或 `duckdb`
* `initdbscript` —— 用于创建并填充临时数据库的 SQL 脚本
* `initquery`（可选）—— 在新的查询标签页中打开的 SQL 查询

任何打开该链接的人只需一次点击即可获得相同的示例数据库和查询 —— 这对教程、错误报告和教学都非常有用。

## 发布只读视图

除了分享可编辑的链接之外，您还可以使用工具栏中的 Publish 按钮**发布** CSV/JSON 文件或 BI 报表的只读视图。这会打开一个独立页面 —— 只有数据和明暗主题切换，没有侧边栏或编辑器 —— 任何拥有该链接的人无需账户即可查看。

## 在 Lite、Central、Premium 和 Team Premium 之间做选择

DbGate Lite 最适合学习和一次性任务。对于持续的专业工作，专门的产品更为合适：

* **DbGate Lite** —— 免费，在浏览器中运行。最适合学习 SQL 和处理临时数据文件。
* **[DbGate Central](../dbgate-central/)** —— 用于处理 API 的托管产品：连接实时的 GraphQL、oData 和 Shopify 端点，在工作区中保存连接和报表，并与团队共享。
* **[DbGate Premium](/zh/dbgate/getting-started/installation/)** —— [DbGate](/zh/dbgate/) 的一个版本：功能完整的桌面应用程序，用于处理数据库，使用全套专业工具连接 SQL 和 NoSQL 服务器。
* **[DbGate Team Premium](/zh/dbgate/getting-started/installation/docker-tp/)** —— [DbGate](/zh/dbgate/) 的另一个版本，面向团队：在本地部署运行的共享 Web 界面，让整个团队都能在自己的基础设施上通过浏览器处理数据库。
