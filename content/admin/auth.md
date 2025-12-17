---
title: Authentication
weight: 10
---

## Authentication tab
There are several methods of authentication. Use will choose authentication method on login page. If you have only one authentication method enabled and authentication method doesn't require login page, login page is skipped.

![Authentication administration - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Local authentication method - user is selected from user list in storage database (configured in "Users" tab)
- Anonymous - no credentials are required, user have permissions from "anonymous-user" role
- Use database login - credentials are redirected to database server. User will choose connection from "Connections" tab
- OAuth 2.0 - generic OAuth provider. With some little effort and proper knowledge, could be configured with most of recent identity providers, like Google, Facebook, Keycloak
- Active Directory - AD access via LDAP protocol
- Microsoft Entra - former Azure Active Directory - single sign-on access to Azure databases

### Option "Allow only defined logins"
For external identity providers, user doesn't have to exist in DbGate storage database. If this checkbox is checked, user, which is not found in storage database, is not allowed to login

### KeyCloak

Keycloak can be integrated with DbGate using the generic OAuth 2.0 Provider. To configure Keycloak authentication, you need to:

1. Create a new client in your Keycloak realm
2. Configure the client settings
3. Set up the OAuth 2.0 provider in DbGate with the following parameters:

**Required Configuration:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: Your Keycloak client ID
- **OAuth login field**: the Keycloak claim that contains the user's login identifier (commonly `preferred_username`; depending on your Keycloak configuration you may also use `given_name`, `email`, or another suitable claim)

**Keycloak Client Configuration:**
- Valid Redirect URIs: `https://dbgate.company.com/`

Make sure your Keycloak user attributes are properly mapped to provide the necessary claims (email, name, username) that DbGate expects from the OAuth provider.


