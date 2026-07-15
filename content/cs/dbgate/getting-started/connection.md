---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: cs
title: Připojení
weight: 20
---

Připojení k databázi z DbGate je snadné. K databázi se můžete připojit několika různými způsoby:

* Menu Soubor/Přidat připojení nebo ikona {{< mdi "plus-thick" >}} ve widgetu PŘIPOJENÍ
* Menu Soubor/Nová databáze SQLite - vytvoří novou databázi SQLite
* Menu Soubor/Otevřít - můžete otevřít existující databázi SQLite

## Obrazovka připojení
![Obrazovka připojení](https://media.dbgate.io/img/new-connection-light.png)

Pole na obrazovce připojení výrazně závisí na typu připojení.

Několik společných polí:

* Server - název hostitele databázového serveru
* Port - port, v případě výchozího portu databáze jej můžete nechat prázdný
* Uživatel, Heslo - autentizace
* Režim hesla
    * Uložit a zašifrovat - heslo je uloženo zašifrovaně, příště jej již neuvidíte
    * Uložit RAW - heslo je uloženo tak, jak je (bez šifrování), můžete si jej později zkontrolovat
    * Neukládat, ptát se na heslo - heslo se neukládá, musíte jej zadat při připojování
    * Neukládat, ptát se na jméno a heslo - neukládá se ani heslo, ani přihlašovací jméno, při připojování musíte zadat obojí
* Je jen pro čtení - Připojení bude pouze pro čtení (u enginů bez podpory relací jen pro čtení v tomto případě nemůžete spouštět SQL dotazy)
* Výchozí databáze - která databáze bude po připojení aktivní
* Používat pouze databázi *&lt;výchozí databáze&gt;* - pokud je zaškrtnuto, ve stromu připojení se objeví pouze výchozí databáze (ostatní databáze na serveru jsou skryté)
* Zobrazovaný název - název, pod kterým se připojení bude v aplikaci zobrazovat

## SSH tunel
Zde můžete nakonfigurovat připojení přes SSH tunel.

Společná pole:
* Použít SSH tunel - zaškrtněte pro použití SSH tunelu
* Host - název hostitele SSH serveru

![DbGate - konfigurace SSH tunelu](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
Konfigurace SSL připojení.

Společná pole:
* Použít SSL - zaškrtněte pro použití SSL. Ve většině případů je to jediné, co musíte pro použití SSL nakonfigurovat

![DbGate - konfigurace SSL připojení](https://media.dbgate.io/img/connection-ssl-window-light.png)
