---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: it
title: Server MCP per agenti AI
weight: 50
---

DbGate Central può esporre il tuo workspace ad assistenti AI come [Claude](https://claude.ai) sotto forma di connettore **MCP (Model Context Protocol)** remoto - in modo che un agente possa esplorare e interrogare le tue API esattamente come fai tu, con un accesso che rimane sotto il tuo controllo.

## Configurazione

1. Apri la scheda **Settings** e crea un **profilo MCP**. Copia il relativo **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), **Client ID** e **Client Secret**.
2. In claude.ai (o in un altro client compatibile con MCP), aggiungi un connettore personalizzato utilizzando quell'URL e le credenziali OAuth.
3. Nell'editor di ogni connessione, imposta il livello di **MCP access** - **No access**, **Read-only** oppure **Writable**. Il valore predefinito è nessun accesso, quindi non viene condiviso nulla finché non lo consenti.
4. L'assistente esegue l'handshake OAuth e tu fornisci il consenso, associando il connettore a quel profilo e a quel workspace.

Ogni workspace può avere più profili MCP, ciascuno con il proprio URL, le proprie credenziali e le autorizzazioni per singola connessione. L'autenticazione utilizza OAuth 2.1 con PKCE obbligatorio e i client secret sono cifrati a riposo.

## Cosa può fare l'agente

Disponibile per connessioni **oData**, **GraphQL** e **Shopify** (SQLite/DuckDB funzionano solo nel browser e non rientrano nell'ambito di MCP):

* **Elencare le connessioni** che il profilo è autorizzato a usare.
* **Elencare le entità** - tabelle, viste o entità di catalogo.
* **Ispezionare lo schema** - nomi e tipi delle colonne.
* **Interrogare le righe** - filtrare, paginare e selezionare i dati.
* **Aggiornare le righe** - solo per Shopify e solo quando concedi l'accesso Writable.

Poiché letture e scritture riutilizzano lo stesso motore della griglia e dello scheduler, un agente vede esattamente gli stessi dati e le stesse funzionalità che vedi tu - mai più dell'accesso che concedi.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
