---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: fr
title: Front matter SQL
weight: 50
---

Le front matter SQL est constitué de métadonnées au format YAML placées au début d'un fichier SQL. Ce concept s'inspire de gohugo et Jekyll, qui ont introduit le front matter pour les fichiers markdown. ([Front matter dans Hugo](https://gohugo.io/content-management/front-matter/))

Le front matter SQL commence immédiatement au début du fichier SQL par la marque `-- >>>` et se termine par une ligne contenant uniquement `-- <<<`. Chaque ligne du contenu YAML est précédée du préfixe `-- `, de sorte que l'ensemble du fichier reste du SQL valide.

Ces métadonnées sont utilisées en particulier pour les graphiques (enregistrement de la configuration du graphique) et pour les attributs de la base de connaissances publique (comme le titre et la description du script). Mais il existe aussi certains attributs utilisables pour tous les scripts SQL dans DbGate.

## Attributs génériques
- autoExecute : `true` ou `false`, indique si le script sera exécuté automatiquement à l'ouverture
- splitterInitialValue : pourcentage (comme 20%) ou taille absolue (comme 220px) - à utiliser pour définir la taille de la zone SQL supérieure. Le reste sera utilisé pour le résultat de la requête

## Attributs de la base de connaissances publique
- title : titre du script (par défaut - nom du fichier sans extension)
- description : description du script (par défaut - vide)
- icon : icône du script (issue des [icônes Material design](https://pictogrammers.com/library/mdi/), au format `mdi mdi-chart-pie`)

## Attributs de graphique
- selected-chart : numéro (à partir de 1) du graphique à sélectionner automatiquement
- chart-N : définition du N-ième graphique
    - title : titre du graphique
    - pieRatioLimit - limite pour le graphique en secteurs, si la valeur est inférieure à celle-ci, elle sera regroupée dans « Autre » (par défaut : 0.05)
    - pieCountLimit - limite du nombre de secteurs du graphique, si le nombre de secteurs est supérieur à celle-ci, ils seront regroupés dans « Autre » (par défaut 10)
    - dataLabelFormatter - formateur de l'étiquette de données, l'un de 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

Pour la liste complète et à jour des champs, vous pouvez utiliser la [définition TypeScript](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts), voir l'interface `ChartDefinition`

## Exemple

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
