---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: sk
title: Skriptovanie
weight: 40
---

DbGate sa skladá z niekoľkých [NPM balíkov](https://www.npmjs.com/search?q=keywords%3Adbgate), ktoré je možné použiť v nodejs skriptoch

Zvyčajne budete potrebovať tieto balíky:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - implementuje pomocné funkcie
* dbgate-plugin-`engine` - sada konektorových pluginov, implementuje pripojenie k databáze a operácie špecifické pre daný databázový engine
* dbgate-plugin-`fileformat` - ak používate export do CSV alebo XML, tieto poskytovatelia formátov sú implementovaní ako externé pluginy

[Dokumentácia API](/sk/dbgate/developer/apidoc)

## Generovanie skriptu z DbGate
Množstvo funkcií DbGate je interne implementovaných pomocou skriptovacieho rozhrania. Takže keď používate nejakú operáciu typu export, niekde sa nachádza tlačidlo "Generate Shell script", ktoré vygeneruje nodejs skript za vás.

Ak chcete použiť nodejs skript na export, môžete použiť nasledujúce kroky:
* Kliknite pravým tlačidlom na tabuľku, zvoľte "Export/Export advanced"
* Nakonfigurujte svoj export
* Zvoľte "Generate script" v spodnom paneli nástrojov. Teraz môžete upraviť JS skript a spustiť ho vnútri DbGate
* Ak zvolíte "Copy nodejs script" v spodnom paneli nástrojov, môžete to uložiť do js súboru a spustiť pomocou [nodejs](https://nodejs.org/) nainštalovaného na vašom počítači


## Príklad 1 - export tabuľky do CSV
Toto je jednoduchý príklad, používame [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) z balíka `dbgateApi` a writer z `dbgate-plugin-csv`. Taktiež je potrebný `dbgate-plugin-mysql`, pretože používame parameter engine `mysql@dbgate-plugin-mysql`
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
