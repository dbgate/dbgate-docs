---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: zh
title: 用户
weight: 30
---

## 用户选项卡
配置用户、密码、用户权限以及用户与连接的映射关系。
密码仅用于“本地”身份验证方式。但所有使用外部身份提供程序的方式都会执行用户查找，因此即使对于通过外部方式进行身份验证的用户，你也可以为其配置权限和可用的连接。

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### 用户详情选项卡
* 信息
  * 配置用户权限
  * 配置分配给该用户的角色
* 团队文件 - 配置对[团队文件](team-files)的访问权限
* 连接 - 配置分配给该用户的连接
* 数据库 - 为该用户配置[数据库权限](permissions#database-permissions)
* 表/视图/对象 - 为该用户配置[表权限](permissions#table-permissions)
* 磁盘文件 - 配置对磁盘/docker 卷上文件的访问权限
