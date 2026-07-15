---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: fr
layout: docs
title: Documentation de l'API
weight: 20
---

## Functions

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Copie un lecteur vers un écrivain. Utilisé pour importer et exporter des tables et pour transférer des données entre tables</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>Déploie dans la base de données le modèle de base de données stocké dans modelFolder (tables sous forme de YAML)</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Supprime tous les objets de la base de données</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>Exécute une requête SQL</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>Génère la requête de déploiement du modèle dans la base de données</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Fonction de lecture, qui lit un fichier ou une URL JSONL. Format JSONL - fichier texte, chaque ligne est une ligne encodée en JSON.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Renvoie un objet écrivain pour la fonction <a href="#copyStream">copyStream</a>. Cet objet écrivain écrit les données dans un fichier JSONL. Format JSONL - fichier texte, chaque ligne est une ligne encodée en JSON, utilisé par exemple par MongoDB.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Crée un objet lecteur pour un fichier JSON destiné à la fonction <a href="#copyStream">copyStream</a>.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Renvoie un objet écrivain pour la fonction <a href="#copyStream">copyStream</a>. Cet objet écrivain écrit les données dans un fichier JSON.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Renvoie un objet lecteur pour la fonction <a href="#copyStream">copyStream</a>. Cet objet lecteur lit les données à partir d'une requête.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Crée un objet lecteur pour la fonction <a href="#copyStream">copyStream</a>. Cet objet lecteur lit les données à partir d'une table ou d'une vue.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Crée un objet écrivain pour la fonction <a href="#copyStream">copyStream</a>. Cet objet écrivain écrit les données dans une table. La table peut être créée si elle n'existe pas.</p>
</dd>
</dl>

## Typedefs

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>Objet lecteur (entrée) pour la fonction <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>Objet écrivain (sortie) pour la fonction <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>Type de rôle utilisateur.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
Copie un lecteur vers un écrivain. Utilisé pour importer et exporter des tables et pour transférer des données entre tables

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | objet lecteur |
| output | [<code>writerType</code>](#writerType) | objet écrivain |
| options | <code>object</code> | options |

<a name="deployDb"></a>

## deployDb(options)
Déploie dans la base de données le modèle de base de données stocké dans modelFolder (tables sous forme de YAML)

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objet de connexion |
| options.systemConnection | <code>object</code> | connexion système (résultat de driver.connect). Si elle n'est pas fournie, une nouvelle connexion sera créée |
| options.driver | <code>object</code> | objet pilote. S'il n'est pas fourni, il sera chargé à partir de la connexion |
| options.analysedStructure | <code>object</code> | structure analysée de la base de données. Si elle n'est pas fournie, elle sera chargée |
| options.modelFolder | <code>string</code> | dossier contenant les fichiers du modèle (fichiers YAML pour les tables, fichiers SQL pour les vues, procédures, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modèle de base de données chargé - ensemble de fichiers YAML et SQL chargés dans un tableau |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | tableau de fonctions pour transformer le modèle |
| options.dbdiffOptionsExtra | <code>object</code> | options supplémentaires pour dbdiff |
| options.ignoreNameRegex | <code>string</code> | expression régulière pour ignorer les objets par nom |
| options.targetSchema | <code>string</code> | schéma cible pour le déploiement |
| options.maxMissingTablesRatio | <code>number</code> | proportion maximale de tables manquantes dans la base de données. Contrôle de sécurité : si la proportion manquante est supérieure, le déploiement est arrêté (ce qui évite la suppression accidentelle de toutes les tables) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
Supprime tous les objets de la base de données

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objet de connexion |
| options.systemConnection | <code>object</code> | connexion système (résultat de driver.connect). Si elle n'est pas fournie, une nouvelle connexion sera créée |
| options.driver | <code>object</code> | objet pilote. S'il n'est pas fourni, il sera chargé à partir de la connexion |
| options.analysedStructure | <code>object</code> | structure analysée de la base de données. Si elle n'est pas fournie, elle sera chargée |

<a name="executeQuery"></a>

## executeQuery(options)
Exécute une requête SQL

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | objet de connexion |
| [options.systemConnection] | <code>object</code> | connexion système (résultat de driver.connect). Si elle n'est pas fournie, une nouvelle connexion sera créée |
| [options.driver] | <code>object</code> | objet pilote. S'il n'est pas fourni, il sera chargé à partir de la connexion |
| [options.sql] | <code>string</code> | requête SQL |
| [options.sqlFile] | <code>string</code> | fichier SQL |
| [options.logScriptItems] | <code>boolean</code> | indique s'il faut journaliser les éléments du script au lieu du script entier |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
Génère la requête de déploiement du modèle dans la base de données

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objet de connexion |
| options.systemConnection | <code>object</code> | connexion système (résultat de driver.connect). Si elle n'est pas fournie, une nouvelle connexion sera créée |
| options.driver | <code>object</code> | objet pilote. S'il n'est pas fourni, il sera chargé à partir de la connexion |
| options.analysedStructure | <code>object</code> | structure analysée de la base de données. Si elle n'est pas fournie, elle sera chargée |
| options.modelFolder | <code>string</code> | dossier contenant les fichiers du modèle (fichiers YAML pour les tables, fichiers SQL pour les vues, procédures, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modèle de base de données chargé - ensemble de fichiers YAML et SQL chargés dans un tableau |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | tableau de fonctions pour transformer le modèle |
| options.dbdiffOptionsExtra | <code>object</code> | options supplémentaires pour dbdiff |
| options.ignoreNameRegex | <code>string</code> | expression régulière pour ignorer les objets par nom |
| options.targetSchema | <code>string</code> | schéma cible pour le déploiement |
| options.maxMissingTablesRatio | <code>number</code> | proportion maximale de tables manquantes dans la base de données. Contrôle de sécurité : si la proportion manquante est supérieure, le déploiement est arrêté (ce qui évite la suppression accidentelle de toutes les tables) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Fonction de lecture, qui lit un fichier ou une URL JSONL. Format JSONL - fichier texte, chaque ligne est une ligne encodée en JSON.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objet lecteur  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | nom du fichier ou URL |
| options.encoding | <code>string</code> | encodage du fichier |
| options.limitRows | <code>number</code> | nombre maximal de lignes à lire |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Renvoie un objet écrivain pour la fonction [copyStream](#copyStream). Cet objet écrivain écrit les données dans un fichier JSONL. Format JSONL - fichier texte, chaque ligne est une ligne encodée en JSON, utilisé par exemple par MongoDB.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objet écrivain  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nom du fichier |
| [options.encoding] | <code>string</code> | encodage du fichier |
| [options.header] | <code>boolean</code> | indique s'il faut écrire l'en-tête. L'en-tête est un JSON décrivant la structure de la table source. L'en-tête est spécifique à DbGate ; si vous souhaitez par exemple importer les données dans MongoDB, vous ne devriez pas écrire d'en-tête. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Crée un objet lecteur pour un fichier JSON destiné à la fonction [copyStream](#copyStream).

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objet lecteur  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nom du fichier ou URL |
| options.jsonStyle | <code>string</code> | 'object' ou 'array' |
| [options.keyField] | <code>string</code> | champ clé pour le style object |
| [options.rootField] | <code>string</code> | champ racine pour le style object |
| [options.encoding] | <code>string</code> | encodage du fichier |
| [options.limitRows] | <code>number</code> | nombre maximal de lignes à lire |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Renvoie un objet écrivain pour la fonction [copyStream](#copyStream). Cet objet écrivain écrit les données dans un fichier JSON.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objet écrivain  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nom du fichier |
| [options.jsonStyle] | <code>string</code> | 'object' ou 'array' |
| [options.keyField] | <code>string</code> | champ clé pour le style object |
| [options.rootField] | <code>string</code> | champ racine pour le style object |
| [options.encoding] | <code>string</code> | encodage du fichier |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Renvoie un objet lecteur pour la fonction [copyStream](#copyStream). Cet objet lecteur lit les données à partir d'une requête.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objet lecteur  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objet de connexion |
| options.query | <code>string</code> | requête SQL |
| [options.queryType] | <code>string</code> | type de requête |
| [options.sql] | <code>string</code> | requête SQL. obsolète ; utilisez query à la place |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Crée un objet lecteur pour la fonction [copyStream](#copyStream). Cet objet lecteur lit les données à partir d'une table ou d'une vue.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objet lecteur  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objet de connexion |
| options.systemConnection | <code>object</code> | connexion système (résultat de driver.connect). Si elle n'est pas fournie, une nouvelle connexion sera créée |
| options.pureName | <code>string</code> | nom de la table |
| options.schemaName | <code>string</code> | nom du schéma |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Crée un objet écrivain pour la fonction [copyStream](#copyStream). Cet objet écrivain écrit les données dans une table. La table peut être créée si elle n'existe pas.

**Kind**: global function  
**Returns**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objet écrivain  

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objet de connexion |
| options.systemConnection | <code>object</code> | connexion système (résultat de driver.connect). Si elle n'est pas fournie, une nouvelle connexion sera créée |
| options.driver | <code>object</code> | objet pilote. S'il n'est pas fourni, il sera chargé à partir de la connexion |
| options.pureName | <code>string</code> | nom de la table |
| options.schemaName | <code>string</code> | nom du schéma |
| options.dropIfExists | <code>boolean</code> | supprimer la table si elle existe |
| options.truncate | <code>boolean</code> | vider la table avant l'insertion |
| options.createIfNotExists | <code>boolean</code> | créer la table si elle n'existe pas |
| options.commitAfterInsert | <code>boolean</code> | valider la transaction après l'insertion |

<a name="readerType"></a>

## readerType : <code>Object</code>
Objet lecteur (entrée) pour la fonction [copyStream](#copyStream)

**Kind**: global typedef  
<a name="writerType"></a>

## writerType : <code>Object</code>
Objet écrivain (sortie) pour la fonction [copyStream](#copyStream)

**Kind**: global typedef  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
L'identifiant du moteur de base de données, sous la forme `engine@plugin-package`.

**Kind**: global typedef  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**Kind**: global typedef  
**Properties**

| Name | Type |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 
