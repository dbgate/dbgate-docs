---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: it
title: Deploy del database
weight: 10
---

*La funzionalità di deploy verrà modificata in modo significativo nella prossima release, questa documentazione si riferisce all'ultima versione BETA*

DbGate offre un meccanismo per il deploy automatico del database. Mentre il modo tradizionale per ottenere questo risultato utilizza script SQL di migrazione, DbGate usa per impostazione predefinita un approccio diverso (anche gli script di migrazione sono supportati).
Si definisce il modello del DB con file YAML che descrivono la struttura delle tabelle e i dati di lista, e con file SQL che descrivono viste, stored procedure e funzioni. Questo modello viene distribuito nel database, confrontando la struttura attuale con la struttura presente nel modello, creando le colonne e le tabelle mancanti e aggiornando le definizioni di viste e procedure. **Non viene eseguita alcuna azione distruttiva** (che potrebbe portare a perdita di dati), quindi quando si rimuove una colonna o una tabella dal modello, essa rimane nel database. Se si rinomina una colonna nel modello, viene creata una nuova colonna con il nuovo nome e la vecchia colonna rimane nel database.

Il deploy può essere invocato dalla riga di comando (usando gli script node) oppure dalla GUI di DbGate. È anche possibile usare la funzione di confronto del DB per confrontare visivamente le differenze tra il modello e il database reale.

## Formato yaml della tabella

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

- I nomi sono definiti senza il nome dello schema, un modello descrive uno schema
- I valori predefiniti sono definiti come espressioni SQL, quindi se si vuole definire una stringa, si devono usare gli 'apici singoli'
- È possibile definire dati statici per la tabella

### Uso degli script di migrazione
È possibile combinare gli script di migrazione più tradizionali con la gestione del deploy specifica di DbGate, alcuni oggetti più specifici possono essere creati con script di migrazione.
I tipi di script sono determinati dall'estensione del file, la struttura delle directory è a scelta dell'utente, DbGate non ne è influenzato.

Sono supportate le seguenti estensioni di script:
- `*.predeploy.sql` - gli script vengono eseguiti prima di ogni processo di deploy
- `*.install.sql` - gli script vengono eseguiti solo se sono diversi rispetto al deploy precedente
- `*.uninstall.sql` - questo script è associato al file `.install.sql`, viene eseguito prima che venga eseguita la nuova versione del file `*.install.sql`
- `*.once.sql` - gli script vengono eseguiti una sola volta
- `*.postdeploy.sql` - gli script vengono eseguiti prima di ogni processo di deploy

DbGate utilizza la tabella `dbgate_deploy_journal` per tenere traccia degli script di deploy distribuiti nel database. Questa tabella viene creata automaticamente quando si distribuisce un progetto con almeno uno script di migrazione.


### Utilizzo nella GUI di DbGate

- Nelle connessioni, nel menu contestuale del database, scegliere "Export DB model" (solo Premium). Il modello del DB viene salvato in una directory o in un file. Se si intende usare la funzionalità di Deploy, scegliere come destinazione Data archive oppure Folder (YAML + SQL).
- Aprire il widget degli archivi, si dovrebbe vedere il modello scaricato
- Nel menu contestuale del modello è possibile eseguire alcune operazioni sul modello:
    - Generate deploy DB SQL - confronta il database corrente (visibile nella barra di stato) e genera uno script SQL che distribuisce le modifiche dal modello al database corrente
    - Shell: Deploy DB - genera una shell JavaScript che può essere usata per distribuire il DB
    - Compare with {current database} - confronta graficamente il database corrente con il modello (solo Premium)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### Utilizzo dalla riga di comando
Copiare il seguente script nel file deploy.js e aggiornare la configurazione del database. È inoltre necessario modificare modelFolder in base alla posizione della cartella del modello.
L'esecuzione di questo script richiede [NodeJs](https://nodejs.org/) installato sul computer.

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

Quindi installare i moduli richiesti, eseguendo i comandi nella directory che contiene deploy.js:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

Eseguire il deploy del database lanciando il comando:
```sh
node deploy.js
```

Questo script è per PostgreSQL, altri motori di database richiedono modifiche al driver.

Questo script può essere generato anche automaticamente dalla GUI di DbGate, usare il menu contestuale "Shell: Deploy DB" dalla cartella dell'archivio, quindi "Copy nodejs script" sullo script generato copierà uno script valido. Tutti i pacchetti usati nel comando require devono essere installati con npm install.
