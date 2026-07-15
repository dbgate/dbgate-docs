---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: it
title: Proxy di connessione
weight: 60
---

DbGate Central può raggiungere API oData e GraphQL che si trovano su una rete privata instradando il loro traffico attraverso un piccolo agente in uscita che esegui all'interno di quella rete. Le connessioni Shopify e OpenAPI non possono essere instradate tramite proxy.

## Configurare un proxy

1. Apri la scheda **Impostazioni** e crea un **proxy** in *Proxy di connessione*. Copia il token generato.
2. Seleziona le connessioni oData/GraphQL che il proxy può servire. Ogni modifica rigenera il token, quindi riavvia l'agente dopo aver cambiato la selezione.
3. Esegui l'agente all'interno della tua rete privata:
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   L'agente effettua solo connessioni in uscita - non è richiesto alcun accesso in entrata alla tua rete.
4. Una volta che l'agente è in esecuzione e connesso, le richieste alle connessioni instradate tramite proxy passano attraverso di esso. Se il proxy non è connesso, DbGate Central ripiega sul recupero diretto.

Lo stesso instradamento si applica anche al [server MCP](../mcp-server): quando uno strumento MCP legge una connessione instradata tramite proxy, la richiesta passa attraverso lo stesso proxy.
