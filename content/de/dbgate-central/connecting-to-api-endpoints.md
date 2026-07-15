---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: de
title: Verbindung zu API-Endpunkten herstellen
weight: 10
---

DbGate Central verbindet sich mit drei Familien von API-Endpunkten und verwendet dafür jeweils denselben Dialog „Neue Verbindung“.

## Unterstützte Endpunkttypen

* **GraphQL** - das Schema per Introspektion abrufen, Typen durchsuchen und Abfragen gegen eine beliebige GraphQL-API ausführen.
* **oData** - mit oData-V4-Diensten arbeiten, als wären sie gewöhnliche Tabellen.
* **Shopify** - über die Shopify Admin API eine Verbindung zu Ihrem Store herstellen und Produkte, Bestellungen, Kunden, Metafelder und mehr erkunden.

## Eine Verbindung erstellen

Öffnen Sie den Dialog **Neue Verbindung**, wählen Sie den Verbindungstyp aus, geben Sie die Dienst-URL ein und legen Sie die Authentifizierungsmethode fest:

* **None** - für offene, öffentliche Endpunkte.
* **Basic** - Benutzername und Passwort.
* **Bearer token** - fügen Sie ein Zugriffstoken ein.
* **API key** - senden Sie einen Schlüssel in einem Header oder Query-Parameter.

Verbindungen werden in Ihrem Workspace gespeichert, sodass sie bei der nächsten Anmeldung auf jedem Gerät verfügbar sind – ganz ohne lokale Einrichtung.

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
