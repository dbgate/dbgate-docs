---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: de
title: Export & Import
weight: 20
---

DbGate verfügt über ein flexibles Export-/Import-System, das sowohl einfache Exporte mit einem Klick als auch komplexe benutzerdefinierte Konfigurationen ermöglicht.

## Einfacher Export mit einem Klick

Wenn Sie keine Konfiguration benötigen und Daten lediglich in eine Datei exportieren möchten, können Sie den einfachen Export verwenden. Es gibt mehrere Möglichkeiten, den einfachen Export aufzurufen:
- Kontextmenü einer Tabelle/View/Collection, "Export"
- Tabellendaten, Kontextmenü "Export" oder Schaltfläche {{<mdi "export" >}}. Filter werden auch auf die exportierten Daten angewendet
- Abfrageergebnis, Kontextmenü "Export" oder Schaltfläche {{<mdi "export" >}}

In der Desktop-Anwendung können Sie die exportierte Datei direkt speichern.

In der Web-App wird die exportierte Datei zum Download angeboten.

## Erweiterter Export/Import
Wenn Sie weitere Details konfigurieren oder mehrere Tabellen in einem Durchgang exportieren möchten, müssen Sie den "Erweiterten Export" verwenden.  
Dasselbe Konfigurationswerkzeug wird auch für den Import verwendet, lediglich mit vertauschter Quell- und Zielkonfiguration.

Der erweiterte Export/Import kann aufgerufen werden über:
- dieselben Stellen wie der einfache Export, wählen Sie nur statt eines Dateiformats "Export advanced..."
- das Kontextmenü der Datenbank, wählen Sie "Export" oder "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} Quellkonfiguration
* Speichertyp - wählen Sie die Datenquelle
  * Datenbank - dann konfigurieren Sie einen "Export"
    * Wählen Sie mehrere Quelltabellen aus
  * Datei (JSON, CSV, DBF...) - dann konfigurieren Sie einen "Import"
    * Öffnen Sie die Quelldatei oder ziehen Sie sie per Drag & Drop hinein
  * Abfrage - in den meisten Fällen benötigen Sie dies nicht, Sie können hier jedoch direkt eine Abfrage eingeben. Diese Option wird intern verwendet, wenn Sie z. B. gefilterte Tabellendaten exportieren.
  * Archiv - Daten aus einem [Datenarchiv](advanced-data-tools/archives) importieren/exportieren

### {{<mdi "export" >}} Zielkonfiguration
* Speichertyp - genauso wie bei der Quellkonfiguration, jedoch mit umgekehrter Bedeutung
  * Datenbank - Sie konfigurieren einen "Import"
  * Datei (JSON, CSV, DBF...) - Sie konfigurieren einen "Export"

### {{< mdi "table-multiple" >}} Quelltabellen/-dateien zuordnen
Sie können festlegen, wie Eingabedateien/-tabellen in die Ausgabe transformiert werden

### Aktionsschaltflächen
  * {{< mdi "play" >}} Run - führt den definierten Import-/Export-Job aus
  * {{< mdi "flash" >}} Generate script - erzeugt JavaScript-Code, der den definierten Job ausführt. Sie können ihn in der DbGate-Shell-Konsole ausführen oder in eine Datei exportieren und über die Kommandozeile mit Node.js ausführen
  * {{< mdi "content-save" >}} Save - speichert den Job für später

## Import-/Export-Skripte
Alle Import-/Export-Jobs in DbGate werden zunächst in Skripte übersetzt. Es folgt ein Beispiel für den Export einer SQLite-Tabelle nach CSV.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

Sie können dieses Skript auch ohne DbGate ausführen. Verwenden Sie im Skript-Editor das Kontextmenü "Copy nodejs script". Damit wird folgendes Skript kopiert:

```js

const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginSqlite = require('dbgate-plugin-sqlite');
const dbgatePluginCsv = require('dbgate-plugin-csv');
dbgateApi.registerPlugins(dbgatePluginSqlite,dbgatePluginCsv);

require=null;
async function run() {

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);


await dbgateApi.finalizer.run();
console.log('Finished job script');
}
dbgateApi.runScript(run);
```

Nachdem Sie die verwendeten Abhängigkeiten im Ordner mit dem Skript installiert haben (alle in der Funktion require() verwendeten Pakete):

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

können Sie dieses Skript mit folgendem Befehl ausführen:

```sh
node myExportScript.js
```
