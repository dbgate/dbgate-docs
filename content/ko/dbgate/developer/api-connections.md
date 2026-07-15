---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: ko
title: API 연결
weight: 10
---

DbGate는 REST API, GraphQL 서비스 및 OData 엔드포인트에 대한 연결을 지원합니다. 이러한 API 연결은 데이터베이스 연결과 동일한 인터페이스 패턴을 사용하므로 통합된 환경에서 API와 데이터베이스를 함께 다룰 수 있습니다.

API 연결 지원은 DbGate Premium에서 제공됩니다.

> 데스크톱 앱 없이 API를 탐색하고 싶으신가요? [DbGate Central](/dbgate-central/connecting-to-api-endpoints/)은 GraphQL/oData/Shopify 연결을 브라우저용으로 처음부터 새로 구현한 별도의 호스팅 구현체입니다.

## GraphQL

GraphQL 연결을 사용하면 GraphQL API와 상호 작용할 수 있습니다. DbGate는 스키마 인트로스펙션과 쿼리 실행 기능을 제공합니다.

### GraphQL 연결 만들기

GraphQL 연결을 만들려면 New Connection 대화 상자를 열고 연결 유형으로 GraphQL을 선택하세요. GraphQL 엔드포인트 URL을 입력하고 필요한 경우 인증을 구성합니다.

### 스키마 인트로스펙션

DbGate는 사용 가능한 타입, 쿼리, 뮤테이션 및 해당 인수를 포함한 GraphQL 스키마를 자동으로 검색합니다. 스키마 브라우저는 타입 시스템을 표시하며 API 구조를 탐색할 수 있게 해줍니다.

### 쿼리 편집기

GraphQL 쿼리 편집기에서 쿼리와 뮤테이션을 작성할 수 있습니다. GraphQL 탐색기를 사용하여 스키마에서 필드와 인수를 선택하는 방식으로 쿼리를 구성할 수 있습니다.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### 변수

GraphQL 쿼리는 변수를 지원합니다. 변수 패널에서 변수를 정의하고 표준 GraphQL 변수 구문을 사용하여 쿼리에서 참조하세요. 변수는 폼에서 편집하거나 원시 JSON으로 편집할 수 있습니다.

### 응답 뷰어

쿼리 결과는 확장 가능한 트리 구조의 서식이 적용된 JSON 뷰어에 표시됩니다. 응답에서 배열이 감지되면 표 형식 보기가 자동으로 표시됩니다. 필요한 경우 원시 JSON 보기로 다시 전환할 수 있습니다.

## OpenAPI (Swagger)

OpenAPI 연결은 OpenAPI 사양(버전 2.0 및 3.0)을 제공하는 REST API를 지원합니다.

### OpenAPI 연결 만들기

새 연결을 만들고 연결 유형으로 OpenAPI를 선택하세요. OpenAPI 사양 파일(일반적으로 swagger.json 또는 openapi.json)의 URL을 입력합니다. DbGate가 사양을 파싱하여 문서화된 모든 엔드포인트를 사용할 수 있게 합니다.

### API 문서 브라우저

OpenAPI 브라우저는 사용 가능한 모든 엔드포인트를 태그와 경로별로 정리하여 표시합니다. 각 엔드포인트에 대해 다음을 확인할 수 있습니다:
- HTTP 메서드 (GET, POST, PUT, DELETE, PATCH)
- 매개변수 (path, query, header, body)
- 요청 본문 스키마
- 문서 설명

### 요청 실행

엔드포인트를 선택하면 요청 빌더가 열립니다. 필수 매개변수, 헤더 및 요청 본문을 입력하세요. 요청을 실행하여 API 서버로 전송합니다.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### 응답 검사

응답 상태 코드, 헤더 및 본문을 확인할 수 있습니다. JSON 응답은 서식이 적용되며 트리 보기와 테이블 보기 모두로 표시할 수 있습니다. JSON이 아닌 응답은 텍스트로 표시됩니다.

## OData

OData 연결은 표준 OData 쿼리 구문을 사용하여 OData 서비스를 쿼리하는 것을 지원합니다.

### OData 연결 만들기

연결 유형으로 OData를 선택하여 새 연결을 만드세요. OData 서비스 루트 URL을 입력합니다. DbGate가 서비스 메타데이터 문서를 가져옵니다.

### 메타데이터 탐색

메타데이터 브라우저는 서비스 메타데이터에 정의된 사용 가능한 엔터티 집합, 엔터티 타입, 속성 및 관계를 보여줍니다.

### 쿼리 실행

OData 쿼리는 표준 OData 쿼리 옵션을 지원합니다:
- `$filter` - 속성 값으로 엔터티 필터링
- `$select` - 반환할 속성 지정
- `$expand` - 관련 엔터티 포함
- `$orderby` - 결과 정렬
- `$top` 및 `$skip` - 페이지네이션
- `$count` - 결과 개수 포함

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

결과는 데이터베이스 쿼리 결과와 유사하게 표 형식으로 표시됩니다.

## 인증

모든 API 연결 유형은 여러 인증 방식을 지원합니다:

- **API 키** - 키 이름과 값을 지정하며, 헤더 또는 쿼리 매개변수로 전송됩니다
- **Bearer 토큰** - Authorization 헤더로 전송되는 OAuth 또는 JWT 토큰
- **기본 인증** - HTTP Basic Auth를 사용하는 사용자 이름과 비밀번호
- **인증 없음** - 공개 API용

인증은 연결 속성에서 구성합니다.

## 데이터 내보내기

API 응답 데이터는 표준 DbGate 내보내기 기능을 사용하여 다양한 형식으로 내보낼 수 있습니다:
- JSON
- CSV
- Excel
- SQL INSERT 문
- XML

표 형식 데이터 브라우저에서 표준 "Export" 컨텍스트 메뉴 옵션을 사용하세요.

## 여러 API 사용하기

여러 API와 데이터베이스에 대한 연결을 만들 수 있습니다. 여러 요청 탭을 열어 서로 다른 엔드포인트를 동시에 다룰 수 있습니다.

탭 상태는 앱을 닫았다가 다시 열어도 유지되며, 닫힌 탭 기록에서 요청을 다시 열 수 있습니다.
