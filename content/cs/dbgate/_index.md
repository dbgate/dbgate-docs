---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: cs
title: DbGate
weight: 5
---

## Co je DbGate?

DbGate je správce databází, který umožňuje připojit se k podporovaným databázím a pracovat s nimi. Je to zároveň desktopová i webová aplikace. Je navržen tak, aby byl rychlý a snadno použitelný.

Produkty běžící v prohlížeči a hostované produkty (DbGate Lite, Central a Shopify App) najdete v [přehledu produktů](/cs/).

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## Podporované databáze

| Databáze | {{< center "Community" >}} | {{< center "Premium" >}} | Další funkce |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | Zálohování, obnova |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | Zálohování, obnova |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | Zálohování, obnova |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## Podporované platformy

- Desktop
  - Windows
  - MacOS (procesory ARM i Intel)
  - Linux
- Webová verze
  - Docker
  - NPM
  - Azure
  - AWS

## Edice

DbGate je k dispozici ve třech edicích:

| Edice | Distribuce | Významné funkce |
|---|---|---|
| Community | Desktopová aplikace nebo self-hosted web (Docker/NPM), zdarma | Připojení a procházení/editace standardních SQL a NoSQL databází, Redis GUI, až 5 připojení/souborů v DbGate Cloud |
| Premium | Desktopová aplikace (jeden uživatel) | Vše z edice Community a navíc [návrhář dotazů](sql-and-queries/query-designer), [grafy](working-with-data/charts), [editovatelné výsledky dotazů a pohledy](sql-and-queries/sql-editor), [pohledy master/detail](working-with-data/data-browser), [nástroje AI](working-with-data/ai-features) (chat s databází, vysvětlení chyby, asistent pro motivy vzhledu), porovnání a nasazení databázových modelů, pokročilý/dávkový export-import, [nasazení dat](working-with-data/advanced-data-tools/data-deployer), [API připojení](developer/api-connections) (GraphQL/oData/OpenAPI), další databázové enginy (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), neomezené úložiště DbGate Cloud |
| Team Premium | Desktopová aplikace + self-hosted web (Docker/NPM/AWS/Azure) | Vše z edice Premium a navíc webová aplikace, [administrátorské rozhraní](admin), uživatelé/role/oprávnění, externí poskytovatelé identit (OAuth/OIDC), nativní zálohování a obnova bez konfigurace |

## V této sekci

* [Začínáme](getting-started) - nainstalujte DbGate a připojte se ke své první databázi
* [Práce s daty](working-with-data) - procházení, editace, filtrování, grafy, mapy, export a archivace dat
* [SQL a dotazy](sql-and-queries) - SQL editor, vizuální návrhář dotazů a ER diagramy
* [Databázové operace](database-operations) - editace schématu, porovnání a nasazení modelů, zálohování a obnova
* [Přizpůsobení](customization) - nastavení vzhledu a běhových parametrů
* [Administrace](admin) - správa uživatelů, rolí a oprávnění (Team Premium)
* [Vývojář a automatizace](developer) - skripty, API připojení a pluginy
* [DbGate Cloud](dbgate-cloud) - online úložiště pro vaše připojení, SQL skripty a sdílené složky
