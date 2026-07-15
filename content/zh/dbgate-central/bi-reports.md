---
sourceHash: ff92448ee8e00aae1c7fc20030ddea3637a2e8c7952daeac5c129c5fbb48e420
language: zh
title: 基于 API 数据的 BI 报表
weight: 40
---

DbGate Central 会将您的 API 响应加载到其内置的数据引擎中，因此您可以对它们进行组合、聚合和可视化 - 把原始的 API 响应变成易读的 BI 报表。

## 从原始响应到洞察

* **聚合和透视**您的数据，生成汇总表 - 按任意维度进行计数、求和与拆分。
* **关联多个数据源**，使一份报表可以联接位于不同端点背后的数据。
* **向下钻取**各级层次结构，从总体概览深入到单行数据。

oData 和 Shopify 端点（以及 CSV/JSON/Excel 文件）可用作 BI 数据源。GraphQL API 非常适合查询，但目前尚不能作为报表数据源 - 请改为直接浏览和查询它们（参见[查询 GraphQL API](../querying-graphql-apis)）。

## 共享报表

报表可以**发布**为独立的只读视图。任何拥有链接的人都能看到实时数据并进行钻取，无需账户，也无需访问您的连接。

![DbGate Central - turn API data into a report](https://lite.dbgate.io/screenshots/central-bi-dark.png)
