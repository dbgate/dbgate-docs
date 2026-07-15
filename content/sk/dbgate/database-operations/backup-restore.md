---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: sk
title: Zálohovanie a obnova
weight: 20
---

DbGate používa na zálohovanie a obnovu vašich databáz natívne nástroje. Táto funkcia je dostupná výhradne v edíciách Premium.

Podporované nástroje:

- PostgreSQL
  - `pg_dump` a `psql`
- MySQL+MariaDB
  - `mysqldump` a `mysql`

## Ako tieto nástroje nainštalovať
Toto nemusíte riešiť, ak používate edíciu Team Premium - verzie Docker, AWS alebo Azure. Tieto balíky už majú všetky potrebné nástroje pribalené.

Najjednoduchším spôsobom je nainštalovať si na počítač celý databázový engine.
Pri väčšine platforiem a databáz však existuje možnosť nainštalovať iba klientov:

- PostgreSQL
  - Windows - stiahnite a rozbaľte klienta z https://www.enterprisedb.com/download-postgresql-binaries
  - Mac: nainštalujte klienta pomocou homebrew: `brew install libpq`
- MySQL:
  - Windows - stiahnite a rozbaľte ZIP z https://dev.mysql.com/downloads/mysql/
  - Mac: brew install mysql-client
