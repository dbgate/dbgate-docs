---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: sk
title: Vlastné témy
weight: 10
---

DbGate má flexibilnú podporu tém. Môžete si vytvoriť vlastnú tému a zmeniť farby rôznych prvkov používateľského rozhrania.

Témy sa vytvárajú ako súbory JSON. Najjednoduchší spôsob, ako vytvoriť vlastnú tému, je použiť AI asistenta pre témy.

## AI asistent pre témy
Ak chcete vyvolať AI asistenta pre témy, otvorte Settings/Themes a potom kliknite na tlačidlo „Customize with AI assistant“.

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

AI asistent pre témy prispôsobí vašu tému podľa vašich pokynov. Môžete určiť, ktoré farby chcete zmeniť a ako. Napríklad môžete povedať „Make primary color green, and background color dark gray“.

![screenshot](/screenshots/dbgate-green.png)

Generovanie témy pomocou AI asistenta trvá niekoľko minút, generuje sa približne 280 premenných. Po vygenerovaní témy môžete kliknúť na tlačidlo „Apply Theme“ a novú tému použiť. Môžete tiež použiť tlačidlo „Save theme“ na uloženie témy ako súboru JSON. Všetky uložené témy sú potom dostupné vo výbere tém. Témy môžete tiež spravovať (premenovať, upraviť, odstrániť) vo widgete súborov {{< mdi "file" >}}.

## Zdieľanie tém v DbGate Cloud
Svoje témy môžete zdieľať s ostatnými používateľmi DbGate prostredníctvom DbGate Cloud. Ak chcete tému zdieľať, vytvorte pull request v [repozitári znalostnej bázy DbGate](https://github.com/dbgate/dbgate-knowledge-base). Témy sú uložené v adresári folder-Themes. Príklady nájdete v existujúcich témach. Stačí skopírovať súbor JSON s vašou témou do tohto adresára a vytvoriť pull request. Po zlúčení vášho pull requestu bude vaša téma dostupná pre všetkých používateľov DbGate vo výbere tém.
