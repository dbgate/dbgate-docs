---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: es
title: Gráficos
weight: 30
---

Con DbGate, puede usar gráficos para visualizar sus consultas SQL. Simplemente ejecute la consulta; si se detecta automáticamente un gráfico, aparecerá la pestaña "Chart 1". Si tiene más resultados de consulta, puede haber más gráficos.

Si no se detecta automáticamente ningún gráfico, pero desea crear alguno a partir de los resultados de su consulta, haga clic con el botón derecho en los datos del resultado de la consulta y elija "Open chart".

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## Configuración del gráfico
Use el botón {{< mdi "pencil" >}} Customize para abrir la configuración del gráfico. Puede configurar el origen de datos y el estilo del gráfico:
* Tipo de gráfico
  * Bar
  * Line
  * Timeline: es un caso especial del gráfico de líneas, con el tiempo en el eje X
  * Pie
  * Polar area
* Campo del eje X: datos en el eje X. Para valores de fecha/hora, están disponibles funciones de agrupación y de línea de tiempo
* Campo de agrupación: define más gráficos especificados por el valor de este campo
* Transformación del eje X: permite definir la agrupación para la línea de tiempo del eje X (p. ej. por año o por mes)
* Campo del eje Y N: puede tener más campos en el eje Y
  * Hay un campo especial disponible para cada conjunto de datos, "Count", que cuenta las filas
* Función de agregación: Sum, Minimum, Maximum, Average, First Value, Last Value

Cuando cambia cualquier opción en la configuración del gráfico, se guarda al principio del script SQL como front-matter.

## Edición manual de la definición del gráfico
Algunas opciones no están disponibles en el editor, pero pueden editarse en el código SQL. Consulte [SQL front matter](/es/dbgate/developer/sql-front-matter) para obtener más información
