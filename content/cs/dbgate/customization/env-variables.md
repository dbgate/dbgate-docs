---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: cs
title: Proměnné prostředí
weight: 20
---

Konfiguraci pomocí proměnných prostředí lze použít v docker kontejnerech, také při použití npm balíčku. NPM balíček podporuje soubory .env.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - NPM balíček pro edici Community
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - NPM balíček pro edici Premium
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - Docker image pro edici Community
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - Docker image pro edici Premium

## Edice Premium vs Team Community
Edice Community (FOSS) používá pouze konfiguraci z níže uvedených proměnných prostředí. Edice Team Premium používá pro nastavení databázové úložiště s [administračním rozhraním](/cs/features/administration), pomocí proměnných prostředí se konfiguruje jen několik základních nastavení.

## Konfigurace edice Team Premium
Tyto proměnné jsou dostupné pouze v edici Team Premium.
  * STORAGE_SERVER - databázový server (název hostitele) pro úložnou databázi
  * STORAGE_USER - databázový uživatel
  * STORAGE_PASSWORD - heslo do databáze
  * STORAGE_PORT - port databáze (volitelné. Pokud je vynechán, použije se výchozí port pro zvolený databázový engine)
  * STORAGE_DATABASE - název úložné databáze
  * STORAGE_SCHEMA - schéma úložné databáze (volitelné, např. pro PostgreSQL (typicky public) nebo MS SQL (typicky dbo))
  * STORAGE_ENGINE - engine použitý pro úložnou databázi. Aktuálně MySQL, PostgreSQL, SQL Server a Oracle. Použijte jednu z následujících hodnot:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - heslo pro administrátora. Administrace je dostupná na URL https://dbgate_url/admin.html. Pokud není heslo definováno a je definována proměnná STORAGE_DATABASE, DbGate se při prvním spuštění zeptá na heslo administrátora.
  * DBGATE_LICENSE - licenční klíč pro DbGate. Pro zkušební licenci kontaktujte prosím sales@dbgate.eu. Pokud není definován, DbGate Premium se při prvním spuštění zeptá na licenci. DbGate Community žádnou licenci nevyžaduje.
  
### Další parametry připojení k úložišti
  * STORAGE_SOCKET_PATH - cesta k socketu pro připojení k úložišti
  * STORAGE_DATABASE_URL - databázová URL pro připojení k úložišti
  * STORAGE_AUTH_TYPE - typ autentizace pro připojení k úložišti. Hodnoty jsou stejné jako pro proměnnou AUTH_TYPE_xxx
  * STORAGE_USE_SSL - nastavte hodnotu 1 nebo true, pokud se má použít SSL
  * STORAGE_KEY_FILE - cesta k souboru s klíčem
  * STORAGE_KEY_FILE_PASSWORD - heslo k souboru s klíčem
  * STORAGE_SSL_CA_FILE - cesta k souboru s CA certifikátem
  * STORAGE_SSL_CERT_FILE - cesta k souboru s certifikátem
  * STORAGE_SSL_CERT_FILE_PASSWORD - heslo k souboru s klíčem certifikátu
  * STORAGE_SSL_KEY_FILE - cesta k souboru s klíčem
  * STORAGE_SSL_KEY_FILE_PASSWORD - heslo k souboru s klíčem
  * STORAGE_SSL_REJECT_UNAUTHORIZED - nastavte hodnotu 1 nebo true, pokud se mají odmítat neautorizovaná připojení
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - nastavte hodnotu 1 nebo true pro nastavení MSSQL volby trustServerCertificate

Následující proměnné jsou dostupné v edici Community i Premium. V edici Premium je však preferovaným způsobem použití úložné databáze a konfigurace přes administrační rozhraní.

## Konfigurace webu a oprávnění
* WEB_ROOT - pokud potřebujete provozovat DbGate ve virtuálním podadresáři (např. pro hodnotu /dbadmin bude dbgate dostupný na localhost:3000/dbadmin )
* LOGIN , PASSWORD - přihlašovací údaje pro přístup k webové aplikaci
* PERMISSIONS - seznam oprávnění oddělených čárkou. Viz také seznam oprávnění níže
* SHELL_CONNECTION - pokud je true nebo 1, lze připojení definovat v shell skriptech. Jinak jsou povolena pouze předkonfigurovaná připojení. Ve výchozím stavu to není z bezpečnostních důvodů povoleno. Mějte na paměti, že pokud je to povoleno, jsou na frontend odesílána zašifrovaná hesla.
* SHELL_SCRIPTING - pokud je true nebo 1, jsou povoleny vlastní JavaScript shell skripty. Ve výchozím stavu to není z bezpečnostních důvodů povoleno.
* LOGIN_PASSWORD_[login] - heslo pro zadané přihlašovací jméno
* LOGIN_PERMISSIONS_[login] - seznam oprávnění oddělených čárkou pro dané přihlašovací jméno. Viz také seznam oprávnění níže
* TOKEN_LIFETIME - životnost přístupového tokenu. Po uplynutí této doby bude přihlášený uživatel přesměrován na přihlašovací stránku. Výchozí hodnota je 1d (znamená 1 den). Možné jsou hodnoty jako 3h (3 hodiny), 10m (10 minut), 2d (2 dny)
* SINGLE_CONNECTION - ID připojení. Pokud je definováno, bude dostupné pouze toto připojení (musí být použito společně s SINGLE_DATABASE)
* SINGLE_DATABASE - název databáze, dostupná bude pouze tato databáze. (musí být použito společně s SINGLE_CONNECTION)
* BASIC_AUTH - pokud je true nebo 1 , použije se basic autentizace pro web i API. Jinak se použije přihlašovací formulář a autentizace API pomocí JWT tokenu. Basic autentizaci nelze použít pro OAuth autentizaci.
* SKIP_ALL_AUTH - pokud je true nebo 1, veškerá autentizace je přeskočena
* ALLOW_DBGATE_PRIVATE_CLOUD - ve výchozím stavu je DbGate cloud pro webovou verzi zakázán. Pomocí této proměnné jej můžete povolit
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - ve webové verzi přesměrovat na přihlášení do DbGate cloudu místo otevření nového okna
* LANGUAGE - jazyk uživatelského rozhraní, např. en, cs, de, fr atd. Viz tabulka konfigurace jazyků níže. Nastavte "auto" pro použití jazyka prohlížeče

## Konfigurace jazyka
| Jazyk | Hodnota |
|----------|-------|
| Angličtina | en |
| Němčina | de |
| Španělština | es |
| Francouzština | fr |
| Italština | it |
| Portugalština (Brazílie) | pt |
| Japonština | ja |
| Čínština - zjednodušená | zh |
| Čeština | cs |
| Slovenština | sk |


## Konfigurace logování
* LOG_LEVEL - všechny zprávy s touto nebo vyšší úrovní logování budou zaznamenány. Jedna z hodnot trace, debug, info, warn, error, fatal. Výchozí je info
* FILE_LOG_LEVEL - úroveň logování pro zápis do log souboru. Pro logování do souboru má vyšší prioritu než LOG_LEVEL
* CONSOLE_LOG_LEVEL - úroveň logování pro zápis do log souboru. Pro logování do konzole má vyšší prioritu než LOG_LEVEL

## Konfigurace OAuth (pouze webová verze)
* OAUTH_AUTH - autentizační endpoint OAuth protokolu
* OAUTH_TOKEN - token endpoint OAuth protokolu
* OAUTH_LOGOUT - odhlašovací URL OAuth poskytovatele. Uživatel bude přesměrován na tuto URL, když požádá o odhlášení
* OAUTH_CLIENT_ID - ID klienta
* OAUTH_CLIENT_SECRET - tajný klíč klienta
* OAUTH_LOGIN_FIELD - název pole z payloadu, které obsahuje přihlašovací jméno. Dostupná pole můžete zjistit v logu dbgate, payload odeslaný od OAuth poskytovatele je logován do konzole. Toto přihlašovací jméno se používá např. pro konfiguraci oprávnění. Nemusí to nutně být přihlašovací jméno zadané v OAuth. Pokud není zadáno, budou mít všichni uživatelé od OAuth poskytovatele stejné přihlašovací jméno.
* OAUTH_ALLOWED_LOGINS - čárkou oddělená přihlašovací jména, kterým bude povoleno přihlášení. Pokud není zadáno, budou aplikaci DbGate moci používat všechna přihlašovací jména.
* OAUTH_SCOPE - scope, který je odesílán na OAuth authorize a token endpoint
* OAUTH_GROUP_FIELD - pole v payloadu z OAuth, které označuje skupinu
* OAUTH_ALLOWED_GROUPS - čárkou oddělené názvy povolených skupin

## Konfigurace Active directory/LDAP (pouze webová verze)
* AD_URL - URL LDAP poskytovatele (např. ldap://domain.com)
* AD_BASEDN - např. dc=domain,dc=com
* AD_USERNAME - uživatelské jméno do active directory
* AD_PASSWORD - heslo do active directory
* AD_ALLOWED_LOGINS - čárkou oddělená přihlašovací jména, kterým bude povoleno přihlášení. Pokud není zadáno, budou aplikaci DbGate moci používat všechna přihlašovací jména.

## Konfigurace Oracle klienta  
* ORACLE_INSTANT_CLIENT - cesta k [Oracle instant client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html)

## Konfigurace připojení
Seznam připojení můžete nakonfigurovat pomocí proměnných prostředí, poté nebudou dostupné příkazy "Add connection" a "Edit connection".

* CONNECTIONS - seznam názvů předkonfigurovaných připojení, oddělený čárkou. V následujících volbách je [connection id] ID z tohoto seznamu
* LABEL_[connection id] - popisek (zobrazovaný název) připojení. 
* SERVER_[connection id] - server (název hostitele) připojení.
* USER_[connection id] - uživatelské jméno pro DB připojení.
* PASSWORD_[connection id] - heslo pro DB připojení.
* PASSWORD_MODE_[connection id] - určuje, zda je heslo a uživatelské jméno uloženo, nebo je musí vyplnit uživatel. Jedna z následujících hodnot:
  * askPassword - DbGate se při připojování zeptá na heslo
  * askUser - DbGate se zeptá na uživatelské jméno a heslo
* PORT_[connection id] - port pro DB připojení.
* FILE_[connection id] - cesta k databázovému souboru (pro SQLite).
* URL_[connection id] - databázová URL (funguje pro MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle).
* SERVICE_NAME_[connection id] - Oracle service name.
* DATABASE_[connection id] - výchozí název databáze.
* READONLY_[connection id] - připojit v režimu pouze pro čtení
* ENGINE_[connection id] - engine připojení (**povinné**, název enginu s pluginem), jeden z:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - nastavte hodnotu 1 nebo true, pokud se má použít SSH tunel
* SSH_HOST_[connection id] - název SSH hostitele
* SSH_PORT_[connection id] - číslo SSH portu
* SSH_MODE_[connection id] - jedna z následujících hodnot
  * userPassword - autentizace uživatelským jménem a heslem
  * agent - autentizace pomocí SSH agenta
  * keyFile - autentizace pomocí souboru s klíčem
* SSH_LOGIN_[connection id] - SSH přihlašovací jméno
* SSH_PASSWORD_[connection id] - SSH heslo
* SSH_KEY_FILE_[connection id] - úplná cesta k souboru s klíčem
* SSH_KEY_FILE_PASSWORD_[connection id] - heslo k souboru s klíčem
* USE_SSL_[connection id] - nastavte hodnotu 1 nebo true, pokud se má použít SSL
* SSL_CA_FILE_[connection id] - cesta k souboru s CA certifikátem
* SSL_CERT_FILE_[connection id] - cesta k souboru s certifikátem
* SSL_CERT_FILE_PASSWORD_[connection id] - heslo k souboru s klíčem certifikátu
* SSL_KEY_FILE_[connection id] - cesta k souboru s klíčem
* SSL_REJECT_UNAUTHORIZED_[connection id] - nastavte hodnotu 1 nebo true, pokud se mají odmítat neautorizovaná připojení
* SSL_TRUST_CERTIFICATE_[connection id] - nastavte hodnotu 1 nebo true pro nastavení MSSQL volby trustServerCertificate
* SETTINGS_[settings key] - předkonfigurovaná hodnota nastavení. Klíč nastavení lze zjistit ze zdrojových kódů, https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - cesta k souboru socketu, pokud se připojujete přes socket
* AUTH_TYPE_[connection id] - typ autentizace
  * hostPort (výchozí)
  * socket - hodnota je nastavena implicitně při nastavení SOCKET_PATH
  * tedious - výchozí přenositelná autentizace pro MS SQL, používá tedious driver
  * sspi - integrovaná autentizace Windows (pouze Windows, MS SQL), používá nativní MSSQL driver
  * sql - SQL autentizace (pouze Windows, MS SQL), používá nativní MSSQL driver
* ALLOWED_DATABASES_[connection id] - povolené názvy databází pro zadané připojení, oddělené svislítkem ("|")
* ALLOWED_DATABASES_REGEX_[connection id] - regulární výraz pro povolené názvy databází pro zadané připojení
* USE_SEPARATE_SCHEMAS_[connection id] - nastavte hodnotu 1 nebo true pro samostatné načítání schémat. Použijte, pokud máte velká schémata.
* LOCAL_DATA_CENTER_[connection id] - lokální datové centrum (pro Apache Cassandra)
* CONNECTION_[connection id]_parameterName - nastavení názvu parametru specifického pro engine

SettingsModal.svelte , najděte řetězec "name="/ Pokud potřebujete definovat "true", použijte hodnotu "1". Pokud potřebujete "false", použijte prázdný řetězec ("0" nebude fungovat)

## Konfigurace rolí
Tuto konfiguraci lze použít pouze v edici Team Premium, když je pro nastavení použita úložná databáze. Role z proměnných prostředí jsou při startu docker kontejneru importovány do úložné databáze.
Můžete definovat role se specifickými oprávněními a přiřadit roli připojení. Přiřazování rolí uživatelům se provádí v administračním rozhraní.
* `ROLE_[role_name]_PERMISSIONS` - čárkou oddělený seznam oprávnění pro danou roli. Viz seznam oprávnění níže
* `ROLE_[role_name]_CONNECTIONS` - čárkou oddělený seznam ID připojení přiřazených dané roli
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - ID připojení pro databázové oprávnění s daným ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - svislítkem ("|") oddělený seznam názvů databází pro databázové oprávnění s daným ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - regulární výraz pro názvy databází pro databázové oprávnění s daným ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - jedna z hodnot: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - ID připojení pro tabulkové oprávnění s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - svislítkem ("|") oddělený seznam názvů databází pro databázové oprávnění s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - regulární výraz pro názvy databází pro databázové oprávnění s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - svislítkem ("|") oddělený seznam názvů schémat pro tabulkové oprávnění s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - regulární výraz pro názvy schémat pro tabulkové oprávnění s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - svislítkem ("|") oddělený seznam názvů tabulek pro databázové oprávnění s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - regulární výraz pro názvy tabulek pro databázové oprávnění s daným ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - jedna z hodnot: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - jedna z hodnot: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## Oprávnění
Ve výchozím stavu jsou dostupná všechna oprávnění. Pokud použijete prefix \~, oprávnění je odebráno.

### Příklady
* ~*, widgets/database - všechna oprávnění jsou odebrána, viditelný je pouze databázový widget
* ~widgets/*, widgets/database - všechna oprávnění k widgetům jsou odebrána, viditelný je pouze databázový widget
* ~connections/*, connections/con1 - všechna připojení kromě con1 jsou skryta a zakázána

### Seznam oprávnění
* settings/change - umožňuje měnit nastavení
* plugins/install - umožňuje instalovat pluginy
* widgets/[widget_name] - pokud není uděleno, widget je skrytý. Widget je pruh na levé straně. Dostupné widgety:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - čtení souborů z dané složky
* files/[folder]/write - zápis souborů do dané složky
* apps/write - ukládání do obsahu aplikací
* archive/write - ukládání do obsahu archivu
* connections/[connection_id] - umožňuje vidět a používat definované připojení
* internal-storage = přístup k internímu úložišti (Premium)
* admin/auth - Administrace - záložka Authentication (Premium)
* admin/connections - Administrace - záložka Connections (Premium)
* admin/users - Administrace - záložka Users (Premium)
* admin/roles - Administrace - záložka Roles (Premium)
* dbops/sql-template/* - SQL šablony (např. SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - SQL generátor
* dbops/sql-dump/import - Import SQL dumpu
* dbops/sql-dump/export - Export SQL dumpu
* dbops/query - Spuštění SQL dotazu
* dbops/import - Import dat
* dbops/export - Export dat
* dbops/charts - Zobrazení grafů
* dbops/profiler - Databázový profiler
* dbops/createdb - Vytvoření databáze
* dbops/dropdb - Zrušení databáze
* dbops/model/view - Zobrazení databázového modelu (diagramy, JSON)
* dbops/model/edit - Úprava databázového modelu (vytváření/změna tabulek, pohledů atd.)
* dbops/model/compare - Porovnání databázových modelů
* dbops/table/rename - Přejmenování tabulky
* dbops/table/truncate - Vyprázdnění tabulky
* dbops/table/backup - Vytvoření zálohy tabulky

