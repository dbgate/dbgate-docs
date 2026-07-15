---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: it
title: Team Premium su Docker
weight: 30
---

Una tipica installazione di Team Premium è composta da due componenti: 
- Container docker del server DbGate
- Server di database (MS SQL, MySQL, PostgreSQL, Oracle) - database di archiviazione interno per connessioni, utenti e ruoli. È possibile utilizzare un server di database esistente oppure installarne uno nuovo.

## Container Docker del server DbGate
Utilizza l'[immagine DbGate Team Premium](https://hub.docker.com/r/dbgate/dbgate-premium) da Docker Hub:
```
docker pull dbgate/dbgate-premium
```

Il container DbGate Team Premium richiede l'impostazione di alcune variabili d'ambiente:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - definiscono la connessione al database di archiviazione interno

Consulta la [documentazione delle variabili d'ambiente](/it/dbgate/customization/env-variables/#team-premium-edition-configuration) per maggiori dettagli sulle variabili d'ambiente disponibili.

## Requisiti di risorse

In realtà, DbGate Team Premium ha un consumo di risorse molto basso, ma per ottenere le migliori prestazioni consigliamo la seguente configurazione (per 10 utenti simultanei):
- 2 core CPU
- 4 GB di RAM (include il consumo di RAM del database di archiviazione interno MySQL o PostgreSQL)
- 10 GB di spazio libero su disco (per l'installazione docker, il database di archiviazione, i file temporanei, i risultati delle query, ecc. Il consumo effettivo di spazio su disco dipende dalle modalità di utilizzo)

Per un numero inferiore di utenti, è possibile utilizzare limiti di risorse più bassi (1 GB di RAM, 1 core CPU).  
Quando è necessario ridurre al minimo il consumo di risorse per installazioni di piccole dimensioni, consigliamo di utilizzare MySQL/MariaDB come archiviazione interna.  

## Configurazione di docker

Se desideri utilizzare i file su disco per l'archiviazione dei file utente (come l'esportazione dei risultati delle query), devi mappare il percorso `/root/.dbgate` nel container.

Di seguito è riportato un esempio di file `docker-compose.yml`, che definisce il container DbGate Team Premium con PostgreSQL come database di archiviazione interno.
- È possibile definire la variabile d'ambiente `DBGATE_LICENSE` per impostare la chiave di licenza. Se non è impostata, DbGate richiederà la chiave di licenza al primo avvio.
-  È possibile definire la variabile d'ambiente 'ADMIN_PASSWORD' per impostare la password dell'utente admin. Se non è impostata, DbGate richiederà la password di admin al primo avvio.

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## Stateless/Statefulness
Il container DbGate è stateful. 

I seguenti dati sono memorizzati all'interno del container:
* Sessioni degli utenti connessi
* Stati di esecuzione delle query
* File temporanei (come i risultati)
* Transazioni di database aperte
* Connessioni di database aperte

Non è possibile eseguire correttamente più container DbGate dietro un load balancer, perché i dati sopra indicati non sono condivisi tra i container.

## Server DbGate da NPM
Se la tua infrastruttura non supporta Docker, puoi utilizzare il [pacchetto NPM DbGate Team Premium](https://www.npmjs.com/package/dbgate-serve-premium):
```
npm install -g dbgate-serve-premium
```
 
## Isolamento dei processi
DbGate Team Premium utilizza l'isolamento dei processi a livello di connessione al database, in modo che più utenti possano utilizzare lo stesso server di database senza interferenze. Il processo derivato da DbGate cresce con il numero di utenti e connessioni attive, quindi assicurati che il tuo server disponga di risorse sufficienti.
Le seguenti entità sono isolate in un nuovo processo:
* Connessioni ai server
* Connessioni ai database
* Sessioni di query
* Esecuzione di job di esportazione/importazione
* Tunneling SSH
