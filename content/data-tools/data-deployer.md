---
title: Data deployer
weight: 2
---

## Data deployer
With data deployer, you could visually compare and sycnhronize your data in **archive folders** with **real database**
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Run data deployer
You could run data deployer from database context menu or from archive folder context menu. When running archive database, you will be asked to choose archive. When running from archive, data deployer will be started with current database.

## Settings
- Database server, database - choose database to work with
- Data archive - choose folder with data, which will be used for compare and synchronize
### Table related
- Key (match columns) - choose columns, which will be used for matching rows between database and archive
### Replicator settings
Settings below ("table" - deploy and Global data deploy settings) are specific for replicator and are described in [Data replicator](data-replicator) topic

## Copy data differences
Data deployer shows differences between data in archive and in database. If you select some cells with difference, you could write these differences to archive or to database. If these cells are selected, nn right bottom corner appears buttons allowing synchronization:
- Write x rows, y columns to archive - copy selected cells from database to archive.
- Write x rows, y columns to database - copy selected cells from archive to database. Confirmation dialog with change SQL is displayed at first.

## Data replicator actions
- Deploy into DB - this action deploys changes into database with configured settings
- Generate shell - this action creates JavaScript file, which will run deploy. This file could be run from command-line
- Generate SQL - creates SQL, which deploys changes from archive into database

More about these actions in [Data replicator](data-replicator) topic