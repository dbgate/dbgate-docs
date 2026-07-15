---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: de
title: Verbindungs-Proxys
weight: 60
---

DbGate Central kann oData- und GraphQL-APIs erreichen, die sich in einem privaten Netzwerk befinden, indem deren Datenverkehr über einen kleinen ausgehenden Agenten geleitet wird, den Sie innerhalb dieses Netzwerks betreiben. Shopify- und OpenAPI-Verbindungen können nicht über einen Proxy geleitet werden.

## Einen Proxy einrichten

1. Öffnen Sie den Tab **Einstellungen** und erstellen Sie unter *Verbindungs-Proxys* einen **Proxy**. Kopieren Sie das generierte Token.
2. Markieren Sie die oData/GraphQL-Verbindungen, die der Proxy bedienen darf. Jede Änderung erzeugt das Token neu, starten Sie den Agenten daher nach einer Änderung der Auswahl neu.
3. Führen Sie den Agenten in Ihrem privaten Netzwerk aus:
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   Der Agent stellt ausschließlich ausgehende Verbindungen her - ein eingehender Zugriff auf Ihr Netzwerk ist nicht erforderlich.
4. Sobald der Agent läuft und verbunden ist, werden Anfragen an die per Proxy geleiteten Verbindungen über ihn geroutet. Ist der Proxy nicht verbunden, greift DbGate Central auf den direkten Abruf zurück.

Dasselbe Routing gilt auch für den [MCP-Server](../mcp-server): Wenn ein MCP-Tool eine per Proxy geleitete Verbindung liest, läuft die Anfrage über denselben Proxy.
