---
sourceHash: ff92448ee8e00aae1c7fc20030ddea3637a2e8c7952daeac5c129c5fbb48e420
language: sk
title: BI reporty z dát API
weight: 40
---

DbGate Central načíta vaše odpovede API do svojho vlastného vstavaného dátového enginu, takže ich môžete kombinovať, agregovať a vizualizovať - a premeniť tak surové odpovede API na prehľadné BI reporty.

## Od surových odpovedí k poznatkom

* **Agregujte a pivotujte** svoje dáta do súhrnných tabuliek - počty, súčty a rozpady podľa ľubovoľnej dimenzie.
* **Prepojte viacero zdrojov**, aby report mohol spojiť dáta, ktoré sa nachádzajú za rôznymi endpointmi.
* **Prejdite do detailu** cez hierarchie a posuňte sa od celkového pohľadu k jednotlivým riadkom.

Ako BI zdroje je možné použiť oData a Shopify endpointy (a súbory CSV/JSON/Excel). GraphQL API sú skvelé na dopytovanie, ale momentálne nie sú dostupné ako zdroj pre reporty - namiesto toho ich prehliadajte a dopytujte priamo (pozri [Dopytovanie GraphQL API](../querying-graphql-apis)).

## Zdieľanie reportu

Reporty je možné **publikovať** ako samostatný zobrazovací pohľad iba na čítanie. Ktokoľvek s odkazom vidí živé dáta a môže prechádzať do detailu, bez účtu a bez prístupu k vášmu pripojeniu.

![DbGate Central - turn API data into a report](https://lite.dbgate.io/screenshots/central-bi-dark.png)
