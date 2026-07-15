---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: es
title: Front Matter de SQL
weight: 50
---

El front matter de SQL son metadatos en formato YAML al principio de un archivo SQL. Este concepto está inspirado en gohugo y Jekyll, que introdujeron el front matter para los archivos markdown. ([Front matter en Hugo](https://gohugo.io/content-management/front-matter/))

El front matter de SQL comienza inmediatamente en la marca de inicio del archivo SQL `-- >>>` y termina con una línea que contiene únicamente `-- <<<`. Cada línea del contenido YAML lleva el prefijo `-- `, de modo que el archivo completo sigue siendo SQL válido.

Estos metadatos se utilizan especialmente para los gráficos (guardar la configuración del gráfico) y para los atributos de la base de conocimiento pública (como el título y la descripción del script). Pero también hay algunos atributos que se pueden usar en cualquier script SQL de DbGate.

## Atributos genéricos
- autoExecute: `true` o `false`, indica si el script se ejecutará automáticamente al abrirlo
- splitterInitialValue: porcentaje (como 20%) o tamaño absoluto (como 220px) - se usa para definir el tamaño del área SQL superior. El resto se utilizará para el resultado de la consulta

## Atributos de la base de conocimiento pública
- title: título del script (por defecto - el nombre del archivo sin extensión)
- description: descripción del script (por defecto - vacía)
- icon: icono del script (de [Material design icons](https://pictogrammers.com/library/mdi/), en formato `mdi mdi-chart-pie`)

## Atributos de gráficos
- selected-chart: número (desde 1) del gráfico que se seleccionará automáticamente
- chart-N: definición del gráfico N
    - title: título del gráfico
    - pieRatioLimit - límite para el gráfico circular; si el valor está por debajo de este, se agrupará en "Otros" (por defecto: 0.05)
    - pieCountLimit - límite del número de porciones del gráfico circular; si el número de porciones supera este valor, se agruparán en "Otros" (por defecto 10)
    - dataLabelFormatter - formateador de la etiqueta de datos, uno de 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

Para obtener la lista completa y actualizada de campos, puedes usar la [definición de TypeScript](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts), consulta la interfaz `ChartDefinition`

## Ejemplo

```sql
-- >>>
-- selected-chart: 1
-- chart-1:
--   chartType: bar
--   xdef:
--     field: InvoiceDate
--     transformFunction: date:month
--   ydefs:
--     - field: Total
--       aggregateFunction: sum
-- <<<
SELECT
  `InvoiceId`,
  `CustomerId`,
  `InvoiceDate`,
  `BillingAddress`,
  `BillingCity`,
  `BillingState`,
  `BillingCountry`,
  `BillingPostalCode`,
  `Total`
FROM
  `Invoice`
```
