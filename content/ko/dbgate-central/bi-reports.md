---
sourceHash: ff92448ee8e00aae1c7fc20030ddea3637a2e8c7952daeac5c129c5fbb48e420
language: ko
title: API 데이터로 만드는 BI 리포트
weight: 40
---

DbGate Central은 API 응답을 자체 내장 데이터 엔진에 적재하므로, 이를 결합하고 집계하고 시각화할 수 있습니다. 즉, 원시 API 응답을 읽기 쉬운 BI 리포트로 바꿔 줍니다.

## 원시 응답에서 인사이트로

* **집계 및 피벗** - 데이터를 요약 테이블로 만들어 임의의 차원별로 건수, 합계, 세부 내역을 확인할 수 있습니다.
* **여러 소스 연결** - 서로 다른 엔드포인트에 있는 데이터를 하나의 리포트에서 조인할 수 있습니다.
* **드릴다운** - 계층 구조를 따라 내려가며 전체 흐름에서 개별 행까지 살펴볼 수 있습니다.

oData 및 Shopify 엔드포인트(그리고 CSV/JSON/Excel 파일)를 BI 소스로 사용할 수 있습니다. GraphQL API는 쿼리에는 훌륭하지만 현재 리포팅 소스로는 사용할 수 없으며, 대신 직접 탐색하고 쿼리할 수 있습니다([GraphQL API 쿼리하기](../querying-graphql-apis) 참조).

## 리포트 공유

리포트는 독립적인 읽기 전용 뷰로 **게시**할 수 있습니다. 링크를 가진 사람은 누구나 계정 없이, 그리고 사용자의 연결에 접근하지 않고도 실시간 데이터를 확인하고 드릴다운할 수 있습니다.

![DbGate Central - turn API data into a report](https://lite.dbgate.io/screenshots/central-bi-dark.png)
