---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: de
title: Datenfilterung
weight: 10
---

DbGate verfügt über eine leistungsfähige Engine zur Datenfilterung, die sowohl sehr einfache Filter als auch komplexe Bedingungen ermöglicht.

Datenfilter können an vielen Stellen in DbGate verwendet werden, am häufigsten jedoch zum Filtern des Datengitters.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

Filter werden mit einem Hintergrund eingefärbt:
* Grüner Hintergrund - der Filter ist korrekt und wird angewendet
* Roter Hintergrund - der Filterausdruck enthält einen Fehler, der Filter wird ignoriert

Sie haben mehrere Möglichkeiten, einen Filter zu erstellen:
* {{< mdi "filter" >}} - zeigt ein Menü mit vordefinierten Filtern und Dialogen an
* {{< mdi "dots-vertical" >}} - ermöglicht die Auswahl der zu filternden Werte
* Sie können den Filter direkt schreiben - verwenden Sie die sehr einfache Syntax, die unter [filter-expressions](#filter-expressions) beschrieben ist
* Oder Sie erstellen den Filter mit visuellen Methoden und bearbeiten ihn anschließend manuell

Weitere Befehle:
* {{< mdi "filter-off" >}} - alle Filter löschen

## Filterausdrücke
Filterausdrücke sind so gestaltet, dass sie intuitiv sind: In den meisten Fällen schreiben Sie einfach direkt das, wonach Sie suchen möchten. Die Syntax ist jedoch sehr leistungsfähig, Sie können mehrere Bedingungen kombinieren und verschiedene Operatoren verwenden.
Die Syntax des Ausdrucks hängt vom Datentyp der Spalte ab.

### Beispiele

| Spaltentyp | Filterausdruck |  Beschreibung |
|----------|-------------|------|
| string | canada | Spaltenwert enthält den Text "canada" |
| string | canada, usa | Spaltenwert enthält den Text "canada" oder "usa" |
| string | canada lake | Spaltenwert enthält den Text "canada" und "lake" |
| string | NOT EMPTY NOT NULL | Zeichenkette hat einen nicht leeren Wert |
| number | >10 | Spaltenwert ist größer als 10 |
| number | >=5 <=10 | Spaltenwert liegt zwischen 5 und 10 |
| number | 1,2,3 | Spaltenwert ist 1 oder 2 oder 3 |
| datetime | 2020-05-26 | Datumswert stammt vom 2020-05-26 (24-Stunden-Intervall)  |

### Allgemeine Filter (für alle Datentypen)
- NULL - Spaltenwert ist null
- NOT NULL - Spaltenwert ist nicht null
- {$$ is null} - SQL-Bedingung, geschrieben in geschweiften Klammern {}. $$ ist ein Platzhalter für die gefilterte Spalte

### Textfilter
Der Textvergleich unterscheidet nicht zwischen Groß- und Kleinschreibung.
- text - Spaltenwert enthält _text_. Kann in 'einfachen Anführungszeichen' oder "doppelten Anführungszeichen" stehen
- +text - Spaltenwert enthält _text_ (dasselbe wie in der Zeile darüber)
- ^text - Spaltenwert beginnt mit _text_
- $text - Spaltenwert endet mit _text_
- !+text - Spaltenwert enthält _text_ nicht (dasselbe wie in der Zeile darüber)
- !^text - Spaltenwert beginnt nicht mit _text_
- !$text - Spaltenwert endet nicht mit _text_
- EMPTY - Spaltenwert enthält kein Zeichen außer Leerraum
- NOT EMPTY - Spaltenwert enthält ein Zeichen außer Leerraum

### Zahlenfilter
- number - Spaltenwert ist gleich der Zahl
- =number - Spaltenwert ist gleich der Zahl
- !=number - Spaltenwert ist ungleich der Zahl
- <>number - Spaltenwert ist ungleich der Zahl
- <number - Spaltenwert ist kleiner als die Zahl
- \>number - Spaltenwert ist größer als die Zahl
- <=number - Spaltenwert ist kleiner oder gleich der Zahl
- \>=number - Spaltenwert ist größer oder gleich der Zahl

### Datums-/Zeitfilter
- 2021 - Jahr des Spaltenwerts
- 2021-02 - Jahr, Monat des Spaltenwerts
- 2021-02-15 - Jahr, Monat, Tag des Spaltenwerts
- 2021-02-15 23:15 - Jahr, Monat, Tag, Stunde, Minute des Spaltenwerts
- 2021-02-15 23:15:51 - Jahr, Monat, Tag, Stunde, Minute, Sekunde des Spaltenwerts
- Filter relativ zum aktuellen Datum
  - YESTERDAY
  - TODAY
  - TOMORROW
  - LAST WEEK
  - THIS WEEK
  - NEXT WEEK
  - LAST MONTH
  - THIS MONTH
  - NEXT MONTH
  - LAST YEAR
  - THIS YEAR
  - NEXT YEAR

### Logische (boolesche) Filter
- TRUE, true, 1 - Spaltenwert ist true/1
- FALSE, false, 0 - Spaltenwert ist false/0

### Kombinationen von Filtern
Filter können miteinander kombiniert werden. Ein Leerzeichen wird als AND-Operator interpretiert, ein Komma als OR-Operator. AND hat eine höhere Priorität als OR.
