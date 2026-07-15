---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: de
title: Skripting
weight: 40
---

DbGate besteht aus mehreren [NPM-Paketen](https://www.npmjs.com/search?q=keywords%3Adbgate), die in nodejs-Skripten verwendet werden können

Typischerweise benötigen Sie diese Pakete:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - implementiert Hilfsfunktionen
* dbgate-plugin-`engine` - Satz von Connector-Plugins, implementiert die Verbindung zur Datenbank und Operationen, die für die jeweilige Datenbank-Engine spezifisch sind
* dbgate-plugin-`fileformat` - wenn Sie den Export nach CSV oder XML verwenden, sind diese Formatanbieter als externe Plugins implementiert

[Dokumentation der API](/de/dbgate/developer/apidoc)

## Skript aus DbGate generieren
Viele Funktionen von DbGate sind intern mit der Skripting-Schnittstelle implementiert. Wenn Sie also eine exportähnliche Operation verwenden, gibt es irgendwo eine Schaltfläche "Generate Shell script", die ein nodejs-Skript für Sie generiert.

Wenn Sie ein nodejs-Skript zum Exportieren verwenden möchten, können Sie die folgenden Schritte ausführen:
* Klicken Sie mit der rechten Maustaste auf die Tabelle und wählen Sie "Export/Export advanced"
* Konfigurieren Sie Ihren Export
* Wählen Sie "Generate script" in der unteren Symbolleiste. Jetzt können Sie das JS-Skript bearbeiten und in DbGate ausführen
* Wenn Sie "Copy nodejs script" in der unteren Symbolleiste wählen, können Sie dies in einer js-Datei speichern und mit [nodejs](https://nodejs.org/) ausführen, das auf Ihrem Computer installiert ist


## Beispiel 1 - Tabelle nach CSV exportieren
Dies ist ein einfaches Beispiel, wir verwenden [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) aus dem Paket `dbgateApi` und den Writer aus `dbgate-plugin-csv`. Außerdem ist `dbgate-plugin-mysql` erforderlich, da wir den Engine-Parameter `mysql@dbgate-plugin-mysql` verwenden
```js
const dbgateApi = require('dbgate-api');
const dbgatePluginMysql = require("dbgate-plugin-mysql");
const dbgatePluginCsv = require("dbgate-plugin-csv");

dbgateApi.registerPlugins(dbgatePluginMysql);

async function run() {
  const reader = await dbgateApi.tableReader({
    connection: { server: 'localhost', engine: 'mysql@dbgate-plugin-mysql', user: 'root', password: 'xxxx', database: 'Chinook' },
    pureName: 'Customer',
  });
  const writer = await dbgatePluginCsv.shellApi.writer({ fileName: 'Customer.csv' });
  await dbgateApi.copyStream(reader, writer);

  console.log('Finished job script');
}
dbgateApi.runScript(run);
```
