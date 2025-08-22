---
title: Authentication
weight: 10
---

## Authentication tab
![Authentication administration - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

There are several methods of authentication. Use will choose authentication method on login page. If you have only one authentication method enabled and authentication method doesn't require login page, login page is skipped.

- Local authentication method - user is selected from user list in storage database (configured in "Users" tab)
- Anonymous - no credentials are required, user have permissions from "anonymous-user" role
- Use database login - credentials are redirected to database server. User will choose connection from "Connections" tab
- OAuth 2.0 - generic OAuth provider. With some little effort and proper knowledge, could be configured with most of recent identity providers, like Google, Facebook, Keycloak
- Active Directory - AD access via LDAP protocol
- Microsoft Entra - former Azure Active Directory - single sign-on access to Azure databases

### Option "Allow only defined logins"
For external identity providers, user doesn't have to exist in DbGate storage database. If this checkbox is checked, user, which is not found in storage database, is not allowed to login
