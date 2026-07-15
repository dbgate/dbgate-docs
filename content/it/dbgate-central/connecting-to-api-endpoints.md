---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: it
title: Connessione agli endpoint API
weight: 10
---

DbGate Central si connette a tre famiglie di endpoint API, utilizzando per tutte la stessa finestra di dialogo New Connection.

## Tipi di endpoint supportati

* **GraphQL** - esegui l'introspezione dello schema, esplora i tipi ed esegui query su qualsiasi API GraphQL.
* **oData** - lavora con i servizi oData V4 come se fossero normali tabelle.
* **Shopify** - connettiti al tuo store tramite l'API Shopify Admin ed esplora prodotti, ordini, clienti, metafield e altro ancora.

## Creazione di una connessione

Apri la finestra di dialogo **New Connection**, scegli il tipo di connessione, inserisci l'URL del servizio e scegli il metodo di autenticazione:

* **None** - per endpoint aperti e pubblici.
* **Basic** - nome utente e password.
* **Bearer token** - incolla un token di accesso.
* **API key** - invia una chiave in un'intestazione o in un parametro di query.

Le connessioni vengono salvate nel tuo workspace, quindi saranno disponibili al successivo accesso, su qualsiasi dispositivo, senza nulla da configurare localmente.

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
