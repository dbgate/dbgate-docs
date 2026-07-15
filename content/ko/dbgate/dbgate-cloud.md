---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: ko
title: DbGate Cloud
weight: 80
---

DbGate cloud는 연결, SQL 스크립트 및 기타 객체를 위한 온라인 저장소입니다. 또한 유용한 SQL 스크립트를 모아 놓은 공개 지식 베이스를 제공합니다.

> DbGate Cloud는 **데스크톱** DbGate 앱을 위한 저장소 도우미입니다(연결, SQL 스크립트, 공유 폴더). 호스팅되는 브라우저 전용 앱을 찾고 계신가요? [DbGate Central](/ko/dbgate-central/)을 참조하세요.

## 로그인
DbGate cloud를 사용하려면 로그인해야 합니다. 왼쪽 패널의 {{< mdi "account-remove-outline" >}} 아이콘을 사용하세요.

클라우드 저장소는 항상 사용자의 이메일 주소와 연결됩니다.  
다음 인증 공급자 중 하나를 선택할 수 있습니다:
* GMail
* GitHub
* 이메일 - 일회용 로그인 매직 링크가 이메일로 전송됩니다

DbGate 서버는 사용자의 비밀번호를 저장하지 않습니다.

## 클라우드에 저장된 연결 사용하기
로그인하면 클라우드 콘텐츠가 {{< mdi "cloud-key" >}} 위젯 아래에 표시됩니다. 기본적으로 Private 폴더(쓰기 권한 포함)가 보입니다.

연결을 클라우드에 저장하기:
* 연결 컨텍스트 메뉴에서 "Copy to cloud folder"를 선택합니다
* {{<mdi "plus-thick" >}}를 클릭한 다음 "Add connection on cloud"를 선택합니다

## 어떤 연결이 클라우드에 저장되나요?
* 클라우드 연결은 항상 {{< mdi "cloud-key" >}} 위젯 아래에 있습니다
* 로컬에 저장된 연결은 {{< mdi "database" >}} 위젯 아래에 있습니다

## 폴더 작업
Private 폴더 외에 추가 폴더를 만들 수 있습니다(Premium 에디션 필요).

{{<mdi "plus-thick" >}} 버튼 아래에 다음 명령이 있습니다:
* New shared folder - 새 공유 폴더를 만듭니다. 기본적으로 본인만 접근할 수 있으며, 다른 사용자를 초대할 수 있습니다
* Add existing shared folder - 다른 사용자가 만든 공유 폴더의 초대 링크가 있다면 여기에서 사용합니다

폴더를 다른 사람과 공유하려면 폴더를 마우스 오른쪽 버튼으로 클릭하고 "Copy invite link"를 선택하세요.

## 공유 폴더 권한
* Admin - 폴더에 대한 모든 권한을 가지며, 다른 사람을 초대하고 콘텐츠를 작성할 수 있습니다
* Write - 콘텐츠를 작성/삭제할 수 있지만, 다른 사람을 초대할 수는 없습니다
* Read - 폴더의 콘텐츠를 읽기만 할 수 있습니다. 이 권한은 서버로 정의된 연결 내부에서 사용 가능한 데이터베이스에는 적용되지 않는다는 점에 유의하세요

## Community 에디션의 공유 폴더
Community 에디션에서는 Premium 사용자가 만든 공유 폴더를 사용할 수 있지만, 자신의 공유 폴더를 만들 수는 없습니다. 이는 Premium 에디션을 사용하는 팀이 Community 에디션을 사용하는 다른 팀원과 연결, SQL 파일 및 ER 다이어그램을 공유할 수 있도록 하기 위한 것입니다.

## 공개 지식 베이스
공개 지식 베이스는 SQL 성능 튜닝, 교착 상태 분석, 인덱스 사용량 등과 같은 작업에 유용한 SQL 스크립트와 차트를 모아 놓은 것입니다. 지식 베이스는 모든 에디션에서 사용할 수 있지만, 차트는 Premium 에디션에서만 사용할 수 있습니다.

왼쪽 위젯 패널의 {{< mdi "cloud-search" >}} 아이콘 아래에서 모든 항목을 볼 수 있습니다.  
회색으로 표시된 스크립트는 현재 선택된 데이터베이스와 호환되지 않는 스크립트를 나타냅니다.

지식 베이스를 자신의 SQL 스크립트로 보강하고 싶다면, [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base) GIT 저장소에 풀 리퀘스트를 생성해 주세요.

지식 베이스의 스크립트는 [SQL front matter](/ko/dbgate/developer/sql-front-matter) 구문으로 주석 처리되어 있습니다

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)

