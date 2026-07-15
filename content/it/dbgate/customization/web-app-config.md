---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: it
title: Esempi di configurazione dell'app web
weight: 30
---

Esistono molti schemi di configurazione, che possono essere ottenuti configurando le variabili d'ambiente.
In questo argomento verranno mostrate alcune configurazioni di esempio dell'app web.

## Utilizzo del database di archiviazione e dell'amministrazione per le impostazioni (Premium)

Questo schema di configurazione utilizza l'amministrazione per configurare le connessioni al database e gli utenti. Tutte le impostazioni sono memorizzate nel database configurato tramite le variabili d'ambiente. Per far funzionare tutto questo, usa il container docker [Premium](https://hub.docker.com/r/dbgate/dbgate-premium).
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

## Più connessioni al database, accesso pubblico (Community/Premium)
Questa configurazione è utilizzata nella [app demo di DbGate](https://demo.dbgate.org)
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

## Connessione a un singolo server (più database), autorizzazione tramite il server DB (Community/Premium)

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

## Connessione a un singolo database MS SQL in modalità di sola lettura, autorizzazione tramite Active Directory (Community/Premium)

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

## Connessione a un server MySQL, autorizzazione tramite server OAuth Keycloak (Community/Premium)

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

Devi inoltre configurare i parametri di redirect URI validi sul provider OAuth (ad es. Keycloak). Deve essere l'indirizzo base sul quale DbGate è in esecuzione, con la barra finale (ad es. "https://dbgate.test.com/")

![screenshot](/screenshots/multi-db.png)
