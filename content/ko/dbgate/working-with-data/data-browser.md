---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: ko
title: 데이터 브라우저 및 편집기
weight: 5
---

데이터 브라우저는 테이블 데이터를 보고 편집하기 위한 DbGate의 핵심 뷰입니다. 아무 테이블, 뷰 또는 컬렉션을 열면 Excel과 유사한 빠른 그리드가 표시됩니다. 이 페이지에서는 데이터 탐색, 편집 및 관련 데이터 탐색을 다룹니다. 필터 표현식은 [데이터 필터링](data-filtering)을 참조하세요.

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## 데이터 탐색

* **키보드 탐색** - 스프레드시트에서처럼 화살표 키로 그리드를 이동합니다.
* **정렬** - 열 머리글을 클릭하면 해당 열을 기준으로 정렬됩니다.
* **필터** - 그리드 위의 필터 행을 사용하여 행을 필터링합니다. 전체 표현식 구문은 [데이터 필터링](data-filtering)을 참조하세요.
* **열 관리자** - 이름으로 열을 찾고 필요 없는 열을 숨깁니다.
* **고급 복사** - 선택한 셀을 CSV, YAML, SQL `INSERT` 또는 MongoDB insert로 복사합니다.

## 데이터 편집

데이터 편집은 그리드에서 직접 이루어집니다:

* **Excel과 유사한 편집** - 셀을 제자리에서 편집하고, 테이블 간을 포함하여 행 범위를 복사하고 붙여넣습니다.
* **보류 중인 변경 사항** - 편집 내용은 보류 중인 변경 사항으로 수집됩니다. 데이터베이스에 적용되기 전에 생성된 SQL 변경 스크립트를 검토한 다음 저장하거나 되돌립니다.
* **행 삽입 및 삭제** - 그리드 또는 컨텍스트 메뉴에서 수행합니다.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### 데이터 편집기 매크로 *(Premium)*

선택한 셀에 미리 정의된 매크로를 적용합니다. 예를 들어 텍스트 대소문자 변경, 분음 부호 제거 또는 UUID 생성 등이 있습니다.

## 관련 데이터 다루기

DbGate를 사용하면 테이블 간의 관계를 쉽게 따라갈 수 있습니다:

* **관계 힌트** - 숫자 외래 키 옆에 참조된 테이블의 텍스트 값을 표시합니다.
* **외래 키 열 확장** - 외래 키 열을 확장하여 참조된 데이터를 인라인으로 봅니다.
* **상세 열기** - 외래 키가 참조하는 행으로 이동합니다.
* **마스터/디테일 뷰** *(Premium)* - 연결된 마스터/디테일 레이아웃에서 관련 행을 탐색합니다.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## 폼 뷰

폼 뷰는 단일 행을 세로로 "전치된" 목록으로 표시하므로 열이 많은 테이블에 적합합니다. 트리 뷰로 작동하므로 외래 키 열을 확장하여 관련 데이터를 탐색할 수 있습니다.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## 그룹화 *(Premium)*

그리드 뷰에서 그룹화(`GROUP BY`)를 적용하여 탐색하는 동안 행을 바로 집계합니다.

## 관련 페이지

* [데이터 필터링](data-filtering) - 필터 표현식 구문
* [내보내기 및 가져오기](export-import) - 테이블 안팎으로 데이터 이동
* [퍼스펙티브](perspectives) - 복잡한 관련 데이터에 대한 중첩된 읽기 전용 뷰
* [SQL 편집기](/ko/dbgate/sql-and-queries/sql-editor/) - 동일한 방식으로 쿼리 결과 편집 *(Premium)*
