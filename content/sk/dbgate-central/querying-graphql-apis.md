---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: sk
title: Dopytovanie GraphQL API
weight: 20
---

Nasmerujte DbGate Central na ľubovoľné GraphQL API a on sám zistí, čo je k dispozícii - nemusíte sa prehrabávať samostatnou dokumentáciou.

## Preskúmajte schému

DbGate Central vykoná introspekciu GraphQL schémy hneď po pripojení. Prechádzajte dostupné typy a polia v strome a potom otvorte kartu dopytu, aby ste mohli začať pracovať.

## Spúšťanie dopytov

* Píšte dopyty v GraphQL editore a spúšťajte ich proti živému API.
* Popri dopyte zadajte premenné dopytu, buď vo formulári, alebo ako surový JSON.
* Výsledky sa vrátia v rovnakej rýchlej mriežke s možnosťou triedenia a filtrovania, aká sa používa všade v DbGate, takže odpoveď GraphQL pôsobí ako databázová tabuľka.
* Vnorené objekty a zoznamy sa vracajú ako štruktúrovaný JSON, ktorý môžete rozbaliť a preskúmať priamo na mieste.

Dopytované pohľady sa ukladajú do cache pre každé pripojenie, takže ich opätovné otvorenie je okamžité a vy môžete pokračovať v práci.

> GraphQL pripojenia v DbGate Central sú samostatná implementácia bežiaca v prehliadači, oddelená od [funkcie GraphQL v desktopovej aplikácii](/sk/dbgate/developer/api-connections/#graphql) - ak používate desktopovú aplikáciu, pozrite si túto stránku.

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
