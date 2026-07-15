---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: cs
title: Ukázkové konfigurace webové aplikace
weight: 30
---

Existuje mnoho konfiguračních uspořádání, kterých lze dosáhnout konfigurací pomocí proměnných prostředí.
V tomto tématu budou ukázány vzorové konfigurace webové aplikace.

## Použití úložné databáze a administrace pro nastavení (Premium)

Toto konfigurační uspořádání používá administraci pro konfiguraci databázových připojení a uživatelů. Veškerá nastavení jsou uložena do databáze nakonfigurované pomocí proměnných prostředí. Aby to fungovalo, použijte prosím docker kontejner [Premium](https://hub.docker.com/r/dbgate/dbgate-premium).
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

## Více databázových připojení, veřejný přístup (Community/Premium)
Tato konfigurace je použita v [demo aplikaci DbGate](https://demo.dbgate.org)
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

## Připojení k jedinému serveru (více databází), autorizace proti databázovému serveru (Community/Premium)

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

## Připojení k jediné MS SQL databázi v režimu jen pro čtení, autorizace proti Active Directory (Community/Premium)

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

## Připojení k MySQL serveru, autorizace proti OAuth serveru Keycloak (Community/Premium)

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

Musíte také nakonfigurovat platné parametry redirect URI u poskytovatele OAuth (např. Keycloak). Mělo by to být základní adresa, na které DbGate běží, s koncovým lomítkem (např. "https://dbgate.test.com/")

![screenshot](/screenshots/multi-db.png)
