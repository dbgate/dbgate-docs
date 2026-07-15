---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: es
title: Consultar APIs de GraphQL
weight: 20
---

Apunta DbGate Central a cualquier API de GraphQL y descubrirá lo que está disponible para ti, sin necesidad de rebuscar en documentación aparte.

## Explorar el esquema

DbGate Central introspecciona el esquema de GraphQL en cuanto te conectas. Explora los tipos y campos disponibles en el árbol y luego abre una pestaña de consulta para empezar a trabajar.

## Ejecutar consultas

* Escribe consultas con el editor de GraphQL y ejecútalas contra la API en vivo.
* Proporciona las variables de la consulta junto con esta, ya sea en un formulario o como JSON sin formato.
* Los resultados se devuelven en la misma cuadrícula rápida, ordenable y filtrable que se usa en todo DbGate, de modo que una respuesta de GraphQL se siente como una tabla de base de datos.
* Los objetos y listas anidados se devuelven como JSON estructurado que puedes expandir e inspeccionar en el momento.

Las vistas consultadas se almacenan en caché por conexión, así que volver a abrirlas es instantáneo mientras sigues trabajando.

> Las conexiones GraphQL en DbGate Central son una implementación independiente, basada en el navegador, distinta de la [función GraphQL de escritorio](/es/dbgate/developer/api-connections/#graphql); consulta esa página si estás usando la aplicación de escritorio.

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
