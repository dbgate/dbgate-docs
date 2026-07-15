---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: sk
title: Administrácia
weight: 60
---

Administračné rozhranie umožňuje tímu prevádzkovať DbGate ako zdieľanú webovú aplikáciu pre viacerých používateľov: pripojenia spravujete centrálne, definujete, kto sa môže prihlásiť a akým spôsobom, a prostredníctvom používateľov, rolí a oprávnení udeľujete jemne odstupňovaný prístup k databázam a objektom. Hostuje tiež zdieľané tímové súbory. Všetko, čo sa tu nakonfiguruje, sa ukladá do úložnej databázy, nie do lokálnych súborov.

Administračný nástroj je dostupný len v edícii Team Premium. V edícii Community nakonfigurujte DbGate pomocou [premenných prostredia](/sk/dbgate/customization/env-variables).

Celá konfigurácia z administrácie sa ukladá do úložnej databázy - na jej nastavenie použite [premenné prostredia STORAGE_xxx](/sk/dbgate/customization/env-variables/#team-premium-edition-configuration).

V tejto sekcii:

* [Autentifikácia](auth) - konfigurácia spôsobov prihlásenia a poskytovateľov identity
* [Pripojenia](connection) - správa pripojení dostupných pre váš tím
* [Tímové súbory](team-files) - zdieľanie SQL skriptov, ER diagramov a grafov
* [Používatelia](users) - správa používateľských účtov
* [Role](roles) - zoskupenie oprávnení do rolí
* [Oprávnenia](permissions) - udeľovanie prístupu k pripojeniam, databázam a tabuľkám

## Prístup administrátora

Administračná stránka je dostupná na adrese https://your_dbgate_instance/admin.html . 

Hlavný administrátor by mal mať definované heslo. Môžete nastaviť premennú prostredia ADMIN_PASSWORD. Ak táto premenná nie je definovaná, DbGate sa na administrátorské heslo spýta pri prvom spustení.

Následne môžete pridať administrátorské oprávnenie inému používateľovi s iným spôsobom autentifikácie, ale najprv musíte otvoriť túto administračnú stránku.
