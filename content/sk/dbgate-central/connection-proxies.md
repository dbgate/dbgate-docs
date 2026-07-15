---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: sk
title: Proxy pripojení
weight: 60
---

DbGate Central dokáže pristupovať k oData a GraphQL API, ktoré sa nachádzajú v privátnej sieti, tak že ich prevádzku smeruje cez malého odchádzajúceho agenta, ktorého spustíte vnútri tejto siete. Pripojenia Shopify a OpenAPI nie je možné smerovať cez proxy.

## Nastavenie proxy

1. Otvorte kartu **Settings** a vytvorte **proxy** v sekcii *Connection proxies*. Skopírujte vygenerovaný token.
2. Zaškrtnite oData/GraphQL pripojenia, ktoré môže proxy obsluhovať. Každá zmena vygeneruje nový token, preto po zmene výberu reštartujte agenta.
3. Spustite agenta vnútri svojej privátnej siete:
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   Agent vytvára iba odchádzajúce spojenia - nie je potrebný žiadny prichádzajúci prístup do vašej siete.
4. Keď agent beží a je pripojený, požiadavky na proxované pripojenia sú smerované cez neho. Ak proxy nie je pripojená, DbGate Central sa vráti k priamemu načítavaniu.

To isté smerovanie platí aj pre [MCP server](../mcp-server): keď MCP nástroj číta proxované pripojenie, požiadavka ide cez tú istú proxy.
