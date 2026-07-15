---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: fr
title: DbGate
weight: 5
---

## Qu'est-ce que DbGate ?

DbGate est un gestionnaire de bases de données qui permet de se connecter aux bases de données prises en charge et de travailler avec elles. C'est à la fois une application de bureau et une application web. Il est conçu pour être rapide et facile à utiliser.

Pour les produits hébergés et fonctionnant dans le navigateur (DbGate Lite, Central et l'application Shopify), consultez l'[aperçu des produits](/fr/).

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## Bases de données prises en charge

| Base de données | {{< center "Community" >}} | {{< center "Premium" >}} | Fonctionnalités supplémentaires |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | Sauvegarde, restauration |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | Sauvegarde, restauration |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | Sauvegarde, restauration |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## Plateformes prises en charge

- Bureau
  - Windows
  - MacOS (processeurs ARM et Intel)
  - Linux
- Version web
  - Docker
  - NPM
  - Azure
  - AWS

## Éditions

DbGate est disponible en trois éditions :

| Édition | Distribution | Fonctionnalités notables |
|---|---|---|
| Community | Application de bureau ou web auto-hébergé (Docker/NPM), gratuit | Connexion et exploration/édition des bases de données SQL et NoSQL standard, interface graphique Redis, jusqu'à 5 connexions/fichiers DbGate Cloud |
| Premium | Application de bureau (utilisateur unique) | Tout ce que contient Community, plus le [concepteur de requêtes](sql-and-queries/query-designer), les [graphiques](working-with-data/charts), les [résultats de requêtes et vues modifiables](sql-and-queries/sql-editor), les [vues maître/détail](working-with-data/data-browser), les [outils d'IA](working-with-data/ai-features) (chat avec la base de données, explication des erreurs, assistant de thème), la comparaison et le déploiement de modèles de bases de données, l'export-import avancé et par lots, le [déployeur de données](working-with-data/advanced-data-tools/data-deployer), les [connexions API](developer/api-connections) (GraphQL/oData/OpenAPI), des moteurs de bases de données supplémentaires (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), un stockage DbGate Cloud illimité |
| Team Premium | Application de bureau + web auto-hébergé (Docker/NPM/AWS/Azure) | Tout ce que contient Premium, plus l'application web, l'[interface d'administration](admin), les utilisateurs/rôles/permissions, les fournisseurs d'identité externes (OAuth/OIDC), la sauvegarde et la restauration natives sans configuration |

## Dans cette section

* [Prise en main](getting-started) - installez DbGate et connectez-vous à votre première base de données
* [Travailler avec les données](working-with-data) - explorez, modifiez, filtrez, représentez graphiquement, cartographiez, exportez et archivez vos données
* [SQL et requêtes](sql-and-queries) - éditeur SQL, concepteur visuel de requêtes et diagrammes ER
* [Opérations sur les bases de données](database-operations) - modifiez le schéma, comparez et déployez des modèles, sauvegardez et restaurez
* [Personnalisation](customization) - configurez l'apparence et les paramètres d'exécution
* [Administration](admin) - gérez les utilisateurs, les rôles et les permissions (Team Premium)
* [Développeur et automatisation](developer) - scripts, connexions API et plugins
* [DbGate Cloud](dbgate-cloud) - stockage en ligne pour vos connexions, scripts SQL et dossiers partagés
