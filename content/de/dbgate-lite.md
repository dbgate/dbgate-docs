---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: de
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) ist ein kostenloses Browser-Tool für die Arbeit mit Daten – ohne Installation und ohne Anmeldung. Es basiert auf derselben Grid-, Filter- und Query-Engine wie [DbGate Central](../dbgate-central/), sodass sich Durchsuchen, Filtern und Bearbeiten in beiden gleich anfühlen.

## SQL lernen und lehren

DbGate Lite führt **SQLite und DuckDB** vollständig in Ihrem Browser aus – mit WebAssembly:

* Schreiben und führen Sie SQL-Abfragen gegen eine Beispieldatenbank im vertrauten DbGate-Grid aus.
* Visualisieren Sie mit ER-Diagrammen, wie Tabellen zusammenhängen.
* Keine Installation, keine Anmeldung – öffnen Sie die Website und legen Sie los.

## Ad-hoc-Arbeit mit Datendateien

Öffnen Sie eine Datei in DbGate Lite und behandeln Sie sie wie eine Datenbank:

* **Importieren** Sie CSV-, JSON- und Excel-Dateien und fragen oder bearbeiten Sie sie mit SQL.
* Bereinigen und strukturieren Sie Daten um und **exportieren** Sie das Ergebnis anschließend wieder nach CSV, JSON oder Excel.

## Eine Datenbank oder Abfrage per Link teilen

Wenn Sie DbGate Lite mit bestimmten Hash-Parametern in der URL öffnen, wird automatisch eine temporäre Datenbank initialisiert:

* `initdbtype` – Datenbanktyp, `sqlite` oder `duckdb`
* `initdbscript` – SQL-Skript zum Erstellen und Befüllen der temporären Datenbank
* `initquery` (optional) – SQL-Abfrage, die in einem neuen Query-Tab geöffnet wird

Jeder, der den Link öffnet, erhält mit einem Klick dieselbe Beispieldatenbank und Abfrage – nützlich für Tutorials, Fehlerberichte und den Unterricht.

## Eine schreibgeschützte Ansicht veröffentlichen

Unabhängig vom Teilen eines bearbeitbaren Links können Sie mit der Schaltfläche „Publish“ in der Symbolleiste eine schreibgeschützte Ansicht einer CSV-/JSON-Datei oder eines BI-Berichts **veröffentlichen**. Dadurch wird eine eigenständige Seite geöffnet – nur die Daten und ein Hell-/Dunkel-Umschalter, ohne Seitenleiste oder Editor –, die jeder mit dem Link ohne Konto ansehen kann.

## Die Wahl zwischen Lite, Central, Premium und Team Premium

DbGate Lite eignet sich am besten zum Lernen und für einmalige Aufgaben. Für die laufende, professionelle Arbeit ist ein dediziertes Produkt besser geeignet:

* **DbGate Lite** – kostenlos, im Browser. Am besten geeignet zum Erlernen von SQL und für Ad-hoc-Datendateien.
* **[DbGate Central](../dbgate-central/)** – gehostetes Produkt für die Arbeit mit APIs: Verbinden Sie sich mit aktiven GraphQL-, oData- und Shopify-Endpunkten, verwalten Sie Verbindungen und Berichte in einem Workspace und teilen Sie sie mit Ihrem Team.
* **[DbGate Premium](/de/dbgate/getting-started/installation/)** – eine Edition von [DbGate](/de/dbgate/): die vollständige Desktop-Anwendung für die Arbeit mit Datenbanken, verbinden Sie sich mit SQL- und NoSQL-Servern und nutzen Sie den kompletten Satz professioneller Werkzeuge.
* **[DbGate Team Premium](/de/dbgate/getting-started/installation/docker-tp/)** – eine weitere Edition von [DbGate](/de/dbgate/), für Teams: eine gemeinsame Weboberfläche, die on-premise läuft, sodass Ihr gesamtes Team über den Browser auf Ihrer eigenen Infrastruktur mit Datenbanken arbeitet.
