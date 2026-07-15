---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: sk
title: Export a import
weight: 20
---

DbGate má flexibilný systém exportu/importu, ktorý umožňuje jednoduché exporty jedným kliknutím aj zložité vlastné nastavenia.

## Jednoduchý export jedným kliknutím

Ak nepotrebujete žiadnu konfiguráciu a chcete iba exportovať dáta do súboru, môžete použiť jednoduchý export. Existuje niekoľko spôsobov, ako jednoduchý export vyvolať:
- Kontextová ponuka tabuľky/pohľadu/kolekcie, Export
- Dáta tabuľky, kontextová ponuka "Export" alebo tlačidlo {{<mdi "export" >}}. Filtre sa uplatnia aj na exportované dáta
- Výsledok dotazu, kontextová ponuka "Export" alebo tlačidlo {{<mdi "export" >}}

V desktopovej aplikácii môžete exportovaný súbor priamo uložiť.

Vo webovej aplikácii je exportovaný súbor ponúknutý na stiahnutie.

## Pokročilý export/import
Ak potrebujete nakonfigurovať viac detailov alebo exportovať viac tabuliek naraz, musíte použiť "Pokročilý export".  
Rovnaký konfiguračný nástroj sa používa aj na import, len s vymenenou konfiguráciou zdroja a cieľa.

Pokročilý export/import je možné vyvolať z:
- rovnakých miest ako jednoduchý export, len namiesto formátu súboru zvoľte "Export advanced..."
- kontextovej ponuky databázy, zvoľte "Export" alebo "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} Konfigurácia zdroja
* Typ úložiska - zvoľte zdroj dát
  * Database - potom konfigurujete "Export"
    * Vyberte viacero zdrojových tabuliek
  * File (JSON, CSV, DBF...) - potom konfigurujete "Import"
    * Otvorte alebo pretiahnite zdrojový súbor
  * Query - vo väčšine prípadov toto nebudete potrebovať, ale môžete tu priamo napísať dotaz. Táto možnosť sa používa interne, keď exportujete napr. filtrované dáta tabuľky.
  * Archive - import/export dát z [dátového archívu](advanced-data-tools/archives)

### {{<mdi "export" >}} Konfigurácia cieľa
* Typ úložiska - rovnaké ako pri konfigurácii zdroja, ale s opačným významom
  * Database - konfigurujete "Import"
  * File (JSON, CSV, DBF...) - konfigurujete "Export"

### {{< mdi "table-multiple" >}} Mapovanie zdrojových tabuliek/súborov
Môžete namapovať, ako sa vstupné súbory/tabuľky transformujú na výstup

### Tlačidlá akcií
  * {{< mdi "play" >}} Run - spustí definovanú úlohu importu/exportu
  * {{< mdi "flash" >}} Generate script - vytvorí JavaScriptový kód, ktorý spúšťa definovanú úlohu. Môžete ho spustiť v konzole DbGate shell alebo ho môžete exportovať do súboru a spustiť z príkazového riadka pomocou nodejs
  * {{< mdi "content-save" >}} Save - uloží úlohu na neskôr

## Skripty importu / exportu
Všetky úlohy importu/exportu sa v DbGate najprv transpilujú do skriptov. Nasleduje príklad exportu SQLite tabuľky do CSV.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

Tento skript môžete spustiť aj bez DbGate. Použite kontextovú ponuku v editore skriptov "Copy nodejs script". Skopíruje sa nasledujúci skript:

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

Po nainštalovaní použitých závislostí v priečinku so skriptom (všetky balíky použité vo funkcii require()):

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

Tento skript môžete spustiť príkazom:

```sh
node myExportScript.js
```