---
sourceHash: 9faead63589d3a58402650e29cd85afd2223ffa5317dbd506eb962c893c3c04e
language: de
title: Modelle vergleichen & bereitstellen
weight: 15
---

DbGate kann Datenbankstrukturen vergleichen und Änderungen bereitstellen *(Premium)*. Das ist nützlich, um Umgebungen synchron zu halten und Ihr Schema unter Versionskontrolle zu stellen.

![Compare database](https://media.dbgate.io/img/compare-database-settings-light.png)

## Datenbanken vergleichen

* **Zwei Datenbanken vergleichen** - Unterschiede in Spalten, View-Definitionen und anderen SQL-Objekten finden.
* **Struktur synchronisieren** - die Aktionen generieren und ausführen, die nötig sind, damit eine Datenbank einer anderen entspricht.
* **Mit einem YAML-Modell vergleichen** - eine echte Datenbank mit einem in YAML gespeicherten Modell vergleichen und die Unterschiede bereitstellen.
* **Einstellungen** - den Vergleich steuern, zum Beispiel Fremdschlüssel ignorieren, bestimmte Objekte ausschließen oder auswählen, welche Synchronisierungsaktionen ausgeführt werden.

## Ein Datenbankmodell exportieren

* **Scaffolding in einen Ordner** - das Modell einer bestehenden Datenbank in einem Ordner oder in einer einzelnen JSON-Datei speichern.
* **YAML-Tabellendateien** - Tabellen werden als einfache YAML-Dateien gespeichert, die Sie in einem Git-Repository verwalten können.
* **SQL-Definitionsdateien** - Views, Stored Procedures und Funktionen werden als SQL-Dateien gespeichert.

## Bereitstellen

Stellen Sie das Modell visuell mit dem Compare-Werkzeug bereit oder über die Kommandozeile als Teil einer CI/CD-Pipeline. Zum Modelldateiformat und zum CLI-Workflow siehe [Datenbank-Deployment](dbdeploy).

## Verwandte Seiten

* [Tabellen- & Schema-Editor](schema-editor) - Tabellenstruktur über die GUI bearbeiten
* [Datenbank-Deployment](dbdeploy) - Modelldateiformat und Deployment über die Kommandozeile
