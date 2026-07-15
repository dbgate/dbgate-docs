---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: sk
title: Prehliadač a editor dát
weight: 5
---

Prehliadač dát je základné zobrazenie DbGate na prezeranie a úpravu údajov v tabuľkách. Otvorte ľubovoľnú tabuľku, pohľad alebo kolekciu a získate rýchlu mriežku podobnú Excelu. Táto stránka sa venuje prehliadaniu, úpravám a navigácii v súvisiacich dátach; syntax filtrovacích výrazov nájdete v časti [Filtrovanie dát](data-filtering).

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## Prehliadanie dát

* **Navigácia klávesnicou** - po mriežke sa pohybujete šípkami, ako v tabuľkovom procesore.
* **Zoradenie** - kliknutím na hlavičku stĺpca zoradíte údaje podľa tohto stĺpca.
* **Filtrovanie** - riadky filtrujete pomocou filtrovacieho riadka nad mriežkou; úplnú syntax výrazov nájdete v časti [Filtrovanie dát](data-filtering).
* **Správca stĺpcov** - vyhľadajte stĺpce podľa názvu a skryte tie, ktoré nepotrebujete.
* **Pokročilé kopírovanie** - skopírujte vybrané bunky ako CSV, YAML, SQL príkazy `INSERT` alebo MongoDB inserty.

## Úprava dát

Úprava dát prebieha priamo v mriežke:

* **Úpravy ako v Exceli** - upravujte bunky priamo na mieste; kopírujte a vkladajte rozsahy riadkov, aj medzi tabuľkami.
* **Pripravené zmeny** - vaše úpravy sa zhromažďujú ako čakajúce zmeny. Skôr než sa dotknú databázy, môžete si prezrieť vygenerovaný SQL skript zmien a potom ich uložiť alebo vrátiť späť.
* **Vkladanie a mazanie riadkov** z mriežky alebo z kontextového menu.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### Makrá editora dát *(Premium)*

Na vybrané bunky použite preddefinované makrá - napríklad zmenu veľkosti písmen, odstránenie diakritiky alebo generovanie UUID.

## Práca so súvisiacimi dátami

DbGate uľahčuje sledovanie vzťahov medzi tabuľkami:

* **Nápovedy vzťahov** - zobrazte textovú hodnotu z odkazovanej tabuľky vedľa číselného cudzieho kľúča.
* **Rozbalenie stĺpca s cudzím kľúčom** - rozbaľte stĺpec s cudzím kľúčom a zobrazte odkazované údaje priamo v mriežke.
* **Otvorenie detailu** - preskočte na odkazovaný riadok cudzieho kľúča.
* **Zobrazenia master/detail** *(Premium)* - preskúmajte súvisiace riadky v prepojenom rozložení master/detail.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## Formulárové zobrazenie

Formulárové zobrazenie ukazuje jeden riadok ako zvislý, „transponovaný“ zoznam - ideálne pre tabuľky s mnohými stĺpcami. Funguje ako stromové zobrazenie, takže stĺpce s cudzími kľúčmi možno rozbaliť a preskúmať súvisiace údaje.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## Zoskupovanie *(Premium)*

V zobrazení mriežky použite zoskupovanie (`GROUP BY`) a agregujte riadky priamo počas prehliadania.

## Súvisiace stránky

* [Filtrovanie dát](data-filtering) - syntax filtrovacích výrazov
* [Export a import](export-import) - presun dát do tabuliek a z nich
* [Perspektívy](perspectives) - vnorené zobrazenia komplexných súvisiacich dát len na čítanie
* [SQL editor](/sk/dbgate/sql-and-queries/sql-editor/) - rovnaký spôsob úpravy výsledkov dotazov *(Premium)*
