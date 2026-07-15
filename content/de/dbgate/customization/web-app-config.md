---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: de
title: Beispielkonfigurationen für die Web-App
weight: 30
---

Es gibt viele Konfigurationsvarianten, die sich über die Konfiguration mit Umgebungsvariablen umsetzen lassen.
In diesem Thema werden Beispielkonfigurationen der Web-App gezeigt.

## Speicherdatenbank und Administration für Einstellungen verwenden (Premium)

Diese Konfigurationsvariante nutzt die Administration zum Konfigurieren von Datenbankverbindungen und Benutzern. Alle Einstellungen werden in der Datenbank gespeichert, die über Umgebungsvariablen konfiguriert wird. Bitte verwenden Sie den [Premium](https://hub.docker.com/r/dbgate/dbgate-premium) Docker-Container, damit dies funktioniert.
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

## Mehrere Datenbankverbindungen, öffentlicher Zugriff (Community/Premium)
Diese Konfiguration wird in der [DbGate Demo-App](https://demo.dbgate.org) verwendet
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

## Einzelne Serververbindung (mehrere Datenbanken), Authentifizierung gegen den DB-Server (Community/Premium)

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

## Verbindung zu einer einzelnen MS SQL Datenbank im Readonly-Modus, Authentifizierung gegen Active Directory (Community/Premium)

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

## Verbindung zu einem MySQL-Server, Authentifizierung gegen einen OAuth Keycloak-Server (Community/Premium)

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

Sie müssen außerdem beim OAuth-Provider (z. B. Keycloak) gültige Redirect-URI-Parameter konfigurieren. Es sollte die Basisadresse sein, unter der DbGate läuft, mit abschließendem Schrägstrich (z. B. "https://dbgate.test.com/")

![screenshot](/screenshots/multi-db.png)
