---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: ko
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/)는 설치나 로그인 없이 데이터를 다룰 수 있는 무료 브라우저 기반 도구입니다. [DbGate Central](../dbgate-central/)과 동일한 그리드, 필터링 및 쿼리 엔진을 기반으로 만들어졌기 때문에 데이터 탐색, 필터링, 편집이 두 제품에서 동일하게 느껴집니다.

## SQL 배우기와 가르치기

DbGate Lite는 WebAssembly를 사용하여 **SQLite와 DuckDB**를 전적으로 브라우저 안에서 실행합니다:

* 익숙한 DbGate 그리드에서 샘플 데이터베이스를 대상으로 SQL 쿼리를 작성하고 실행합니다.
* ER 다이어그램으로 테이블 간의 관계를 시각화합니다.
* 설치도 로그인도 필요 없습니다 - 사이트를 열고 바로 작업을 시작하세요.

## 데이터 파일로 하는 임시 작업

DbGate Lite에서 파일을 열고 데이터베이스처럼 다뤄 보세요:

* CSV, JSON, Excel 파일을 **가져와서** SQL로 쿼리하거나 편집합니다.
* 데이터를 정리하고 재구성한 다음, 결과를 다시 CSV, JSON 또는 Excel로 **내보냅니다**.

## 링크로 데이터베이스나 쿼리 공유하기

URL에 특정 해시 매개변수를 넣어 DbGate Lite를 열면 임시 데이터베이스가 자동으로 초기화됩니다:

* `initdbtype` - 데이터베이스 유형, `sqlite` 또는 `duckdb`
* `initdbscript` - 임시 데이터베이스를 생성하고 채우는 데 사용되는 SQL 스크립트
* `initquery` (선택 사항) - 새 Query 탭에서 열리는 SQL 쿼리

링크를 여는 사람은 누구나 클릭 한 번으로 동일한 샘플 데이터베이스와 쿼리를 받게 됩니다 - 튜토리얼, 버그 리포트, 교육에 유용합니다.

## 읽기 전용 뷰 게시하기

편집 가능한 링크를 공유하는 것과는 별개로, 툴바의 Publish 버튼을 사용하여 CSV/JSON 파일이나 BI 리포트의 읽기 전용 뷰를 **게시할** 수 있습니다. 그러면 독립된 페이지가 열리는데 - 사이드바나 편집기 없이 데이터와 라이트/다크 전환 버튼만 있습니다 - 링크가 있는 사람은 누구나 계정 없이 볼 수 있습니다.

## Lite, Central, Premium, Team Premium 중에서 선택하기

DbGate Lite는 학습과 일회성 작업에 가장 적합합니다. 지속적이고 전문적인 작업에는 전용 제품이 더 적합합니다:

* **DbGate Lite** - 무료, 브라우저 기반. SQL 학습과 임시 데이터 파일 작업에 가장 적합합니다.
* **[DbGate Central](../dbgate-central/)** - API 작업을 위한 호스팅 제품: 실시간 GraphQL, oData, Shopify 엔드포인트에 연결하고, 연결과 리포트를 워크스페이스에 보관하며, 팀과 공유할 수 있습니다.
* **[DbGate Premium](/ko/dbgate/getting-started/installation/)** - [DbGate](/ko/dbgate/)의 에디션: 데이터베이스 작업을 위한 완전한 데스크톱 애플리케이션으로, 전문가용 도구 전체를 갖추고 SQL 및 NoSQL 서버에 연결합니다.
* **[DbGate Team Premium](/ko/dbgate/getting-started/installation/docker-tp/)** - 팀을 위한 [DbGate](/ko/dbgate/)의 또 다른 에디션: 온프레미스로 실행되는 공유 웹 인터페이스로, 팀 전체가 자체 인프라에서 브라우저를 통해 데이터베이스 작업을 할 수 있습니다.
