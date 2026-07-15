---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: ko
title: 백업 및 복원
weight: 20
---

DbGate는 데이터베이스를 백업하고 복원하기 위해 네이티브 도구를 사용합니다. 이 기능은 Premium 에디션 전용입니다.

지원되는 도구:

- PostgreSQL
  - `pg_dump` 및 `psql`
- MySQL+MariaDB
  - `mysqldump` 및 `mysql`

## 이러한 도구를 설치하는 방법
Team Premium 에디션의 Docker, AWS 또는 Azure 버전을 사용하는 경우에는 이 문제를 해결할 필요가 없습니다. 이 패키지들에는 필요한 모든 도구가 이미 번들로 포함되어 있습니다.

가장 쉬운 방법은 전체 데이터베이스 엔진을 데스크톱에 설치하는 것입니다.
하지만 대부분의 플랫폼과 데이터베이스에서는 클라이언트만 설치하는 것도 가능합니다:

- PostgreSQL
  - Windows - https://www.enterprisedb.com/download-postgresql-binaries 에서 클라이언트를 다운로드하고 압축을 해제하세요
  - Mac: homebrew로 클라이언트를 설치하세요: `brew install libpq`
- MySQL:
  - Windows - https://dev.mysql.com/downloads/mysql/ 에서 ZIP 파일을 다운로드하고 압축을 해제하세요
  - Mac: brew install mysql-client
