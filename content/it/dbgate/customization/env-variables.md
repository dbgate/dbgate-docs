---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: it
title: Variabili d'ambiente
weight: 20
---

La configurazione tramite variabili d'ambiente può essere usata nei container docker, anche quando si utilizza il pacchetto npm. Il pacchetto NPM supporta i file .env.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - pacchetto NPM per l'edizione Community
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - pacchetto NPM per l'edizione Premium
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - immagine Docker per l'edizione Community
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - immagine Docker per l'edizione Premium

## Edizione Premium vs Team Community
L'edizione Community (FOSS) utilizza solo la configurazione dalle variabili d'ambiente elencate di seguito. L'edizione Team Premium utilizza l'archiviazione su database per le impostazioni con l'[interfaccia di amministrazione](/it/features/administration), solo poche impostazioni di base vengono configurate con variabili d'ambiente.

## Configurazione dell'edizione Team Premium
Queste variabili sono disponibili solo nell'edizione Team Premium.
  * STORAGE_SERVER - server di database (nome host) per il database di archiviazione
  * STORAGE_USER - utente del database
  * STORAGE_PASSWORD - password del database
  * STORAGE_PORT - porta del database (opzionale. Se omessa, viene usata la porta predefinita del motore di database selezionato)
  * STORAGE_DATABASE - nome del database di archiviazione
  * STORAGE_SCHEMA - schema del database di archiviazione (opzionale, ad es. per PostgreSQL (tipicamente public) o MS SQL (tipicamente dbo))
  * STORAGE_ENGINE - motore usato per il database di archiviazione. Attualmente MySQL, PostgreSQL, SQL Server e Oracle. Usa uno dei seguenti valori:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - password per l'amministratore. L'amministrazione è disponibile all'URL https://dbgate_url/admin.html. Se la password non è definita e STORAGE_DATABASE è definito, DbGate chiede la password di amministratore al primo avvio.
  * DBGATE_LICENSE - chiave di licenza per DbGate. Contatta sales@dbgate.eu per una licenza di prova. Se non è definita, DbGate Premium chiede la licenza al primo avvio. DbGate Community non richiede alcuna licenza.
  
### Parametri di connessione aggiuntivi dell'archiviazione
  * STORAGE_SOCKET_PATH - percorso del socket per la connessione di archiviazione
  * STORAGE_DATABASE_URL - URL del database per la connessione di archiviazione
  * STORAGE_AUTH_TYPE - tipo di autenticazione per la connessione di archiviazione. I valori sono gli stessi della variabile AUTH_TYPE_xxx
  * STORAGE_USE_SSL - imposta il valore 1 o true quando deve essere usato SSL
  * STORAGE_KEY_FILE - percorso del file di chiave
  * STORAGE_KEY_FILE_PASSWORD - passphrase del file di chiave
  * STORAGE_SSL_CA_FILE - percorso del file CA Cert
  * STORAGE_SSL_CERT_FILE - percorso del file di certificato
  * STORAGE_SSL_CERT_FILE_PASSWORD - password del file di chiave del certificato
  * STORAGE_SSL_KEY_FILE - percorso del file di chiave
  * STORAGE_SSL_KEY_FILE_PASSWORD - passphrase del file di chiave
  * STORAGE_SSL_REJECT_UNAUTHORIZED - imposta il valore 1 o true per rifiutare le connessioni non autorizzate
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - imposta il valore 1 o true per impostare l'opzione MSSQL trustServerCertificate

Le seguenti variabili sono disponibili sia nell'edizione Community sia in quella Premium. Tuttavia, nell'edizione Premium il modo preferito è usare il database di archiviazione e l'interfaccia di amministrazione per la configurazione.

## Configurazione web e permessi
* WEB_ROOT - se hai bisogno di eseguire DbGate in una sottodirectory virtuale (ad es. con il valore /dbadmin, dbgate sarà accessibile su localhost:3000/dbadmin)
* LOGIN , PASSWORD - credenziali per accedere all'app web
* PERMISSIONS - elenco di permessi separati da virgola. Vedi anche l'elenco dei permessi più sotto
* SHELL_CONNECTION - se true o 1, le connessioni possono essere definite negli script shell. Altrimenti sono consentite solo le connessioni preconfigurate. Per impostazione predefinita questo non è consentito per motivi di sicurezza. Attenzione: quando è consentito, le password cifrate vengono inviate al frontend.
* SHELL_SCRIPTING - se true o 1, sono consentiti script shell JavaScript personalizzati. Per impostazione predefinita questo non è consentito per motivi di sicurezza.
* LOGIN_PASSWORD_[login] - password per il login specificato
* LOGIN_PERMISSIONS_[login] - elenco di permessi separati da virgola per il login indicato. Vedi anche l'elenco dei permessi più sotto
* TOKEN_LIFETIME - durata del token di accesso. Trascorso questo tempo, l'utente connesso verrà reindirizzato alla pagina di login. Il valore predefinito è 1d (significa 1 giorno). Sono possibili valori come 3h (3 ore), 10m (10 minuti), 2d (2 giorni)
* SINGLE_CONNECTION - ID della connessione. Se definito, sarà disponibile solo questa connessione (deve essere usato con SINGLE_DATABASE)
* SINGLE_DATABASE - nome del database, sarà disponibile solo questo database. (deve essere usato con SINGLE_CONNECTION)
* BASIC_AUTH - se true o 1, viene usata l'autenticazione basic sia per il web sia per le API. Altrimenti vengono usati il modulo di login e l'autenticazione API basata su token JWT. L'autenticazione basic non può essere usata per l'autenticazione OAuth.
* SKIP_ALL_AUTH - se true o 1, tutta l'autenticazione viene saltata
* ALLOW_DBGATE_PRIVATE_CLOUD - per impostazione predefinita, DbGate Cloud è disabilitato per la versione web. Con questa variabile puoi abilitarlo
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - nella versione web, reindirizza al login di DbGate Cloud invece di aprire una nuova finestra
* LANGUAGE - lingua dell'interfaccia, ad es. en, cs, de, fr, ecc. Vedi la tabella di configurazione delle lingue più sotto. Imposta "auto" per usare la lingua del browser

## Configurazione delle lingue
| Lingua | Valore |
|----------|-------|
| Inglese | en |
| Tedesco | de |
| Spagnolo | es |
| Francese | fr |
| Italiano | it |
| Portoghese (Brasile) | pt |
| Giapponese | ja |
| Cinese - semplificato | zh |
| Ceco | cs |
| Slovacco | sk |


## Configurazione del logging
* LOG_LEVEL - tutti i messaggi con questo livello di log o superiore verranno registrati. Uno dei valori trace, debug, info, warn, error, fatal. Il valore predefinito è info
* FILE_LOG_LEVEL - livello di log per la registrazione su file di log. Per il logging su file, questo ha priorità maggiore rispetto a LOG_LEVEL
* CONSOLE_LOG_LEVEL - livello di log per la registrazione su file di log. Per il logging su console, questo ha priorità maggiore rispetto a LOG_LEVEL

## Configurazione OAuth (solo versione web)
* OAUTH_AUTH - endpoint di autenticazione del protocollo OAuth
* OAUTH_TOKEN - endpoint del token del protocollo OAuth
* OAUTH_LOGOUT - URL di logout del provider OAuth. L'utente verrà reindirizzato a questo URL quando richiede la disconnessione
* OAUTH_CLIENT_ID - ID client
* OAUTH_CLIENT_SECRET - segreto del client
* OAUTH_LOGIN_FIELD - nome del campo del payload che contiene il nome di login. Per i campi disponibili puoi ispezionare il log di dbgate: il payload inviato dal provider OAuth viene registrato nella console. Questo nome di login viene usato ad es. per configurare i permessi. Non è necessariamente il login inserito in OAuth. Se non specificato, tutti gli utenti del provider OAuth avranno lo stesso nome di login.
* OAUTH_ALLOWED_LOGINS - nomi di login separati da virgola a cui sarà consentito l'accesso. Se non specificato, tutti i login potranno usare l'app DbGate.
* OAUTH_SCOPE - scope che viene inviato agli endpoint OAuth authorize e token
* OAUTH_GROUP_FIELD - campo del payload OAuth che indica il gruppo
* OAUTH_ALLOWED_GROUPS - nomi di gruppo consentiti separati da virgola

## Configurazione Active Directory/LDAP (solo versione web)
* AD_URL - URL del provider LDAP (ad es. ldap://domain.com)
* AD_BASEDN - ad es. dc=domain,dc=com
* AD_USERNAME - nome utente per Active Directory
* AD_PASSWORD - password per Active Directory
* AD_ALLOWED_LOGINS - nomi di login separati da virgola a cui sarà consentito l'accesso. Se non specificato, tutti i login potranno usare l'app DbGate.

## Configurazione del client Oracle  
* ORACLE_INSTANT_CLIENT - percorso dell'[Oracle instant client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html)

## Configurazione delle connessioni
Puoi configurare l'elenco delle connessioni con le variabili d'ambiente; in tal caso i comandi "Add connection" e "Edit connection" non saranno disponibili.

* CONNECTIONS - elenco dei nomi delle connessioni preconfigurate, separati da virgola. Nelle opzioni seguenti, [connection id] è l'ID di questo elenco
* LABEL_[connection id] - etichetta (nome visualizzato) della connessione. 
* SERVER_[connection id] - server (nome host) della connessione.
* USER_[connection id] - nome utente per la connessione al DB.
* PASSWORD_[connection id] - password per la connessione al DB.
* PASSWORD_MODE_[connection id] - determina se la password e il nome utente sono memorizzati o devono essere inseriti dall'utente. Uno dei seguenti valori:
  * askPassword - DbGate chiede la password durante la connessione
  * askUser - DbGate chiede nome utente e password
* PORT_[connection id] - porta per la connessione al DB.
* FILE_[connection id] - percorso del file di database (per SQLite).
* URL_[connection id] - URL del database (funziona per MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle).
* SERVICE_NAME_[connection id] - nome del servizio Oracle.
* DATABASE_[connection id] - nome del database predefinito.
* READONLY_[connection id] - connetti in modalità sola lettura
* ENGINE_[connection id] - motore della connessione (**obbligatorio**, nome del motore con il plugin), uno tra:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - imposta il valore 1 o true quando deve essere usato un tunnel SSH
* SSH_HOST_[connection id] - nome host SSH
* SSH_PORT_[connection id] - numero di porta SSH
* SSH_MODE_[connection id] - uno dei seguenti valori
  * userPassword - autenticazione con utente e password
  * agent - autenticazione con agente SSH
  * keyFile - autenticazione con file di chiave
* SSH_LOGIN_[connection id] - login SSH
* SSH_PASSWORD_[connection id] - password SSH
* SSH_KEY_FILE_[connection id] - percorso completo del file di chiave
* SSH_KEY_FILE_PASSWORD_[connection id] - passphrase del file di chiave
* USE_SSL_[connection id] - imposta il valore 1 o true quando deve essere usato SSL
* SSL_CA_FILE_[connection id] - percorso del file CA Cert
* SSL_CERT_FILE_[connection id] - percorso del file di certificato
* SSL_CERT_FILE_PASSWORD_[connection id] - password del file di chiave del certificato
* SSL_KEY_FILE_[connection id] - percorso del file di chiave
* SSL_REJECT_UNAUTHORIZED_[connection id] - imposta il valore 1 o true per rifiutare le connessioni non autorizzate
* SSL_TRUST_CERTIFICATE_[connection id] - imposta il valore 1 o true per impostare l'opzione MSSQL trustServerCertificate
* SETTINGS_[settings key] - preconfigura un valore di impostazione. La chiave dell'impostazione può essere ricavata dal codice sorgente, https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - percorso del file socket, se ci si connette tramite socket
* AUTH_TYPE_[connection id] - tipo di autenticazione
  * hostPort (predefinito)
  * socket - il valore viene impostato implicitamente quando si imposta SOCKET_PATH
  * tedious - autenticazione portabile predefinita per MS SQL, usando il driver tedious
  * sspi - autenticazione integrata di Windows (solo Windows, MS SQL), usando il driver MSSQL nativo
  * sql - autenticazione SQL (solo Windows, MS SQL), usando il driver MSSQL nativo
* ALLOWED_DATABASES_[connection id] - nomi di database consentiti per la connessione specificata, separati da pipe ("|")
* ALLOWED_DATABASES_REGEX_[connection id] - espressione regolare per i nomi di database consentiti per la connessione specificata
* USE_SEPARATE_SCHEMAS_[connection id] - imposta il valore 1 o true per caricare gli schemi separatamente. Usalo se hai schemi di grandi dimensioni.
* LOCAL_DATA_CENTER_[connection id] - data center locale (per Apache Cassandra)
* CONNECTION_[connection id]_parameterName - imposta un nome di parametro specifico del motore

SettingsModal.svelte , cerca la stringa "name="/ Se hai bisogno di definire "true", usa il valore "1". Se hai bisogno di "false", usa una stringa vuota ("0" non funzionerà)

## Configurazione dei ruoli
Questa configurazione può essere usata solo nell'edizione Team Premium, quando il database di archiviazione è usato per le impostazioni. I ruoli definiti dalle variabili d'ambiente vengono importati nel database di archiviazione all'avvio del container docker.
Puoi definire ruoli con permessi specifici e assegnare connessioni al ruolo. L'assegnazione dei ruoli agli utenti avviene nell'interfaccia di amministrazione.
* `ROLE_[role_name]_PERMISSIONS` - elenco di permessi separati da virgola per il ruolo indicato. Vedi l'elenco dei permessi più sotto
* `ROLE_[role_name]_CONNECTIONS` - elenco di ID di connessione separati da virgola assegnati al ruolo indicato
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - ID della connessione per il permesso di database con l'ID indicato
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - elenco di nomi di database separati da pipe ("|") per il permesso di database con l'ID indicato
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - espressione regolare per i nomi di database per il permesso di database con l'ID indicato
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - uno tra: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - ID della connessione per il permesso di tabella con l'ID indicato
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - elenco di nomi di database separati da pipe ("|") per il permesso di database con l'ID indicato
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - espressione regolare per i nomi di database per il permesso di database con l'ID indicato
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - elenco di nomi di schema separati da pipe ("|") per il permesso di tabella con l'ID indicato
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - espressione regolare per i nomi di schema per il permesso di tabella con l'ID indicato
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - elenco di nomi di tabella separati da pipe ("|") per il permesso di database con l'ID indicato
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - espressione regolare per i nomi di tabella per il permesso di database con l'ID indicato
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - uno tra: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - uno tra: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## Permessi
Per impostazione predefinita, tutti i permessi sono disponibili. Se usi il prefisso \~, il permesso viene revocato.

### Esempi
* ~*, widgets/database - tutti i permessi sono revocati, solo il widget del database è visibile
* ~widgets/*, widgets/database - tutti i permessi dei widget sono revocati, solo il widget del database è visibile
* ~connections/*, connections/con1 - tutte le connessioni tranne con1 sono nascoste e disabilitate

### Elenco dei permessi
* settings/change - consente di modificare le impostazioni
* plugins/install - consente di installare i plugin
* widgets/[widget_name] - se non concesso, il widget è nascosto. Il widget è la striscia sul lato sinistro. Widget disponibili:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - legge i file dalla cartella indicata
* files/[folder]/write - scrive i file nella cartella indicata
* apps/write - salva nel contenuto delle app
* archive/write - salva nel contenuto dell'archivio
* connections/[connection_id] - consente di vedere e usare la connessione definita
* internal-storage = accesso all'archiviazione interna (Premium)
* admin/auth - Amministrazione - scheda Authentication (Premium)
* admin/connections - Amministrazione - scheda Connections (Premium)
* admin/users - Amministrazione - scheda Users (Premium)
* admin/roles - Amministrazione - scheda Roles (Premium)
* dbops/sql-template/* - template SQL (ad es. SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - generatore SQL
* dbops/sql-dump/import - importa dump SQL
* dbops/sql-dump/export - esporta dump SQL
* dbops/query - esegui query SQL
* dbops/import - importa dati
* dbops/export - esporta dati
* dbops/charts - visualizza grafici
* dbops/profiler - profiler del database
* dbops/createdb - crea database
* dbops/dropdb - elimina database
* dbops/model/view - visualizza il modello del database (diagrammi, JSON)
* dbops/model/edit - modifica il modello del database (crea/modifica tabelle, viste, ecc.)
* dbops/model/compare - confronta modelli di database
* dbops/table/rename - rinomina tabella
* dbops/table/truncate - svuota tabella
* dbops/table/backup - crea backup della tabella

