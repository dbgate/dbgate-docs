---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: de
title: Query-Designer
weight: 20
---

Der Query-Designer *(Premium)* ermöglicht es Ihnen, SQL-Abfragen visuell zu erstellen, ohne SQL von Hand zu schreiben. Fügen Sie Tabellen zur Arbeitsfläche hinzu, wählen Sie Spalten aus und definieren Sie Bedingungen - DbGate generiert das SQL für Sie.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## Erstellen einer Abfrage

* **Tabellen hinzufügen** - ziehen Sie Tabellen auf die Design-Arbeitsfläche; DbGate zeichnet Beziehungen automatisch anhand von Fremdschlüsseln.
* **Spalten auswählen** - wählen Sie, welche Spalten im Ergebnis erscheinen, und definieren Sie Sortierung und Gruppierung.
* **JOIN-Typen** - neben den standardmäßigen SQL-Joins (`INNER`, `LEFT`, `RIGHT`) können Sie Pseudo-Joins verwenden - der nützlichste davon ist `WHERE NOT EXISTS`.
* **Leistungsstarke Filter** - filtern Sie mit derselben Engine wie im [Daten-Browser](/de/dbgate/working-with-data/data-browser/), einschließlich zusammengesetzter Bedingungen und Filterung nach einer Wertemenge.

## Ergebnis

Der Designer erzeugt eine normale SQL-Abfrage, sodass sie mit derselben Performance läuft wie handgeschriebenes SQL. Sie können jederzeit zum generierten SQL wechseln und es im [SQL-Editor](sql-editor) weiter bearbeiten.

## Perspectives - der universelle Designer

Für verschachtelte, hierarchische Ansichten - und zum clientseitigen Verknüpfen von Daten über SQL-Tabellen und MongoDB-Collections hinweg - verwenden Sie [Perspectives](/de/dbgate/working-with-data/perspectives/), die nicht durch das eingeschränkt sind, was die Quelldatenbank verknüpfen kann.
