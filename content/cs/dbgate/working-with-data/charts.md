---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: cs
title: Grafy
weight: 30
---

S DbGate můžete použít graf pro vizualizaci svých SQL dotazů. Stačí spustit dotaz, a pokud je graf automaticky detekován, objeví se záložka "Chart 1". Pokud máte více výsledků dotazu, může být grafů více.

Pokud není žádný graf automaticky detekován, ale chtěli byste z výsledků dotazu nějaký graf vytvořit, klikněte pravým tlačítkem na data výsledku dotazu a zvolte "Open chart".

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## Nastavení grafu
Pomocí tlačítka {{< mdi "pencil" >}} Customize vyvoláte nastavení grafu. Můžete konfigurovat zdroj dat a styl grafu:
* Typ grafu
  * Bar
  * Line
  * Timeline - jde o zvláštní případ spojnicového grafu, s časem na ose X
  * Pie
  * Polar area
* Pole osy X - data na ose X. Pro hodnoty typu datum/čas jsou k dispozici funkce seskupování a časové osy
* Pole seskupení - definuje více grafů určených hodnotou tohoto pole
* Transformace osy X - umožňuje definovat seskupení pro časovou osu X (např. podle roku nebo podle měsíce)
* Pole osy Y N - na ose Y můžete mít více polí
  * Pro každou datovou sadu je k dispozici speciální pole "Count", které počítá řádky
* Agregační funkce - Sum, Minimum, Maximum, Average, First Value, Last Value

Když změníte jakoukoli volbu v nastavení grafu, uloží se na začátek SQL skriptu jako front-matter.

## Ruční úprava definice grafu
Některé volby nejsou v editoru dostupné, ale lze je upravit v SQL kódu. Více informací najdete v článku [SQL front matter](/cs/dbgate/developer/sql-front-matter)
