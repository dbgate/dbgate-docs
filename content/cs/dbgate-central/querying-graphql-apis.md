---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: cs
title: Dotazování GraphQL API
weight: 20
---

Nasměrujte DbGate Central na libovolné GraphQL API a on sám zjistí, co je k dispozici - není potřeba se probírat samostatnou dokumentací.

## Prozkoumání schématu

DbGate Central provede introspekci schématu GraphQL hned po připojení. Procházejte dostupné typy a pole ve stromu a poté otevřete záložku s dotazem a začněte pracovat.

## Spouštění dotazů

* Pište dotazy v editoru GraphQL a spouštějte je proti živému API.
* Zadávejte proměnné dotazu spolu s dotazem, buď ve formuláři, nebo jako čisté JSON.
* Výsledky se vracejí ve stejné rychlé mřížce s možností řazení a filtrování, která se používá všude v DbGate, takže odpověď GraphQL působí jako databázová tabulka.
* Vnořené objekty a seznamy se vracejí jako strukturované JSON, které můžete přímo na místě rozbalit a prozkoumat.

Dotazované pohledy se ukládají do mezipaměti pro každé připojení, takže jejich opětovné otevření je okamžité, zatímco pokračujete v práci.

> Připojení GraphQL v DbGate Central jsou samostatná implementace založená na prohlížeči, oddělená od [desktopové funkce GraphQL](/cs/dbgate/developer/api-connections/#graphql) - pokud používáte desktopovou aplikaci, podívejte se na tuto stránku.

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
