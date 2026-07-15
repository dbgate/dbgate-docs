---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: zh
title: 数据浏览器和编辑器
weight: 5
---

数据浏览器是 DbGate 用于查看和编辑表数据的核心视图。打开任意表、视图或集合，即可获得快速的、类似 Excel 的网格。本页介绍浏览、编辑以及在相关数据之间导航；关于筛选表达式，请参阅[数据筛选](data-filtering)。

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## 浏览数据

* **键盘导航** - 使用方向键在网格中移动，就像在电子表格中一样。
* **排序** - 单击列标题即可按该列排序。
* **筛选** - 使用网格上方的筛选行筛选行；完整的表达式语法请参阅[数据筛选](data-filtering)。
* **列管理器** - 按名称查找列，并隐藏不需要的列。
* **高级复制** - 将选定的单元格复制为 CSV、YAML、SQL `INSERT` 语句或 MongoDB 插入语句。

## 编辑数据

数据编辑直接在网格中进行：

* **类似 Excel 的编辑** - 就地编辑单元格；复制和粘贴行区域，包括在不同表之间。
* **暂存的更改** - 你的编辑会作为待处理更改收集起来。在更改影响数据库之前，先查看生成的 SQL 更改脚本，然后保存或还原。
* **插入和删除行** - 可从网格或右键菜单进行。

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### 数据编辑器宏 *(Premium)*

对选定的单元格应用预定义的宏 - 例如更改文本大小写、移除变音符号或生成 UUID。

## 处理相关数据

DbGate 让你可以轻松地跟踪表之间的关系：

* **关系提示** - 在数字外键旁边显示被引用表中的文本值。
* **外键列展开** - 展开外键列，以内联方式查看被引用的数据。
* **打开明细** - 跳转到外键所引用的行。
* **主从视图** *(Premium)* - 在关联的主从布局中浏览相关行。

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## 表单视图

表单视图将单行显示为垂直的“转置”列表 - 非常适合列很多的表。它以树状视图的方式工作，因此可以展开外键列来浏览相关数据。

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## 分组 *(Premium)*

在网格视图中应用分组（`GROUP BY`），在浏览的同时直接聚合行。

## 相关页面

* [数据筛选](data-filtering) - 筛选表达式语法
* [导出和导入](export-import) - 将数据导入表或从表中导出
* [透视图](perspectives) - 针对复杂关联数据的嵌套只读视图
* [SQL 编辑器](/zh/dbgate/sql-and-queries/sql-editor/) - 以相同的方式编辑查询结果 *(Premium)*
