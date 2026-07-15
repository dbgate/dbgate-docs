---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: cs
title: SQL Front Matter
weight: 50
---

SQL front matter jsou metadata ve formátu YAML na začátku SQL souboru. Tento koncept je inspirován nástroji gohugo a Jekyll, které zavedly front matter pro markdown soubory. ([Front matter v Hugo](https://gohugo.io/content-management/front-matter/))

SQL front matter začíná hned na začátku SQL souboru značkou `-- >>>` a končí řádkem obsahujícím pouze `-- <<<`. Každý řádek YAML obsahu je uvozen předponou `-- `, takže celý soubor zůstává platným SQL.

Tato metadata se používají zejména pro grafy (uložení konfigurace grafu) a pro atributy veřejné znalostní báze (jako je název a popis skriptu). Existují ale i některé atributy použitelné pro každý SQL skript v DbGate.

## Obecné atributy
- autoExecute: `true` nebo `false`, zda bude skript automaticky spuštěn při otevření
- splitterInitialValue: procenta (například 20%) nebo absolutní velikost (například 220px) - použijte pro definování velikosti horní SQL oblasti. Zbytek bude použit pro výsledek dotazu

## Atributy veřejné znalostní báze
- title: název skriptu (výchozí - název souboru bez přípony)
- description: popis skriptu (výchozí - prázdný)
- icon: ikona skriptu (z [Material design icons](https://pictogrammers.com/library/mdi/), ve formátu `mdi mdi-chart-pie`)

## Atributy grafů
- selected-chart: číslo (od 1) grafu, který se má automaticky vybrat
- chart-N: definice N-tého grafu
    - title: název grafu
    - pieRatioLimit - limit pro koláčový graf, pokud je hodnota pod touto hranicí, bude seskupena do kategorie "Ostatní" (výchozí: 0.05)
    - pieCountLimit - limit počtu výsečí koláčového grafu, pokud je počet výsečí vyšší, budou seskupeny do kategorie "Ostatní" (výchozí: 10)
    - dataLabelFormatter - formátovač popisku dat, jeden z 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

Kompletní aktuální seznam polí najdete v [TypeScript definici](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts), viz rozhraní `ChartDefinition`

## Příklad

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
