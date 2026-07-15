---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: de
title: KI-Funktionen
weight: 55
---

DbGate enthält mehrere KI-gestützte Funktionen *(Premium und Team Premium)*. Sie stehen allen Premium-Benutzern ohne API-Schlüssel oder Konfiguration zur Verfügung - DbGate verwendet ein eigenes KI-Gateway, das Anfragen an den LLM-Anbieter weiterleitet.

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## Datenbank-Chat

Der Datenbank-Chat ist ein KI-Chatbot, der sowohl Ihr Datenbankschema als auch dessen Daten versteht.

* **Natürliche Konversation** - stellen Sie Fragen in jeder natürlichen Sprache und erhalten Sie Antworten oder sofort ausführbares SQL.
* **Kontextbewusst** - das Modell kennt Ihr Schema und (mit Erlaubnis) die Live-Daten, sodass es korrekte Joins, Filter und Aggregationen vorschlägt.
* **Iterativ** - verfeinern Sie mit Befehlen wie "füge einen Datumsfilter hinzu" oder "gruppiere nach Kunde", und die Abfrage wird sofort aktualisiert.
* **Diagramme** - fragen Sie nach einem Balken-, Kreis- oder Liniendiagramm, das aus den Ergebnissen erstellt wird.
* **Berater-Modus** - er kann gespeicherte Prozeduren und Views analysieren, sodass Sie Fragen stellen können wie "Erkläre Prozedur X" oder "Welche Tabellen sind von Prozedur Y betroffen". DbGate zeigt an, welche Objekte analysiert wurden.

### SQL ausführen - Sicherheit zuerst

Der Datenbank-Chat kann SQL ausführen, um Fragen zu beantworten. Sie entscheiden, wie:

* **Vor dem Ausführen von SQL fragen (Standard)** - DbGate fragt vor der Ausführung jeder Abfrage nach.
* **SQL automatisch ausführen** - Abfragen, die kein `SELECT` sind, erfordern weiterhin eine Bestätigung.
* **Niemals ausführen, nur SQL vorschlagen** - der Chat zeigt nur Abfragen an; es werden keine Daten aus Ihrer Datenbank an das LLM gesendet.

Wenn eine vorgeschlagene Abfrage fehlschlägt, sendet DbGate den Fehler an das Modell zurück, das die Abfrage in der Regel automatisch korrigiert.

## SQL-KI-Assistent

Nutzen Sie den Chat als SQL-Assistenten - "Schreibe eine SQL-Abfrage für die Top-10-Kunden nach Umsatz" - und öffnen Sie das Ergebnis in einem [SQL-Editor](/de/dbgate/sql-and-queries/sql-editor/)-Tab.

## SQL-Fehler erklären

Klicken Sie neben einer Fehlermeldung auf **Erklären**, um eine KI-Erklärung zu erhalten, was schiefgelaufen ist und wie es behoben werden kann.

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## KI-Assistent für Themes

Die KI kann auch benutzerdefinierte Farb-Themes erzeugen - siehe [Benutzerdefinierte Themes](/de/dbgate/customization/custom-themes/).

## KI-Funktionen deaktivieren

KI-Funktionen können vollständig deaktiviert werden (zum Beispiel in eingeschränkten Umgebungen) - über die DbGate-Einstellungen.
