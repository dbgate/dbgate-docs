---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: ko
title: 플러그인 개발
weight: 30
---

DbGate는 플러그인 생성을 지원합니다. 플러그인 마법사 덕분에 기본 플러그인을 만드는 것은 매우 간단합니다. DbGate 플러그인은 NPM(JavaScript) 패키지이며, 의존성을 가질 수 있습니다. (단, 네이티브 의존성은 제외)

현재 3가지 유형의 플러그인이 있습니다:
- 테마 플러그인
- 파일 형식 플러그인
- 데이터베이스 드라이버 플러그인

## 사전 요구 사항 설치
[node.js](https://nodejs.org)가 설치되어 있어야 합니다.

또한 [Yeoman](https://yeoman.io/)과 yeoman [DbGate 플러그인 제너레이터](https://www.npmjs.com/package/generator-dbgate)가 필요합니다:

```sh
npm install -g yo
npm install -g generator-dbgate
```

## 플러그인 생성
콘솔에서 다음 명령을 실행하세요:

```sh
yo dbgate
```

3가지 질문에 답해야 합니다:
- 플러그인 이름. 반드시 dbgate-plugin- 으로 시작해야 합니다. 예: dbgate-plugin-myplugin
- 플러그인 유형. 예를 들어 "Database driver"를 선택합니다.
- 패키지 관리자. npm 또는 yarn 중 원하는 것을 선택합니다. DbGate는 yarn을 사용합니다.

## 플러그인 편집 및 테스트
편집기를 여세요. 권장 옵션은 [Visual Studio Code](https://code.visualstudio.com/)입니다.
테마 플러그인은 단 하나의 소스 파일 src/index.js만 포함합니다. 원하는 대로 테마 색상을 수정할 수 있습니다. themeName 속성은 DbGate 테마 선택기에 표시되는 이름입니다.

새 테마를 확인하려면 (플러그인 디렉터리에서) 콘솔에서 다음을 실행하세요:
```sh
yarn plugin
```
npm을 사용하는 경우에는 다음과 같습니다:
```sh
npm run plugin
```
이 명령은 로컬에 설치된 DbGate 인스턴스에 플러그인을 설치합니다(변경한 경우에는 업데이트합니다). DbGate를 재시작하면 새 테마가 보일 것입니다.
재시작은 필수가 아니며, "yarn plugin" 실행 후 새 플러그인 버전을 사용하려면 앱을 다시 로드(메뉴 View/Reload)하는 것만으로 충분합니다.

## 플러그인 제거
DbGate 플러그인 위젯에서 플러그인을 제거할 수 있습니다. 또는 다음 명령을 사용할 수 있습니다:
```sh
yarn plugout
```

## 플러그인 게시
플러그인은 일반적인 NPM 패키지이므로 NPM 저장소에 게시할 수 있습니다. 게시 후에는 모든 DbGate 사용자가 "Plugins" 위젯에서 사용할 수 있습니다.

## 플러그인 아이콘
각 플러그인은 확장 목록에서 아이콘으로 표시됩니다. NPM은 NPM 패키지의 아이콘을 지원하지 않으므로, 아이콘은 package.json 파일의 description 필드에 다음 구문으로 넣을 수 있습니다:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

yeoman 제너레이터를 사용하면 이 부분을 조금 도와줍니다.

## 데이터베이스 드라이버 플러그인 생성
드라이버 플러그인 생성은 앞의 과정과 매우 유사하며, "Database driver plugin"을 선택하기만 하면 됩니다. `yarn plugin` 이후에는 새 드라이버를 사용하여 연결을 정의하고 더미 데이터베이스 목록과 테이블 목록을 볼 수 있어야 합니다.

기본 기능을 갖춘 간단한 드라이버는 매우 빠르게 만들 수 있으며, 더 복잡한 기능은 나중에 구현할 수 있습니다.

드라이버 생성은 다음 단계로 구성될 수 있습니다:
* 적절한 nodejs 패키지(드라이버)를 찾습니다. 가능하면 순수 JavaScript 패키지를 선택하세요. 네이티브 패키지는 큰 어려움을 초래합니다. 해당 네이티브 패키지를 DbGate 배포판에 추가해야 하며, 플랫폼마다 빌드 문제가 발생할 수 있습니다. 반면 순수 JavaScript 패키지는 DbGate를 변경할 필요 없이 모든 플랫폼에서 문제없이 정상적으로 동작합니다.
* frontend/driver.js의 showConnectionField 함수에서 연결을 위한 필드를 정의합니다.
* backend/driver.js에서 connect 함수를 구현합니다.
* backend/driver.js에서 getVersion 함수를 구현합니다(선택 사항이지만, 구현하면 연결 탭의 "Test" 버튼으로 연결을 테스트할 수 있습니다).
* backend/Analyser.js 클래스에서 _rynAnalysis 메서드를 구현합니다. 이 메서드는 데이터베이스 구조를 반환해야 합니다.
* backend/driver.js에서 query 메서드를 구현합니다. 이후에는 테이블 목록을 보고 테이블 데이터를 탐색할 수 있어야 합니다.
* 나머지 메서드를 구현합니다. 다른 드라이버 플러그인을 참고하세요. 가장 대표적인 플러그인은 아마도 PostgreSQL 플러그인일 것입니다. https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
