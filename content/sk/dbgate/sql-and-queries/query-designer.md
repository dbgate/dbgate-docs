---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: sk
title: Návrhár dotazov
weight: 20
---

Návrhár dotazov *(Premium)* umožňuje vytvárať SQL dotazy vizuálne, bez ručného písania SQL. Pridajte tabuľky na plátno, vyberte stĺpce a definujte podmienky - DbGate vygeneruje SQL za vás.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## Vytvorenie dotazu

* **Pridanie tabuliek** - presuňte tabuľky na návrhové plátno; DbGate automaticky vykreslí vzťahy podľa cudzích kľúčov.
* **Výber stĺpcov** - zvoľte, ktoré stĺpce sa objavia vo výsledku, definujte triedenie a zoskupovanie.
* **Typy JOIN** - okrem štandardných SQL joinov (`INNER`, `LEFT`, `RIGHT`) môžete použiť pseudo-joiny - najužitočnejším je `WHERE NOT EXISTS`.
* **Výkonné filtre** - filtrujte pomocou rovnakého enginu ako v [prehliadači dát](/sk/dbgate/working-with-data/data-browser/), vrátane zložených podmienok a filtrovania podľa množiny hodnôt.

## Výsledok

Návrhár vytvára bežný SQL dotaz, takže beží s rovnakým výkonom ako ručne písané SQL. Kedykoľvek môžete prepnúť na vygenerované SQL a pokračovať v jeho úprave v [SQL editore](sql-editor).

## Perspektívy - univerzálny návrhár

Pre vnorené, hierarchické pohľady - a pre spájanie dát naprieč SQL tabuľkami a MongoDB kolekciami na strane klienta - použite [Perspektívy](/sk/dbgate/working-with-data/perspectives/), ktoré nie sú obmedzené tým, čo dokáže spojiť zdrojová databáza.
