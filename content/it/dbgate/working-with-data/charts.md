---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: it
title: Grafici
weight: 30
---

Con DbGate puoi utilizzare i grafici per la visualizzazione delle tue query SQL. È sufficiente eseguire la query: se il grafico viene rilevato automaticamente, comparirà la scheda "Chart 1". Se hai più risultati di query, possono esserci più grafici.

Se nessun grafico viene rilevato automaticamente, ma desideri creare un grafico dai risultati della tua query, fai clic con il tasto destro sui dati del risultato della query e scegli "Open chart".

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## Impostazioni del grafico
Usa il pulsante {{< mdi "pencil" >}} Customize per aprire le impostazioni del grafico. Puoi configurare l'origine dati e lo stile del grafico:
* Tipo di grafico
  * Bar
  * Line
  * Timeline - è un caso particolare del grafico a linee, con il tempo sull'asse X
  * Pie
  * Polar area
* Campo dell'asse X - dati sull'asse X. Per i valori di tipo data/ora sono disponibili funzioni di raggruppamento e timeline
* Campo di raggruppamento - definisce più grafici specificati dal valore di questo campo
* Trasformazione dell'asse X - consente di definire il raggruppamento per la timeline dell'asse X (ad es. per anno o per mese)
* Campo N dell'asse Y - puoi avere più campi sull'asse Y
  * Per ogni set di dati è disponibile un campo speciale, "Count", che conta le righe
* Funzione di aggregazione - Sum, Minimum, Maximum, Average, First Value, Last Value

Quando modifichi una qualsiasi opzione nelle impostazioni del grafico, essa viene salvata all'inizio dello script SQL come front-matter.

## Modifica manuale della definizione del grafico
Alcune opzioni non sono disponibili nell'editor, ma possono essere modificate nel codice SQL. Per maggiori informazioni leggi [SQL front matter](/it/dbgate/developer/sql-front-matter)
