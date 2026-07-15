---
sourceHash: 80df2a73525118cee579014e200ff5f67715aa6f35468656abb3f8b70c254566
language: de
title: Datenarchive
weight: 1
---

Archive sind Ordner mit Daten im JSONL-Format (NDJSON). DbGate ermöglicht ein sehr effizientes Arbeiten mit ihnen: Sie können sie in eine Datenbank importieren, in andere Formate exportieren oder die Daten direkt im Archiv bearbeiten. Ein Archiv verhält sich wie eine sehr schnelle und leichtgewichtige Datenbank, die in lokalen Dateien gespeichert ist.

## JSONL-Format
DbGate verwendet intern überall das JSONL-Format. JSONL ist eine Textdatei, bei der jede Zeile eine als JSON serialisierte Zeile enthält. DbGate geht davon aus, dass die erste Zeile einen Header (ebenfalls als JSON) mit der Tabellenstruktur enthalten kann. Wenn Sie JSONL mit dynamischer Struktur (ohne feste erste Zeile) verwenden, ist dieses Format standardisiert und kann in viele andere Werkzeuge geladen werden.

## Archivordner
Ein Archiv ist in Ordner mit JSONL-Dateien organisiert. Es hat eine ähnliche Struktur wie eine Datenbank. Sie können daher eine ganze Datenbank in ein neues Archiv exportieren – jede Tabelle wird in eine JSON-Datei exportiert, und dank der Header-Zeile bleibt auch die Tabellenstruktur erhalten.

## Archivdateien anzeigen und bearbeiten
Sie können JSONL-Dateien in verschiedenen Modi öffnen:
- Kontextmenü „Open“ – öffnet ein Datenraster, das Sortieren, Filtern und Bearbeiten Ihrer JSONL-Daten ermöglicht
- Kontextmenü „Open in text editor“ – ermöglicht das manuelle Bearbeiten der JSONL-Datei

## Archive und DB-Modelle
Archivordner werden auch als Speicher für DB-Modelle verwendet. Sie können ein DB-Modell im Kontextmenü der Datenbank über „Export DB model“ exportieren. Sie können dieses Modell anschließend bearbeiten (YAML-Dateien für die Tabellenstruktur, SQL-Dateien für Views und Stored Procedures), mit der realen Datenbank vergleichen und in die Datenbank übertragen
