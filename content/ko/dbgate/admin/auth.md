---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: ko
title: 인증
weight: 10
---

## 인증 탭
여러 가지 인증 방법이 있습니다. 사용자는 로그인 페이지에서 인증 방법을 선택합니다. 인증 방법이 하나만 활성화되어 있고 그 인증 방법이 로그인 페이지를 필요로 하지 않는 경우, 로그인 페이지는 건너뜁니다.

![Authentication administration - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- 로컬 인증 방법 - 저장소 데이터베이스의 사용자 목록("Users" 탭에서 구성)에서 사용자를 선택합니다
- 익명(Anonymous) - 자격 증명이 필요하지 않으며, 사용자는 "anonymous-user" 역할의 권한을 갖습니다
- 데이터베이스 로그인 사용 - 자격 증명이 데이터베이스 서버로 전달됩니다. 사용자는 "Connections" 탭에서 연결을 선택합니다
- OAuth 2.0 - 일반 OAuth 공급자입니다. 약간의 노력과 적절한 지식이 있으면 Google, Facebook, Keycloak 등 대부분의 최신 ID 공급자와 함께 구성할 수 있습니다
- Active Directory - LDAP 프로토콜을 통한 AD 접근
- Microsoft Entra - 이전의 Azure Active Directory - Azure 데이터베이스에 대한 통합 인증(SSO) 접근

### "정의된 로그인만 허용" 옵션
외부 ID 공급자를 사용하는 경우, 사용자가 DbGate 저장소 데이터베이스에 존재하지 않아도 됩니다. 이 확인란을 선택하면 저장소 데이터베이스에서 찾을 수 없는 사용자는 로그인할 수 없습니다

### Keycloak

Keycloak은 일반 OAuth 2.0 공급자를 사용하여 DbGate와 통합할 수 있습니다. Keycloak 인증을 구성하려면 다음이 필요합니다:

1. Keycloak realm에서 새 클라이언트 만들기
2. 클라이언트 설정 구성하기
3. 다음 매개변수로 DbGate에서 OAuth 2.0 공급자 설정하기:

**필수 구성:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: Keycloak 클라이언트 ID
- **OAuth login field**: 사용자의 로그인 식별자가 포함된 Keycloak 클레임(일반적으로 `preferred_username`이며, Keycloak 구성에 따라 `given_name`, `email` 또는 다른 적절한 클레임을 사용할 수도 있습니다)

**Keycloak 클라이언트 구성:**
- 유효한 리디렉션 URI: `https://dbgate.company.com/`

DbGate가 OAuth 공급자로부터 기대하는 필수 클레임(email, name, username)을 제공할 수 있도록 Keycloak 사용자 속성이 올바르게 매핑되어 있는지 확인하세요.


