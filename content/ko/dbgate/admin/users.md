---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: ko
title: 사용자
weight: 30
---

## 사용자 탭
사용자, 비밀번호, 사용자 권한 및 사용자-연결 매핑을 구성합니다.
비밀번호는 "로컬" 인증 방식에만 사용됩니다. 하지만 외부 ID 공급자를 사용하는 모든 방식도 사용자 조회를 수행하므로, 외부에서 인증된 사용자에 대해서도 해당 사용자가 사용할 수 있는 권한과 연결을 구성할 수 있습니다. 

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### 사용자 상세 탭
* 정보
  * 사용자 권한 구성
  * 이 사용자에게 할당된 역할 구성
* 팀 파일 - [팀 파일](team-files)에 대한 접근 권한 구성
* 연결 - 이 사용자에게 할당된 연결 구성
* 데이터베이스 - 이 사용자에 대한 [데이터베이스 권한](permissions#database-permissions) 구성
* 테이블/뷰/객체 - 이 사용자에 대한 [테이블 권한](permissions#table-permissions) 구성
* 디스크 파일 - 디스크/docker 볼륨의 파일에 대한 접근 권한 구성
