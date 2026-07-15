---
sourceHash: 80df2a73525118cee579014e200ff5f67715aa6f35468656abb3f8b70c254566
language: cs
title: Datové archivy
weight: 1
---

Archivy jsou složky s daty ve formátu JSONL (NDJSON). DbGate s nimi umožňuje pracovat velmi efektivně, můžete je importovat do databáze, exportovat do jiných formátů nebo data v archivu přímo editovat. Archiv se chová jako velmi rychlá a odlehčená databáze uložená v lokálních souborech.

## Formát JSONL
DbGate interně používá formát JSONL všude. JSONL je textový soubor, kde každý řádek obsahuje řádek dat serializovaný do JSON. DbGate předpokládá, že první řádek může obsahovat hlavičku (rovněž jako JSON) se strukturou tabulky. Když použijete JSONL s dynamickou strukturou (bez prvního pevného řádku), je tento formát standardizovaný a lze jej načíst do mnoha dalších nástrojů.

## Složky archivu
Archiv je organizován do složek se soubory JSONL. Má podobnou strukturu jako databáze. Můžete tak exportovat celou databázi do nového archivu — každá tabulka je exportována do jednoho souboru JSON, díky řádku s hlavičkou je zachována i struktura tabulky.

## Prohlížení a editace souborů archivu
Soubory JSONL můžete otevřít v různých režimech:
- kontextové menu "Open" – otevře datovou mřížku, která umožňuje řazení, filtrování a editaci vašich dat JSONL
- kontextové menu "Open in text editor" – umožňuje ruční editaci souboru JSONL

## Archivy a DB modely
Složky archivu se používají také jako úložiště pro DB modely. DB model můžete exportovat v kontextovém menu databáze pomocí "Export DB model". Tento model pak můžete editovat (soubory YAML pro strukturu tabulek, soubory SQL pro pohledy a uložené procedury), porovnat jej se skutečnou databází a nasadit do databáze
