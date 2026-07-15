---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: it
title: Scripting
weight: 40
---

DbGate è composto da diversi [pacchetti NPM](https://www.npmjs.com/search?q=keywords%3Adbgate), che possono essere utilizzati negli script nodejs

Di solito avrai bisogno di questi pacchetti:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - implementa le funzioni di utilità
* dbgate-plugin-`engine` - insieme di plugin connettori, implementa la connessione al database e le operazioni specifiche del motore di database indicato
* dbgate-plugin-`fileformat` - se utilizzi l'esportazione in CSV o XML, questi provider di formato sono implementati come plugin esterni

[Documentazione dell'API](/it/dbgate/developer/apidoc)

## Generare uno script da DbGate
Molte funzionalità di DbGate sono internamente implementate con l'interfaccia di scripting. Quindi, quando utilizzi qualche operazione di tipo esportazione, da qualche parte c'è un pulsante "Generate Shell script", che genera per te uno script nodejs.

Se vuoi utilizzare uno script nodejs per l'esportazione, puoi seguire questi passaggi:
* Fai clic con il pulsante destro del mouse sulla tabella, scegli "Export/Export advanced"
* Configura la tua esportazione
* Scegli "Generate script" nella barra degli strumenti in basso. Ora puoi modificare lo script JS ed eseguirlo all'interno di DbGate
* Se scegli "Copy nodejs script" nella barra degli strumenti in basso, puoi salvarlo in un file js ed eseguirlo con [nodejs](https://nodejs.org/) installato sul tuo computer


## Esempio 1 - esportare una tabella in CSV
Questo è un esempio semplice, utilizziamo [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) dal pacchetto `dbgateApi` e il writer da `dbgate-plugin-csv`. È necessario anche `dbgate-plugin-mysql`, perché utilizziamo il parametro engine `mysql@dbgate-plugin-mysql`
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
