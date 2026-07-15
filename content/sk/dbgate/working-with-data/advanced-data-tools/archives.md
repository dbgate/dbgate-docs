---
sourceHash: 80df2a73525118cee579014e200ff5f67715aa6f35468656abb3f8b70c254566
language: sk
title: Dátové archívy
weight: 1
---

Archívy sú priečinky s dátami vo formáte JSONL (NDJSON). DbGate umožňuje s nimi pracovať veľmi efektívne, môžete ich importovať do databázy, exportovať do iných formátov alebo priamo upravovať dáta v archíve. Archív sa správa ako veľmi rýchla a odľahčená databáza uložená v lokálnych súboroch.

## Formát JSONL
DbGate interne používa formát JSONL všade. JSONL je textový súbor, kde každý riadok obsahuje riadok dát serializovaný do JSON. DbGate predpokladá, že prvý riadok môže obsahovať hlavičku (tiež ako JSON) so štruktúrou tabuľky. Keď použijete JSONL s dynamickou štruktúrou (bez prvého pevného riadku), tento formát je štandardizovaný a dá sa načítať do mnohých ďalších nástrojov. 

## Priečinky archívov
Archív je organizovaný do priečinkov so súbormi JSONL. Má podobnú štruktúru ako databáza. Celú databázu tak môžete exportovať do nového archívu - každá tabuľka sa exportuje do jedného súboru JSON, vďaka riadku s hlavičkou sa zachová aj štruktúra tabuľky.

## Zobrazenie a úprava súborov archívu
Súbory JSONL môžete otvoriť v rôznych režimoch:
- kontextové menu "Open" - otvorí dátovú mriežku, ktorá umožňuje triedenie, filtrovanie a úpravu vašich dát JSONL
- kontextové menu "Open in text editor" - umožňuje manuálnu úpravu súboru JSONL

## Archívy a DB modely
Priečinky archívov sa používajú aj ako úložisko pre DB modely. DB model môžete exportovať v kontextovom menu databázy, "Export DB model". Tento model potom môžete upravovať (súbory YAML pre štruktúru tabuliek, súbory SQL pre pohľady a uložené procedúry), porovnať ho so skutočnou databázou a nasadiť ho do databázy
