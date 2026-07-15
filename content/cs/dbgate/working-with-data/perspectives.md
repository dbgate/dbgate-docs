---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: cs
title: Perspektivy
weight: 50
---

Perspektiva je pouze pro čtení určený pohled na složitá vnořená data. Připomíná sestavy, ale perspektivy se vytvářejí jednoduše přidáním dat do pohledu. Můžete použít návrhář perspektiv, který umožňuje spojovat data i podle jiných vztahů než cizích klíčů.

Perspektivy dokážou snadno spojovat data dohromady a zobrazovat skupiny.

<!-- ![screenshot](/screenshots/perspective1.png) -->

## Vytvoření perspektivy
Perspektivy lze vytvářet ze SQL tabulek a pohledů (kolekce MongoDB zatím nejsou podporovány, ale tato podpora se plánuje).
Použijte kontextové menu tabulky/pohledu, "Open perspective".

![screenshot](/img/perspective-create.png)

DbGate otevře jednoduchou perspektivu, ve které je zobrazen pouze jeden sloupec. Tento sloupec je vybrán heuristickým algoritmem tak, aby byl nejlepší reprezentací celého řádku.
## Přizpůsobení perspektivy
Můžete určit, které sloupce jsou v pohledu k dispozici. Také můžete do pohledu přidat odkazovaná data. Pro procházení stromu referencí použijte tlačítko pro rozbalení.

## Filtrování dat
Použijte kontextové menu v tabulce nebo v seznamu sloupců na levé straně, "Add to filter". Můžete použít stejné filtrovací výrazy jako na jiných místech v DbGate. Nebo můžete na buňce tabulky použít příkaz kontextového menu "Filter this value".

## Filtrování nadřazených řádků
Předpokládejme následující perspektivu. Máme vztah master/detail, Genre se souvisejícími skladbami. Chceme filtrovat podle Track (zkusil jsem hledat text "mix").

![screenshot](/img/parentrows1.png)

Jak vidíte, je zde mnoho řádků Genre bez jakékoli skladby odpovídající kritériím vyhledávání. Pokud chcete filtrovat i řádky Genre, použijte příkaz "Filter parent rows" v kontextovém menu záhlaví tabulky. Také můžete použít přepínací tlačítko v řádku filtru.

![screenshot](/img/parentrows2.png)

## Definování vlastních spojení
Perspektivy fungují velmi dobře s cizími klíči. Ale tuto funkci můžete využít i tehdy, když máte databázi bez cizích klíčů. Je možné definovat vlastní spojení s libovolnou podmínkou. Můžete dokonce definovat vlastní spojení do jiné databáze (která může být na jiném databázovém serveru, dokonce i s odlišným databázovým strojem).

![screenshot](/img/customjoin.png)

Sloupce můžete také přetáhnout myší a vytvořit tak vztah spojení.

![screenshot](/img/customjoin2.png)
