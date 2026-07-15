---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: de
title: SQL-Editor
weight: 10
---

Im SQL-Editor schreiben und führen Sie SQL-Skripte gegen Ihre Verbindung aus. Öffnen Sie ihn über die Schaltfläche {{< mdi "flash" >}} "Neue Abfrage" in der Symbolleiste oder über das Kontextmenü einer Verbindung oder Datenbank.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## SQL ausführen

* **Skript ausführen** - führt das gesamte Skript über die Schaltfläche {{< mdi "play" >}} Ausführen (oder F5) aus.
* **Aktuelle Anweisung ausführen** - führt nur die Anweisung unter dem Cursor aus.
* **Auswahl ausführen** - wenn Sie einen Teil des Skripts markieren, wird nur der markierte Text ausgeführt.
* Die Ergebnisse erscheinen im Ergebnisraster unterhalb des Editors. Mehrere Ergebnismengen werden in separaten Registerkarten angezeigt.
* Meldungen, Zeilenanzahlen und Fehler werden in der Registerkarte **Messages** angezeigt.

## Hilfsmittel beim Bearbeiten

* **SQL-Code-Formatierer** - formatiert das aktuelle Skript neu, für einheitliche Einrückung und Groß-/Kleinschreibung.
* **Code-Vervollständigung** - Vorschläge für Tabellen, Spalten und Schlüsselwörter auf Basis des Schemas der verbundenen Datenbank.
* **Join-Assistent** - das Hilfsprogramm "Add SQL join" erzeugt eine `LEFT`/`INNER`/`RIGHT JOIN`-Klausel aus Fremdschlüsseln, sodass Sie Join-Bedingungen nicht von Hand eingeben müssen.

## Arbeiten mit Ergebnissen

Das Ergebnisraster verwendet dieselbe Engine wie der [Daten-Browser](/de/dbgate/working-with-data/data-browser/), sodass Sie [filtern und sortieren](/de/dbgate/working-with-data/data-filtering/), Zellen in verschiedenen Formaten kopieren und das Ergebnis [exportieren](/de/dbgate/working-with-data/export-import/) können.

### Abfrageergebnisse & Views bearbeiten *(Premium)*

Abfrageergebnisse sind bearbeitbar, wenn DbGate das Ergebnis einer einzelnen Tabelle oder einer aktualisierbaren View zuordnen kann. Bearbeiten Sie Zellen direkt im Ergebnisraster, prüfen Sie das generierte Änderungsskript und speichern Sie es zurück in die Datenbank - derselbe Workflow mit vorgemerkten Änderungen wie im [Daten-Browser](/de/dbgate/working-with-data/data-browser/). Auch das Bearbeiten von Views wird unterstützt.

> Bearbeitbare Abfrageergebnisse und bearbeitbare Views wurden in DbGate 7.2 eingeführt.

## Transaktionssteuerung

Sie können Transaktionen aus dem Editor heraus steuern - Skripte innerhalb einer expliziten Transaktion ausführen und die Änderungen bestätigen (Commit) oder zurücksetzen (Rollback), was beim Testen datenverändernder Skripte nützlich ist.

## Weitere Editoren

* **Mongo-JavaScript-Editor** - für MongoDB-Verbindungen: Mongo-Skripte in NodeJS-Syntax schreiben und ausführen.
* **Redis** - den Redis-Schlüsselbaum durchsuchen, ein Skript aus ausgewählten Schlüsseln generieren und Redis-Skripte ausführen.
