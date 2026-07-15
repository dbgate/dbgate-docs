---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: cs
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) je bezplatný nástroj pro práci s daty přímo v prohlížeči - bez instalace a bez přihlášení. Je postaven na stejné mřížce, filtrování a dotazovacím jádru jako [DbGate Central](../dbgate-central/), takže procházení, filtrování a editace fungují v obou produktech stejně.

## Učte se a učte SQL

DbGate Lite spouští **SQLite a DuckDB** kompletně ve vašem prohlížeči pomocí WebAssembly:

* Pište a spouštějte SQL dotazy nad ukázkovou databází ve známé mřížce DbGate.
* Vizualizujte vztahy mezi tabulkami pomocí ER diagramů.
* Žádná instalace, žádné přihlášení - otevřete web a začněte pracovat.

## Práce s datovými soubory ad-hoc

Otevřete soubor v DbGate Lite a pracujte s ním jako s databází:

* **Importujte** soubory CSV, JSON a Excel a dotazujte se na ně nebo je upravujte pomocí SQL.
* Vyčistěte a přeuspořádejte data a poté výsledek **exportujte** zpět do CSV, JSON nebo Excelu.

## Sdílení databáze nebo dotazu odkazem

Otevření DbGate Lite s určitými hash parametry v URL automaticky inicializuje dočasnou databázi:

* `initdbtype` - typ databáze, `sqlite` nebo `duckdb`
* `initdbscript` - SQL skript sloužící k vytvoření a naplnění dočasné databáze
* `initquery` (volitelné) - SQL dotaz otevřený v nové záložce Query

Každý, kdo odkaz otevře, získá jedním kliknutím stejnou ukázkovou databázi a dotaz - hodí se pro tutoriály, hlášení chyb a výuku.

## Publikování pohledu jen pro čtení

Nezávisle na sdílení editovatelného odkazu můžete **publikovat** pohled jen pro čtení na soubor CSV/JSON nebo BI report pomocí tlačítka Publish na nástrojové liště. Otevře se samostatná stránka - jen data a přepínač světlého/tmavého režimu, bez postranního panelu či editoru - kterou si může prohlédnout kdokoli s odkazem, aniž by měl účet.

## Volba mezi Lite, Central, Premium a Team Premium

DbGate Lite je nejvhodnější pro učení a jednorázové úkoly. Pro průběžnou profesionální práci se lépe hodí specializovaný produkt:

* **DbGate Lite** - zdarma, v prohlížeči. Nejlepší pro učení SQL a ad-hoc datové soubory.
* **[DbGate Central](../dbgate-central/)** - hostovaný produkt pro práci s API: připojte se k živým GraphQL, oData a Shopify endpointům, uchovávejte připojení a reporty v pracovním prostoru a sdílejte je se svým týmem.
* **[DbGate Premium](/cs/dbgate/getting-started/installation/)** - edice [DbGate](/cs/dbgate/): plnohodnotná desktopová aplikace pro práci s databázemi, připojte se k SQL i NoSQL serverům s kompletní sadou profesionálních nástrojů.
* **[DbGate Team Premium](/cs/dbgate/getting-started/installation/docker-tp/)** - další edice [DbGate](/cs/dbgate/), určená pro týmy: sdílené webové rozhraní běžící on-premise, takže celý váš tým pracuje s databázemi z prohlížeče na vaší vlastní infrastruktuře.
