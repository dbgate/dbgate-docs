---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: cs
title: Záloha a obnovení
weight: 20
---

DbGate používá pro zálohování a obnovení vašich databází nativní nástroje. Tato funkce je dostupná výhradně v edicích Premium.

Podporované nástroje:

- PostgreSQL
  - `pg_dump` a `psql`
- MySQL+MariaDB
  - `mysqldump` a `mysql`

## Jak tyto nástroje nainstalovat
Toto nemusíte řešit, pokud používáte edici Team Premium - verze Docker, AWS nebo Azure. Tyto balíčky již obsahují všechny potřebné nástroje.

Nejjednodušší způsob je nainstalovat na váš počítač celý databázový engine.
Pro většinu platforem a databází však existuje možnost nainstalovat pouze klienty:

- PostgreSQL
  - Windows - stáhněte a rozbalte klienta z https://www.enterprisedb.com/download-postgresql-binaries
  - Mac: nainstalujte klienta pomocí homebrew: `brew install libpq`
- MySQL:
  - Windows - stáhněte a rozbalte ZIP z https://dev.mysql.com/downloads/mysql/
  - Mac: brew install mysql-client
