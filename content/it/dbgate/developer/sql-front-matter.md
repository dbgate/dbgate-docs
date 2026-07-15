---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: it
title: Front Matter SQL
weight: 50
---

Il front matter SQL è un insieme di metadati in formato YAML posti all'inizio di un file SQL. Questo concetto è ispirato a gohugo e Jekyll, che hanno introdotto il front matter per i file markdown. ([Front matter in Hugo](https://gohugo.io/content-management/front-matter/))

Il front matter SQL inizia immediatamente all'inizio del file SQL con il marcatore `-- >>>` e termina con una riga contenente solo `-- <<<`. Ogni riga del contenuto YAML è preceduta dal prefisso `-- `, in modo che l'intero file rimanga SQL valido.

Questi metadati sono usati soprattutto per i grafici (per salvare la configurazione del grafico) e per gli attributi della knowledge base pubblica (come titolo e descrizione dello script). Ma esistono anche alcuni attributi utilizzabili per qualsiasi script SQL in DbGate.

## Attributi generici
- autoExecute: `true` o `false`, indica se lo script verrà eseguito automaticamente all'apertura
- splitterInitialValue: percentuale (come 20%) o dimensione assoluta (come 220px) - da usare per definire la dimensione dell'area SQL superiore. Il resto sarà usato per il risultato della query

## Attributi della knowledge base pubblica
- title: titolo dello script (predefinito - nome del file senza estensione)
- description: descrizione dello script (predefinito - vuota)
- icon: icona dello script (dalle [icone Material design](https://pictogrammers.com/library/mdi/), nel formato `mdi mdi-chart-pie`)

## Attributi dei grafici
- selected-chart: numero (a partire da 1) del grafico da selezionare automaticamente
- chart-N: definizione dell'N-esimo grafico
    - title: titolo del grafico
    - pieRatioLimit - limite per il grafico a torta; se il valore è inferiore a questo, verrà raggruppato in "Altro" (predefinito: 0.05)
    - pieCountLimit - limite per il numero di fette del grafico a torta; se il numero di fette è superiore a questo, verranno raggruppate in "Altro" (predefinito 10)
    - dataLabelFormatter - formattatore dell'etichetta dati, uno tra 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

Per l'elenco completo e aggiornato dei campi, puoi consultare la [definizione TypeScript](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts), vedi l'interfaccia `ChartDefinition`

## Esempio

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
