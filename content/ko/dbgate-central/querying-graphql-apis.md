---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: ko
title: GraphQL API 쿼리하기
weight: 20
---

DbGate Central을 임의의 GraphQL API에 연결하기만 하면 사용 가능한 항목을 자동으로 찾아냅니다 - 별도의 문서를 뒤질 필요가 없습니다.

## 스키마 살펴보기

DbGate Central은 연결하는 즉시 GraphQL 스키마를 인트로스펙션합니다. 트리에서 사용 가능한 타입과 필드를 둘러본 다음, 쿼리 탭을 열어 작업을 시작하세요.

## 쿼리 실행

* GraphQL 편집기로 쿼리를 작성하고 실제 API에 대해 실행합니다.
* 쿼리와 함께 쿼리 변수를 폼 형태 또는 원시 JSON으로 전달할 수 있습니다.
* 결과는 DbGate 전반에서 사용하는 것과 동일하게 빠르고 정렬 및 필터링이 가능한 그리드로 표시되므로, GraphQL 응답이 마치 데이터베이스 테이블처럼 느껴집니다.
* 중첩된 객체와 목록은 구조화된 JSON으로 반환되어 그 자리에서 펼쳐 확인할 수 있습니다.

쿼리한 뷰는 연결별로 캐시되므로, 작업을 계속하면서 다시 열 때 즉시 표시됩니다.

> DbGate Central의 GraphQL 연결은 [데스크톱 GraphQL 기능](/ko/dbgate/developer/api-connections/#graphql)과는 별개인 브라우저 기반 구현입니다 - 데스크톱 앱을 사용 중이라면 해당 페이지를 참고하세요.

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
