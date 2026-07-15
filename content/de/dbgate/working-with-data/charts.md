---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: de
title: Diagramme
weight: 30
---

Mit DbGate können Sie Diagramme zur Visualisierung Ihrer SQL-Abfragen verwenden. Führen Sie einfach die Abfrage aus; wird ein Diagramm automatisch erkannt, erscheint der Tab "Chart 1". Wenn Sie mehrere Abfrageergebnisse haben, können auch mehrere Diagramme vorhanden sein.

Wenn kein Diagramm automatisch erkannt wird, Sie aber ein Diagramm aus Ihren Abfrageergebnissen erstellen möchten, klicken Sie mit der rechten Maustaste auf die Daten des Abfrageergebnisses und wählen Sie "Open chart".

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## Diagrammeinstellungen
Verwenden Sie die Schaltfläche {{< mdi "pencil" >}} Customize, um die Diagrammeinstellungen aufzurufen. Sie können die Datenquelle und den Stil des Diagramms konfigurieren:
* Diagrammtyp
  * Balken
  * Linie
  * Zeitachse – ein Sonderfall des Liniendiagramms, mit der Zeit auf der X-Achse
  * Kreis
  * Polarbereich
* Feld der X-Achse – Daten auf der X-Achse. Für Datums-/Zeitwerte stehen Gruppierungs- und Zeitachsenfunktionen zur Verfügung
* Gruppierungsfeld – definiert mehrere Diagramme, die durch den Wert dieses Feldes bestimmt werden
* X-Achsen-Transformation – ermöglicht die Definition einer Gruppierung für die Zeitachse der X-Achse (z. B. nach Jahr oder nach Monat)
* Feld N der Y-Achse – Sie können mehrere Felder auf der Y-Achse haben
  * Für jeden Datensatz steht ein spezielles Feld "Count" zur Verfügung, das Zeilen zählt
* Aggregatfunktion – Summe, Minimum, Maximum, Durchschnitt, Erster Wert, Letzter Wert

Wenn Sie eine Option in den Diagrammeinstellungen ändern, wird sie am Anfang des SQL-Skripts als Front-Matter gespeichert.

## Diagrammdefinition manuell bearbeiten
Einige Optionen sind im Editor nicht verfügbar, können aber im SQL-Code bearbeitet werden. Weitere Informationen finden Sie unter [SQL Front Matter](/de/dbgate/developer/sql-front-matter)
