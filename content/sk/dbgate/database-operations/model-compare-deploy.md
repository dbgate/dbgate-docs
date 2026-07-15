---
sourceHash: 9faead63589d3a58402650e29cd85afd2223ffa5317dbd506eb962c893c3c04e
language: sk
title: Porovnanie a nasadenie modelov
weight: 15
---

DbGate dokáže porovnávať štruktúru databázy a nasadzovať zmeny *(Premium)*. Je to užitočné pri udržiavaní prostredí v synchronizácii a pri verziovaní schémy.

![Compare database](https://media.dbgate.io/img/compare-database-settings-light.png)

## Porovnanie databáz

* **Porovnanie dvoch databáz** - nájdite rozdiely v stĺpcoch, definíciách pohľadov a ďalších SQL objektoch.
* **Synchronizácia štruktúry** - vygenerujte a spustite akcie potrebné na to, aby sa jedna databáza zhodovala s druhou.
* **Porovnanie s YAML modelom** - porovnajte reálnu databázu s modelom uloženým v YAML a nasaďte rozdiely.
* **Nastavenia** - riaďte porovnávanie, napríklad ignorujte cudzie kľúče, vylúčte konkrétne objekty alebo zvoľte, ktoré synchronizačné akcie sa majú vykonať.

## Export modelu databázy

* **Scaffold do priečinka** - uložte model existujúcej databázy do priečinka alebo do jedného JSON súboru.
* **YAML súbory tabuliek** - tabuľky sú uložené ako jednoduché YAML súbory, ktoré môžete udržiavať v Git repozitári.
* **SQL súbory definícií** - pohľady, uložené procedúry a funkcie sú uložené ako SQL súbory.

## Nasadenie

Model nasaďte vizuálne pomocou nástroja Compare alebo z príkazového riadka ako súčasť CI/CD pipeline. Formát súboru modelu a postup cez CLI nájdete v článku [Nasadenie databázy](dbdeploy).

## Súvisiace stránky

* [Editor tabuliek a schém](schema-editor) - úprava štruktúry tabuliek cez GUI
* [Nasadenie databázy](dbdeploy) - formát súboru modelu a nasadenie z príkazového riadka
