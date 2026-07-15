---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: cs
title: DbGate Cloud
weight: 80
---

DbGate cloud je online úložiště pro vaše připojení, SQL skripty a další objekty. Nabízí také veřejnou znalostní bázi užitečných SQL skriptů.

> DbGate Cloud je úložný doplněk pro **desktopovou** aplikaci DbGate (připojení, SQL skripty, sdílené složky). Hledáte místo toho hostovanou aplikaci běžící pouze v prohlížeči? Podívejte se na [DbGate Central](/cs/dbgate-central/).

## Přihlášení
Pro používání DbGate cloudu je nutné se přihlásit. Použijte ikonu {{< mdi "account-remove-outline" >}} v levém panelu.

Vaše cloudové úložiště je vždy spojeno s vaší e-mailovou adresou.  
Můžete si vybrat jednoho z následujících poskytovatelů ověření:
* GMail
* GitHub
* E-mail - na váš e-mail bude zaslán jednorázový přihlašovací magic link

Servery DbGate neukládají vaše heslo.

## Používání připojení uložených v cloudu
Váš cloudový obsah se po přihlášení zobrazí ve widgetu {{< mdi "cloud-key" >}}. Ve výchozím nastavení vidíte svou složku Private (s právem zápisu).

Uložení připojení do cloudu:
* Kontextové menu připojení, zvolte "Copy to cloud folder"
* Klikněte na {{<mdi "plus-thick" >}} a zvolte "Add connection on cloud"

## Které připojení je uloženo v cloudu?
* Vaše cloudová připojení jsou vždy ve widgetu {{< mdi "cloud-key" >}}
* Vaše lokálně uložená připojení ve widgetu {{< mdi "database" >}}

## Práce se složkami
Kromě své složky Private můžete vytvářet další složky (je potřeba edice Premium).

Pod tlačítkem {{<mdi "plus-thick" >}} jsou k dispozici příkazy:
* New shared folder - vytvoří novou sdílenou složku. Ve výchozím nastavení je přístupná pouze vám, můžete pozvat další uživatele
* Add existing shared folder - pokud máte pozvánkový odkaz na nějakou sdílenou složku (vytvořenou jiným uživatelem), toto je správné místo, kde jej použít

Pokud chcete svou složku sdílet s dalšími lidmi, klikněte na složku pravým tlačítkem a zvolte "Copy invite link"

## Oprávnění sdílených složek
* Admin - máte plný přístup ke složce, můžete pozvat další lidi a zapisovat obsah
* Write - Můžete zapisovat/mazat obsah, ale nemůžete pozvat další lidi
* Read - pouze čtení obsahu složky. Mějte prosím na paměti, že toto oprávnění se nevztahuje na databáze dostupné uvnitř připojení definovaného na server

## Sdílené složky v edici Community
V edici Community můžete používat sdílené složky vytvořené uživateli edice Premium, ale nemůžete vytvářet vlastní sdílené složky. Cílem je umožnit týmům s edicí Premium sdílet připojení, SQL soubory a ER diagramy s ostatními členy týmu s edicí Community.

## Veřejná znalostní báze
Veřejná znalostní báze je kolekce užitečných SQL skriptů a grafů pro úlohy jako ladění výkonu SQL, analýza deadlocků, využití indexů atd... Znalostní báze je dostupná ve všech edicích, ale grafy jsou dostupné pouze v edicích Premium.

Všechny položky uvidíte pod ikonou {{< mdi "cloud-search" >}} v levém panelu widgetů.  
Šedě zobrazené skripty označují skripty, které nejsou kompatibilní s aktuálně zvolenou databází.

Pokud byste chtěli znalostní bázi rozšířit o své SQL skripty, vytvořte prosím pull request do GIT repozitáře [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base).

Skripty ve znalostní bázi jsou anotovány syntaxí [SQL front matter](/cs/dbgate/developer/sql-front-matter)

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)
