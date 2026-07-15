---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: de
title: Rollen
weight: 40
---

## Registerkarte "Rollen"
Konfigurieren Sie Rollen, Rollenberechtigungen und die Zuordnung von Rollen zu Verbindungen. Sie können eigene Rollen erstellen und ihnen Benutzer zuweisen, sodass Berechtigungen und verknüpfte Verbindungen von allen dieser Rolle zugewiesenen Benutzern gemeinsam genutzt werden.

Es gibt einige vordefinierte Rollen:
- superadmin - Rolle für die Administrationsseite, https://your_dbgate_instance/admin.html
- logged-user - Rolle für alle angemeldeten Benutzer. Sie können die Berechtigungen für bestimmte Benutzer überschreiben
- anonymous-user - Rolle für Benutzer, die mit der Authentifizierungsmethode "Anonymous" angemeldet sind

![Role administration - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Registerkarten der Rollendetails
* Info
  * Rollenberechtigungen konfigurieren
  * Der Rolle zugewiesene Benutzer konfigurieren
* Team files - Zugriff auf [Team-Dateien](team-files) konfigurieren
* Connections - dieser Rolle zugewiesene Verbindungen konfigurieren
* Databases - [Datenbankberechtigungen](permissions#database-permissions) für diese Rolle konfigurieren
* Tables/views/objects - [Tabellenberechtigungen](permissions#table-permissions) für diese Rolle konfigurieren
* Disk files - Zugriff auf Dateien auf der Festplatte bzw. im Docker-Volume konfigurieren
