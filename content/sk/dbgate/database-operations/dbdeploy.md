---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: sk
title: Nasadenie databázy
weight: 10
---

*Funkcionalita nasadenia sa v pripravovanom vydaní výrazne zmení, táto dokumentácia sa vzťahuje na najnovšiu BETA verziu*

DbGate ponúka mechanizmus na automatické nasadenie databázy. Zatiaľ čo tradičný spôsob to dosahuje pomocou migračných SQL skriptov, DbGate štandardne používa iný spôsob (migračné skripty sú tiež podporované).
Definujete DB model pomocou YAML súborov popisujúcich štruktúru tabuliek a dáta číselníkov a SQL súborov popisujúcich pohľady, uložené procedúry a funkcie. Tento model sa nasadí do databázy, pričom sa porovná aktuálna štruktúra so štruktúrou v modeli, vytvoria sa chýbajúce stĺpce a tabuľky a aktualizujú sa definície pohľadov a procedúr. **Nevykonávajú sa žiadne deštruktívne akcie** (ktoré by mohli viesť k strate dát), takže keď odstránite stĺpec alebo tabuľku z modelu, v databáze zostanú. Ak v modeli premenujete stĺpec, vytvorí sa nový stĺpec s novým názvom a starý stĺpec zostane v databáze.

Nasadenie je možné vyvolať z príkazového riadka (pomocou node skriptov) alebo z DbGate GUI. Môžete tiež použiť funkciu porovnania DB na vizuálne porovnanie rozdielov medzi modelom a skutočnou databázou.

## Formát yaml pre tabuľku

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

- Názvy sa definujú bez názvu schémy, jeden model popisuje jednu schému
- Predvolené hodnoty sú definované ako SQL výrazy, takže ak chcete definovať reťazec, musíte použiť 'jednoduché úvodzovky'
- Pre tabuľku môžete definovať statické dáta

### Použitie migračných skriptov
Tradičnejšie migračné skripty môžete kombinovať so správou nasadenia špecifickou pre DbGate, niektoré špecifickejšie objekty je možné vytvoriť migračnými skriptami.
Typy skriptov sú určené príponou súboru, usporiadanie adresárov je na voľbe používateľa, DbGate to neovplyvňuje.

Podporované sú nasledujúce prípony skriptov:
- `*.predeploy.sql` - skripty sa spúšťajú pred každým procesom nasadenia
- `*.install.sql` - skripty sa vykonajú len ak sa líšia od predchádzajúceho nasadenia
- `*.uninstall.sql` - tento skript je spárovaný so súborom `.install.sql`, vykoná sa pred vykonaním novej verzie súboru `*.install.sql`
- `*.once.sql` - skripty sa vykonajú iba raz
- `*.postdeploy.sql` - skripty sa spúšťajú pred každým procesom nasadenia

DbGate používa tabuľku `dbgate_deploy_journal` na sledovanie skriptov nasadenia nasadených do databázy. Táto tabuľka sa vytvorí automaticky, keď nasadíte akýkoľvek projekt s aspoň jedným migračným skriptom.


### Použitie v DbGate GUI

- V pripojeniach, v kontextovom menu databázy, zvoľte "Export DB model" (iba Premium). DB model sa uloží do adresára alebo do súboru. Ak plánujete používať funkcionalitu nasadenia, zvoľte cieľ Data archive alebo Folder (YAML + SQL).
- Otvorte widget archívov, mali by ste vidieť stiahnutý model
- V kontextovom menu modelu môžete s modelom vykonať niekoľko operácií:
    - Generate deploy DB SQL - porovná aktuálnu databázu (vidíte ju v stavovom riadku) a vygeneruje SQL skript, ktorý nasadí zmeny z modelu do aktuálnej databázy
    - Shell: Deploy DB - vygeneruje JavaScript shell, ktorý je možné použiť na nasadenie DB
    - Compare with {current database} - graficky porovná aktuálnu databázu s modelom (iba Premium)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### Použitie z príkazového riadka
Skopírujte nasledujúci skript do súboru deploy.js a upravte konfiguráciu databázy. Tiež by ste mali zmeniť modelFolder podľa umiestnenia vášho priečinka s modelom.
Spustenie tohto skriptu vyžaduje nainštalovaný [NodeJs](https://nodejs.org/) na vašom počítači.

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

Potom nainštalujte potrebné moduly spustením príkazov v adresári so súborom deploy.js:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

Nasadenie databázy spustíte príkazom:
```sh
node deploy.js
```

Tento skript je pre PostgreSQL, ostatné databázové enginy vyžadujú zmeny ovládača.

Tento skript je možné vygenerovať aj automaticky z DbGate GUI, použite kontextové menu "Shell: Deploy DB" z priečinka archívu, potom "Copy nodejs script" na vygenerovanom skripte skopíruje platný skript. Všetky balíky, ktoré sú použité v príkaze require, musia byť nainštalované pomocou npm install.
