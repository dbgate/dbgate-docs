---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: fr
title: Exemples de configuration de l'application web
weight: 30
---

Il existe de nombreuses dispositions de configuration réalisables grâce à la configuration par variables d'environnement.
Dans cette rubrique, des exemples de configurations de l'application web seront présentés.

## Utiliser une base de données de stockage et l'administration pour les paramètres (Premium)

Cette disposition de configuration utilise l'administration pour configurer les connexions aux bases de données et les utilisateurs. Tous les paramètres sont stockés dans une base de données configurée à l'aide de variables d'environnement. Veuillez utiliser le conteneur docker [Premium](https://hub.docker.com/r/dbgate/dbgate-premium) pour que cela fonctionne.
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

## Plusieurs connexions aux bases de données, accès public (Community/Premium)
Cette configuration est utilisée dans l'[application de démonstration DbGate](https://demo.dbgate.org)
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

## Connexion à un seul serveur (plusieurs bases de données), authentification auprès du serveur de base de données (Community/Premium)

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

## Connexion à une seule base de données MS SQL en mode lecture seule, authentification auprès d'Active Directory (Community/Premium)

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

## Connexion à un serveur MySQL, authentification auprès d'un serveur OAuth Keycloak (Community/Premium)

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

Vous devez également configurer des paramètres d'URI de redirection valides sur le fournisseur OAuth (par ex. Keycloak). Il doit s'agir de l'adresse de base sur laquelle DbGate s'exécute, avec une barre oblique finale (par ex. "https://dbgate.test.com/")

![screenshot](/screenshots/multi-db.png)
