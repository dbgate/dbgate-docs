---
title: DbGate Classic
weight: 5
---

## What is DbGate?

DbGate is database manager, allowing to connect and work with supported databases. It is both desktop app and web app. It's designed to by fast and easy to use.

DbGate Classic is the original DbGate application. For the browser-based and hosted products (DbGate Lite, Central and the Shopify App), see the [products overview](/).

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## Supported databases

| Database | {{< center "Community" >}} | {{< center "Premium" >}} | Extra Features |
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

## Supported platforms

- Desktop
  - Windows
  - MacOS (both ARM and Intel processors)
  - Linux
- Web version
  - Docker
  - NPM
  - Azure
  - AWS

## Editions

DbGate Classic comes in three editions:

| Edition | Distribution | Notable features |
|---|---|---|
| Community | Desktop app, or self-hosted web (Docker/NPM), free | Connect and browse/edit standard SQL and NoSQL databases, Redis GUI, up to 5 DbGate Cloud connections/files |
| Premium | Desktop app (single user) | Everything in Community, plus [query designer](sql-and-queries/query-designer), [charts](working-with-data/charts), [editable query results & views](sql-and-queries/sql-editor), [master/detail views](working-with-data/data-browser), [AI tools](working-with-data/ai-features) (DB chat, explain error, theme assistant), compare & deploy DB models, advanced/batch export-import, [data deployer](working-with-data/advanced-data-tools/data-deployer), [API connections](developer/api-connections) (GraphQL/oData/OpenAPI), extra database engines (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), unlimited DbGate Cloud storage |
| Team Premium | Desktop app + self-hosted web (Docker/NPM/AWS/Azure) | Everything in Premium, plus web application, [Administration UI](admin), users/roles/permissions, external identity providers (OAuth/OIDC), zero-config native backup & restore |

## In this section

* [Getting Started](getting-started) - install DbGate and connect to your first database
* [Working with Data](working-with-data) - browse, edit, filter, chart, map, export and archive data
* [SQL & Queries](sql-and-queries) - SQL editor, visual query designer and ER diagrams
* [Database Operations](database-operations) - edit schema, compare and deploy models, back up and restore
* [Customization](customization) - configure appearance and runtime settings
* [Administration](admin) - manage users, roles and permissions (Team Premium)
* [Developer & Automation](developer) - scripts, API connections and plugins
* [DbGate Cloud](dbgate-cloud) - online storage for your connections, SQL scripts and shared folders
