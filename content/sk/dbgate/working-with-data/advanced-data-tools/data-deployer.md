---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: sk
title: Nasadzovanie dát (Data deployer)
weight: 2
---

Pomocou nástroja data deployer môžete vizuálne porovnávať a synchronizovať dáta v **archívnych priečinkoch** so **skutočnou databázou**
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Spustenie nástroja data deployer
Nástroj data deployer môžete spustiť z kontextového menu databázy alebo z kontextového menu archívneho priečinka. Pri spustení z databázy budete vyzvaní na výber archívu. Pri spustení z archívu sa data deployer spustí s aktuálnou databázou.

## Nastavenia
- Databázový server, databáza - vyberte databázu, s ktorou chcete pracovať
- Dátový archív - vyberte priečinok s dátami, ktoré sa použijú na porovnanie a synchronizáciu
### Nastavenia týkajúce sa tabuľky
- Kľúč (porovnávacie stĺpce) - vyberte stĺpce, ktoré sa použijú na párovanie riadkov medzi databázou a archívom
### Nastavenia replikátora
Nastavenia nižšie ("tabuľka" - deploy a globálne nastavenia nasadzovania dát) sú špecifické pre replikátor a sú popísané v téme [Data replicator](data-replicator)

## Kopírovanie rozdielov v dátach
Data deployer zobrazuje rozdiely medzi dátami v archíve a v databáze. Ak vyberiete niektoré bunky s rozdielom, môžete tieto rozdiely zapísať do archívu alebo do databázy. Ak sú tieto bunky vybraté, v pravom dolnom rohu sa objavia tlačidlá umožňujúce synchronizáciu:
- Write x rows, y columns to archive - skopíruje vybraté bunky z databázy do archívu.
- Write x rows, y columns to database - skopíruje vybraté bunky z archívu do databázy. Najprv sa zobrazí potvrdzovací dialóg so zmenovým SQL.

## Akcie nástroja data replicator
- Deploy into DB - táto akcia nasadí zmeny do databázy s nakonfigurovanými nastaveniami
- Generate shell - táto akcia vytvorí JavaScript súbor, ktorý spustí nasadenie. Tento súbor je možné spustiť z príkazového riadka
- Generate SQL - vytvorí SQL, ktoré nasadí zmeny z archívu do databázy

Viac o týchto akciách v téme [Data replicator](data-replicator)
