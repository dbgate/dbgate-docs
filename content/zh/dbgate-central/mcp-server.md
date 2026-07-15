---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: zh
title: 面向 AI 智能体的 MCP 服务器
weight: 50
---

DbGate Central 可以将您的工作区作为远程 **MCP（Model Context Protocol，模型上下文协议）** 连接器暴露给 [Claude](https://claude.ai) 等 AI 助手 —— 这样智能体就能像您一样探索和查询您的 API，而访问权限始终由您掌控。

## 设置方法

1. 打开 **Settings** 标签页并创建一个 **MCP profile**。复制它的 **Server URL**（`https://central.dbgate.cloud/mcp/{profileId}`）、**Client ID** 和 **Client Secret**。
2. 在 claude.ai（或其他兼容 MCP 的客户端）中，使用该 URL 和 OAuth 凭据添加一个自定义连接器。
3. 在每个连接的编辑器中，设置其 **MCP access** 级别 —— **No access**、**Read-only** 或 **Writable**。默认是无访问权限，因此在您授权之前不会共享任何内容。
4. 助手会执行 OAuth 握手，您同意后，连接器即绑定到该 profile 和工作区。

每个工作区可以拥有多个 MCP profile，每个 profile 都有自己的 URL、凭据和按连接授予的权限。身份验证使用带强制 PKCE 的 OAuth 2.1，客户端密钥以加密方式静态存储。

## 智能体可以做什么

适用于 **oData**、**GraphQL** 和 **Shopify** 连接（SQLite/DuckDB 仅限浏览器，不在 MCP 的支持范围内）：

* **列出连接** —— 该 profile 被允许使用的连接。
* **列出实体** —— 表、视图或目录实体。
* **检查架构** —— 列名和类型。
* **查询行** —— 筛选、分页和选择数据。
* **更新行** —— 仅限 Shopify，且仅在您授予 Writable 访问权限时可用。

由于读取和写入复用与数据网格和调度器相同的引擎，智能体看到的数据和能力与您完全一致 —— 绝不会超出您授予的访问权限。

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
