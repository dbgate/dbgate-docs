---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: es
title: Explorador y editor de datos
weight: 5
---

El explorador de datos es la vista principal de DbGate para consultar y editar los datos de las tablas. Abre cualquier tabla, vista o colección para obtener una cuadrícula rápida y similar a Excel. Esta página cubre la navegación, la edición y el acceso a los datos relacionados; para las expresiones de filtro consulta [Filtrado de datos](data-filtering).

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## Explorar los datos

* **Navegación con el teclado** - muévete por la cuadrícula con las teclas de flecha, como en una hoja de cálculo.
* **Ordenar** - haz clic en el encabezado de una columna para ordenar por esa columna.
* **Filtrar** - filtra las filas mediante la fila de filtros situada encima de la cuadrícula; consulta [Filtrado de datos](data-filtering) para conocer la sintaxis completa de las expresiones.
* **Gestor de columnas** - busca columnas por nombre y oculta las que no necesites.
* **Copia avanzada** - copia las celdas seleccionadas como CSV, YAML, sentencias `INSERT` de SQL o inserciones de MongoDB.

## Editar los datos

La edición de datos funciona directamente en la cuadrícula:

* **Edición similar a Excel** - edita las celdas en el sitio; copia y pega rangos de filas, incluso entre tablas.
* **Cambios preparados** - tus modificaciones se recopilan como cambios pendientes. Revisa el script SQL de cambios generado antes de que llegue a la base de datos y, a continuación, guarda o revierte.
* **Insertar y eliminar filas** desde la cuadrícula o el menú contextual.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### Macros del editor de datos *(Premium)*

Aplica macros predefinidas a las celdas seleccionadas: por ejemplo, cambiar el uso de mayúsculas y minúsculas, eliminar los diacríticos o generar un UUID.

## Trabajar con datos relacionados

DbGate facilita el seguimiento de las relaciones entre tablas:

* **Sugerencias de relación** - consulta un valor de texto de la tabla referenciada junto a una clave externa numérica.
* **Expansión de columnas de clave externa** - expande una columna de clave externa para ver los datos referenciados en línea.
* **Abrir detalle** - salta a la fila referenciada por una clave externa.
* **Vistas maestro/detalle** *(Premium)* - explora las filas relacionadas en un diseño maestro/detalle enlazado.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## Vista de formulario

La vista de formulario muestra una única fila como una lista vertical "transpuesta", ideal para tablas con muchas columnas. Funciona como una vista de árbol, por lo que las columnas de clave externa se pueden expandir para explorar los datos relacionados.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## Agrupación *(Premium)*

Aplica una agrupación (`GROUP BY`) en la vista de cuadrícula para agregar filas directamente mientras exploras los datos.

## Páginas relacionadas

* [Filtrado de datos](data-filtering) - sintaxis de las expresiones de filtro
* [Exportación e importación](export-import) - mueve datos hacia dentro y fuera de las tablas
* [Perspectivas](perspectives) - vistas anidadas de solo lectura sobre datos relacionados complejos
* [Editor SQL](/es/dbgate/sql-and-queries/sql-editor/) - edita los resultados de las consultas de la misma manera *(Premium)*
