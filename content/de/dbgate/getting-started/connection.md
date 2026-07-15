---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: de
title: Verbindung
weight: 20
---

Die Verbindung zu Ihrer Datenbank von DbGate aus ist einfach. Sie können sich auf verschiedene Arten mit einer Datenbank verbinden:

* Menü Datei/Verbindung hinzufügen oder Symbol {{< mdi "plus-thick" >}} im Widget VERBINDUNGEN
* Menü Datei/Neue SQLite-Datenbank - erstellt eine neue SQLite-Datenbank
* Menü Datei/Öffnen - Sie können eine vorhandene SQLite-Datenbank öffnen

## Verbindungsbildschirm
![Verbindungsbildschirm](https://media.dbgate.io/img/new-connection-light.png)

Die Felder im Verbindungsbildschirm hängen stark vom Verbindungstyp ab.

Einige allgemeine Felder:

* Server - Hostname des Datenbankservers
* Port - Port, im Falle des Standardports der Datenbank können Sie ihn leer lassen
* Benutzer, Passwort - Authentifizierung
* Passwortmodus
    * Speichern und verschlüsseln - das Passwort wird verschlüsselt gespeichert, Sie können es beim nächsten Mal nicht mehr einsehen
    * RAW speichern - das Passwort wird unverändert (ohne Verschlüsselung) gespeichert, Sie können es später überprüfen
    * Nicht speichern, nach Passwort fragen - das Passwort wird nicht gespeichert, Sie müssen es beim Verbinden eingeben
    * Nicht speichern, nach Benutzername und Passwort fragen - weder Passwort noch Benutzername werden gespeichert, Sie müssen beim Verbinden beides eingeben
* Ist schreibgeschützt - die Verbindung ist schreibgeschützt (bei Engines ohne Unterstützung für schreibgeschützte Sitzungen können Sie in diesem Fall keine SQL-Abfragen ausführen)
* Standarddatenbank - welche Datenbank nach dem Verbinden aktiv sein wird
* Nur Datenbank *&lt;Standarddatenbank&gt;* verwenden - wenn aktiviert, erscheint nur die Standarddatenbank im Verbindungsbaum (andere Datenbanken auf dem Server werden ausgeblendet)
* Anzeigename - Name, unter dem die Verbindung in der Anwendung erscheint

## SSH-Tunnel
Hier können Sie die Verbindung über einen SSH-Tunnel konfigurieren. 

Allgemeine Felder:
* SSH-Tunnel verwenden - aktivieren, um einen SSH-Tunnel zu verwenden
* Host - Hostname des SSH-Servers

![DbGate - Konfiguration des SSH-Tunnels](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
Konfiguration der SSL-Verbindung.

Allgemeine Felder:
* SSL verwenden - aktivieren, um SSL zu verwenden. In den meisten Fällen ist dies das Einzige, was Sie für die Verwendung von SSL konfigurieren müssen

![DbGate - Konfiguration der SSL-Verbindung](https://media.dbgate.io/img/connection-ssl-window-light.png)
