---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: ko
title: AI 에이전트를 위한 MCP 서버
weight: 50
---

DbGate Central은 워크스페이스를 [Claude](https://claude.ai)와 같은 AI 어시스턴트에 원격 **MCP(Model Context Protocol)** 커넥터로 노출할 수 있습니다. 따라서 에이전트는 여러분과 동일한 방식으로 API를 탐색하고 쿼리할 수 있으며, 그 접근 권한은 여러분이 계속 통제합니다.

## 설정 방법

1. **Settings** 탭을 열고 **MCP 프로필**을 만듭니다. 해당 프로필의 **Server URL**(`https://central.dbgate.cloud/mcp/{profileId}`), **Client ID** 및 **Client Secret**을 복사합니다.
2. claude.ai(또는 다른 MCP 호환 클라이언트)에서 해당 URL과 OAuth 자격 증명을 사용하여 사용자 지정 커넥터를 추가합니다.
3. 각 연결의 편집기에서 **MCP access** 수준을 **No access**, **Read-only** 또는 **Writable** 중에서 설정합니다. 기본값은 접근 불가이므로, 허용하기 전까지는 아무것도 공유되지 않습니다.
4. 어시스턴트가 OAuth 핸드셰이크를 수행하고 여러분이 동의하면, 커넥터가 해당 프로필 및 워크스페이스에 바인딩됩니다.

각 워크스페이스는 여러 개의 MCP 프로필을 가질 수 있으며, 각 프로필은 고유한 URL, 자격 증명 및 연결별 권한을 갖습니다. 인증에는 필수 PKCE가 적용된 OAuth 2.1이 사용되며, 클라이언트 시크릿은 저장 시 암호화됩니다.

## 에이전트가 할 수 있는 일

**oData**, **GraphQL** 및 **Shopify** 연결에서 사용할 수 있습니다(SQLite/DuckDB는 브라우저 전용이므로 MCP 대상에서 제외됩니다).

* 프로필이 사용할 수 있는 **연결 목록 조회**.
* **엔터티 목록 조회** - 테이블, 뷰 또는 카탈로그 엔터티.
* **스키마 확인** - 컬럼 이름과 타입.
* **행 쿼리** - 데이터 필터링, 페이징 및 선택.
* **행 업데이트** - Shopify 전용이며, Writable 접근 권한을 부여한 경우에만 가능합니다.

읽기와 쓰기는 그리드 및 스케줄러와 동일한 엔진을 재사용하므로, 에이전트는 여러분이 보는 것과 정확히 동일한 데이터와 기능을 보게 되며 여러분이 부여한 접근 권한 이상은 결코 얻지 못합니다.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
