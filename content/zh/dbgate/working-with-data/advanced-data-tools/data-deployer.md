---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: zh
title: 数据部署器
weight: 2
---

使用数据部署器，您可以可视化地比较并同步 **归档文件夹** 中的数据与 **实际数据库** 中的数据
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## 运行数据部署器
您可以从数据库上下文菜单或归档文件夹上下文菜单运行数据部署器。从数据库运行时，系统会要求您选择归档。从归档运行时，数据部署器将以当前数据库启动。

## 设置
- 数据库服务器、数据库 - 选择要使用的数据库
- 数据归档 - 选择包含数据的文件夹，该文件夹将用于比较和同步
### 表相关
- 键（匹配列） - 选择用于在数据库与归档之间匹配行的列
### 复制器设置
下面的设置（“表”-部署和全局数据部署设置）专用于复制器，详见 [数据复制器](data-replicator) 主题

## 复制数据差异
数据部署器会显示归档与数据库中数据之间的差异。如果您选择了一些存在差异的单元格，就可以将这些差异写入归档或数据库。选中这些单元格后，右下角会出现允许同步的按钮：
- Write x rows, y columns to archive - 将选中的单元格从数据库复制到归档。
- Write x rows, y columns to database - 将选中的单元格从归档复制到数据库。首先会显示包含变更 SQL 的确认对话框。

## 数据复制器操作
- Deploy into DB - 此操作按配置的设置将变更部署到数据库
- Generate shell - 此操作会创建一个用于执行部署的 JavaScript 文件。该文件可以从命令行运行
- Generate SQL - 创建将变更从归档部署到数据库的 SQL

有关这些操作的更多信息，请参阅 [数据复制器](data-replicator) 主题
