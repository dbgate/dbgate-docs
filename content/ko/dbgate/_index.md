---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: ko
title: DbGate
weight: 5
---

## DbGate란?

DbGate는 지원되는 데이터베이스에 연결하여 작업할 수 있는 데이터베이스 관리 도구입니다. 데스크톱 앱이자 웹 앱이기도 합니다. 빠르고 사용하기 쉽도록 설계되었습니다.

브라우저 기반 및 호스팅 제품(DbGate Lite, Central, Shopify App)에 대해서는 [제품 개요](/ko/)를 참조하세요.

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## 지원되는 데이터베이스

| 데이터베이스 | {{< center "Community" >}} | {{< center "Premium" >}} | 추가 기능 |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | 백업, 복원 |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | 백업, 복원 |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | 백업, 복원 |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## 지원되는 플랫폼

- 데스크톱
  - Windows
  - MacOS (ARM 및 Intel 프로세서 모두)
  - Linux
- 웹 버전
  - Docker
  - NPM
  - Azure
  - AWS

## 에디션

DbGate는 세 가지 에디션으로 제공됩니다:

| 에디션 | 배포 방식 | 주요 기능 |
|---|---|---|
| Community | 데스크톱 앱 또는 자체 호스팅 웹(Docker/NPM), 무료 | 표준 SQL 및 NoSQL 데이터베이스 연결 및 탐색/편집, Redis GUI, 최대 5개의 DbGate Cloud 연결/파일 |
| Premium | 데스크톱 앱(단일 사용자) | Community의 모든 기능에 더해 [쿼리 디자이너](sql-and-queries/query-designer), [차트](working-with-data/charts), [편집 가능한 쿼리 결과 및 뷰](sql-and-queries/sql-editor), [마스터/디테일 뷰](working-with-data/data-browser), [AI 도구](working-with-data/ai-features)(DB 채팅, 오류 설명, 테마 어시스턴트), DB 모델 비교 및 배포, 고급/일괄 내보내기-가져오기, [데이터 디플로이어](working-with-data/advanced-data-tools/data-deployer), [API 연결](developer/api-connections)(GraphQL/oData/OpenAPI), 추가 데이터베이스 엔진(libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), 무제한 DbGate Cloud 스토리지 |
| Team Premium | 데스크톱 앱 + 자체 호스팅 웹(Docker/NPM/AWS/Azure) | Premium의 모든 기능에 더해 웹 애플리케이션, [관리 UI](admin), 사용자/역할/권한, 외부 ID 공급자(OAuth/OIDC), 무설정 네이티브 백업 및 복원 |

## 이 섹션의 내용

* [시작하기](getting-started) - DbGate를 설치하고 첫 데이터베이스에 연결합니다
* [데이터 작업](working-with-data) - 데이터 탐색, 편집, 필터링, 차트, 지도, 내보내기 및 아카이브
* [SQL 및 쿼리](sql-and-queries) - SQL 편집기, 시각적 쿼리 디자이너 및 ER 다이어그램
* [데이터베이스 작업](database-operations) - 스키마 편집, 모델 비교 및 배포, 백업 및 복원
* [커스터마이징](customization) - 모양 및 런타임 설정 구성
* [관리](admin) - 사용자, 역할 및 권한 관리 (Team Premium)
* [개발자 및 자동화](developer) - 스크립트, API 연결 및 플러그인
* [DbGate Cloud](dbgate-cloud) - 연결, SQL 스크립트 및 공유 폴더를 위한 온라인 스토리지
