---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: es
title: Ejemplos de configuración de la aplicación web
weight: 30
---

Existen muchos diseños de configuración que se pueden lograr mediante la configuración con variables de entorno.
En este tema se mostrarán configuraciones de ejemplo de la aplicación web.

## Usar la base de datos de almacenamiento y la administración para la configuración (Premium)

Este diseño de configuración utiliza la administración para configurar las conexiones de base de datos y los usuarios. Todos los ajustes se almacenan en la base de datos configurada con variables de entorno. Utilice el contenedor docker [Premium](https://hub.docker.com/r/dbgate/dbgate-premium) para que esto funcione.
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

## Más conexiones de base de datos, acceso público (Community/Premium)
Esta configuración se utiliza en la [aplicación de demostración de DbGate](https://demo.dbgate.org)
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

## Conexión a un solo servidor (varias bases de datos), autorización contra el servidor de base de datos (Community/Premium)

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

## Conexión a una sola base de datos MS SQL en modo de solo lectura, autorización contra Active Directory (Community/Premium)

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

## Conexión a un servidor MySQL, autorización contra un servidor OAuth Keycloak (Community/Premium)

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

También tiene que configurar los parámetros de URI de redirección válidos en el proveedor de OAuth (p. ej. Keycloak). Debe ser la dirección base en la que se ejecuta DbGate, con una barra final (p. ej. "https://dbgate.test.com/")

![screenshot](/screenshots/multi-db.png)
