---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: zh
title: 查询设计器
weight: 20
---

查询设计器 *(Premium)* 让你以可视化方式构建 SQL 查询，无需手写 SQL。将表添加到画布上，选择列并定义条件 - DbGate 会为你生成 SQL。

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## 构建查询

* **添加表** - 将表拖放到设计画布上；DbGate 会根据外键自动绘制关系。
* **选择列** - 选择结果中显示哪些列，定义排序和分组。
* **JOIN 类型** - 除了标准的 SQL 连接（`INNER`、`LEFT`、`RIGHT`）之外，你还可以使用伪连接 - 其中最有用的是 `WHERE NOT EXISTS`。
* **强大的筛选** - 使用与[数据浏览器](/zh/dbgate/working-with-data/data-browser/)相同的引擎进行筛选，包括复合条件和按值集合筛选。

## 结果

设计器生成的是普通的 SQL 查询，因此其运行性能与手写的 SQL 相同。你可以随时切换到生成的 SQL，并在 [SQL 编辑器](sql-editor)中继续编辑它。

## Perspectives - 通用设计器

对于嵌套的层次化视图 - 以及在客户端连接 SQL 表和 MongoDB 集合的数据 - 请使用 [Perspectives](/zh/dbgate/working-with-data/perspectives/)，它不受源数据库能够连接什么的限制。
