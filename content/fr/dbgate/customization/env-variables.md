---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: fr
title: Variables d'environnement
weight: 20
---

La configuration via les variables d'environnement peut être utilisée dans les conteneurs docker, ainsi qu'avec le paquet npm. Le paquet NPM prend en charge les fichiers .env.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - paquet NPM pour l'édition Community
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - paquet NPM pour l'édition Premium
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - image Docker pour l'édition Community
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - image Docker pour l'édition Premium

## Édition Premium ou Team Community
L'édition Community (FOSS) utilise uniquement la configuration issue des variables d'environnement listées ci-dessous. L'édition Team Premium utilise un stockage en base de données pour les paramètres avec une [interface d'administration](/fr/features/administration), seuls quelques paramètres de base sont configurés avec des variables d'environnement.

## Configuration de l'édition Team Premium
Ces variables sont disponibles uniquement dans l'édition Team Premium.
  * STORAGE_SERVER - serveur de base de données (nom d'hôte) pour la base de données de stockage
  * STORAGE_USER - utilisateur de la base de données
  * STORAGE_PASSWORD - mot de passe de la base de données
  * STORAGE_PORT - port de la base de données (facultatif. S'il est omis, le port par défaut du moteur de base de données sélectionné est utilisé)
  * STORAGE_DATABASE - nom de la base de données de stockage
  * STORAGE_SCHEMA - schéma de la base de données de stockage (facultatif, par ex. pour PostgreSQL (typiquement public) ou MS SQL (typiquement dbo))
  * STORAGE_ENGINE - moteur utilisé pour la base de données de stockage. Actuellement, MySQL, PostgreSQL, SQL Server et Oracle. Utilisez l'une des valeurs suivantes :
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - mot de passe de l'administrateur. L'administration est disponible à l'URL https://dbgate_url/admin.html. Si le mot de passe n'est pas défini et que STORAGE_DATABASE est défini, DbGate demande le mot de passe administrateur au premier démarrage.
  * DBGATE_LICENSE - clé de licence pour DbGate. Veuillez contacter sales@dbgate.eu pour une licence d'essai. Si elle n'est pas définie, DbGate Premium demande la licence au premier démarrage. DbGate Community ne nécessite aucune licence.
  
### Paramètres de connexion supplémentaires du stockage
  * STORAGE_SOCKET_PATH - chemin du socket pour la connexion de stockage
  * STORAGE_DATABASE_URL - URL de la base de données pour la connexion de stockage
  * STORAGE_AUTH_TYPE - type d'authentification pour la connexion de stockage. Les valeurs sont les mêmes que pour la variable AUTH_TYPE_xxx
  * STORAGE_USE_SSL - définissez la valeur 1 ou true lorsque SSL doit être utilisé
  * STORAGE_KEY_FILE - chemin vers le fichier de clé
  * STORAGE_KEY_FILE_PASSWORD - phrase secrète du fichier de clé
  * STORAGE_SSL_CA_FILE - chemin vers le fichier de certificat CA
  * STORAGE_SSL_CERT_FILE - chemin vers le fichier de certificat
  * STORAGE_SSL_CERT_FILE_PASSWORD - mot de passe du fichier de clé du certificat
  * STORAGE_SSL_KEY_FILE - chemin vers le fichier de clé
  * STORAGE_SSL_KEY_FILE_PASSWORD - phrase secrète du fichier de clé
  * STORAGE_SSL_REJECT_UNAUTHORIZED - définissez la valeur 1 ou true pour rejeter les connexions non autorisées
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - définissez la valeur 1 ou true pour activer l'option MSSQL trustServerCertificate

Les variables suivantes sont disponibles à la fois dans les éditions Community et Premium. Cependant, dans l'édition Premium, la méthode recommandée consiste à utiliser la base de données de stockage et l'interface d'administration pour la configuration.

## Configuration web et des permissions
* WEB_ROOT - si vous devez exécuter DbGate dans un sous-répertoire virtuel (par ex. pour la valeur /dbadmin , dbgate sera accessible sur localhost:3000/dbadmin )
* LOGIN , PASSWORD - identifiants pour accéder à l'application web
* PERMISSIONS - liste de permissions séparées par des virgules. Voir aussi la liste des permissions ci-dessous
* SHELL_CONNECTION - si true ou 1, les connexions peuvent être définies dans les scripts shell. Sinon, seules les connexions préconfigurées sont autorisées. Par défaut, ceci n'est pas autorisé pour des raisons de sécurité. Attention : lorsque cela est autorisé, les mots de passe chiffrés sont envoyés au frontend.
* SHELL_SCRIPTING - si true ou 1, les scripts shell JavaScript personnalisés sont autorisés. Par défaut, ceci n'est pas autorisé pour des raisons de sécurité.
* LOGIN_PASSWORD_[login] - mot de passe pour le login spécifié
* LOGIN_PERMISSIONS_[login] - liste de permissions séparées par des virgules pour le login donné. Voir aussi la liste des permissions ci-dessous
* TOKEN_LIFETIME - durée de vie du jeton d'accès. Passé ce délai, l'utilisateur connecté sera redirigé vers la page de connexion. La valeur par défaut est 1d (soit 1 jour). Des valeurs comme 3h (3 heures), 10m (10 minutes), 2d (2 jours) sont possibles
* SINGLE_CONNECTION - identifiant de connexion. S'il est défini, seule cette connexion sera disponible (doit être utilisé avec SINGLE_DATABASE)
* SINGLE_DATABASE - nom de base de données, seule cette base de données sera disponible. (doit être utilisé avec SINGLE_CONNECTION)
* BASIC_AUTH - si true ou 1 , l'authentification basique est utilisée à la fois pour le web et l'API. Sinon, le formulaire de connexion et l'authentification API basée sur un jeton JWT sont utilisés. L'authentification basique ne peut pas être utilisée pour l'authentification OAuth.
* SKIP_ALL_AUTH - si true ou 1, toute authentification est ignorée
* ALLOW_DBGATE_PRIVATE_CLOUD - par défaut, DbGate cloud est désactivé pour la version web. Cette variable permet de l'activer
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - dans la version web, redirige vers la connexion DbGate cloud au lieu d'ouvrir une nouvelle fenêtre
* LANGUAGE - langue de l'interface, par ex. en, cs, de, fr, etc. Voir le tableau de configuration des langues ci-dessous. Définissez "auto" pour utiliser la langue du navigateur

## Configuration des langues
| Langue | Valeur |
|----------|-------|
| Anglais | en |
| Allemand | de |
| Espagnol | es |
| Français | fr |
| Italien | it |
| Portugais (Brésil) | pt |
| Japonais | ja |
| Chinois - simplifié | zh |
| Tchèque | cs |
| Slovaque | sk |


## Configuration de la journalisation
* LOG_LEVEL - tous les messages de ce niveau de journalisation ou supérieur seront journalisés. Une des valeurs trace, debug, info, warn, error, fatal. La valeur par défaut est info
* FILE_LOG_LEVEL - niveau de journalisation pour l'écriture dans le fichier journal. Pour la journalisation dans un fichier, ceci est prioritaire sur LOG_LEVEL
* CONSOLE_LOG_LEVEL - niveau de journalisation pour l'écriture dans le fichier journal. Pour la journalisation dans la console, ceci est prioritaire sur LOG_LEVEL

## Configuration OAuth (version web uniquement)
* OAUTH_AUTH - point de terminaison d'authentification du protocole OAuth
* OAUTH_TOKEN - point de terminaison de jeton du protocole OAuth
* OAUTH_LOGOUT - URL de déconnexion du fournisseur OAuth. L'utilisateur sera redirigé vers cette URL lorsqu'il demandera à se déconnecter
* OAUTH_CLIENT_ID - identifiant client
* OAUTH_CLIENT_SECRET - secret client
* OAUTH_LOGIN_FIELD - nom du champ dans le payload qui contient le nom de login. Pour connaître les champs disponibles, vous pouvez inspecter le journal de dbgate, le payload envoyé par le fournisseur OAuth est journalisé dans la console. Ce nom de login est utilisé par ex. pour configurer les permissions. Il ne s'agit pas nécessairement du login saisi dans OAuth. S'il n'est pas spécifié, tous les utilisateurs du fournisseur OAuth auront le même nom de login.
* OAUTH_ALLOWED_LOGINS - noms de login séparés par des virgules, qui seront autorisés à se connecter. S'il n'est pas spécifié, tous les logins seront autorisés à utiliser l'application DbGate.
* OAUTH_SCOPE - scope envoyé aux points de terminaison OAuth authorize et token
* OAUTH_GROUP_FIELD - champ du payload OAuth qui désigne le groupe
* OAUTH_ALLOWED_GROUPS - noms de groupes autorisés séparés par des virgules

## Configuration Active Directory/LDAP (version web uniquement)
* AD_URL - URL du fournisseur LDAP (par ex. ldap://domain.com)
* AD_BASEDN - par ex. dc=domain,dc=com
* AD_USERNAME - nom d'utilisateur pour Active Directory
* AD_PASSWORD - mot de passe pour Active Directory
* AD_ALLOWED_LOGINS - noms de login séparés par des virgules, qui seront autorisés à se connecter. S'il n'est pas spécifié, tous les logins seront autorisés à utiliser l'application DbGate.

## Configuration du client Oracle  
* ORACLE_INSTANT_CLIENT - chemin vers le [client Oracle instant](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html)

## Configuration des connexions
Vous pouvez configurer la liste des connexions avec des variables d'environnement, les commandes "Add connection" et "Edit connection" ne seront alors plus disponibles.

* CONNECTIONS - liste des noms de connexions préconfigurées, séparés par des virgules. Dans les options suivantes, [connection id] est un ID de cette liste
* LABEL_[connection id] - libellé (nom affiché) de la connexion. 
* SERVER_[connection id] - serveur (nom d'hôte) de la connexion.
* USER_[connection id] - nom d'utilisateur pour la connexion à la base de données.
* PASSWORD_[connection id] - mot de passe pour la connexion à la base de données.
* PASSWORD_MODE_[connection id] - détermine si le mot de passe et le nom d'utilisateur sont stockés ou doivent être saisis par l'utilisateur. Une des valeurs suivantes :
  * askPassword - DbGate demande le mot de passe lors de la connexion
  * askUser - DbGate demande le nom d'utilisateur et le mot de passe
* PORT_[connection id] - port pour la connexion à la base de données.
* FILE_[connection id] - chemin du fichier de base de données (pour SQLite).
* URL_[connection id] - URL de la base de données (fonctionne pour MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle).
* SERVICE_NAME_[connection id] - nom du service Oracle.
* DATABASE_[connection id] - nom de la base de données par défaut.
* READONLY_[connection id] - se connecter en mode lecture seule
* ENGINE_[connection id] - moteur de la connexion (**obligatoire**, nom du moteur avec le plugin), l'un de :
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - définissez la valeur 1 ou true lorsqu'un tunnel SSH doit être utilisé
* SSH_HOST_[connection id] - nom d'hôte SSH
* SSH_PORT_[connection id] - numéro de port SSH
* SSH_MODE_[connection id] - une des valeurs suivantes
  * userPassword - authentification avec utilisateur et mot de passe
  * agent - authentification avec l'agent SSH
  * keyFile - authentification avec un fichier de clé
* SSH_LOGIN_[connection id] - login SSH
* SSH_PASSWORD_[connection id] - mot de passe SSH
* SSH_KEY_FILE_[connection id] - chemin complet vers le fichier de clé
* SSH_KEY_FILE_PASSWORD_[connection id] - phrase secrète du fichier de clé
* USE_SSL_[connection id] - définissez la valeur 1 ou true lorsque SSL doit être utilisé
* SSL_CA_FILE_[connection id] - chemin vers le fichier de certificat CA
* SSL_CERT_FILE_[connection id] - chemin vers le fichier de certificat
* SSL_CERT_FILE_PASSWORD_[connection id] - mot de passe du fichier de clé du certificat
* SSL_KEY_FILE_[connection id] - chemin vers le fichier de clé
* SSL_REJECT_UNAUTHORIZED_[connection id] - définissez la valeur 1 ou true pour rejeter les connexions non autorisées
* SSL_TRUST_CERTIFICATE_[connection id] - définissez la valeur 1 ou true pour activer l'option MSSQL trustServerCertificate
* SETTINGS_[settings key] - préconfigure une valeur de paramètre. La clé du paramètre peut être trouvée dans le code source, https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - chemin vers le fichier socket, si la connexion se fait via un socket
* AUTH_TYPE_[connection id] - type d'authentification
  * hostPort (par défaut)
  * socket - la valeur est définie implicitement lors de la configuration de SOCKET_PATH
  * tedious - authentification portable par défaut pour MS SQL, utilisant le pilote tedious
  * sspi - authentification intégrée Windows (Windows uniquement, MS SQL), utilisant le pilote MSSQL natif
  * sql - authentification SQL (Windows uniquement, MS SQL), utilisant le pilote MSSQL natif
* ALLOWED_DATABASES_[connection id] - noms de bases de données autorisés pour la connexion spécifiée, séparés par une barre verticale ("|")
* ALLOWED_DATABASES_REGEX_[connection id] - expression régulière pour les noms de bases de données autorisés pour la connexion spécifiée
* USE_SEPARATE_SCHEMAS_[connection id] - définissez la valeur 1 ou true pour charger les schémas séparément. Utilisez ceci si vous avez de grands schémas.
* LOCAL_DATA_CENTER_[connection id] - centre de données local (pour Apache Cassandra)
* CONNECTION_[connection id]_parameterName - définit un nom de paramètre spécifique au moteur

SettingsModal.svelte , cherchez la chaîne "name="/ Si vous devez définir "true", utilisez la valeur "1". Si vous avez besoin de "false", utilisez une chaîne vide ("0" ne fonctionnera pas)

## Configuration des rôles
Cette configuration ne peut être utilisée que dans l'édition Team Premium, lorsque la base de données de stockage est utilisée pour les paramètres. Les rôles issus des variables d'environnement sont importés dans la base de données de stockage au démarrage du conteneur docker.
Vous pouvez définir des rôles avec des permissions spécifiques et assigner des connexions au rôle. L'attribution des rôles aux utilisateurs se fait dans l'interface d'administration.
* `ROLE_[role_name]_PERMISSIONS` - liste de permissions séparées par des virgules pour le rôle donné. Voir la liste des permissions ci-dessous
* `ROLE_[role_name]_CONNECTIONS` - liste d'identifiants de connexion séparés par des virgules, assignés au rôle donné
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - identifiant de connexion pour la permission de base de données avec l'ID donné
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - liste de noms de bases de données séparés par une barre verticale ("|") pour la permission de base de données avec l'ID donné
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - expression régulière pour les noms de bases de données pour la permission de base de données avec l'ID donné
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - l'un de : deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - identifiant de connexion pour la permission de table avec l'ID donné
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - liste de noms de bases de données séparés par une barre verticale ("|") pour la permission de base de données avec l'ID donné
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - expression régulière pour les noms de bases de données pour la permission de base de données avec l'ID donné
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - liste de noms de schémas séparés par une barre verticale ("|") pour la permission de table avec l'ID donné
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - expression régulière pour les noms de schémas pour la permission de table avec l'ID donné
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - liste de noms de tables séparés par une barre verticale ("|") pour la permission de base de données avec l'ID donné
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - expression régulière pour les noms de tables pour la permission de base de données avec l'ID donné
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - l'un de : deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - l'un de : collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## Permissions
Par défaut, toutes les permissions sont disponibles. Si vous utilisez le préfixe \~, la permission est révoquée.

### Exemples
* ~*, widgets/database - toutes les permissions sont révoquées, seul le widget de base de données est visible
* ~widgets/*, widgets/database - toutes les permissions de widgets sont révoquées, seul le widget de base de données est visible
* ~connections/*, connections/con1 - toutes les connexions sauf con1 sont masquées et désactivées

### Liste des permissions
* settings/change - autorise la modification des paramètres
* plugins/install - autorise l'installation de plugins
* widgets/[widget_name] - si non accordée, le widget est masqué. Les widgets se trouvent dans la barre latérale gauche. Widgets disponibles :
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - lire les fichiers du dossier donné
* files/[folder]/write - écrire des fichiers dans le dossier donné
* apps/write - enregistrer dans le contenu des applications
* archive/write - enregistrer dans le contenu de l'archive
* connections/[connection_id] - autorise à voir et utiliser la connexion définie
* internal-storage = accès au stockage interne (Premium)
* admin/auth - Administration - onglet Authentification (Premium)
* admin/connections - Administration - onglet Connexions (Premium)
* admin/users - Administration - onglet Utilisateurs (Premium)
* admin/roles - Administration - onglet Rôles (Premium)
* dbops/sql-template/* - Modèles SQL (par ex. SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - Générateur SQL
* dbops/sql-dump/import - Importer un dump SQL
* dbops/sql-dump/export - Exporter un dump SQL
* dbops/query - Exécuter une requête SQL
* dbops/import - Importer des données
* dbops/export - Exporter des données
* dbops/charts - Voir les graphiques
* dbops/profiler - Profileur de base de données
* dbops/createdb - Créer une base de données
* dbops/dropdb - Supprimer une base de données
* dbops/model/view - Voir le modèle de base de données (diagrammes, JSON)
* dbops/model/edit - Modifier le modèle de base de données (créer/modifier des tables, vues, etc.)
* dbops/model/compare - Comparer les modèles de bases de données
* dbops/table/rename - Renommer une table
* dbops/table/truncate - Vider une table
* dbops/table/backup - Créer une sauvegarde de table
