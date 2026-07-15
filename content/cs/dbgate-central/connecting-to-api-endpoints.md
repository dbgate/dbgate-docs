---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: cs
title: Připojení k API endpointům
weight: 10
---

DbGate Central se připojuje ke třem skupinám API endpointů, přičemž pro všechny používá stejný dialog New Connection.

## Podporované typy endpointů

* **GraphQL** - prozkoumejte schéma, procházejte typy a spouštějte dotazy proti libovolnému GraphQL API.
* **oData** - pracujte se službami oData V4, jako by to byly běžné tabulky.
* **Shopify** - připojte se ke svému obchodu prostřednictvím Shopify Admin API a prozkoumejte produkty, objednávky, zákazníky, metafieldy a další.

## Vytvoření připojení

Otevřete dialog **New Connection**, zvolte typ připojení, zadejte URL služby a vyberte způsob autentizace:

* **None** - pro otevřené, veřejné endpointy.
* **Basic** - uživatelské jméno a heslo.
* **Bearer token** - vložte přístupový token.
* **API key** - odešlete klíč v hlavičce nebo parametru dotazu.

Připojení se ukládají do vašeho workspace, takže je najdete i při příštím přihlášení, na jakémkoli zařízení, bez nutnosti cokoli lokálně nastavovat.

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
