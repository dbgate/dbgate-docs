---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: es
title: Diseñador de consultas
weight: 20
---

El diseñador de consultas *(Premium)* le permite crear consultas SQL visualmente, sin escribir SQL a mano. Añada tablas al lienzo, elija columnas y defina condiciones: DbGate genera el SQL por usted.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## Creación de una consulta

* **Añadir tablas** - arrastre las tablas al lienzo de diseño; DbGate dibuja automáticamente las relaciones a partir de las claves foráneas.
* **Elegir columnas** - elija qué columnas aparecen en el resultado, defina la ordenación y la agrupación.
* **Tipos de JOIN** - además de las uniones SQL estándar (`INNER`, `LEFT`, `RIGHT`), puede usar pseudo-uniones, siendo la más útil `WHERE NOT EXISTS`.
* **Filtros potentes** - filtre usando el mismo motor que el [explorador de datos](/es/dbgate/working-with-data/data-browser/), incluidas las condiciones compuestas y el filtrado por un conjunto de valores.

## Resultado

El diseñador produce una consulta SQL normal, por lo que se ejecuta con el mismo rendimiento que el SQL escrito a mano. Puede cambiar al SQL generado en cualquier momento y seguir editándolo en el [editor SQL](sql-editor).

## Perspectivas: el diseñador universal

Para vistas anidadas y jerárquicas, y para unir datos entre tablas SQL y colecciones de MongoDB en el lado del cliente, use [Perspectivas](/es/dbgate/working-with-data/perspectives/), que no están limitadas por lo que la base de datos de origen puede unir.
