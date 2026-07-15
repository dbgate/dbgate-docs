---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: zh
title: DbGate
weight: 5
---

## 什么是 DbGate？

DbGate 是一款数据库管理工具，可以连接受支持的数据库并对其进行操作。它既是桌面应用，也是 Web 应用。其设计目标是快速且易于使用。

关于在浏览器中运行的产品和托管产品（DbGate Lite、Central 和 Shopify App），请参阅[产品概览](/zh/)。

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## 支持的数据库

| 数据库 | {{< center "Community" >}} | {{< center "Premium" >}} | 额外功能 |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | 备份、还原 |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | 备份、还原 |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | 备份、还原 |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## 支持的平台

- 桌面
  - Windows
  - MacOS（ARM 和 Intel 处理器均支持）
  - Linux
- Web 版本
  - Docker
  - NPM
  - Azure
  - AWS

## 版本

DbGate 提供三个版本：

| 版本 | 分发方式 | 主要功能 |
|---|---|---|
| Community | 桌面应用，或自托管 Web（Docker/NPM），免费 | 连接并浏览/编辑标准 SQL 和 NoSQL 数据库、Redis GUI、最多 5 个 DbGate Cloud 连接/文件 |
| Premium | 桌面应用（单用户） | 包含 Community 的全部功能，另外还有[查询设计器](sql-and-queries/query-designer)、[图表](working-with-data/charts)、[可编辑的查询结果和视图](sql-and-queries/sql-editor)、[主从视图](working-with-data/data-browser)、[AI 工具](working-with-data/ai-features)（数据库对话、错误解释、主题助手）、比较和部署数据库模型、高级/批量导出导入、[数据部署器](working-with-data/advanced-data-tools/data-deployer)、[API 连接](developer/api-connections)（GraphQL/oData/OpenAPI）、更多数据库引擎（libSQL、CosmosDB、Amazon Redshift、Firestore、Amazon DynamoDB）、无限量的 DbGate Cloud 存储 |
| Team Premium | 桌面应用 + 自托管 Web（Docker/NPM/AWS/Azure） | 包含 Premium 的全部功能，另外还有 Web 应用、[管理界面](admin)、用户/角色/权限、外部身份提供程序（OAuth/OIDC）、零配置的原生备份和还原 |

## 本章节内容

* [入门指南](getting-started) - 安装 DbGate 并连接到您的第一个数据库
* [使用数据](working-with-data) - 浏览、编辑、筛选、绘制图表、绘制地图、导出和归档数据
* [SQL 与查询](sql-and-queries) - SQL 编辑器、可视化查询设计器和 ER 图
* [数据库操作](database-operations) - 编辑架构、比较和部署模型、备份和还原
* [自定义](customization) - 配置外观和运行时设置
* [管理](admin) - 管理用户、角色和权限（Team Premium）
* [开发者与自动化](developer) - 脚本、API 连接和插件
* [DbGate Cloud](dbgate-cloud) - 在线存储您的连接、SQL 脚本和共享文件夹
