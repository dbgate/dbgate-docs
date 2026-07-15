---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: it
title: Prospettive
weight: 50
---

Una prospettiva è una vista di sola lettura di dati annidati complessi. Assomiglia ai report, ma le prospettive vengono create semplicemente aggiungendo dati alla vista. Puoi usare il designer di prospettive, che consente di unire i dati seguendo relazioni diverse dalle chiavi esterne.

Le prospettive possono unire facilmente i dati tra loro e mostrare i gruppi.

<!-- ![screenshot](/screenshots/perspective1.png) -->

## Creare una prospettiva
Le prospettive possono essere create da tabelle e viste SQL (le collection di MongoDB non sono ancora supportate, ma il supporto è pianificato).
Usa il menu contestuale della tabella/vista, "Open perspective".

![screenshot](/img/perspective-create.png)

DbGate apre una prospettiva semplice, con una sola colonna visualizzata. Questa colonna viene scelta da un algoritmo euristico, in modo da essere la migliore rappresentazione dell'intera riga.
## Personalizzare la prospettiva
Puoi definire quali colonne sono disponibili nella vista. Inoltre puoi aggiungere alla vista i dati referenziati. Usa il pulsante di espansione per esplorare l'albero dei riferimenti.

## Filtrare i dati
Usa il menu contestuale nella tabella o nell'elenco delle colonne sul lato sinistro, "Add to filter". Puoi usare le stesse espressioni di filtro usate in altre parti di DbGate. Oppure puoi usare il comando del menu contestuale "Filter this value" su una cella della tabella.

## Filtrare le righe padre
Immagina la seguente prospettiva. Abbiamo una relazione master/dettaglio, Genre, con i track correlati. Vogliamo filtrare per Track (ho provato a cercare il testo "mix").

![screenshot](/img/parentrows1.png)

Come puoi vedere, ci sono molte righe Genre senza alcun track che corrisponda ai criteri di ricerca. Se vuoi filtrare anche le righe Genre, usa il comando "Filter parent rows" nel menu contestuale dell'intestazione della tabella. Puoi anche usare il pulsante interruttore nella riga del filtro.

![screenshot](/img/parentrows2.png)

## Definire join personalizzati
Le prospettive funzionano molto bene con le chiavi esterne. Ma puoi usare questa funzionalità anche quando hai un DB senza chiavi esterne. È possibile definire un join personalizzato con qualsiasi condizione. Puoi persino definire un join personalizzato verso un altro database (che potrebbe trovarsi su un server DB diverso, anche con un motore di database sottostante differente).

![screenshot](/img/customjoin.png)

Puoi anche trascinare e rilasciare le colonne per creare una relazione di join.

![screenshot](/img/customjoin2.png)
