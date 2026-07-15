---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: de
title: Backup & Wiederherstellung
weight: 20
---

DbGate verwendet native Tools zum Sichern und Wiederherstellen Ihrer Datenbanken. Diese Funktionalität ist exklusiv den Premium-Editionen vorbehalten.

Unterstützte Tools:

- PostgreSQL
  - `pg_dump` und `psql`
- MySQL+MariaDB
  - `mysqldump` und `mysql`

## Installation dieser Tools
Sie müssen sich darum nicht kümmern, wenn Sie die Team Premium Edition verwenden – Docker-, AWS- oder Azure-Versionen. In diesen Paketen sind bereits alle benötigten Tools enthalten.

Am einfachsten ist es, die gesamte Datenbank-Engine auf Ihrem Desktop zu installieren.
Für die meisten Plattformen und Datenbanken besteht jedoch die Möglichkeit, nur die Clients zu installieren:

- PostgreSQL
  - Windows – Client herunterladen und entpacken von https://www.enterprisedb.com/download-postgresql-binaries
  - Mac: Client mit Homebrew installieren: `brew install libpq`
- MySQL:
  - Windows – ZIP herunterladen und entpacken von https://dev.mysql.com/downloads/mysql/
  - Mac: brew install mysql-client
