---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: it
title: Connessione
weight: 20
---

Connettersi al proprio database da DbGate è semplice. È possibile connettersi a un database in diversi modi:

* Menu File/Aggiungi connessione oppure l'icona {{< mdi "plus-thick" >}} nel widget CONNESSIONI
* Menu File/Nuovo database SQLite - crea un nuovo database SQLite
* Menu File/Apri - è possibile aprire un database SQLite esistente

## Schermata di connessione
![Schermata di connessione](https://media.dbgate.io/img/new-connection-light.png)

I campi nella schermata di connessione dipendono in larga misura dal tipo di connessione.

Alcuni campi comuni:

* Server - nome host del server di database
* Port - porta; nel caso della porta predefinita del database, è possibile lasciarla vuota
* User, Password - autenticazione
* Password mode
    * Save and encrypt - la password viene salvata in forma crittografata, non sarà possibile visualizzarla in seguito
    * Save RAW - la password viene salvata così com'è (senza crittografia), è possibile consultarla in seguito
    * Don't save, ask for password - la password non viene salvata, occorre inserirla al momento della connessione
    * Don't save, ask for login and password - non vengono salvati né la password né il nome utente, occorre inserirli entrambi al momento della connessione
* Is read only - la connessione sarà di sola lettura (per i motori che non supportano le sessioni di sola lettura, in questo caso non sarà possibile eseguire query SQL)
* Default database - quale database sarà attivo dopo la connessione
* Use only database *&lt;default database&gt;* - se selezionato, nell'albero delle connessioni compare solo il database predefinito (gli altri database sul server vengono nascosti)
* Display name - nome con cui la connessione apparirà nell'applicazione

## Tunnel SSH
Qui è possibile configurare la connessione tramite tunnel SSH.

Campi comuni:
* Use SSH tunnel - selezionare per utilizzare il tunnel SSH
* Host - nome host del server SSH

![DbGate - configurazione del tunnel SSH](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
Configurare la connessione SSL.

Campi comuni:
* Use SSL - selezionare per utilizzare SSL. Nella maggior parte dei casi, questo è l'unico elemento da configurare per utilizzare SSL

![DbGate - configurazione della connessione SSL](https://media.dbgate.io/img/connection-ssl-window-light.png)
