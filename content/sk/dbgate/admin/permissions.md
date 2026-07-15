---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: sk
title: Oprávnenia
weight: 50
---

Oprávnenia v DbGate používajú **dve dimenzie**:

1. **Zdroj oprávnení (kto ich nastavuje)**
   Oprávnenia kaskádovito prechádzajú od všeobecných ku konkrétnym. Konkrétnejšie nastavenia prepisujú tie všeobecnejšie:
   * Preddefinované sady oprávnení
   * Preddefinované role (*superadmin*, *prihlásený používateľ*, *anonymný*)
   * Vlastné role
   * Jednotlivý používateľ

2. **Rozsah objektov**
   Oprávnenia môžu cieliť na konkrétne **databázy** a **tabuľky/objekty**. Pozrite si **[Oprávnenia k databázam](#database-permissions)** a **[Oprávnenia k tabuľkám](#table-permissions)**.

---

## Základné oprávnenia

Globálne/základné oprávnenia nakonfigurujete v **strome oprávnení** v **Detaile používateľa** alebo **Detaile role**.

* **Zošedený** zaškrtávací boxík znamená, že oprávnenie je **zdedené** (napr. z role alebo z preddefinovanej sady oprávnení), nie je nastavené priamo na danom používateľovi/roli.

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## Oprávnenia k databázam

Oprávnenia na úrovni databázy nastavíte na karte **Databases** (v Detaile role aj v Detaile používateľa).

> **Dôležité:** Pravidlá pre databázy sa uplatnia **iba vtedy**, ak je v základných oprávneniach odškrtnuté oprávnenie **„All databases“**.

* Každý riadok v tabuľke pravidiel povoľuje alebo zamieta prístup k databázam, ktoré **zodpovedajú** filtrom daného riadku.
* **Na poradí pravidiel záleží**: pravidlá **nižšie** v zozname **prepisujú** pravidlá nad nimi.

![Database permissions - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**Stĺpce**

* **Connection** – na ktoré pripojenie sa pravidlo vzťahuje.
* **Database names** – databázy, ktoré sa majú zhodovať (zoznam názvov alebo regulárny výraz).
* **Role (úroveň prístupu)**
  * **View** – vidí databázu, ale nie jej tabuľky/pohľady/atď.
  * **Read content** – prístup k obsahu databázy iba na čítanie.
  * **Write data** – môže upravovať dáta v tabuľkách.
  * **Run script** – môže spúšťať ľubovoľný SQL skript; môže vytvárať/rušiť/meniť objekty.
  * **Deny** – blokuje prístup k databáze.

---

## Oprávnenia k tabuľkám

Oprávnenia na úrovni tabuliek/objektov nastavíte na karte **Tables / Views / Objects** (v Detaile role a v Detaile používateľa).

> **Dôležité:** Pravidlá pre tabuľky/objekty sa uplatnia **iba vtedy**, ak je v základných oprávneniach odškrtnuté oprávnenie **„All tables/views/objects“**.

* Každý riadok definuje prístup k tabuľkám/objektom, ktoré **zodpovedajú** filtrom.
* **Na poradí pravidiel záleží**: pravidlá **nižšie** v zozname **prepisujú** pravidlá nad nimi.
* Predvolene sa oprávnenia k tabuľkám **dedia z oprávnenia k databáze**.

**Stĺpce**

* **Connection** – na ktoré pripojenie sa pravidlo vzťahuje.
* **Database names** – databázy, ktoré sa majú zhodovať (zoznam alebo regulárny výraz).
* **Schema names** – schémy, ktoré sa majú zhodovať (zoznam alebo regulárny výraz).
* **Table names** – názvy objektov, ktoré sa majú zhodovať (tabuľka/pohľad/procedúra/trigger), ako zoznam alebo regulárny výraz.
* **Scope** – ktoré typy objektov pravidlo pokrýva (tabuľky, pohľady, procedúry, triggery, …).
* **Role (úroveň prístupu)**
  * **Read** – môže čítať dáta tabuľky.
  * **Update only** – môže aktualizovať riadky; **vkladanie** a **mazanie** nie sú povolené.
  * **Create, update, delete** - môže upravovať riadky bez obmedzení
  * **Run script** – môže spustiť skript, ktorý pracuje s týmto objektom.
    > Poznámka: Ak **nemáte** oprávnenie **„Run script“** na úrovni **databázy**, nemôžete ho použiť na úrovni tabuľky.
  * **Deny** – blokuje prístup k objektu.

