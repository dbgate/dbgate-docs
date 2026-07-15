---
sourceHash: 9faead63589d3a58402650e29cd85afd2223ffa5317dbd506eb962c893c3c04e
language: it
title: Confronta e distribuisci modelli
weight: 15
---

DbGate può confrontare la struttura del database e distribuire le modifiche *(Premium)*. Questo è utile per mantenere sincronizzati gli ambienti e per gestire lo schema con il controllo di versione.

![Compare database](https://media.dbgate.io/img/compare-database-settings-light.png)

## Confronta database

* **Confronta due database** - trova le differenze in colonne, definizioni di viste e altri oggetti SQL.
* **Sincronizza la struttura** - genera ed esegue le azioni necessarie per rendere un database uguale a un altro.
* **Confronta con un modello YAML** - confronta un database reale con un modello memorizzato in YAML e distribuisci le differenze.
* **Impostazioni** - controlla il confronto, ad esempio ignora le chiavi esterne, escludi oggetti specifici o scegli quali azioni di sincronizzazione eseguire.

## Esporta un modello di database

* **Scaffold in una cartella** - salva il modello di un database esistente in una cartella o in un singolo file JSON.
* **File YAML delle tabelle** - le tabelle sono memorizzate come semplici file YAML che puoi conservare in un repository Git.
* **File di definizione SQL** - viste, stored procedure e funzioni sono memorizzate come file SQL.

## Distribuzione

Distribuisci il modello visivamente con lo strumento Compare, oppure dalla riga di comando come parte di una pipeline CI/CD. Per il formato del file del modello e il flusso di lavoro da CLI, vedi [Distribuzione del database](dbdeploy).

## Pagine correlate

* [Editor di tabelle e schemi](schema-editor) - modifica la struttura delle tabelle tramite la GUI
* [Distribuzione del database](dbdeploy) - formato del file del modello e distribuzione da riga di comando
