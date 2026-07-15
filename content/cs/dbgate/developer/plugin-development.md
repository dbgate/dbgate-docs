---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: cs
title: Vývoj pluginů
weight: 30
---

DbGate podporuje vytváření pluginů. Díky průvodci vytvořením pluginu je opravdu jednoduché vytvořit základní plugin. Pluginy DbGate jsou NPM (JavaScript) balíčky, mohou mít závislosti. (ale ne nativní závislosti)

Nyní existují 3 typy pluginů:
- Plugin s tématem vzhledu
- Plugin pro formát souboru
- Plugin s databázovým ovladačem

## Instalace nezbytných nástrojů
Musíte mít nainstalovaný [node.js](https://nodejs.org). 

Dále budete potřebovat [Yeoman](https://yeoman.io/) a yeoman [generátor pluginů DbGate](https://www.npmjs.com/package/generator-dbgate):

```sh
npm install -g yo
npm install -g generator-dbgate
```

## Vytvoření pluginu
Spusťte v konzoli následující příkaz:

```sh
yo dbgate
```

Musíte odpovědět na 3 otázky:
- Název pluginu, musí začínat na dbgate-plugin-, např. dbgate-plugin-myplugin
- Typ pluginu, zvolte např. "Database driver"
- Správce balíčků, zvolte npm nebo yarn, podle toho, co preferujete. DbGate používá yarn.

## Úprava a testování pluginu
Otevřete nějaký editor, doporučenou volbou je [Visual Studio Code](https://code.visualstudio.com/)  . 
Plugin s tématem vzhledu obsahuje pouze jeden zdrojový soubor, src/index.js. Barvy tématu můžete upravit podle svého přání. Atribut themeName je název, který se zobrazuje ve výběru témat v DbGate.

Když si chcete své nové téma prohlédnout, spusťte toto z konzole (z adresáře pluginu):
```sh
yarn plugin
```
nebo pokud používáte npm, tak
```sh
npm run plugin
```
Tento příkaz nainstaluje váš plugin do lokálně nainstalované instance DbGate (nebo jej aktualizuje, když provedete změny). Po restartu DbGate byste měli vidět nové téma.  
Restart není nutný, k použití nové verze pluginu po spuštění "yarn plugin" stačí znovunačtení aplikace (menu View/Reload)

## Odebrání pluginu
Plugin můžete odinstalovat z widgetu pluginů v DbGate. Nebo pomocí následujícího příkazu:
```sh
yarn plugout
```

## Publikování pluginu
Plugin je běžný NPM balíček, můžete jej publikovat do NPM repozitáře. Po publikování bude dostupný všem uživatelům DbGate ve widgetu "Plugins".

## Ikona pluginu
Každý plugin je v seznamu rozšíření reprezentován ikonou. NPM nepodporuje ikony pro NPM balíčky, takže ikona může být v poli description v souboru package.json s následující syntaxí:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Pokud použijete yeoman generátor, trochu vám s tímto pomůže.

## Vytvoření pluginu s databázovým ovladačem
Vytvoření pluginu s ovladačem je velmi podobné vytvoření pluginu, pouze zvolíte "Database driver plugin". Po `yarn plugin` byste měli být schopni definovat připojení pomocí svého nového ovladače a vidět fiktivní seznam databází a seznam tabulek.

Jednoduchý ovladač se základní funkcionalitou můžete vytvořit velmi rychle, složitější funkce lze implementovat později.

Vytvoření ovladače může sestávat z následujících kroků:
* najděte vhodný nodejs balíček (ovladač). Pokud je to možné, zvolte čistě JavaScriptový balíček. Nativní balíčky jsou velká komplikace, takový nativní balíček musí být přidán do distribuce DbGate a také můžete očekávat problémy se sestavením na různých platformách. Na druhou stranu čistě JavaScriptové balíčky fungují normálně bez problémů na všech platformách, bez nutnosti měnit DbGate.
* definujte pole pro připojení ve frontend/driver.js, funkce showConnectionField
* implementujte funkci connect v backend/driver.js 
* implementujte funkci getVersion v backend/driver.js (volitelné, ale když je hotová, můžete nyní otestovat připojení tlačítkem "Test" na záložce připojení)
* implementujte metodu _rynAnalysis ve třídě backend/Analyser.js. Tato metoda by měla vracet strukturu databáze.
* implementujte metodu query v backend/driver.js. Poté byste měli být schopni zobrazit seznam tabulek a procházet data tabulek
* implementujte ostatní metody. Pro inspiraci prosím použijte jiné pluginy s ovladači, nejtypičtějším pluginem je pravděpodobně plugin PostgreSQL, https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
