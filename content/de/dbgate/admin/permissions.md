---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: de
title: Berechtigungen
weight: 50
---

Die Berechtigungen von DbGate nutzen **zwei Dimensionen**:

1. **Quelle der Berechtigungen (wer sie festlegt)**
   Berechtigungen werden von allgemein zu spezifisch vererbt. Spezifischere Einstellungen überschreiben allgemeinere:
   * Vordefinierte Berechtigungssätze
   * Vordefinierte Rollen (*superadmin*, *logged user*, *anonymous*)
   * Benutzerdefinierte Rollen
   * Einzelner Benutzer

2. **Objektbereich**
   Berechtigungen können auf bestimmte **Datenbanken** und **Tabellen/Objekte** abzielen. Siehe **[Datenbankberechtigungen](#database-permissions)** und **[Tabellenberechtigungen](#table-permissions)**.

---

## Grundlegende Berechtigungen

Globale/grundlegende Berechtigungen konfigurieren Sie im **Berechtigungsbaum** im **Benutzerdetail** oder **Rollendetail**.

* Ein **ausgegrautes** Kontrollkästchen bedeutet, dass die Berechtigung **vererbt** ist (z. B. von einer Rolle oder einem vordefinierten Berechtigungssatz) und nicht direkt für diesen Benutzer bzw. diese Rolle gesetzt wurde.

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## Datenbankberechtigungen

Berechtigungen auf Datenbankebene legen Sie auf der Registerkarte **Databases** fest (sowohl im Rollendetail als auch im Benutzerdetail).

> **Wichtig:** Datenbankregeln werden **nur dann** angewendet, wenn die Berechtigung **„All databases“** in den grundlegenden Berechtigungen deaktiviert ist.

* Jede Zeile in der Regeltabelle erlaubt oder verweigert den Zugriff auf Datenbanken, die den Filtern der Zeile **entsprechen**.
* **Die Reihenfolge der Regeln ist wichtig**: Regeln **weiter unten** in der Liste **überschreiben** die Regeln darüber.

![Database permissions - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**Spalten**

* **Connection** – auf welche Verbindung die Regel angewendet wird.
* **Database names** – zu treffende Datenbanken (Liste von Namen oder ein regulärer Ausdruck).
* **Role (Zugriffsebene)**
  * **View** – kann die Datenbank sehen, aber nicht deren Tabellen/Views/usw.
  * **Read content** – schreibgeschützter Zugriff auf den Datenbankinhalt.
  * **Write data** – kann Tabellendaten ändern.
  * **Run script** – kann beliebige SQL-Skripte ausführen; kann Objekte erstellen/löschen/ändern.
  * **Deny** – blockiert den Zugriff auf die Datenbank.

---

## Tabellenberechtigungen

Berechtigungen auf Tabellen-/Objektebene legen Sie auf der Registerkarte **Tables / Views / Objects** fest (im Rollendetail und im Benutzerdetail).

> **Wichtig:** Tabellen-/Objektregeln werden **nur dann** angewendet, wenn die Berechtigung **„All tables/views/objects“** in den grundlegenden Berechtigungen deaktiviert ist.

* Jede Zeile definiert den Zugriff auf Tabellen/Objekte, die den Filtern **entsprechen**.
* **Die Reihenfolge der Regeln ist wichtig**: Regeln **weiter unten** in der Liste **überschreiben** die Regeln darüber.
* Standardmäßig werden Tabellenberechtigungen **von der Datenbankberechtigung vererbt**.

**Spalten**

* **Connection** – auf welche Verbindung die Regel angewendet wird.
* **Database names** – zu treffende Datenbanken (Liste oder regulärer Ausdruck).
* **Schema names** – zu treffende Schemas (Liste oder regulärer Ausdruck).
* **Table names** – zu treffende Objektnamen (Tabelle/View/Prozedur/Trigger) als Liste oder regulärer Ausdruck.
* **Scope** – welche Objekttypen die Regel abdeckt (Tabellen, Views, Prozeduren, Trigger, …).
* **Role (Zugriffsebene)**
  * **Read** – kann Tabellendaten lesen.
  * **Update only** – kann Zeilen aktualisieren; **Einfügen** und **Löschen** sind nicht erlaubt.
  * **Create, update, delete** - kann Zeilen ohne Einschränkungen bearbeiten
  * **Run script** – kann ein Skript ausführen, das dieses Objekt berührt.
    > Hinweis: Wenn Sie **„Run script“** nicht auf **Datenbankebene** haben, können Sie es auch nicht auf Tabellenebene verwenden.
  * **Deny** – blockiert den Zugriff auf das Objekt.

