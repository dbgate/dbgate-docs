---
sourceHash: a1e2c8e626b7d397e242c5a182c920ca58971109a164a8c90e909a521a92e5db
language: de
title: Karten
weight: 40
---

DbGate unterstützt die Anzeige geografischer Daten in Karten.

## Unterstützte Kartenquellen
- MySQL: Alle räumlichen Spalten
- MSSQL: GEOGRAPHY-Spalten
- PostGIS: GEOGRAPHY-Spalten
- Alle Datenquellen: Koordinaten, die in Breitengrad-/Längengrad-Spalten gespeichert sind

## Kartenansicht aufrufen
Die Kartenansicht wird aus dem Datenraster aufgerufen. Wählen Sie zuerst Zellen mit den gewünschten geografischen Daten aus. Am einfachsten ist es, eine GEOGRAPHY- oder GEOMETRY-Zelle auszuwählen. Sie können auch mehrere Zeilen auswählen. Klicken Sie dann auf das Widget „Zelldaten“. Im Zelldaten-Widget sollte nun die Karte angezeigt werden.

![screenshot](/img/map1.png)

Wenn Sie Breitengrad- und Längengrad-Spalten gespeichert haben, wählen Sie alle Daten aus, die Sie in der Karte haben möchten. Spalten, die weder Breitengrad noch Längengrad sind, werden in den Popups der Markierungen angezeigt.

![screenshot](/img/map2.png)

Alternativ können Sie im Datenraster das Kontextmenü „Auswahl in Karte öffnen“ auf den ausgewählten Zellen verwenden; dann wird ein neuer Tab mit der Karte geöffnet.

Im Kontextmenü der Karte gibt es außerdem die Möglichkeit, die Karte in eine eigenständige HTML-Datei zu exportieren, die überall dort angezeigt werden kann, wo DbGate nicht installiert ist.