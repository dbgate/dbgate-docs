---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: zh
title: 透视图
weight: 50
---

透视图（Perspective）是复杂嵌套数据的只读视图。它类似于报表，但透视图只需将数据添加到视图中即可创建。你可以使用透视图设计器，它允许你按照外键以外的其他关系来联接数据。

透视图可以轻松地将数据联接在一起，并显示分组。

<!-- ![screenshot](/screenshots/perspective1.png) -->

## 创建透视图
透视图可以从 SQL 表和视图创建（目前尚不支持 MongoDB 集合，但已计划提供该支持）。
使用表/视图的上下文菜单，选择“Open perspective”（打开透视图）。

![screenshot](/img/perspective-create.png)

DbGate 会打开一个简单的透视图，其中只显示一列。该列由启发式算法选出，作为整行的最佳表示。
## 自定义透视图
你可以定义视图中有哪些列可用。你也可以将引用的数据添加到视图中。使用展开按钮浏览引用树。

## 筛选数据
在表中或左侧的列列表中使用上下文菜单，选择“Add to filter”（添加到筛选器）。你可以使用与 DbGate 中其他位置相同的筛选表达式。或者你可以在表格单元格上使用上下文菜单命令“Filter this value”（筛选此值）。

## 筛选父行
假设有以下透视图。我们有主/从关系：Genre 及其相关的 tracks。我们想按 Track 进行筛选（这里尝试搜索“mix”文本）。

![screenshot](/img/parentrows1.png)

如你所见，有很多 Genre 行没有任何符合搜索条件的 track。如果你也想筛选 Genre 行，请在表头的上下文菜单中使用“Filter parent rows”（筛选父行）命令。你也可以使用筛选行中的切换按钮。

![screenshot](/img/parentrows2.png)

## 定义自定义联接
透视图与外键配合得非常好。但即使你的数据库没有外键，也可以使用此功能。你可以定义带有任意条件的自定义联接。你甚至可以定义到其他数据库的自定义联接（该数据库可以位于不同的数据库服务器上，甚至使用不同的底层数据库引擎）。

![screenshot](/img/customjoin.png)

你也可以通过拖放列来创建联接关系。

![screenshot](/img/customjoin2.png)
