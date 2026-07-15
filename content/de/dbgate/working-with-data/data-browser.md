---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: de
title: Datenbrowser & Editor
weight: 5
---

Der Datenbrowser ist die zentrale Ansicht von DbGate zum Betrachten und Bearbeiten von Tabellendaten. Öffnen Sie eine beliebige Tabelle, View oder Collection und Sie erhalten ein schnelles, Excel-ähnliches Raster. Diese Seite behandelt das Durchsuchen, Bearbeiten und Navigieren verknüpfter Daten; Filterausdrücke finden Sie unter [Datenfilterung](data-filtering).

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## Daten durchsuchen

* **Tastaturnavigation** - bewegen Sie sich mit den Pfeiltasten durch das Raster, wie in einer Tabellenkalkulation.
* **Sortieren** - klicken Sie auf eine Spaltenüberschrift, um nach dieser Spalte zu sortieren.
* **Filtern** - filtern Sie Zeilen über die Filterzeile oberhalb des Rasters; die vollständige Ausdruckssyntax finden Sie unter [Datenfilterung](data-filtering).
* **Spaltenmanager** - finden Sie Spalten anhand ihres Namens und blenden Sie nicht benötigte Spalten aus.
* **Erweitertes Kopieren** - kopieren Sie ausgewählte Zellen als CSV, YAML, SQL-`INSERT`s oder MongoDB-Inserts.

## Daten bearbeiten

Die Datenbearbeitung erfolgt direkt im Raster:

* **Excel-ähnliche Bearbeitung** - bearbeiten Sie Zellen an Ort und Stelle; kopieren und fügen Sie Zeilenbereiche ein, auch zwischen Tabellen.
* **Vorgemerkte Änderungen** - Ihre Bearbeitungen werden als ausstehende Änderungen gesammelt. Prüfen Sie das generierte SQL-Änderungsskript, bevor es die Datenbank berührt, und wählen Sie dann Speichern oder Verwerfen.
* **Zeilen einfügen und löschen** über das Raster oder das Kontextmenü.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### Makros für den Dateneditor *(Premium)*

Wenden Sie vordefinierte Makros auf die ausgewählten Zellen an - zum Beispiel Groß-/Kleinschreibung ändern, Diakritika entfernen oder eine UUID generieren.

## Arbeiten mit verknüpften Daten

DbGate macht es einfach, Beziehungen zwischen Tabellen zu folgen:

* **Beziehungshinweise** - sehen Sie einen Textwert aus der referenzierten Tabelle neben einem numerischen Fremdschlüssel.
* **Erweiterung von Fremdschlüsselspalten** - erweitern Sie eine Fremdschlüsselspalte, um referenzierte Daten inline anzuzeigen.
* **Detail öffnen** - springen Sie zur referenzierten Zeile eines Fremdschlüssels.
* **Master/Detail-Ansichten** *(Premium)* - erkunden Sie verknüpfte Zeilen in einem verbundenen Master/Detail-Layout.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## Formularansicht

Die Formularansicht zeigt eine einzelne Zeile als vertikale, "transponierte" Liste - ideal für Tabellen mit vielen Spalten. Sie funktioniert als Baumansicht, sodass Fremdschlüsselspalten erweitert werden können, um verknüpfte Daten zu erkunden.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## Gruppierung *(Premium)*

Wenden Sie eine Gruppierung (`GROUP BY`) in der Rasteransicht an, um Zeilen direkt beim Durchsuchen zu aggregieren.

## Verwandte Seiten

* [Datenfilterung](data-filtering) - Syntax von Filterausdrücken
* [Export & Import](export-import) - Daten in Tabellen hinein- und herausbewegen
* [Perspektiven](perspectives) - verschachtelte, schreibgeschützte Ansichten über komplexe verknüpfte Daten
* [SQL-Editor](/de/dbgate/sql-and-queries/sql-editor/) - Abfrageergebnisse auf dieselbe Weise bearbeiten *(Premium)*
