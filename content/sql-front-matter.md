---
title: SQL Front Matter
weight: 205
---

SQL front matter is metadata in YAML format at the beginning of SQL file. This concept is inspired by gohugo and Jekyll, which introduced front matter for markdown files. ([Front matter in Hugo](https://gohugo.io/content-management/front-matter/))

SQL front matter starts immediately at the SQL file start file mark `-- >>>` and ends with line containing only `-- <<<`. Every line of YAML content is prefixed with `-- `  prefix, so that the whole file remains valid SQL.

This metadata is used especially for charts (saving chart configuration) and for public knowledge base attributes (like script title and description). But there are also some attributes usable fior every SQL script in DbGate.

## Generic attributes
- autoExecute: `true` or `false`, whether the script will be automatically executed when opening
- splitterInitialValue: percentage (like 20%) or absolute size (like 220px) - use for defining size of upper SQL are. The rest will be used for query result

## Public knowledge base attributes
- title: script title (default - file name without extension)
- description: script description (default - empty)
- icon: script icon (from [Material design icons](https://pictogrammers.com/library/mdi/), in format `mdi mdi-chart-pie`)

## Chart attributes
- selected-chart: number (from 1) of chart to autoselect
- chart-N: definition of Nth chart
    - title: chart title
    - pieRatioLimit - limit for pie chart, if the value is below this, it will be grouped into "Other" (default: 0.05)
    - pieCountLimit - limit for number of pie chart slices, if the number of slices is above this, it will be grouped into "Other" (default 10)
    - dataLabelFormatter - formatter of data label, on of 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

For complete up-to-date field list, you could use [TypeScript definition](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts), see `ChartDefinition` interface

## Example

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