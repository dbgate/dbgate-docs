---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: zh
title: DbGate Cloud
weight: 80
---

DbGate Cloud 是用于存储您的连接、SQL 脚本及其他对象的在线存储服务。它还提供了实用 SQL 脚本的公共知识库。

> DbGate Cloud 是**桌面版** DbGate 应用的存储伴侣（连接、SQL 脚本、共享文件夹）。想要托管的、纯浏览器的应用？请参阅 [DbGate Central](/dbgate-central/)。

## 登录
要使用 DbGate Cloud，必须先登录。请使用左侧面板中的 {{< mdi "account-remove-outline" >}} 图标。

您的云存储始终与您的电子邮件地址关联。  
您可以选择以下身份验证提供程序之一：
* GMail
* GitHub
* 电子邮件 - 一次性登录魔法链接将发送到您的邮箱

DbGate 服务器不会存储您的密码。

## 使用存储在云端的连接
登录后，您的云端内容会显示在 {{< mdi "cloud-key" >}} 小部件下。默认情况下，您会看到自己的 Private 文件夹（具有写入权限）。

将连接保存到云端：
* 在连接的上下文菜单中，选择 "Copy to cloud folder"
* 点击 {{<mdi "plus-thick" >}}，然后选择 "Add connection on cloud"

## 哪些连接存储在云端？
* 您的云端连接始终位于 {{< mdi "cloud-key" >}} 小部件下
* 您本地存储的连接位于 {{< mdi "database" >}} 小部件下

## 使用文件夹
除了 Private 文件夹之外，您还可以创建其他文件夹（需要 Premium 版本）。

在 {{<mdi "plus-thick" >}} 按钮下，有以下命令：
* New shared folder - 创建新的共享文件夹。默认情况下，只有您可以访问，您可以邀请其他用户
* Add existing shared folder - 如果您拥有某个共享文件夹（由其他用户创建）的邀请链接，就在这里使用它

如果您想与他人共享您的文件夹，请右键点击该文件夹并选择 "Copy invite link"

## 共享文件夹权限
* Admin - 您对文件夹拥有完全访问权限，可以邀请其他人并写入内容
* Write - 您可以写入/删除内容，但不能邀请其他人
* Read - 仅可读取文件夹内容。请注意，此权限不适用于服务器定义的连接内部可用的数据库

## Community 版本中的共享文件夹
在 Community 版本中，您可以使用由 Premium 用户创建的共享文件夹，但不能创建自己的共享文件夹。这样设计是为了让使用 Premium 版本的团队能够与使用 Community 版本的其他团队成员共享连接、SQL 文件和 ER 图。

## 公共知识库
公共知识库是一系列实用的 SQL 脚本和图表的集合，用于诸如 SQL 性能调优、死锁分析、索引使用情况等任务……知识库在所有版本中均可使用，但图表仅在 Premium 版本中可用。

您可以在左侧小部件面板的 {{< mdi "cloud-search" >}} 图标下查看所有项目。  
灰显的脚本表示这些脚本与当前选定的数据库不兼容。

如果您想用自己的 SQL 脚本来丰富知识库，请向 [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base) GIT 仓库创建拉取请求。

知识库中的脚本使用 [SQL front matter](/zh/dbgate/developer/sql-front-matter) 语法进行注解

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)
