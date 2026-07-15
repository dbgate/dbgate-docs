---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: it
title: Backup e ripristino
weight: 20
---

DbGate utilizza strumenti nativi per il backup e il ripristino dei database. Questa funzionalità è esclusiva delle edizioni Premium.

Strumenti supportati:

- PostgreSQL
  - `pg_dump` e `psql`
- MySQL+MariaDB
  - `mysqldump` e `mysql`

## Come installare questi strumenti
Non devi preoccuparti di questo se utilizzi l'edizione Team Premium - versioni Docker, AWS o Azure. Questi pacchetti includono già tutti gli strumenti necessari.

Il modo più semplice è installare l'intero motore di database sul tuo desktop.
Tuttavia, per la maggior parte delle piattaforme e dei database, esiste la possibilità di installare solo i client:

- PostgreSQL
  - Windows - scarica e decomprimi il client da https://www.enterprisedb.com/download-postgresql-binaries
  - Mac: installa il client con homebrew: `brew install libpq`
- MySQL:
  - Windows - scarica e decomprimi lo ZIP da https://dev.mysql.com/downloads/mysql/
  - Mac: brew install mysql-client
