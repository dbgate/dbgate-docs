---
sourceHash: a1e2c8e626b7d397e242c5a182c920ca58971109a164a8c90e909a521a92e5db
language: es
title: Mapas
weight: 40
---

DbGate permite mostrar datos geográficos en mapas. 

## Fuentes de mapas compatibles
- MySQL: todas las columnas espaciales
- MSSQL: columnas GEOGRAPHY
- PostGIS: columnas GEOGRAPHY
- Todas las fuentes de datos: coordenadas almacenadas en columnas de latitud/longitud

## Abrir la vista de mapa
La vista de mapa se abre desde la cuadrícula de datos. Primero, seleccione las celdas con los datos geográficos deseados. La forma más sencilla es seleccionar una celda GEOGRAPHY o GEOMETRY. También puede seleccionar varias filas. A continuación, haga clic en el widget Datos de celda. Debería ver el mapa en el widget de datos de celda.

![screenshot](/img/map1.png)

Si tiene almacenadas columnas de latitud y longitud, seleccione todos los datos que quiera tener en el mapa. Las columnas distintas de latitud o longitud se mostrarán en las ventanas emergentes de los marcadores.

![screenshot](/img/map2.png)

Como alternativa, puede usar el menú contextual "Abrir selección en el mapa" en la cuadrícula de datos sobre las celdas seleccionadas; entonces se abrirá una nueva pestaña con el mapa.

En el menú contextual del mapa también existe la posibilidad de exportar el mapa a un archivo HTML independiente, que se puede mostrar en cualquier lugar donde DbGate no esté instalado.