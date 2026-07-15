---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: pt
title: Backup e restauração
weight: 20
---

O DbGate usa ferramentas nativas para fazer backup e restaurar seus bancos de dados. Esta funcionalidade é exclusiva das edições Premium.

Ferramentas suportadas:

- PostgreSQL
  - `pg_dump` e `psql`
- MySQL+MariaDB
  - `mysqldump` e `mysql`

## Como instalar essas ferramentas
Você não precisa se preocupar com isso se usar a edição Team Premium - versões Docker, AWS ou Azure. Esses pacotes já trazem todas as ferramentas necessárias.

A maneira mais fácil é instalar todo o mecanismo de banco de dados no seu desktop.
No entanto, para a maioria das plataformas e bancos de dados, existe a possibilidade de instalar somente os clientes:

- PostgreSQL
  - Windows - baixe e descompacte o cliente em https://www.enterprisedb.com/download-postgresql-binaries
  - Mac: instale o cliente com o homebrew: `brew install libpq`
- MySQL:
  - Windows - baixe e descompacte o ZIP em https://dev.mysql.com/downloads/mysql/
  - Mac: brew install mysql-client
