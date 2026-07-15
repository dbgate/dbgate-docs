---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: zh
title: 图表
weight: 30
---

在 DbGate 中，你可以使用图表来可视化 SQL 查询结果。只需执行查询，如果自动检测到图表，就会出现 "Chart 1" 标签页。如果有多个查询结果，则可能会有多个图表。

如果没有自动检测到图表，但你希望根据查询结果创建图表，请右键点击查询结果数据并选择 "Open chart"。

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## 图表设置
使用 {{< mdi "pencil" >}} Customize 按钮打开图表设置。你可以配置图表的数据源和样式：
* 图表类型
  * 柱状图（Bar）
  * 折线图（Line）
  * 时间线（Timeline）—— 折线图的特殊形式，X 轴为时间
  * 饼图（Pie）
  * 极区图（Polar area）
* X 轴字段 —— X 轴上的数据。对于日期/时间值，可以使用分组和时间线功能
* 分组字段 —— 根据该字段的值定义多个图表
* X 轴变换 —— 允许为 X 轴时间线定义分组（例如按年或按月）
* Y 轴字段 N —— Y 轴上可以有多个字段
  * 每个数据集都有一个特殊字段 "Count"，用于统计行数
* 聚合函数 —— Sum、Minimum、Maximum、Average、First Value、Last Value

当你更改图表设置中的任何选项时，它会以 front-matter 的形式保存在 SQL 脚本的开头。

## 手动编辑图表定义
某些选项在编辑器中不可用，但可以在 SQL 代码中编辑。更多信息请阅读 [SQL front matter](/zh/dbgate/developer/sql-front-matter)
