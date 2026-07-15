---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: ko
title: 관리
weight: 60
---

관리 인터페이스를 사용하면 팀이 DbGate를 공유형 다중 사용자 웹 애플리케이션으로 운영할 수 있습니다. 연결을 중앙에서 관리하고, 누가 어떤 방식으로 로그인할 수 있는지 정의하며, 사용자, 역할 및 권한을 통해 데이터베이스와 객체에 대한 세분화된 접근 권한을 부여할 수 있습니다. 또한 공유 팀 파일도 여기에서 호스팅됩니다. 여기에서 구성한 모든 내용은 로컬 파일이 아니라 스토리지 데이터베이스에 저장됩니다.

관리 도구는 Team Premium 에디션에서만 사용할 수 있습니다. Community 에디션에서는 [환경 변수](/ko/dbgate/customization/env-variables)를 사용하여 DbGate를 구성하십시오.

관리에서 설정한 모든 구성은 스토리지 데이터베이스에 저장됩니다 - [STORAGE_xxx 환경 변수](/ko/dbgate/customization/env-variables/#team-premium-edition-configuration)를 사용하여 구성하십시오.

이 섹션의 내용:

* [인증](auth) - 로그인 방법 및 ID 공급자 구성
* [연결](connection) - 팀에서 사용할 수 있는 연결 관리
* [팀 파일](team-files) - SQL 스크립트, ER 다이어그램 및 차트 공유
* [사용자](users) - 사용자 계정 관리
* [역할](roles) - 권한을 역할로 그룹화
* [권한](permissions) - 연결, 데이터베이스 및 테이블에 대한 접근 권한 부여

## 관리자 접근

관리 페이지는 https://your_dbgate_instance/admin.html URL에서 사용할 수 있습니다. 

루트 관리자에게는 비밀번호가 정의되어 있어야 합니다. ADMIN_PASSWORD 환경 변수를 설정할 수 있습니다. 이 변수가 정의되어 있지 않으면 DbGate가 처음에 관리자 비밀번호를 묻습니다.

이후 다른 인증 방법을 사용하는 다른 사용자에게 관리 권한을 추가할 수 있지만, 우선 이 관리 페이지를 열어야 합니다.

