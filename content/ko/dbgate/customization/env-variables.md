---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: ko
title: 환경 변수
weight: 20
---

환경 변수를 통한 설정은 docker 컨테이너에서 사용할 수 있으며, npm 패키지를 사용할 때도 사용할 수 있습니다. NPM 패키지는 .env 파일을 지원합니다.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - Community 에디션용 NPM 패키지
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - Premium 에디션용 NPM 패키지
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - Community 에디션용 Docker 이미지
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - Premium 에디션용 Docker 이미지

## Premium 에디션과 Team Community 에디션 비교
Community(FOSS) 에디션은 아래에 나열된 환경 변수의 설정만 사용합니다. Team Premium 에디션은 [관리 UI](/ko/features/administration)와 함께 설정을 위한 데이터베이스 저장소를 사용하며, 몇 가지 기본 설정만 환경 변수로 구성됩니다.

## Team Premium 에디션 설정
이 변수들은 Team Premium 에디션에서만 사용할 수 있습니다.
  * STORAGE_SERVER - 저장소 데이터베이스의 데이터베이스 서버(호스트 이름)
  * STORAGE_USER - 데이터베이스 사용자
  * STORAGE_PASSWORD - 데이터베이스 비밀번호
  * STORAGE_PORT - 데이터베이스 포트(선택 사항. 생략하면 선택한 데이터베이스 엔진의 기본 포트가 사용됩니다)
  * STORAGE_DATABASE - 저장소 데이터베이스 이름
  * STORAGE_SCHEMA - 저장소 데이터베이스 스키마(선택 사항, 예: PostgreSQL(일반적으로 public) 또는 MS SQL(일반적으로 dbo))
  * STORAGE_ENGINE - 저장소 데이터베이스에 사용되는 엔진. 현재는 MySQL, PostgreSQL, SQL Server 및 Oracle을 지원합니다. 다음 값 중 하나를 사용하세요:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - 관리자 비밀번호. 관리 기능은 https://dbgate_url/admin.html URL에서 사용할 수 있습니다. 비밀번호가 정의되지 않고 STORAGE_DATABASE가 정의된 경우, DbGate는 처음에 관리자 비밀번호를 묻습니다.
  * DBGATE_LICENSE - DbGate 라이선스 키. 평가판 라이선스는 sales@dbgate.eu로 문의하세요. 정의되지 않은 경우 DbGate Premium은 처음에 라이선스를 묻습니다. DbGate Community는 라이선스가 필요하지 않습니다.
  
### 저장소의 추가 연결 매개변수
  * STORAGE_SOCKET_PATH - 저장소 연결의 소켓 경로
  * STORAGE_DATABASE_URL - 저장소 연결의 데이터베이스 URL
  * STORAGE_AUTH_TYPE - 저장소 연결의 인증 유형. 값은 AUTH_TYPE_xxx 변수와 동일합니다
  * STORAGE_USE_SSL - SSL을 사용해야 하는 경우 값 1 또는 true로 설정
  * STORAGE_KEY_FILE - 키 파일 경로
  * STORAGE_KEY_FILE_PASSWORD - 키 파일 암호
  * STORAGE_SSL_CA_FILE - CA 인증서 파일 경로
  * STORAGE_SSL_CERT_FILE - 인증서 파일 경로
  * STORAGE_SSL_CERT_FILE_PASSWORD - 인증서 키 파일 비밀번호
  * STORAGE_SSL_KEY_FILE - 키 파일 경로
  * STORAGE_SSL_KEY_FILE_PASSWORD - 키 파일 암호
  * STORAGE_SSL_REJECT_UNAUTHORIZED - 승인되지 않은 연결을 거부하려면 값 1 또는 true로 설정
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - MSSQL의 trustServerCertificate 옵션을 설정하려면 값 1 또는 true로 설정

다음 변수들은 Community 및 Premium 에디션 모두에서 사용할 수 있습니다. 다만 Premium 에디션에서는 저장소 데이터베이스를 사용하고 관리 UI로 설정하는 것이 권장되는 방법입니다.

## 웹 및 권한 설정
* WEB_ROOT - DbGate를 가상 하위 디렉터리에서 실행해야 하는 경우(예: 값이 /dbadmin 이면 dbgate는 localhost:3000/dbadmin 에서 접근할 수 있습니다)
* LOGIN , PASSWORD - 웹 앱 접근을 위한 자격 증명
* PERMISSIONS - 쉼표로 구분된 권한 목록. 아래 권한 목록도 참조하세요
* SHELL_CONNECTION - true 또는 1이면 셸 스크립트에서 연결을 정의할 수 있습니다. 그렇지 않으면 미리 구성된 연결만 허용됩니다. 기본적으로 보안상의 이유로 허용되지 않습니다. 허용하는 경우 암호화된 비밀번호가 프런트엔드로 전송된다는 점에 유의하세요.
* SHELL_SCRIPTING - true 또는 1이면 사용자 정의 JavaScript 셸 스크립트가 허용됩니다. 기본적으로 보안상의 이유로 허용되지 않습니다.
* LOGIN_PASSWORD_[login] - 지정된 로그인의 비밀번호
* LOGIN_PERMISSIONS_[login] - 지정된 로그인에 대한 쉼표로 구분된 권한 목록. 아래 권한 목록도 참조하세요
* TOKEN_LIFETIME - 액세스 토큰의 수명. 이 시간이 지나면 로그인한 사용자는 로그인 페이지로 리디렉션됩니다. 기본값은 1d(1일을 의미)입니다. 3h(3시간), 10m(10분), 2d(2일)과 같은 값을 사용할 수 있습니다
* SINGLE_CONNECTION - 연결 ID. 정의된 경우 이 연결만 사용할 수 있습니다(SINGLE_DATABASE와 함께 사용해야 함)
* SINGLE_DATABASE - 데이터베이스 이름, 이 데이터베이스만 사용할 수 있습니다. (SINGLE_CONNECTION과 함께 사용해야 함)
* BASIC_AUTH - true 또는 1이면 웹과 API 모두에 기본 인증이 사용됩니다. 그렇지 않으면 로그인 폼과 JWT 토큰 기반 API 인증이 사용됩니다. 기본 인증은 OAuth 인증에는 사용할 수 없습니다.
* SKIP_ALL_AUTH - true 또는 1이면 모든 인증을 건너뜁니다
* ALLOW_DBGATE_PRIVATE_CLOUD - 기본적으로 DbGate cloud는 웹 버전에서 비활성화되어 있습니다. 이 변수를 사용하여 활성화할 수 있습니다
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - 웹 버전에서 새 창을 여는 대신 DbGate cloud 로그인으로 리디렉션합니다
* LANGUAGE - UI 언어, 예: en, cs, de, fr 등. 아래 언어 설정 표를 참조하세요. 브라우저 언어를 사용하려면 "auto"로 설정하세요

## 언어 설정
| 언어 | 값 |
|----------|-------|
| 영어 | en |
| 독일어 | de |
| 스페인어 | es |
| 프랑스어 | fr |
| 이탈리아어 | it |
| 포르투갈어(브라질) | pt |
| 일본어 | ja |
| 중국어 - 간체 | zh |
| 체코어 | cs |
| 슬로바키아어 | sk |


## 로깅 설정
* LOG_LEVEL - 이 로그 레벨 이상의 모든 메시지가 기록됩니다. trace, debug, info, warn, error, fatal 중 하나의 값. 기본값은 info입니다
* FILE_LOG_LEVEL - 로그 파일에 기록하기 위한 로그 레벨. 파일 로깅의 경우 이 값이 LOG_LEVEL보다 우선순위가 높습니다
* CONSOLE_LOG_LEVEL - 로그 파일에 기록하기 위한 로그 레벨. 콘솔 로깅의 경우 이 값이 LOG_LEVEL보다 우선순위가 높습니다

## OAuth 설정(웹 버전 전용)
* OAUTH_AUTH - OAuth 프로토콜의 인증 엔드포인트
* OAUTH_TOKEN - OAuth 프로토콜의 토큰 엔드포인트
* OAUTH_LOGOUT - OAuth 공급자의 로그아웃 URL. 사용자가 로그아웃을 요청하면 이 URL로 리디렉션됩니다
* OAUTH_CLIENT_ID - 클라이언트 ID
* OAUTH_CLIENT_SECRET - 클라이언트 시크릿
* OAUTH_LOGIN_FIELD - 로그인 이름을 담고 있는 페이로드의 필드 이름. 사용 가능한 필드는 dbgate 로그를 확인하면 됩니다. OAuth 공급자가 보낸 페이로드는 콘솔에 기록됩니다. 이 로그인 이름은 예를 들어 권한 설정에 사용됩니다. 반드시 OAuth에서 입력한 로그인일 필요는 없습니다. 지정하지 않으면 OAuth 공급자의 모든 사용자가 동일한 로그인 이름을 갖게 됩니다.
* OAUTH_ALLOWED_LOGINS - 로그인이 허용될 쉼표로 구분된 로그인 이름. 지정하지 않으면 모든 로그인이 DbGate 앱을 사용할 수 있습니다.
* OAUTH_SCOPE - OAuth 인가 및 토큰 엔드포인트로 전송되는 scope
* OAUTH_GROUP_FIELD - 그룹을 나타내는 OAuth 페이로드의 필드
* OAUTH_ALLOWED_GROUPS - 쉼표로 구분된 허용 그룹 이름

## Active directory/LDAP 설정(웹 버전 전용)
* AD_URL - LDAP 공급자의 URL(예: ldap://domain.com)
* AD_BASEDN - 예: dc=domain,dc=com
* AD_USERNAME - active directory 사용자 이름
* AD_PASSWORD - active directory 비밀번호
* AD_ALLOWED_LOGINS - 로그인이 허용될 쉼표로 구분된 로그인 이름. 지정하지 않으면 모든 로그인이 DbGate 앱을 사용할 수 있습니다.

## Oracle 클라이언트 설정  
* ORACLE_INSTANT_CLIENT - [Oracle instant client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html) 경로

## 연결 설정
환경 변수로 연결 목록을 구성할 수 있으며, 그러면 "연결 추가" 및 "연결 편집" 명령을 사용할 수 없게 됩니다.

* CONNECTIONS - 쉼표로 구분된 미리 구성된 연결 이름 목록. 다음 옵션들에서 [connection id]는 이 목록의 ID입니다
* LABEL_[connection id] - 연결의 레이블(표시 이름). 
* SERVER_[connection id] - 연결의 서버(호스트 이름).
* USER_[connection id] - DB 연결의 사용자 이름.
* PASSWORD_[connection id] - DB 연결의 비밀번호.
* PASSWORD_MODE_[connection id] - 비밀번호와 사용자 이름을 저장할지, 아니면 사용자가 입력해야 하는지를 결정합니다. 다음 값 중 하나:
  * askPassword - DbGate가 연결할 때 비밀번호를 묻습니다
  * askUser - DbGate가 사용자 이름과 비밀번호를 묻습니다
* PORT_[connection id] - DB 연결의 포트.
* FILE_[connection id] - 데이터베이스 파일 경로(SQLite용).
* URL_[connection id] - 데이터베이스 URL(MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle에서 작동).
* SERVICE_NAME_[connection id] - Oracle 서비스 이름.
* DATABASE_[connection id] - 기본 데이터베이스 이름.
* READONLY_[connection id] - 읽기 전용 모드로 연결
* ENGINE_[connection id] - 연결의 엔진(**필수**, 플러그인이 포함된 엔진 이름), 다음 중 하나:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - SSH 터널을 사용해야 하는 경우 값 1 또는 true로 설정
* SSH_HOST_[connection id] - SSH 호스트 이름
* SSH_PORT_[connection id] - SSH 포트 번호
* SSH_MODE_[connection id] - 다음 값 중 하나
  * userPassword - 사용자와 비밀번호로 인증
  * agent - SSH 에이전트로 인증
  * keyFile - 키 파일로 인증
* SSH_LOGIN_[connection id] - SSH 로그인
* SSH_PASSWORD_[connection id] - SSH 비밀번호
* SSH_KEY_FILE_[connection id] - 키 파일의 전체 경로
* SSH_KEY_FILE_PASSWORD_[connection id] - 키 파일 암호
* USE_SSL_[connection id] - SSL을 사용해야 하는 경우 값 1 또는 true로 설정
* SSL_CA_FILE_[connection id] - CA 인증서 파일 경로
* SSL_CERT_FILE_[connection id] - 인증서 파일 경로
* SSL_CERT_FILE_PASSWORD_[connection id] - 인증서 키 파일 비밀번호
* SSL_KEY_FILE_[connection id] - 키 파일 경로
* SSL_REJECT_UNAUTHORIZED_[connection id] - 승인되지 않은 연결을 거부하려면 값 1 또는 true로 설정
* SSL_TRUST_CERTIFICATE_[connection id] - MSSQL의 trustServerCertificate 옵션을 설정하려면 값 1 또는 true로 설정
* SETTINGS_[settings key] - 설정 값을 미리 구성합니다. 설정 키는 소스 코드에서 확인할 수 있습니다. https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - 소켓을 통해 연결하는 경우 소켓 파일 경로
* AUTH_TYPE_[connection id] - 인증 유형
  * hostPort (기본값)
  * socket - SOCKET_PATH를 설정하면 암묵적으로 설정되는 값
  * tedious - tedious 드라이버를 사용하는 MS SQL의 기본 이식 가능 인증
  * sspi - Windows 통합 인증(Windows 전용, MS SQL), 네이티브 MSSQL 드라이버 사용
  * sql - SQL 인증(Windows 전용, MS SQL), 네이티브 MSSQL 드라이버 사용
* ALLOWED_DATABASES_[connection id] - 지정된 연결에 허용되는 데이터베이스 이름, 파이프("|")로 구분
* ALLOWED_DATABASES_REGEX_[connection id] - 지정된 연결에 허용되는 데이터베이스 이름에 대한 정규 표현식
* USE_SEPARATE_SCHEMAS_[connection id] - 스키마를 개별적으로 로드하려면 값 1 또는 true로 설정. 스키마가 큰 경우 사용하세요.
* LOCAL_DATA_CENTER_[connection id] - 로컬 데이터 센터(Apache Cassandra용)
* CONNECTION_[connection id]_parameterName - 엔진별 매개변수 이름 설정

SettingsModal.svelte 에서 "name=" 문자열을 찾으세요. "true"를 정의해야 하는 경우 값 "1"을 사용하세요. "false"가 필요한 경우 빈 문자열을 사용하세요("0"은 작동하지 않습니다)

## 역할 설정
이 설정은 저장소 데이터베이스가 설정에 사용될 때 Team Premium 에디션에서만 사용할 수 있습니다. 환경 변수의 역할은 docker 컨테이너 시작 시 저장소 데이터베이스로 가져옵니다.
특정 권한을 가진 역할을 정의하고 해당 역할에 연결을 할당할 수 있습니다. 사용자에게 역할을 할당하는 것은 관리 UI에서 수행합니다.
* `ROLE_[role_name]_PERMISSIONS` - 지정된 역할에 대한 쉼표로 구분된 권한 목록. 아래 권한 목록을 참조하세요
* `ROLE_[role_name]_CONNECTIONS` - 지정된 역할에 할당된 쉼표로 구분된 연결 ID 목록
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - 지정된 ID의 데이터베이스 권한에 대한 연결 ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - 지정된 ID의 데이터베이스 권한에 대한 파이프("|")로 구분된 데이터베이스 이름 목록
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - 지정된 ID의 데이터베이스 권한에 대한 데이터베이스 이름 정규 표현식
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - 다음 중 하나: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - 지정된 ID의 테이블 권한에 대한 연결 ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - 지정된 ID의 데이터베이스 권한에 대한 파이프("|")로 구분된 데이터베이스 이름 목록
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - 지정된 ID의 데이터베이스 권한에 대한 데이터베이스 이름 정규 표현식
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - 지정된 ID의 테이블 권한에 대한 파이프("|")로 구분된 스키마 이름 목록
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - 지정된 ID의 테이블 권한에 대한 스키마 이름 정규 표현식
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - 지정된 ID의 데이터베이스 권한에 대한 파이프("|")로 구분된 테이블 이름 목록
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - 지정된 ID의 데이터베이스 권한에 대한 테이블 이름 정규 표현식
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - 다음 중 하나: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - 다음 중 하나: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## 권한
기본적으로 모든 권한을 사용할 수 있습니다. \~ 접두사를 사용하면 해당 권한이 취소됩니다.

### 예시
* ~*, widgets/database - 모든 권한이 취소되고 데이터베이스 위젯만 표시됩니다
* ~widgets/*, widgets/database - 모든 위젯 권한이 취소되고 데이터베이스 위젯만 표시됩니다
* ~connections/*, connections/con1 - con1을 제외한 모든 연결이 숨겨지고 비활성화됩니다

### 권한 목록
* settings/change - 설정 변경을 허용합니다
* plugins/install - 플러그인 설치를 허용합니다
* widgets/[widget_name] - 부여되지 않으면 위젯이 숨겨집니다. 위젯은 왼쪽의 스트립입니다. 사용 가능한 위젯:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - 지정된 폴더에서 파일 읽기
* files/[folder]/write - 지정된 폴더에 파일 쓰기
* apps/write - 앱 콘텐츠에 저장
* archive/write - 아카이브 콘텐츠에 저장
* connections/[connection_id] - 정의된 연결을 보고 사용하도록 허용
* internal-storage = 내부 저장소 접근 (Premium)
* admin/auth - 관리 - 인증 탭 (Premium)
* admin/connections - 관리 - 연결 탭 (Premium)
* admin/users - 관리 - 사용자 탭 (Premium)
* admin/roles - 관리 - 역할 탭 (Premium)
* dbops/sql-template/* - SQL 템플릿 (예: SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - SQL 생성기
* dbops/sql-dump/import - SQL 덤프 가져오기
* dbops/sql-dump/export - SQL 덤프 내보내기
* dbops/query - SQL 쿼리 실행
* dbops/import - 데이터 가져오기
* dbops/export - 데이터 내보내기
* dbops/charts - 차트 보기
* dbops/profiler - 데이터베이스 프로파일러
* dbops/createdb - 데이터베이스 생성
* dbops/dropdb - 데이터베이스 삭제
* dbops/model/view - 데이터베이스 모델 보기(다이어그램, JSON)
* dbops/model/edit - 데이터베이스 모델 편집(테이블, 뷰 등 생성/변경)
* dbops/model/compare - 데이터베이스 모델 비교
* dbops/table/rename - 테이블 이름 변경
* dbops/table/truncate - 테이블 비우기
* dbops/table/backup - 테이블 백업 생성
