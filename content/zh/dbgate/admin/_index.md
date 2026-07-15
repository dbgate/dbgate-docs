---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: zh
title: 管理
weight: 60
---

管理界面让团队能够将 DbGate 作为共享的多用户 Web 应用来运行：您可以集中管理连接、定义谁可以登录以及如何登录，并通过用户、角色和权限授予对数据库和对象的细粒度访问权。它还托管共享的团队文件。此处配置的所有内容都存储在存储数据库中，而不是本地文件中。

管理工具仅在 Team Premium 版本中可用。在 Community 版本中，请改用[环境变量](/zh/dbgate/customization/env-variables)来配置 DbGate。

管理中的所有配置都保存到存储数据库中 - 请使用 [STORAGE_xxx 环境变量](/zh/dbgate/customization/env-variables/#team-premium-edition-configuration)来配置它。

本节内容：

* [身份验证](auth) - 配置登录方法和身份提供程序
* [连接](connection) - 管理团队可用的连接
* [团队文件](team-files) - 共享 SQL 脚本、ER 图和图表
* [用户](users) - 管理用户账户
* [角色](roles) - 将权限分组为角色
* [权限](permissions) - 授予对连接、数据库和表的访问权

## 管理员访问

管理页面位于 URL https://your_dbgate_instance/admin.html 。 

根管理员应该设置密码。您可以设置环境变量 ADMIN_PASSWORD。如果未定义此变量，DbGate 会在首次使用时询问管理员密码。

之后，您可以为使用不同身份验证方法的其他用户添加管理权限，但首先您必须打开此管理页面。

