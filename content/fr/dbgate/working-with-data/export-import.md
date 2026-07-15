---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: fr
title: Export et import
weight: 20
---

DbGate dispose d'un système d'export/import flexible permettant aussi bien des exports simples en un clic que des configurations personnalisées complexes.

## Export simple en un clic

Si vous n'avez besoin d'aucune configuration et souhaitez simplement exporter des données vers un fichier, vous pouvez utiliser l'export simple. Il existe plusieurs façons d'invoquer l'export simple :
- Menu contextuel d'une table/vue/collection, Export
- Données de la table, menu contextuel "Export" ou bouton {{<mdi "export" >}}. Les filtres sont également appliqués aux données exportées
- Résultat d'une requête, menu contextuel "Export" ou bouton {{<mdi "export" >}}

Dans l'application de bureau, vous pouvez enregistrer directement le fichier exporté.

Dans l'application web, le fichier exporté est proposé au téléchargement.

## Export/import avancé
Si vous devez configurer plus de détails ou exporter plusieurs tables en une seule fois, vous devez utiliser l'"Export avancé".  
Le même outil de configuration est utilisé pour l'import, simplement avec la source et la cible inversées.

L'export/import avancé peut être invoqué depuis :
- les mêmes endroits que l'export simple, il suffit de choisir "Export advanced..." au lieu d'un format de fichier
- le menu contextuel de la base de données, en choisissant "Export" ou "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} Configuration de la source
* Type de stockage - choisissez la source des données
  * Base de données - vous configurez alors un "Export"
    * Sélectionnez plusieurs tables sources
  * Fichier (JSON, CSV, DBF...) - vous configurez alors un "Import"
    * Ouvrez ou glissez-déposez le fichier source
  * Requête - dans la plupart des cas, vous n'en aurez pas besoin, mais vous pouvez saisir une requête directement ici. Cette option est utilisée en interne lorsque vous exportez par exemple les données filtrées d'une table.
  * Archive - importez/exportez des données depuis une [archive de données](advanced-data-tools/archives)

### {{<mdi "export" >}} Configuration de la cible
* Type de stockage - identique à la configuration de la source, mais avec la signification opposée
  * Base de données - vous configurez un "Import"
  * Fichier (JSON, CSV, DBF...) - vous configurez un "Export"

### {{< mdi "table-multiple" >}} Mapper les tables/fichiers sources
Vous pouvez définir comment les fichiers/tables d'entrée sont transformés en sortie

### Boutons d'action
  * {{< mdi "play" >}} Run - exécute la tâche d'import/export définie
  * {{< mdi "flash" >}} Generate script - crée un code JavaScript exécutant la tâche définie. Vous pouvez l'exécuter dans la console shell de DbGate, ou l'exporter vers un fichier et l'exécuter en ligne de commande avec nodejs
  * {{< mdi "content-save" >}} Save - enregistre la tâche pour plus tard

## Scripts d'import / export
Toutes les tâches d'import/export dans DbGate sont d'abord transpilées en scripts. Voici un exemple d'export d'une table SQLite vers CSV.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

Vous pouvez également exécuter ce script sans DbGate. Utilisez le menu contextuel de l'éditeur de scripts "Copy nodejs script". Cela copiera le script suivant :

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

Après avoir installé les dépendances utilisées dans le dossier contenant le script (tous les paquets utilisés dans la fonction require()) :

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

Vous pouvez exécuter ce script avec la commande :

```sh
node myExportScript.js
```