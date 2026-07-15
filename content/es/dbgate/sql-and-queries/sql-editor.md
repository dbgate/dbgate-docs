---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: es
title: Editor SQL
weight: 10
---

El editor SQL es donde escribes y ejecutas scripts SQL contra tu conexión. Ábrelo desde el botón {{< mdi "flash" >}} "Nueva consulta" de la barra de herramientas, o desde el menú contextual de una conexión o base de datos.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## Ejecutar SQL

* **Ejecutar script** - ejecuta el script completo con el botón {{< mdi "play" >}} Ejecutar (o F5).
* **Ejecutar la sentencia actual** - ejecuta solo la sentencia sobre la que está el cursor.
* **Ejecutar la selección** - si seleccionas una parte del script, solo se ejecuta el texto seleccionado.
* Los resultados aparecen en la cuadrícula de resultados debajo del editor. Los conjuntos de resultados múltiples se muestran en pestañas separadas.
* Los mensajes, el número de filas y los errores se muestran en la pestaña **Mensajes**.

## Ayudas de edición

* **Formateador de código SQL** - reformatea el script actual para conseguir una indentación y un uso de mayúsculas coherentes.
* **Autocompletado de código** - sugerencias de tablas, columnas y palabras clave basadas en el esquema de la base de datos conectada.
* **Asistente de joins** - la utilidad "Añadir join SQL" genera una cláusula `LEFT`/`INNER`/`RIGHT JOIN` a partir de las claves foráneas, de modo que no tienes que escribir las condiciones de join a mano.

## Trabajar con los resultados

La cuadrícula de resultados utiliza el mismo motor que el [explorador de datos](/es/dbgate/working-with-data/data-browser/), por lo que puedes [filtrar y ordenar](/es/dbgate/working-with-data/data-filtering/), copiar celdas en varios formatos y [exportar](/es/dbgate/working-with-data/export-import/) el resultado.

### Editar resultados de consultas y vistas *(Premium)*

Los resultados de las consultas son editables cuando DbGate puede mapear el resultado de vuelta a una única tabla o a una vista actualizable. Edita las celdas directamente en la cuadrícula de resultados, revisa el script de cambios generado y guárdalo en la base de datos - el mismo flujo de trabajo de cambios preparados que en el [explorador de datos](/es/dbgate/working-with-data/data-browser/). También se admite la edición de vistas.

> Los resultados de consultas editables y las vistas editables se introdujeron en DbGate 7.2.

## Control de transacciones

Puedes controlar las transacciones desde el editor - ejecutar dentro de una transacción explícita y confirmar o deshacer los cambios, lo que resulta útil al probar scripts que modifican datos.

## Otros editores

* **Editor JavaScript de Mongo** - para conexiones MongoDB, escribe y ejecuta scripts de Mongo usando la sintaxis de NodeJS.
* **Redis** - explora el árbol de claves de Redis, genera un script a partir de las claves seleccionadas y ejecuta scripts de Redis.
