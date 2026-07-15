---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: zh
title: 连接
weight: 20
---

从 DbGate 连接到数据库非常简单。你可以通过以下几种方式连接数据库：

* 菜单 文件/添加连接，或 CONNECTIONS 挂件中的 {{< mdi "plus-thick" >}} 图标
* 菜单 文件/新建 SQLite 数据库 - 创建新的 SQLite 数据库
* 菜单 文件/打开 - 你可以打开已有的 SQLite 数据库

## 连接界面
![连接界面](https://media.dbgate.io/img/new-connection-light.png)

连接界面中的字段在很大程度上取决于连接类型。

几个常见字段：

* Server - 数据库服务器的主机名
* Port - 端口，如果使用数据库的默认端口，可以留空
* User、Password - 身份验证
* Password mode（密码模式）
    * Save and encrypt - 密码以加密方式保存，下次无法查看
    * Save RAW - 密码按原样保存（不加密），之后可以查看
    * Don't save, ask for password - 不保存密码，连接时必须输入
    * Don't save, ask for login and password - 登录名和密码都不保存，连接时必须同时输入
* Is read only - 连接将为只读（对于不支持只读会话的引擎，此时你无法执行 SQL 查询）
* Default database - 连接后哪个数据库将处于活动状态
* Use only database *&lt;default database&gt;* - 如果勾选，连接树中只显示默认数据库（服务器上的其他数据库将被隐藏）
* Display name - 该连接在应用程序中显示的名称

## SSH 隧道
你可以在这里配置通过 SSH 隧道的连接。

常见字段：
* Use SSH tunnel - 勾选以使用 SSH 隧道
* Host - SSH 服务器的主机名

![DbGate - SSH 隧道配置](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
配置 SSL 连接。

常见字段：
* Use SSL - 勾选以使用 SSL。在大多数情况下，这是使用 SSL 时唯一需要配置的项

![DbGate - SSL 连接配置](https://media.dbgate.io/img/connection-ssl-window-light.png)
