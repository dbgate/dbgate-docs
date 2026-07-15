---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: zh
title: API 连接
weight: 10
---

DbGate 支持连接到 REST API、GraphQL 服务和 OData 端点。这些 API 连接使用与数据库连接相同的界面模式，让你可以在统一的环境中同时处理 API 和数据库。

API 连接支持在 DbGate Premium 中提供。

> 想在不使用桌面应用的情况下浏览 API？[DbGate Central](/zh/dbgate-central/connecting-to-api-endpoints/) 是一个独立的托管式 GraphQL/oData/Shopify 连接实现，专为浏览器从零重新构建。

## GraphQL

GraphQL 连接让你可以与 GraphQL API 交互。DbGate 提供架构内省和查询执行功能。

### 创建 GraphQL 连接

要创建 GraphQL 连接，请使用“新建连接”对话框并选择 GraphQL 作为连接类型。输入 GraphQL 端点 URL，并根据需要配置身份验证。

### 架构内省

DbGate 会自动发现 GraphQL 架构，包括可用的类型、查询、变更及其参数。架构浏览器会显示类型系统，让你可以探索 API 结构。

### 查询编辑器

GraphQL 查询编辑器让你可以编写查询和变更。你可以使用 GraphQL 浏览器，通过从架构中选择字段和参数来构建查询。

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### 变量

GraphQL 查询支持变量。在变量面板中定义变量，并使用标准的 GraphQL 变量语法在查询中引用它们。变量可以在表单中编辑，也可以以原始 JSON 的形式编辑。

### 响应查看器

查询结果会显示在格式化的 JSON 查看器中，采用可展开的树形结构。如果在响应中检测到数组，则会自动显示表格视图。如有需要，你可以切换回原始 JSON 视图。

## OpenAPI (Swagger)

OpenAPI 连接支持提供 OpenAPI 规范（2.0 和 3.0 版本）的 REST API。

### 创建 OpenAPI 连接

新建一个连接并选择 OpenAPI 作为连接类型。提供 OpenAPI 规范文件的 URL（通常是 swagger.json 或 openapi.json）。DbGate 会解析该规范，并提供所有已记录的端点。

### API 文档浏览器

OpenAPI 浏览器会显示所有可用的端点，按标签和路径进行组织。对于每个端点，你可以查看：
- HTTP 方法（GET、POST、PUT、DELETE、PATCH）
- 参数（路径、查询、标头、正文）
- 请求正文架构
- 文档说明

### 执行请求

选择一个端点以打开请求生成器。填写必需的参数、标头和请求正文。执行请求以将其发送到 API 服务器。

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### 响应检查

查看响应的状态码、标头和正文。JSON 响应会被格式化，并且可以在树形视图和表格视图中显示。非 JSON 响应则以文本形式显示。

## OData

OData 连接支持使用标准 OData 查询语法来查询 OData 服务。

### 创建 OData 连接

新建一个连接并选择 OData 作为连接类型。输入 OData 服务的根 URL。DbGate 会获取该服务的元数据文档。

### 元数据浏览

元数据浏览器会显示服务元数据中定义的可用实体集、实体类型、属性和关系。

### 执行查询

OData 查询支持标准的 OData 查询选项：
- `$filter` - 按属性值筛选实体
- `$select` - 指定要返回的属性
- `$expand` - 包含相关实体
- `$orderby` - 对结果排序
- `$top` 和 `$skip` - 分页
- `$count` - 包含结果计数

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

结果以表格形式显示，类似于数据库查询结果。

## 身份验证

所有 API 连接类型都支持多种身份验证方式：

- **API Key** - 指定键名和值，以标头或查询参数的形式发送
- **Bearer Token** - 在 Authorization 标头中发送的 OAuth 或 JWT 令牌
- **Basic Authentication** - 使用 HTTP Basic Auth 的用户名和密码
- **No Authentication** - 适用于公开 API

在连接属性中配置身份验证。

## 数据导出

API 响应数据可以使用 DbGate 标准的导出功能导出为多种格式：
- JSON
- CSV
- Excel
- SQL INSERT 语句
- XML

在表格数据浏览器中使用标准的“导出”上下文菜单选项。

## 使用多个 API

你可以创建到多个 API 和数据库的连接。打开多个请求标签页，即可同时处理不同的端点。

标签页状态在关闭并重新打开应用后会被保留，你可以从已关闭标签页的历史记录中重新打开某个请求。
