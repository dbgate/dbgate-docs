---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: sk
title: Filtrovanie údajov
weight: 10
---

DbGate má výkonný filtrovací engine, ktorý umožňuje veľmi jednoduché filtrovanie údajov aj zložité podmienky.

Filtre údajov sa dajú použiť na mnohých miestach v DbGate, ale najbežnejším miestom je filtrovanie mriežky s údajmi.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

Filtre sú vyplnené pozadím:
* Zelené pozadie - filter je správny a je použitý
* Červené pozadie - vo výraze filtra je chyba, filter sa ignoruje

Máte niekoľko možností, ako vytvoriť filter:
* {{< mdi "filter" >}} - zobrazí ponuku s preddefinovanými filtrami a dialógmi
* {{< mdi "dots-vertical" >}} - umožňuje vybrať hodnoty na filtrovanie
* Filter môžete napísať priamo - použite veľmi jednoduchú syntax opísanú v [filter-expressions](#filter-expressions)
* Alebo môžete filter vytvoriť vizuálnymi metódami a upraviť ho manuálne

Ďalšie príkazy:
* {{< mdi "filter-off" >}} - vymaže všetky filtre

## Filter expressions
Výrazy filtrov sú navrhnuté tak, aby boli intuitívne, vo väčšine prípadov jednoducho priamo napíšete, čo chcete hľadať. Syntax je však pomerne výkonná, môžete kombinovať niekoľko podmienok a používať rôzne operátory.
Syntax výrazu závisí od dátového typu stĺpca.

### Príklady

| Typ stĺpca | Výraz filtra |  Popis |
|----------|-------------|------|
| string | canada | hodnota stĺpca obsahuje text "canada" |
| string | canada, usa | hodnota stĺpca obsahuje text "canada" alebo "usa" |
| string | canada lake | hodnota stĺpca obsahuje text "canada" a "lake" |
| string | NOT EMPTY NOT NULL | reťazec má neprázdnu hodnotu |
| number | >10 | hodnota stĺpca je väčšia ako 10 |
| number | >=5 <=10 | hodnota stĺpca je medzi 5 a 10 |
| number | 1,2,3 | hodnota stĺpca je 1 alebo 2 alebo 3 |
| datetime | 2020-05-26 | hodnota dátumu je z 2020-05-26 (24-hodinový interval)  |

### Spoločné filtre (pre všetky dátové typy)
- NULL - hodnota stĺpca je null
- NOT NULL - hodnota stĺpca nie je null
- {$$ is null} - SQL podmienka, zapísaná v zátvorkách {}. $$ je zástupný symbol pre filtrovaný stĺpec

### Textové filtre
Porovnávanie textu nerozlišuje veľké a malé písmená.
- text - hodnota stĺpca obsahuje _text_. Môže byť v 'jednoduchých úvodzovkách' alebo "dvojitých úvodzovkách"
- +text - hodnota stĺpca obsahuje _text_ (to isté ako riadok vyššie)
- ^text - hodnota stĺpca začína na _text_
- $text - hodnota stĺpca končí na _text_
- !+text - hodnota stĺpca neobsahuje _text_ (to isté ako riadok vyššie)
- !^text - hodnota stĺpca nezačína na _text_
- !$text - hodnota stĺpca nekončí na _text_
- EMPTY - hodnota stĺpca neobsahuje žiadny nebiely znak
- NOT EMPTY - hodnota stĺpca obsahuje nebiely znak

### Číselné filtre
- number - hodnota stĺpca sa rovná číslu
- =number - hodnota stĺpca sa rovná číslu
- !=number - hodnota stĺpca sa nerovná číslu
- <>number - hodnota stĺpca sa nerovná číslu
- <number - hodnota stĺpca je menšia ako číslo
- \>number - hodnota stĺpca je väčšia ako číslo
- <=number - hodnota stĺpca je menšia alebo rovná číslu
- \>=number - hodnota stĺpca je väčšia alebo rovná číslu

### Filtre dátumu a času
- 2021 - rok hodnoty stĺpca
- 2021-02 - rok, mesiac hodnoty stĺpca
- 2021-02-15 - rok, mesiac, deň hodnoty stĺpca
- 2021-02-15 23:15 - rok, mesiac, deň, hodina, minúta hodnoty stĺpca
- 2021-02-15 23:15:51 - rok, mesiac, deň, hodina, minúta, sekunda hodnoty stĺpca
- Relatívne filtre voči aktuálnemu dátumu
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

### Logické (boolean) filtre
- TRUE, true, 1 - hodnota stĺpca je true/1
- FALSE, false, 0 - hodnota stĺpca je false/0

### Kombinácie filtrov
Filtre je možné navzájom kombinovať. Medzera sa interpretuje ako operátor AND, čiarka ako operátor OR. AND má vyššiu prioritu ako OR.
