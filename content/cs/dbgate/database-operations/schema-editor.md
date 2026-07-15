---
sourceHash: 0f10d627c0492363d84834c24da993d0686916c833728726a2d34648885161b1
language: cs
title: Editor tabulek a schématu
weight: 5
---

DbGate umí vytvářet a upravovat strukturu databáze přes grafické rozhraní, bez ručního psaní DDL. Editor struktury tabulky otevřete z její kontextové nabídky („Upravit tabulku“), nebo vytvořte novou tabulku z kontextové nabídky databáze.

![Table structure editor](https://media.dbgate.io/img/table-structure-editor-light.png)

## Úpravy tabulek

* **Sloupce a datové typy** - definujte sloupce, datové typy, možnost hodnoty NULL a výchozí hodnoty pro nové i existující tabulky.
* **Klíče a indexy** - spravujte primární klíče, cizí klíče a indexy.
* **Vlastnosti specifické pro engine** - nastavte volby specifické pro danou databázi, například engine tabulky v MySQL.

## Náhled SQL a bezpečné změny

* **Náhled SQL** - dříve než se cokoli uloží, DbGate zobrazí vygenerované SQL, abyste si ho mohli zkontrolovat.
* **Upozornění na znovuvytvoření tabulky** - pokud změna vyžaduje znovuvytvoření tabulky (omezení některých databází), DbGate vás upozorní a umožní vám nejprve prohlédnout vygenerovaný skript.

## Další databázové objekty

Můžete také vytvářet, mazat a upravovat další objekty - pohledy, uložené procedury a funkce - a procházet tabulky, pohledy, procedury, funkce a MongoDB kolekce ve stromu objektů.

## Související stránky

* [Porovnání a nasazení modelů](model-compare-deploy) - porovnání struktury mezi databázemi a nasazení změn *(Premium)*
* [Nasazení databáze](dbdeploy) - modelové soubory YAML/SQL a nasazení přes CLI
