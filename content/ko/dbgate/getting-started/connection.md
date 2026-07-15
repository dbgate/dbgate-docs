---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: ko
title: 연결
weight: 20
---

DbGate에서 데이터베이스에 연결하는 것은 간단합니다. 다음과 같은 몇 가지 방법으로 데이터베이스에 연결할 수 있습니다:

* 메뉴 File/Add Connection 또는 CONNECTIONS 위젯의 {{< mdi "plus-thick" >}} 아이콘
* 메뉴 File/New SQLite database - 새 SQLite 데이터베이스를 만듭니다
* 메뉴 File/Open - 기존 SQLite 데이터베이스를 열 수 있습니다

## 연결 화면
![연결 화면](https://media.dbgate.io/img/new-connection-light.png)

연결 화면의 필드는 연결 유형에 따라 크게 달라집니다.

몇 가지 공통 필드:

* Server - 데이터베이스 서버의 호스트 이름
* Port - 포트, 데이터베이스 기본 포트를 사용하는 경우 비워 둘 수 있습니다
* User, Password - 인증
* Password mode
    * Save and encrypt - 비밀번호가 암호화되어 저장되며, 다음에 확인할 수 없습니다
    * Save RAW - 비밀번호가 그대로(암호화 없이) 저장되며, 나중에 확인할 수 있습니다
    * Don't save, ask for password - 비밀번호가 저장되지 않으며, 연결할 때 입력해야 합니다
    * Don't save, ask for login and password - 비밀번호와 로그인 모두 저장되지 않으며, 연결할 때 둘 다 입력해야 합니다
* Is read only - 연결이 읽기 전용이 됩니다(읽기 전용 세션을 지원하지 않는 엔진의 경우, 이때는 SQL 쿼리를 실행할 수 없습니다)
* Default database - 연결 후 활성화될 데이터베이스
* Use only database *&lt;default database&gt;* - 선택하면 연결 트리에 기본 데이터베이스만 표시됩니다(서버의 다른 데이터베이스는 숨겨집니다)
* Display name - 애플리케이션에 연결이 표시될 이름

## SSH 터널
여기에서 SSH 터널을 통한 연결을 구성할 수 있습니다. 

공통 필드:
* Use SSH tunnel - SSH 터널을 사용하려면 선택합니다
* Host - SSH 서버 호스트 이름

![DbGate - SSH 터널 구성](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
SSL 연결을 구성합니다.

공통 필드:
* Use SSL - SSL을 사용하려면 선택합니다. 대부분의 경우 SSL을 사용하기 위해 구성해야 하는 것은 이것뿐입니다

![DbGate - SSL 연결 구성](https://media.dbgate.io/img/connection-ssl-window-light.png)
