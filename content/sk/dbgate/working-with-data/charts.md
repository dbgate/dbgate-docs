---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: sk
title: Grafy
weight: 30
---

V DbGate môžete použiť graf na vizualizáciu svojich SQL dotazov. Jednoducho spustite dotaz a ak je graf automaticky rozpoznaný, zobrazí sa záložka "Chart 1". Ak máte viac výsledkov dotazu, môže byť aj viac grafov.

Ak nie je automaticky rozpoznaný žiadny graf, ale chceli by ste vytvoriť graf z výsledkov svojho dotazu, kliknite pravým tlačidlom na dáta výsledku dotazu a zvoľte "Open chart".

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## Nastavenia grafu
Na vyvolanie nastavení grafu použite tlačidlo {{< mdi "pencil" >}} Customize. Môžete nakonfigurovať zdroj dát a štýl grafu:
* Typ grafu
  * Stĺpcový (Bar)
  * Čiarový (Line)
  * Časová os (Timeline) - je to špeciálny prípad čiarového grafu, s časom na osi X
  * Koláčový (Pie)
  * Polárna oblasť (Polar area)
* Pole osi X - dáta na osi X. Pre hodnoty typu dátum/čas sú dostupné funkcie zoskupovania a časovej osi
* Pole zoskupenia - definuje viac grafov určených hodnotou tohto poľa
* Transformácia osi X - umožňuje definovať zoskupenie pre časovú os na osi X (napr. podľa roku alebo podľa mesiaca)
* Pole osi Y N - na osi Y môžete mať viac polí
  * Pre každú dátovú sadu je dostupné špeciálne pole "Count", ktoré počíta riadky
* Agregačná funkcia - Sum, Minimum, Maximum, Average, First Value, Last Value

Keď zmeníte akúkoľvek voľbu v nastaveniach grafu, uloží sa na začiatok SQL skriptu ako front-matter.

## Manuálna úprava definície grafu
Niektoré voľby nie sú dostupné v editore, ale dajú sa upraviť v SQL kóde. Pre viac informácií si prečítajte [SQL front matter](/sk/dbgate/developer/sql-front-matter)
