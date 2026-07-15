---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: de
title: Administration
weight: 60
---

Die Administrationsoberfläche ermöglicht es einem Team, DbGate als gemeinsam genutzte Mehrbenutzer-Webanwendung zu betreiben: Sie verwalten Verbindungen zentral, legen fest, wer sich anmelden darf und auf welche Weise, und vergeben feingranularen Zugriff auf Datenbanken und Objekte über Benutzer, Rollen und Berechtigungen. Außerdem werden hier gemeinsame Teamdateien gehostet. Alles, was hier konfiguriert wird, wird in der Speicherdatenbank abgelegt und nicht in lokalen Dateien.

Das Administrationswerkzeug ist nur in der Team Premium Edition verfügbar. In der Community Edition konfigurieren Sie DbGate bitte stattdessen über [Umgebungsvariablen](/de/dbgate/customization/env-variables).

Die gesamte Konfiguration aus der Administration wird in der Speicherdatenbank gespeichert – verwenden Sie die [STORAGE_xxx-Umgebungsvariablen](/de/dbgate/customization/env-variables/#team-premium-edition-configuration), um sie zu konfigurieren.

In diesem Abschnitt:

* [Authentifizierung](auth) - Anmeldemethoden und Identitätsanbieter konfigurieren
* [Verbindungen](connection) - die für Ihr Team verfügbaren Verbindungen verwalten
* [Teamdateien](team-files) - SQL-Skripte, ER-Diagramme und Diagramme teilen
* [Benutzer](users) - Benutzerkonten verwalten
* [Rollen](roles) - Berechtigungen in Rollen gruppieren
* [Berechtigungen](permissions) - Zugriff auf Verbindungen, Datenbanken und Tabellen gewähren

## Administratorzugriff

Die Administrationsseite ist unter der URL https://your_dbgate_instance/admin.html verfügbar. 

Für den Root-Administrator sollte ein Passwort definiert sein. Sie können die Umgebungsvariable ADMIN_PASSWORD setzen. Wenn diese Variable nicht definiert ist, fragt DbGate beim ersten Mal nach dem Admin-Passwort.

Sie können anschließend einem anderen Benutzer mit einer anderen Authentifizierungsmethode die Administrationsberechtigung erteilen, aber zunächst müssen Sie diese Admin-Seite öffnen.

