---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: cs
title: Oprávnění
weight: 50
---

Oprávnění v DbGate používají **dvě dimenze**:

1. **Zdroj oprávnění (kdo je nastavuje)**
   Oprávnění se kaskádovitě šíří od obecných ke konkrétním. Konkrétnější nastavení přepisují ta obecnější:
   * Předdefinované sady oprávnění
   * Předdefinované role (*superadmin*, *přihlášený uživatel*, *anonymní*)
   * Vlastní role
   * Jednotlivý uživatel

2. **Rozsah objektů**
   Oprávnění mohou cílit na konkrétní **databáze** a **tabulky/objekty**. Viz **[Oprávnění k databázím](#database-permissions)** a **[Oprávnění k tabulkám](#table-permissions)**.

---

## Základní oprávnění

Globální/základní oprávnění nastavíte ve **stromu oprávnění** v **Detailu uživatele** nebo **Detailu role**.

* **Šedě zobrazené** zaškrtávací políčko znamená, že oprávnění je **zděděné** (např. z role nebo z předdefinované sady oprávnění), nikoli nastavené přímo na daném uživateli/roli.

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## Oprávnění k databázím

Oprávnění na úrovni databáze nastavíte na kartě **Databases** (jak v Detailu role, tak v Detailu uživatele).

> **Důležité:** Pravidla pro databáze se uplatní **pouze tehdy**, když je v základních oprávněních odškrtnuto oprávnění **„All databases“**.

* Každý řádek v tabulce pravidel povoluje nebo zakazuje přístup k databázím, které **odpovídají** filtrům daného řádku.
* **Na pořadí pravidel záleží**: pravidla **níže** v seznamu **přepisují** pravidla nad nimi.

![Database permissions - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**Sloupce**

* **Connection** – na které připojení se pravidlo vztahuje.
* **Database names** – databáze, které se mají porovnávat (seznam názvů nebo regulární výraz).
* **Role (úroveň přístupu)**
  * **View** – může vidět databázi, ale ne její tabulky/pohledy/atd.
  * **Read content** – přístup pouze pro čtení obsahu databáze.
  * **Write data** – může měnit data v tabulkách.
  * **Run script** – může spouštět libovolný SQL skript; může vytvářet/mazat/měnit objekty.
  * **Deny** – blokuje přístup k databázi.

---

## Oprávnění k tabulkám

Oprávnění na úrovni tabulek/objektů nastavíte na kartě **Tables / Views / Objects** (v Detailu role a Detailu uživatele).

> **Důležité:** Pravidla pro tabulky/objekty se uplatní **pouze tehdy**, když je v základních oprávněních odškrtnuto oprávnění **„All tables/views/objects“**.

* Každý řádek definuje přístup k tabulkám/objektům, které **odpovídají** filtrům.
* **Na pořadí pravidel záleží**: pravidla **níže** v seznamu **přepisují** pravidla nad nimi.
* Ve výchozím nastavení se oprávnění k tabulkám **dědí z oprávnění k databázi**.

**Sloupce**

* **Connection** – na které připojení se pravidlo vztahuje.
* **Database names** – databáze, které se mají porovnávat (seznam nebo regulární výraz).
* **Schema names** – schémata, která se mají porovnávat (seznam nebo regulární výraz).
* **Table names** – názvy objektů, které se mají porovnávat (tabulka/pohled/procedura/trigger), jako seznam nebo regulární výraz.
* **Scope** – které typy objektů pravidlo pokrývá (tabulky, pohledy, procedury, triggery, …).
* **Role (úroveň přístupu)**
  * **Read** – může číst data tabulky.
  * **Update only** – může aktualizovat řádky; **vkládání** a **mazání** není povoleno.
  * **Create, update, delete** - může upravovat řádky bez omezení
  * **Run script** – může spustit skript, který pracuje s tímto objektem.
    > Poznámka: Pokud **nemáte** oprávnění **„Run script“** na úrovni **databáze**, nemůžete jej použít na úrovni tabulky.
  * **Deny** – blokuje přístup k objektu.

