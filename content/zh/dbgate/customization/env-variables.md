---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: zh
title: 环境变量
weight: 20
---

通过环境变量进行配置可用于 docker 容器，也可用于 npm 包。NPM 包支持 .env 文件。
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - Community 版的 NPM 包
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - Premium 版的 NPM 包
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - Community 版的 Docker 镜像
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - Premium 版的 Docker 镜像

## Premium 版与 Team Community 版对比
Community（FOSS）版仅使用下列环境变量中的配置。Team Premium 版使用数据库存储设置，并配备[管理界面](/zh/features/administration)，只有少数基本设置通过环境变量配置。

## Team Premium 版配置
这些变量仅在 Team Premium 版中可用。
  * STORAGE_SERVER - 存储数据库的数据库服务器（主机名）
  * STORAGE_USER - 数据库用户
  * STORAGE_PASSWORD - 数据库密码
  * STORAGE_PORT - 数据库端口（可选。如果省略，则使用所选数据库引擎的默认端口）
  * STORAGE_DATABASE - 存储数据库名称
  * STORAGE_SCHEMA - 存储数据库架构（可选，例如用于 PostgreSQL（通常为 public）或 MS SQL（通常为 dbo））
  * STORAGE_ENGINE - 用于存储数据库的引擎。目前支持 MySQL、PostgreSQL、SQL Server 和 Oracle。请使用以下值之一：
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - 管理员密码。管理界面可通过 URL https://dbgate_url/admin.html 访问。如果未定义密码且已定义 STORAGE_DATABASE，DbGate 将在首次启动时询问管理员密码。
  * DBGATE_LICENSE - DbGate 的许可证密钥。如需试用许可证，请联系 sales@dbgate.eu。如果未定义，DbGate Premium 将在首次启动时询问许可证。DbGate Community 不需要任何许可证。
  
### 存储的其他连接参数
  * STORAGE_SOCKET_PATH - 存储连接的 socket 路径
  * STORAGE_DATABASE_URL - 存储连接的数据库 URL
  * STORAGE_AUTH_TYPE - 存储连接的认证类型。取值与 AUTH_TYPE_xxx 变量相同
  * STORAGE_USE_SSL - 当应使用 SSL 时，设置值为 1 或 true
  * STORAGE_KEY_FILE - 密钥文件路径
  * STORAGE_KEY_FILE_PASSWORD - 密钥文件口令
  * STORAGE_SSL_CA_FILE - CA 证书文件路径
  * STORAGE_SSL_CERT_FILE - 证书文件路径
  * STORAGE_SSL_CERT_FILE_PASSWORD - 证书密钥文件密码
  * STORAGE_SSL_KEY_FILE - 密钥文件路径
  * STORAGE_SSL_KEY_FILE_PASSWORD - 密钥文件口令
  * STORAGE_SSL_REJECT_UNAUTHORIZED - 如果拒绝未经授权的连接，设置值为 1 或 true
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - 设置值为 1 或 true 以启用 MSSQL 的 trustServerCertificate 选项

以下变量在 Community 版和 Premium 版中均可用。但在 Premium 版中，推荐的方式是使用存储数据库并通过管理界面进行配置。

## Web 与权限配置
* WEB_ROOT - 如果需要在虚拟子目录中运行 DbGate（例如值为 /dbadmin 时，dbgate 将可通过 localhost:3000/dbadmin 访问）
* LOGIN , PASSWORD - 访问 Web 应用的凭据
* PERMISSIONS - 逗号分隔的权限列表。另请参阅下方的权限列表
* SHELL_CONNECTION - 如果为 true 或 1，则可以在 shell 脚本中定义连接。否则，仅允许预配置的连接。出于安全原因，默认不允许此项。请注意，启用后加密的密码会被发送到前端。
* SHELL_SCRIPTING - 如果为 true 或 1，则允许自定义 JavaScript shell 脚本。出于安全原因，默认不允许此项。
* LOGIN_PASSWORD_[login] - 指定登录名的密码
* LOGIN_PERMISSIONS_[login] - 给定登录名的逗号分隔权限列表。另请参阅下方的权限列表
* TOKEN_LIFETIME - 访问令牌的有效期。超过此时间后，已登录用户将被重定向到登录页面。默认值为 1d（表示 1 天）。可能的值如 3h（3 小时）、10m（10 分钟）、2d（2 天）
* SINGLE_CONNECTION - 连接 ID。如果已定义，则仅此连接可用（必须与 SINGLE_DATABASE 一起使用）
* SINGLE_DATABASE - 数据库名称，仅此数据库可用。（必须与 SINGLE_CONNECTION 一起使用）
* BASIC_AUTH - 如果为 true 或 1，则 Web 和 API 均使用基本认证。否则，使用登录表单和基于 JWT 令牌的 API 认证。基本认证不能用于 OAuth 认证。
* SKIP_ALL_AUTH - 如果为 true 或 1，则跳过所有认证
* ALLOW_DBGATE_PRIVATE_CLOUD - 默认情况下，DbGate cloud 在 Web 版中被禁用。使用此变量可以启用它
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - 在 Web 版中，重定向到 DbGate cloud 登录页面，而不是打开新窗口
* LANGUAGE - 界面语言，例如 en、cs、de、fr 等。请参阅下方的语言配置表。设置为 "auto" 可使用浏览器语言

## 语言配置
| 语言 | 值 |
|----------|-------|
| 英语 | en |
| 德语 | de |
| 西班牙语 | es |
| 法语 | fr |
| 意大利语 | it |
| 葡萄牙语（巴西） | pt |
| 日语 | ja |
| 中文 - 简体 | zh |
| 捷克语 | cs |
| 斯洛伐克语 | sk |


## 日志配置
* LOG_LEVEL - 所有达到或高于此日志级别的消息都将被记录。取值为 trace、debug、info、warn、error、fatal 之一。默认为 info
* FILE_LOG_LEVEL - 记录到日志文件的日志级别。对于文件日志记录，此项优先级高于 LOG_LEVEL
* CONSOLE_LOG_LEVEL - 记录到日志文件的日志级别。对于控制台日志记录，此项优先级高于 LOG_LEVEL

## OAuth 配置（仅限 Web 版）
* OAUTH_AUTH - OAuth 协议的认证端点
* OAUTH_TOKEN - OAuth 协议的令牌端点
* OAUTH_LOGOUT - OAuth 提供程序的注销 URL。当用户请求注销时，将被重定向到此 URL
* OAUTH_CLIENT_ID - 客户端 ID
* OAUTH_CLIENT_SECRET - 客户端密钥
* OAUTH_LOGIN_FIELD - 载荷中保存登录名的字段名。要查看可用字段，您可以检查 dbgate 日志，OAuth 提供程序发送的载荷会记录到控制台。此登录名用于例如配置权限。它不一定是在 OAuth 中输入的登录名。如果未指定，来自 OAuth 提供程序的所有用户将拥有相同的登录名。
* OAUTH_ALLOWED_LOGINS - 逗号分隔的登录名，这些登录名将被允许登录。如果未指定，则所有登录名都将被允许使用 DbGate 应用。
* OAUTH_SCOPE - 发送到 OAuth 授权和令牌端点的 scope
* OAUTH_GROUP_FIELD - OAuth 载荷中表示组的字段
* OAUTH_ALLOWED_GROUPS - 逗号分隔的允许组名

## Active directory/LDAP 配置（仅限 Web 版）
* AD_URL - LDAP 提供程序的 URL（例如 ldap://domain.com）
* AD_BASEDN - 例如 dc=domain,dc=com
* AD_USERNAME - Active Directory 的用户名
* AD_PASSWORD - Active Directory 的密码
* AD_ALLOWED_LOGINS - 逗号分隔的登录名，这些登录名将被允许登录。如果未指定，则所有登录名都将被允许使用 DbGate 应用。

## Oracle 客户端配置  
* ORACLE_INSTANT_CLIENT - [Oracle instant client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html) 的路径

## 连接配置
您可以使用环境变量配置连接列表，此时"添加连接"和"编辑连接"命令将不可用。

* CONNECTIONS - 逗号分隔的预配置连接名称列表。在以下选项中，[connection id] 是此列表中的 ID
* LABEL_[connection id] - 连接的标签（显示名称）。
* SERVER_[connection id] - 连接的服务器（主机名）。
* USER_[connection id] - 数据库连接的用户名。
* PASSWORD_[connection id] - 数据库连接的密码。
* PASSWORD_MODE_[connection id] - 确定用户名和密码是被存储还是必须由用户填写。为以下值之一：
  * askPassword - DbGate 在连接时询问密码
  * askUser - DbGate 询问用户名和密码
* PORT_[connection id] - 数据库连接的端口。
* FILE_[connection id] - 数据库文件路径（适用于 SQLite）。
* URL_[connection id] - 数据库 URL（适用于 MongoDB、PostgreSQL、CockroachDb、Redshift、Oracle）。
* SERVICE_NAME_[connection id] - Oracle 服务名。
* DATABASE_[connection id] - 默认数据库名称。
* READONLY_[connection id] - 以只读模式连接
* ENGINE_[connection id] - 连接的引擎（**必填**，引擎名称及插件），为以下之一：
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - 当应使用 SSH 隧道时，设置值为 1 或 true
* SSH_HOST_[connection id] - SSH 主机名
* SSH_PORT_[connection id] - SSH 端口号
* SSH_MODE_[connection id] - 为以下值之一
  * userPassword - 使用用户名和密码认证
  * agent - 使用 SSH agent 认证
  * keyFile - 使用密钥文件认证
* SSH_LOGIN_[connection id] - SSH 登录名
* SSH_PASSWORD_[connection id] - SSH 密码
* SSH_KEY_FILE_[connection id] - 密钥文件的完整路径
* SSH_KEY_FILE_PASSWORD_[connection id] - 密钥文件口令
* USE_SSL_[connection id] - 当应使用 SSL 时，设置值为 1 或 true
* SSL_CA_FILE_[connection id] - CA 证书文件路径
* SSL_CERT_FILE_[connection id] - 证书文件路径
* SSL_CERT_FILE_PASSWORD_[connection id] - 证书密钥文件密码
* SSL_KEY_FILE_[connection id] - 密钥文件路径
* SSL_REJECT_UNAUTHORIZED_[connection id] - 如果拒绝未经授权的连接，设置值为 1 或 true
* SSL_TRUST_CERTIFICATE_[connection id] - 设置值为 1 或 true 以启用 MSSQL 的 trustServerCertificate 选项
* SETTINGS_[settings key] - 预配置设置值。设置键可以从源代码中查找，https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - socket 文件路径，如果通过 socket 连接
* AUTH_TYPE_[connection id] - 认证类型
  * hostPort（默认）
  * socket - 设置 SOCKET_PATH 时会隐式设置此值
  * tedious - MS SQL 的默认可移植认证，使用 tedious 驱动程序
  * sspi - Windows 集成认证（仅限 Windows，MS SQL），使用原生 MSSQL 驱动程序
  * sql - SQL 认证（仅限 Windows，MS SQL），使用原生 MSSQL 驱动程序
* ALLOWED_DATABASES_[connection id] - 指定连接允许的数据库名称，以竖线（"|"）分隔
* ALLOWED_DATABASES_REGEX_[connection id] - 指定连接允许的数据库名称的正则表达式
* USE_SEPARATE_SCHEMAS_[connection id] - 设置值为 1 或 true 以单独加载架构。如果您的架构较大，请使用此项。
* LOCAL_DATA_CENTER_[connection id] - 本地数据中心（适用于 Apache Cassandra）
* CONNECTION_[connection id]_parameterName - 设置引擎特定的参数名

SettingsModal.svelte，查找字符串 "name="/ 如果需要定义 "true"，请使用值 "1"。如果需要 "false"，请使用空字符串（"0" 无效）

## 角色配置
此配置仅可在 Team Premium 版中使用，且需使用存储数据库来保存设置。环境变量中的角色会在 docker 容器启动时导入存储数据库。
您可以定义具有特定权限的角色，并将连接分配给该角色。将角色分配给用户是在管理界面中完成的。
* `ROLE_[role_name]_PERMISSIONS` - 给定角色的逗号分隔权限列表。请参阅下方的权限列表
* `ROLE_[role_name]_CONNECTIONS` - 分配给给定角色的逗号分隔连接 ID 列表
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - 具有给定 ID 的数据库权限的连接 ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - 具有给定 ID 的数据库权限的数据库名称列表，以竖线（"|"）分隔
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - 具有给定 ID 的数据库权限的数据库名称正则表达式
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - 为以下之一：deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - 具有给定 ID 的表权限的连接 ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - 具有给定 ID 的数据库权限的数据库名称列表，以竖线（"|"）分隔
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - 具有给定 ID 的数据库权限的数据库名称正则表达式
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - 具有给定 ID 的表权限的架构名称列表，以竖线（"|"）分隔
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - 具有给定 ID 的表权限的架构名称正则表达式
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - 具有给定 ID 的数据库权限的表名称列表，以竖线（"|"）分隔
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - 具有给定 ID 的数据库权限的表名称正则表达式
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - 为以下之一：deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - 为以下之一：collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## 权限
默认情况下，所有权限均可用。如果使用 \~ 前缀，则撤销该权限。

### 示例
* ~*, widgets/database - 撤销所有权限，仅数据库小部件可见
* ~widgets/*, widgets/database - 撤销所有小部件权限，仅数据库小部件可见
* ~connections/*, connections/con1 - 除 con1 之外的所有连接都被隐藏和禁用

### 权限列表
* settings/change - 允许更改设置
* plugins/install - 允许安装插件
* widgets/[widget_name] - 如果未授予，则小部件被隐藏。小部件是左侧的条带。可用的小部件：
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - 从给定文件夹读取文件
* files/[folder]/write - 向给定文件夹写入文件
* apps/write - 保存到 apps 内容
* archive/write - 保存到 archive 内容
* connections/[connection_id] - 允许查看和使用已定义的连接
* internal-storage = 访问内部存储（Premium）
* admin/auth - 管理 - 认证选项卡（Premium）
* admin/connections - 管理 - 连接选项卡（Premium）
* admin/users - 管理 - 用户选项卡（Premium）
* admin/roles - 管理 - 角色选项卡（Premium）
* dbops/sql-template/* - SQL 模板（例如 SQL: CREATE TABLE、SQL: SELECT）
* dbops/sql-generator - SQL 生成器
* dbops/sql-dump/import - 导入 SQL 转储
* dbops/sql-dump/export - 导出 SQL 转储
* dbops/query - 运行 SQL 查询
* dbops/import - 导入数据
* dbops/export - 导出数据
* dbops/charts - 查看图表
* dbops/profiler - 数据库分析器
* dbops/createdb - 创建数据库
* dbops/dropdb - 删除数据库
* dbops/model/view - 查看数据库模型（图表、JSON）
* dbops/model/edit - 编辑数据库模型（创建/更改表、视图等）
* dbops/model/compare - 比较数据库模型
* dbops/table/rename - 重命名表
* dbops/table/truncate - 清空表
* dbops/table/backup - 创建表备份

