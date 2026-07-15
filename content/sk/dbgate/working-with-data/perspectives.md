---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: sk
title: Perspektívy
weight: 50
---

Perspektíva je pohľad na komplexné vnorené dáta určený len na čítanie. Pripomína zostavy, ale perspektívy sa vytvárajú jednoducho pridávaním dát do pohľadu. Môžete použiť návrhára perspektív, ktorý umožňuje spájať dáta aj podľa iných vzťahov než cudzích kľúčov.

Perspektívy dokážu ľahko spájať dáta a zobrazovať skupiny.

<!-- ![screenshot](/screenshots/perspective1.png) -->

## Vytvorenie perspektívy
Perspektívy je možné vytvárať zo SQL tabuliek a pohľadov (kolekcie MongoDB zatiaľ nie sú podporované, ale táto podpora sa plánuje).
Použite kontextové menu tabuľky/pohľadu, "Open perspective".

![screenshot](/img/perspective-create.png)

DbGate otvorí jednoduchú perspektívu, v ktorej je zobrazený iba jeden stĺpec. Tento stĺpec je vybraný heuristickým algoritmom tak, aby čo najlepšie reprezentoval celý riadok.
## Prispôsobenie perspektívy
Môžete určiť, ktoré stĺpce sú v pohľade dostupné. Takisto môžete do pohľadu pridať odkazované dáta. Na prechádzanie stromu odkazov použite tlačidlo rozbalenia.

## Filtrovanie dát
Použite kontextové menu v tabuľke alebo v zozname stĺpcov na ľavej strane, "Add to filter". Môžete použiť rovnaké filtrovacie výrazy ako na iných miestach v DbGate. Prípadne môžete na bunke tabuľky použiť príkaz kontextového menu "Filter this value".

## Filtrovanie nadradených riadkov
Predpokladajme nasledujúcu perspektívu. Máme vzťah master/detail, Genre so súvisiacimi skladbami (Track). Chceme filtrovať podľa Track (skúsil som vyhľadať text "mix").

![screenshot](/img/parentrows1.png)

Ako vidíte, je tu množstvo riadkov Genre bez akejkoľvek skladby vyhovujúcej kritériám vyhľadávania. Ak chcete filtrovať aj riadky Genre, použite príkaz "Filter parent rows" v kontextovom menu hlavičky tabuľky. Takisto môžete použiť prepínacie tlačidlo vo filtrovacom riadku.

![screenshot](/img/parentrows2.png)

## Definovanie vlastných spojení
Perspektívy fungujú veľmi dobre s cudzími kľúčmi. Túto funkciu však môžete použiť aj vtedy, keď máte databázu bez cudzích kľúčov. Je možné definovať vlastné spojenie s ľubovoľnou podmienkou. Môžete dokonca definovať vlastné spojenie do inej databázy (ktorá môže byť na inom databázovom serveri, dokonca s odlišným databázovým strojom).

![screenshot](/img/customjoin.png)

Vzťah spojenia môžete vytvoriť aj presunutím stĺpcov metódou drag &amp; drop.

![screenshot](/img/customjoin2.png)
