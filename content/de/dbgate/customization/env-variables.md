---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: de
title: Umgebungsvariablen
weight: 20
---

Die Konfiguration über Umgebungsvariablen kann in Docker-Containern verwendet werden, ebenso bei Verwendung des npm-Pakets. Das NPM-Paket unterstützt .env-Dateien.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - NPM-Paket für die Community-Edition
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - NPM-Paket für die Premium-Edition
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - Docker-Image für die Community-Edition
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - Docker-Image für die Premium-Edition

## Premium- vs. Team-Community-Edition
Die Community-Edition (FOSS) verwendet ausschließlich die Konfiguration aus den unten aufgeführten Umgebungsvariablen. Die Team Premium-Edition speichert die Einstellungen in einer Datenbank und bietet eine [Administrationsoberfläche](/de/features/administration); nur wenige grundlegende Einstellungen werden über Umgebungsvariablen konfiguriert.

## Konfiguration der Team Premium-Edition
Diese Variablen sind nur in der Team Premium-Edition verfügbar.
  * STORAGE_SERVER - Datenbankserver (Hostname) für die Storage-Datenbank
  * STORAGE_USER - Datenbankbenutzer
  * STORAGE_PASSWORD - Datenbankkennwort
  * STORAGE_PORT - Datenbankport (optional. Wird er weggelassen, wird der Standardport der ausgewählten Datenbank-Engine verwendet)
  * STORAGE_DATABASE - Name der Storage-Datenbank
  * STORAGE_SCHEMA - Schema der Storage-Datenbank (optional, z. B. für PostgreSQL (typischerweise public) oder MS SQL (typischerweise dbo))
  * STORAGE_ENGINE - Engine für die Storage-Datenbank. Derzeit MySQL, PostgreSQL, SQL Server und Oracle. Verwenden Sie einen der folgenden Werte:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - Kennwort für den Administrator. Die Administration ist unter der URL https://dbgate_url/admin.html verfügbar. Wenn kein Kennwort definiert ist und STORAGE_DATABASE definiert ist, fragt DbGate beim ersten Start nach dem Admin-Kennwort.
  * DBGATE_LICENSE - Lizenzschlüssel für DbGate. Für eine Testlizenz wenden Sie sich bitte an sales@dbgate.eu. Wenn nicht definiert, fragt DbGate Premium beim ersten Start nach der Lizenz. DbGate Community benötigt keine Lizenz.
  
### Zusätzliche Verbindungsparameter des Storage
  * STORAGE_SOCKET_PATH - Socket-Pfad für die Storage-Verbindung
  * STORAGE_DATABASE_URL - Datenbank-URL für die Storage-Verbindung
  * STORAGE_AUTH_TYPE - Authentifizierungstyp für die Storage-Verbindung. Die Werte sind dieselben wie für die Variable AUTH_TYPE_xxx
  * STORAGE_USE_SSL - Wert 1 oder true setzen, wenn SSL verwendet werden soll
  * STORAGE_KEY_FILE - Pfad zur Schlüsseldatei
  * STORAGE_KEY_FILE_PASSWORD - Passphrase der Schlüsseldatei
  * STORAGE_SSL_CA_FILE - Pfad zur CA-Zertifikatsdatei
  * STORAGE_SSL_CERT_FILE - Pfad zur Zertifikatsdatei
  * STORAGE_SSL_CERT_FILE_PASSWORD - Kennwort der Zertifikatsschlüsseldatei
  * STORAGE_SSL_KEY_FILE - Pfad zur Schlüsseldatei
  * STORAGE_SSL_KEY_FILE_PASSWORD - Passphrase der Schlüsseldatei
  * STORAGE_SSL_REJECT_UNAUTHORIZED - Wert 1 oder true setzen, wenn nicht autorisierte Verbindungen abgelehnt werden sollen
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - Wert 1 oder true setzen, um die MSSQL-Option trustServerCertificate zu aktivieren

Die folgenden Variablen sind sowohl in der Community- als auch in der Premium-Edition verfügbar. In der Premium-Edition ist es jedoch der bevorzugte Weg, die Storage-Datenbank zu verwenden und die Konfiguration über die Administrationsoberfläche vorzunehmen.

## Web- & Berechtigungskonfiguration
* WEB_ROOT - falls Sie DbGate in einem virtuellen Unterverzeichnis betreiben müssen (z. B. beim Wert /dbadmin ist DbGate unter localhost:3000/dbadmin erreichbar)
* LOGIN , PASSWORD - Zugangsdaten für den Zugriff auf die Web-App
* PERMISSIONS - Liste kommagetrennter Berechtigungen. Siehe auch die Berechtigungsliste unten
* SHELL_CONNECTION - falls true oder 1, können Verbindungen in Shell-Skripten definiert werden. Andernfalls sind nur vorkonfigurierte Verbindungen erlaubt. Standardmäßig ist dies aus Sicherheitsgründen nicht erlaubt. Beachten Sie: wenn erlaubt, werden verschlüsselte Kennwörter an das Frontend gesendet.
* SHELL_SCRIPTING - falls true oder 1, sind eigene JavaScript-Shell-Skripte erlaubt. Standardmäßig ist dies aus Sicherheitsgründen nicht erlaubt.
* LOGIN_PASSWORD_[login] - Kennwort für den angegebenen Login
* LOGIN_PERMISSIONS_[login] - Liste kommagetrennter Berechtigungen für den angegebenen Login. Siehe auch die Berechtigungsliste unten
* TOKEN_LIFETIME - Lebensdauer des Access-Tokens. Nach Ablauf dieser Zeit wird der angemeldete Benutzer auf die Login-Seite umgeleitet. Standard ist 1d (bedeutet 1 Tag). Möglich sind Werte wie 3h (3 Stunden), 10m (10 Minuten), 2d (2 Tage)
* SINGLE_CONNECTION - Verbindungs-ID. Falls definiert, ist nur diese Verbindung verfügbar (muss zusammen mit SINGLE_DATABASE verwendet werden)
* SINGLE_DATABASE - Datenbankname, nur diese Datenbank ist verfügbar. (muss zusammen mit SINGLE_CONNECTION verwendet werden)
* BASIC_AUTH - falls true oder 1, wird Basic-Authentifizierung für Web und API verwendet. Andernfalls werden das Login-Formular und die JWT-Token-basierte API-Authentifizierung verwendet. Basic-Authentifizierung kann nicht für OAuth-Authentifizierung verwendet werden.
* SKIP_ALL_AUTH - falls true oder 1, wird die gesamte Authentifizierung übersprungen
* ALLOW_DBGATE_PRIVATE_CLOUD - standardmäßig ist DbGate Cloud in der Web-Version deaktiviert. Mit dieser Variable können Sie es aktivieren
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - in der Web-Version zum DbGate Cloud-Login weiterleiten, anstatt ein neues Fenster zu öffnen
* LANGUAGE - Sprache der Benutzeroberfläche, z. B. en, cs, de, fr usw. Siehe die Tabelle zur Sprachkonfiguration unten. Setzen Sie "auto", um die Browsersprache zu verwenden

## Sprachkonfiguration
| Sprache | Wert |
|----------|-------|
| Englisch | en |
| Deutsch | de |
| Spanisch | es |
| Französisch | fr |
| Italienisch | it |
| Portugiesisch (Brasilien) | pt |
| Japanisch | ja |
| Chinesisch - vereinfacht | zh |
| Tschechisch | cs |
| Slowakisch | sk |


## Logging-Konfiguration
* LOG_LEVEL - alle Meldungen mit diesem Log-Level oder höher werden protokolliert. Einer der Werte trace, debug, info, warn, error, fatal. Standard ist info
* FILE_LOG_LEVEL - Log-Level für die Protokollierung in die Logdatei. Für die Datei-Protokollierung hat dies eine höhere Priorität als LOG_LEVEL
* CONSOLE_LOG_LEVEL - Log-Level für die Protokollierung in die Logdatei. Für die Konsolen-Protokollierung hat dies eine höhere Priorität als LOG_LEVEL

## OAuth-Konfiguration (nur Web-Version)
* OAUTH_AUTH - Authentifizierungs-Endpunkt des OAuth-Protokolls
* OAUTH_TOKEN - Token-Endpunkt des OAuth-Protokolls
* OAUTH_LOGOUT - Logout-URL des OAuth-Providers. Der Benutzer wird zu dieser URL weitergeleitet, wenn er sich abmelden möchte
* OAUTH_CLIENT_ID - Client-ID
* OAUTH_CLIENT_SECRET - Client Secret
* OAUTH_LOGIN_FIELD - Feldname aus dem Payload, der den Login-Namen enthält. Die verfügbaren Felder können Sie im DbGate-Log einsehen, das vom OAuth-Provider gesendete Payload wird in der Konsole protokolliert. Dieser Login-Name wird z. B. zum Konfigurieren von Berechtigungen verwendet. Es ist nicht zwingend der in OAuth eingegebene Login. Wenn nicht angegeben, haben alle Benutzer vom OAuth-Provider denselben Login-Namen.
* OAUTH_ALLOWED_LOGINS - kommagetrennte Login-Namen, denen die Anmeldung erlaubt ist. Wenn nicht angegeben, dürfen alle Logins die DbGate-App verwenden.
* OAUTH_SCOPE - Scope, der an den OAuth-Authorize- und Token-Endpunkt gesendet wird
* OAUTH_GROUP_FIELD - Feld im Payload von OAuth, das die Gruppe bezeichnet
* OAUTH_ALLOWED_GROUPS - kommagetrennte Liste erlaubter Gruppennamen

## Active Directory/LDAP-Konfiguration (nur Web-Version)
* AD_URL - URL des LDAP-Providers (z. B. ldap://domain.com)
* AD_BASEDN - z. B. dc=domain,dc=com
* AD_USERNAME - Benutzername für Active Directory
* AD_PASSWORD - Kennwort für Active Directory
* AD_ALLOWED_LOGINS - kommagetrennte Login-Namen, denen die Anmeldung erlaubt ist. Wenn nicht angegeben, dürfen alle Logins die DbGate-App verwenden.

## Oracle-Client-Konfiguration  
* ORACLE_INSTANT_CLIENT - Pfad zum [Oracle Instant Client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html)

## Verbindungskonfiguration
Sie können die Verbindungsliste über Umgebungsvariablen konfigurieren, dann sind die Befehle "Add connection" und "Edit connection" nicht verfügbar.

* CONNECTIONS - Liste der vorkonfigurierten Verbindungsnamen, kommagetrennt. In den folgenden Optionen ist [connection id] eine ID aus dieser Liste
* LABEL_[connection id] - Bezeichnung (Anzeigename) der Verbindung. 
* SERVER_[connection id] - Server (Hostname) der Verbindung.
* USER_[connection id] - Benutzername für die DB-Verbindung.
* PASSWORD_[connection id] - Kennwort für die DB-Verbindung.
* PASSWORD_MODE_[connection id] - legt fest, ob Kennwort und Benutzername gespeichert werden oder vom Benutzer eingegeben werden müssen. Einer der folgenden Werte:
  * askPassword - DbGate fragt beim Verbinden nach dem Kennwort
  * askUser - DbGate fragt nach Benutzername und Kennwort
* PORT_[connection id] - Port für die DB-Verbindung.
* FILE_[connection id] - Pfad zur Datenbankdatei (für SQLite).
* URL_[connection id] - Datenbank-URL (funktioniert für MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle).
* SERVICE_NAME_[connection id] - Oracle-Servicename.
* DATABASE_[connection id] - Standard-Datenbankname.
* READONLY_[connection id] - im Readonly-Modus verbinden
* ENGINE_[connection id] - Engine der Verbindung (**Pflichtfeld**, Name der Engine mit Plugin), eine von:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - Wert 1 oder true setzen, wenn ein SSH-Tunnel verwendet werden soll
* SSH_HOST_[connection id] - SSH-Hostname
* SSH_PORT_[connection id] - SSH-Portnummer
* SSH_MODE_[connection id] - einer der folgenden Werte
  * userPassword - Authentifizierung mit Benutzer und Kennwort
  * agent - Authentifizierung mit SSH-Agent
  * keyFile - Authentifizierung mit Schlüsseldatei
* SSH_LOGIN_[connection id] - SSH-Login
* SSH_PASSWORD_[connection id] - SSH-Kennwort
* SSH_KEY_FILE_[connection id] - vollständiger Pfad zur Schlüsseldatei
* SSH_KEY_FILE_PASSWORD_[connection id] - Passphrase der Schlüsseldatei
* USE_SSL_[connection id] - Wert 1 oder true setzen, wenn SSL verwendet werden soll
* SSL_CA_FILE_[connection id] - Pfad zur CA-Zertifikatsdatei
* SSL_CERT_FILE_[connection id] - Pfad zur Zertifikatsdatei
* SSL_CERT_FILE_PASSWORD_[connection id] - Kennwort der Zertifikatsschlüsseldatei
* SSL_KEY_FILE_[connection id] - Pfad zur Schlüsseldatei
* SSL_REJECT_UNAUTHORIZED_[connection id] - Wert 1 oder true setzen, wenn nicht autorisierte Verbindungen abgelehnt werden sollen
* SSL_TRUST_CERTIFICATE_[connection id] - Wert 1 oder true setzen, um die MSSQL-Option trustServerCertificate zu aktivieren
* SETTINGS_[settings key] - Einstellungswert vorkonfigurieren. Die Einstellungsschlüssel können aus dem Quellcode entnommen werden, https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - Pfad zur Socket-Datei, falls über Socket verbunden wird
* AUTH_TYPE_[connection id] - Authentifizierungstyp
  * hostPort (Standard)
  * socket - der Wert wird implizit gesetzt, wenn SOCKET_PATH konfiguriert ist
  * tedious - portable Standard-Authentifizierung für MS SQL, mit dem tedious-Treiber
  * sspi - integrierte Windows-Authentifizierung (nur Windows, MS SQL), mit dem nativen MSSQL-Treiber
  * sql - SQL-Authentifizierung (nur Windows, MS SQL), mit dem nativen MSSQL-Treiber
* ALLOWED_DATABASES_[connection id] - erlaubte Datenbanknamen für die angegebene Verbindung, durch Pipe ("|") getrennt
* ALLOWED_DATABASES_REGEX_[connection id] - regulärer Ausdruck für erlaubte Datenbanknamen der angegebenen Verbindung
* USE_SEPARATE_SCHEMAS_[connection id] - Wert 1 oder true setzen, um Schemas separat zu laden. Verwenden Sie dies, wenn Sie große Schemas haben.
* LOCAL_DATA_CENTER_[connection id] - lokales Rechenzentrum (für Apache Cassandra)
* CONNECTION_[connection id]_parameterName - engine-spezifischen Parameternamen setzen

SettingsModal.svelte , suchen Sie nach der Zeichenkette "name="/ Wenn Sie "true" definieren müssen, verwenden Sie den Wert "1". Wenn Sie "false" benötigen, verwenden Sie eine leere Zeichenkette ("0" funktioniert nicht)

## Rollenkonfiguration
Diese Konfiguration kann nur in der Team Premium-Edition verwendet werden, wenn eine Storage-Datenbank für die Einstellungen genutzt wird. Rollen aus Umgebungsvariablen werden beim Start des Docker-Containers in die Storage-Datenbank importiert.
Sie können Rollen mit bestimmten Berechtigungen definieren und der Rolle Verbindungen zuweisen. Die Zuweisung von Rollen an Benutzer erfolgt in der Administrationsoberfläche.
* `ROLE_[role_name]_PERMISSIONS` - kommagetrennte Liste der Berechtigungen für die angegebene Rolle. Siehe die Berechtigungsliste unten
* `ROLE_[role_name]_CONNECTIONS` - kommagetrennte Liste der Verbindungs-IDs, die der angegebenen Rolle zugewiesen sind
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - Verbindungs-ID für die Datenbankberechtigung mit der angegebenen ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - durch Pipe ("|") getrennte Liste der Datenbanknamen für die Datenbankberechtigung mit der angegebenen ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - regulärer Ausdruck für Datenbanknamen der Datenbankberechtigung mit der angegebenen ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - einer von: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - Verbindungs-ID für die Tabellenberechtigung mit der angegebenen ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - durch Pipe ("|") getrennte Liste der Datenbanknamen für die Datenbankberechtigung mit der angegebenen ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - regulärer Ausdruck für Datenbanknamen der Datenbankberechtigung mit der angegebenen ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - durch Pipe ("|") getrennte Liste der Schemanamen für die Tabellenberechtigung mit der angegebenen ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - regulärer Ausdruck für Schemanamen der Tabellenberechtigung mit der angegebenen ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - durch Pipe ("|") getrennte Liste der Tabellennamen für die Datenbankberechtigung mit der angegebenen ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - regulärer Ausdruck für Tabellennamen der Tabellenberechtigung mit der angegebenen ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - einer von: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - einer von: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## Berechtigungen
Standardmäßig sind alle Berechtigungen verfügbar. Wenn Sie das Präfix \~ verwenden, wird die Berechtigung entzogen.

### Beispiele
* ~*, widgets/database - alle Berechtigungen werden entzogen, nur das Datenbank-Widget ist sichtbar
* ~widgets/*, widgets/database - alle Widget-Berechtigungen werden entzogen, nur das Datenbank-Widget ist sichtbar
* ~connections/*, connections/con1 - alle Verbindungen außer con1 sind ausgeblendet und deaktiviert

### Berechtigungsliste
* settings/change - erlaubt das Ändern von Einstellungen
* plugins/install - erlaubt das Installieren von Plugins
* widgets/[widget_name] - wenn nicht gewährt, ist das Widget ausgeblendet. Widgets sind die Leiste auf der linken Seite. Verfügbare Widgets:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - Dateien aus dem angegebenen Ordner lesen
* files/[folder]/write - Dateien in den angegebenen Ordner schreiben
* apps/write - in App-Inhalte speichern
* archive/write - in Archiv-Inhalte speichern
* connections/[connection_id] - erlaubt, die definierte Verbindung zu sehen und zu nutzen
* internal-storage = Zugriff auf den internen Speicher (Premium)
* admin/auth - Administration - Registerkarte Authentifizierung (Premium)
* admin/connections - Administration - Registerkarte Verbindungen (Premium)
* admin/users - Administration - Registerkarte Benutzer (Premium)
* admin/roles - Administration - Registerkarte Rollen (Premium)
* dbops/sql-template/* - SQL-Vorlagen (z. B. SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - SQL-Generator
* dbops/sql-dump/import - SQL-Dump importieren
* dbops/sql-dump/export - SQL-Dump exportieren
* dbops/query - SQL-Abfrage ausführen
* dbops/import - Daten importieren
* dbops/export - Daten exportieren
* dbops/charts - Diagramme anzeigen
* dbops/profiler - Datenbank-Profiler
* dbops/createdb - Datenbank erstellen
* dbops/dropdb - Datenbank löschen
* dbops/model/view - Datenbankmodell anzeigen (Diagramme, JSON)
* dbops/model/edit - Datenbankmodell bearbeiten (Tabellen, Views usw. erstellen/ändern)
* dbops/model/compare - Datenbankmodelle vergleichen
* dbops/table/rename - Tabelle umbenennen
* dbops/table/truncate - Tabelle leeren (truncate)
* dbops/table/backup - Tabellen-Backup erstellen

