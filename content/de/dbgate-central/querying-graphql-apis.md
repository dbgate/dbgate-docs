---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: de
title: GraphQL-APIs abfragen
weight: 20
---

Richten Sie DbGate Central auf eine beliebige GraphQL-API und es erkennt, was verfügbar ist - Sie müssen sich nicht durch separate Dokumentationen wühlen.

## Das Schema erkunden

DbGate Central führt eine Introspektion des GraphQL-Schemas durch, sobald Sie sich verbinden. Durchsuchen Sie die verfügbaren Typen und Felder im Baum und öffnen Sie dann einen Abfrage-Tab, um mit der Arbeit zu beginnen.

## Abfragen ausführen

* Schreiben Sie Abfragen mit dem GraphQL-Editor und führen Sie sie gegen die Live-API aus.
* Übergeben Sie Abfragevariablen zusammen mit der Abfrage, entweder in einem Formular oder als reines JSON.
* Die Ergebnisse werden in demselben schnellen, sortier- und filterbaren Raster zurückgegeben, das überall in DbGate verwendet wird, sodass sich eine GraphQL-Antwort wie eine Datenbanktabelle anfühlt.
* Verschachtelte Objekte und Listen werden als strukturiertes JSON zurückgegeben, das Sie direkt aufklappen und untersuchen können.

Abgefragte Ansichten werden pro Verbindung zwischengespeichert, sodass ihr erneutes Öffnen sofort erfolgt, während Sie weiterarbeiten.

> GraphQL-Verbindungen in DbGate Central sind eine separate, browserbasierte Implementierung, die sich von der [GraphQL-Funktion der Desktop-Anwendung](/de/dbgate/developer/api-connections/#graphql) unterscheidet - siehe diese Seite, wenn Sie stattdessen die Desktop-App verwenden.

![DbGate Central - eine GraphQL-API abfragen](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
