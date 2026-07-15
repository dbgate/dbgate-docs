---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: ko
title: Docker에서 Team Premium 실행
weight: 30
---

일반적인 Team Premium 설치는 두 가지 구성 요소로 이루어집니다:
- DbGate 서버 도커 컨테이너
- 데이터베이스 서버 (MS SQL, MySQL, PostgreSQL, Oracle) - 연결, 사용자 및 역할을 저장하는 내부 스토리지 데이터베이스입니다. 기존 데이터베이스 서버를 사용하거나 새로 설치할 수 있습니다.

## DbGate 서버 도커 컨테이너
Docker Hub의 [DbGate Team Premium 이미지](https://hub.docker.com/r/dbgate/dbgate-premium)를 사용하세요:
```
docker pull dbgate/dbgate-premium
```

DbGate Team Premium 컨테이너는 몇 가지 환경 변수를 설정해야 합니다:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - 내부 스토리지 데이터베이스로의 연결을 정의합니다

사용 가능한 환경 변수에 대한 자세한 내용은 [환경 변수 문서](/ko/dbgate/customization/env-variables/#team-premium-edition-configuration)를 참조하세요.

## 리소스 요구 사항

실제로 DbGate Team Premium은 리소스 소비가 매우 적지만, 최상의 성능을 위해 다음 구성을 권장합니다 (동시 사용자 10명 기준):
- CPU 코어 2개
- RAM 4GB (MySQL 또는 PostgreSQL 내부 스토리지 데이터베이스의 RAM 소비 포함)
- 여유 디스크 공간 10GB (도커 설치, 스토리지 데이터베이스, 임시 파일, 쿼리 결과 등을 위한 공간입니다. 실제 디스크 공간 소비는 사용 패턴에 따라 달라집니다)

사용자 수가 적다면 더 낮은 리소스 제한(RAM 1GB, CPU 코어 1개)을 사용할 수 있습니다.  
소규모 설치에서 리소스 소비를 최소화해야 하는 경우, 내부 스토리지로 MySQL/MariaDB를 사용하는 것을 권장합니다.  

## 도커 구성

사용자 파일(예: 쿼리 결과 내보내기)을 디스크 파일로 저장하려면 컨테이너의 `/root/.dbgate` 경로를 매핑해야 합니다.

아래는 PostgreSQL을 내부 스토리지 데이터베이스로 사용하는 DbGate Team Premium 컨테이너를 정의하는 `docker-compose.yml` 파일 예시입니다.
- `DBGATE_LICENSE` 환경 변수를 정의하여 라이선스 키를 설정할 수 있습니다. 설정하지 않으면 DbGate가 첫 실행 시 라이선스 키를 요청합니다.
-  'ADMIN_PASSWORD' 환경 변수를 정의하여 admin 사용자 비밀번호를 설정할 수 있습니다. 설정하지 않으면 DbGate가 첫 실행 시 admin 비밀번호를 요청합니다.

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## 무상태/상태 저장
DbGate 컨테이너는 상태를 저장합니다.

다음 데이터가 컨테이너 내부에 저장됩니다:
* 로그인한 사용자 세션
* 쿼리 실행 상태
* 임시 파일 (예: 결과)
* 열린 데이터베이스 트랜잭션
* 열린 데이터베이스 연결

위의 데이터는 컨테이너 간에 공유되지 않기 때문에, 로드 밸런서 뒤에서 여러 DbGate 컨테이너를 올바르게 실행하는 것은 불가능합니다.

## NPM에서 DbGate 서버 설치
인프라가 Docker를 지원하지 않는 경우 [DbGate Team Premium NPM 패키지](https://www.npmjs.com/package/dbgate-serve-premium)를 사용할 수 있습니다:
```
npm install -g dbgate-serve-premium
```
 
## 프로세스 격리
DbGate Team Premium은 데이터베이스 연결 수준에서 프로세스 격리를 사용하므로, 여러 사용자가 서로 간섭 없이 동일한 데이터베이스 서버를 사용할 수 있습니다. DbGate에서 포크된 프로세스는 활성 사용자 및 연결 수에 따라 늘어나므로, 서버에 충분한 리소스가 있는지 확인하세요.
다음 엔터티는 새 프로세스로 격리됩니다:
* 서버 연결
* 데이터베이스 연결
* 쿼리 세션
* 내보내기/가져오기 작업 실행
* SSH 터널링
