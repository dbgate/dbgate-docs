---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: de
title: API-Verbindungen
weight: 10
---

DbGate unterstützt Verbindungen zu REST-APIs, GraphQL-Diensten und OData-Endpunkten. Diese API-Verbindungen verwenden dieselben Oberflächenmuster wie Datenbankverbindungen, sodass Sie APIs und Datenbanken in einer einheitlichen Umgebung nutzen können.

Die Unterstützung für API-Verbindungen ist in DbGate Premium verfügbar.

> Sie suchen nach API-Browsing ohne die Desktop-Anwendung? [DbGate Central](/de/dbgate-central/connecting-to-api-endpoints/) ist eine separate, gehostete Implementierung von GraphQL-/oData-/Shopify-Verbindungen, die von Grund auf neu für den Browser umgesetzt wurde.

## GraphQL

GraphQL-Verbindungen ermöglichen die Interaktion mit GraphQL-APIs. DbGate bietet Funktionen zur Schema-Introspektion und zur Ausführung von Abfragen.

### Eine GraphQL-Verbindung erstellen

Um eine GraphQL-Verbindung zu erstellen, verwenden Sie den Dialog "Neue Verbindung" und wählen Sie GraphQL als Verbindungstyp aus. Geben Sie die URL des GraphQL-Endpunkts ein und konfigurieren Sie bei Bedarf die Authentifizierung.

### Schema-Introspektion

DbGate erkennt das GraphQL-Schema automatisch, einschließlich der verfügbaren Typen, Abfragen, Mutationen und deren Argumente. Der Schema-Browser zeigt das Typsystem an und ermöglicht es Ihnen, die API-Struktur zu erkunden.

### Abfrage-Editor

Im GraphQL-Abfrage-Editor können Sie Abfragen und Mutationen schreiben. Mit dem GraphQL-Explorer können Sie Abfragen erstellen, indem Sie Felder und Argumente aus dem Schema auswählen.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Variablen

GraphQL-Abfragen unterstützen Variablen. Definieren Sie Variablen im Variablen-Panel und referenzieren Sie sie in Ihren Abfragen mit der Standard-GraphQL-Variablensyntax. Variablen können in einem Formular oder als reines JSON bearbeitet werden.

### Antwort-Viewer

Abfrageergebnisse werden in einem formatierten JSON-Viewer mit aufklappbarer Baumstruktur dargestellt. Werden in der Antwort Arrays erkannt, wird automatisch die Tabellenansicht angezeigt. Bei Bedarf können Sie zurück zur reinen JSON-Ansicht wechseln.

## OpenAPI (Swagger)

OpenAPI-Verbindungen unterstützen REST-APIs, die OpenAPI-Spezifikationen bereitstellen (Versionen 2.0 und 3.0).

### Eine OpenAPI-Verbindung erstellen

Erstellen Sie eine neue Verbindung und wählen Sie OpenAPI als Verbindungstyp aus. Geben Sie die URL zur OpenAPI-Spezifikationsdatei an (typischerweise swagger.json oder openapi.json). DbGate analysiert die Spezifikation und stellt alle dokumentierten Endpunkte zur Verfügung.

### API-Dokumentations-Browser

Der OpenAPI-Browser zeigt alle verfügbaren Endpunkte an, geordnet nach Tags und Pfaden. Für jeden Endpunkt können Sie Folgendes einsehen:
- HTTP-Methode (GET, POST, PUT, DELETE, PATCH)
- Parameter (Pfad, Query, Header, Body)
- Schemas des Request-Bodys
- Beschreibungen aus der Dokumentation

### Ausführen von Anfragen

Wählen Sie einen Endpunkt aus, um den Request-Builder zu öffnen. Füllen Sie die erforderlichen Parameter, Header und den Request-Body aus. Führen Sie die Anfrage aus, um sie an den API-Server zu senden.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Antwort untersuchen

Sehen Sie sich den Statuscode, die Header und den Body der Antwort an. JSON-Antworten werden formatiert und können sowohl in der Baum- als auch in der Tabellenansicht dargestellt werden. Antworten, die kein JSON sind, werden als Text angezeigt.

## OData

OData-Verbindungen unterstützen das Abfragen von OData-Diensten mit der Standard-OData-Abfragesyntax.

### Eine OData-Verbindung erstellen

Erstellen Sie eine neue Verbindung mit OData als Verbindungstyp. Geben Sie die Root-URL des OData-Dienstes ein. DbGate ruft das Metadatendokument des Dienstes ab.

### Metadaten erkunden

Der Metadaten-Browser zeigt die verfügbaren Entity Sets, Entitätstypen, Eigenschaften und Beziehungen an, die in den Metadaten des Dienstes definiert sind.

### Ausführen von Abfragen

OData-Abfragen unterstützen die Standard-OData-Abfrageoptionen:
- `$filter` - Entitäten nach Eigenschaftswerten filtern
- `$select` - festlegen, welche Eigenschaften zurückgegeben werden
- `$expand` - verwandte Entitäten einbeziehen
- `$orderby` - Ergebnisse sortieren
- `$top` und `$skip` - Paginierung
- `$count` - Anzahl der Ergebnisse einbeziehen

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

Die Ergebnisse werden in tabellarischer Form dargestellt, ähnlich wie die Ergebnisse von Datenbankabfragen.

## Authentifizierung

Alle Typen von API-Verbindungen unterstützen mehrere Authentifizierungsmethoden:

- **API Key** - Name und Wert des Schlüssels angeben, gesendet als Header oder Query-Parameter
- **Bearer Token** - OAuth- oder JWT-Token, die im Authorization-Header gesendet werden
- **Basic Authentication** - Benutzername und Passwort mittels HTTP Basic Auth
- **Keine Authentifizierung** - für öffentliche APIs

Konfigurieren Sie die Authentifizierung in den Verbindungseigenschaften.

## Datenexport

Daten aus API-Antworten können mit der Standard-Exportfunktion von DbGate in verschiedene Formate exportiert werden:
- JSON
- CSV
- Excel
- SQL-INSERT-Anweisungen
- XML

Verwenden Sie dazu den Standard-Kontextmenüeintrag "Export" im tabellarischen Daten-Browser.

## Arbeiten mit mehreren APIs

Sie können Verbindungen zu mehreren APIs und Datenbanken erstellen. Öffnen Sie mehrere Anfrage-Tabs, um gleichzeitig mit verschiedenen Endpunkten zu arbeiten.

Der Zustand der Tabs bleibt nach dem Schließen und erneuten Öffnen der Anwendung erhalten; Sie können eine Anfrage aus dem Verlauf der geschlossenen Tabs erneut öffnen.
