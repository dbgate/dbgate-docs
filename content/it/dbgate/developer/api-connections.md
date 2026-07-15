---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: it
title: Connessioni API
weight: 10
---

DbGate supporta connessioni ad API REST, servizi GraphQL ed endpoint OData. Queste connessioni API utilizzano gli stessi schemi di interfaccia delle connessioni ai database, permettendoti di lavorare con API e database in un ambiente unificato.

Il supporto per le connessioni API è disponibile in DbGate Premium.

> Cerchi la navigazione delle API senza l'applicazione desktop? [DbGate Central](/it/dbgate-central/connecting-to-api-endpoints/) è un'implementazione separata e ospitata delle connessioni GraphQL/oData/Shopify, riprogettata da zero per il browser.

## GraphQL

Le connessioni GraphQL ti permettono di interagire con le API GraphQL. DbGate offre funzionalità di introspezione dello schema ed esecuzione delle query.

### Creazione di una connessione GraphQL

Per creare una connessione GraphQL, usa la finestra di dialogo Nuova connessione e seleziona GraphQL come tipo di connessione. Inserisci l'URL dell'endpoint GraphQL e configura l'autenticazione se necessario.

### Introspezione dello schema

DbGate rileva automaticamente lo schema GraphQL, inclusi i tipi disponibili, le query, le mutation e i relativi argomenti. Il browser dello schema mostra il sistema dei tipi e ti permette di esplorare la struttura dell'API.

### Editor delle query

L'editor delle query GraphQL ti permette di scrivere query e mutation. Puoi usare l'esploratore GraphQL per costruire le query selezionando campi e argomenti dallo schema.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Variabili

Le query GraphQL supportano le variabili. Definisci le variabili nel pannello delle variabili e referenziale nelle tue query usando la sintassi standard delle variabili GraphQL. Le variabili possono essere modificate tramite un modulo oppure come JSON grezzo.

### Visualizzatore delle risposte

I risultati delle query sono mostrati in un visualizzatore JSON formattato con una struttura ad albero espandibile. Se nella risposta vengono rilevati degli array, la vista tabellare viene visualizzata automaticamente. Se necessario, puoi tornare alla vista JSON grezza.

## OpenAPI (Swagger)

Le connessioni OpenAPI supportano le API REST che forniscono specifiche OpenAPI (versioni 2.0 e 3.0).

### Creazione di una connessione OpenAPI

Crea una nuova connessione e seleziona OpenAPI come tipo di connessione. Fornisci l'URL del file di specifica OpenAPI (in genere swagger.json o openapi.json). DbGate analizzerà la specifica e renderà disponibili tutti gli endpoint documentati.

### Browser della documentazione API

Il browser OpenAPI mostra tutti gli endpoint disponibili, organizzati per tag e percorsi. Per ogni endpoint puoi visualizzare:
- Metodo HTTP (GET, POST, PUT, DELETE, PATCH)
- Parametri (path, query, header, body)
- Schemi del corpo della richiesta
- Descrizioni della documentazione

### Esecuzione delle richieste

Seleziona un endpoint per aprire il costruttore di richieste. Compila i parametri richiesti, le intestazioni e il corpo della richiesta. Esegui la richiesta per inviarla al server API.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Ispezione delle risposte

Visualizza il codice di stato, le intestazioni e il corpo della risposta. Le risposte JSON vengono formattate e possono essere mostrate sia in vista ad albero che in vista tabellare. Le risposte non JSON vengono mostrate come testo.

## OData

Le connessioni OData supportano l'interrogazione dei servizi OData usando la sintassi di query standard di OData.

### Creazione di una connessione OData

Crea una nuova connessione con OData come tipo di connessione. Inserisci l'URL radice del servizio OData. DbGate recupererà il documento dei metadati del servizio.

### Esplorazione dei metadati

Il browser dei metadati mostra gli entity set, i tipi di entità, le proprietà e le relazioni disponibili definiti nei metadati del servizio.

### Esecuzione delle query

Le query OData supportano le opzioni di query standard di OData:
- `$filter` - filtra le entità in base ai valori delle proprietà
- `$select` - specifica quali proprietà restituire
- `$expand` - include le entità correlate
- `$orderby` - ordina i risultati
- `$top` e `$skip` - paginazione
- `$count` - include il conteggio dei risultati

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

I risultati sono mostrati in formato tabellare, in modo simile ai risultati delle query sui database.

## Autenticazione

Tutti i tipi di connessione API supportano diversi metodi di autenticazione:

- **API Key** - specifica il nome e il valore della chiave, inviata come intestazione o come parametro di query
- **Bearer Token** - token OAuth o JWT inviati nell'intestazione Authorization
- **Basic Authentication** - nome utente e password tramite HTTP Basic Auth
- **Nessuna autenticazione** - per le API pubbliche

Configura l'autenticazione nelle proprietà della connessione.

## Esportazione dei dati

I dati delle risposte API possono essere esportati in vari formati usando la funzionalità di esportazione standard di DbGate:
- JSON
- CSV
- Excel
- Istruzioni SQL INSERT
- XML

Usa l'opzione "Export" del menu contestuale standard nel browser dei dati tabellari.

## Lavorare con più API

Puoi creare connessioni a più API e database. Apri più schede di richiesta per lavorare contemporaneamente con endpoint diversi.

Lo stato delle schede viene mantenuto dopo la chiusura e la riapertura dell'applicazione; puoi riaprire una richiesta dalla cronologia delle schede chiuse.
