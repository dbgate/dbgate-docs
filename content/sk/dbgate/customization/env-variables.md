---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: sk
title: Premenné prostredia
weight: 20
---

Konfiguráciu pomocou premenných prostredia je možné použiť v docker kontajneroch, tiež pri použití npm balíčka. NPM balíček podporuje súbory .env.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - NPM balíček pre edíciu Community
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - NPM balíček pre edíciu Premium
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - Docker image pre edíciu Community
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - Docker image pre edíciu Premium

## Edícia Premium vs Team Community
Edícia Community (FOSS) používa iba konfiguráciu z nižšie uvedených premenných prostredia. Edícia Team Premium používa pre nastavenia databázové úložisko s [administračným rozhraním](/sk/features/administration), pomocou premenných prostredia sa konfiguruje len niekoľko základných nastavení.

## Konfigurácia edície Team Premium
Tieto premenné sú dostupné iba v edícii Team Premium.
  * STORAGE_SERVER - databázový server (názov hostiteľa) pre úložnú databázu
  * STORAGE_USER - databázový používateľ
  * STORAGE_PASSWORD - heslo do databázy
  * STORAGE_PORT - port databázy (voliteľné. Ak je vynechaný, použije sa predvolený port pre zvolený databázový engine)
  * STORAGE_DATABASE - názov úložnej databázy
  * STORAGE_SCHEMA - schéma úložnej databázy (voliteľné, napr. pre PostgreSQL (typicky public) alebo MS SQL (typicky dbo))
  * STORAGE_ENGINE - engine použitý pre úložnú databázu. Aktuálne MySQL, PostgreSQL, SQL Server a Oracle. Použite jednu z nasledujúcich hodnôt:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - heslo pre administrátora. Administrácia je dostupná na URL https://dbgate_url/admin.html. Ak nie je heslo definované a je definovaná premenná STORAGE_DATABASE, DbGate sa pri prvom spustení opýta na heslo administrátora.
  * DBGATE_LICENSE - licenčný kľúč pre DbGate. Pre skúšobnú licenciu kontaktujte prosím sales@dbgate.eu. Ak nie je definovaný, DbGate Premium si pri prvom spustení vyžiada licenciu. DbGate Community nevyžaduje žiadnu licenciu.
  
### Ďalšie parametre pripojenia úložiska
  * STORAGE_SOCKET_PATH - cesta k socketu pre pripojenie k úložisku
  * STORAGE_DATABASE_URL - URL databázy pre pripojenie k úložisku
  * STORAGE_AUTH_TYPE - typ autentifikácie pre pripojenie k úložisku. Hodnoty sú rovnaké ako pre premennú AUTH_TYPE_xxx
  * STORAGE_USE_SSL - nastavte hodnotu 1 alebo true, ak sa má použiť SSL
  * STORAGE_KEY_FILE - cesta k súboru s kľúčom
  * STORAGE_KEY_FILE_PASSWORD - heslo k súboru s kľúčom
  * STORAGE_SSL_CA_FILE - cesta k súboru s CA certifikátom
  * STORAGE_SSL_CERT_FILE - cesta k súboru s certifikátom
  * STORAGE_SSL_CERT_FILE_PASSWORD - heslo k súboru s kľúčom certifikátu
  * STORAGE_SSL_KEY_FILE - cesta k súboru s kľúčom
  * STORAGE_SSL_KEY_FILE_PASSWORD - heslo k súboru s kľúčom
  * STORAGE_SSL_REJECT_UNAUTHORIZED - nastavte hodnotu 1 alebo true, ak sa majú odmietať neautorizované pripojenia
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - nastavte hodnotu 1 alebo true pre nastavenie MSSQL voľby trustServerCertificate

Nasledujúce premenné sú dostupné v edícii Community aj Premium. V edícii Premium je však preferovaným spôsobom použitie úložnej databázy a konfigurácia cez administračné rozhranie.

## Konfigurácia webu a oprávnení
* WEB_ROOT - ak potrebujete spustiť DbGate vo virtuálnom podadresári (napr. pre hodnotu /dbadmin bude dbgate dostupný na localhost:3000/dbadmin )
* LOGIN , PASSWORD - prihlasovacie údaje pre prístup do webovej aplikácie
* PERMISSIONS - zoznam oprávnení oddelených čiarkou. Pozrite si tiež zoznam oprávnení nižšie
* SHELL_CONNECTION - ak je true alebo 1, pripojenia môžu byť definované v shell skriptoch. Inak sú povolené iba predkonfigurované pripojenia. Predvolene to nie je povolené z bezpečnostných dôvodov. Majte na pamäti, že ak je to povolené, zašifrované heslá sa posielajú na frontend.
* SHELL_SCRIPTING - ak je true alebo 1, sú povolené vlastné JavaScriptové shell skripty. Predvolene to nie je povolené z bezpečnostných dôvodov.
* LOGIN_PASSWORD_[login] - heslo pre zadané prihlasovacie meno
* LOGIN_PERMISSIONS_[login] - zoznam oprávnení oddelených čiarkou pre dané prihlasovacie meno. Pozrite si tiež zoznam oprávnení nižšie
* TOKEN_LIFETIME - životnosť prístupového tokenu. Po uplynutí tejto doby bude prihlásený používateľ presmerovaný na prihlasovaciu stránku. Predvolená hodnota je 1d (znamená 1 deň). Možné sú hodnoty ako 3h (3 hodiny), 10m (10 minút), 2d (2 dni)
* SINGLE_CONNECTION - ID pripojenia. Ak je definované, dostupné bude iba toto pripojenie (musí sa použiť spolu so SINGLE_DATABASE)
* SINGLE_DATABASE - názov databázy, dostupná bude iba táto databáza. (musí sa použiť spolu so SINGLE_CONNECTION)
* BASIC_AUTH - ak je true alebo 1 , použije sa basic autentifikácia webu aj API. Inak sa použije prihlasovací formulár a autentifikácia API založená na JWT tokene. Basic autentifikáciu nie je možné použiť pre OAuth autentifikáciu.
* SKIP_ALL_AUTH - ak je true alebo 1, preskočí sa všetka autentifikácia
* ALLOW_DBGATE_PRIVATE_CLOUD - predvolene je DbGate cloud pre webovú verziu vypnutý. Pomocou tejto premennej ho môžete zapnúť
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - vo webovej verzii presmerovať na prihlásenie do DbGate cloudu namiesto otvorenia nového okna
* LANGUAGE - jazyk používateľského rozhrania, napr. en, cs, de, fr, atď. Pozrite si tabuľku konfigurácie jazyka nižšie. Nastavte "auto" pre použitie jazyka prehliadača

## Konfigurácia jazyka
| Jazyk | Hodnota |
|----------|-------|
| angličtina | en |
| nemčina | de |
| španielčina | es |
| francúzština | fr |
| taliančina | it |
| portugalčina (Brazília) | pt |
| japončina | ja |
| čínština - zjednodušená | zh |
| čeština | cs |
| slovenčina | sk |


## Konfigurácia logovania
* LOG_LEVEL - všetky správy s touto úrovňou logovania alebo vyššou budú zalogované. Jedna z hodnôt trace, debug, info, warn, error, fatal. Predvolená je info
* FILE_LOG_LEVEL - úroveň logovania pre zápis do log súboru. Pre logovanie do súboru má vyššiu prioritu ako LOG_LEVEL
* CONSOLE_LOG_LEVEL - úroveň logovania pre zápis do log súboru. Pre logovanie do konzoly má vyššiu prioritu ako LOG_LEVEL

## Konfigurácia OAuth (iba webová verzia)
* OAUTH_AUTH - autentifikačný endpoint protokolu OAuth
* OAUTH_TOKEN - token endpoint protokolu OAuth
* OAUTH_LOGOUT - URL odhlásenia OAuth poskytovateľa. Používateľ bude presmerovaný na túto URL, keď požiada o odhlásenie
* OAUTH_CLIENT_ID - ID klienta
* OAUTH_CLIENT_SECRET - tajný kľúč klienta
* OAUTH_LOGIN_FIELD - názov poľa z payloadu, ktoré obsahuje prihlasovacie meno. Dostupné polia si môžete pozrieť v logu dbgate, payload zaslaný od OAuth poskytovateľa sa loguje do konzoly. Toto prihlasovacie meno sa používa napr. pri konfigurácii oprávnení. Nemusí to byť nutne prihlasovacie meno zadané v OAuth. Ak nie je zadané, všetci používatelia od OAuth poskytovateľa budú mať rovnaké prihlasovacie meno.
* OAUTH_ALLOWED_LOGINS - čiarkou oddelené prihlasovacie mená, ktoré sa budú môcť prihlásiť. Ak nie je zadané, všetky prihlasovacie mená budú môcť používať aplikáciu DbGate.
* OAUTH_SCOPE - scope, ktorý sa posiela na OAuth authorize a token endpoint
* OAUTH_GROUP_FIELD - pole v payloade z OAuth, ktoré označuje skupinu
* OAUTH_ALLOWED_GROUPS - čiarkou oddelené názvy povolených skupín

## Konfigurácia Active directory/LDAP (iba webová verzia)
* AD_URL - URL LDAP poskytovateľa (napr. ldap://domain.com)
* AD_BASEDN - napr. dc=domain,dc=com
* AD_USERNAME - používateľské meno do active directory
* AD_PASSWORD - heslo do active directory
* AD_ALLOWED_LOGINS - čiarkou oddelené prihlasovacie mená, ktoré sa budú môcť prihlásiť. Ak nie je zadané, všetky prihlasovacie mená budú môcť používať aplikáciu DbGate.

## Konfigurácia Oracle klienta  
* ORACLE_INSTANT_CLIENT - cesta k [Oracle instant clientu](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html)

## Konfigurácia pripojení
Zoznam pripojení môžete nakonfigurovať pomocou premenných prostredia, potom nebudú dostupné príkazy "Add connection" a "Edit connection".

* CONNECTIONS - zoznam predkonfigurovaných názvov pripojení, oddelených čiarkou. V nasledujúcich voľbách je [connection id] ID z tohto zoznamu
* LABEL_[connection id] - označenie (zobrazovaný názov) pripojenia. 
* SERVER_[connection id] - server (názov hostiteľa) pripojenia.
* USER_[connection id] - používateľské meno pre DB pripojenie.
* PASSWORD_[connection id] - heslo pre DB pripojenie.
* PASSWORD_MODE_[connection id] - určuje, či sa heslo a používateľské meno ukladajú, alebo ich musí vyplniť používateľ. Jedna z nasledujúcich hodnôt:
  * askPassword - DbGate sa pri pripájaní opýta na heslo
  * askUser - DbGate sa opýta na používateľské meno a heslo
* PORT_[connection id] - port pre DB pripojenie.
* FILE_[connection id] - cesta k databázovému súboru (pre SQLite).
* URL_[connection id] - URL databázy (funguje pre MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle).
* SERVICE_NAME_[connection id] - Oracle service name.
* DATABASE_[connection id] - predvolený názov databázy.
* READONLY_[connection id] - pripojiť sa v režime iba na čítanie
* ENGINE_[connection id] - engine pripojenia (**povinné**, názov enginu s pluginom), jedna z hodnôt:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - nastavte hodnotu 1 alebo true, ak sa má použiť SSH tunel
* SSH_HOST_[connection id] - názov SSH hostiteľa
* SSH_PORT_[connection id] - číslo SSH portu
* SSH_MODE_[connection id] - jedna z nasledujúcich hodnôt
  * userPassword - autentifikácia používateľským menom a heslom
  * agent - autentifikácia pomocou SSH agenta
  * keyFile - autentifikácia pomocou súboru s kľúčom
* SSH_LOGIN_[connection id] - SSH prihlasovacie meno
* SSH_PASSWORD_[connection id] - SSH heslo
* SSH_KEY_FILE_[connection id] - úplná cesta k súboru s kľúčom
* SSH_KEY_FILE_PASSWORD_[connection id] - heslo k súboru s kľúčom
* USE_SSL_[connection id] - nastavte hodnotu 1 alebo true, ak sa má použiť SSL
* SSL_CA_FILE_[connection id] - cesta k súboru s CA certifikátom
* SSL_CERT_FILE_[connection id] - cesta k súboru s certifikátom
* SSL_CERT_FILE_PASSWORD_[connection id] - heslo k súboru s kľúčom certifikátu
* SSL_KEY_FILE_[connection id] - cesta k súboru s kľúčom
* SSL_REJECT_UNAUTHORIZED_[connection id] - nastavte hodnotu 1 alebo true, ak sa majú odmietať neautorizované pripojenia
* SSL_TRUST_CERTIFICATE_[connection id] - nastavte hodnotu 1 alebo true pre nastavenie MSSQL voľby trustServerCertificate
* SETTINGS_[settings key] - predkonfigurovaná hodnota nastavenia. Kľúč nastavenia je možné vyčítať zo zdrojových kódov, https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - cesta k socket súboru, ak sa pripájate cez socket
* AUTH_TYPE_[connection id] - typ autentifikácie
  * hostPort (predvolené)
  * socket - hodnota je nastavená implicitne pri nastavení SOCKET_PATH
  * tedious - predvolená prenositeľná autentifikácia pre MS SQL, používajúca ovládač tedious
  * sspi - integrovaná autentifikácia Windows (iba Windows, MS SQL), používajúca natívny MSSQL ovládač
  * sql - SQL autentifikácia (iba Windows, MS SQL), používajúca natívny MSSQL ovládač
* ALLOWED_DATABASES_[connection id] - povolené názvy databáz pre zadané pripojenie, oddelené zvislou čiarou ("|")
* ALLOWED_DATABASES_REGEX_[connection id] - regulárny výraz pre povolené názvy databáz pre zadané pripojenie
* USE_SEPARATE_SCHEMAS_[connection id] - nastavte hodnotu 1 alebo true pre samostatné načítanie schém. Použite to, ak máte veľké schémy.
* LOCAL_DATA_CENTER_[connection id] - lokálne dátové centrum (pre Apache Cassandra)
* CONNECTION_[connection id]_parameterName - nastavenie názvu parametra špecifického pre engine

SettingsModal.svelte , nájdite reťazec "name="/ Ak potrebujete definovať "true", použite hodnotu "1". Ak potrebujete "false", použite prázdny reťazec ("0" nebude fungovať)

## Konfigurácia rolí
Túto konfiguráciu je možné použiť iba v edícii Team Premium, keď sa pre nastavenia používa úložná databáza. Roly z premenných prostredia sa pri štarte docker kontajnera importujú do úložnej databázy.
Môžete definovať roly so špecifickými oprávneniami a priradiť k roli pripojenia. Priraďovanie rolí používateľom sa vykonáva v administračnom rozhraní.
* `ROLE_[role_name]_PERMISSIONS` - čiarkou oddelený zoznam oprávnení pre danú rolu. Pozrite si zoznam oprávnení nižšie
* `ROLE_[role_name]_CONNECTIONS` - čiarkou oddelený zoznam ID pripojení priradených danej roli
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - ID pripojenia pre databázové oprávnenie s daným ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - zvislou čiarou ("|") oddelený zoznam názvov databáz pre databázové oprávnenie s daným ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - regulárny výraz pre názvy databáz pre databázové oprávnenie s daným ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - jedna z hodnôt: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - ID pripojenia pre tabuľkové oprávnenie s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - zvislou čiarou ("|") oddelený zoznam názvov databáz pre databázové oprávnenie s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - regulárny výraz pre názvy databáz pre databázové oprávnenie s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - zvislou čiarou ("|") oddelený zoznam názvov schém pre tabuľkové oprávnenie s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - regulárny výraz pre názvy schém pre tabuľkové oprávnenie s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - zvislou čiarou ("|") oddelený zoznam názvov tabuliek pre databázové oprávnenie s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - regulárny výraz pre názvy tabuliek pre tabuľkové oprávnenie s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - jedna z hodnôt: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - jedna z hodnôt: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## Oprávnenia
Predvolene sú dostupné všetky oprávnenia. Ak použijete predponu \~, oprávnenie je odobraté.

### Príklady
* ~*, widgets/database - všetky oprávnenia sú odobraté, viditeľný je iba databázový widget
* ~widgets/*, widgets/database - všetky oprávnenia na widgety sú odobraté, viditeľný je iba databázový widget
* ~connections/*, connections/con1 - všetky pripojenia okrem con1 sú skryté a zakázané

### Zoznam oprávnení
* settings/change - umožňuje meniť nastavenia
* plugins/install - umožňuje inštalovať pluginy
* widgets/[widget_name] - ak nie je udelené, widget je skrytý. Widget je pruh na ľavej strane. Dostupné widgety:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - čítanie súborov z daného priečinka
* files/[folder]/write - zápis súborov do daného priečinka
* apps/write - ukladanie do obsahu aplikácií
* archive/write - ukladanie do obsahu archívu
* connections/[connection_id] - povolenie vidieť a používať definované pripojenie
* internal-storage = prístup k internému úložisku (Premium)
* admin/auth - Administrácia - záložka Authentication (Premium)
* admin/connections - Administrácia - záložka Connections (Premium)
* admin/users - Administrácia - záložka Users (Premium)
* admin/roles - Administrácia - záložka Roles (Premium)
* dbops/sql-template/* - SQL šablóny (napr. SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - SQL generátor
* dbops/sql-dump/import - Import SQL dumpu
* dbops/sql-dump/export - Export SQL dumpu
* dbops/query - Spustenie SQL dotazu
* dbops/import - Import dát
* dbops/export - Export dát
* dbops/charts - Zobrazenie grafov
* dbops/profiler - Databázový profiler
* dbops/createdb - Vytvorenie databázy
* dbops/dropdb - Zrušenie databázy
* dbops/model/view - Zobrazenie databázového modelu (diagramy, JSON)
* dbops/model/edit - Úprava databázového modelu (vytváranie/zmena tabuliek, pohľadov atď.)
* dbops/model/compare - Porovnanie databázových modelov
* dbops/table/rename - Premenovanie tabuľky
* dbops/table/truncate - Vyprázdnenie tabuľky
* dbops/table/backup - Vytvorenie zálohy tabuľky
