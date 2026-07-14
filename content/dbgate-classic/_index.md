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
| Community | Desktop app, or self-hosted web (Docker/NPM), free | Connect and browse/edit standard SQL and NoSQL databases |
| Premium | Desktop app, or self-hosted web (Docker/NPM/AWS/Azure) | Adds API connections (GraphQL/oData/OpenAPI), backup & restore, DB model deploy/compare, extra database engines (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB) |
| Team Premium | Self-hosted web (Docker/NPM/AWS/Azure) | Multi-user: storage database for settings, Administration UI, users/roles/permissions |

## In this section

* [Getting Started](getting-started) - install DbGate and connect to your first database
* [Working with Data](working-with-data) - filter, chart, map, export and archive data
* [Database Operations](database-operations) - deploy database models, back up and restore
* [Customization](customization) - configure appearance and runtime settings
* [Administration](admin) - manage users, roles and permissions (Team Premium)
* [Developer & Automation](developer) - scripts, API connections and plugins
* [DbGate Cloud](dbgate-cloud) - online storage for your connections, SQL scripts and shared folders
