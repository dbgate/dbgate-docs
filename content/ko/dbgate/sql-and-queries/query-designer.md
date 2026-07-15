---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: ko
title: 쿼리 디자이너
weight: 20
---

쿼리 디자이너 *(Premium)* 를 사용하면 SQL을 직접 작성하지 않고도 시각적으로 SQL 쿼리를 만들 수 있습니다. 캔버스에 테이블을 추가하고 컬럼을 선택한 뒤 조건을 정의하면 DbGate가 SQL을 생성해 줍니다.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## 쿼리 만들기

* **테이블 추가** - 디자인 캔버스에 테이블을 끌어다 놓으면 DbGate가 외래 키를 기반으로 관계를 자동으로 그려 줍니다.
* **컬럼 선택** - 결과에 표시할 컬럼을 선택하고 정렬 및 그룹화를 정의합니다.
* **JOIN 유형** - 표준 SQL 조인(`INNER`, `LEFT`, `RIGHT`) 외에도 의사 조인(pseudo-join)을 사용할 수 있으며, 그중 가장 유용한 것은 `WHERE NOT EXISTS`입니다.
* **강력한 필터** - [데이터 브라우저](/ko/dbgate/working-with-data/data-browser/)와 동일한 엔진으로 필터링하며, 복합 조건과 값 집합을 이용한 필터링도 지원합니다.

## 결과

디자이너는 일반적인 SQL 쿼리를 생성하므로, 직접 작성한 SQL과 동일한 성능으로 실행됩니다. 언제든지 생성된 SQL로 전환하여 [SQL 편집기](sql-editor)에서 계속 편집할 수 있습니다.

## Perspectives - 범용 디자이너

중첩된 계층형 뷰가 필요하거나 SQL 테이블과 MongoDB 컬렉션의 데이터를 클라이언트 측에서 조인해야 한다면 [Perspectives](/ko/dbgate/working-with-data/perspectives/)를 사용하세요. Perspectives는 소스 데이터베이스가 조인할 수 있는 범위에 제한받지 않습니다.
