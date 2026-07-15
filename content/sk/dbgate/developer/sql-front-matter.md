---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: sk
title: SQL Front Matter
weight: 50
---

SQL front matter sú metadáta vo formáte YAML na začiatku SQL súboru. Tento koncept je inšpirovaný nástrojmi gohugo a Jekyll, ktoré zaviedli front matter pre markdown súbory. ([Front matter v Hugo](https://gohugo.io/content-management/front-matter/))

SQL front matter začína hneď na začiatku SQL súboru značkou `-- >>>` a končí riadkom obsahujúcim iba `-- <<<`. Každý riadok YAML obsahu má predponu `-- `, takže celý súbor zostáva platným SQL.

Tieto metadáta sa používajú najmä pre grafy (ukladanie konfigurácie grafu) a pre atribúty verejnej knowledge base (napríklad názov a popis skriptu). Existujú však aj niektoré atribúty použiteľné pre každý SQL skript v DbGate.

## Všeobecné atribúty
- autoExecute: `true` alebo `false`, či sa skript automaticky vykoná pri otvorení
- splitterInitialValue: percento (napríklad 20%) alebo absolútna veľkosť (napríklad 220px) - použite na definovanie veľkosti hornej SQL oblasti. Zvyšok sa použije pre výsledok dotazu

## Atribúty verejnej knowledge base
- title: názov skriptu (predvolene - názov súboru bez prípony)
- description: popis skriptu (predvolene - prázdny)
- icon: ikona skriptu (z [Material design icons](https://pictogrammers.com/library/mdi/), vo formáte `mdi mdi-chart-pie`)

## Atribúty grafov
- selected-chart: číslo (od 1) grafu, ktorý sa má automaticky vybrať
- chart-N: definícia N-tého grafu
    - title: názov grafu
    - pieRatioLimit - limit pre koláčový graf, ak je hodnota nižšia ako tento limit, bude zoskupená do "Ostatné" (predvolene: 0.05)
    - pieCountLimit - limit pre počet výsekov koláčového grafu, ak je počet výsekov vyšší ako tento limit, budú zoskupené do "Ostatné" (predvolene 10)
    - dataLabelFormatter - formátovač popisku dát, jeden z 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

Kompletný aktuálny zoznam polí nájdete v [TypeScript definícii](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts), pozrite si rozhranie `ChartDefinition`

## Príklad

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