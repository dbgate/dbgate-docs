---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: sk
title: DbGate
weight: 5
---

## Čo je DbGate?

DbGate je správca databáz, ktorý umožňuje pripojiť sa k podporovaným databázam a pracovať s nimi. Je to zároveň desktopová aj webová aplikácia. Je navrhnutý tak, aby bol rýchly a jednoducho použiteľný.

Informácie o produktoch založených na prehliadači a hosťovaných produktoch (DbGate Lite, Central a Shopify App) nájdete v [prehľade produktov](/).

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## Podporované databázy

| Databáza | {{< center "Community" >}} | {{< center "Premium" >}} | Ďalšie funkcie |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | Zálohovanie, Obnova |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | Zálohovanie, Obnova |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | Zálohovanie, Obnova |
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
  - MacOS (procesory ARM aj Intel)
  - Linux
- Webová verzia
  - Docker
  - NPM
  - Azure
  - AWS

## Edície

DbGate je dostupný v troch edíciách:

| Edícia | Distribúcia | Významné funkcie |
|---|---|---|
| Community | Desktopová aplikácia alebo self-hosted web (Docker/NPM), zadarmo | Pripojenie a prehliadanie/úprava štandardných SQL a NoSQL databáz, Redis GUI, až 5 pripojení/súborov v DbGate Cloud |
| Premium | Desktopová aplikácia (jeden používateľ) | Všetko z edície Community a navyše [návrhár dotazov](sql-and-queries/query-designer), [grafy](working-with-data/charts), [editovateľné výsledky dotazov a pohľady](sql-and-queries/sql-editor), [pohľady master/detail](working-with-data/data-browser), [AI nástroje](working-with-data/ai-features) (DB chat, vysvetlenie chyby, asistent tém), porovnanie a nasadenie DB modelov, pokročilý/dávkový export-import, [data deployer](working-with-data/advanced-data-tools/data-deployer), [API pripojenia](developer/api-connections) (GraphQL/oData/OpenAPI), ďalšie databázové enginy (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), neobmedzené úložisko DbGate Cloud |
| Team Premium | Desktopová aplikácia + self-hosted web (Docker/NPM/AWS/Azure) | Všetko z edície Premium a navyše webová aplikácia, [administračné rozhranie](admin), používatelia/roly/oprávnenia, externí poskytovatelia identity (OAuth/OIDC), natívne zálohovanie a obnova bez konfigurácie |

## V tejto sekcii

* [Začíname](getting-started) - nainštalujte DbGate a pripojte sa k svojej prvej databáze
* [Práca s dátami](working-with-data) - prehliadanie, úprava, filtrovanie, grafy, mapy, export a archivácia dát
* [SQL a dotazy](sql-and-queries) - SQL editor, vizuálny návrhár dotazov a ER diagramy
* [Databázové operácie](database-operations) - úprava schémy, porovnanie a nasadenie modelov, zálohovanie a obnova
* [Prispôsobenie](customization) - konfigurácia vzhľadu a nastavení behu
* [Administrácia](admin) - správa používateľov, rolí a oprávnení (Team Premium)
* [Vývojár a automatizácia](developer) - skripty, API pripojenia a pluginy
* [DbGate Cloud](dbgate-cloud) - online úložisko pre vaše pripojenia, SQL skripty a zdieľané priečinky
