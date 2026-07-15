---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: zh
title: 权限
weight: 50
---

DbGate 的权限包含**两个维度**：

1. **权限来源（由谁设置）**
   权限按从宽泛到具体的顺序层层传递。更具体的设置会覆盖更通用的设置：
   * 预定义权限集
   * 预定义角色（*superadmin*、*logged user*、*anonymous*）
   * 自定义角色
   * 单个用户

2. **对象范围**
   权限可以针对特定的**数据库**和**表/对象**。请参阅 **[数据库权限](#database-permissions)** 和 **[表权限](#table-permissions)**。

---

## 基本权限

在 **用户详情** 或 **角色详情** 中的**权限树**里配置全局/基本权限。

* 复选框显示为**灰色**表示该权限是**继承而来**的（例如来自某个角色或预定义权限集），而不是直接在该用户/角色上设置的。

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## 数据库权限

在 **Databases** 选项卡（角色详情和用户详情中均有）上设置数据库级别的权限。

> **重要提示：** 只有在基本权限中未勾选 **“All databases”** 权限时，数据库规则才会生效。

* 规则表中的每一行都会对**匹配**该行筛选条件的数据库授予或拒绝访问权限。
* **规则顺序很重要**：列表中**靠下**的规则会**覆盖**其上方的规则。

![Database permissions - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**列说明**

* **Connection** – 规则适用于哪个连接。
* **Database names** – 要匹配的数据库（名称列表或正则表达式）。
* **Role (access level)**
  * **View** – 可以看到该数据库，但看不到其中的表/视图等。
  * **Read content** – 对数据库内容的只读访问权限。
  * **Write data** – 可以修改表数据。
  * **Run script** – 可以运行任意 SQL 脚本；可以创建/删除/修改对象。
  * **Deny** – 阻止访问该数据库。

---

## 表权限

在 **Tables / Views / Objects** 选项卡（角色详情和用户详情中均有）上设置表/对象级别的权限。

> **重要提示：** 只有在基本权限中未勾选 **“All tables/views/objects”** 权限时，表/对象规则才会生效。

* 每一行都定义了对**匹配**筛选条件的表/对象的访问权限。
* **规则顺序很重要**：列表中**靠下**的规则会**覆盖**其上方的规则。
* 默认情况下，表权限**继承自数据库权限**。

**列说明**

* **Connection** – 规则适用于哪个连接。
* **Database names** – 要匹配的数据库（列表或正则表达式）。
* **Schema names** – 要匹配的架构（列表或正则表达式）。
* **Table names** – 要匹配的对象名称（表/视图/存储过程/触发器），可以是列表或正则表达式。
* **Scope** – 规则涵盖哪些对象类型（表、视图、存储过程、触发器等）。
* **Role (access level)**
  * **Read** – 可以读取表数据。
  * **Update only** – 可以更新行；不允许**插入**和**删除**。
  * **Create, update, delete** - 可以不受限制地编辑行
  * **Run script** – 可以运行涉及此对象的脚本。
    > 注意：如果您在**数据库**级别没有 **“Run script”** 权限，则无法在表级别使用它。
  * **Deny** – 阻止访问该对象。

