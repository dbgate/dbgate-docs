---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: sk
title: Pripojenie
weight: 20
---

Pripojiť sa k databáze z DbGate je jednoduché. K databáze sa môžete pripojiť niekoľkými rôznymi spôsobmi:

* Menu Súbor/Pridať pripojenie alebo ikona {{< mdi "plus-thick" >}} vo widgete PRIPOJENIA
* Menu Súbor/Nová SQLite databáza - vytvorí novú SQLite databázu
* Menu Súbor/Otvoriť - môžete otvoriť existujúcu SQLite databázu

## Obrazovka pripojenia
![Obrazovka pripojenia](https://media.dbgate.io/img/new-connection-light.png)

Polia na obrazovke pripojenia výrazne závisia od typu pripojenia.

Niekoľko bežných polí:

* Server - názov hostiteľa databázového servera
* Port - port, v prípade predvoleného portu databázy ho môžete nechať prázdny
* Používateľ, Heslo - autentifikácia
* Režim hesla
    * Uložiť a zašifrovať - heslo sa uloží zašifrované, nabudúce ho neuvidíte
    * Uložiť RAW - heslo sa uloží tak, ako je (bez šifrovania), neskôr si ho môžete pozrieť
    * Neukladať, pýtať sa na heslo - heslo sa neukladá, musíte ho zadať pri pripájaní
    * Neukladať, pýtať sa na prihlasovacie meno a heslo - neukladá sa ani heslo, ani prihlasovacie meno, pri pripájaní musíte zadať oboje
* Iba na čítanie - Pripojenie bude iba na čítanie (pri enginoch bez podpory relácií iba na čítanie v tomto prípade nemôžete spúšťať SQL dotazy)
* Predvolená databáza - ktorá databáza bude aktívna po pripojení
* Použiť iba databázu *&lt;predvolená databáza&gt;* - ak je zaškrtnuté, v strome pripojení sa zobrazí iba predvolená databáza (ostatné databázy na serveri sú skryté)
* Zobrazovaný názov - názov, pod ktorým sa pripojenie zobrazí v aplikácii

## SSH tunel
Tu môžete nakonfigurovať pripojenie cez SSH tunel. 

Bežné polia:
* Použiť SSH tunel - zaškrtnite pre použitie SSH tunela
* Hostiteľ - názov hostiteľa SSH servera

![DbGate - konfigurácia SSH tunela](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
Konfigurácia SSL pripojenia.

Bežné polia:
* Použiť SSL - zaškrtnite pre použitie SSL. Vo väčšine prípadov je to jediné, čo musíte nakonfigurovať pre použitie SSL

![DbGate - konfigurácia SSL pripojenia](https://media.dbgate.io/img/connection-ssl-window-light.png)
