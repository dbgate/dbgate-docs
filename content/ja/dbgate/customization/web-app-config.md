---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: ja
title: Web アプリ設定のサンプル
weight: 30
---

環境変数による設定で実現できる構成のパターンは数多くあります。
このトピックでは、Web アプリのサンプル設定を紹介します。

## ストレージデータベースと管理機能を設定に使用する (Premium)

この構成パターンでは、データベース接続とユーザーの設定に管理機能を使用します。すべての設定は環境変数で構成したデータベースに保存されます。これを利用するには [Premium](https://hub.docker.com/r/dbgate/dbgate-premium) の docker コンテナーを使用してください。
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

## 複数のデータベース接続、パブリックアクセス (Community/Premium)
この設定は [DbGate デモアプリ](https://demo.dbgate.org) で使用されています
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

## 単一サーバー接続 (複数データベース)、DB サーバーに対して認証する (Community/Premium)

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

## 単一の MS SQL データベースへの読み取り専用モードでの接続、Active Directory に対して認証する (Community/Premium)

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

## MySQL サーバーへの接続、OAuth Keycloak サーバーに対して認証する (Community/Premium)

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

また、OAuth プロバイダー (例: Keycloak) 側で有効なリダイレクト URI パラメーターを設定する必要があります。DbGate が動作しているベースアドレスに末尾のスラッシュを付けたもの (例: "https://dbgate.test.com/") を指定してください。

![screenshot](/screenshots/multi-db.png)
