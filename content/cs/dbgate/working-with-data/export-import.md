---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: cs
title: Export a import
weight: 20
---

DbGate má flexibilní systém exportu/importu, který umožňuje jak jednoduché exporty na jedno kliknutí, tak složitá vlastní nastavení.

## Jednoduchý export na jedno kliknutí

Pokud nepotřebujete žádnou konfiguraci a chcete pouze exportovat data do souboru, můžete použít jednoduchý export. Jednoduchý export lze vyvolat několika způsoby:
- Kontextové menu tabulky/pohledu/kolekce, Export
- Data tabulky, kontextové menu "Export" nebo tlačítko {{<mdi "export" >}}. Na exportovaná data se aplikují také filtry
- Výsledek dotazu, kontextové menu "Export" nebo tlačítko {{<mdi "export" >}}

V desktopové aplikaci můžete exportovaný soubor uložit přímo.

Ve webové aplikaci je exportovaný soubor nabídnut ke stažení.

## Pokročilý export/import
Pokud potřebujete nakonfigurovat více detailů nebo exportovat více tabulek najednou, musíte použít "Pokročilý export".  
Stejný konfigurační nástroj se používá i pro import, jen s prohozenou konfigurací zdroje a cíle.

Pokročilý export/import lze vyvolat z:
- stejných míst jako jednoduchý export, jen místo formátu souboru zvolte "Export advanced..."
- kontextového menu databáze, zvolte "Export" nebo "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} Konfigurace zdroje
* Typ úložiště - zvolte zdroj dat
  * Databáze - poté konfigurujete "Export"
    * Vyberte více zdrojových tabulek
  * Soubor (JSON, CSV, DBF...) - poté konfigurujete "Import"
    * Otevřete nebo přetáhněte zdrojový soubor
  * Dotaz - ve většině případů toto nebudete potřebovat, ale můžete zde zadat dotaz přímo. Tato volba se interně používá, když exportujete např. filtrovaná data tabulky.
  * Archiv - import/export dat z [datového archivu](advanced-data-tools/archives)

### {{<mdi "export" >}} Konfigurace cíle
* Typ úložiště - stejné jako u konfigurace zdroje, ale s opačným významem
  * Databáze - konfigurujete "Import"
  * Soubor (JSON, CSV, DBF...) - konfigurujete "Export"

### {{< mdi "table-multiple" >}} Mapování zdrojových tabulek/souborů
Můžete namapovat, jak jsou vstupní soubory/tabulky transformovány na výstup

### Akční tlačítka
  * {{< mdi "play" >}} Run - spustí definovanou úlohu importu/exportu
  * {{< mdi "flash" >}} Generate script - vytvoří JavaScriptový kód spouštějící definovanou úlohu. Můžete jej spustit v konzoli DbGate shell, nebo jej můžete exportovat do souboru a spustit z příkazové řádky pomocí nodejs
  * {{< mdi "content-save" >}} Save - uloží úlohu pro pozdější použití

## Skripty pro import / export
Všechny úlohy importu/exportu jsou v DbGate nejprve přeloženy do skriptů. Následuje příklad exportu SQLite tabulky do CSV.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

Tento skript můžete spustit i bez DbGate. Použijte kontextové menu v editoru skriptů "Copy nodejs script". Zkopíruje se následující skript:

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

Po instalaci použitých závislostí ve složce se skriptem (všechny balíčky použité ve funkci require()):

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

Tento skript můžete spustit příkazem:

```sh
node myExportScript.js
```