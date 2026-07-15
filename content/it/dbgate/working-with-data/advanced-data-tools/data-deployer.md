---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: it
title: Data deployer
weight: 2
---

Con il data deployer puoi confrontare e sincronizzare visivamente i tuoi dati nelle **cartelle di archivio** con il **database reale**
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Eseguire il data deployer
Puoi eseguire il data deployer dal menu contestuale del database o dal menu contestuale della cartella di archivio. Quando lo esegui dal database, ti verrà chiesto di scegliere un archivio. Quando lo esegui da un archivio, il data deployer verrà avviato con il database corrente.

## Impostazioni
- Database server, database - scegli il database con cui lavorare
- Data archive - scegli la cartella con i dati che verrà utilizzata per il confronto e la sincronizzazione
### Relative alla tabella
- Key (match columns) - scegli le colonne che verranno utilizzate per la corrispondenza delle righe tra database e archivio
### Impostazioni del replicator
Le impostazioni riportate di seguito ("table" - deploy e le impostazioni globali di data deploy) sono specifiche del replicator e sono descritte nell'argomento [Data replicator](data-replicator)

## Copiare le differenze tra i dati
Il data deployer mostra le differenze tra i dati nell'archivio e nel database. Se selezioni alcune celle con differenze, puoi scrivere queste differenze nell'archivio o nel database. Se queste celle sono selezionate, nell'angolo in basso a destra compaiono i pulsanti che consentono la sincronizzazione:
- Write x rows, y columns to archive - copia le celle selezionate dal database all'archivio.
- Write x rows, y columns to database - copia le celle selezionate dall'archivio al database. Viene visualizzata prima una finestra di conferma con l'SQL delle modifiche.

## Azioni del data replicator
- Deploy into DB - questa azione distribuisce le modifiche nel database con le impostazioni configurate
- Generate shell - questa azione crea un file JavaScript che eseguirà il deploy. Questo file può essere eseguito da riga di comando
- Generate SQL - crea l'SQL che distribuisce le modifiche dall'archivio nel database

Maggiori informazioni su queste azioni nell'argomento [Data replicator](data-replicator)
