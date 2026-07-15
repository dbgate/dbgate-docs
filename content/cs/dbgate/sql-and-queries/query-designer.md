---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: cs
title: Návrhář dotazů
weight: 20
---

Návrhář dotazů *(Premium)* umožňuje sestavovat SQL dotazy vizuálně, bez ručního psaní SQL. Přidejte tabulky na plátno, vyberte sloupce a definujte podmínky - DbGate za vás vygeneruje SQL.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## Sestavení dotazu

* **Přidání tabulek** - přetáhněte tabulky na návrhové plátno; DbGate automaticky vykreslí vazby podle cizích klíčů.
* **Výběr sloupců** - zvolte, které sloupce se objeví ve výsledku, definujte řazení a seskupování.
* **Typy JOIN** - kromě standardních SQL joinů (`INNER`, `LEFT`, `RIGHT`) můžete použít pseudo-joiny - nejužitečnějším z nich je `WHERE NOT EXISTS`.
* **Výkonné filtry** - filtrujte pomocí stejného enginu jako v [prohlížeči dat](/cs/dbgate/working-with-data/data-browser/), včetně složených podmínek a filtrování podle množiny hodnot.

## Výsledek

Návrhář vytváří běžný SQL dotaz, takže běží se stejným výkonem jako ručně psané SQL. Kdykoli můžete přepnout na vygenerované SQL a pokračovat v jeho úpravách v [SQL editoru](sql-editor).

## Perspektivy - univerzální návrhář

Pro vnořené, hierarchické pohledy - a pro spojování dat napříč SQL tabulkami a MongoDB kolekcemi na straně klienta - použijte [Perspektivy](/cs/dbgate/working-with-data/perspectives/), které nejsou omezeny tím, co dokáže spojit zdrojová databáze.
