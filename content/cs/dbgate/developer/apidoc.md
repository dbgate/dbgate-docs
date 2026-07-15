---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: cs
layout: docs
title: Dokumentace API
weight: 20
---

## Funkce

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Kopíruje data ze čtecího objektu do zapisovacího objektu. Používá se pro import, export tabulek a přenos dat mezi tabulkami</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>Nasazuje databázový model uložený ve složce modelFolder (tabulky jako soubory yaml) do databáze</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Odstraní všechny databázové objekty</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>Spustí SQL dotaz</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>Generuje dotaz pro nasazení modelu do databáze</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Čtecí funkce, která načítá soubor nebo URL ve formátu JSNOL. Formát JSONL – textový soubor, kde každý řádek je řádek zakódovaný v JSON.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Vrací zapisovací objekt pro funkci <a href="#copyStream">copyStream</a>. Tento zapisovací objekt zapisuje data do souboru JSONL. Formát JSONL – textový soubor, kde každý řádek je řádek zakódovaný v JSON, používá jej např. MongoDB.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Vytváří čtecí objekt pro soubor JSON pro funkci <a href="#copyStream">copyStream</a>.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Vrací zapisovací objekt pro funkci <a href="#copyStream">copyStream</a>. Tento zapisovací objekt zapisuje data do souboru JSON.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Vrací čtecí objekt pro funkci <a href="#copyStream">copyStream</a>. Tento čtecí objekt načítá data z dotazu.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Vytváří čtecí objekt pro funkci <a href="#copyStream">copyStream</a>. Tento čtecí objekt načítá data z tabulky nebo pohledu.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Vytváří zapisovací objekt pro funkci <a href="#copyStream">copyStream</a>. Tento zapisovací objekt zapisuje data do tabulky. Tabulka může být vytvořena, pokud neexistuje.</p>
</dd>
</dl>

## Definice typů

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>Čtecí (vstupní) objekt pro funkci <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>Zapisovací (výstupní) objekt pro funkci <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>Typ uživatelské role.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
Kopíruje data ze čtecího objektu do zapisovacího objektu. Používá se pro import, export tabulek a přenos dat mezi tabulkami

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | čtecí objekt |
| output | [<code>writerType</code>](#writerType) | zapisovací objekt |
| options | <code>object</code> | volby |

<a name="deployDb"></a>

## deployDb(options)
Nasazuje databázový model uložený ve složce modelFolder (tabulky jako soubory yaml) do databáze

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt připojení |
| options.systemConnection | <code>object</code> | systémové připojení (výsledek driver.connect). Pokud není zadáno, bude vytvořeno nové připojení |
| options.driver | <code>object</code> | objekt driveru. Pokud není zadán, bude načten z připojení |
| options.analysedStructure | <code>object</code> | analyzovaná struktura databáze. Pokud není zadána, bude načtena |
| options.modelFolder | <code>string</code> | složka se soubory modelu (soubory YAML pro tabulky, soubory SQL pro pohledy, procedury, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | načtený databázový model – kolekce souborů yaml a SQL načtených do pole |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | pole funkcí pro transformaci modelu |
| options.dbdiffOptionsExtra | <code>object</code> | další volby pro dbdiff |
| options.ignoreNameRegex | <code>string</code> | regulární výraz pro ignorování objektů podle názvu |
| options.targetSchema | <code>string</code> | cílové schéma pro nasazení |
| options.maxMissingTablesRatio | <code>number</code> | maximální podíl chybějících tabulek v databázi. Bezpečnostní kontrola, pokud je podíl chybějících tabulek vyšší, nasazení se zastaví (zabraňuje nechtěnému odstranění všech tabulek) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
Odstraní všechny databázové objekty

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt připojení |
| options.systemConnection | <code>object</code> | systémové připojení (výsledek driver.connect). Pokud není zadáno, bude vytvořeno nové připojení |
| options.driver | <code>object</code> | objekt driveru. Pokud není zadán, bude načten z připojení |
| options.analysedStructure | <code>object</code> | analyzovaná struktura databáze. Pokud není zadána, bude načtena |

<a name="executeQuery"></a>

## executeQuery(options)
Spustí SQL dotaz

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | objekt připojení |
| [options.systemConnection] | <code>object</code> | systémové připojení (výsledek driver.connect). Pokud není zadáno, bude vytvořeno nové připojení |
| [options.driver] | <code>object</code> | objekt driveru. Pokud není zadán, bude načten z připojení |
| [options.sql] | <code>string</code> | SQL dotaz |
| [options.sqlFile] | <code>string</code> | SQL soubor |
| [options.logScriptItems] | <code>boolean</code> | zda logovat jednotlivé položky skriptu místo celého skriptu |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
Generuje dotaz pro nasazení modelu do databáze

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt připojení |
| options.systemConnection | <code>object</code> | systémové připojení (výsledek driver.connect). Pokud není zadáno, bude vytvořeno nové připojení |
| options.driver | <code>object</code> | objekt driveru. Pokud není zadán, bude načten z připojení |
| options.analysedStructure | <code>object</code> | analyzovaná struktura databáze. Pokud není zadána, bude načtena |
| options.modelFolder | <code>string</code> | složka se soubory modelu (soubory YAML pro tabulky, soubory SQL pro pohledy, procedury, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | načtený databázový model – kolekce souborů yaml a SQL načtených do pole |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | pole funkcí pro transformaci modelu |
| options.dbdiffOptionsExtra | <code>object</code> | další volby pro dbdiff |
| options.ignoreNameRegex | <code>string</code> | regulární výraz pro ignorování objektů podle názvu |
| options.targetSchema | <code>string</code> | cílové schéma pro nasazení |
| options.maxMissingTablesRatio | <code>number</code> | maximální podíl chybějících tabulek v databázi. Bezpečnostní kontrola, pokud je podíl chybějících tabulek vyšší, nasazení se zastaví (zabraňuje nechtěnému odstranění všech tabulek) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Čtecí funkce, která načítá soubor nebo URL ve formátu JSNOL. Formát JSONL – textový soubor, kde každý řádek je řádek zakódovaný v JSON.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - čtecí objekt  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | název souboru nebo URL |
| options.encoding | <code>string</code> | kódování souboru |
| options.limitRows | <code>number</code> | maximální počet načítaných řádků |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Vrací zapisovací objekt pro funkci [copyStream](#copyStream). Tento zapisovací objekt zapisuje data do souboru JSONL. Formát JSONL – textový soubor, kde každý řádek je řádek zakódovaný v JSON, používá jej např. MongoDB.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - zapisovací objekt  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | název souboru |
| [options.encoding] | <code>string</code> | kódování souboru |
| [options.header] | <code>boolean</code> | zda zapsat hlavičku. Hlavička je JSON popisující strukturu zdrojové tabulky. Hlavička je specifická pro DbGate, pokud chcete např. importovat data do MongoDB, hlavičku byste zapisovat neměli. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Vytváří čtecí objekt pro soubor JSON pro funkci [copyStream](#copyStream).

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - čtecí objekt  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | název souboru nebo URL |
| options.jsonStyle | <code>string</code> | 'object' nebo 'array' |
| [options.keyField] | <code>string</code> | klíčové pole pro styl object |
| [options.rootField] | <code>string</code> | kořenové pole pro styl object |
| [options.encoding] | <code>string</code> | kódování souboru |
| [options.limitRows] | <code>number</code> | maximální počet načítaných řádků |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Vrací zapisovací objekt pro funkci [copyStream](#copyStream). Tento zapisovací objekt zapisuje data do souboru JSON.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - zapisovací objekt  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | název souboru |
| [options.jsonStyle] | <code>string</code> | 'object' nebo 'array' |
| [options.keyField] | <code>string</code> | klíčové pole pro styl object |
| [options.rootField] | <code>string</code> | kořenové pole pro styl object |
| [options.encoding] | <code>string</code> | kódování souboru |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Vrací čtecí objekt pro funkci [copyStream](#copyStream). Tento čtecí objekt načítá data z dotazu.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - čtecí objekt  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt připojení |
| options.query | <code>string</code> | SQL dotaz |
| [options.queryType] | <code>string</code> | typ dotazu |
| [options.sql] | <code>string</code> | SQL dotaz. zastaralé; použijte místo toho query |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Vytváří čtecí objekt pro funkci [copyStream](#copyStream). Tento čtecí objekt načítá data z tabulky nebo pohledu.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - čtecí objekt  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt připojení |
| options.systemConnection | <code>object</code> | systémové připojení (výsledek driver.connect). Pokud není zadáno, bude vytvořeno nové připojení |
| options.pureName | <code>string</code> | název tabulky |
| options.schemaName | <code>string</code> | název schématu |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Vytváří zapisovací objekt pro funkci [copyStream](#copyStream). Tento zapisovací objekt zapisuje data do tabulky. Tabulka může být vytvořena, pokud neexistuje.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - zapisovací objekt  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt připojení |
| options.systemConnection | <code>object</code> | systémové připojení (výsledek driver.connect). Pokud není zadáno, bude vytvořeno nové připojení |
| options.driver | <code>object</code> | objekt driveru. Pokud není zadán, bude načten z připojení |
| options.pureName | <code>string</code> | název tabulky |
| options.schemaName | <code>string</code> | název schématu |
| options.dropIfExists | <code>boolean</code> | odstranit tabulku, pokud existuje |
| options.truncate | <code>boolean</code> | vyprázdnit tabulku před vložením |
| options.createIfNotExists | <code>boolean</code> | vytvořit tabulku, pokud neexistuje |
| options.commitAfterInsert | <code>boolean</code> | potvrdit transakci po vložení |

<a name="readerType"></a>

## readerType : <code>Object</code>
Čtecí (vstupní) objekt pro funkci [copyStream](#copyStream)

**Kind**: global typedef  
<a name="writerType"></a>

## writerType : <code>Object</code>
Zapisovací (výstupní) objekt pro funkci [copyStream](#copyStream)

**Kind**: global typedef  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
Identifikátor databázového enginu ve tvaru `engine@plugin-package`.

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

