---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: de
title: Perspektiven
weight: 50
---

Eine Perspektive ist eine schreibgeschützte Ansicht komplexer, verschachtelter Daten. Sie ähnelt Berichten, allerdings werden Perspektiven einfach durch Hinzufügen von Daten zur Ansicht erstellt. Sie können den Perspektiven-Designer verwenden, mit dem sich Daten auch über andere Beziehungen als Fremdschlüssel verknüpfen lassen.

Perspektiven können Daten problemlos miteinander verknüpfen und Gruppen anzeigen.

<!-- ![screenshot](/screenshots/perspective1.png) -->

## Perspektive erstellen
Perspektiven können aus SQL-Tabellen und -Views erstellt werden (MongoDB-Collections werden noch nicht unterstützt, diese Unterstützung ist jedoch geplant).
Verwenden Sie das Kontextmenü der Tabelle bzw. des Views, „Perspektive öffnen“.

![screenshot](/img/perspective-create.png)

DbGate öffnet eine einfache Perspektive, in der nur eine Spalte angezeigt wird. Diese Spalte wird durch einen heuristischen Algorithmus so gewählt, dass sie die gesamte Zeile bestmöglich repräsentiert.
## Perspektive anpassen
Sie können festlegen, welche Spalten in der Ansicht verfügbar sind. Außerdem können Sie referenzierte Daten zur Ansicht hinzufügen. Verwenden Sie die Aufklapp-Schaltfläche, um den Referenzbaum zu durchsuchen.

## Daten filtern
Verwenden Sie das Kontextmenü in der Tabelle oder in der Spaltenliste auf der linken Seite, „Zum Filter hinzufügen“. Sie können dieselben Filterausdrücke wie an anderen Stellen in DbGate verwenden. Oder Sie nutzen den Kontextmenübefehl „Diesen Wert filtern“ auf einer Tabellenzelle.

## Übergeordnete Zeilen filtern
Nehmen wir folgende Perspektive an. Wir haben eine Master/Detail-Beziehung, Genre, mit den zugehörigen Tracks. Wir möchten nach Track filtern (ich habe versucht, nach dem Text „mix“ zu suchen).

![screenshot](/img/parentrows1.png)

Wie Sie sehen, gibt es viele Genre-Zeilen ohne einen Track, der den Suchkriterien entspricht. Wenn Sie auch die Genre-Zeilen filtern möchten, verwenden Sie den Befehl „Übergeordnete Zeilen filtern“ im Kontextmenü der Tabellenkopfzeile. Sie können auch die Umschalt-Schaltfläche in der Filterzeile verwenden.

![screenshot](/img/parentrows2.png)

## Benutzerdefinierte Joins definieren
Perspektiven funktionieren sehr gut mit Fremdschlüsseln. Aber auch wenn Sie eine Datenbank ohne Fremdschlüssel haben, können Sie diese Funktion nutzen. Es ist möglich, einen benutzerdefinierten Join mit einer beliebigen Bedingung zu definieren. Sie können sogar einen benutzerdefinierten Join zu einer anderen Datenbank definieren (die sich auf einem anderen DB-Server befinden kann, sogar mit einer anderen zugrunde liegenden Datenbank-Engine).

![screenshot](/img/customjoin.png)

Sie können auch Spalten per Drag &amp; Drop ziehen, um eine Join-Beziehung zu erstellen.

![screenshot](/img/customjoin2.png)
