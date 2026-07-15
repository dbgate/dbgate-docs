---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: zh
title: 角色
weight: 40
---

## 角色选项卡
配置角色、角色权限以及角色与连接的映射关系。您可以创建自定义角色并将用户分配给这些角色，这样分配到该角色的所有用户之间就可以共享权限和关联的连接。

系统预定义了一些角色：
- superadmin - 用于管理页面的角色，https://your_dbgate_instance/admin.html
- logged-user - 用于所有已登录用户的角色。您可以为特定用户覆盖权限
- anonymous-user - 用于以"匿名"身份验证方式登录的用户的角色

![角色管理 - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### 角色详情选项卡
* 信息
  * 配置角色权限
  * 配置分配到该角色的用户
* 团队文件 - 配置对[团队文件](team-files)的访问权限
* 连接 - 配置分配到该角色的连接
* 数据库 - 为该角色配置[数据库权限](permissions#database-permissions)
* 表/视图/对象 - 为该角色配置[表权限](permissions#table-permissions)
* 磁盘文件 - 配置对磁盘/docker 卷上文件的访问权限
