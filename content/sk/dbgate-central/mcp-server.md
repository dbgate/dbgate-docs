---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: sk
title: MCP server pre AI agentov
weight: 50
---

DbGate Central môže sprístupniť váš pracovný priestor AI asistentom, ako je [Claude](https://claude.ai), ako vzdialený konektor **MCP (Model Context Protocol)** - takže agent môže preskúmavať a dopytovať vaše API rovnakým spôsobom ako vy, s prístupom, ktorý máte pod kontrolou.

## Nastavenie

1. Otvorte kartu **Settings** a vytvorte **MCP profil**. Skopírujte jeho **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), **Client ID** a **Client Secret**.
2. V claude.ai (alebo inom klientovi kompatibilnom s MCP) pridajte vlastný konektor s použitím tejto URL a OAuth prihlasovacích údajov.
3. V editore každého pripojenia nastavte jeho úroveň **MCP access** - **No access**, **Read-only** alebo **Writable**. Predvolene je bez prístupu, takže sa nič nezdieľa, kým to nepovolíte.
4. Asistent vykoná OAuth handshake a vy udelíte súhlas, čím sa konektor naviaže na daný profil a pracovný priestor.

Každý pracovný priestor môže mať viacero MCP profilov, každý s vlastnou URL, prihlasovacími údajmi a oprávneniami pre jednotlivé pripojenia. Autentifikácia používa OAuth 2.1 s povinným PKCE a client secrets sú šifrované v úložisku.

## Čo môže agent robiť

Dostupné pre pripojenia **oData**, **GraphQL** a **Shopify** (SQLite/DuckDB fungujú iba v prehliadači a sú mimo rozsahu MCP):

* **Zobraziť zoznam pripojení**, ktoré profil smie používať.
* **Zobraziť zoznam entít** - tabuliek, pohľadov alebo katalógových entít.
* **Preskúmať schému** - názvy a typy stĺpcov.
* **Dopytovať riadky** - filtrovať, stránkovať a vyberať dáta.
* **Aktualizovať riadky** - iba Shopify a iba vtedy, keď udelíte prístup Writable.

Keďže čítanie aj zápis využívajú rovnaký engine ako mriežka a plánovač, agent vidí presne tie isté dáta a možnosti ako vy - nikdy nie viac, než aký prístup mu udelíte.

![DbGate Central - MCP server pre AI agentov](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
