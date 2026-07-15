---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: cs
title: Skriptování
weight: 40
---

DbGate se skládá z několika [NPM balíčků](https://www.npmjs.com/search?q=keywords%3Adbgate), které lze použít ve skriptech pro nodejs

Typicky budete potřebovat tyto balíčky:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - implementuje pomocné funkce
* dbgate-plugin-`engine` - sada konektorových pluginů, implementuje připojení k databázi a operace specifické pro daný databázový engine
* dbgate-plugin-`fileformat` - pokud používáte export do CSV nebo XML, tito poskytovatelé formátů jsou implementováni jako externí pluginy

[Dokumentace API](/cs/dbgate/developer/apidoc)

## Generování skriptu z DbGate
Spousta funkcí DbGate je interně implementována pomocí skriptovacího rozhraní. Takže když používáte nějakou operaci typu export, je někde tlačítko "Generate Shell script", které pro vás vygeneruje nodejs skript.

Pokud chcete pro export použít nodejs skript, můžete použít následující kroky:
* Klikněte pravým tlačítkem na tabulku a zvolte "Export/Export advanced"
* Nakonfigurujte svůj export
* Zvolte "Generate script" ve spodním panelu nástrojů. Nyní můžete JS skript upravit a spustit uvnitř DbGate
* Pokud zvolíte "Copy nodejs script" ve spodním panelu nástrojů, můžete tento skript uložit do js souboru a spustit ho pomocí [nodejs](https://nodejs.org/) nainstalovaného na vašem počítači


## Příklad 1 - export tabulky do CSV
Toto je jednoduchý příklad, používáme [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) z balíčku `dbgateApi` a writer z `dbgate-plugin-csv`. Také je vyžadován `dbgate-plugin-mysql`, protože používáme parametr engine `mysql@dbgate-plugin-mysql`
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
