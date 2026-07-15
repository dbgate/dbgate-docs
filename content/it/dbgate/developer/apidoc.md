---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: it
layout: docs
title: Documentazione API
weight: 20
---

## Funzioni

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Copia il reader nel writer. Utilizzato per importare, esportare tabelle e trasferire dati tra tabelle</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>Distribuisce nel database il modello di database memorizzato in modelFolder (tabelle come file yaml)</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Elimina tutti gli oggetti del database</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>Esegue una query SQL</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>Genera la query per distribuire il modello nel database</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Funzione reader che legge un file o un URL JSNOL. Formato JSONL - file di testo in cui ogni riga è una riga codificata in JSON.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Restituisce l'oggetto writer per la funzione <a href="#copyStream">copyStream</a>. Questo oggetto writer scrive i dati in un file JSONL. Formato JSONL - file di testo in cui ogni riga è una riga codificata in JSON, utilizzato ad esempio da MongoDB.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Crea l'oggetto reader per un file JSON per la funzione <a href="#copyStream">copyStream</a>.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Restituisce l'oggetto writer per la funzione <a href="#copyStream">copyStream</a>. Questo oggetto writer scrive i dati in un file JSON.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Restituisce l'oggetto reader per la funzione <a href="#copyStream">copyStream</a>. Questo oggetto reader legge i dati da una query.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Crea l'oggetto reader per la funzione <a href="#copyStream">copyStream</a>. Questo oggetto reader legge i dati da una tabella o da una vista.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Crea l'oggetto writer per la funzione <a href="#copyStream">copyStream</a>. Questo oggetto writer scrive i dati in una tabella. La tabella può essere creata se non esiste.</p>
</dd>
</dl>

## Typedef

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>Oggetto reader (input) per la funzione <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>Oggetto writer (output) per la funzione <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>Tipo di ruolo utente.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
Copia il reader nel writer. Utilizzato per importare, esportare tabelle e trasferire dati tra tabelle

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | oggetto reader |
| output | [<code>writerType</code>](#writerType) | oggetto writer |
| options | <code>object</code> | opzioni |

<a name="deployDb"></a>

## deployDb(options)
Distribuisce nel database il modello di database memorizzato in modelFolder (tabelle come file yaml)

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | oggetto connessione |
| options.systemConnection | <code>object</code> | connessione di sistema (risultato di driver.connect). Se non fornita, verrà creata una nuova connessione |
| options.driver | <code>object</code> | oggetto driver. Se non fornito, verrà caricato dalla connessione |
| options.analysedStructure | <code>object</code> | struttura analizzata del database. Se non fornita, verrà caricata |
| options.modelFolder | <code>string</code> | cartella con i file del modello (file YAML per le tabelle, file SQL per viste, procedure, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modello di database caricato - insieme di file yaml e SQL caricati in un array |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | array di funzioni per la trasformazione del modello |
| options.dbdiffOptionsExtra | <code>object</code> | opzioni aggiuntive per dbdiff |
| options.ignoreNameRegex | <code>string</code> | regex per ignorare gli oggetti in base al nome |
| options.targetSchema | <code>string</code> | schema di destinazione per la distribuzione |
| options.maxMissingTablesRatio | <code>number</code> | rapporto massimo di tabelle mancanti nel database. Controllo di sicurezza: se il rapporto di tabelle mancanti è superiore, la distribuzione viene interrotta (prevenendo l'eliminazione accidentale di tutte le tabelle) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
Elimina tutti gli oggetti del database

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | oggetto connessione |
| options.systemConnection | <code>object</code> | connessione di sistema (risultato di driver.connect). Se non fornita, verrà creata una nuova connessione |
| options.driver | <code>object</code> | oggetto driver. Se non fornito, verrà caricato dalla connessione |
| options.analysedStructure | <code>object</code> | struttura analizzata del database. Se non fornita, verrà caricata |

<a name="executeQuery"></a>

## executeQuery(options)
Esegue una query SQL

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | oggetto connessione |
| [options.systemConnection] | <code>object</code> | connessione di sistema (risultato di driver.connect). Se non fornita, verrà creata una nuova connessione |
| [options.driver] | <code>object</code> | oggetto driver. Se non fornito, verrà caricato dalla connessione |
| [options.sql] | <code>string</code> | query SQL |
| [options.sqlFile] | <code>string</code> | file SQL |
| [options.logScriptItems] | <code>boolean</code> | se registrare nel log i singoli elementi dello script invece dell'intero script |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
Genera la query per distribuire il modello nel database

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | oggetto connessione |
| options.systemConnection | <code>object</code> | connessione di sistema (risultato di driver.connect). Se non fornita, verrà creata una nuova connessione |
| options.driver | <code>object</code> | oggetto driver. Se non fornito, verrà caricato dalla connessione |
| options.analysedStructure | <code>object</code> | struttura analizzata del database. Se non fornita, verrà caricata |
| options.modelFolder | <code>string</code> | cartella con i file del modello (file YAML per le tabelle, file SQL per viste, procedure, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modello di database caricato - insieme di file yaml e SQL caricati in un array |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | array di funzioni per la trasformazione del modello |
| options.dbdiffOptionsExtra | <code>object</code> | opzioni aggiuntive per dbdiff |
| options.ignoreNameRegex | <code>string</code> | regex per ignorare gli oggetti in base al nome |
| options.targetSchema | <code>string</code> | schema di destinazione per la distribuzione |
| options.maxMissingTablesRatio | <code>number</code> | rapporto massimo di tabelle mancanti nel database. Controllo di sicurezza: se il rapporto di tabelle mancanti è superiore, la distribuzione viene interrotta (prevenendo l'eliminazione accidentale di tutte le tabelle) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Funzione reader che legge un file o un URL JSNOL. Formato JSONL - file di testo in cui ogni riga è una riga codificata in JSON.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - oggetto reader  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | nome del file o URL |
| options.encoding | <code>string</code> | codifica del file |
| options.limitRows | <code>number</code> | numero massimo di righe da leggere |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Restituisce l'oggetto writer per la funzione [copyStream](#copyStream). Questo oggetto writer scrive i dati in un file JSONL. Formato JSONL - file di testo in cui ogni riga è una riga codificata in JSON, utilizzato ad esempio da MongoDB.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - oggetto writer  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nome del file |
| [options.encoding] | <code>string</code> | codifica del file |
| [options.header] | <code>boolean</code> | se scrivere l'intestazione. L'intestazione è un JSON che descrive la struttura della tabella di origine. L'intestazione è specifica di DbGate; se vuoi ad esempio importare i dati in MongoDB, non dovresti scrivere l'intestazione. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Crea l'oggetto reader per un file JSON per la funzione [copyStream](#copyStream).

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - oggetto reader  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nome del file o URL |
| options.jsonStyle | <code>string</code> | 'object' oppure 'array' |
| [options.keyField] | <code>string</code> | campo chiave per lo stile object |
| [options.rootField] | <code>string</code> | campo radice per lo stile object |
| [options.encoding] | <code>string</code> | codifica del file |
| [options.limitRows] | <code>number</code> | numero massimo di righe da leggere |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Restituisce l'oggetto writer per la funzione [copyStream](#copyStream). Questo oggetto writer scrive i dati in un file JSON.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - oggetto writer  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nome del file |
| [options.jsonStyle] | <code>string</code> | 'object' oppure 'array' |
| [options.keyField] | <code>string</code> | campo chiave per lo stile object |
| [options.rootField] | <code>string</code> | campo radice per lo stile object |
| [options.encoding] | <code>string</code> | codifica del file |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Restituisce l'oggetto reader per la funzione [copyStream](#copyStream). Questo oggetto reader legge i dati da una query.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - oggetto reader  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | oggetto connessione |
| options.query | <code>string</code> | query SQL |
| [options.queryType] | <code>string</code> | tipo di query |
| [options.sql] | <code>string</code> | query SQL. obsoleto; usa invece query |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Crea l'oggetto reader per la funzione [copyStream](#copyStream). Questo oggetto reader legge i dati da una tabella o da una vista.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - oggetto reader  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | oggetto connessione |
| options.systemConnection | <code>object</code> | connessione di sistema (risultato di driver.connect). Se non fornita, verrà creata una nuova connessione |
| options.pureName | <code>string</code> | nome della tabella |
| options.schemaName | <code>string</code> | nome dello schema |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Crea l'oggetto writer per la funzione [copyStream](#copyStream). Questo oggetto writer scrive i dati in una tabella. La tabella può essere creata se non esiste.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - oggetto writer  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | oggetto connessione |
| options.systemConnection | <code>object</code> | connessione di sistema (risultato di driver.connect). Se non fornita, verrà creata una nuova connessione |
| options.driver | <code>object</code> | oggetto driver. Se non fornito, verrà caricato dalla connessione |
| options.pureName | <code>string</code> | nome della tabella |
| options.schemaName | <code>string</code> | nome dello schema |
| options.dropIfExists | <code>boolean</code> | elimina la tabella se esiste |
| options.truncate | <code>boolean</code> | svuota la tabella prima dell'inserimento |
| options.createIfNotExists | <code>boolean</code> | crea la tabella se non esiste |
| options.commitAfterInsert | <code>boolean</code> | esegue il commit della transazione dopo l'inserimento |

<a name="readerType"></a>

## readerType : <code>Object</code>
Oggetto reader (input) per la funzione [copyStream](#copyStream)

**Kind**: global typedef  
<a name="writerType"></a>

## writerType : <code>Object</code>
Oggetto writer (output) per la funzione [copyStream](#copyStream)

**Kind**: global typedef  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
L'identificatore del motore di database, nella forma `engine@plugin-package`.

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
