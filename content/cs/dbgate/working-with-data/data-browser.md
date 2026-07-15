---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: cs
title: Prohlížeč a editor dat
weight: 5
---

Prohlížeč dat je hlavní pohled DbGate pro zobrazování a úpravu dat v tabulkách. Otevřete libovolnou tabulku, pohled nebo kolekci a získáte rychlou mřížku připomínající Excel. Tato stránka popisuje procházení, úpravy a navigaci v souvisejících datech; výrazy filtrů najdete v části [Filtrování dat](data-filtering).

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## Procházení dat

* **Ovládání klávesnicí** - pohybujte se v mřížce pomocí šipek, stejně jako v tabulkovém procesoru.
* **Řazení** - kliknutím na záhlaví sloupce seřadíte data podle tohoto sloupce.
* **Filtrování** - filtrujte řádky pomocí řádku filtru nad mřížkou; kompletní syntaxi výrazů najdete v části [Filtrování dat](data-filtering).
* **Správce sloupců** - vyhledávejte sloupce podle názvu a skryjte ty, které nepotřebujete.
* **Pokročilé kopírování** - kopírujte vybrané buňky jako CSV, YAML, SQL příkazy `INSERT` nebo vkládání do MongoDB.

## Úprava dat

Úprava dat probíhá přímo v mřížce:

* **Úpravy jako v Excelu** - upravujte buňky přímo na místě; kopírujte a vkládejte oblasti řádků, a to i mezi tabulkami.
* **Připravené změny** - vaše úpravy se shromažďují jako čekající změny. Před zápisem do databáze si můžete prohlédnout vygenerovaný SQL skript změn a poté je uložit nebo vrátit zpět.
* **Vkládání a mazání řádků** z mřížky nebo z kontextové nabídky.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### Makra editoru dat *(Premium)*

Aplikujte na vybrané buňky předdefinovaná makra - například změňte velikost písmen, odstraňte diakritiku nebo vygenerujte UUID.

## Práce se souvisejícími daty

DbGate usnadňuje sledování vztahů mezi tabulkami:

* **Nápovědy vztahů** - vedle číselného cizího klíče uvidíte textovou hodnotu z odkazované tabulky.
* **Rozbalení sloupce cizího klíče** - rozbalte sloupec cizího klíče a zobrazte odkazovaná data přímo v mřížce.
* **Otevřít detail** - přejděte na odkazovaný řádek cizího klíče.
* **Pohledy master/detail** *(Premium)* - procházejte související řádky v propojeném rozvržení master/detail.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## Formulářový pohled

Formulářový pohled zobrazuje jediný řádek jako svislý, "transponovaný" seznam - ideální pro tabulky s mnoha sloupci. Funguje jako stromový pohled, takže sloupce s cizími klíči lze rozbalit a prozkoumat související data.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## Seskupování *(Premium)*

Použijte v mřížce seskupování (`GROUP BY`) a agregujte řádky přímo při procházení.

## Související stránky

* [Filtrování dat](data-filtering) - syntaxe filtrovacích výrazů
* [Export a import](export-import) - přesun dat do tabulek a z tabulek
* [Perspektivy](perspectives) - vnořené pohledy pouze pro čtení nad složitými souvisejícími daty
* [SQL editor](/cs/dbgate/sql-and-queries/sql-editor/) - stejný způsob úpravy výsledků dotazů *(Premium)*
