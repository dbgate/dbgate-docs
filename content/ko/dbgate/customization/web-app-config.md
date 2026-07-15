---
sourceHash: 7478378fe369b54890faf5cc471d7eeb59a4aba2fcccc6b90bc8c6413160b83b
language: ko
title: 웹 앱 설정 예제
weight: 30
---

환경 변수 설정으로 구성할 수 있는 다양한 설정 레이아웃이 있습니다.
이 문서에서는 웹 앱의 설정 예제를 소개합니다.

## 설정에 스토리지 데이터베이스와 관리 기능 사용하기 (Premium)

이 설정 레이아웃은 데이터베이스 연결과 사용자를 구성하기 위해 관리 기능을 사용합니다. 모든 설정은 환경 변수로 구성된 데이터베이스에 저장됩니다. 이 기능을 사용하려면 [Premium](https://hub.docker.com/r/dbgate/dbgate-premium) 도커 컨테이너를 사용하세요.
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

## 여러 데이터베이스 연결, 공개 접근 (Community/Premium)
이 설정은 [DbGate 데모 앱](https://demo.dbgate.org)에서 사용됩니다.
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

## 단일 서버 연결(여러 데이터베이스), DB 서버를 통한 인증 (Community/Premium)

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

## 읽기 전용 모드로 단일 MS SQL 데이터베이스에 연결, Active Directory를 통한 인증 (Community/Premium)

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

## MySQL 서버에 연결, OAuth Keycloak 서버를 통한 인증 (Community/Premium)

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

또한 OAuth 공급자(예: Keycloak)에서 유효한 리디렉션 URI 매개변수를 구성해야 합니다. 이 값은 DbGate가 실행 중인 기본 주소에 슬래시를 붙인 형태여야 합니다(예: "https://dbgate.test.com/").

![screenshot](/screenshots/multi-db.png)
