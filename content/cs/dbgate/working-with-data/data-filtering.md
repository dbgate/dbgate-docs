---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: cs
title: Filtrování dat
weight: 10
---

DbGate má výkonný filtrovací engine, který umožňuje jak velmi snadné filtrování dat, tak i složité podmínky.

Filtry dat lze v DbGate použít na mnoha místech, ale nejběžnějším místem je filtrování datové mřížky.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

Filtry jsou vyplněny pozadím:
* Zelené pozadí - filtr je správný a je použit
* Červené pozadí - ve výrazu filtru je chyba, filtr je ignorován

Máte několik možností, jak filtr vytvořit:
* {{< mdi "filter" >}} - zobrazí nabídku s předdefinovanými filtry a dialogy
* {{< mdi "dots-vertical" >}} - umožňuje vybrat hodnoty pro filtrování
* Filtr můžete napsat přímo - použijte velmi jednoduchou syntaxi popsanou v [filter-expressions](#filter-expressions)
* Nebo můžete filtr vytvořit vizuálními metodami a upravit jej ručně

Další příkazy:
* {{< mdi "filter-off" >}} - vymazat všechny filtry

## Filter expressions
Výrazy filtrů jsou navrženy tak, aby byly intuitivní, ve většině případů jednoduše přímo napíšete, co chcete hledat. Syntaxe je však poměrně výkonná, můžete kombinovat několik podmínek a používat různé operátory.
Syntaxe výrazu závisí na datovém typu sloupce.

### Příklady

| Typ sloupce | Výraz filtru |  Popis |
|----------|-------------|------|
| string | canada | hodnota sloupce obsahuje text "canada" |
| string | canada, usa | hodnota sloupce obsahuje text "canada" nebo "usa" |
| string | canada lake | hodnota sloupce obsahuje text "canada" a "lake" |
| string | NOT EMPTY NOT NULL | řetězec nemá prázdnou hodnotu |
| number | >10 | hodnota sloupce je větší než 10 |
| number | >=5 <=10 | hodnota sloupce je mezi 5 a 10 |
| number | 1,2,3 | hodnota sloupce je 1 nebo 2 nebo 3 |
| datetime | 2020-05-26 | hodnota data je z 2020-05-26 (24hodinový interval)  |

### Společné filtry (pro všechny datové typy)
- NULL - hodnota sloupce je null
- NOT NULL - hodnota sloupce není null
- {$$ is null} - SQL podmínka, zapsaná ve složených závorkách {}. $$ je zástupný symbol pro filtrovaný sloupec

### Textové filtry
Porovnávání textu nerozlišuje velká a malá písmena.
- text - hodnota sloupce obsahuje _text_. Může být v 'jednoduchých uvozovkách' nebo "dvojitých uvozovkách"
- +text - hodnota sloupce obsahuje _text_ (stejné jako řádek výše)
- ^text - hodnota sloupce začíná na _text_
- $text - hodnota sloupce končí na _text_
- !+text - hodnota sloupce neobsahuje _text_ (stejné jako řádek výše)
- !^text - hodnota sloupce nezačíná na _text_
- !$text - hodnota sloupce nekončí na _text_
- EMPTY - hodnota sloupce neobsahuje žádný nebílý znak
- NOT EMPTY - hodnota sloupce obsahuje nebílý znak

### Číselné filtry
- number - hodnota sloupce se rovná číslu
- =number - hodnota sloupce se rovná číslu
- !=number - hodnota sloupce se nerovná číslu
- <>number - hodnota sloupce se nerovná číslu
- <number - hodnota sloupce je menší než číslo
- \>number - hodnota sloupce je větší než číslo
- <=number - hodnota sloupce je menší nebo rovna číslu
- \>=number - hodnota sloupce je větší nebo rovna číslu

### Filtry data a času
- 2021 - rok hodnoty sloupce
- 2021-02 - rok, měsíc hodnoty sloupce
- 2021-02-15 - rok, měsíc, den hodnoty sloupce
- 2021-02-15 23:15 - rok, měsíc, den, hodina, minuta hodnoty sloupce
- 2021-02-15 23:15:51 - rok, měsíc, den, hodina, minuta, sekunda hodnoty sloupce
- Relativní filtry k aktuálnímu datu
  - YESTERDAY
  - TODAY
  - TOMORROW
  - LAST WEEK
  - THIS WEEK
  - NEXT WEEK
  - LAST MONTH
  - THIS MONTH
  - NEXT MONTH
  - LAST YEAR
  - THIS YEAR
  - NEXT YEAR

### Logické (boolean) filtry
- TRUE, true, 1 - hodnota sloupce je true/1
- FALSE, false, 0 - hodnota sloupce je false/0

### Kombinace filtrů
Filtry lze vzájemně kombinovat. Mezera je interpretována jako operátor AND, čárka jako operátor OR. AND má vyšší prioritu než OR.
