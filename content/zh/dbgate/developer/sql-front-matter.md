---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: zh
title: SQL Front Matter
weight: 50
---

SQL front matter 是位于 SQL 文件开头的 YAML 格式元数据。这一概念的灵感来自 gohugo 和 Jekyll，它们为 markdown 文件引入了 front matter。（[Hugo 中的 Front matter](https://gohugo.io/content-management/front-matter/)）

SQL front matter 从 SQL 文件开头的文件标记 `-- >>>` 处立即开始，并以仅包含 `-- <<<` 的行结束。YAML 内容的每一行都以 `-- `  前缀开头，因此整个文件仍然是有效的 SQL。

此元数据尤其用于图表（保存图表配置）以及公共知识库属性（如脚本标题和描述）。但也有一些属性可用于 DbGate 中的每个 SQL 脚本。

## 通用属性
- autoExecute：`true` 或 `false`，脚本在打开时是否自动执行
- splitterInitialValue：百分比（如 20%）或绝对尺寸（如 220px）- 用于定义上方 SQL 区域的大小。其余部分将用于查询结果

## 公共知识库属性
- title：脚本标题（默认值 - 不含扩展名的文件名）
- description：脚本描述（默认值 - 空）
- icon：脚本图标（来自 [Material design icons](https://pictogrammers.com/library/mdi/)，格式为 `mdi mdi-chart-pie`）

## 图表属性
- selected-chart：要自动选中的图表编号（从 1 开始）
- chart-N：第 N 个图表的定义
    - title：图表标题
    - pieRatioLimit - 饼图的限制值，如果数值低于此值，将被归入 "Other"（默认值：0.05）
    - pieCountLimit - 饼图扇区数量的限制，如果扇区数量超过此值，将被归入 "Other"（默认值 10）
    - dataLabelFormatter - 数据标签的格式化器，取值为 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb' 之一

如需完整的最新字段列表，可以使用 [TypeScript 定义](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts)，参见 `ChartDefinition` 接口

## 示例

```sql
-- >>>
-- selected-chart: 1
-- chart-1:
--   chartType: bar
--   xdef:
--     field: InvoiceDate
--     transformFunction: date:month
--   ydefs:
--     - field: Total
--       aggregateFunction: sum
-- <<<
SELECT
  `InvoiceId`,
  `CustomerId`,
  `InvoiceDate`,
  `BillingAddress`,
  `BillingCity`,
  `BillingState`,
  `BillingCountry`,
  `BillingPostalCode`,
  `Total`
FROM
  `Invoice`
```
