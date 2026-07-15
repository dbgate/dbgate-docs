---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: de
title: Datenbank-Deployment
weight: 10
---

*Die Deploy-Funktionalität wird in einem der nächsten Releases erheblich geändert, diese Dokumentation bezieht sich auf die neueste BETA-Version*

DbGate bietet einen Mechanismus für das automatische Deployment von Datenbanken. Während der traditionelle Weg dazu Migrations-SQL-Skripte verwendet, geht DbGate standardmäßig einen anderen Weg (Migrationsskripte werden ebenfalls unterstützt).
Sie definieren das DB-Modell mit YAML-Dateien, die die Tabellenstruktur und Listendaten beschreiben, sowie mit SQL-Dateien, die Views, Stored Procedures und Funktionen beschreiben. Dieses Modell wird in die Datenbank deployt, wobei die aktuelle Struktur mit der Struktur im Modell verglichen wird, fehlende Spalten und Tabellen angelegt und View- und Prozedur-Definitionen aktualisiert werden. Es werden **keine destruktiven Aktionen** (die zu Datenverlust führen könnten) ausgeführt, wenn Sie also eine Spalte oder Tabelle aus dem Modell entfernen, bleibt sie in der Datenbank erhalten. Wenn Sie eine Spalte im Modell umbenennen, wird eine neue Spalte mit dem neuen Namen erstellt und die alte Spalte bleibt in der Datenbank erhalten.

Das Deployment kann über die Kommandozeile (mit Node-Skripten) oder über die DbGate GUI ausgelöst werden. Sie können auch die Funktion zum Vergleichen von Datenbanken verwenden, um Unterschiede zwischen Modell und realer Datenbank visuell zu vergleichen.

## YAML-Format für Tabellen

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

- Namen werden ohne Schemanamen definiert, ein Modell beschreibt ein Schema
- Standardwerte werden als SQL-Ausdrücke definiert, wenn Sie also eine Zeichenkette definieren möchten, müssen Sie 'einfache Anführungszeichen' verwenden
- Sie können statische Daten für eine Tabelle definieren

### Verwendung von Migrationsskripten
Sie können traditionellere Migrationsskripte mit dem DbGate-spezifischen Deploy-Management kombinieren, einige speziellere Objekte können mit Migrationsskripten erstellt werden.
Die Skripttypen werden anhand der Dateiendung bestimmt, die Verzeichnisstruktur liegt in der Wahl des Benutzers, DbGate wird davon nicht beeinflusst.

Die folgenden Skript-Endungen werden unterstützt:
- `*.predeploy.sql` - Skripte werden vor jedem Deploy-Vorgang ausgeführt
- `*.install.sql` - Skripte werden nur ausgeführt, wenn sie sich vom vorherigen Deployment unterscheiden
- `*.uninstall.sql` - dieses Skript ist mit einer `.install.sql`-Datei gepaart und wird ausgeführt, bevor die neue Version der `*.install.sql`-Datei ausgeführt wird
- `*.once.sql` - Skripte werden nur einmal ausgeführt
- `*.postdeploy.sql` - Skripte werden vor jedem Deploy-Vorgang ausgeführt

DbGate verwendet die Tabelle `dbgate_deploy_journal`, um die in die Datenbank deployten Deploy-Skripte zu verfolgen. Diese Tabelle wird automatisch erstellt, wenn Sie ein Projekt mit mindestens einem Migrationsskript deployen.


### Verwendung in der DbGate GUI

- Wählen Sie in den Verbindungen im Kontextmenü der Datenbank "Export DB model" (nur Premium). Das DB-Modell wird in ein Verzeichnis oder in eine Datei gespeichert. Wenn Sie die Deploy-Funktionalität nutzen möchten, wählen Sie als Ziel Data archive oder Folder (YAML + SQL).
- Öffnen Sie das Archiv-Widget, dort sollten Sie das heruntergeladene Modell sehen
- Im Kontextmenü des Modells können Sie einige Operationen mit dem Modell durchführen:
    - Generate deploy DB SQL - vergleicht die aktuelle Datenbank (Sie sehen sie in der Statusleiste) und generiert ein SQL-Skript, das die Änderungen aus dem Modell in die aktuelle Datenbank deployt
    - Shell: Deploy DB - generiert eine JavaScript-Shell, die zum Deployen der DB verwendet werden kann
    - Compare with {current database} - vergleicht die aktuelle Datenbank grafisch mit dem Modell (nur Premium)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### Verwendung über die Kommandozeile
Kopieren Sie das folgende Skript in die Datei deploy.js und passen Sie die Datenbankkonfiguration an. Außerdem sollten Sie modelFolder entsprechend dem Speicherort Ihres Modellordners ändern.
Zum Ausführen dieses Skripts muss [NodeJs](https://nodejs.org/) auf Ihrem Computer installiert sein.

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

Installieren Sie dann die erforderlichen Module, indem Sie die Befehle im Verzeichnis mit deploy.js ausführen:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

Führen Sie das Datenbank-Deployment mit folgendem Befehl aus:
```sh
node deploy.js
```

Dieses Skript ist für PostgreSQL, andere Datenbank-Engines erfordern Änderungen am Treiber.

Dieses Skript kann auch automatisch aus der DbGate GUI generiert werden. Verwenden Sie das Kontextmenü "Shell: Deploy DB" im Archivordner, danach kopiert "Copy nodejs script" im generierten Skript ein gültiges Skript. Alle Pakete, die im require-Befehl verwendet werden, müssen mit npm install installiert werden.
