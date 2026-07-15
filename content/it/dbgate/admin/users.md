---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: it
title: Utenti
weight: 30
---

## Scheda Users
Configura utenti, password, permessi degli utenti e la mappatura utente-connessione.
Le password vengono utilizzate solo per i metodi di autenticazione "Local". Tuttavia, tutti i metodi con provider di identità esterni utilizzano la ricerca dell'utente, quindi è possibile configurare i permessi e le connessioni disponibili per un utente, anche per un utente autenticato esternamente. 

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### Schede di dettaglio dell'utente
* Info
  * Configura i permessi dell'utente
  * Configura i ruoli assegnati a questo utente
* Team files - configura l'accesso ai [file del team](team-files)
* Connections - configura le connessioni assegnate a questo utente
* Databases - configura i [permessi sui database](permissions#database-permissions) per questo utente
* Tables/views/objects - configura i [permessi sulle tabelle](permissions#table-permissions) per questo utente
* Disk files - configura l'accesso ai file su disco/volume docker
