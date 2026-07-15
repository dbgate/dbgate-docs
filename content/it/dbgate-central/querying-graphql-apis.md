---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: it
title: Interrogare le API GraphQL
weight: 20
---

Punta DbGate Central su una qualsiasi API GraphQL e scoprirà automaticamente ciò che è disponibile - senza bisogno di consultare una documentazione separata.

## Esplorare lo schema

DbGate Central esegue l'introspezione dello schema GraphQL non appena ti connetti. Sfoglia i tipi e i campi disponibili nell'albero, quindi apri una scheda di query per iniziare a lavorare.

## Eseguire query

* Scrivi le query con l'editor GraphQL ed eseguile sull'API attiva.
* Fornisci le variabili della query insieme alla query stessa, tramite un modulo oppure come JSON grezzo.
* I risultati vengono restituiti nella stessa griglia veloce, ordinabile e filtrabile utilizzata ovunque in DbGate, così una risposta GraphQL sembra una tabella di database.
* Gli oggetti e gli elenchi annidati vengono restituiti come JSON strutturato che puoi espandere e ispezionare direttamente.

Le viste interrogate vengono memorizzate nella cache per ogni connessione, così la loro riapertura è istantanea mentre continui a lavorare.

> Le connessioni GraphQL in DbGate Central sono un'implementazione separata, basata su browser, rispetto alla [funzionalità GraphQL desktop](/it/dbgate/developer/api-connections/#graphql) - consulta quella pagina se stai utilizzando invece l'applicazione desktop.

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
