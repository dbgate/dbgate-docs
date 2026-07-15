---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: es
title: Perspectivas
weight: 50
---

Una perspectiva es una vista de solo lectura de datos anidados complejos. Se parece a los informes, pero las perspectivas se crean simplemente añadiendo datos a la vista. Puedes usar el diseñador de perspectivas, que te permite unir datos siguiendo otras relaciones distintas de las claves foráneas.

Las perspectivas pueden unir datos fácilmente y mostrar grupos.

<!-- ![screenshot](/screenshots/perspective1.png) -->

## Crear una perspectiva
Las perspectivas se pueden crear a partir de tablas y vistas SQL (las colecciones de MongoDB aún no son compatibles, pero está previsto añadir esta compatibilidad).
Usa el menú contextual de la tabla/vista, "Open perspective".

![screenshot](/img/perspective-create.png)

DbGate abre una perspectiva simple, con solo una columna mostrada. Esta columna se elige mediante un algoritmo heurístico, para que sea la mejor representación de toda la fila.
## Personalizar la perspectiva
Puedes definir qué columnas están disponibles en la vista. También puedes añadir datos referenciados a la vista. Usa el botón de expandir para explorar el árbol de referencias.

## Filtrar datos
Usa el menú contextual en la tabla o en la lista de columnas del lado izquierdo, "Add to filter". Puedes usar las mismas expresiones de filtro que en otros lugares de DbGate. O puedes usar el comando del menú contextual "Filter this value" sobre una celda de la tabla.

## Filtrar filas padre
Supongamos la siguiente perspectiva. Tenemos una relación maestro/detalle, Genre, con las pistas relacionadas. Queremos filtrar por Track (he intentado buscar el texto "mix").

![screenshot](/img/parentrows1.png)

Como puedes ver, hay muchas filas de Genre sin ninguna pista que coincida con los criterios de búsqueda. Si quieres filtrar también las filas de Genre, usa el comando "Filter parent rows" en el menú contextual del encabezado de la tabla. También puedes usar el botón de conmutación en la fila de filtro.

![screenshot](/img/parentrows2.png)

## Definir uniones personalizadas
Las perspectivas funcionan muy bien con claves foráneas. Pero también cuando tienes una base de datos sin claves foráneas, puedes usar esta función. Es posible definir una unión personalizada con cualquier condición. Incluso puedes definir una unión personalizada con otra base de datos (que podría estar en un servidor de base de datos diferente, incluso con un motor de base de datos subyacente distinto).

![screenshot](/img/customjoin.png)

También puedes arrastrar &amp; soltar columnas para crear una relación de unión.

![screenshot](/img/customjoin2.png)
