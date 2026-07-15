---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: de
title: Data deployer
weight: 2
---

Mit dem Data deployer können Sie Ihre Daten in **Archivordnern** visuell mit der **echten Datenbank** vergleichen und synchronisieren
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Data deployer starten
Sie können den Data deployer über das Kontextmenü der Datenbank oder über das Kontextmenü des Archivordners starten. Beim Start aus der Datenbank werden Sie aufgefordert, ein Archiv auszuwählen. Beim Start aus dem Archiv wird der Data deployer mit der aktuellen Datenbank gestartet.

## Einstellungen
- Datenbankserver, Datenbank - wählen Sie die Datenbank aus, mit der Sie arbeiten möchten
- Datenarchiv - wählen Sie den Ordner mit den Daten aus, die für Vergleich und Synchronisierung verwendet werden
### Tabellenbezogen
- Schlüssel (Vergleichsspalten) - wählen Sie die Spalten aus, die für das Zuordnen der Zeilen zwischen Datenbank und Archiv verwendet werden
### Replikator-Einstellungen
Die nachfolgenden Einstellungen ("table" - deploy und Globale Einstellungen für die Datenbereitstellung) sind spezifisch für den Replikator und werden im Thema [Data replicator](data-replicator) beschrieben

## Datenunterschiede kopieren
Der Data deployer zeigt die Unterschiede zwischen den Daten im Archiv und in der Datenbank an. Wenn Sie einige Zellen mit Unterschieden auswählen, können Sie diese Unterschiede in das Archiv oder in die Datenbank schreiben. Wenn diese Zellen ausgewählt sind, erscheinen in der rechten unteren Ecke Schaltflächen, die die Synchronisierung ermöglichen:
- Write x rows, y columns to archive - kopiert die ausgewählten Zellen aus der Datenbank in das Archiv.
- Write x rows, y columns to database - kopiert die ausgewählten Zellen aus dem Archiv in die Datenbank. Zuerst wird ein Bestätigungsdialog mit dem Änderungs-SQL angezeigt.

## Aktionen des Data replicators
- Deploy into DB - diese Aktion stellt die Änderungen mit den konfigurierten Einstellungen in der Datenbank bereit
- Generate shell - diese Aktion erstellt eine JavaScript-Datei, die die Bereitstellung ausführt. Diese Datei kann über die Kommandozeile ausgeführt werden
- Generate SQL - erstellt SQL, das die Änderungen aus dem Archiv in der Datenbank bereitstellt

Mehr über diese Aktionen im Thema [Data replicator](data-replicator)
