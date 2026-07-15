---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: ja
layout: docs
title: API ドキュメント
weight: 20
---

## 関数

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>リーダーをライターにコピーします。テーブルのインポート、エクスポート、およびテーブル間のデータ転送に使用されます</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>modelFolder に保存されたデータベースモデル（YAML 形式のテーブル）をデータベースにデプロイします</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>すべてのデータベースオブジェクトを削除します</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>SQL クエリを実行します</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>モデルをデータベースにデプロイするためのクエリを生成します</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>JSONL ファイルまたは URL を読み取るリーダー関数です。JSONL 形式 - テキストファイルで、各行が JSON エンコードされた行です。</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用のライターオブジェクトを返します。このライターオブジェクトはデータを JSONL ファイルに書き込みます。JSONL 形式 - テキストファイルで、各行が JSON エンコードされた行であり、例えば MongoDB で使用されます。</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用に JSON ファイルのリーダーオブジェクトを作成します。</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用のライターオブジェクトを返します。このライターオブジェクトはデータを JSON ファイルに書き込みます。</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用のリーダーオブジェクトを返します。このリーダーオブジェクトはクエリからデータを読み取ります。</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用のリーダーオブジェクトを作成します。このリーダーオブジェクトはテーブルまたはビューからデータを読み取ります。</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用のライターオブジェクトを作成します。このライターオブジェクトはデータをテーブルに書き込みます。テーブルが存在しない場合は作成することもできます。</p>
</dd>
</dl>

## 型定義

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用のリーダー（入力）オブジェクト</p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p><a href="#copyStream">copyStream</a> 関数用のライター（出力）オブジェクト</p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>ユーザーロールの型。</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
リーダーをライターにコピーします。テーブルのインポート、エクスポート、およびテーブル間のデータ転送に使用されます

**種類**: グローバル関数  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | リーダーオブジェクト |
| output | [<code>writerType</code>](#writerType) | ライターオブジェクト |
| options | <code>object</code> | オプション |

<a name="deployDb"></a>

## deployDb(options)
modelFolder に保存されたデータベースモデル（YAML 形式のテーブル）をデータベースにデプロイします

**種類**: グローバル関数  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 接続オブジェクト |
| options.systemConnection | <code>object</code> | システム接続（driver.connect の結果）。指定されていない場合、新しい接続が作成されます |
| options.driver | <code>object</code> | ドライバーオブジェクト。指定されていない場合、接続から読み込まれます |
| options.analysedStructure | <code>object</code> | データベースの解析済み構造。指定されていない場合、読み込まれます |
| options.modelFolder | <code>string</code> | モデルファイルのフォルダー（テーブル用の YAML ファイル、ビューやプロシージャなど用の SQL ファイル） |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | 読み込み済みのデータベースモデル - 配列に読み込まれた YAML および SQL ファイルのコレクション |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | モデルを変換する関数の配列 |
| options.dbdiffOptionsExtra | <code>object</code> | dbdiff の追加オプション |
| options.ignoreNameRegex | <code>string</code> | 名前でオブジェクトを無視するための正規表現 |
| options.targetSchema | <code>string</code> | デプロイ先のスキーマ |
| options.maxMissingTablesRatio | <code>number</code> | データベース内で欠落しているテーブルの最大比率。安全チェックであり、欠落比率がこれより高い場合、デプロイは停止されます（すべてのテーブルの誤削除を防止） |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
すべてのデータベースオブジェクトを削除します

**種類**: グローバル関数  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 接続オブジェクト |
| options.systemConnection | <code>object</code> | システム接続（driver.connect の結果）。指定されていない場合、新しい接続が作成されます |
| options.driver | <code>object</code> | ドライバーオブジェクト。指定されていない場合、接続から読み込まれます |
| options.analysedStructure | <code>object</code> | データベースの解析済み構造。指定されていない場合、読み込まれます |

<a name="executeQuery"></a>

## executeQuery(options)
SQL クエリを実行します

**種類**: グローバル関数  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | 接続オブジェクト |
| [options.systemConnection] | <code>object</code> | システム接続（driver.connect の結果）。指定されていない場合、新しい接続が作成されます |
| [options.driver] | <code>object</code> | ドライバーオブジェクト。指定されていない場合、接続から読み込まれます |
| [options.sql] | <code>string</code> | SQL クエリ |
| [options.sqlFile] | <code>string</code> | SQL ファイル |
| [options.logScriptItems] | <code>boolean</code> | スクリプト全体ではなくスクリプト項目をログに記録するかどうか |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
モデルをデータベースにデプロイするためのクエリを生成します

**種類**: グローバル関数  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 接続オブジェクト |
| options.systemConnection | <code>object</code> | システム接続（driver.connect の結果）。指定されていない場合、新しい接続が作成されます |
| options.driver | <code>object</code> | ドライバーオブジェクト。指定されていない場合、接続から読み込まれます |
| options.analysedStructure | <code>object</code> | データベースの解析済み構造。指定されていない場合、読み込まれます |
| options.modelFolder | <code>string</code> | モデルファイルのフォルダー（テーブル用の YAML ファイル、ビューやプロシージャなど用の SQL ファイル） |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | 読み込み済みのデータベースモデル - 配列に読み込まれた YAML および SQL ファイルのコレクション |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | モデルを変換する関数の配列 |
| options.dbdiffOptionsExtra | <code>object</code> | dbdiff の追加オプション |
| options.ignoreNameRegex | <code>string</code> | 名前でオブジェクトを無視するための正規表現 |
| options.targetSchema | <code>string</code> | デプロイ先のスキーマ |
| options.maxMissingTablesRatio | <code>number</code> | データベース内で欠落しているテーブルの最大比率。安全チェックであり、欠落比率がこれより高い場合、デプロイは停止されます（すべてのテーブルの誤削除を防止） |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
JSONL ファイルまたは URL を読み取るリーダー関数です。JSONL 形式 - テキストファイルで、各行が JSON エンコードされた行です。

**種類**: グローバル関数  
**戻り値**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - リーダーオブジェクト  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | ファイル名または URL |
| options.encoding | <code>string</code> | ファイルのエンコーディング |
| options.limitRows | <code>number</code> | 読み取る行の最大数 |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
[copyStream](#copyStream) 関数用のライターオブジェクトを返します。このライターオブジェクトはデータを JSONL ファイルに書き込みます。JSONL 形式 - テキストファイルで、各行が JSON エンコードされた行であり、例えば MongoDB で使用されます。

**種類**: グローバル関数  
**戻り値**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - ライターオブジェクト  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | ファイル名 |
| [options.encoding] | <code>string</code> | ファイルのエンコーディング |
| [options.header] | <code>boolean</code> | ヘッダーを書き込むかどうか。ヘッダーはソーステーブルの構造を記述する JSON です。ヘッダーは DbGate 固有のものであり、例えば MongoDB にデータをインポートしたい場合は、ヘッダーを書き込むべきではありません。 |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
[copyStream](#copyStream) 関数用に JSON ファイルのリーダーオブジェクトを作成します。

**種類**: グローバル関数  
**戻り値**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - リーダーオブジェクト  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | ファイル名または URL |
| options.jsonStyle | <code>string</code> | 'object' または 'array' |
| [options.keyField] | <code>string</code> | object スタイルのキーフィールド |
| [options.rootField] | <code>string</code> | object スタイルのルートフィールド |
| [options.encoding] | <code>string</code> | ファイルのエンコーディング |
| [options.limitRows] | <code>number</code> | 読み取る行の最大数 |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
[copyStream](#copyStream) 関数用のライターオブジェクトを返します。このライターオブジェクトはデータを JSON ファイルに書き込みます。

**種類**: グローバル関数  
**戻り値**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - ライターオブジェクト  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | ファイル名 |
| [options.jsonStyle] | <code>string</code> | 'object' または 'array' |
| [options.keyField] | <code>string</code> | object スタイルのキーフィールド |
| [options.rootField] | <code>string</code> | object スタイルのルートフィールド |
| [options.encoding] | <code>string</code> | ファイルのエンコーディング |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
[copyStream](#copyStream) 関数用のリーダーオブジェクトを返します。このリーダーオブジェクトはクエリからデータを読み取ります。

**種類**: グローバル関数  
**戻り値**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - リーダーオブジェクト  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 接続オブジェクト |
| options.query | <code>string</code> | SQL クエリ |
| [options.queryType] | <code>string</code> | クエリタイプ |
| [options.sql] | <code>string</code> | SQL クエリ。廃止予定。代わりに query を使用してください |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
[copyStream](#copyStream) 関数用のリーダーオブジェクトを作成します。このリーダーオブジェクトはテーブルまたはビューからデータを読み取ります。

**種類**: グローバル関数  
**戻り値**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - リーダーオブジェクト  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 接続オブジェクト |
| options.systemConnection | <code>object</code> | システム接続（driver.connect の結果）。指定されていない場合、新しい接続が作成されます |
| options.pureName | <code>string</code> | テーブル名 |
| options.schemaName | <code>string</code> | スキーマ名 |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
[copyStream](#copyStream) 関数用のライターオブジェクトを作成します。このライターオブジェクトはデータをテーブルに書き込みます。テーブルが存在しない場合は作成することもできます。

**種類**: グローバル関数  
**戻り値**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - ライターオブジェクト  

| パラメーター | 型 | 説明 |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | 接続オブジェクト |
| options.systemConnection | <code>object</code> | システム接続（driver.connect の結果）。指定されていない場合、新しい接続が作成されます |
| options.driver | <code>object</code> | ドライバーオブジェクト。指定されていない場合、接続から読み込まれます |
| options.pureName | <code>string</code> | テーブル名 |
| options.schemaName | <code>string</code> | スキーマ名 |
| options.dropIfExists | <code>boolean</code> | テーブルが存在する場合は削除する |
| options.truncate | <code>boolean</code> | 挿入前にテーブルを truncate する |
| options.createIfNotExists | <code>boolean</code> | テーブルが存在しない場合は作成する |
| options.commitAfterInsert | <code>boolean</code> | 挿入後にトランザクションをコミットする |

<a name="readerType"></a>

## readerType : <code>Object</code>
[copyStream](#copyStream) 関数用のリーダー（入力）オブジェクト

**種類**: グローバル型定義  
<a name="writerType"></a>

## writerType : <code>Object</code>
[copyStream](#copyStream) 関数用のライター（出力）オブジェクト

**種類**: グローバル型定義  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
データベースエンジンの識別子。`engine@plugin-package` の形式です。

**種類**: グローバル型定義  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**種類**: グローバル型定義  
**プロパティ**

| 名前 | 型 |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 
