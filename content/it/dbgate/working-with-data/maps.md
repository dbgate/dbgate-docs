---
sourceHash: a1e2c8e626b7d397e242c5a182c920ca58971109a164a8c90e909a521a92e5db
language: it
title: Mappe
weight: 40
---

DbGate supporta la visualizzazione di dati geografici nelle mappe. 

## Origini dati supportate per le mappe
- MySQL: tutte le colonne spaziali
- MSSQL: colonne GEOGRAPHY
- PostGIS: colonne GEOGRAPHY
- Tutte le origini dati: coordinate memorizzate in colonne di latitudine/longitudine

## Attivare la vista mappa
La vista mappa viene attivata dalla griglia dei dati. Per prima cosa, seleziona le celle con i dati geografici desiderati. Il modo più semplice è selezionare una cella GEOGRAPHY o GEOMETRY. Puoi anche selezionare più righe. Quindi, fai clic sul widget Dati cella. Dovresti vedere la mappa nel widget Dati cella.

![screenshot](/img/map1.png)

Se hai colonne di latitudine e longitudine memorizzate, seleziona tutti i dati che vuoi visualizzare nella mappa. Le colonne diverse da latitudine o longitudine verranno mostrate nei popup dei marcatori.

![screenshot](/img/map2.png)

In alternativa, puoi usare il menu contestuale "Apri selezione nella mappa" nella griglia dei dati sulle celle selezionate; verrà quindi aperta una nuova scheda con la mappa.

Nel menu contestuale della mappa è presente anche la possibilità di esportare la mappa in un file HTML autonomo, che può essere visualizzato ovunque, anche dove DbGate non è installato.
