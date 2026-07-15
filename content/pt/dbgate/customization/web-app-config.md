---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: pt
title: Exemplos de configuração do aplicativo web
weight: 30
---

Existem muitos layouts de configuração que podem ser obtidos por meio da configuração de variáveis de ambiente.
Neste tópico, serão apresentadas configurações de exemplo do aplicativo web.

## Usar banco de dados de armazenamento e administração para as configurações (Premium)

Este layout de configuração usa a administração para configurar conexões de banco de dados e usuários. Todas as configurações são armazenadas no banco de dados definido pelas variáveis de ambiente. Utilize o contêiner docker [Premium](https://hub.docker.com/r/dbgate/dbgate-premium) para que isso funcione.
```
STORAGE_SERVER: mariadb
STORAGE_USER: root
STORAGE_PASSWORD: <Your password into database>
STORAGE_PORT: 3306
STORAGE_DATABASE: dbgate
STORAGE_ENGINE: mysql@dbgate-plugin-mysql
ADMIN_PASSWORD: <Admin password>
```

![screenshot](/screenshots/authentication-administration.png)

## Mais conexões de banco de dados, acesso público (Community/Premium)
Esta configuração é usada no [aplicativo de demonstração do DbGate](https://demo.dbgate.org)
```
CONNECTIONS=mysql,postgres

LABEL_mysql=MySql localhost
SERVER_mysql=localhost
USER_mysql=root
PASSWORD_mysql=test
PORT_mysql=3306
ENGINE_mysql=mysql@dbgate-plugin-mysql

LABEL_postgres=Postgres localhost
SERVER_postgres=localhost
USER_postgres=postgres
PASSWORD_postgres=test
PORT_postgres=5432
ENGINE_postgres=postgres@dbgate-plugin-postgres
```

![screenshot](/screenshots/multi-db.png)

## Conexão a um único servidor (vários bancos de dados), autorização no servidor de banco de dados (Community/Premium)

```
CONNECTIONS=mysql
SINGLE_CONNECTION=mysql
LABEL_mysql=MySql localhost
SERVER_mysql=localhost
PORT_mysql=3306
ENGINE_mysql=mysql@dbgate-plugin-mysql
PASSWORD_MODE_mysql=askUser
```

![screenshot](/screenshots/db-login.png)

## Conexão a um único banco de dados MS SQL em modo somente leitura, autorização no Active Directory (Community/Premium)

```
AD_URL=ldap://company.com
AD_BASEDN=dc=company,dc=com
AD_USERNAME=company\\ldap-user
AD_PASSWORD=xxxx

CONNECTIONS=mssql

SINGLE_CONNECTION=mssql
SINGLE_DATABASE=Chinook

LABEL_mssql=MsSql localhost
SERVER_mssql=localhost
USER_mssql=sa
PASSWORD_mssql=xxxx
READONLY_mssql=1

```

![screenshot](/screenshots/single-db.png)

## Conexão a um servidor MySQL, autorização em um servidor OAuth Keycloak (Community/Premium)

```
CONNECTIONS=mysql
SINGLE_CONNECTION=mysql
LABEL_mysql=MySql localhost
SERVER_mysql=localhost
PORT_mysql=3306
ENGINE_mysql=mysql@dbgate-plugin-mysql
USER_mysql=root
PASSWORD_mysql=test

OAUTH_AUTH=https://keycloak.company.com/realms/dbgate/protocol/openid-connect/auth
OAUTH_TOKEN=https://keycloak.company.com/realms/dbgate/protocol/openid-connect/token
OAUTH_LOGOUT=https://keycloak.company.com/realms/dbgate/protocol/openid-connect/logout
OAUTH_CLIENT_ID=dbgate
OAUTH_CLIENT_SECRET=xxxx
OAUTH_LOGIN_FIELD=given_name
OAUTH_SCOPE=email

```

Você também precisa configurar os parâmetros de URI de redirecionamento válidos no provedor OAuth (por exemplo, Keycloak). Deve ser o endereço base no qual o DbGate está sendo executado, com barra no final (por exemplo, "https://dbgate.test.com/")

![screenshot](/screenshots/multi-db.png)
