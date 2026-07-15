---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: sk
title: Pripojenie k API endpointom
weight: 10
---

DbGate Central sa pripája k trom skupinám API endpointov, pričom pre všetky používa rovnaký dialóg Nové pripojenie.

## Podporované typy endpointov

* **GraphQL** - introspekcia schémy, prehliadanie typov a spúšťanie dotazov proti ľubovoľnému GraphQL API.
* **oData** - práca so službami oData V4, akoby to boli bežné tabuľky.
* **Shopify** - pripojenie k vášmu obchodu cez Shopify Admin API a prehliadanie produktov, objednávok, zákazníkov, metafieldov a ďalších objektov.

## Vytvorenie pripojenia

Otvorte dialóg **Nové pripojenie**, vyberte typ pripojenia, zadajte URL služby a zvoľte spôsob overenia:

* **Žiadne** - pre otvorené, verejné endpointy.
* **Basic** - používateľské meno a heslo.
* **Bearer token** - vložte prístupový token.
* **API kľúč** - odošlite kľúč v hlavičke alebo v parametri dotazu.

Pripojenia sa ukladajú vo vašom workspace, takže ich máte k dispozícii pri ďalšom prihlásení, na akomkoľvek zariadení, bez potreby čokoľvek lokálne nastavovať.

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
