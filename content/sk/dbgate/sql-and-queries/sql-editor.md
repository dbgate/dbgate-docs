---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: sk
title: SQL editor
weight: 10
---

SQL editor je miesto, kde píšete a spúšťate SQL skripty voči vášmu pripojeniu. Otvoríte ho tlačidlom {{< mdi "flash" >}} „Nový dotaz“ na paneli nástrojov alebo z kontextového menu pripojenia či databázy.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## Spúšťanie SQL

* **Spustiť skript** - spustí celý skript tlačidlom {{< mdi "play" >}} Spustiť (alebo klávesom F5).
* **Spustiť aktuálny príkaz** - spustí iba príkaz pod kurzorom.
* **Spustiť výber** - ak označíte časť skriptu, vykoná sa iba označený text.
* Výsledky sa zobrazia vo výsledkovej mriežke pod editorom. Viaceré výsledkové sady sa zobrazujú v samostatných záložkách.
* Správy, počty riadkov a chyby sa zobrazujú v záložke **Messages**.

## Pomôcky pri editovaní

* **Formátovač SQL kódu** - preformátuje aktuálny skript kvôli konzistentnému odsadeniu a veľkosti písmen.
* **Dopĺňanie kódu** - návrhy tabuliek, stĺpcov a kľúčových slov na základe schémy pripojenej databázy.
* **Pomocník pre JOIN** - nástroj „Add SQL join“ vygeneruje klauzulu `LEFT`/`INNER`/`RIGHT JOIN` z cudzích kľúčov, takže nemusíte podmienky spojenia písať ručne.

## Práca s výsledkami

Výsledková mriežka používa rovnaký engine ako [prehliadač dát](/sk/dbgate/working-with-data/data-browser/), takže môžete [filtrovať a triediť](/sk/dbgate/working-with-data/data-filtering/), kopírovať bunky v rôznych formátoch a výsledok [exportovať](/sk/dbgate/working-with-data/export-import/).

### Úprava výsledkov dotazov a pohľadov *(Premium)*

Výsledky dotazov sú editovateľné, keď ich DbGate dokáže namapovať späť na jednu tabuľku alebo na aktualizovateľný pohľad. Bunky upravujte priamo vo výsledkovej mriežke, skontrolujte vygenerovaný skript zmien a uložte ho späť do databázy - ide o rovnaký postup s pripravenými zmenami ako v [prehliadači dát](/sk/dbgate/working-with-data/data-browser/). Podporovaná je aj úprava pohľadov.

> Editovateľné výsledky dotazov a editovateľné pohľady boli zavedené v DbGate 7.2.

## Riadenie transakcií

Transakcie môžete riadiť priamo z editora - vykonať skript v explicitnej transakcii a zmeny potvrdiť alebo vrátiť späť, čo je užitočné pri testovaní skriptov meniacich dáta.

## Ďalšie editory

* **Mongo JavaScript editor** - pre pripojenia k MongoDB píšte a spúšťajte Mongo skripty pomocou syntaxe NodeJS.
* **Redis** - prehliadajte strom kľúčov Redis, vygenerujte skript z vybraných kľúčov a spúšťajte Redis skripty.
