---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: ko
title: API 엔드포인트에 연결하기
weight: 10
---

DbGate Central은 세 가지 계열의 API 엔드포인트에 연결하며, 모든 연결에 동일한 새 연결 대화 상자를 사용합니다.

## 지원되는 엔드포인트 유형

* **GraphQL** - 스키마를 인트로스펙션하고, 타입을 탐색하며, 모든 GraphQL API에 대해 쿼리를 실행합니다.
* **oData** - oData V4 서비스를 일반 테이블처럼 다룹니다.
* **Shopify** - Shopify Admin API를 통해 스토어에 연결하여 제품, 주문, 고객, 메타필드 등을 살펴봅니다.

## 연결 만들기

**새 연결** 대화 상자를 열고, 연결 유형을 선택한 다음, 서비스 URL을 입력하고 인증 방식을 선택하세요:

* **None** - 개방된 공개 엔드포인트용입니다.
* **Basic** - 사용자 이름과 비밀번호입니다.
* **Bearer token** - 액세스 토큰을 붙여넣습니다.
* **API key** - 헤더 또는 쿼리 매개변수로 키를 전송합니다.

연결은 워크스페이스에 저장되므로, 다음에 어떤 기기에서 로그인하더라도 로컬에서 아무것도 설정할 필요 없이 그대로 사용할 수 있습니다.

![DbGate Central - API 엔드포인트에 연결](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
