---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: pt
title: DbGate
weight: 5
---

## O que é o DbGate?

O DbGate é um gerenciador de bancos de dados que permite conectar-se e trabalhar com os bancos de dados suportados. É ao mesmo tempo um aplicativo desktop e um aplicativo web. Foi projetado para ser rápido e fácil de usar.

Para os produtos baseados em navegador e hospedados (DbGate Lite, Central e o Shopify App), consulte a [visão geral dos produtos](/pt/).

![DbGate screenshot](https://media.dbgate.io/img/common-data-browser-light.png)

## Bancos de dados suportados

| Banco de dados | {{< center "Community" >}} | {{< center "Premium" >}} | Recursos extras |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | Backup, restauração |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | Backup, restauração |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | Backup, restauração |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## Plataformas suportadas

- Desktop
  - Windows
  - MacOS (processadores ARM e Intel)
  - Linux
- Versão web
  - Docker
  - NPM
  - Azure
  - AWS

## Edições

O DbGate está disponível em três edições:

| Edição | Distribuição | Principais recursos |
|---|---|---|
| Community | Aplicativo desktop ou web auto-hospedado (Docker/NPM), gratuito | Conectar-se e navegar/editar bancos de dados SQL e NoSQL padrão, GUI para Redis, até 5 conexões/arquivos no DbGate Cloud |
| Premium | Aplicativo desktop (usuário único) | Tudo da edição Community, além de [designer de consultas](sql-and-queries/query-designer), [gráficos](working-with-data/charts), [resultados de consultas e views editáveis](sql-and-queries/sql-editor), [visualizações mestre/detalhe](working-with-data/data-browser), [ferramentas de IA](working-with-data/ai-features) (chat com o BD, explicação de erros, assistente de temas), comparação e implantação de modelos de BD, exportação-importação avançada/em lote, [data deployer](working-with-data/advanced-data-tools/data-deployer), [conexões de API](developer/api-connections) (GraphQL/oData/OpenAPI), mecanismos de banco de dados adicionais (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), armazenamento ilimitado no DbGate Cloud |
| Team Premium | Aplicativo desktop + web auto-hospedado (Docker/NPM/AWS/Azure) | Tudo da edição Premium, além de aplicativo web, [interface de administração](admin), usuários/funções/permissões, provedores de identidade externos (OAuth/OIDC), backup e restauração nativos sem configuração |

## Nesta seção

* [Primeiros passos](getting-started) - instale o DbGate e conecte-se ao seu primeiro banco de dados
* [Trabalhando com dados](working-with-data) - navegue, edite, filtre, crie gráficos e mapas, exporte e arquive dados
* [SQL e consultas](sql-and-queries) - editor SQL, designer visual de consultas e diagramas ER
* [Operações de banco de dados](database-operations) - edite o esquema, compare e implante modelos, faça backup e restauração
* [Personalização](customization) - configure a aparência e as opções de execução
* [Administração](admin) - gerencie usuários, funções e permissões (Team Premium)
* [Desenvolvedor e automação](developer) - scripts, conexões de API e plugins
* [DbGate Cloud](dbgate-cloud) - armazenamento online para suas conexões, scripts SQL e pastas compartilhadas
