---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: de
title: MCP-Server für KI-Agenten
weight: 50
---

DbGate Central kann Ihren Workspace für KI-Assistenten wie [Claude](https://claude.ai) als Remote-**MCP-Konnektor (Model Context Protocol)** bereitstellen - damit ein Agent Ihre APIs auf dieselbe Weise erkunden und abfragen kann wie Sie, mit einem Zugriff, über den Sie die Kontrolle behalten.

## Einrichtung

1. Öffnen Sie den Tab **Settings** und erstellen Sie ein **MCP-Profil**. Kopieren Sie dessen **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), **Client ID** und **Client Secret**.
2. Fügen Sie in claude.ai (oder einem anderen MCP-kompatiblen Client) einen benutzerdefinierten Konnektor mit dieser URL und den OAuth-Zugangsdaten hinzu.
3. Legen Sie im Editor jeder Verbindung deren **MCP access**-Stufe fest - **No access**, **Read-only** oder **Writable**. Die Voreinstellung ist kein Zugriff, es wird also nichts freigegeben, bis Sie es erlauben.
4. Der Assistent führt den OAuth-Handshake durch und Sie erteilen Ihre Zustimmung, wodurch der Konnektor an dieses Profil und diesen Workspace gebunden wird.

Jeder Workspace kann mehrere MCP-Profile haben, jedes mit eigener URL, eigenen Zugangsdaten und verbindungsspezifischen Berechtigungen. Die Authentifizierung verwendet OAuth 2.1 mit verpflichtendem PKCE, und Client Secrets werden verschlüsselt gespeichert.

## Was der Agent tun kann

Verfügbar für **oData**-, **GraphQL**- und **Shopify**-Verbindungen (SQLite/DuckDB laufen nur im Browser und sind für MCP nicht vorgesehen):

* **Verbindungen auflisten**, die das Profil verwenden darf.
* **Entitäten auflisten** - Tabellen, Views oder Katalogentitäten.
* **Das Schema untersuchen** - Spaltennamen und -typen.
* **Zeilen abfragen** - Daten filtern, seitenweise durchblättern und auswählen.
* **Zeilen aktualisieren** - nur bei Shopify und nur, wenn Sie Writable-Zugriff gewähren.

Da Lese- und Schreibvorgänge dieselbe Engine wie das Grid und der Scheduler nutzen, sieht ein Agent genau dieselben Daten und Möglichkeiten wie Sie - niemals mehr als den Zugriff, den Sie gewähren.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
