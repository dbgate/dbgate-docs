---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: de
title: Benutzer
weight: 30
---

## Registerkarte "Users"
Konfigurieren Sie Benutzer, Passwörter, Benutzerberechtigungen und die Zuordnung von Benutzern zu Verbindungen.
Passwörter werden nur für Authentifizierungsmethoden vom Typ "Local" verwendet. Aber alle Methoden mit externen Identitätsanbietern verwenden eine Benutzersuche, sodass Sie Berechtigungen und Verbindungen für einen Benutzer konfigurieren können, auch für extern authentifizierte Benutzer. 

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### Registerkarten der Benutzerdetails
* Info
  * Benutzerberechtigungen konfigurieren
  * Die diesem Benutzer zugewiesenen Rollen konfigurieren
* Team files - Zugriff auf [Team-Dateien](team-files) konfigurieren
* Connections - die diesem Benutzer zugewiesenen Verbindungen konfigurieren
* Databases - [Datenbankberechtigungen](permissions#database-permissions) für diesen Benutzer konfigurieren
* Tables/views/objects - [Tabellenberechtigungen](permissions#table-permissions) für diesen Benutzer konfigurieren
* Disk files - Zugriff auf Dateien auf der Festplatte / im Docker-Volume konfigurieren
