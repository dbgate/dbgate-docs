---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: ko
title: 내보내기 및 가져오기
weight: 20
---

DbGate는 간단한 원클릭 내보내기부터 복잡한 사용자 지정 설정까지 모두 지원하는 유연한 내보내기/가져오기 시스템을 갖추고 있습니다.

## 간단한 원클릭 내보내기

별도의 설정이 필요 없이 데이터를 파일로 내보내기만 하면 되는 경우에는 간단한 내보내기를 사용할 수 있습니다. 간단한 내보내기를 실행하는 방법은 여러 가지가 있습니다.
- 테이블/뷰/컬렉션 컨텍스트 메뉴의 내보내기
- 테이블 데이터의 "Export" 컨텍스트 메뉴 또는 {{<mdi "export" >}} 버튼. 필터도 내보내는 데이터에 적용됩니다
- 쿼리 결과의 "Export" 컨텍스트 메뉴 또는 {{<mdi "export" >}} 버튼

데스크톱 애플리케이션에서는 내보낸 파일을 바로 저장할 수 있습니다.

웹 앱에서는 내보낸 파일이 다운로드로 제공됩니다.

## 고급 내보내기/가져오기
더 자세한 설정이 필요하거나 한 번에 여러 테이블을 내보내야 하는 경우에는 "고급 내보내기"를 사용해야 합니다.  
가져오기에도 동일한 설정 도구가 사용되며, 원본과 대상 설정만 서로 바뀝니다.

고급 내보내기/가져오기는 다음 위치에서 실행할 수 있습니다.
- 간단한 내보내기와 동일한 위치에서 파일 형식 대신 "Export advanced..."를 선택
- 데이터베이스 컨텍스트 메뉴에서 "Export" 또는 "Import"를 선택


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} 원본 설정
* 저장소 유형 - 데이터의 원본을 선택합니다
  * 데이터베이스 - 이 경우 "내보내기"를 설정합니다
    * 여러 원본 테이블을 선택합니다
  * 파일 (JSON, CSV, DBF...) - 이 경우 "가져오기"를 설정합니다
    * 원본 파일을 열거나 끌어다 놓습니다
  * 쿼리 - 대부분의 경우에는 필요하지 않지만, 여기에 쿼리를 직접 입력할 수 있습니다. 이 옵션은 예를 들어 필터링된 테이블 데이터를 내보낼 때 내부적으로 사용됩니다.
  * 아카이브 - [데이터 아카이브](advanced-data-tools/archives)에서 데이터를 가져오거나 내보냅니다

### {{<mdi "export" >}} 대상 설정
* 저장소 유형 - 원본 설정과 동일하지만 의미가 반대입니다
  * 데이터베이스 - "가져오기"를 설정합니다
  * 파일 (JSON, CSV, DBF...) - "내보내기"를 설정합니다

### {{< mdi "table-multiple" >}} 원본 테이블/파일 매핑
입력 파일/테이블이 출력으로 어떻게 변환되는지 매핑할 수 있습니다

### 작업 버튼
  * {{< mdi "play" >}} 실행 - 정의된 가져오기/내보내기 작업을 실행합니다
  * {{< mdi "flash" >}} 스크립트 생성 - 정의된 작업을 실행하는 JavaScript 코드를 만듭니다. DbGate 셸 콘솔에서 실행하거나, 파일로 내보내 명령줄에서 nodejs로 실행할 수 있습니다
  * {{< mdi "content-save" >}} 저장 - 나중을 위해 작업을 저장합니다

## 가져오기 / 내보내기 스크립트
DbGate의 모든 가져오기/내보내기 작업은 먼저 스크립트로 변환됩니다. 다음은 SQLite 테이블을 CSV로 내보내는 예시입니다.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

이 스크립트는 DbGate 없이도 실행할 수 있습니다. 스크립트 편집기의 컨텍스트 메뉴에서 "Copy nodejs script"를 사용하세요. 다음 스크립트가 복사됩니다.

```js

const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginSqlite = require('dbgate-plugin-sqlite');
const dbgatePluginCsv = require('dbgate-plugin-csv');
dbgateApi.registerPlugins(dbgatePluginSqlite,dbgatePluginCsv);

require=null;
async function run() {

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);


await dbgateApi.finalizer.run();
console.log('Finished job script');
}
dbgateApi.runScript(run);
```

스크립트가 있는 폴더에 사용된 의존성(require() 함수에서 사용된 모든 패키지)을 설치한 후:

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

다음 명령으로 스크립트를 실행할 수 있습니다.

```sh
node myExportScript.js
```
