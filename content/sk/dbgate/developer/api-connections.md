---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: sk
title: API pripojenia
weight: 10
---

DbGate podporuje pripojenia k REST API, službám GraphQL a koncovým bodom OData. Tieto API pripojenia využívajú rovnaké vzory rozhrania ako databázové pripojenia, čo vám umožňuje pracovať s API a databázami v jednotnom prostredí.

Podpora API pripojení je dostupná v DbGate Premium.

> Hľadáte prehliadanie API bez desktopovej aplikácie? [DbGate Central](/sk/dbgate-central/connecting-to-api-endpoints/) je samostatná, hostovaná implementácia pripojení GraphQL/oData/Shopify, prepracovaná od základov pre prehliadač.

## GraphQL

Pripojenia GraphQL vám umožňujú komunikovať s GraphQL API. DbGate poskytuje možnosti introspekcie schémy a spúšťania dotazov.

### Vytvorenie pripojenia GraphQL

Ak chcete vytvoriť pripojenie GraphQL, použite dialóg New Connection a vyberte GraphQL ako typ pripojenia. Zadajte URL koncového bodu GraphQL a v prípade potreby nakonfigurujte autentifikáciu.

### Introspekcia schémy

DbGate automaticky zistí schému GraphQL vrátane dostupných typov, dotazov, mutácií a ich argumentov. Prehliadač schémy zobrazuje typový systém a umožňuje vám preskúmať štruktúru API.

### Editor dotazov

Editor dotazov GraphQL vám umožňuje písať dotazy a mutácie. Pomocou prieskumníka GraphQL môžete zostavovať dotazy výberom polí a argumentov zo schémy.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Premenné

Dotazy GraphQL podporujú premenné. Definujte premenné v paneli premenných a odkazujte sa na ne vo svojich dotazoch pomocou štandardnej syntaxe premenných GraphQL. Premenné je možné upravovať vo formulári alebo ako čistý JSON.

### Prehliadač odpovedí

Výsledky dotazov sa zobrazujú vo formátovanom prehliadači JSON s rozbaliteľnou stromovou štruktúrou. Ak sa v odpovedi zistia polia, automaticky sa zobrazí tabuľkové zobrazenie. V prípade potreby sa môžete prepnúť späť na zobrazenie čistého JSON.

## OpenAPI (Swagger)

Pripojenia OpenAPI podporujú REST API, ktoré poskytujú špecifikácie OpenAPI (verzie 2.0 a 3.0).

### Vytvorenie pripojenia OpenAPI

Vytvorte nové pripojenie a vyberte OpenAPI ako typ pripojenia. Zadajte URL k súboru so špecifikáciou OpenAPI (zvyčajne swagger.json alebo openapi.json). DbGate špecifikáciu spracuje a sprístupní všetky zdokumentované koncové body.

### Prehliadač dokumentácie API

Prehliadač OpenAPI zobrazuje všetky dostupné koncové body usporiadané podľa značiek a ciest. Pre každý koncový bod si môžete zobraziť:
- HTTP metódu (GET, POST, PUT, DELETE, PATCH)
- Parametre (cesta, dotaz, hlavička, telo)
- Schémy tela požiadavky
- Popisy dokumentácie

### Spustenie požiadavky

Vyberte koncový bod a otvorí sa nástroj na zostavenie požiadavky. Vyplňte požadované parametre, hlavičky a telo požiadavky. Spustením požiadavky ju odošlete na server API.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Kontrola odpovede

Zobrazte si stavový kód odpovede, hlavičky a telo. Odpovede vo formáte JSON sú naformátované a je možné ich zobraziť v stromovom aj tabuľkovom zobrazení. Odpovede, ktoré nie sú vo formáte JSON, sa zobrazujú ako text.

## OData

Pripojenia OData podporujú dotazovanie služieb OData pomocou štandardnej syntaxe dotazov OData.

### Vytvorenie pripojenia OData

Vytvorte nové pripojenie s typom pripojenia OData. Zadajte koreňovú URL služby OData. DbGate načíta dokument s metadátami služby.

### Preskúmanie metadát

Prehliadač metadát zobrazuje dostupné množiny entít, typy entít, vlastnosti a vzťahy definované v metadátach služby.

### Spúšťanie dotazov

Dotazy OData podporujú štandardné možnosti dotazov OData:
- `$filter` - filtrovanie entít podľa hodnôt vlastností
- `$select` - určenie, ktoré vlastnosti sa majú vrátiť
- `$expand` - zahrnutie súvisiacich entít
- `$orderby` - zoradenie výsledkov
- `$top` a `$skip` - stránkovanie
- `$count` - zahrnutie počtu výsledkov

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

Výsledky sa zobrazujú v tabuľkovom formáte, podobne ako výsledky databázových dotazov.

## Autentifikácia

Všetky typy API pripojení podporujú viacero metód autentifikácie:

- **API Key** - zadajte názov a hodnotu kľúča, odosiela sa ako hlavička alebo parameter dotazu
- **Bearer Token** - tokeny OAuth alebo JWT odosielané v hlavičke Authorization
- **Basic Authentication** - používateľské meno a heslo pomocou HTTP Basic Auth
- **No Authentication** - pre verejné API

Autentifikáciu nakonfigurujte vo vlastnostiach pripojenia.

## Export údajov

Údaje z odpovedí API je možné exportovať do rôznych formátov pomocou štandardnej funkcie exportu v DbGate:
- JSON
- CSV
- Excel
- SQL príkazy INSERT
- XML

Použite štandardnú možnosť "Export" v kontextovom menu v tabuľkovom prehliadači údajov.

## Práca s viacerými API

Môžete vytvoriť pripojenia k viacerým API a databázam. Otvorte viacero kariet s požiadavkami a pracujte s rôznymi koncovými bodmi súčasne.

Stav kariet sa zachová po zatvorení a opätovnom otvorení aplikácie, požiadavku môžete znova otvoriť z histórie zatvorených kariet.
