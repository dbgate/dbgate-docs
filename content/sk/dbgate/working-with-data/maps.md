---
sourceHash: a1e2c8e626b7d397e242c5a182c920ca58971109a164a8c90e909a521a92e5db
language: sk
title: Mapy
weight: 40
---

DbGate podporuje zobrazovanie geografických údajov v mapách.

## Podporované zdroje máp
- MySQL: Všetky priestorové stĺpce
- MSSQL: Stĺpce typu GEOGRAPHY
- PostGIS: Stĺpce typu GEOGRAPHY
- Všetky zdroje údajov: súradnice uložené v stĺpcoch zemepisnej šírky/dĺžky

## Vyvolanie zobrazenia mapy
Zobrazenie mapy sa vyvoláva z dátovej mriežky. Najprv vyberte bunky s požadovanými geografickými údajmi. Najjednoduchší spôsob je vybrať bunku typu GEOGRAPHY alebo GEOMETRY. Môžete tiež vybrať viacero riadkov. Potom kliknite na widget Cell data. V tomto widgete by ste mali vidieť mapu.

![screenshot](/img/map1.png)

Ak máte uložené stĺpce so zemepisnou šírkou a dĺžkou, vyberte všetky údaje, ktoré chcete mať v mape. Iné stĺpce než zemepisná šírka alebo dĺžka sa zobrazia vo vyskakovacích oknách značiek.

![screenshot](/img/map2.png)

Alternatívne môžete na vybraných bunkách v dátovej mriežke použiť kontextovú ponuku "Open selection in map", čím sa otvorí nová karta s mapou.

V kontextovej ponuke mapy je tiež možnosť exportovať mapu do samostatného HTML súboru, ktorý je možné zobraziť kdekoľvek, kde DbGate nie je nainštalovaný.
