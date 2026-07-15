---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: zh
title: AI 功能
weight: 55
---

DbGate 包含多项由 AI 驱动的功能 *(Premium 和 Team Premium)*。所有 Premium 用户都可以使用它们，无需 API 密钥或任何配置 —— DbGate 使用自己的 AI 网关，将请求转发给 LLM 提供商。

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## 数据库聊天

数据库聊天是一个既理解数据库结构、也理解其中数据的 AI 聊天机器人。

* **自然对话** - 用任何自然语言提问，获得答案或可直接运行的 SQL。
* **上下文感知** - 模型了解你的数据库结构，并（在获得许可时）了解实时数据，因此能够建议正确的连接、筛选和聚合。
* **迭代式** - 使用诸如“添加日期筛选”或“按客户分组”这样的指令进行细化，查询会立即更新。
* **图表** - 请求根据结果生成柱状图、饼图或折线图。
* **顾问模式** - 它可以分析存储过程和视图，因此你可以问“解释过程 X”或“哪些表受过程 Y 影响”之类的问题。DbGate 会显示分析了哪些对象。

### 执行 SQL - 安全第一

数据库聊天可以运行 SQL 来回答问题。你可以选择方式：

* **执行 SQL 前询问（默认）** - DbGate 在运行每个查询之前都会询问。
* **自动执行 SQL** - 非 `SELECT` 查询仍需要确认。
* **从不执行，仅建议 SQL** - 聊天只显示查询；不会向 LLM 发送数据库中的任何数据。

如果建议的查询失败，DbGate 会把错误发送回模型，模型通常会自动纠正查询。

## SQL AI 助手

把聊天当作 SQL 助手使用 —— “编写一个查询销售额前 10 名客户的 SQL 查询” —— 并在 [SQL 编辑器](/zh/dbgate/sql-and-queries/sql-editor/) 选项卡中打开结果。

## 解释 SQL 错误

点击错误消息旁边的 **Explain**，即可获得 AI 对出错原因和修复方法的解释。

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## 主题 AI 助手

AI 还可以生成自定义配色主题 - 参见[自定义主题](/zh/dbgate/customization/custom-themes/)。

## 禁用 AI 功能

可以通过 DbGate 设置完全关闭 AI 功能（例如在受限环境中）。
