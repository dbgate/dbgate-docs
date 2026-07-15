---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: es
title: Copia de seguridad y restauración
weight: 20
---

DbGate utiliza herramientas nativas para realizar copias de seguridad y restaurar sus bases de datos. Esta funcionalidad es exclusiva de las ediciones Premium.

Herramientas compatibles:

- PostgreSQL
  - `pg_dump` y `psql`
- MySQL+MariaDB
  - `mysqldump` y `mysql`

## Cómo instalar estas herramientas
No tiene que resolver esto si utiliza la edición Team Premium: las versiones de Docker, AWS o Azure. Estos paquetes ya incluyen todas las herramientas necesarias.

La forma más sencilla es instalar todo el motor de base de datos en su equipo de escritorio.
Sin embargo, para la mayoría de las plataformas y bases de datos, existe la posibilidad de instalar solo los clientes:

- PostgreSQL
  - Windows: descargue y descomprima el cliente desde https://www.enterprisedb.com/download-postgresql-binaries
  - Mac: instale el cliente con homebrew: `brew install libpq`
- MySQL:
  - Windows: descargue y descomprima el archivo ZIP desde https://dev.mysql.com/downloads/mysql/
  - Mac: brew install mysql-client
