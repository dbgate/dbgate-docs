---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: zh
title: 数据筛选
weight: 10
---

DbGate 拥有强大的数据筛选引擎，既支持非常简单的数据筛选，也支持复杂的条件。

数据筛选器可以在 DbGate 的许多地方使用，但最常见的地方是筛选数据网格。

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

筛选器会以背景色填充：
* 绿色背景 —— 筛选器正确并已应用
* 红色背景 —— 筛选器表达式有错误，该筛选器被忽略

你有多种创建筛选器的方式：
* {{< mdi "filter" >}} —— 显示包含预定义筛选器和对话框的菜单
* {{< mdi "dots-vertical" >}} —— 允许你选择要筛选的值
* 你可以直接编写筛选器 —— 使用 [filter-expressions](#filter-expressions) 中描述的非常简单的语法
* 或者你可以用可视化方式创建筛选器，然后手动编辑它

其他命令：
* {{< mdi "filter-off" >}} —— 清除所有筛选器

## Filter expressions
筛选表达式的设计力求直观，在大多数情况下，你只需直接写出想要搜索的内容。不过，其语法相当强大，你可以组合多个条件并使用各种运算符。
表达式语法取决于列的数据类型。

### 示例

| 列类型 | 筛选表达式 |  说明 |
|----------|-------------|------|
| string | canada | 列值包含文本 "canada" |
| string | canada, usa | 列值包含文本 "canada" 或 "usa" |
| string | canada lake | 列值包含文本 "canada" 和 "lake" |
| string | NOT EMPTY NOT NULL | 字符串的值非空 |
| number | >10 | 列值大于 10 |
| number | >=5 <=10 | 列值介于 5 和 10 之间 |
| number | 1,2,3 | 列值为 1 或 2 或 3 |
| datetime | 2020-05-26 | 日期值为 2020-05-26（24 小时区间） |

### 通用筛选器（适用于所有数据类型）
- NULL - 列值为 null
- NOT NULL - 列值不为 null
- {$$ is null} - SQL 条件，写在 {} 大括号中。$$ 是被筛选列的占位符

### 文本筛选器
文本比较不区分大小写。
- text - 列值包含 _text_。可以用 'single quotes' 或 "double quotes" 括起来
- +text - 列值包含 _text_（与上一行相同）
- ^text - 列值以 _text_ 开头
- $text - 列值以 _text_ 结尾
- !+text - 列值不包含 _text_（与上一行相同）
- !^text - 列值不以 _text_ 开头
- !$text - 列值不以 _text_ 结尾
- EMPTY - 列值不包含非空白字符
- NOT EMPTY - 列值包含非空白字符

### 数字筛选器
- number - 列值等于 number
- =number - 列值等于 number
- !=number - 列值不等于 number
- <>number - 列值不等于 number
- <number - 列值小于 number
- \>number - 列值大于 number
- <=number - 列值小于或等于 number
- \>=number - 列值大于或等于 number

### 日期时间筛选器
- 2021 - 列值的年份
- 2021-02 - 列值的年份、月份
- 2021-02-15 - 列值的年份、月份、日
- 2021-02-15 23:15 - 列值的年份、月份、日、时、分
- 2021-02-15 23:15:51 - 列值的年份、月份、日、时、分、秒
- 相对于当前日期的筛选器
  - YESTERDAY
  - TODAY
  - TOMORROW
  - LAST WEEK
  - THIS WEEK
  - NEXT WEEK
  - LAST MONTH
  - THIS MONTH
  - NEXT MONTH
  - LAST YEAR
  - THIS YEAR
  - NEXT YEAR

### 逻辑（布尔）筛选器
- TRUE, true, 1 - 列值为 true/1
- FALSE, false, 0 - 列值为 false/0

### 筛选器的组合
筛选器可以组合在一起。空格被解释为 AND 运算符，逗号被解释为 OR 运算符。AND 的优先级高于 OR。
