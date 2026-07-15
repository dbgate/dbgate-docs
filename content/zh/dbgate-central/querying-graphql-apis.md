---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: zh
title: 查询 GraphQL API
weight: 20
---

将 DbGate Central 指向任意 GraphQL API，它就会自动发现可用的内容 —— 无需翻阅单独的文档。

## 浏览架构

连接后，DbGate Central 会立即对 GraphQL 架构进行内省。在树中浏览可用的类型和字段，然后打开查询标签页开始工作。

## 运行查询

* 使用 GraphQL 编辑器编写查询，并针对实时 API 运行它们。
* 在查询旁提供查询变量，可以使用表单形式，也可以使用原始 JSON。
* 结果会显示在 DbGate 中随处可见的那种快速、可排序、可筛选的网格里，因此 GraphQL 响应用起来就像数据库表一样。
* 嵌套的对象和列表以结构化 JSON 的形式返回，你可以就地展开并查看。

已查询的视图会按连接进行缓存，因此在你继续工作时重新打开它们是即时的。

> DbGate Central 中的 GraphQL 连接是一个独立的、基于浏览器的实现，与[桌面版 GraphQL 功能](/zh/dbgate/developer/api-connections/#graphql)不同 —— 如果你使用的是桌面应用，请参阅该页面。

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
