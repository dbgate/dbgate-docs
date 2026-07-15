---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: cs
title: Proxy připojení
weight: 60
---

DbGate Central umí přistupovat k oData a GraphQL API, která běží v privátní síti, tak, že jejich provoz směruje přes malého odchozího agenta, kterého spustíte uvnitř této sítě. Připojení Shopify a OpenAPI nelze proxovat.

## Nastavení proxy

1. Otevřete záložku **Nastavení** a vytvořte **proxy** v sekci *Proxy připojení*. Zkopírujte vygenerovaný token.
2. Zaškrtněte oData/GraphQL připojení, která smí proxy obsluhovat. Každá změna znovu vygeneruje token, takže po změně výběru agenta restartujte.
3. Spusťte agenta uvnitř své privátní sítě:
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   Agent vytváří pouze odchozí spojení - není potřeba žádný příchozí přístup do vaší sítě.
4. Jakmile agent běží a je připojen, požadavky na proxovaná připojení jsou směrovány přes něj. Pokud proxy není připojena, DbGate Central se vrátí k přímému načítání.

Stejné směrování platí i pro [MCP server](../mcp-server): když nástroj MCP čte proxované připojení, požadavek jde přes stejnou proxy.
