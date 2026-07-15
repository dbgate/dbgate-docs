---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: zh
layout: docs
title: API 文档
weight: 20
---

## 函数

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>将 reader 复制到 writer。用于导入、导出表以及在表之间传输数据</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>将存储在 modelFolder 中的数据库模型（表以 yaml 格式保存）部署到数据库</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>删除所有数据库对象</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>执行 SQL 查询</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>生成用于将模型部署到数据库的查询</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Reader 函数，用于读取 JSNOL 文件或 URL。JSONL 格式 - 文本文件，每一行都是一个 JSON 编码的行数据。</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>返回供 <a href="#copyStream">copyStream</a> 函数使用的 writer 对象。该 writer 对象将数据写入 JSONL 文件。JSONL 格式 - 文本文件，每一行都是一个 JSON 编码的行数据，例如 MongoDB 使用该格式。</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>为 JSON 文件创建供 <a href="#copyStream">copyStream</a> 函数使用的 reader 对象。</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>返回供 <a href="#copyStream">copyStream</a> 函数使用的 writer 对象。该 writer 对象将数据写入 JSON 文件。</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>返回供 <a href="#copyStream">copyStream</a> 函数使用的 reader 对象。该 reader 对象从查询中读取数据。</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>创建供 <a href="#copyStream">copyStream</a> 函数使用的 reader 对象。该 reader 对象从表或视图中读取数据。</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>创建供 <a href="#copyStream">copyStream</a> 函数使用的 writer 对象。该 writer 对象将数据写入表。如果表不存在，可以创建该表。</p>
</dd>
</dl>

## 类型定义

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>供 <a href="#copyStream">copyStream</a> 函数使用的 Reader（输入）对象</p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>供 <a href="#copyStream">copyStream</a> 函数使用的 Writer（输出）对象</p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>用户角色类型。</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
将 reader 复制到 writer。用于导入、导出表以及在表之间传输数据

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | reader 对象 |
| output | [<code>writerType</code>](#writerType) | writer 对象 |
| options | <code>object</code> | 选项 |

<a name="deployDb"></a>

## deployDb(options)
将存储在 modelFolder 中的数据库模型（表以 yaml 格式保存）部署到数据库

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 连接对象 |
| options.systemConnection | <code>object</code> | 系统连接（driver.connect 的结果）。如果未提供，将创建新连接 |
| options.driver | <code>object</code> | driver 对象。如果未提供，将从连接中加载 |
| options.analysedStructure | <code>object</code> | 数据库的已分析结构。如果未提供，将自动加载 |
| options.modelFolder | <code>string</code> | 包含模型文件的文件夹（表使用 YAML 文件，视图、存储过程等使用 SQL 文件，……） |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | 已加载的数据库模型 - 加载到数组中的 yaml 和 SQL 文件集合 |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | 用于转换模型的函数数组 |
| options.dbdiffOptionsExtra | <code>object</code> | dbdiff 的额外选项 |
| options.ignoreNameRegex | <code>string</code> | 用于按名称忽略对象的正则表达式 |
| options.targetSchema | <code>string</code> | 部署的目标 schema |
| options.maxMissingTablesRatio | <code>number</code> | 数据库中缺失表的最大比例。安全检查，如果缺失比例更高，则停止部署（防止意外删除所有表） |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
删除所有数据库对象

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 连接对象 |
| options.systemConnection | <code>object</code> | 系统连接（driver.connect 的结果）。如果未提供，将创建新连接 |
| options.driver | <code>object</code> | driver 对象。如果未提供，将从连接中加载 |
| options.analysedStructure | <code>object</code> | 数据库的已分析结构。如果未提供，将自动加载 |

<a name="executeQuery"></a>

## executeQuery(options)
执行 SQL 查询

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | 连接对象 |
| [options.systemConnection] | <code>object</code> | 系统连接（driver.connect 的结果）。如果未提供，将创建新连接 |
| [options.driver] | <code>object</code> | driver 对象。如果未提供，将从连接中加载 |
| [options.sql] | <code>string</code> | SQL 查询 |
| [options.sqlFile] | <code>string</code> | SQL 文件 |
| [options.logScriptItems] | <code>boolean</code> | 是否记录脚本条目而非整个脚本 |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
生成用于将模型部署到数据库的查询

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 连接对象 |
| options.systemConnection | <code>object</code> | 系统连接（driver.connect 的结果）。如果未提供，将创建新连接 |
| options.driver | <code>object</code> | driver 对象。如果未提供，将从连接中加载 |
| options.analysedStructure | <code>object</code> | 数据库的已分析结构。如果未提供，将自动加载 |
| options.modelFolder | <code>string</code> | 包含模型文件的文件夹（表使用 YAML 文件，视图、存储过程等使用 SQL 文件，……） |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | 已加载的数据库模型 - 加载到数组中的 yaml 和 SQL 文件集合 |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | 用于转换模型的函数数组 |
| options.dbdiffOptionsExtra | <code>object</code> | dbdiff 的额外选项 |
| options.ignoreNameRegex | <code>string</code> | 用于按名称忽略对象的正则表达式 |
| options.targetSchema | <code>string</code> | 部署的目标 schema |
| options.maxMissingTablesRatio | <code>number</code> | 数据库中缺失表的最大比例。安全检查，如果缺失比例更高，则停止部署（防止意外删除所有表） |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Reader 函数，用于读取 JSNOL 文件或 URL。JSONL 格式 - 文本文件，每一行都是一个 JSON 编码的行数据。

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 对象  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | 文件名或 URL |
| options.encoding | <code>string</code> | 文件的编码 |
| options.limitRows | <code>number</code> | 要读取的最大行数 |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
返回供 [copyStream](#copyStream) 函数使用的 writer 对象。该 writer 对象将数据写入 JSONL 文件。JSONL 格式 - 文本文件，每一行都是一个 JSON 编码的行数据，例如 MongoDB 使用该格式。

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - writer 对象  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | 文件名 |
| [options.encoding] | <code>string</code> | 文件的编码 |
| [options.header] | <code>boolean</code> | 是否写入头部。头部是描述源表结构的 JSON。头部是 DbGate 特有的，如果你想将数据导入到 MongoDB 等，则不应写入头部。 |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
为 JSON 文件创建供 [copyStream](#copyStream) 函数使用的 reader 对象。

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 对象  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | 文件名或 URL |
| options.jsonStyle | <code>string</code> | 'object' 或 'array' |
| [options.keyField] | <code>string</code> | object 样式的键字段 |
| [options.rootField] | <code>string</code> | object 样式的根字段 |
| [options.encoding] | <code>string</code> | 文件的编码 |
| [options.limitRows] | <code>number</code> | 要读取的最大行数 |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
返回供 [copyStream](#copyStream) 函数使用的 writer 对象。该 writer 对象将数据写入 JSON 文件。

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - writer 对象  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | 文件名 |
| [options.jsonStyle] | <code>string</code> | 'object' 或 'array' |
| [options.keyField] | <code>string</code> | object 样式的键字段 |
| [options.rootField] | <code>string</code> | object 样式的根字段 |
| [options.encoding] | <code>string</code> | 文件的编码 |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
返回供 [copyStream](#copyStream) 函数使用的 reader 对象。该 reader 对象从查询中读取数据。

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 对象  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 连接对象 |
| options.query | <code>string</code> | SQL 查询 |
| [options.queryType] | <code>string</code> | 查询类型 |
| [options.sql] | <code>string</code> | SQL 查询。已废弃；请改用 query |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
创建供 [copyStream](#copyStream) 函数使用的 reader 对象。该 reader 对象从表或视图中读取数据。

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - reader 对象  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 连接对象 |
| options.systemConnection | <code>object</code> | 系统连接（driver.connect 的结果）。如果未提供，将创建新连接 |
| options.pureName | <code>string</code> | 表名 |
| options.schemaName | <code>string</code> | schema 名称 |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
创建供 [copyStream](#copyStream) 函数使用的 writer 对象。该 writer 对象将数据写入表。如果表不存在，可以创建该表。

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - writer 对象  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 连接对象 |
| options.systemConnection | <code>object</code> | 系统连接（driver.connect 的结果）。如果未提供，将创建新连接 |
| options.driver | <code>object</code> | driver 对象。如果未提供，将从连接中加载 |
| options.pureName | <code>string</code> | 表名 |
| options.schemaName | <code>string</code> | schema 名称 |
| options.dropIfExists | <code>boolean</code> | 如果表存在则删除 |
| options.truncate | <code>boolean</code> | 插入前清空表 |
| options.createIfNotExists | <code>boolean</code> | 如果表不存在则创建 |
| options.commitAfterInsert | <code>boolean</code> | 插入后提交事务 |

<a name="readerType"></a>

## readerType : <code>Object</code>
供 [copyStream](#copyStream) 函数使用的 Reader（输入）对象

**Kind**: global typedef  
<a name="writerType"></a>

## writerType : <code>Object</code>
供 [copyStream](#copyStream) 函数使用的 Writer（输出）对象

**Kind**: global typedef  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
数据库引擎标识符，格式为 `engine@plugin-package`。

**Kind**: global typedef  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**Kind**: global typedef  
**Properties**

| Name | Type |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 

