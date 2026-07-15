---
sourceHash: 8396e36170a2f74ec485cc366db64869390b971ebf497d3127e7005ee1837c1d
language: cs
title: Týmové soubory
weight: 25
---

Týmové soubory jsou SQL, diagramy nebo jiné soubory uložené v interním úložišti DbGate. Desktopová verze DbGate ukládá soubory do uživatelské složky, edice Team umožňuje ukládat soubory stejným způsobem (v docker volume), ale vhodnější je ukládat soubory v databázi úložiště, která není znovu vytvářena při obnovení kontejneru DbGate.

- Diskové soubory 
    - soubory uložené na disku nebo v docker volume
    - pokud explicitně nedefinujete docker volume (např. v docker-compose.yaml), jsou soubory znovu vytvořeny při obnovení kontejneru.
- Týmové soubory 
    - soubory uložené v databázi úložiště
    - nejsou ztraceny při obnovení kontejneru, bez nutnosti definovat docker volume
    - umožňují definovat jemně odstupňovaná přístupová oprávnění pro uživatele a role

## Uložení SQL souboru jako týmového souboru
Při ukládání SQL souboru stačí zaškrtnout políčko "Save to team folder". Soubor bude uložen jako týmový soubor. 