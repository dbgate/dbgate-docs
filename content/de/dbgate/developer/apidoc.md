---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: de
layout: docs
title: API-Dokumentation
weight: 20
---

## Funktionen

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Kopiert den Reader in den Writer. Wird für den Import und Export von Tabellen sowie für die Datenübertragung zwischen Tabellen verwendet</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>Stellt das im modelFolder gespeicherte Datenbankmodell (Tabellen als YAML-Dateien) in der Datenbank bereit</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Löscht alle Datenbankobjekte</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>Führt eine SQL-Abfrage aus</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>Generiert eine Abfrage für die Bereitstellung des Modells in der Datenbank</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Reader-Funktion, die eine JSONL-Datei oder eine URL liest. JSONL-Format – Textdatei, wobei jede Zeile eine JSON-codierte Zeile ist.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Gibt ein Writer-Objekt für die Funktion <a href="#copyStream">copyStream</a> zurück. Dieses Writer-Objekt schreibt Daten in eine JSONL-Datei. JSONL-Format – Textdatei, wobei jede Zeile eine JSON-codierte Zeile ist, verwendet z. B. von MongoDB.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Erstellt ein Reader-Objekt für eine JSON-Datei für die Funktion <a href="#copyStream">copyStream</a>.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Gibt ein Writer-Objekt für die Funktion <a href="#copyStream">copyStream</a> zurück. Dieses Writer-Objekt schreibt Daten in eine JSON-Datei.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Gibt ein Reader-Objekt für die Funktion <a href="#copyStream">copyStream</a> zurück. Dieses Reader-Objekt liest Daten aus einer Abfrage.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Erstellt ein Reader-Objekt für die Funktion <a href="#copyStream">copyStream</a>. Dieses Reader-Objekt liest Daten aus einer Tabelle oder einer View.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Erstellt ein Writer-Objekt für die Funktion <a href="#copyStream">copyStream</a>. Dieses Writer-Objekt schreibt Daten in eine Tabelle. Die Tabelle kann erstellt werden, falls sie nicht existiert.</p>
</dd>
</dl>

## Typedefs

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>Reader-Objekt (Eingabe) für die Funktion <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>Writer-Objekt (Ausgabe) für die Funktion <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>Typ der Benutzerrolle.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
Kopiert den Reader in den Writer. Wird für den Import und Export von Tabellen sowie für die Datenübertragung zwischen Tabellen verwendet

**Kind**: globale Funktion  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | Reader-Objekt |
| output | [<code>writerType</code>](#writerType) | Writer-Objekt |
| options | <code>object</code> | Optionen |

<a name="deployDb"></a>

## deployDb(options)
Stellt das im modelFolder gespeicherte Datenbankmodell (Tabellen als YAML-Dateien) in der Datenbank bereit

**Kind**: globale Funktion  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | Verbindungsobjekt |
| options.systemConnection | <code>object</code> | Systemverbindung (Ergebnis von driver.connect). Wenn nicht angegeben, wird eine neue Verbindung erstellt |
| options.driver | <code>object</code> | Treiberobjekt. Wenn nicht angegeben, wird es aus der Verbindung geladen |
| options.analysedStructure | <code>object</code> | analysierte Struktur der Datenbank. Wenn nicht angegeben, wird sie geladen |
| options.modelFolder | <code>string</code> | Ordner mit Modelldateien (YAML-Dateien für Tabellen, SQL-Dateien für Views, Prozeduren, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | geladenes Datenbankmodell – Sammlung von YAML- und SQL-Dateien, die in ein Array geladen wurden |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | Array von Funktionen zum Transformieren des Modells |
| options.dbdiffOptionsExtra | <code>object</code> | zusätzliche Optionen für dbdiff |
| options.ignoreNameRegex | <code>string</code> | Regex zum Ignorieren von Objekten anhand des Namens |
| options.targetSchema | <code>string</code> | Zielschema für die Bereitstellung |
| options.maxMissingTablesRatio | <code>number</code> | maximaler Anteil fehlender Tabellen in der Datenbank. Sicherheitsprüfung: Wenn der Anteil höher ist, wird die Bereitstellung gestoppt (verhindert das versehentliche Löschen aller Tabellen) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
Löscht alle Datenbankobjekte

**Kind**: globale Funktion  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | Verbindungsobjekt |
| options.systemConnection | <code>object</code> | Systemverbindung (Ergebnis von driver.connect). Wenn nicht angegeben, wird eine neue Verbindung erstellt |
| options.driver | <code>object</code> | Treiberobjekt. Wenn nicht angegeben, wird es aus der Verbindung geladen |
| options.analysedStructure | <code>object</code> | analysierte Struktur der Datenbank. Wenn nicht angegeben, wird sie geladen |

<a name="executeQuery"></a>

## executeQuery(options)
Führt eine SQL-Abfrage aus

**Kind**: globale Funktion  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | Verbindungsobjekt |
| [options.systemConnection] | <code>object</code> | Systemverbindung (Ergebnis von driver.connect). Wenn nicht angegeben, wird eine neue Verbindung erstellt |
| [options.driver] | <code>object</code> | Treiberobjekt. Wenn nicht angegeben, wird es aus der Verbindung geladen |
| [options.sql] | <code>string</code> | SQL-Abfrage |
| [options.sqlFile] | <code>string</code> | SQL-Datei |
| [options.logScriptItems] | <code>boolean</code> | ob Skriptelemente anstelle des gesamten Skripts protokolliert werden sollen |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
Generiert eine Abfrage für die Bereitstellung des Modells in der Datenbank

**Kind**: globale Funktion  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | Verbindungsobjekt |
| options.systemConnection | <code>object</code> | Systemverbindung (Ergebnis von driver.connect). Wenn nicht angegeben, wird eine neue Verbindung erstellt |
| options.driver | <code>object</code> | Treiberobjekt. Wenn nicht angegeben, wird es aus der Verbindung geladen |
| options.analysedStructure | <code>object</code> | analysierte Struktur der Datenbank. Wenn nicht angegeben, wird sie geladen |
| options.modelFolder | <code>string</code> | Ordner mit Modelldateien (YAML-Dateien für Tabellen, SQL-Dateien für Views, Prozeduren, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | geladenes Datenbankmodell – Sammlung von YAML- und SQL-Dateien, die in ein Array geladen wurden |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | Array von Funktionen zum Transformieren des Modells |
| options.dbdiffOptionsExtra | <code>object</code> | zusätzliche Optionen für dbdiff |
| options.ignoreNameRegex | <code>string</code> | Regex zum Ignorieren von Objekten anhand des Namens |
| options.targetSchema | <code>string</code> | Zielschema für die Bereitstellung |
| options.maxMissingTablesRatio | <code>number</code> | maximaler Anteil fehlender Tabellen in der Datenbank. Sicherheitsprüfung: Wenn der Anteil höher ist, wird die Bereitstellung gestoppt (verhindert das versehentliche Löschen aller Tabellen) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Reader-Funktion, die eine JSONL-Datei oder eine URL liest. JSONL-Format – Textdatei, wobei jede Zeile eine JSON-codierte Zeile ist.

**Kind**: globale Funktion  
**Rückgabewert**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - Reader-Objekt  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | Dateiname oder URL |
| options.encoding | <code>string</code> | Codierung der Datei |
| options.limitRows | <code>number</code> | maximale Anzahl der zu lesenden Zeilen |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Gibt ein Writer-Objekt für die Funktion [copyStream](#copyStream) zurück. Dieses Writer-Objekt schreibt Daten in eine JSONL-Datei. JSONL-Format – Textdatei, wobei jede Zeile eine JSON-codierte Zeile ist, verwendet z. B. von MongoDB.

**Kind**: globale Funktion  
**Rückgabewert**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - Writer-Objekt  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | Dateiname |
| [options.encoding] | <code>string</code> | Codierung der Datei |
| [options.header] | <code>boolean</code> | ob ein Header geschrieben werden soll. Der Header ist JSON, das die Struktur der Quelltabelle beschreibt. Der Header ist spezifisch für DbGate; wenn Sie z. B. Daten in MongoDB importieren möchten, sollten Sie keinen Header schreiben. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Erstellt ein Reader-Objekt für eine JSON-Datei für die Funktion [copyStream](#copyStream).

**Kind**: globale Funktion  
**Rückgabewert**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - Reader-Objekt  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | Dateiname oder URL |
| options.jsonStyle | <code>string</code> | 'object' oder 'array' |
| [options.keyField] | <code>string</code> | Schlüsselfeld für den Object-Stil |
| [options.rootField] | <code>string</code> | Root-Feld für den Object-Stil |
| [options.encoding] | <code>string</code> | Codierung der Datei |
| [options.limitRows] | <code>number</code> | maximale Anzahl der zu lesenden Zeilen |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Gibt ein Writer-Objekt für die Funktion [copyStream](#copyStream) zurück. Dieses Writer-Objekt schreibt Daten in eine JSON-Datei.

**Kind**: globale Funktion  
**Rückgabewert**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - Writer-Objekt  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | Dateiname |
| [options.jsonStyle] | <code>string</code> | 'object' oder 'array' |
| [options.keyField] | <code>string</code> | Schlüsselfeld für den Object-Stil |
| [options.rootField] | <code>string</code> | Root-Feld für den Object-Stil |
| [options.encoding] | <code>string</code> | Codierung der Datei |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Gibt ein Reader-Objekt für die Funktion [copyStream](#copyStream) zurück. Dieses Reader-Objekt liest Daten aus einer Abfrage.

**Kind**: globale Funktion  
**Rückgabewert**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - Reader-Objekt  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | Verbindungsobjekt |
| options.query | <code>string</code> | SQL-Abfrage |
| [options.queryType] | <code>string</code> | Abfragetyp |
| [options.sql] | <code>string</code> | SQL-Abfrage. veraltet; verwenden Sie stattdessen query |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Erstellt ein Reader-Objekt für die Funktion [copyStream](#copyStream). Dieses Reader-Objekt liest Daten aus einer Tabelle oder einer View.

**Kind**: globale Funktion  
**Rückgabewert**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - Reader-Objekt  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | Verbindungsobjekt |
| options.systemConnection | <code>object</code> | Systemverbindung (Ergebnis von driver.connect). Wenn nicht angegeben, wird eine neue Verbindung erstellt |
| options.pureName | <code>string</code> | Tabellenname |
| options.schemaName | <code>string</code> | Schemaname |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Erstellt ein Writer-Objekt für die Funktion [copyStream](#copyStream). Dieses Writer-Objekt schreibt Daten in eine Tabelle. Die Tabelle kann erstellt werden, falls sie nicht existiert.

**Kind**: globale Funktion  
**Rückgabewert**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - Writer-Objekt  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | Verbindungsobjekt |
| options.systemConnection | <code>object</code> | Systemverbindung (Ergebnis von driver.connect). Wenn nicht angegeben, wird eine neue Verbindung erstellt |
| options.driver | <code>object</code> | Treiberobjekt. Wenn nicht angegeben, wird es aus der Verbindung geladen |
| options.pureName | <code>string</code> | Tabellenname |
| options.schemaName | <code>string</code> | Schemaname |
| options.dropIfExists | <code>boolean</code> | Tabelle löschen, falls sie existiert |
| options.truncate | <code>boolean</code> | Tabelle vor dem Einfügen leeren |
| options.createIfNotExists | <code>boolean</code> | Tabelle erstellen, falls sie nicht existiert |
| options.commitAfterInsert | <code>boolean</code> | Transaktion nach dem Einfügen committen |

<a name="readerType"></a>

## readerType : <code>Object</code>
Reader-Objekt (Eingabe) für die Funktion [copyStream](#copyStream)

**Kind**: globales Typedef  
<a name="writerType"></a>

## writerType : <code>Object</code>
Writer-Objekt (Ausgabe) für die Funktion [copyStream](#copyStream)

**Kind**: globales Typedef  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
Der Bezeichner der Datenbank-Engine in der Form `engine@plugin-package`.

**Kind**: globales Typedef  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**Kind**: globales Typedef  
**Eigenschaften**

| Name | Typ |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 
