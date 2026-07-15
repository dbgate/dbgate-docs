---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: cs
title: API připojení
weight: 10
---

DbGate podporuje připojení k REST API, GraphQL službám a OData endpointům. Tato API připojení používají stejné vzory rozhraní jako databázová připojení, což vám umožňuje pracovat s API a databázemi v jednotném prostředí.

Podpora API připojení je dostupná v DbGate Premium.

> Hledáte procházení API bez desktopové aplikace? [DbGate Central](/cs/dbgate-central/connecting-to-api-endpoints/) je samostatná hostovaná implementace GraphQL/oData/Shopify připojení, přepracovaná od základu pro prohlížeč.

## GraphQL

GraphQL připojení vám umožňují pracovat s GraphQL API. DbGate poskytuje možnosti introspekce schématu a spouštění dotazů.

### Vytvoření GraphQL připojení

Pro vytvoření GraphQL připojení použijte dialog New Connection a vyberte GraphQL jako typ připojení. Zadejte URL GraphQL endpointu a v případě potřeby nakonfigurujte autentizaci.

### Introspekce schématu

DbGate automaticky zjistí GraphQL schéma včetně dostupných typů, dotazů, mutací a jejich argumentů. Prohlížeč schématu zobrazuje typový systém a umožňuje vám prozkoumat strukturu API.

### Editor dotazů

Editor GraphQL dotazů vám umožňuje psát dotazy a mutace. Pomocí GraphQL exploreru můžete sestavovat dotazy výběrem polí a argumentů ze schématu.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Proměnné

GraphQL dotazy podporují proměnné. Definujte proměnné v panelu proměnných a odkazujte na ně ve svých dotazech pomocí standardní syntaxe GraphQL proměnných. Proměnné lze upravovat ve formuláři nebo jako čisté JSON.

### Prohlížeč odpovědí

Výsledky dotazů se zobrazují ve formátovaném JSON prohlížeči s rozbalitelnou stromovou strukturou. Pokud jsou v odpovědi detekována pole, automaticky se zobrazí tabulkový pohled. V případě potřeby se můžete přepnout zpět na zobrazení čistého JSON.

## OpenAPI (Swagger)

OpenAPI připojení podporují REST API, která poskytují OpenAPI specifikace (verze 2.0 a 3.0).

### Vytvoření OpenAPI připojení

Vytvořte nové připojení a vyberte OpenAPI jako typ připojení. Zadejte URL souboru s OpenAPI specifikací (typicky swagger.json nebo openapi.json). DbGate specifikaci zpracuje a zpřístupní všechny dokumentované endpointy.

### Prohlížeč API dokumentace

Prohlížeč OpenAPI zobrazuje všechny dostupné endpointy uspořádané podle tagů a cest. Pro každý endpoint můžete zobrazit:
- HTTP metodu (GET, POST, PUT, DELETE, PATCH)
- Parametry (path, query, header, body)
- Schémata těla požadavku
- Popisy z dokumentace

### Spuštění požadavku

Vyberte endpoint pro otevření nástroje pro sestavení požadavku. Vyplňte požadované parametry, hlavičky a tělo požadavku. Spuštěním požadavku jej odešlete na API server.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Kontrola odpovědi

Zobrazte stavový kód odpovědi, hlavičky a tělo. JSON odpovědi jsou formátovány a lze je zobrazit ve stromovém i tabulkovém pohledu. Odpovědi, které nejsou ve formátu JSON, se zobrazují jako text.

## OData

OData připojení podporují dotazování OData služeb pomocí standardní syntaxe OData dotazů.

### Vytvoření OData připojení

Vytvořte nové připojení s OData jako typem připojení. Zadejte kořenovou URL OData služby. DbGate načte dokument s metadaty služby.

### Prozkoumávání metadat

Prohlížeč metadat zobrazuje dostupné sady entit, typy entit, vlastnosti a vztahy definované v metadatech služby.

### Spuštění dotazu

OData dotazy podporují standardní volby OData dotazů:
- `$filter` - filtrování entit podle hodnot vlastností
- `$select` - určení, které vlastnosti se mají vrátit
- `$expand` - zahrnutí souvisejících entit
- `$orderby` - řazení výsledků
- `$top` a `$skip` - stránkování
- `$count` - zahrnutí počtu výsledků

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

Výsledky se zobrazují v tabulkovém formátu, podobně jako výsledky databázových dotazů.

## Autentizace

Všechny typy API připojení podporují více metod autentizace:

- **API Key** - zadání názvu a hodnoty klíče, odesílá se jako hlavička nebo parametr dotazu
- **Bearer Token** - OAuth nebo JWT tokeny odesílané v hlavičce Authorization
- **Basic Authentication** - uživatelské jméno a heslo pomocí HTTP Basic Auth
- **No Authentication** - pro veřejná API

Autentizaci nakonfigurujte ve vlastnostech připojení.

## Export dat

Data z API odpovědí lze exportovat do různých formátů pomocí standardní exportní funkcionality DbGate:
- JSON
- CSV
- Excel
- SQL INSERT příkazy
- XML

Použijte standardní volbu "Export" z kontextového menu v tabulkovém prohlížeči dat.

## Práce s více API

Můžete vytvořit připojení k více API a databázím. Otevřete více záložek s požadavky a pracujte s různými endpointy současně.

Stav záložek je zachován po zavření a opětovném otevření aplikace, požadavek můžete znovu otevřít z historie zavřených záložek.
