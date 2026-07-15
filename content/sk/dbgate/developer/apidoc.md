---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: sk
layout: docs
title: Dokumentácia API
weight: 20
---

## Funkcie

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Kopíruje čítač do zapisovača. Používa sa na import, export tabuliek a prenos dát medzi tabuľkami</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>Nasadí databázový model uložený v priečinku modelFolder (tabuľky ako yaml súbory) do databázy</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Zmaže všetky databázové objekty</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>Vykoná SQL dotaz</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>Vygeneruje dotaz na nasadenie modelu do databázy</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Funkcia čítača, ktorá číta súbor alebo URL vo formáte JSNOL. Formát JSONL - textový súbor, každý riadok je riadok zakódovaný v JSON.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Vracia objekt zapisovača pre funkciu <a href="#copyStream">copyStream</a>. Tento objekt zapisovača zapisuje dáta do súboru JSONL. Formát JSONL - textový súbor, každý riadok je riadok zakódovaný v JSON, používa ho napr. MongoDB.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Vytvára objekt čítača pre súbor JSON pre funkciu <a href="#copyStream">copyStream</a>.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Vracia objekt zapisovača pre funkciu <a href="#copyStream">copyStream</a>. Tento objekt zapisovača zapisuje dáta do súboru JSON.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Vracia objekt čítača pre funkciu <a href="#copyStream">copyStream</a>. Tento objekt čítača číta dáta z dotazu.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Vytvára objekt čítača pre funkciu <a href="#copyStream">copyStream</a>. Tento objekt čítača číta dáta z tabuľky alebo pohľadu.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Vytvára objekt zapisovača pre funkciu <a href="#copyStream">copyStream</a>. Tento objekt zapisovača zapisuje dáta do tabuľky. Tabuľka môže byť vytvorená, ak neexistuje.</p>
</dd>
</dl>

## Definície typov

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>Objekt čítača (vstup) pre funkciu <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>Objekt zapisovača (výstup) pre funkciu <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>Typ používateľskej roly.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
Kopíruje čítač do zapisovača. Používa sa na import, export tabuliek a prenos dát medzi tabuľkami

**Druh**: globálna funkcia  

| Parameter | Typ | Popis |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | objekt čítača |
| output | [<code>writerType</code>](#writerType) | objekt zapisovača |
| options | <code>object</code> | možnosti |

<a name="deployDb"></a>

## deployDb(options)
Nasadí databázový model uložený v priečinku modelFolder (tabuľky ako yaml súbory) do databázy

**Druh**: globálna funkcia  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt pripojenia |
| options.systemConnection | <code>object</code> | systémové pripojenie (výsledok driver.connect). Ak nie je zadané, vytvorí sa nové pripojenie |
| options.driver | <code>object</code> | objekt ovládača. Ak nie je zadaný, načíta sa z pripojenia |
| options.analysedStructure | <code>object</code> | analyzovaná štruktúra databázy. Ak nie je zadaná, načíta sa |
| options.modelFolder | <code>string</code> | priečinok so súbormi modelu (súbory YAML pre tabuľky, súbory SQL pre pohľady, procedúry, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | načítaný databázový model - kolekcia súborov yaml a SQL načítaných do poľa |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | pole funkcií na transformáciu modelu |
| options.dbdiffOptionsExtra | <code>object</code> | doplnkové možnosti pre dbdiff |
| options.ignoreNameRegex | <code>string</code> | regulárny výraz na ignorovanie objektov podľa názvu |
| options.targetSchema | <code>string</code> | cieľová schéma pre nasadenie |
| options.maxMissingTablesRatio | <code>number</code> | maximálny podiel chýbajúcich tabuliek v databáze. Bezpečnostná kontrola, ak je podiel chýbajúcich vyšší, nasadenie sa zastaví (zabraňuje náhodnému zmazaniu všetkých tabuliek) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
Zmaže všetky databázové objekty

**Druh**: globálna funkcia  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt pripojenia |
| options.systemConnection | <code>object</code> | systémové pripojenie (výsledok driver.connect). Ak nie je zadané, vytvorí sa nové pripojenie |
| options.driver | <code>object</code> | objekt ovládača. Ak nie je zadaný, načíta sa z pripojenia |
| options.analysedStructure | <code>object</code> | analyzovaná štruktúra databázy. Ak nie je zadaná, načíta sa |

<a name="executeQuery"></a>

## executeQuery(options)
Vykoná SQL dotaz

**Druh**: globálna funkcia  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | objekt pripojenia |
| [options.systemConnection] | <code>object</code> | systémové pripojenie (výsledok driver.connect). Ak nie je zadané, vytvorí sa nové pripojenie |
| [options.driver] | <code>object</code> | objekt ovládača. Ak nie je zadaný, načíta sa z pripojenia |
| [options.sql] | <code>string</code> | SQL dotaz |
| [options.sqlFile] | <code>string</code> | SQL súbor |
| [options.logScriptItems] | <code>boolean</code> | či logovať položky skriptu namiesto celého skriptu |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
Vygeneruje dotaz na nasadenie modelu do databázy

**Druh**: globálna funkcia  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt pripojenia |
| options.systemConnection | <code>object</code> | systémové pripojenie (výsledok driver.connect). Ak nie je zadané, vytvorí sa nové pripojenie |
| options.driver | <code>object</code> | objekt ovládača. Ak nie je zadaný, načíta sa z pripojenia |
| options.analysedStructure | <code>object</code> | analyzovaná štruktúra databázy. Ak nie je zadaná, načíta sa |
| options.modelFolder | <code>string</code> | priečinok so súbormi modelu (súbory YAML pre tabuľky, súbory SQL pre pohľady, procedúry, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | načítaný databázový model - kolekcia súborov yaml a SQL načítaných do poľa |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | pole funkcií na transformáciu modelu |
| options.dbdiffOptionsExtra | <code>object</code> | doplnkové možnosti pre dbdiff |
| options.ignoreNameRegex | <code>string</code> | regulárny výraz na ignorovanie objektov podľa názvu |
| options.targetSchema | <code>string</code> | cieľová schéma pre nasadenie |
| options.maxMissingTablesRatio | <code>number</code> | maximálny podiel chýbajúcich tabuliek v databáze. Bezpečnostná kontrola, ak je podiel chýbajúcich vyšší, nasadenie sa zastaví (zabraňuje náhodnému zmazaniu všetkých tabuliek) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Funkcia čítača, ktorá číta súbor alebo URL vo formáte JSNOL. Formát JSONL - textový súbor, každý riadok je riadok zakódovaný v JSON.

**Druh**: globálna funkcia  
**Vracia**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objekt čítača  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | názov súboru alebo URL |
| options.encoding | <code>string</code> | kódovanie súboru |
| options.limitRows | <code>number</code> | maximálny počet riadkov na načítanie |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Vracia objekt zapisovača pre funkciu [copyStream](#copyStream). Tento objekt zapisovača zapisuje dáta do súboru JSONL. Formát JSONL - textový súbor, každý riadok je riadok zakódovaný v JSON, používa ho napr. MongoDB.

**Druh**: globálna funkcia  
**Vracia**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objekt zapisovača  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | názov súboru |
| [options.encoding] | <code>string</code> | kódovanie súboru |
| [options.header] | <code>boolean</code> | či zapisovať hlavičku. Hlavička je JSON popisujúci štruktúru zdrojovej tabuľky. Hlavička je špecifická pre DbGate, ak chcete napr. importovať dáta do MongoDB, hlavičku by ste zapisovať nemali. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Vytvára objekt čítača pre súbor JSON pre funkciu [copyStream](#copyStream).

**Druh**: globálna funkcia  
**Vracia**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objekt čítača  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | názov súboru alebo URL |
| options.jsonStyle | <code>string</code> | 'object' alebo 'array' |
| [options.keyField] | <code>string</code> | kľúčové pole pre štýl object |
| [options.rootField] | <code>string</code> | koreňové pole pre štýl object |
| [options.encoding] | <code>string</code> | kódovanie súboru |
| [options.limitRows] | <code>number</code> | maximálny počet riadkov na načítanie |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Vracia objekt zapisovača pre funkciu [copyStream](#copyStream). Tento objekt zapisovača zapisuje dáta do súboru JSON.

**Druh**: globálna funkcia  
**Vracia**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objekt zapisovača  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | názov súboru |
| [options.jsonStyle] | <code>string</code> | 'object' alebo 'array' |
| [options.keyField] | <code>string</code> | kľúčové pole pre štýl object |
| [options.rootField] | <code>string</code> | koreňové pole pre štýl object |
| [options.encoding] | <code>string</code> | kódovanie súboru |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Vracia objekt čítača pre funkciu [copyStream](#copyStream). Tento objekt čítača číta dáta z dotazu.

**Druh**: globálna funkcia  
**Vracia**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objekt čítača  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt pripojenia |
| options.query | <code>string</code> | SQL dotaz |
| [options.queryType] | <code>string</code> | typ dotazu |
| [options.sql] | <code>string</code> | SQL dotaz. zastarané; použite namiesto toho query |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Vytvára objekt čítača pre funkciu [copyStream](#copyStream). Tento objekt čítača číta dáta z tabuľky alebo pohľadu.

**Druh**: globálna funkcia  
**Vracia**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objekt čítača  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt pripojenia |
| options.systemConnection | <code>object</code> | systémové pripojenie (výsledok driver.connect). Ak nie je zadané, vytvorí sa nové pripojenie |
| options.pureName | <code>string</code> | názov tabuľky |
| options.schemaName | <code>string</code> | názov schémy |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Vytvára objekt zapisovača pre funkciu [copyStream](#copyStream). Tento objekt zapisovača zapisuje dáta do tabuľky. Tabuľka môže byť vytvorená, ak neexistuje.

**Druh**: globálna funkcia  
**Vracia**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objekt zapisovača  

| Parameter | Typ | Popis |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objekt pripojenia |
| options.systemConnection | <code>object</code> | systémové pripojenie (výsledok driver.connect). Ak nie je zadané, vytvorí sa nové pripojenie |
| options.driver | <code>object</code> | objekt ovládača. Ak nie je zadaný, načíta sa z pripojenia |
| options.pureName | <code>string</code> | názov tabuľky |
| options.schemaName | <code>string</code> | názov schémy |
| options.dropIfExists | <code>boolean</code> | zmazať tabuľku, ak existuje |
| options.truncate | <code>boolean</code> | vyprázdniť tabuľku pred vložením |
| options.createIfNotExists | <code>boolean</code> | vytvoriť tabuľku, ak neexistuje |
| options.commitAfterInsert | <code>boolean</code> | potvrdiť transakciu po vložení |

<a name="readerType"></a>

## readerType : <code>Object</code>
Objekt čítača (vstup) pre funkciu [copyStream](#copyStream)

**Druh**: globálna definícia typu  
<a name="writerType"></a>

## writerType : <code>Object</code>
Objekt zapisovača (výstup) pre funkciu [copyStream](#copyStream)

**Druh**: globálna definícia typu  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
Identifikátor databázového enginu v tvare `engine@plugin-package`.

**Druh**: globálna definícia typu  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**Druh**: globálna definícia typu  
**Vlastnosti**

| Názov | Typ |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 
