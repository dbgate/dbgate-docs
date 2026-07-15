---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: fr
title: Scripting
weight: 40
---

DbGate est composé de plusieurs [paquets NPM](https://www.npmjs.com/search?q=keywords%3Adbgate), qui peuvent être utilisés dans des scripts nodejs

En règle générale, vous aurez besoin de ces paquets :
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - implémente les fonctions utilitaires
* dbgate-plugin-`engine` - ensemble de plugins de connexion, implémente la connexion à la base de données et les opérations spécifiques au moteur de base de données donné
* dbgate-plugin-`fileformat` - si vous utilisez l'export vers CSV ou XML, ces fournisseurs de format sont implémentés sous forme de plugins externes

[Documentation de l'API](/fr/dbgate/developer/apidoc)

## Générer un script depuis DbGate
De nombreuses fonctionnalités de DbGate sont implémentées en interne à l'aide de l'interface de scripting. Ainsi, lorsque vous utilisez une opération de type export, il y a quelque part un bouton « Generate Shell script », qui génère un script nodejs pour vous.

Si vous souhaitez utiliser un script nodejs pour l'export, vous pouvez suivre ces étapes :
* Faites un clic droit sur la table, choisissez « Export/Export advanced »
* Configurez votre export
* Choisissez « Generate script » dans la barre d'outils en bas. Vous pouvez maintenant modifier le script JS et l'exécuter dans DbGate
* Si vous choisissez « Copy nodejs script » dans la barre d'outils en bas, vous pouvez l'enregistrer dans un fichier js et l'exécuter avec [nodejs](https://nodejs.org/) installé sur votre ordinateur


## Exemple 1 - exporter une table vers CSV
Il s'agit d'un exemple simple, nous utilisons [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) du paquet `dbgateApi` et le writer de `dbgate-plugin-csv`. `dbgate-plugin-mysql` est également requis, car nous utilisons le paramètre engine `mysql@dbgate-plugin-mysql`
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
