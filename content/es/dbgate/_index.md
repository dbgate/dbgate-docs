---
sourceHash: a0952a91721d3de723fc485de4acd652657b6a1396c45ea5fd5d40b2b70172d4
language: es
title: DbGate
weight: 5
---

## ¿Qué es DbGate?

DbGate es un gestor de bases de datos que permite conectarse y trabajar con las bases de datos compatibles. Es a la vez una aplicación de escritorio y una aplicación web. Está diseñado para ser rápido y fácil de usar.

Para los productos basados en navegador y alojados (DbGate Lite, Central y la Shopify App), consulta la [descripción general de los productos](/es/).

![Captura de pantalla de DbGate](https://media.dbgate.io/img/common-data-browser-light.png)

## Bases de datos compatibles

| Base de datos | {{< center "Community" >}} | {{< center "Premium" >}} | Funciones adicionales |
|---|---|---|---|
| [MySQL](https://www.mysql.com/) | {{< check >}}  | {{< check >}} | Copia de seguridad, Restauración |
| [PostgreSQL](https://postgresql.org/) | {{< check >}}  | {{< check >}} | Copia de seguridad, Restauración |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | {{< check >}}  | {{< check >}} | |
| [Oracle](https://www.oracle.com/database/) | {{< check >}}  | {{< check >}} | |
| [SQLite](https://sqlite.org/) | {{< check >}}  | {{< check >}} | |
| [MongoDB](https://www.mongodb.com/) | {{< check >}}  | {{< check >}} | |
| [Cassandra](http://cassandra.apache.org/) | {{< check >}}  | {{< check >}} | |
| [ClickHouse](https://clickhouse.tech/) | {{< check >}}  | {{< check >}} | |
| [Redis](https://redis.io/) | {{< check >}}  | {{< check >}} | |
| [MariaDB](https://mariadb.org/) | {{< check >}}  | {{< check >}} | Copia de seguridad, Restauración |
| [CockroachDB](https://www.cockroachlabs.com/) | {{< check >}}  | {{< check >}} | |
| [DuckDB](https://duckdb.org/) | {{< check >}}  | {{< check >}} | |
| [Firebird](https://www.firebirdsql.org//) | {{< check >}}  | {{< check >}} | |
| [libSQL](https://libsql.org/) |  | {{< check >}} | |
| [CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db) |  | {{< check >}} | |
| [Amazon Redshift](https://aws.amazon.com/redshift/) |   | {{< check >}} | |
| [Firestore](https://firebase.google.com/products/firestore) |  | {{< check >}} | |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) |  | {{< check >}} | |

## Plataformas compatibles

- Escritorio
  - Windows
  - MacOS (procesadores ARM e Intel)
  - Linux
- Versión web
  - Docker
  - NPM
  - Azure
  - AWS

## Ediciones

DbGate está disponible en tres ediciones:

| Edición | Distribución | Funciones destacadas |
|---|---|---|
| Community | Aplicación de escritorio o web autoalojada (Docker/NPM), gratuita | Conectar y explorar/editar bases de datos SQL y NoSQL estándar, GUI de Redis, hasta 5 conexiones/archivos de DbGate Cloud |
| Premium | Aplicación de escritorio (usuario único) | Todo lo de Community, más [diseñador de consultas](sql-and-queries/query-designer), [gráficos](working-with-data/charts), [resultados y vistas de consulta editables](sql-and-queries/sql-editor), [vistas maestro/detalle](working-with-data/data-browser), [herramientas de IA](working-with-data/ai-features) (chat con la BD, explicar error, asistente de temas), comparar y desplegar modelos de BD, exportación-importación avanzada/por lotes, [desplegador de datos](working-with-data/advanced-data-tools/data-deployer), [conexiones API](developer/api-connections) (GraphQL/oData/OpenAPI), motores de bases de datos adicionales (libSQL, CosmosDB, Amazon Redshift, Firestore, Amazon DynamoDB), almacenamiento ilimitado en DbGate Cloud |
| Team Premium | Aplicación de escritorio + web autoalojada (Docker/NPM/AWS/Azure) | Todo lo de Premium, más aplicación web, [interfaz de administración](admin), usuarios/roles/permisos, proveedores de identidad externos (OAuth/OIDC), copia de seguridad y restauración nativas sin configuración |

## En esta sección

* [Primeros pasos](getting-started) - instala DbGate y conéctate a tu primera base de datos
* [Trabajar con datos](working-with-data) - explora, edita, filtra, representa en gráficos y mapas, exporta y archiva datos
* [SQL y consultas](sql-and-queries) - editor SQL, diseñador visual de consultas y diagramas ER
* [Operaciones con bases de datos](database-operations) - edita el esquema, compara y despliega modelos, haz copias de seguridad y restaura
* [Personalización](customization) - configura la apariencia y los ajustes de ejecución
* [Administración](admin) - gestiona usuarios, roles y permisos (Team Premium)
* [Desarrollador y automatización](developer) - scripts, conexiones API y plugins
* [DbGate Cloud](dbgate-cloud) - almacenamiento en línea para tus conexiones, scripts SQL y carpetas compartidas
