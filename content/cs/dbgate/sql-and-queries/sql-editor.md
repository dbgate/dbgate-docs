---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: cs
title: SQL editor
weight: 10
---

SQL editor je místo, kde píšete a spouštíte SQL skripty nad svým připojením. Otevřete jej tlačítkem {{< mdi "flash" >}} "New query" na nástrojové liště nebo z kontextové nabídky připojení či databáze.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## Spouštění SQL

* **Spustit skript** - spustí celý skript tlačítkem {{< mdi "play" >}} Execute (nebo klávesou F5).
* **Spustit aktuální příkaz** - spustí pouze příkaz, na kterém je kurzor.
* **Spustit výběr** - pokud vyberete část skriptu, spustí se pouze vybraný text.
* Výsledky se zobrazí ve výsledkové mřížce pod editorem. Více výsledkových sad se zobrazuje v samostatných záložkách.
* Zprávy, počty řádků a chyby se zobrazují v záložce **Messages**.

## Pomůcky pro editaci

* **Formátovač SQL kódu** - přeformátuje aktuální skript pro konzistentní odsazení a velikost písmen.
* **Dokončování kódu** - návrhy tabulek, sloupců a klíčových slov na základě schématu připojené databáze.
* **Pomocník pro joiny** - nástroj "Add SQL join" vygeneruje klauzuli `LEFT`/`INNER`/`RIGHT JOIN` z cizích klíčů, takže nemusíte podmínky spojení psát ručně.

## Práce s výsledky

Výsledková mřížka používá stejný engine jako [prohlížeč dat](/cs/dbgate/working-with-data/data-browser/), takže můžete [filtrovat a řadit](/cs/dbgate/working-with-data/data-filtering/), kopírovat buňky v různých formátech a výsledek [exportovat](/cs/dbgate/working-with-data/export-import/).

### Editace výsledků dotazů a pohledů *(Premium)*

Výsledky dotazů lze editovat, pokud DbGate dokáže výsledek namapovat zpět na jedinou tabulku nebo aktualizovatelný pohled. Upravujte buňky přímo ve výsledkové mřížce, zkontrolujte vygenerovaný skript změn a uložte jej zpět do databáze - stejný postup s odloženými změnami jako v [prohlížeči dat](/cs/dbgate/working-with-data/data-browser/). Podporována je i editace pohledů.

> Editovatelné výsledky dotazů a editovatelné pohledy byly zavedeny v DbGate 7.2.

## Řízení transakcí

Transakce můžete řídit přímo z editoru - spustit skript v explicitní transakci a změny potvrdit nebo vrátit zpět, což je užitečné při testování skriptů, které modifikují data.

## Další editory

* **Mongo JavaScript editor** - pro připojení k MongoDB umožňuje psát a spouštět Mongo skripty se syntaxí NodeJS.
* **Redis** - procházejte strom klíčů Redis, generujte skript z vybraných klíčů a spouštějte Redis skripty.
