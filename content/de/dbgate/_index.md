---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: de
title: DbGate
weight: 5
---

## Was ist DbGate?

DbGate ist ein Datenbankmanager, mit dem Sie sich mit unterstützten Datenbanken verbinden und arbeiten können. Er ist sowohl eine Desktop-App als auch eine Web-App. Er ist auf Geschwindigkeit und einfache Bedienung ausgelegt.

Informationen zu den browserbasierten und gehosteten Produkten (DbGate Lite, Central und die Shopify-App) finden Sie in der [Produktübersicht](/de/).

![DbGate Screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## Unterstützte Datenbanken

| Datenbank | {{< center "Community" >}} | {{< center "Premium" >}} | Zusätzliche Funktionen |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | Backup, Restore |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | Backup, Restore |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | Backup, Restore |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## Unterstützte Plattformen

- Desktop
  - Windows
  - MacOS (sowohl ARM- als auch Intel-Prozessoren)
  - Linux
- Web-Version
  - Docker
  - NPM
  - Azure
  - AWS

## Editionen

DbGate ist in drei Editionen erhältlich:

| Edition | Vertrieb | Wichtige Funktionen |
|---|---|---|
| Community | Desktop-App oder selbst gehostetes Web (Docker/NPM), kostenlos | Verbinden und Durchsuchen/Bearbeiten von gängigen SQL- und NoSQL-Datenbanken, Redis-GUI, bis zu 5 DbGate Cloud-Verbindungen/-Dateien |
| Premium | Desktop-App (Einzelbenutzer) | Alles aus Community, zusätzlich [Query-Designer](sql-and-queries/query-designer), [Diagramme](working-with-data/charts), [bearbeitbare Abfrageergebnisse und Views](sql-and-queries/sql-editor), [Master/Detail-Ansichten](working-with-data/data-browser), [KI-Werkzeuge](working-with-data/ai-features) (DB-Chat, Fehler erklären, Theme-Assistent), Vergleichen und Bereitstellen von DB-Modellen, erweiterter/Batch-Export-Import, [Data-Deployer](working-with-data/advanced-data-tools/data-deployer), [API-Verbindungen](developer/api-connections) (GraphQL/oData/OpenAPI), zusätzliche Datenbank-Engines (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), unbegrenzter DbGate Cloud-Speicher |
| Team Premium | Desktop-App + selbst gehostetes Web (Docker/NPM/AWS/Azure) | Alles aus Premium, zusätzlich Webanwendung, [Administrationsoberfläche](admin), Benutzer/Rollen/Berechtigungen, externe Identitätsanbieter (OAuth/OIDC), Backup und Restore ohne Konfigurationsaufwand |

## In diesem Abschnitt

* [Erste Schritte](getting-started) - DbGate installieren und mit Ihrer ersten Datenbank verbinden
* [Arbeiten mit Daten](working-with-data) - Daten durchsuchen, bearbeiten, filtern, in Diagrammen und Karten darstellen, exportieren und archivieren
* [SQL und Abfragen](sql-and-queries) - SQL-Editor, visueller Query-Designer und ER-Diagramme
* [Datenbankoperationen](database-operations) - Schema bearbeiten, Modelle vergleichen und bereitstellen, Backup und Restore
* [Anpassung](customization) - Erscheinungsbild und Laufzeiteinstellungen konfigurieren
* [Administration](admin) - Benutzer, Rollen und Berechtigungen verwalten (Team Premium)
* [Entwickler und Automatisierung](developer) - Skripte, API-Verbindungen und Plugins
* [DbGate Cloud](dbgate-cloud) - Online-Speicher für Ihre Verbindungen, SQL-Skripte und freigegebenen Ordner
