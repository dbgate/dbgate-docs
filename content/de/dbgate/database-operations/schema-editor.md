---
sourceHash: 0f10d627c0492363d84834c24da993d0686916c833728726a2d34648885161b1
language: de
title: Tabellen- & Schema-Editor
weight: 5
---

DbGate kann Datenbankstrukturen über eine grafische Oberfläche erstellen und ändern, ohne dass Sie DDL von Hand schreiben müssen. Öffnen Sie den Strukturen-Editor einer Tabelle über deren Kontextmenü ("Edit table") oder erstellen Sie eine neue Tabelle über das Kontextmenü der Datenbank.

![Tabellenstruktur-Editor](https://media.dbgate.io/img/table-structure-editor-light.png)

## Tabellen bearbeiten

* **Spalten und Datentypen** - definieren Sie Spalten, Datentypen, Nullbarkeit und Standardwerte für neue oder bestehende Tabellen.
* **Schlüssel und Indizes** - verwalten Sie Primärschlüssel, Fremdschlüssel und Indizes.
* **Engine-spezifische Eigenschaften** - legen Sie datenbankspezifische Optionen fest, wie z. B. die MySQL-Tabellen-Engine.

## SQL-Vorschau und sichere Änderungen

* **SQL-Vorschau** - bevor etwas gespeichert wird, zeigt DbGate das generierte SQL an, damit Sie es prüfen können.
* **Warnung beim Neuerstellen von Tabellen** - wenn eine Änderung das Neuerstellen der Tabelle erfordert (eine Einschränkung mancher Datenbanken), warnt DbGate Sie und lässt Sie zuerst das generierte Skript einsehen.

## Weitere Datenbankobjekte

Sie können auch andere Objekte erstellen, löschen und ändern - Views, Stored Procedures und Funktionen - sowie Tabellen, Views, Prozeduren, Funktionen und MongoDB-Collections im Objektbaum durchsuchen.

## Verwandte Seiten

* [Modelle vergleichen & bereitstellen](model-compare-deploy) - Struktur zwischen Datenbanken vergleichen und Änderungen bereitstellen *(Premium)*
* [Datenbank-Deployment](dbdeploy) - YAML/SQL-Modelldateien und CLI-Deployment
