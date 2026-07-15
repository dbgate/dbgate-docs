---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: it
title: Progettazione query
weight: 20
---

La progettazione query *(Premium)* consente di creare query SQL visivamente, senza scrivere SQL a mano. Aggiungi le tabelle all'area di lavoro, scegli le colonne e definisci le condizioni: DbGate genera l'SQL per te.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## Creazione di una query

* **Aggiungere tabelle** - trascina le tabelle sull'area di progettazione; DbGate disegna automaticamente le relazioni in base alle chiavi esterne.
* **Scegliere le colonne** - scegli quali colonne compaiono nel risultato, definisci l'ordinamento e il raggruppamento.
* **Tipi di JOIN** - oltre ai join SQL standard (`INNER`, `LEFT`, `RIGHT`), puoi usare gli pseudo-join, il più utile dei quali è `WHERE NOT EXISTS`.
* **Filtri potenti** - filtra usando lo stesso motore del [browser dei dati](/it/dbgate/working-with-data/data-browser/), inclusi condizioni composte e filtri per insiemi di valori.

## Risultato

La progettazione produce una normale query SQL, quindi viene eseguita con le stesse prestazioni dell'SQL scritto a mano. Puoi passare in qualsiasi momento all'SQL generato e continuare a modificarlo nell'[editor SQL](sql-editor).

## Prospettive - la progettazione universale

Per viste nidificate e gerarchiche - e per unire dati tra tabelle SQL e collezioni MongoDB lato client - usa le [Prospettive](/it/dbgate/working-with-data/perspectives/), che non sono limitate da ciò che il database di origine è in grado di unire.
