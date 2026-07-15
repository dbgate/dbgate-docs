---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: zh
title: Docker 上的 Team Premium
weight: 30
---

典型的 Team Premium 安装由两个组件构成：
- DbGate 服务器 docker 容器
- 数据库服务器（MS SQL、MySQL、PostgreSQL、Oracle）—— 用于存储连接、用户和角色的内部存储数据库。您可以使用现有的数据库服务器，也可以安装新的数据库服务器。

## DbGate 服务器 Docker 容器
使用 Docker Hub 上的 [DbGate Team Premium 镜像](https://hub.docker.com/r/dbgate/dbgate-premium)：
```
docker pull dbgate/dbgate-premium
```

DbGate Team Premium 容器需要设置一些环境变量：
- `STORAGE_SERVER`、`STORAGE_DATABASE`、`STORAGE_USER`、`STORAGE_PASSWORD`、`STORAGE_ENGINE` —— 定义到内部存储数据库的连接

有关可用环境变量的更多详细信息，请参阅[环境变量文档](/zh/dbgate/customization/env-variables/#team-premium-edition-configuration)。

## 资源要求

实际上，DbGate Team Premium 的资源消耗非常低，但为了获得最佳性能，我们推荐以下配置（针对 10 个并发用户）：
- 2 个 CPU 核心
- 4 GB 内存（包含 MySQL 或 PostgreSQL 内部存储数据库的内存消耗）
- 10 GB 可用磁盘空间（用于 docker 安装、存储数据库、临时文件、查询结果等。实际磁盘空间消耗取决于使用模式）

对于用户数量较少的情况，您可以使用更低的资源限制（1 GB 内存、1 个 CPU 核心）。  
当您需要为小型安装最小化资源消耗时，我们建议使用 MySQL/MariaDB 作为内部存储。  

## 配置 docker

如果您想使用磁盘文件来存储用户文件（例如查询结果导出），应该映射容器中的 `/root/.dbgate` 路径。

下面是一个示例 `docker-compose.yml` 文件，定义了以 PostgreSQL 作为内部存储数据库的 DbGate Team Premium 容器。
- 您可以定义 `DBGATE_LICENSE` 环境变量来设置许可证密钥。如果未设置，DbGate 将在首次启动时要求输入许可证密钥。
-  您可以定义 'ADMIN_PASSWORD' 环境变量来设置管理员用户密码。如果未设置，DbGate 将在首次启动时要求输入管理员密码。

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## 无状态/有状态
DbGate 容器是有状态的。

以下数据存储在容器内部：
* 已登录的用户会话
* 查询执行状态
* 临时文件（例如结果）
* 已打开的数据库事务
* 已打开的数据库连接

无法在负载均衡器后面正确运行多个 DbGate 容器，因为上述数据不会在容器之间共享。

## 来自 NPM 的 DbGate 服务器
如果您的基础设施不支持 Docker，您可以使用 [DbGate Team Premium NPM 包](https://www.npmjs.com/package/dbgate-serve-premium)：
```
npm install -g dbgate-serve-premium
```
 
## 进程隔离
DbGate Team Premium 在数据库连接级别使用进程隔离，因此多个用户可以使用同一个数据库服务器而不会相互干扰。从 DbGate 派生的进程会随着活动用户和连接数量的增加而增长，因此请确保您的服务器有足够的资源。
以下实体会被隔离到新进程中：
* 服务器连接
* 数据库连接
* 查询会话
* 导出/导入作业执行
* SSH 隧道
