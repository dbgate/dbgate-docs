---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: zh
title: 连接到 API 端点
weight: 10
---

DbGate Central 可连接三类 API 端点，并且全部使用同一个"新建连接"对话框。

## 支持的端点类型

* **GraphQL** - 内省架构、浏览类型，并对任何 GraphQL API 运行查询。
* **oData** - 像操作普通表一样使用 oData V4 服务。
* **Shopify** - 通过 Shopify Admin API 连接到你的店铺，浏览商品、订单、客户、元字段等内容。

## 创建连接

打开 **New Connection**（新建连接）对话框，选择连接类型，输入服务 URL，然后选择认证方式：

* **None** - 适用于开放的公共端点。
* **Basic** - 用户名和密码。
* **Bearer token** - 粘贴访问令牌。
* **API key** - 在请求头或查询参数中发送密钥。

连接会保存在你的工作区中，因此下次登录时（在任何设备上）它们都在那里，无需在本地进行任何设置。

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
