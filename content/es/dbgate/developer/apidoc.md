---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: es
layout: docs
title: Documentación de la API
weight: 20
---

## Funciones

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Copia el lector al escritor. Se utiliza para importar y exportar tablas y para transferir datos entre tablas</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>Despliega en la base de datos el modelo de base de datos almacenado en modelFolder (tablas como archivos YAML)</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Elimina todos los objetos de la base de datos</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>Ejecuta una consulta SQL</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>Genera la consulta para desplegar el modelo en la base de datos</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Función lectora que lee un archivo o URL JSONL. Formato JSONL: archivo de texto en el que cada línea es una fila codificada en JSON.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Devuelve un objeto escritor para la función <a href="#copyStream">copyStream</a>. Este objeto escritor escribe los datos en un archivo JSONL. Formato JSONL: archivo de texto en el que cada línea es una fila codificada en JSON, utilizado por ejemplo por MongoDB.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Crea un objeto lector de un archivo JSON para la función <a href="#copyStream">copyStream</a>.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Devuelve un objeto escritor para la función <a href="#copyStream">copyStream</a>. Este objeto escritor escribe los datos en un archivo JSON.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Devuelve un objeto lector para la función <a href="#copyStream">copyStream</a>. Este objeto lector lee los datos de una consulta.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Crea un objeto lector para la función <a href="#copyStream">copyStream</a>. Este objeto lector lee los datos de una tabla o vista.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Crea un objeto escritor para la función <a href="#copyStream">copyStream</a>. Este objeto escritor escribe los datos en una tabla. La tabla se puede crear si no existe.</p>
</dd>
</dl>

## Definiciones de tipos

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>Objeto lector (de entrada) para la función <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>Objeto escritor (de salida) para la función <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>Tipo de rol de usuario.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
Copia el lector al escritor. Se utiliza para importar y exportar tablas y para transferir datos entre tablas

**Tipo**: función global  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | objeto lector |
| output | [<code>writerType</code>](#writerType) | objeto escritor |
| options | <code>object</code> | opciones |

<a name="deployDb"></a>

## deployDb(options)
Despliega en la base de datos el modelo de base de datos almacenado en modelFolder (tablas como archivos YAML)

**Tipo**: función global  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexión |
| options.systemConnection | <code>object</code> | conexión de sistema (resultado de driver.connect). Si no se proporciona, se creará una nueva conexión |
| options.driver | <code>object</code> | objeto de controlador. Si no se proporciona, se cargará desde la conexión |
| options.analysedStructure | <code>object</code> | estructura analizada de la base de datos. Si no se proporciona, se cargará |
| options.modelFolder | <code>string</code> | carpeta con los archivos del modelo (archivos YAML para las tablas, archivos SQL para las vistas, procedimientos, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modelo de base de datos cargado: colección de archivos YAML y SQL cargados en un array |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | array de funciones para transformar el modelo |
| options.dbdiffOptionsExtra | <code>object</code> | opciones adicionales para dbdiff |
| options.ignoreNameRegex | <code>string</code> | expresión regular para ignorar objetos por su nombre |
| options.targetSchema | <code>string</code> | esquema de destino para el despliegue |
| options.maxMissingTablesRatio | <code>number</code> | proporción máxima de tablas faltantes en la base de datos. Comprobación de seguridad: si la proporción de tablas faltantes es mayor, el despliegue se detiene (para evitar la eliminación accidental de todas las tablas) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
Elimina todos los objetos de la base de datos

**Tipo**: función global  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexión |
| options.systemConnection | <code>object</code> | conexión de sistema (resultado de driver.connect). Si no se proporciona, se creará una nueva conexión |
| options.driver | <code>object</code> | objeto de controlador. Si no se proporciona, se cargará desde la conexión |
| options.analysedStructure | <code>object</code> | estructura analizada de la base de datos. Si no se proporciona, se cargará |

<a name="executeQuery"></a>

## executeQuery(options)
Ejecuta una consulta SQL

**Tipo**: función global  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | objeto de conexión |
| [options.systemConnection] | <code>object</code> | conexión de sistema (resultado de driver.connect). Si no se proporciona, se creará una nueva conexión |
| [options.driver] | <code>object</code> | objeto de controlador. Si no se proporciona, se cargará desde la conexión |
| [options.sql] | <code>string</code> | consulta SQL |
| [options.sqlFile] | <code>string</code> | archivo SQL |
| [options.logScriptItems] | <code>boolean</code> | si se deben registrar los elementos del script en lugar del script completo |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
Genera la consulta para desplegar el modelo en la base de datos

**Tipo**: función global  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexión |
| options.systemConnection | <code>object</code> | conexión de sistema (resultado de driver.connect). Si no se proporciona, se creará una nueva conexión |
| options.driver | <code>object</code> | objeto de controlador. Si no se proporciona, se cargará desde la conexión |
| options.analysedStructure | <code>object</code> | estructura analizada de la base de datos. Si no se proporciona, se cargará |
| options.modelFolder | <code>string</code> | carpeta con los archivos del modelo (archivos YAML para las tablas, archivos SQL para las vistas, procedimientos, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modelo de base de datos cargado: colección de archivos YAML y SQL cargados en un array |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | array de funciones para transformar el modelo |
| options.dbdiffOptionsExtra | <code>object</code> | opciones adicionales para dbdiff |
| options.ignoreNameRegex | <code>string</code> | expresión regular para ignorar objetos por su nombre |
| options.targetSchema | <code>string</code> | esquema de destino para el despliegue |
| options.maxMissingTablesRatio | <code>number</code> | proporción máxima de tablas faltantes en la base de datos. Comprobación de seguridad: si la proporción de tablas faltantes es mayor, el despliegue se detiene (para evitar la eliminación accidental de todas las tablas) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Función lectora que lee un archivo o URL JSONL. Formato JSONL: archivo de texto en el que cada línea es una fila codificada en JSON.

**Tipo**: función global  
**Devuelve**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto lector  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | nombre de archivo o URL |
| options.encoding | <code>string</code> | codificación del archivo |
| options.limitRows | <code>number</code> | número máximo de filas a leer |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Devuelve un objeto escritor para la función [copyStream](#copyStream). Este objeto escritor escribe los datos en un archivo JSONL. Formato JSONL: archivo de texto en el que cada línea es una fila codificada en JSON, utilizado por ejemplo por MongoDB.

**Tipo**: función global  
**Devuelve**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objeto escritor  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nombre de archivo |
| [options.encoding] | <code>string</code> | codificación del archivo |
| [options.header] | <code>boolean</code> | si se debe escribir el encabezado. El encabezado es un JSON que describe la estructura de la tabla de origen. El encabezado es específico de DbGate; si desea, por ejemplo, importar datos a MongoDB, no debería escribir el encabezado. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Crea un objeto lector de un archivo JSON para la función [copyStream](#copyStream).

**Tipo**: función global  
**Devuelve**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto lector  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nombre de archivo o URL |
| options.jsonStyle | <code>string</code> | 'object' o 'array' |
| [options.keyField] | <code>string</code> | campo clave para el estilo object |
| [options.rootField] | <code>string</code> | campo raíz para el estilo object |
| [options.encoding] | <code>string</code> | codificación del archivo |
| [options.limitRows] | <code>number</code> | número máximo de filas a leer |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Devuelve un objeto escritor para la función [copyStream](#copyStream). Este objeto escritor escribe los datos en un archivo JSON.

**Tipo**: función global  
**Devuelve**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objeto escritor  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nombre de archivo |
| [options.jsonStyle] | <code>string</code> | 'object' o 'array' |
| [options.keyField] | <code>string</code> | campo clave para el estilo object |
| [options.rootField] | <code>string</code> | campo raíz para el estilo object |
| [options.encoding] | <code>string</code> | codificación del archivo |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Devuelve un objeto lector para la función [copyStream](#copyStream). Este objeto lector lee los datos de una consulta.

**Tipo**: función global  
**Devuelve**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto lector  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexión |
| options.query | <code>string</code> | consulta SQL |
| [options.queryType] | <code>string</code> | tipo de consulta |
| [options.sql] | <code>string</code> | consulta SQL. obsoleto; utilice query en su lugar |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Crea un objeto lector para la función [copyStream](#copyStream). Este objeto lector lee los datos de una tabla o vista.

**Tipo**: función global  
**Devuelve**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto lector  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexión |
| options.systemConnection | <code>object</code> | conexión de sistema (resultado de driver.connect). Si no se proporciona, se creará una nueva conexión |
| options.pureName | <code>string</code> | nombre de la tabla |
| options.schemaName | <code>string</code> | nombre del esquema |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Crea un objeto escritor para la función [copyStream](#copyStream). Este objeto escritor escribe los datos en una tabla. La tabla se puede crear si no existe.

**Tipo**: función global  
**Devuelve**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objeto escritor  

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexión |
| options.systemConnection | <code>object</code> | conexión de sistema (resultado de driver.connect). Si no se proporciona, se creará una nueva conexión |
| options.driver | <code>object</code> | objeto de controlador. Si no se proporciona, se cargará desde la conexión |
| options.pureName | <code>string</code> | nombre de la tabla |
| options.schemaName | <code>string</code> | nombre del esquema |
| options.dropIfExists | <code>boolean</code> | eliminar la tabla si existe |
| options.truncate | <code>boolean</code> | vaciar la tabla antes de la inserción |
| options.createIfNotExists | <code>boolean</code> | crear la tabla si no existe |
| options.commitAfterInsert | <code>boolean</code> | confirmar la transacción después de la inserción |

<a name="readerType"></a>

## readerType : <code>Object</code>
Objeto lector (de entrada) para la función [copyStream](#copyStream)

**Tipo**: typedef global  
<a name="writerType"></a>

## writerType : <code>Object</code>
Objeto escritor (de salida) para la función [copyStream](#copyStream)

**Tipo**: typedef global  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
El identificador del motor de base de datos, con el formato `engine@plugin-package`.

**Tipo**: typedef global  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**Tipo**: typedef global  
**Propiedades**

| Nombre | Tipo |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 

