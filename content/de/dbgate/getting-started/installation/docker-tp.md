---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: de
title: Team Premium unter Docker
weight: 30
---

Eine typische Team-Premium-Installation besteht aus zwei Komponenten:
- DbGate-Server-Docker-Container
- Datenbankserver (MS SQL, MySQL, PostgreSQL, Oracle) – interne Speicherdatenbank für Verbindungen, Benutzer und Rollen. Sie können einen vorhandenen Datenbankserver verwenden oder einen neuen installieren.

## DbGate-Server-Docker-Container
Verwenden Sie das [DbGate Team Premium Image](https://hub.docker.com/r/dbgate/dbgate-premium) von Docker Hub:
```
docker pull dbgate/dbgate-premium
```

Für den DbGate-Team-Premium-Container müssen einige Umgebungsvariablen gesetzt werden:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` – definieren die Verbindung zur internen Speicherdatenbank

Weitere Details zu den verfügbaren Umgebungsvariablen finden Sie in der [Dokumentation der Umgebungsvariablen](/de/dbgate/customization/env-variables/#team-premium-edition-configuration).

## Ressourcenanforderungen

Tatsächlich hat DbGate Team Premium einen sehr geringen Ressourcenverbrauch, für beste Performance empfehlen wir jedoch die folgende Konfiguration (für 10 gleichzeitige Benutzer):
- 2 CPU-Kerne
- 4 GB RAM (einschließlich RAM-Verbrauch der internen Speicherdatenbank MySQL oder PostgreSQL)
- 10 GB freier Speicherplatz (für die Docker-Installation, die Speicherdatenbank, temporäre Dateien, Abfrageergebnisse usw. Der tatsächliche Speicherplatzverbrauch hängt vom Nutzungsverhalten ab)

Für eine kleinere Anzahl von Benutzern können Sie niedrigere Ressourcenlimits verwenden (1 GB RAM, 1 CPU-Kern).  
Wenn Sie den Ressourcenverbrauch für kleine Installationen minimieren möchten, empfehlen wir die Verwendung von MySQL/MariaDB als internen Speicher.  

## Docker konfigurieren

Wenn Sie Festplattendateien zum Speichern von Benutzerdateien (wie den Export von Abfrageergebnissen) verwenden möchten, sollten Sie den Pfad `/root/.dbgate` im Container mappen.

Nachfolgend sehen Sie eine Beispieldatei `docker-compose.yml`, die einen DbGate-Team-Premium-Container mit PostgreSQL als interner Speicherdatenbank definiert.
- Sie können die Umgebungsvariable `DBGATE_LICENSE` definieren, um den Lizenzschlüssel festzulegen. Wenn sie nicht gesetzt ist, fragt DbGate beim ersten Start nach dem Lizenzschlüssel.
-  Sie können die Umgebungsvariable 'ADMIN_PASSWORD' definieren, um das Passwort des Admin-Benutzers festzulegen. Wenn sie nicht gesetzt ist, fragt DbGate beim ersten Start nach dem Admin-Passwort.

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## Zustandslosigkeit/Zustandsbehaftung
Der DbGate-Container ist zustandsbehaftet.

Die folgenden Daten werden im Container gespeichert:
* Sitzungen angemeldeter Benutzer
* Zustände der Abfrageausführung
* Temporäre Dateien (wie Ergebnisse)
* Geöffnete Datenbanktransaktionen
* Geöffnete Datenbankverbindungen

Es ist nicht möglich, mehrere DbGate-Container korrekt hinter einem Load Balancer zu betreiben, da die oben genannten Daten nicht zwischen den Containern geteilt werden.

## DbGate-Server aus NPM
Wenn Ihre Infrastruktur Docker nicht unterstützt, können Sie das [DbGate Team Premium NPM-Paket](https://www.npmjs.com/package/dbgate-serve-premium) verwenden:
```
npm install -g dbgate-serve-premium
```
 
## Prozessisolation
DbGate Team Premium verwendet Prozessisolation auf Ebene der Datenbankverbindung, sodass mehrere Benutzer denselben Datenbankserver ohne gegenseitige Beeinträchtigung nutzen können. Der von DbGate abgezweigte Prozess wächst mit der Anzahl der aktiven Benutzer und Verbindungen. Stellen Sie daher sicher, dass Ihr Server über ausreichend Ressourcen verfügt.
Die folgenden Entitäten werden in einen neuen Prozess isoliert:
* Serververbindungen
* Datenbankverbindungen
* Abfragesitzungen
* Ausführung von Export-/Importaufträgen
* SSH-Tunneling
