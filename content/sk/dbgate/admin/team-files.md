---
sourceHash: 8396e36170a2f74ec485cc366db64869390b971ebf497d3127e7005ee1837c1d
language: sk
title: Tímové súbory
weight: 25
---

Tímové súbory sú SQL súbory, diagramy alebo iné súbory uložené v internom úložisku DbGate. Desktopová verzia DbGate ukladá súbory do používateľského priečinka, edícia Team umožňuje ukladať súbory rovnakým spôsobom (v docker volume), ale vhodnejšie je ukladať súbory do úložnej databázy, ktorá sa pri opätovnom vytvorení kontajnera DbGate nevytvára nanovo.

- Diskové súbory 
    - súbory uložené na disku alebo v docker volume
    - pokiaľ nedefinujete docker volume explicitne (napr. v docker-compose.yaml), súbory sa pri opätovnom vytvorení kontajnera vytvoria nanovo.
- Tímové súbory 
    - súbory uložené v úložnej databáze
    - nestratia sa pri opätovnom vytvorení kontajnera, bez potreby definovať docker volume
    - umožňujú definovať podrobné prístupové oprávnenia pre používateľov a roly

## Uloženie SQL súboru ako tímového súboru
Pri ukladaní SQL súboru stačí zaškrtnúť políčko "Save to team folder". Súbor sa uloží ako tímový súbor.
