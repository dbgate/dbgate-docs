---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: ko
title: 역할
weight: 40
---

## 역할 탭
역할, 역할 권한 및 역할-연결 매핑을 구성합니다. 사용자 지정 역할을 만들고 사용자를 해당 역할에 할당하여, 이 역할에 할당된 모든 사용자 간에 권한과 연결된 커넥션을 공유할 수 있습니다.

미리 정의된 역할이 몇 가지 있습니다:
- superadmin - 관리자 페이지(https://your_dbgate_instance/admin.html)에 사용되는 역할
- logged-user - 로그인한 모든 사용자에 사용되는 역할입니다. 특정 사용자에 대해 권한을 재정의할 수 있습니다
- anonymous-user - "Anonymous" 인증 방식으로 로그인한 사용자에 사용되는 역할

![Role administration - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### 역할 상세 탭
* Info
  * 역할 권한 구성
  * 이 역할에 할당된 사용자 구성
* Team files - [팀 파일](team-files)에 대한 접근 권한 구성
* Connections - 이 역할에 할당된 커넥션 구성
* Databases - 이 역할에 대한 [데이터베이스 권한](permissions#database-permissions) 구성
* Tables/views/objects - 이 역할에 대한 [테이블 권한](permissions#table-permissions) 구성
* Disk files - 디스크/도커 볼륨의 파일에 대한 접근 권한 구성
