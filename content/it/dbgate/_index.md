---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: it
title: DbGate
weight: 5
---

## Che cos'è DbGate?

DbGate è un gestore di database che permette di connettersi e lavorare con i database supportati. È sia un'applicazione desktop che un'applicazione web. È progettato per essere veloce e facile da usare.

Per i prodotti basati su browser e ospitati (DbGate Lite, Central e l'app Shopify), consulta la [panoramica dei prodotti](/it/).

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## Database supportati

| Database | {{< center "Community" >}} | {{< center "Premium" >}} | Funzionalità aggiuntive |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | Backup, Ripristino |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | Backup, Ripristino |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | Backup, Ripristino |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## Piattaforme supportate

- Desktop
  - Windows
  - MacOS (sia processori ARM che Intel)
  - Linux
- Versione web
  - Docker
  - NPM
  - Azure
  - AWS

## Edizioni

DbGate è disponibile in tre edizioni:

| Edizione | Distribuzione | Funzionalità principali |
|---|---|---|
| Community | Applicazione desktop, oppure web self-hosted (Docker/NPM), gratuita | Connessione e navigazione/modifica di database SQL e NoSQL standard, GUI per Redis, fino a 5 connessioni/file DbGate Cloud |
| Premium | Applicazione desktop (utente singolo) | Tutto ciò che è incluso in Community, più [query designer](sql-and-queries/query-designer), [grafici](working-with-data/charts), [risultati e viste di query modificabili](sql-and-queries/sql-editor), [viste master/dettaglio](working-with-data/data-browser), [strumenti AI](working-with-data/ai-features) (chat con il DB, spiegazione degli errori, assistente per i temi), confronto e distribuzione di modelli di DB, esportazione-importazione avanzata/in batch, [data deployer](working-with-data/advanced-data-tools/data-deployer), [connessioni API](developer/api-connections) (GraphQL/oData/OpenAPI), motori di database aggiuntivi (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), spazio di archiviazione DbGate Cloud illimitato |
| Team Premium | Applicazione desktop + web self-hosted (Docker/NPM/AWS/Azure) | Tutto ciò che è incluso in Premium, più applicazione web, [interfaccia di amministrazione](admin), utenti/ruoli/permessi, provider di identità esterni (OAuth/OIDC), backup e ripristino nativi senza configurazione |

## In questa sezione

* [Per iniziare](getting-started) - installa DbGate e connettiti al tuo primo database
* [Lavorare con i dati](working-with-data) - naviga, modifica, filtra, crea grafici e mappe, esporta e archivia i dati
* [SQL e query](sql-and-queries) - editor SQL, query designer visuale e diagrammi ER
* [Operazioni sui database](database-operations) - modifica lo schema, confronta e distribuisci modelli, esegui backup e ripristini
* [Personalizzazione](customization) - configura l'aspetto e le impostazioni di runtime
* [Amministrazione](admin) - gestisci utenti, ruoli e permessi (Team Premium)
* [Sviluppatori e automazione](developer) - script, connessioni API e plugin
* [DbGate Cloud](dbgate-cloud) - archiviazione online per connessioni, script SQL e cartelle condivise
