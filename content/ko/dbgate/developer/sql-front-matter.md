---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: ko
title: SQL 프론트 매터
weight: 50
---

SQL 프론트 매터는 SQL 파일의 시작 부분에 있는 YAML 형식의 메타데이터입니다. 이 개념은 마크다운 파일에 프론트 매터를 도입한 gohugo와 Jekyll에서 영감을 받았습니다. ([Hugo의 프론트 매터](https://gohugo.io/content-management/front-matter/))

SQL 프론트 매터는 SQL 파일 시작 부분의 파일 표시 `-- >>>`에서 바로 시작하며 `-- <<<`만 포함된 줄로 끝납니다. YAML 내용의 모든 줄에는 `-- ` 접두사가 붙으므로 파일 전체가 유효한 SQL로 유지됩니다.

이 메타데이터는 특히 차트(차트 구성 저장)와 공개 지식 베이스 속성(스크립트 제목 및 설명 등)에 사용됩니다. 하지만 DbGate의 모든 SQL 스크립트에서 사용할 수 있는 속성도 있습니다.

## 일반 속성
- autoExecute: `true` 또는 `false`, 열 때 스크립트를 자동으로 실행할지 여부
- splitterInitialValue: 백분율(예: 20%) 또는 절대 크기(예: 220px) - 상단 SQL 영역의 크기를 정의하는 데 사용합니다. 나머지는 쿼리 결과에 사용됩니다

## 공개 지식 베이스 속성
- title: 스크립트 제목(기본값 - 확장자를 제외한 파일 이름)
- description: 스크립트 설명(기본값 - 비어 있음)
- icon: 스크립트 아이콘([Material design icons](https://pictogrammers.com/library/mdi/)에서, `mdi mdi-chart-pie` 형식)

## 차트 속성
- selected-chart: 자동 선택할 차트의 번호(1부터 시작)
- chart-N: N번째 차트의 정의
    - title: 차트 제목
    - pieRatioLimit - 파이 차트의 한계값, 값이 이보다 작으면 "기타"로 그룹화됩니다(기본값: 0.05)
    - pieCountLimit - 파이 차트 조각 수의 한계값, 조각 수가 이보다 많으면 "기타"로 그룹화됩니다(기본값 10)
    - dataLabelFormatter - 데이터 레이블의 포맷터, 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb' 중 하나

최신 전체 필드 목록은 [TypeScript 정의](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts)의 `ChartDefinition` 인터페이스를 참조하세요

## 예제

```sql
-- >>>
-- selected-chart: 1
-- chart-1:
--   chartType: bar
--   xdef:
--     field: InvoiceDate
--     transformFunction: date:month
--   ydefs:
--     - field: Total
--       aggregateFunction: sum
-- <<<
SELECT
  `InvoiceId`,
  `CustomerId`,
  `InvoiceDate`,
  `BillingAddress`,
  `BillingCity`,
  `BillingState`,
  `BillingCountry`,
  `BillingPostalCode`,
  `Total`
FROM
  `Invoice`
```
