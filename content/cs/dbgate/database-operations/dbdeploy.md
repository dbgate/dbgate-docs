---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: cs
title: Nasazení databáze
weight: 10
---

*Funkce nasazení bude v nadcházející verzi výrazně změněna, tato dokumentace se vztahuje k nejnovější BETA verzi*

DbGate nabízí mechanismus pro automatické nasazení databáze. Zatímco tradiční způsob, jak toho dosáhnout, používá migrační SQL skripty, DbGate ve výchozím nastavení používá jiný způsob (migrační skripty jsou rovněž podporovány).
Model DB definujete pomocí YAML souborů popisujících strukturu tabulek a číselníková data a SQL souborů popisujících pohledy, uložené procedury a funkce. Tento model je nasazen do databáze, přičemž se porovná aktuální struktura se strukturou v modelu, vytvoří se chybějící sloupce a tabulky a aktualizují se definice pohledů a procedur. Neprovádějí se **žádné destruktivní akce** (které by mohly vést ke ztrátě dat), takže když z modelu odeberete sloupec nebo tabulku, v databázi zůstane. Pokud sloupec v modelu přejmenujete, vytvoří se nový sloupec s novým názvem a starý sloupec v databázi zůstane.

Nasazení lze vyvolat z příkazové řádky (pomocí node skriptů) nebo z GUI DbGate. Můžete také použít funkci porovnání DB pro vizuální porovnání rozdílů mezi modelem a skutečnou databází.

## Formát yaml pro tabulku

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

- Názvy jsou definovány bez názvu schématu, jeden model popisuje jedno schéma
- Výchozí hodnoty jsou definovány jako SQL výrazy, takže pokud chcete definovat řetězec, musíte použít 'jednoduché uvozovky'
- Pro tabulku můžete definovat statická data

### Použití migračních skriptů
Tradičnější migrační skripty můžete zkombinovat se správou nasazení specifickou pro DbGate, některé specifičtější objekty lze vytvořit migračními skripty.
Typy skriptů jsou určeny příponou souboru, uspořádání adresářů je na uživateli, DbGate to nijak neovlivňuje.

Podporovány jsou následující přípony skriptů:
- `*.predeploy.sql` - skripty se spouštějí před každým procesem nasazení
- `*.install.sql` - skripty se spustí pouze tehdy, pokud se liší od předchozího nasazení
- `*.uninstall.sql` - tento skript je spárován se souborem `.install.sql`, spustí se před spuštěním nové verze souboru `*.install.sql`
- `*.once.sql` - skripty se spustí pouze jednou
- `*.postdeploy.sql` - skripty se spouštějí před každým procesem nasazení

DbGate používá tabulku `dbgate_deploy_journal` pro sledování skriptů nasazených do databáze. Tato tabulka se vytvoří automaticky, když nasadíte jakýkoli projekt s alespoň jedním migračním skriptem.


### Použití v GUI DbGate

- V připojeních, v kontextovém menu databáze, zvolte "Export DB model" (pouze Premium). Model DB se uloží do adresáře nebo do souboru. Pokud plánujete používat funkci nasazení, zvolte cíl Data archive nebo Folder (YAML + SQL).
- Otevřete widget archivů, měli byste vidět stažený model
- V kontextovém menu modelu můžete s modelem provádět některé operace:
    - Generate deploy DB SQL - porovná aktuální databázi (vidíte ji ve stavovém řádku) a vygeneruje SQL skript, který nasadí změny z modelu do aktuální databáze
    - Shell: Deploy DB - vygeneruje JavaScript shell, který lze použít pro nasazení DB
    - Compare with {current database} - graficky porovná aktuální databázi s modelem (pouze Premium)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### Použití z příkazové řádky
Zkopírujte následující skript do souboru deploy.js a upravte konfiguraci databáze. Také byste měli změnit modelFolder podle umístění vaší složky s modelem.
Spuštění tohoto skriptu vyžaduje nainstalovaný [NodeJs](https://nodejs.org/) na vašem počítači.

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

Poté nainstalujte potřebné moduly spuštěním příkazů v adresáři se souborem deploy.js:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

Nasazení databáze spusťte příkazem:
```sh
node deploy.js
```

Tento skript je pro PostgreSQL, ostatní databázové enginy vyžadují změnu driveru.

Tento skript lze vygenerovat také automaticky z GUI DbGate, použijte kontextové menu "Shell: Deploy DB" ze složky archivu, poté "Copy nodejs script" na vygenerovaném skriptu zkopíruje platný skript. Všechny balíčky, které jsou použity v příkazu require, musí být nainstalovány pomocí npm install.
