---
sourceHash: 98567960505dd913b53691e56158219d62b00d924912216d2b21b7fe2c557623
language: fr
title: Sauvegarde et restauration
weight: 20
---

DbGate utilise des outils natifs pour sauvegarder et restaurer vos bases de données. Cette fonctionnalité est exclusive aux éditions Premium.

Outils pris en charge :

- PostgreSQL
  - `pg_dump` et `psql`
- MySQL+MariaDB
  - `mysqldump` et `mysql`

## Comment installer ces outils
Vous n'avez pas à vous en préoccuper si vous utilisez l'édition Team Premium - versions Docker, AWS ou Azure. Ces paquets contiennent déjà tous les outils nécessaires.

Le moyen le plus simple est d'installer l'ensemble du moteur de base de données sur votre poste de travail.
Cependant, pour la plupart des plateformes et des bases de données, il est possible d'installer uniquement les clients :

- PostgreSQL
  - Windows - téléchargez et décompressez le client depuis https://www.enterprisedb.com/download-postgresql-binaries
  - Mac : installez le client avec homebrew : `brew install libpq`
- MySQL :
  - Windows - téléchargez et décompressez le fichier ZIP depuis https://dev.mysql.com/downloads/mysql/
  - Mac : brew install mysql-client
