---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: sk
title: Vývoj pluginov
weight: 30
---

DbGate podporuje vytváranie pluginov. Vďaka sprievodcovi pluginmi je naozaj jednoduché vytvoriť základný plugin. Pluginy DbGate sú NPM (JavaScript) balíky, môžu mať závislosti. (ale nie natívne závislosti)

Momentálne existujú 3 typy pluginov:
- Plugin s témou
- Plugin formátu súboru
- Plugin databázového ovládača

## Inštalácia prerekvizít
Potrebujete mať nainštalovaný [node.js](https://nodejs.org). 

Ďalej budete potrebovať [Yeoman](https://yeoman.io/) a yeoman [generátor pluginov DbGate](https://www.npmjs.com/package/generator-dbgate):

```sh
npm install -g yo
npm install -g generator-dbgate
```

## Vytvorenie pluginu
Spustite v konzole nasledujúci príkaz:

```sh
yo dbgate
```

Musíte odpovedať na 3 otázky:
- Názov pluginu, musí začínať na dbgate-plugin-, napr. dbgate-plugin-myplugin
- Typ pluginu, zvoľte napr. "Database driver"
- Správca balíkov, zvoľte npm alebo yarn, podľa toho, čo preferujete. DbGate používa yarn.

## Úprava a testovanie pluginu
Otvorte nejaký editor, odporúčanou možnosťou je [Visual Studio Code](https://code.visualstudio.com/)  . 
Plugin s témou obsahuje iba jeden zdrojový súbor, src/index.js. Farby témy môžete upraviť podľa vlastného uváženia. Atribút themeName je názov, ktorý sa zobrazuje vo výbere tém v DbGate.

Keď si chcete pozrieť svoju novú tému, spustite toto z konzoly (z adresára pluginu):
```sh
yarn plugin
```
alebo ak používate npm, tak
```sh
npm run plugin
```
Tento príkaz nainštaluje váš plugin do lokálne nainštalovanej inštancie DbGate (alebo ho aktualizuje, keď urobíte zmeny). Po reštarte DbGate by ste mali vidieť novú tému.  
Reštart nie je nutný, na použitie novej verzie pluginu po spustení "yarn plugin" stačí znovu načítať aplikáciu (menu View/Reload)

## Odstránenie pluginu
Plugin môžete odinštalovať z widgetu pluginov v DbGate. Alebo pomocou nasledujúceho príkazu:
```sh
yarn plugout
```

## Publikovanie pluginu
Plugin je bežný NPM balík, môžete ho publikovať do NPM repozitára. Po publikovaní bude dostupný pre všetkých používateľov DbGate vo widgete "Plugins".

## Ikona pluginu
Každý plugin je v zozname rozšírení reprezentovaný ikonou. NPM nepodporuje ikony pre NPM balíky, takže ikona môže byť v poli description v súbore package.json s nasledujúcou syntaxou:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Ak použijete generátor yeoman, trochu vám s tým pomôže.

## Vytvorenie pluginu databázového ovládača
Vytvorenie pluginu ovládača je veľmi podobné vytváraniu, len zvolíte "Database driver plugin". Po `yarn plugin` by ste mali byť schopní definovať pripojenie pomocou vášho nového ovládača a vidieť fiktívny zoznam databáz a zoznam tabuliek.

Jednoduchý ovládač so základnou funkcionalitou môžete vytvoriť veľmi rýchlo, zložitejšie funkcie je možné implementovať neskôr.

Vytvorenie ovládača môže pozostávať z nasledujúcich krokov:
* nájdite vhodný nodejs balík (ovládač). Ak je to možné, zvoľte čisto JavaScriptový balík. Natívne balíky sú veľká komplikácia, takýto natívny balík musí byť pridaný do distribúcie DbGate a tiež môžete očakávať problémy so zostavením na rôznych platformách. Na druhej strane čisto JavaScriptové balíky fungujú normálne bez problémov na všetkých platformách, bez nutnosti meniť DbGate.
* definujte polia pre pripojenie vo frontend/driver.js, funkcia showConnectionField
* implementujte funkciu connect v backend/driver.js 
* implementujte funkciu getVersion v backend/driver.js (voliteľné, ale keď to urobíte, môžete pripojenie otestovať tlačidlom "Test" na karte pripojenia)
* implementujte metódu _rynAnalysis v triede backend/Analyser.js. Táto metóda by mala vrátiť štruktúru databázy.
* implementujte metódu query v backend/driver.js. Potom by ste mali byť schopní zobraziť zoznam tabuliek a prehliadať dáta tabuliek
* implementujte ostatné metódy. Ako inšpiráciu použite prosím iné pluginy ovládačov, najtypickejším pluginom je pravdepodobne PostgreSQL plugin, https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
