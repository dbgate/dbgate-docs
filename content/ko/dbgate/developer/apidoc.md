---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: ko
layout: docs
title: API 문서
weight: 20
---

## Functions

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>reader를 writer로 복사합니다. 테이블 가져오기, 내보내기 및 테이블 간 데이터 전송에 사용됩니다</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>modelFolder에 저장된 데이터베이스 모델(YAML 형식의 테이블)을 데이터베이스에 배포합니다</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>모든 데이터베이스 객체를 삭제합니다</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>SQL 쿼리를 실행합니다</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>모델을 데이터베이스에 배포하기 위한 쿼리를 생성합니다</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>JSONL 파일 또는 URL을 읽는 reader 함수입니다. JSONL 형식 - 텍스트 파일이며, 각 줄은 JSON으로 인코딩된 행입니다.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 writer 객체를 반환합니다. 이 writer 객체는 데이터를 JSONL 파일에 씁니다. JSONL 형식 - 텍스트 파일이며, 각 줄은 JSON으로 인코딩된 행으로, 예를 들어 MongoDB에서 사용됩니다.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 JSON 파일 reader 객체를 생성합니다.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 writer 객체를 반환합니다. 이 writer 객체는 데이터를 JSON 파일에 씁니다.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 reader 객체를 반환합니다. 이 reader 객체는 쿼리에서 데이터를 읽습니다.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 reader 객체를 생성합니다. 이 reader 객체는 테이블 또는 뷰에서 데이터를 읽습니다.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 writer 객체를 생성합니다. 이 writer 객체는 데이터를 테이블에 씁니다. 테이블이 존재하지 않으면 생성할 수 있습니다.</p>
</dd>
</dl>

## Typedefs

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 Reader(입력) 객체</p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p><a href="#copyStream">copyStream</a> 함수를 위한 Writer(출력) 객체</p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>사용자 역할의 유형입니다.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
reader를 writer로 복사합니다. 테이블 가져오기, 내보내기 및 테이블 간 데이터 전송에 사용됩니다

**종류**: 전역 함수  

| Param | Type | Description |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | reader 객체 |
| output | [<code>writerType</code>](#writerType) | writer 객체 |
| options | <code>object</code> | 옵션 |

<a name="deployDb"></a>

## deployDb(options)
modelFolder에 저장된 데이터베이스 모델(YAML 형식의 테이블)을 데이터베이스에 배포합니다

**종류**: 전역 함수  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 연결 객체 |
| options.systemConnection | <code>object</code> | 시스템 연결(driver.connect의 결과). 제공되지 않으면 새 연결이 생성됩니다 |
| options.driver | <code>object</code> | 드라이버 객체. 제공되지 않으면 연결에서 로드됩니다 |
| options.analysedStructure | <code>object</code> | 데이터베이스의 분석된 구조. 제공되지 않으면 로드됩니다 |
| options.modelFolder | <code>string</code> | 모델 파일이 있는 폴더(테이블용 YAML 파일, 뷰·프로시저 등을 위한 SQL 파일) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | 로드된 데이터베이스 모델 - 배열로 로드된 YAML 및 SQL 파일의 모음 |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | 모델을 변환하기 위한 함수의 배열 |
| options.dbdiffOptionsExtra | <code>object</code> | dbdiff를 위한 추가 옵션 |
| options.ignoreNameRegex | <code>string</code> | 이름으로 객체를 무시하기 위한 정규식 |
| options.targetSchema | <code>string</code> | 배포 대상 스키마 |
| options.maxMissingTablesRatio | <code>number</code> | 데이터베이스에서 누락된 테이블의 최대 비율. 안전 검사이며, 누락 비율이 더 높으면 배포가 중단됩니다(모든 테이블이 실수로 삭제되는 것을 방지) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
모든 데이터베이스 객체를 삭제합니다

**종류**: 전역 함수  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 연결 객체 |
| options.systemConnection | <code>object</code> | 시스템 연결(driver.connect의 결과). 제공되지 않으면 새 연결이 생성됩니다 |
| options.driver | <code>object</code> | 드라이버 객체. 제공되지 않으면 연결에서 로드됩니다 |
| options.analysedStructure | <code>object</code> | 데이터베이스의 분석된 구조. 제공되지 않으면 로드됩니다 |

<a name="executeQuery"></a>

## executeQuery(options)
SQL 쿼리를 실행합니다

**종류**: 전역 함수  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | 연결 객체 |
| [options.systemConnection] | <code>object</code> | 시스템 연결(driver.connect의 결과). 제공되지 않으면 새 연결이 생성됩니다 |
| [options.driver] | <code>object</code> | 드라이버 객체. 제공되지 않으면 연결에서 로드됩니다 |
| [options.sql] | <code>string</code> | SQL 쿼리 |
| [options.sqlFile] | <code>string</code> | SQL 파일 |
| [options.logScriptItems] | <code>boolean</code> | 전체 스크립트 대신 스크립트 항목을 로깅할지 여부 |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
모델을 데이터베이스에 배포하기 위한 쿼리를 생성합니다

**종류**: 전역 함수  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 연결 객체 |
| options.systemConnection | <code>object</code> | 시스템 연결(driver.connect의 결과). 제공되지 않으면 새 연결이 생성됩니다 |
| options.driver | <code>object</code> | 드라이버 객체. 제공되지 않으면 연결에서 로드됩니다 |
| options.analysedStructure | <code>object</code> | 데이터베이스의 분석된 구조. 제공되지 않으면 로드됩니다 |
| options.modelFolder | <code>string</code> | 모델 파일이 있는 폴더(테이블용 YAML 파일, 뷰·프로시저 등을 위한 SQL 파일) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | 로드된 데이터베이스 모델 - 배열로 로드된 YAML 및 SQL 파일의 모음 |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | 모델을 변환하기 위한 함수의 배열 |
| options.dbdiffOptionsExtra | <code>object</code> | dbdiff를 위한 추가 옵션 |
| options.ignoreNameRegex | <code>string</code> | 이름으로 객체를 무시하기 위한 정규식 |
| options.targetSchema | <code>string</code> | 배포 대상 스키마 |
| options.maxMissingTablesRatio | <code>number</code> | 데이터베이스에서 누락된 테이블의 최대 비율. 안전 검사이며, 누락 비율이 더 높으면 배포가 중단됩니다(모든 테이블이 실수로 삭제되는 것을 방지) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
JSONL 파일 또는 URL을 읽는 reader 함수입니다. JSONL 형식 - 텍스트 파일이며, 각 줄은 JSON으로 인코딩된 행입니다.

**종류**: 전역 함수  
**반환값**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 객체  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | 파일 이름 또는 URL |
| options.encoding | <code>string</code> | 파일의 인코딩 |
| options.limitRows | <code>number</code> | 읽을 최대 행 수 |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
[copyStream](#copyStream) 함수를 위한 writer 객체를 반환합니다. 이 writer 객체는 데이터를 JSONL 파일에 씁니다. JSONL 형식 - 텍스트 파일이며, 각 줄은 JSON으로 인코딩된 행으로, 예를 들어 MongoDB에서 사용됩니다.

**종류**: 전역 함수  
**반환값**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - writer 객체  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | 파일 이름 |
| [options.encoding] | <code>string</code> | 파일의 인코딩 |
| [options.header] | <code>boolean</code> | 헤더를 쓸지 여부. 헤더는 원본 테이블 구조를 설명하는 JSON입니다. 헤더는 DbGate 고유의 것이므로, 예를 들어 MongoDB로 데이터를 가져오려는 경우에는 헤더를 쓰지 않아야 합니다. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
[copyStream](#copyStream) 함수를 위한 JSON 파일 reader 객체를 생성합니다.

**종류**: 전역 함수  
**반환값**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 객체  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | 파일 이름 또는 URL |
| options.jsonStyle | <code>string</code> | 'object' 또는 'array' |
| [options.keyField] | <code>string</code> | object 스타일을 위한 키 필드 |
| [options.rootField] | <code>string</code> | object 스타일을 위한 루트 필드 |
| [options.encoding] | <code>string</code> | 파일의 인코딩 |
| [options.limitRows] | <code>number</code> | 읽을 최대 행 수 |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
[copyStream](#copyStream) 함수를 위한 writer 객체를 반환합니다. 이 writer 객체는 데이터를 JSON 파일에 씁니다.

**종류**: 전역 함수  
**반환값**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - writer 객체  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | 파일 이름 |
| [options.jsonStyle] | <code>string</code> | 'object' 또는 'array' |
| [options.keyField] | <code>string</code> | object 스타일을 위한 키 필드 |
| [options.rootField] | <code>string</code> | object 스타일을 위한 루트 필드 |
| [options.encoding] | <code>string</code> | 파일의 인코딩 |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
[copyStream](#copyStream) 함수를 위한 reader 객체를 반환합니다. 이 reader 객체는 쿼리에서 데이터를 읽습니다.

**종류**: 전역 함수  
**반환값**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 객체  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 연결 객체 |
| options.query | <code>string</code> | SQL 쿼리 |
| [options.queryType] | <code>string</code> | 쿼리 유형 |
| [options.sql] | <code>string</code> | SQL 쿼리. 사용되지 않음(obsolete); 대신 query를 사용하세요 |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
[copyStream](#copyStream) 함수를 위한 reader 객체를 생성합니다. 이 reader 객체는 테이블 또는 뷰에서 데이터를 읽습니다.

**종류**: 전역 함수  
**반환값**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 객체  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 연결 객체 |
| options.systemConnection | <code>object</code> | 시스템 연결(driver.connect의 결과). 제공되지 않으면 새 연결이 생성됩니다 |
| options.pureName | <code>string</code> | 테이블 이름 |
| options.schemaName | <code>string</code> | 스키마 이름 |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
[copyStream](#copyStream) 함수를 위한 writer 객체를 생성합니다. 이 writer 객체는 데이터를 테이블에 씁니다. 테이블이 존재하지 않으면 생성할 수 있습니다.

**종류**: 전역 함수  
**반환값**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - writer 객체  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 연결 객체 |
| options.systemConnection | <code>object</code> | 시스템 연결(driver.connect의 결과). 제공되지 않으면 새 연결이 생성됩니다 |
| options.driver | <code>object</code> | 드라이버 객체. 제공되지 않으면 연결에서 로드됩니다 |
| options.pureName | <code>string</code> | 테이블 이름 |
| options.schemaName | <code>string</code> | 스키마 이름 |
| options.dropIfExists | <code>boolean</code> | 테이블이 존재하면 삭제 |
| options.truncate | <code>boolean</code> | 삽입 전에 테이블 비우기 |
| options.createIfNotExists | <code>boolean</code> | 테이블이 존재하지 않으면 생성 |
| options.commitAfterInsert | <code>boolean</code> | 삽입 후 트랜잭션 커밋 |

<a name="readerType"></a>

## readerType : <code>Object</code>
[copyStream](#copyStream) 함수를 위한 Reader(입력) 객체

**종류**: 전역 typedef  
<a name="writerType"></a>

## writerType : <code>Object</code>
[copyStream](#copyStream) 함수를 위한 Writer(출력) 객체

**종류**: 전역 typedef  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
데이터베이스 엔진 식별자이며, `engine@plugin-package` 형식입니다.

**종류**: 전역 typedef  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**종류**: 전역 typedef  
**속성**

| Name | Type |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 
