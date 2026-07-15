---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: ko
title: 스크립팅
weight: 40
---

DbGate는 여러 [NPM 패키지](https://www.npmjs.com/search?q=keywords%3Adbgate)로 구성되어 있으며, 이 패키지들은 nodejs 스크립트에서 사용할 수 있습니다

일반적으로 다음 패키지들이 필요합니다:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - 유틸리티 함수를 구현합니다
* dbgate-plugin-`engine` - 커넥터 플러그인 모음으로, 데이터베이스 연결 및 특정 데이터베이스 엔진에 고유한 작업을 구현합니다
* dbgate-plugin-`fileformat` - CSV 또는 XML로 내보내기를 사용하는 경우, 이러한 형식 제공자는 외부 플러그인으로 구현되어 있습니다

[API 문서](/ko/dbgate/developer/apidoc)

## DbGate에서 스크립트 생성하기
DbGate의 많은 기능은 내부적으로 스크립팅 인터페이스로 구현되어 있습니다. 따라서 내보내기와 유사한 작업을 사용할 때, 어딘가에 "Generate Shell script" 버튼이 있으며 이 버튼이 nodejs 스크립트를 생성해 줍니다.

내보내기에 nodejs 스크립트를 사용하려면 다음 단계를 따르면 됩니다:
* 테이블을 마우스 오른쪽 버튼으로 클릭하고 "Export/Export advanced"를 선택합니다
* 내보내기를 구성합니다
* 하단 툴바에서 "Generate script"를 선택합니다. 이제 JS 스크립트를 편집하고 DbGate 안에서 실행할 수 있습니다
* 하단 툴바에서 "Copy nodejs script"를 선택하면, 이를 js 파일로 저장한 후 컴퓨터에 설치된 [nodejs](https://nodejs.org/)로 실행할 수 있습니다


## 예제 1 - 테이블을 CSV로 내보내기
이것은 간단한 예제로, `dbgateApi` 패키지의 [tableReader](https://dbgate.org/docs/apidoc.html#tableReader)와 `dbgate-plugin-csv`의 writer를 사용합니다. 또한 엔진 매개변수 `mysql@dbgate-plugin-mysql`을 사용하기 때문에 `dbgate-plugin-mysql`도 필요합니다
```js
const dbgateApi = require('dbgate-api');
const dbgatePluginMysql = require("dbgate-plugin-mysql");
const dbgatePluginCsv = require("dbgate-plugin-csv");

dbgateApi.registerPlugins(dbgatePluginMysql);

async function run() {
  const reader = await dbgateApi.tableReader({
    connection: { server: 'localhost', engine: 'mysql@dbgate-plugin-mysql', user: 'root', password: 'xxxx', database: 'Chinook' },
    pureName: 'Customer',
  });
  const writer = await dbgatePluginCsv.shellApi.writer({ fileName: 'Customer.csv' });
  await dbgateApi.copyStream(reader, writer);

  console.log('Finished job script');
}
dbgateApi.runScript(run);
```