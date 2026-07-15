---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: cs
title: Data deployer
weight: 2
---

Pomocí data deployeru můžete vizuálně porovnat a synchronizovat data v **archivních složkách** se **skutečnou databází**
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Spuštění data deployeru
Data deployer můžete spustit z kontextového menu databáze nebo z kontextového menu archivní složky. Při spuštění z databáze budete vyzváni k výběru archivu. Při spuštění z archivu bude data deployer spuštěn s aktuální databází.

## Nastavení
- Databázový server, databáze - vyberte databázi, se kterou chcete pracovat
- Datový archiv - vyberte složku s daty, která bude použita pro porovnání a synchronizaci
### Související s tabulkou
- Klíč (porovnávací sloupce) - vyberte sloupce, které budou použity pro párování řádků mezi databází a archivem
### Nastavení replikátoru
Níže uvedená nastavení ("table" - deploy a Globální nastavení nasazení dat) jsou specifická pro replikátor a jsou popsána v tématu [Data replicator](data-replicator)

## Kopírování rozdílů v datech
Data deployer zobrazuje rozdíly mezi daty v archivu a v databázi. Pokud vyberete některé buňky s rozdílem, můžete tyto rozdíly zapsat do archivu nebo do databáze. Pokud jsou tyto buňky vybrány, v pravém dolním rohu se objeví tlačítka umožňující synchronizaci:
- Write x rows, y columns to archive - zkopíruje vybrané buňky z databáze do archivu.
- Write x rows, y columns to database - zkopíruje vybrané buňky z archivu do databáze. Nejprve se zobrazí potvrzovací dialog s SQL změnami.

## Akce data replikátoru
- Deploy into DB - tato akce nasadí změny do databáze s nakonfigurovaným nastavením
- Generate shell - tato akce vytvoří soubor JavaScript, který spustí nasazení. Tento soubor lze spustit z příkazové řádky
- Generate SQL - vytvoří SQL, které nasadí změny z archivu do databáze

Více o těchto akcích v tématu [Data replicator](data-replicator)
