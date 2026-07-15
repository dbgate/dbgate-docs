---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: de
title: DbGate Cloud
weight: 80
---

DbGate Cloud ist ein Online-Speicher für Ihre Verbindungen, SQL-Skripte und andere Objekte. Außerdem bietet er eine öffentliche Wissensdatenbank mit nützlichen SQL-Skripten.

> DbGate Cloud ist eine Speicherergänzung für die **Desktop**-App von DbGate (Verbindungen, SQL-Skripte, freigegebene Ordner). Suchen Sie stattdessen eine gehostete Anwendung, die nur im Browser läuft? Siehe [DbGate Central](/de/dbgate-central/).

## Anmelden
Um DbGate Cloud zu nutzen, ist eine Anmeldung erforderlich. Verwenden Sie das Symbol {{< mdi "account-remove-outline" >}} im linken Bereich.

Ihr Cloud-Speicher ist immer mit Ihrer E-Mail-Adresse verknüpft.  
Sie können einen der folgenden Authentifizierungsanbieter wählen:
* GMail
* GitHub
* E-Mail - ein einmaliger Magic Link zur Anmeldung wird an Ihre E-Mail-Adresse gesendet

DbGate-Server speichern Ihr Passwort nicht.

## In der Cloud gespeicherte Verbindungen verwenden
Ihre Cloud-Inhalte erscheinen nach der Anmeldung unter dem Widget {{< mdi "cloud-key" >}}. Standardmäßig sehen Sie Ihren privaten Ordner (mit Schreibzugriff).

Verbindung in der Cloud speichern:
* Kontextmenü der Verbindung, wählen Sie "Copy to cloud folder"
* Klicken Sie auf {{<mdi "plus-thick" >}} und wählen Sie dann "Add connection on cloud"

## Welche Verbindung ist in der Cloud gespeichert?
* Ihre Cloud-Verbindungen befinden sich immer unter dem Widget {{< mdi "cloud-key" >}}
* Ihre lokal gespeicherten Verbindungen unter dem Widget {{< mdi "database" >}}

## Arbeiten mit Ordnern
Sie können neben Ihrem privaten Ordner weitere Ordner erstellen (Premium-Edition erforderlich).

Unter der Schaltfläche {{<mdi "plus-thick" >}} finden Sie folgende Befehle:
* New shared folder - erstellt einen neuen freigegebenen Ordner. Standardmäßig ist er nur für Sie zugänglich, Sie können weitere Benutzer einladen
* Add existing shared folder - wenn Sie einen Einladungslink zu einem freigegebenen Ordner haben (der von einem anderen Benutzer erstellt wurde), ist dies die richtige Stelle, um ihn zu verwenden

Wenn Sie Ihren Ordner mit anderen Personen teilen möchten, klicken Sie mit der rechten Maustaste auf den Ordner und wählen Sie "Copy invite link"

## Berechtigungen für freigegebene Ordner
* Admin - Sie haben vollen Zugriff auf den Ordner, Sie können andere Personen einladen und Inhalte schreiben
* Write - Sie können Inhalte schreiben/löschen, aber Sie können keine anderen Personen einladen
* Read - nur den Inhalt des Ordners lesen. Bitte beachten Sie, dass diese Berechtigung nicht für Datenbanken gilt, die innerhalb einer serverdefinierten Verbindung verfügbar sind

## Freigegebene Ordner in der Community-Edition
In der Community-Edition können Sie von Premium-Benutzern erstellte freigegebene Ordner verwenden, aber Sie können keine eigenen freigegebenen Ordner erstellen. Dies soll Teams mit der Premium-Edition ermöglichen, Verbindungen, SQL-Dateien und ER-Diagramme mit anderen Teammitgliedern zu teilen, die die Community-Edition verwenden.

## Öffentliche Wissensdatenbank
Die öffentliche Wissensdatenbank ist eine Sammlung nützlicher SQL-Skripte und Diagramme für Aufgaben wie SQL-Performance-Tuning, Deadlock-Analyse, Indexnutzung usw. Die Wissensdatenbank ist in allen Editionen verfügbar, Diagramme jedoch nur in den Premium-Editionen.

Alle Einträge sehen Sie unter dem Symbol {{< mdi "cloud-search" >}} im linken Widget-Bereich.  
Ausgegraute Skripte kennzeichnen Skripte, die mit der aktuell ausgewählten Datenbank nicht kompatibel sind.

Wenn Sie die Wissensdatenbank mit Ihren SQL-Skripten erweitern möchten, erstellen Sie bitte einen Pull Request im GIT-Repository [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base).

Skripte in der Wissensdatenbank sind mit der Syntax [SQL front matter](/de/dbgate/developer/sql-front-matter) annotiert

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)
