---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: ko
title: 데이터 필터링
weight: 10
---

DbGate는 강력한 데이터 필터링 엔진을 갖추고 있어, 매우 간단한 데이터 필터링부터 복잡한 조건까지 모두 사용할 수 있습니다.

데이터 필터는 DbGate의 여러 곳에서 사용할 수 있지만, 가장 일반적인 곳은 데이터 그리드 필터링입니다.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

필터는 배경색으로 표시됩니다:
* 초록색 배경 - 필터가 올바르며 적용되었습니다
* 빨간색 배경 - 필터 표현식에 오류가 있어 필터가 무시됩니다

필터를 만드는 방법에는 여러 가지가 있습니다:
* {{< mdi "filter" >}} - 미리 정의된 필터와 대화 상자가 있는 메뉴를 표시합니다
* {{< mdi "dots-vertical" >}} - 필터링할 값을 선택할 수 있습니다
* 필터를 직접 입력할 수 있습니다 - [필터 표현식](#filter-expressions)에 설명된 매우 간단한 구문을 사용하세요
* 또는 시각적 방법으로 필터를 만든 다음 수동으로 편집할 수 있습니다

기타 명령:
* {{< mdi "filter-off" >}} - 모든 필터 지우기

## Filter expressions
필터 표현식은 직관적으로 설계되어 있어, 대부분의 경우 찾고자 하는 것을 그대로 입력하면 됩니다. 하지만 구문은 상당히 강력해서, 여러 조건을 결합하고 다양한 연산자를 사용할 수 있습니다.
표현식 구문은 컬럼의 데이터 타입에 따라 달라집니다.

### 예제

| 컬럼 타입 | 필터 표현식 |  설명 |
|----------|-------------|------|
| string | canada | 컬럼 값이 "canada" 텍스트를 포함합니다 |
| string | canada, usa | 컬럼 값이 "canada" 또는 "usa" 텍스트를 포함합니다 |
| string | canada lake | 컬럼 값이 "canada"와 "lake" 텍스트를 모두 포함합니다 |
| string | NOT EMPTY NOT NULL | 문자열이 비어 있지 않은 값을 가집니다 |
| number | >10 | 컬럼 값이 10보다 큽니다 |
| number | >=5 <=10 | 컬럼 값이 5와 10 사이입니다 |
| number | 1,2,3 | 컬럼 값이 1 또는 2 또는 3입니다 |
| datetime | 2020-05-26 | 날짜 값이 2020-05-26입니다 (24시간 간격)  |

### 공통 필터 (모든 데이터 타입용)
- NULL - 컬럼 값이 null입니다
- NOT NULL - 컬럼 값이 null이 아닙니다
- {$$ is null} - SQL 조건, {} 중괄호 안에 작성합니다. $$는 필터링되는 컬럼의 자리 표시자입니다

### 텍스트 필터
텍스트 비교는 대소문자를 구분하지 않습니다.
- text - 컬럼 값이 _text_를 포함합니다. '작은따옴표' 또는 "큰따옴표"로 묶을 수 있습니다
- +text - 컬럼 값이 _text_를 포함합니다 (위 줄과 동일)
- ^text - 컬럼 값이 _text_로 시작합니다
- $text - 컬럼 값이 _text_로 끝납니다
- !+text - 컬럼 값이 _text_를 포함하지 않습니다 (위 줄과 동일)
- !^text - 컬럼 값이 _text_로 시작하지 않습니다
- !$text - 컬럼 값이 _text_로 끝나지 않습니다
- EMPTY - 컬럼 값에 공백이 아닌 문자가 없습니다
- NOT EMPTY - 컬럼 값에 공백이 아닌 문자가 있습니다

### 숫자 필터
- number - 컬럼 값이 number와 같습니다
- =number - 컬럼 값이 number와 같습니다
- !=number - 컬럼 값이 number와 같지 않습니다
- <>number - 컬럼 값이 number와 같지 않습니다
- <number - 컬럼 값이 number보다 작습니다
- \>number - 컬럼 값이 number보다 큽니다
- <=number - 컬럼 값이 number보다 작거나 같습니다
- \>=number - 컬럼 값이 number보다 크거나 같습니다

### 날짜/시간 필터
- 2021 - 컬럼 값의 연도
- 2021-02 - 컬럼 값의 연도, 월
- 2021-02-15 - 컬럼 값의 연도, 월, 일
- 2021-02-15 23:15 - 컬럼 값의 연도, 월, 일, 시, 분
- 2021-02-15 23:15:51 - 컬럼 값의 연도, 월, 일, 시, 분, 초
- 현재 날짜에 대한 상대 필터
  - YESTERDAY
  - TODAY
  - TOMORROW
  - LAST WEEK
  - THIS WEEK
  - NEXT WEEK
  - LAST MONTH
  - THIS MONTH
  - NEXT MONTH
  - LAST YEAR
  - THIS YEAR
  - NEXT YEAR

### 논리(boolean) 필터
- TRUE, true, 1 - 컬럼 값이 true/1입니다
- FALSE, false, 0 - 컬럼 값이 false/0입니다

### 필터 조합
필터는 서로 결합할 수 있습니다. 공백은 AND 연산자로, 쉼표는 OR 연산자로 해석됩니다. AND가 OR보다 우선순위가 높습니다.
