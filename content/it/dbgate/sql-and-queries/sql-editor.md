---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: it
title: Editor SQL
weight: 10
---

L'editor SQL è il punto in cui scrivi ed esegui script SQL sulla tua connessione. Aprilo dal pulsante {{< mdi "flash" >}} "Nuova query" nella barra degli strumenti, oppure dal menu contestuale di una connessione o di un database.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## Esecuzione di SQL

* **Esegui script** - esegue l'intero script con il pulsante {{< mdi "play" >}} Esegui (o F5).
* **Esegui istruzione corrente** - esegue solo l'istruzione sotto il cursore.
* **Esegui selezione** - se selezioni una parte dello script, viene eseguito solo il testo selezionato.
* I risultati compaiono nella griglia dei risultati sotto l'editor. Più set di risultati vengono mostrati in schede separate.
* Messaggi, conteggi di righe ed errori vengono mostrati nella scheda **Messaggi**.

## Strumenti di supporto alla scrittura

* **Formattatore di codice SQL** - riformatta lo script corrente per ottenere indentazione e maiuscole/minuscole coerenti.
* **Completamento del codice** - suggerimenti di tabelle, colonne e parole chiave basati sullo schema del database connesso.
* **Assistente join** - l'utilità "Aggiungi join SQL" genera una clausola `LEFT`/`INNER`/`RIGHT JOIN` a partire dalle chiavi esterne, così non devi digitare a mano le condizioni di join.

## Lavorare con i risultati

La griglia dei risultati usa lo stesso motore del [data browser](/it/dbgate/working-with-data/data-browser/), quindi puoi [filtrare e ordinare](/it/dbgate/working-with-data/data-filtering/), copiare celle in vari formati ed [esportare](/it/dbgate/working-with-data/export-import/) il risultato.

### Modifica dei risultati delle query e delle viste *(Premium)*

I risultati delle query sono modificabili quando DbGate riesce a mappare il risultato su una singola tabella o su una vista aggiornabile. Modifica le celle direttamente nella griglia dei risultati, controlla lo script di modifica generato e salvalo nel database - lo stesso flusso di lavoro con modifiche in sospeso presente nel [data browser](/it/dbgate/working-with-data/data-browser/). È supportata anche la modifica delle viste.

> I risultati delle query modificabili e le viste modificabili sono stati introdotti in DbGate 7.2.

## Controllo delle transazioni

Puoi controllare le transazioni dall'editor - eseguire all'interno di una transazione esplicita ed effettuare il commit o il rollback delle modifiche, cosa utile quando si testano script che modificano i dati.

## Altri editor

* **Editor JavaScript per Mongo** - per le connessioni MongoDB, scrivi ed esegui script Mongo usando la sintassi NodeJS.
* **Redis** - esplora l'albero delle chiavi Redis, genera uno script dalle chiavi selezionate ed esegui script Redis.
