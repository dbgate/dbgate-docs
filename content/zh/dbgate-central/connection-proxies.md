---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: zh
title: 连接代理
weight: 60
---

DbGate Central 可以通过在私有网络内运行的一个小型出站代理程序转发流量，从而访问位于该私有网络中的 oData 和 GraphQL API。Shopify 和 OpenAPI 连接无法使用代理。

## 设置代理

1. 打开 **Settings** 选项卡，在 *Connection proxies* 下创建一个 **proxy**。复制它生成的令牌。
2. 勾选该代理可以服务的 oData/GraphQL 连接。每次更改都会重新生成令牌，因此更改选择后请重启代理程序。
3. 在你的私有网络内运行代理程序：
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   该代理程序仅建立出站连接 - 无需对你的网络进行任何入站访问。
4. 代理程序运行并连接后，对被代理连接的请求就会通过它进行路由。如果代理未连接，DbGate Central 会回退到直接获取数据。

同样的路由方式也适用于 [MCP 服务器](../mcp-server)：当 MCP 工具读取被代理的连接时，请求会经过同一个代理。
