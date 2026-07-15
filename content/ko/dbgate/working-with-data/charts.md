---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: ko
title: 차트
weight: 30
---

DbGate에서는 SQL 쿼리를 시각화하는 데 차트를 사용할 수 있습니다. 쿼리를 실행하기만 하면 차트가 자동으로 감지되어 "Chart 1" 탭이 나타납니다. 쿼리 결과가 여러 개인 경우 차트도 여러 개 있을 수 있습니다.

차트가 자동으로 감지되지 않았지만 쿼리 결과에서 차트를 만들고 싶다면, 쿼리 결과 데이터를 마우스 오른쪽 버튼으로 클릭하고 "Open chart"를 선택하세요.

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## 차트 설정
{{< mdi "pencil" >}} Customize 버튼을 사용하여 차트 설정을 엽니다. 차트 데이터 원본과 스타일을 구성할 수 있습니다:
* 차트 유형
  * Bar
  * Line
  * Timeline - X축에 시간이 표시되는 선형 차트의 특수한 경우입니다
  * Pie
  * Polar area
* X축 필드 - X축의 데이터입니다. 날짜/시간 값의 경우 그룹화 및 타임라인 함수를 사용할 수 있습니다
* 그룹화 필드 - 이 필드의 값으로 지정되는 여러 차트를 정의합니다
* X축 변환 - X축 타임라인에 대한 그룹화를 정의할 수 있습니다(예: 연도별 또는 월별)
* Y축 필드 N - Y축에 여러 필드를 둘 수 있습니다
  * 각 데이터 집합에는 행 수를 세는 특수 필드 "Count"를 사용할 수 있습니다
* 집계 함수 - Sum, Minimum, Maximum, Average, First Value, Last Value

차트 설정에서 옵션을 변경하면 SQL 스크립트 시작 부분에 front-matter로 저장됩니다.

## 차트 정의 직접 편집하기
일부 옵션은 편집기에서 사용할 수 없지만 SQL 코드에서 편집할 수 있습니다. 자세한 내용은 [SQL front matter](/ko/dbgate/developer/sql-front-matter)를 참조하세요
