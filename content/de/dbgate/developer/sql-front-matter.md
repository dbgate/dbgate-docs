---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: de
title: SQL Front Matter
weight: 50
---

SQL Front Matter sind Metadaten im YAML-Format am Anfang einer SQL-Datei. Dieses Konzept ist von gohugo und Jekyll inspiriert, die Front Matter für Markdown-Dateien eingeführt haben. ([Front Matter in Hugo](https://gohugo.io/content-management/front-matter/))

SQL Front Matter beginnt unmittelbar am Dateianfang mit der Markierung `-- >>>` und endet mit einer Zeile, die nur `-- <<<` enthält. Jeder Zeile des YAML-Inhalts wird das Präfix `-- ` vorangestellt, damit die gesamte Datei gültiges SQL bleibt.

Diese Metadaten werden insbesondere für Diagramme (Speichern der Diagrammkonfiguration) und für Attribute der öffentlichen Wissensdatenbank (wie Skripttitel und Beschreibung) verwendet. Es gibt aber auch einige Attribute, die für jedes SQL-Skript in DbGate nutzbar sind.

## Allgemeine Attribute
- autoExecute: `true` oder `false`, ob das Skript beim Öffnen automatisch ausgeführt wird
- splitterInitialValue: Prozentwert (z. B. 20%) oder absolute Größe (z. B. 220px) – zur Festlegung der Größe des oberen SQL-Bereichs. Der Rest wird für das Abfrageergebnis verwendet

## Attribute der öffentlichen Wissensdatenbank
- title: Skripttitel (Standard – Dateiname ohne Erweiterung)
- description: Skriptbeschreibung (Standard – leer)
- icon: Skriptsymbol (aus [Material Design Icons](https://pictogrammers.com/library/mdi/), im Format `mdi mdi-chart-pie`)

## Diagramm-Attribute
- selected-chart: Nummer (ab 1) des Diagramms, das automatisch ausgewählt werden soll
- chart-N: Definition des N-ten Diagramms
    - title: Diagrammtitel
    - pieRatioLimit – Grenzwert für Kreisdiagramme; liegt der Wert darunter, wird er unter „Sonstige“ gruppiert (Standard: 0.05)
    - pieCountLimit – Grenzwert für die Anzahl der Segmente eines Kreisdiagramms; liegt die Anzahl der Segmente darüber, werden sie unter „Sonstige“ gruppiert (Standard: 10)
    - dataLabelFormatter – Formatierer für die Datenbeschriftung, eines von 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

Für die vollständige, aktuelle Feldliste können Sie die [TypeScript-Definition](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts) verwenden, siehe Interface `ChartDefinition`

## Beispiel

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
