---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: cs
title: Administrace
weight: 60
---

Administrační rozhraní umožňuje týmu provozovat DbGate jako sdílenou víceuživatelskou webovou aplikaci: připojení spravujete centrálně, definujete, kdo se může přihlásit a jakým způsobem, a prostřednictvím uživatelů, rolí a oprávnění udělujete jemně odstupňovaný přístup k databázím a objektům. Rovněž zde jsou umístěny sdílené týmové soubory. Vše, co je zde nakonfigurováno, se ukládá do úložné databáze, nikoli do lokálních souborů.

Administrační nástroj je k dispozici pouze v edici Team Premium. V edici Community prosím konfigurujte DbGate pomocí [proměnných prostředí](/cs/dbgate/customization/env-variables).

Veškerá konfigurace z administrace se ukládá do úložné databáze - k její konfiguraci použijte [proměnné prostředí STORAGE_xxx](/cs/dbgate/customization/env-variables/#team-premium-edition-configuration).

V této sekci:

* [Autentizace](auth) - konfigurace způsobů přihlášení a poskytovatelů identity
* [Připojení](connection) - správa připojení dostupných vašemu týmu
* [Týmové soubory](team-files) - sdílení SQL skriptů, ER diagramů a grafů
* [Uživatelé](users) - správa uživatelských účtů
* [Role](roles) - seskupení oprávnění do rolí
* [Oprávnění](permissions) - udělení přístupu k připojením, databázím a tabulkám

## Přístup administrátora

Administrační stránka je dostupná na URL https://your_dbgate_instance/admin.html . 

Kořenový administrátor by měl mít definované heslo. Můžete nastavit proměnnou prostředí ADMIN_PASSWORD. Pokud tato proměnná není definována, DbGate se na administrátorské heslo zeptá při prvním spuštění.

Následně můžete přidat administrační oprávnění jinému uživateli s jinou metodou autentizace, ale nejprve musíte otevřít tuto administrační stránku.

