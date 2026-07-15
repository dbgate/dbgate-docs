---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: sk
title: Ukážky konfigurácie webovej aplikácie
weight: 30
---

Existuje množstvo konfiguračných usporiadaní, ktoré je možné dosiahnuť konfiguráciou pomocou premenných prostredia.
V tejto téme budú predstavené ukážkové konfigurácie webovej aplikácie.

## Použitie úložnej databázy a administrácie pre nastavenia (Premium)

Toto konfiguračné usporiadanie využíva administráciu na konfiguráciu databázových pripojení a používateľov. Všetky nastavenia sú uložené v databáze nakonfigurovanej pomocou premenných prostredia. Aby to fungovalo, použite prosím docker kontajner [Premium](https://hub.docker.com/r/dbgate/dbgate-premium).
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

## Viac databázových pripojení, verejný prístup (Community/Premium)
Táto konfigurácia sa používa v [demo aplikácii DbGate](https://demo.dbgate.org)
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

## Pripojenie k jednému serveru (viacero databáz), autorizácia voči DB serveru (Community/Premium)

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

## Pripojenie k jednej MS SQL databáze v režime len na čítanie, autorizácia voči Active Directory (Community/Premium)

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

## Pripojenie k MySQL serveru, autorizácia voči OAuth serveru Keycloak (Community/Premium)

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

Musíte tiež nakonfigurovať platné parametre presmerovacích URI u poskytovateľa OAuth (napr. Keycloak). Malo by ísť o základnú adresu, na ktorej beží DbGate, s koncovou lomkou (napr. "https://dbgate.test.com/")

![screenshot](/screenshots/multi-db.png)
