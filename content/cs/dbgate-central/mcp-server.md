---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: cs
title: MCP Server pro AI agenty
weight: 50
---

DbGate Central může zpřístupnit váš workspace AI asistentům, jako je [Claude](https://claude.ai), jako vzdálený **MCP (Model Context Protocol)** konektor - agent tak může prozkoumávat a dotazovat vaše API stejným způsobem jako vy, s přístupem, který máte plně pod kontrolou.

## Nastavení

1. Otevřete záložku **Settings** a vytvořte **MCP profil**. Zkopírujte jeho **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), **Client ID** a **Client Secret**.
2. V claude.ai (nebo jiném klientovi kompatibilním s MCP) přidejte vlastní konektor pomocí této URL a OAuth přihlašovacích údajů.
3. V editoru každého připojení nastavte úroveň **MCP access** - **No access**, **Read-only** nebo **Writable**. Výchozí hodnotou je žádný přístup, takže nic není sdíleno, dokud to nepovolíte.
4. Asistent provede OAuth handshake a vy udělíte souhlas, čímž se konektor naváže na daný profil a workspace.

Každý workspace může mít více MCP profilů, každý s vlastní URL, přihlašovacími údaji a oprávněními pro jednotlivá připojení. Autentizace používá OAuth 2.1 s povinným PKCE a client secrets jsou uloženy zašifrované.

## Co může agent dělat

Dostupné pro připojení **oData**, **GraphQL** a **Shopify** (SQLite/DuckDB fungují pouze v prohlížeči a jsou mimo rozsah MCP):

* **List connections** - vypsat připojení, která smí profil používat.
* **List entities** - tabulky, pohledy nebo katalogové entity.
* **Inspect the schema** - názvy a typy sloupců.
* **Query rows** - filtrování, stránkování a výběr dat.
* **Update rows** - pouze pro Shopify a pouze pokud udělíte přístup Writable.

Protože čtení i zápisy využívají stejný engine jako grid a plánovač, agent vidí přesně stejná data a možnosti jako vy - nikdy více, než jaký přístup mu udělíte.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
