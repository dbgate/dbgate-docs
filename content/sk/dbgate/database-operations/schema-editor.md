---
sourceHash: 0f10d627c0492363d84834c24da993d0686916c833728726a2d34648885161b1
language: sk
title: Editor tabuliek a schém
weight: 5
---

DbGate dokáže vytvárať a upravovať štruktúru databázy pomocou grafického rozhrania, bez ručného písania DDL. Editor štruktúry tabuľky otvoríte z jej kontextového menu ("Edit table"), prípadne vytvoríte novú tabuľku z kontextového menu databázy.

![Editor štruktúry tabuľky](https://media.dbgate.io/img/table-structure-editor-light.png)

## Úprava tabuliek

* **Stĺpce a dátové typy** - definujte stĺpce, dátové typy, nullovateľnosť a predvolené hodnoty pre nové aj existujúce tabuľky.
* **Kľúče a indexy** - spravujte primárne kľúče, cudzie kľúče a indexy.
* **Vlastnosti špecifické pre engine** - nastavte možnosti špecifické pre danú databázu, napríklad engine tabuľky v MySQL.

## Náhľad SQL a bezpečné zmeny

* **Náhľad SQL** - skôr než sa čokoľvek uloží, DbGate zobrazí vygenerované SQL, aby ste si ho mohli skontrolovať.
* **Upozornenie na opätovné vytvorenie tabuľky** - keď si zmena vyžaduje opätovné vytvorenie tabuľky (obmedzenie niektorých databáz), DbGate vás upozorní a umožní vám najprv si prezrieť vygenerovaný skript.

## Ďalšie databázové objekty

Môžete tiež vytvárať, odstraňovať a upravovať ďalšie objekty - pohľady, uložené procedúry a funkcie - a prehliadať tabuľky, pohľady, procedúry, funkcie a MongoDB kolekcie zo stromu objektov.

## Súvisiace stránky

* [Porovnanie a nasadenie modelov](model-compare-deploy) - porovnanie štruktúry medzi databázami a nasadenie zmien *(Premium)*
* [Nasadenie databázy](dbdeploy) - modelové súbory YAML/SQL a nasadenie cez CLI
