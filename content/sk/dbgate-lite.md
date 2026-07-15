---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: sk
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) je bezplatný nástroj na prácu s dátami priamo v prehliadači - bez inštalácie a bez prihlásenia. Je postavený na rovnakej mriežke, filtrovaní a dotazovacom engine ako [DbGate Central](../dbgate-central/), takže prehliadanie, filtrovanie a úpravy fungujú v oboch rovnako.

## Učte sa a učte SQL

DbGate Lite spúšťa **SQLite a DuckDB** úplne vo vašom prehliadači pomocou technológie WebAssembly:

* Píšte a spúšťajte SQL dotazy nad ukážkovou databázou v známej mriežke DbGate.
* Vizualizujte vzťahy medzi tabuľkami pomocou ER diagramov.
* Žiadna inštalácia, žiadne prihlásenie - otvorte stránku a začnite pracovať.

## Ad-hoc práca s dátovými súbormi

Otvorte súbor v DbGate Lite a pracujte s ním ako s databázou:

* **Importujte** súbory CSV, JSON a Excel a dotazujte sa na ne alebo ich upravujte pomocou SQL.
* Vyčistite a pretvorte dáta a potom výsledok **exportujte** späť do CSV, JSON alebo Excelu.

## Zdieľanie databázy alebo dotazu pomocou odkazu

Otvorenie DbGate Lite s určitými hash parametrami v URL automaticky inicializuje dočasnú databázu:

* `initdbtype` - typ databázy, `sqlite` alebo `duckdb`
* `initdbscript` - SQL skript použitý na vytvorenie a naplnenie dočasnej databázy
* `initquery` (voliteľné) - SQL dotaz otvorený na novej karte Query

Ktokoľvek, kto odkaz otvorí, získa jedným kliknutím rovnakú ukážkovú databázu a dotaz - to sa hodí pre tutoriály, hlásenia chýb a výučbu.

## Publikovanie zobrazenia iba na čítanie

Nezávisle od zdieľania upraviteľného odkazu môžete **publikovať** zobrazenie iba na čítanie pre súbor CSV/JSON alebo BI report pomocou tlačidla Publish na paneli nástrojov. Otvorí sa samostatná stránka - len dáta a prepínač svetlého/tmavého režimu, bez bočného panela či editora - ktorú si môže pozrieť ktokoľvek s odkazom, a to bez konta.

## Voľba medzi Lite, Central, Premium a Team Premium

DbGate Lite je najvhodnejší na učenie a jednorazové úlohy. Pre priebežnú profesionálnu prácu je vhodnejší špecializovaný produkt:

* **DbGate Lite** - bezplatný, v prehliadači. Najvhodnejší na učenie SQL a ad-hoc dátové súbory.
* **[DbGate Central](../dbgate-central/)** - hostovaný produkt na prácu s API: pripojte sa k živým endpointom GraphQL, oData a Shopify, uchovávajte pripojenia a reporty v pracovnom priestore a zdieľajte ich so svojím tímom.
* **[DbGate Premium](/sk/dbgate/getting-started/installation/)** - edícia produktu [DbGate](/sk/dbgate/): plnohodnotná desktopová aplikácia na prácu s databázami, pripojte sa k SQL a NoSQL serverom s kompletnou sadou profesionálnych nástrojov.
* **[DbGate Team Premium](/sk/dbgate/getting-started/installation/docker-tp/)** - ďalšia edícia produktu [DbGate](/sk/dbgate/), určená pre tímy: zdieľané webové rozhranie bežiace on-premise, takže celý váš tím pracuje s databázami z prehliadača na vašej vlastnej infraštruktúre.
