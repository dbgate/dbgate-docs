---
sourceHash: a1e2c8e626b7d397e242c5a182c920ca58971109a164a8c90e909a521a92e5db
language: cs
title: Mapy
weight: 40
---

DbGate podporuje zobrazování geografických dat v mapách.

## Podporované zdroje map
- MySQL: Všechny prostorové sloupce
- MSSQL: Sloupce typu GEOGRAPHY
- PostGIS: Sloupce typu GEOGRAPHY
- Všechny datové zdroje: souřadnice uložené ve sloupcích se zeměpisnou šířkou/délkou

## Vyvolání zobrazení mapy
Zobrazení mapy se vyvolává z datové mřížky. Nejprve vyberte buňky s požadovanými geografickými daty. Nejjednodušší způsob je vybrat buňku typu GEOGRAPHY nebo GEOMETRY. Můžete také vybrat více řádků. Poté klikněte na widget Data buňky. V něm byste měli vidět mapu.

![screenshot](/img/map1.png)

Pokud máte uložené sloupce se zeměpisnou šířkou a délkou, vyberte všechna data, která chcete mít v mapě. Sloupce jiné než zeměpisná šířka nebo délka se zobrazí ve vyskakovacích oknech značek.

![screenshot](/img/map2.png)

Případně můžete v datové mřížce použít na vybraných buňkách kontextovou nabídku „Open selection in map“, čímž se otevře nová záložka s mapou.

V kontextové nabídce mapy je také možnost exportovat mapu do samostatného HTML souboru, který lze zobrazit kdekoli, kde není nainstalován DbGate.
