---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: zh
title: 备份与还原
weight: 20
---

DbGate 使用原生工具来备份和还原数据库。此功能仅在 Premium 版本中提供。

支持的工具：

- PostgreSQL
  - `pg_dump` 和 `psql`
- MySQL+MariaDB
  - `mysqldump` 和 `mysql`

## 如何安装这些工具
如果您使用 Team Premium 版本的 Docker、AWS 或 Azure 版本，则无需处理此问题。这些软件包已经捆绑了所需的全部工具。

最简单的方法是在您的桌面上安装整个数据库引擎。
不过，对于大多数平台和数据库，也可以只安装客户端：

- PostgreSQL
  - Windows - 从 https://www.enterprisedb.com/download-postgresql-binaries 下载并解压客户端
  - Mac：使用 homebrew 安装客户端：`brew install libpq`
- MySQL：
  - Windows - 从 https://dev.mysql.com/downloads/mysql/ 下载并解压 ZIP 包
  - Mac：brew install mysql-client
