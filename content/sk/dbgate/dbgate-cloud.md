---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: sk
title: DbGate Cloud
weight: 80
---

DbGate cloud je online úložisko pre vaše pripojenia, SQL skripty a ďalšie objekty. Zároveň ponúka verejnú znalostnú databázu užitočných SQL skriptov.

> DbGate Cloud je úložný doplnok pre **desktopovú** aplikáciu DbGate (pripojenia, SQL skripty, zdieľané priečinky). Hľadáte namiesto toho hostovanú aplikáciu bežiacu iba v prehliadači? Pozrite si [DbGate Central](/sk/dbgate-central/).

## Prihlásenie
Na používanie DbGate cloudu je potrebné sa prihlásiť. Použite ikonu {{< mdi "account-remove-outline" >}} v ľavom paneli.

Vaše cloudové úložisko je vždy spojené s vašou e-mailovou adresou.  
Môžete si vybrať jedného z nasledujúcich poskytovateľov overenia:
* GMail
* GitHub
* E-mail - na váš e-mail bude odoslaný jednorazový prihlasovací magic link

Servery DbGate neukladajú vaše heslo.

## Používanie pripojení uložených v cloude
Váš cloudový obsah sa po prihlásení zobrazí vo widgete {{< mdi "cloud-key" >}}. Predvolene vidíte svoj priečinok Private (s právom na zápis).

Uloženie pripojenia do cloudu:
* Kontextové menu pripojenia, zvoľte "Copy to cloud folder"
* Kliknite na {{<mdi "plus-thick" >}} a potom zvoľte "Add connection on cloud"

## Ktoré pripojenie je uložené v cloude?
* Vaše cloudové pripojenia sú vždy vo widgete {{< mdi "cloud-key" >}}
* Vaše lokálne uložené pripojenia sú vo widgete {{< mdi "database" >}}

## Práca s priečinkami
Okrem priečinka Private môžete vytvárať ďalšie priečinky (je potrebná edícia Premium).

Pod tlačidlom {{<mdi "plus-thick" >}} sú príkazy:
* New shared folder - vytvorí nový zdieľaný priečinok. Predvolene je prístupný iba vám, môžete pozvať ďalších používateľov
* Add existing shared folder - ak máte pozývací odkaz na nejaký zdieľaný priečinok (vytvorený iným používateľom), toto je správne miesto na jeho použitie

Ak chcete svoj priečinok zdieľať s ďalšími ľuďmi, kliknite pravým tlačidlom na priečinok a zvoľte "Copy invite link"

## Oprávnenia zdieľaného priečinka
* Admin - máte plný prístup k priečinku, môžete pozývať ďalších ľudí a zapisovať obsah
* Write - môžete zapisovať/mazať obsah, ale nemôžete pozývať ďalších ľudí
* Read - iba čítanie obsahu priečinka. Majte na pamäti, že toto oprávnenie sa nevzťahuje na databázy dostupné v rámci pripojenia definovaného na server

## Zdieľané priečinky v edícii Community
V edícii Community môžete používať zdieľané priečinky vytvorené používateľmi edície Premium, ale nemôžete vytvárať vlastné zdieľané priečinky. Cieľom je umožniť tímom s edíciou Premium zdieľať pripojenia, SQL súbory a ER diagramy s ďalšími členmi tímu, ktorí používajú edíciu Community.

## Verejná znalostná databáza
Verejná znalostná databáza je zbierka užitočných SQL skriptov a grafov pre úlohy ako ladenie výkonu SQL, analýza deadlockov, využitie indexov atď... Znalostná databáza je dostupná vo všetkých edíciách, ale grafy sú dostupné iba v edíciách Premium.

Všetky položky uvidíte pod ikonou {{< mdi "cloud-search" >}} v ľavom paneli widgetov.  
Sivo zobrazené skripty označujú skripty, ktoré nie sú kompatibilné s aktuálne vybranou databázou.

Ak by ste chceli rozšíriť znalostnú databázu o svoje SQL skripty, vytvorte prosím pull request do GIT repozitára [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base).

Skripty v znalostnej databáze sú anotované syntaxou [SQL front matter](/sk/dbgate/developer/sql-front-matter)

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)
