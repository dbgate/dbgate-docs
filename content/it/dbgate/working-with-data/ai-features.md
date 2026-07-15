---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: it
title: Funzionalità AI
weight: 55
---

DbGate include diverse funzionalità basate sull'AI *(Premium e Team Premium)*. Sono disponibili per tutti gli utenti Premium senza chiavi API né configurazione: DbGate utilizza il proprio gateway AI, che inoltra le richieste al provider LLM.

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## Chat con il database

La chat con il database è un chatbot AI che comprende sia lo schema del database sia i suoi dati.

* **Conversazione naturale** - poni domande in qualsiasi linguaggio naturale e ottieni risposte o SQL pronto da eseguire.
* **Consapevole del contesto** - il modello conosce il tuo schema e (con l'autorizzazione) i dati reali, quindi suggerisce join, filtri e aggregazioni corretti.
* **Iterativa** - affina con comandi come "aggiungi un filtro sulla data" o "raggruppa per cliente" e la query si aggiorna immediatamente.
* **Grafici** - richiedi un grafico a barre, a torta o a linee costruito a partire dai risultati.
* **Modalità consulente** - può analizzare stored procedure e viste, così puoi chiedere cose come "Spiega la procedura X" o "Quali tabelle sono interessate dalla procedura Y". DbGate mostra quali oggetti sono stati analizzati.

### Esecuzione di SQL - la sicurezza prima di tutto

La chat con il database può eseguire SQL per rispondere alle domande. Sei tu a scegliere come:

* **Chiedi prima di eseguire SQL (predefinito)** - DbGate chiede conferma prima di eseguire ogni query.
* **Esegui SQL automaticamente** - le query diverse da `SELECT` richiedono comunque una conferma.
* **Non eseguire mai, suggerisci solo SQL** - la chat mostra solo le query; nessun dato del tuo database viene inviato all'LLM.

Se una query suggerita fallisce, DbGate invia l'errore al modello, che di solito corregge la query automaticamente.

## Assistente SQL AI

Usa la chat come assistente SQL - "Scrivi una query SQL per i 10 migliori clienti per vendite" - e apri il risultato in una scheda dell'[editor SQL](/it/dbgate/sql-and-queries/sql-editor/).

## Spiegazione degli errori SQL

Fai clic su **Explain** accanto a un messaggio di errore per ottenere una spiegazione AI di cosa è andato storto e di come risolverlo.

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## Assistente AI per i temi

L'AI può anche generare temi di colore personalizzati - vedi [Temi personalizzati](/it/dbgate/customization/custom-themes/).

## Disattivazione delle funzionalità AI

Le funzionalità AI possono essere disattivate completamente (ad esempio in ambienti con restrizioni) tramite le impostazioni di DbGate.
