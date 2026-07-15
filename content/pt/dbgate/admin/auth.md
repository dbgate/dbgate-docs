---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: pt
title: Autenticação
weight: 10
---

## Aba Authentication
Existem vários métodos de autenticação. O usuário escolherá o método de autenticação na página de login. Se você tiver apenas um método de autenticação habilitado e esse método não exigir a página de login, a página de login será ignorada.

![Administração de autenticação - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Método de autenticação local - o usuário é selecionado a partir da lista de usuários no banco de dados de armazenamento (configurado na aba "Users")
- Anonymous - nenhuma credencial é necessária, o usuário tem permissões da função "anonymous-user"
- Use database login - as credenciais são redirecionadas para o servidor de banco de dados. O usuário escolherá a conexão na aba "Connections"
- OAuth 2.0 - provedor OAuth genérico. Com um pouco de esforço e o conhecimento adequado, pode ser configurado com a maioria dos provedores de identidade recentes, como Google, Facebook, Keycloak
- Active Directory - acesso ao AD via protocolo LDAP
- Microsoft Entra - antigo Azure Active Directory - acesso com single sign-on a bancos de dados Azure

### Opção "Allow only defined logins"
Para provedores de identidade externos, o usuário não precisa existir no banco de dados de armazenamento do DbGate. Se esta caixa de seleção estiver marcada, o usuário que não for encontrado no banco de dados de armazenamento não poderá fazer login

### Keycloak

O Keycloak pode ser integrado ao DbGate usando o provedor OAuth 2.0 genérico. Para configurar a autenticação do Keycloak, você precisa:

1. Criar um novo cliente no seu realm do Keycloak
2. Configurar as definições do cliente
3. Configurar o provedor OAuth 2.0 no DbGate com os seguintes parâmetros:

**Configuração necessária:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: o ID do cliente do seu Keycloak
- **OAuth login field**: o claim do Keycloak que contém o identificador de login do usuário (geralmente `preferred_username`; dependendo da sua configuração do Keycloak, você também pode usar `given_name`, `email` ou outro claim adequado)

**Configuração do cliente Keycloak:**
- Valid Redirect URIs: `https://dbgate.company.com/`

Certifique-se de que os atributos de usuário do seu Keycloak estejam corretamente mapeados para fornecer os claims necessários (email, name, username) que o DbGate espera do provedor OAuth.


