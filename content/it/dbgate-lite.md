---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: it
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) è uno strumento gratuito, direttamente nel browser, per lavorare con i dati - senza installazione e senza login. È basato sullo stesso motore di griglia, filtri e query di [DbGate Central](../dbgate-central/), quindi la navigazione, il filtraggio e la modifica funzionano allo stesso modo in entrambi.

## Imparare e insegnare SQL

DbGate Lite esegue **SQLite e DuckDB** interamente nel tuo browser, utilizzando WebAssembly:

* Scrivi ed esegui query SQL su un database di esempio nella familiare griglia di DbGate.
* Visualizza le relazioni tra le tabelle con i diagrammi ER.
* Nessuna installazione, nessun login - apri il sito e inizia a lavorare.

## Lavoro ad-hoc con file di dati

Apri un file in DbGate Lite e trattalo come un database:

* **Importa** file CSV, JSON ed Excel ed eseguine query o modificali con SQL.
* Pulisci e ristruttura i dati, poi **esporta** il risultato di nuovo in CSV, JSON o Excel.

## Condividere un database o una query con un link

Aprendo DbGate Lite con determinati parametri hash nell'URL viene automaticamente inizializzato un database temporaneo:

* `initdbtype` - tipo di database, `sqlite` o `duckdb`
* `initdbscript` - script SQL utilizzato per creare e popolare il database temporaneo
* `initquery` (opzionale) - query SQL aperta in una nuova scheda Query

Chiunque apra il link ottiene lo stesso database di esempio e la stessa query con un solo clic - utile per tutorial, segnalazioni di bug e insegnamento.

## Pubblicare una vista in sola lettura

Oltre alla condivisione di un link modificabile, puoi **pubblicare** una vista in sola lettura di un file CSV/JSON o di un report BI utilizzando il pulsante Publish nella barra degli strumenti. Questo apre una pagina autonoma - solo i dati e un selettore chiaro/scuro, senza barra laterale né editor - che chiunque abbia il link può visualizzare senza un account.

## Scegliere tra Lite, Central, Premium e Team Premium

DbGate Lite è ideale per l'apprendimento e per attività occasionali. Per un lavoro professionale e continuativo, un prodotto dedicato è più adatto:

* **DbGate Lite** - gratuito, nel browser. Ideale per imparare SQL e per file di dati ad-hoc.
* **[DbGate Central](../dbgate-central/)** - prodotto in hosting per lavorare con le API: connettiti a endpoint GraphQL, oData e Shopify in tempo reale, mantieni connessioni e report in un workspace e condividili con il tuo team.
* **[DbGate Premium](/it/dbgate/getting-started/installation/)** - un'edizione di [DbGate](/it/dbgate/): l'applicazione desktop completa per lavorare con i database, connettiti a server SQL e NoSQL con l'insieme completo di strumenti professionali.
* **[DbGate Team Premium](/it/dbgate/getting-started/installation/docker-tp/)** - un'altra edizione di [DbGate](/it/dbgate/), per i team: un'interfaccia web condivisa che gira on-premise, così tutto il tuo team lavora con i database dal browser sulla vostra infrastruttura.
