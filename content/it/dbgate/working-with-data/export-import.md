---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: it
title: Esportazione e importazione
weight: 20
---

DbGate dispone di un sistema di esportazione/importazione flessibile che consente sia semplici esportazioni con un clic sia configurazioni personalizzate complesse.

## Esportazione semplice con un clic

Se non hai bisogno di alcuna configurazione e ti serve solo esportare i dati in un file, puoi usare l'esportazione semplice. Ci sono diversi modi per richiamare l'esportazione semplice:
- Menu contestuale di tabella/vista/collezione, Export
- Dati della tabella, menu contestuale "Export" o pulsante {{<mdi "export" >}}. I filtri vengono applicati anche ai dati esportati
- Risultato della query, menu contestuale "Export" o pulsante {{<mdi "export" >}}

Nell'applicazione desktop puoi salvare direttamente il file esportato.

Nell'applicazione web il file esportato viene offerto per il download.

## Esportazione/importazione avanzata
Se hai bisogno di configurare maggiori dettagli o di esportare più tabelle in un'unica operazione, devi usare "Advanced export".  
Lo stesso strumento di configurazione viene usato per l'importazione, semplicemente con la configurazione di origine e destinazione invertite.

L'esportazione/importazione avanzata può essere richiamata da:
- gli stessi punti dell'esportazione semplice, solo che invece del formato del file scegli "Export advanced..."
- il menu contestuale del database, scegli "Export" o "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} Configurazione dell'origine
* Storage type - scegli l'origine dei dati
  * Database - in questo caso configuri l'"Export"
    * Seleziona più tabelle di origine
  * File (JSON, CSV, DBF...) - in questo caso configuri l'"Import"
    * Apri o trascina il file di origine
  * Query - nella maggior parte dei casi non ti servirà, ma qui puoi digitare direttamente una query. Questa opzione viene usata internamente, ad esempio quando esporti dati filtrati di una tabella.
  * Archive - importa/esporta dati da un [archivio dati](advanced-data-tools/archives)

### {{<mdi "export" >}} Configurazione della destinazione
* Storage type - lo stesso della configurazione dell'origine, ma con significato opposto
  * Database - configuri l'"Import"
  * File (JSON, CSV, DBF...) - configuri l'"Export"

### {{< mdi "table-multiple" >}} Mappatura di tabelle/file di origine
Puoi mappare come i file/le tabelle di input vengono trasformati in output

### Pulsanti di azione
  * {{< mdi "play" >}} Run - esegue il job di importazione/esportazione definito
  * {{< mdi "flash" >}} Generate script - crea codice JavaScript che esegue il job definito. Puoi eseguirlo nella console shell di DbGate, oppure puoi esportarlo in un file ed eseguirlo da riga di comando con nodejs
  * {{< mdi "content-save" >}} Save - salva il job per un uso successivo

## Script di importazione/esportazione
Tutti i job di importazione/esportazione in DbGate vengono dapprima convertiti in script. Segue un esempio di esportazione di una tabella SQLite in CSV.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

Puoi eseguire questo script anche senza DbGate. Usa il menu contestuale nell'editor di script "Copy nodejs script". Verrà copiato il seguente script:

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

Dopo aver installato le dipendenze usate nella cartella con lo script (tutti i pacchetti usati nella funzione require()):

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

Puoi eseguire questo script con il comando:

```sh
node myExportScript.js
```
