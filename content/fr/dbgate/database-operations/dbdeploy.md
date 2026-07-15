---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: fr
title: Déploiement de base de données
weight: 10
---

*La fonctionnalité de déploiement sera considérablement modifiée dans la prochaine version, cette documentation concerne la dernière version BETA*

DbGate propose un mécanisme de déploiement automatique de base de données. Alors que la méthode traditionnelle pour y parvenir utilise des scripts SQL de migration, DbGate utilise par défaut une approche différente (les scripts de migration sont également pris en charge).
Vous définissez le modèle de base de données avec des fichiers YAML décrivant la structure des tables et les données de liste, et des fichiers SQL décrivant les vues, les procédures stockées et les fonctions. Ce modèle est déployé dans la base de données, en comparant la structure actuelle avec la structure du modèle, en créant les colonnes et les tables manquantes et en mettant à jour les définitions des vues et des procédures. **Aucune action destructive** (qui pourrait entraîner une perte de données) n'est effectuée, donc lorsque vous supprimez une colonne ou une table du modèle, elle reste dans la base de données. Si vous renommez une colonne dans le modèle, une nouvelle colonne avec le nouveau nom est créée et l'ancienne colonne reste dans la base de données.

Le déploiement peut être invoqué depuis la ligne de commande (à l'aide de scripts node) ou depuis l'interface graphique de DbGate. Vous pouvez également utiliser la fonction de comparaison de bases de données pour comparer visuellement les différences entre le modèle et la base de données réelle.

## Format yaml des tables

```yaml
name: Album # table name 
columns:
  - name: AlbumId # column name 
    type: int # data type. is used directly in target SQL engine  
    autoIncrement: true # column is autoincrement 
    notNull: true # column is not nullable (default: is nullable) 
  - name: Title
    type: nvarchar(150)
    notNull: true
  - name: ArtistId
    type: int
    references: Artist # name of table. Is used for creating foreign key 
  - name: isDeleted
    type: bit
    notNull: true
    default: 0 # default value 
  - name: created
    type: timestamp
    default: current_timestamp
primaryKey:
  - AlbumId # list of primary key column names 
indexes:
  - name: UQ_AlbumTitleArtistId # index name 
    unique: true # whether index is unique. default=false 
    columns: # list of index columns 
      - Title
      - ArtistId
data: # static data (only for list tables) 
  - AlbumId: -1 # values for all columns, which should be filled 
    Title: Predefined static album
```

- Les noms sont définis sans nom de schéma, un modèle décrit un schéma
- Les valeurs par défaut sont définies comme des expressions SQL, donc si vous souhaitez définir une chaîne de caractères, vous devez utiliser des 'guillemets simples'
- Vous pouvez définir des données statiques pour une table

### Utilisation des scripts de migration
Vous pouvez combiner des scripts de migration plus traditionnels avec la gestion de déploiement spécifique à DbGate, certains objets plus spécifiques pouvant être créés avec des scripts de migration.
Les types de scripts sont déterminés par l'extension de fichier, l'organisation des répertoires est au choix de l'utilisateur, DbGate n'en est pas affecté.

Les extensions de script suivantes sont prises en charge :
- `*.predeploy.sql` - les scripts sont exécutés avant chaque processus de déploiement
- `*.install.sql` - les scripts ne sont exécutés que s'ils sont différents du déploiement précédent
- `*.uninstall.sql` - ce script est associé au fichier `.install.sql`, il est exécuté avant que la nouvelle version du fichier `*.install.sql` ne soit exécutée
- `*.once.sql` - les scripts ne sont exécutés qu'une seule fois
- `*.postdeploy.sql` - les scripts sont exécutés avant chaque processus de déploiement

DbGate utilise la table `dbgate_deploy_journal` pour le suivi des scripts de déploiement déployés dans la base de données. Cette table est créée automatiquement lorsque vous déployez un projet comportant au moins un script de migration.


### Utilisation dans l'interface graphique de DbGate

- Dans les connexions, menu contextuel de la base de données, choisissez « Export DB model » (Premium uniquement). Le modèle de base de données est enregistré dans un répertoire ou dans un fichier. Si vous prévoyez d'utiliser la fonctionnalité de déploiement, choisissez les destinations Data archive ou Folder (YAML + SQL).
- Ouvrez le widget des archives, vous devriez voir le modèle téléchargé
- Dans le menu contextuel du modèle, vous pouvez effectuer certaines opérations sur le modèle :
    - Generate deploy DB SQL - compare la base de données actuelle (vous pouvez la voir dans la barre d'état) et génère un script SQL, qui déploie les modifications du modèle dans la base de données actuelle
    - Shell: Deploy DB - génère un shell JavaScript, qui peut être utilisé pour déployer la base de données
    - Compare with {current database} - compare graphiquement la base de données actuelle avec le modèle (Premium uniquement)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### Utilisation depuis la ligne de commande
Copiez le script suivant dans un fichier deploy.js et mettez à jour la configuration de la base de données. Vous devez également modifier modelFolder, en fonction de l'emplacement de votre dossier de modèle.
L'exécution de ce script nécessite l'installation de [NodeJs](https://nodejs.org/) sur votre ordinateur.

```js
const path = require('path');
const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginPostgres = require('dbgate-plugin-postgres');
dbgateApi.registerPlugins(dbgatePluginPostgres);

async function run() {
	await dbgateApi.deployDb({
		connection: {
			server: process.env.DB_SERVER || 'localhost',
			engine: 'postgres@dbgate-plugin-postgres',
			password: process.env.DB_PASSWORD || 'test',
			user: process.env.DB_USER || 'postgres',
			port: process.env.DB_PORT || 5432,
			database: process.env.DB_NAME || 'my_database',
		},
		modelFolder: path.join(__dirname, 'database'),
	});
	await dbgateApi.finalizer.run();
	console.log('Finished job script');
}
dbgateApi.runScript(run);
```

Ensuite, installez les modules requis en exécutant les commandes dans le répertoire contenant deploy.js :
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

Lancez le déploiement de la base de données en exécutant la commande :
```sh
node deploy.js
```

Ce script est destiné à PostgreSQL, les autres moteurs de base de données nécessitent des modifications de pilote.

Ce script peut également être généré automatiquement depuis l'interface graphique de DbGate : utilisez le menu contextuel « Shell: Deploy DB » du dossier d'archive, puis « Copy nodejs script » sur le script généré copiera un script valide. Tous les paquets utilisés dans la commande require doivent être installés avec npm install.
