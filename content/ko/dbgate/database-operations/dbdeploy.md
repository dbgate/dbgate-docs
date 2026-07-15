---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: ko
title: 데이터베이스 배포
weight: 10
---

*배포 기능은 다음 릴리스에서 크게 변경될 예정이며, 이 문서는 최신 BETA 버전에 관한 것입니다*

DbGate는 자동 데이터베이스 배포 메커니즘을 제공합니다. 전통적인 방식은 마이그레이션 SQL 스크립트를 사용하지만, DbGate는 기본적으로 다른 방식을 사용합니다(마이그레이션 스크립트도 지원됩니다).
테이블 구조와 목록 데이터를 기술하는 YAML 파일, 그리고 뷰, 저장 프로시저, 함수를 기술하는 SQL 파일로 DB 모델을 정의합니다. 이 모델은 데이터베이스에 배포되며, 현재 구조와 모델의 구조를 비교하여 누락된 컬럼과 테이블을 생성하고 뷰 및 프로시저 정의를 업데이트합니다. **파괴적인 작업**(데이터 손실로 이어질 수 있는 작업)은 수행되지 않으므로, 모델에서 컬럼이나 테이블을 제거해도 데이터베이스에는 그대로 남아 있습니다. 모델에서 컬럼의 이름을 변경하면 새 이름의 컬럼이 생성되고 기존 컬럼은 데이터베이스에 남아 있습니다.

배포는 명령줄에서(node 스크립트를 사용하여) 또는 DbGate GUI에서 호출할 수 있습니다. 또한 DB 비교 기능을 사용하여 모델과 실제 데이터베이스의 차이를 시각적으로 비교할 수도 있습니다.

## 테이블 yaml 형식

```yaml
name: Album # table name 
columns:
  - name: AlbumId # column name 
    type: int # data type. is used directly in target SQL engine  
    autoIncrement: true # column is autoincrement 
    notNull: true # column is not nullable (default: is nullable) 
  - name: Title
    type: nvarchar(150)
    notNull: true
  - name: ArtistId
    type: int
    references: Artist # name of table. Is used for creating foreign key 
  - name: isDeleted
    type: bit
    notNull: true
    default: 0 # default value 
  - name: created
    type: timestamp
    default: current_timestamp
primaryKey:
  - AlbumId # list of primary key column names 
indexes:
  - name: UQ_AlbumTitleArtistId # index name 
    unique: true # whether index is unique. default=false 
    columns: # list of index columns 
      - Title
      - ArtistId
data: # static data (only for list tables) 
  - AlbumId: -1 # values for all columns, which should be filled 
    Title: Predefined static album
```

- 이름은 스키마 이름 없이 정의되며, 하나의 모델은 하나의 스키마를 기술합니다
- 기본값은 SQL 표현식으로 정의되므로, 문자열을 정의하려면 '작은따옴표'를 사용해야 합니다
- 테이블에 정적 데이터를 정의할 수 있습니다

### 마이그레이션 스크립트 사용
보다 전통적인 마이그레이션 스크립트를 DbGate 고유의 배포 관리와 결합할 수 있으며, 일부 특수한 객체는 마이그레이션 스크립트로 생성할 수 있습니다.
스크립트 유형은 파일 확장자로 결정되며, 디렉터리 구조는 사용자의 선택에 따르고 DbGate는 이에 영향을 받지 않습니다.

지원되는 스크립트 확장자는 다음과 같습니다:
- `*.predeploy.sql` - 모든 배포 프로세스 전에 실행되는 스크립트
- `*.install.sql` - 이전 배포와 다른 경우에만 실행되는 스크립트
- `*.uninstall.sql` - 이 스크립트는 `.install.sql` 파일과 짝을 이루며, 새 버전의 `*.install.sql` 파일이 실행되기 전에 실행됩니다
- `*.once.sql` - 한 번만 실행되는 스크립트
- `*.postdeploy.sql` - 모든 배포 프로세스 전에 실행되는 스크립트

DbGate는 데이터베이스에 배포된 배포 스크립트를 추적하기 위해 `dbgate_deploy_journal` 테이블을 사용합니다. 이 테이블은 마이그레이션 스크립트가 하나 이상 포함된 프로젝트를 배포할 때 자동으로 생성됩니다.


### DbGate GUI에서 사용하기

- 연결에서 데이터베이스 컨텍스트 메뉴를 열고 "Export DB model"을 선택합니다(Premium 전용). DB 모델은 디렉터리 또는 파일로 저장됩니다. 배포 기능을 사용할 계획이라면 Data archive 또는 Folder (YAML + SQL) 대상을 선택하세요.
- 아카이브 위젯을 열면 다운로드된 모델이 보일 것입니다
- 모델 컨텍스트 메뉴에서 모델과 관련된 몇 가지 작업을 수행할 수 있습니다:
    - Generate deploy DB SQL - 현재 데이터베이스(상태 표시줄에서 확인할 수 있습니다)와 비교하여 모델의 변경 사항을 현재 데이터베이스에 배포하는 SQL 스크립트를 생성합니다
    - Shell: Deploy DB - DB 배포에 사용할 수 있는 JavaScript 셸을 생성합니다
    - Compare with {current database} - 현재 데이터베이스와 모델을 그래픽으로 비교합니다(Premium 전용)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### 명령줄에서 사용하기
다음 스크립트를 deploy.js 파일에 복사하고 데이터베이스 구성을 업데이트하세요. 또한 모델 폴더 위치에 맞게 modelFolder를 변경해야 합니다.
이 스크립트를 실행하려면 컴퓨터에 [NodeJs](https://nodejs.org/)가 설치되어 있어야 합니다.

```js
const path = require('path');
const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginPostgres = require('dbgate-plugin-postgres');
dbgateApi.registerPlugins(dbgatePluginPostgres);

async function run() {
	await dbgateApi.deployDb({
		connection: {
			server: process.env.DB_SERVER || 'localhost',
			engine: 'postgres@dbgate-plugin-postgres',
			password: process.env.DB_PASSWORD || 'test',
			user: process.env.DB_USER || 'postgres',
			port: process.env.DB_PORT || 5432,
			database: process.env.DB_NAME || 'my_database',
		},
		modelFolder: path.join(__dirname, 'database'),
	});
	await dbgateApi.finalizer.run();
	console.log('Finished job script');
}
dbgateApi.runScript(run);
```

그런 다음 deploy.js가 있는 디렉터리에서 명령을 실행하여 필요한 모듈을 설치합니다:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

다음 명령을 실행하여 데이터베이스 배포를 수행합니다:
```sh
node deploy.js
```

이 스크립트는 PostgreSQL용이며, 다른 데이터베이스 엔진에서는 드라이버를 변경해야 합니다.

이 스크립트는 DbGate GUI에서 자동으로 생성할 수도 있습니다. 아카이브 폴더의 "Shell: Deploy DB" 컨텍스트 메뉴를 사용한 다음, 생성된 스크립트에서 "Copy nodejs script"를 선택하면 유효한 스크립트가 복사됩니다. require 명령에서 사용되는 모든 패키지는 npm install로 설치되어야 합니다.
