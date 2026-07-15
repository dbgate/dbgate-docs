---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: es
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) es una herramienta gratuita, dentro del navegador, para trabajar con datos: sin instalación y sin necesidad de iniciar sesión. Está construida sobre el mismo motor de cuadrícula, filtrado y consultas que [DbGate Central](../dbgate-central/), por lo que navegar, filtrar y editar se siente igual en ambos.

## Aprender y enseñar SQL

DbGate Lite ejecuta **SQLite y DuckDB** completamente en tu navegador, usando WebAssembly:

* Escribe y ejecuta consultas SQL contra una base de datos de ejemplo en la conocida cuadrícula de DbGate.
* Visualiza cómo se relacionan las tablas mediante diagramas ER.
* Sin instalación, sin inicio de sesión: abre el sitio y empieza a trabajar.

## Trabajo ad-hoc con archivos de datos

Abre un archivo en DbGate Lite y trátalo como una base de datos:

* **Importa** archivos CSV, JSON y Excel y consúltalos o edítalos con SQL.
* Limpia y reestructura los datos, y luego **exporta** el resultado de vuelta a CSV, JSON o Excel.

## Compartir una base de datos o consulta con un enlace

Abrir DbGate Lite con ciertos parámetros de hash en la URL inicializa automáticamente una base de datos temporal:

* `initdbtype` - tipo de base de datos, `sqlite` o `duckdb`
* `initdbscript` - script SQL usado para crear y rellenar la base de datos temporal
* `initquery` (opcional) - consulta SQL abierta en una nueva pestaña de consulta

Cualquiera que abra el enlace obtiene la misma base de datos de ejemplo y la misma consulta con un solo clic: útil para tutoriales, informes de errores y enseñanza.

## Publicar una vista de solo lectura

Aparte de compartir un enlace editable, puedes **publicar** una vista de solo lectura de un archivo CSV/JSON o de un informe de BI mediante el botón Publish de la barra de herramientas. Esto abre una página independiente -solo los datos y un conmutador de tema claro/oscuro, sin barra lateral ni editor- que cualquiera con el enlace puede ver sin una cuenta.

## Elegir entre Lite, Central, Premium y Team Premium

DbGate Lite es ideal para aprender y para tareas puntuales. Para el trabajo profesional continuo, un producto dedicado encaja mejor:

* **DbGate Lite** - gratuito, dentro del navegador. Ideal para aprender SQL y para archivos de datos ad-hoc.
* **[DbGate Central](../dbgate-central/)** - producto alojado para trabajar con APIs: conéctate a endpoints en vivo de GraphQL, oData y Shopify, mantén conexiones e informes en un espacio de trabajo y compártelos con tu equipo.
* **[DbGate Premium](/es/dbgate/getting-started/installation/)** - una edición de [DbGate](/es/dbgate/): la aplicación de escritorio completa para trabajar con bases de datos, conéctate a servidores SQL y NoSQL con el conjunto completo de herramientas profesionales.
* **[DbGate Team Premium](/es/dbgate/getting-started/installation/docker-tp/)** - otra edición de [DbGate](/es/dbgate/), para equipos: una interfaz web compartida que se ejecuta on-premise, para que todo tu equipo trabaje con bases de datos desde el navegador en tu propia infraestructura.
