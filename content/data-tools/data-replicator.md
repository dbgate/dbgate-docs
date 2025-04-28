---
title: Data replicator
weight: 3
---

## Data replicator
Data replicator is feature, which allows importing related data in data archives into SQL database. It could be started from data archive context menu, choose "Data deployer". This menu is visible only when you have selected current database. Data replicator then shows you settings for duplicating your archive.

![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-replicator-light.png)

Operations supported:
- Copy row - insert new row into database from data archive. Autoincrement id is used for references to this table.,
- Lookup (find matching row) - nothing is inserted. Duplicator finds matched row (by column defined in "Marched column") and uses it in ther references.
- Insert if not exists - combination of preceding tow options. Lookup, it no row is matched, copy row

