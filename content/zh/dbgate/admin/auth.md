---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: zh
title: 身份验证
weight: 10
---

## 身份验证选项卡
有多种身份验证方法。用户将在登录页面上选择身份验证方法。如果您只启用了一种身份验证方法，并且该方法不需要登录页面，则会跳过登录页面。

![Authentication administration - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- 本地身份验证方法 - 从存储数据库中的用户列表中选择用户（在"Users"选项卡中配置）
- 匿名 - 不需要任何凭据，用户拥有"anonymous-user"角色的权限
- 使用数据库登录 - 凭据被重定向到数据库服务器。用户将从"Connections"选项卡中选择连接
- OAuth 2.0 - 通用 OAuth 提供程序。只需少量配置和适当的知识，即可与大多数较新的身份提供程序集成，例如 Google、Facebook、Keycloak
- Active Directory - 通过 LDAP 协议访问 AD
- Microsoft Entra - 前身为 Azure Active Directory - 对 Azure 数据库的单点登录访问

### 选项"仅允许已定义的登录名"
对于外部身份提供程序，用户不必存在于 DbGate 存储数据库中。如果选中此复选框，则在存储数据库中找不到的用户将不允许登录

### Keycloak

Keycloak 可以使用通用 OAuth 2.0 提供程序与 DbGate 集成。要配置 Keycloak 身份验证，您需要：

1. 在您的 Keycloak realm 中创建一个新客户端
2. 配置客户端设置
3. 使用以下参数在 DbGate 中设置 OAuth 2.0 提供程序：

**必需的配置：**
- **OAuth auth endpoint**：`https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**：`https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**：`https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**：您的 Keycloak 客户端 ID
- **OAuth login field**：包含用户登录标识符的 Keycloak claim（通常为 `preferred_username`；根据您的 Keycloak 配置，您也可以使用 `given_name`、`email` 或其他合适的 claim）

**Keycloak 客户端配置：**
- 有效重定向 URI：`https://dbgate.company.com/`

请确保您的 Keycloak 用户属性已正确映射，以提供 DbGate 期望从 OAuth 提供程序获得的必要 claim（email、name、username）。


