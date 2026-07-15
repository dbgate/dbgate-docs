---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: it
title: DbGate Cloud
weight: 80
---

DbGate Cloud è uno spazio di archiviazione online per le tue connessioni, gli script SQL e altri oggetti. Offre inoltre una knowledge base pubblica di script SQL utili.

> DbGate Cloud è un complemento di archiviazione per l'applicazione DbGate **desktop** (connessioni, script SQL, cartelle condivise). Cerchi invece un'applicazione ospitata, utilizzabile solo dal browser? Consulta [DbGate Central](/it/dbgate-central/).

## Accesso
Per utilizzare DbGate Cloud è necessario effettuare l'accesso. Usa l'icona {{< mdi "account-remove-outline" >}} nel pannello di sinistra.

Il tuo spazio di archiviazione cloud è sempre associato al tuo indirizzo e-mail.  
Puoi scegliere uno dei seguenti provider di autenticazione:
* GMail
* GitHub
* E-mail - un magic link di accesso monouso verrà inviato alla tua e-mail

I server di DbGate non memorizzano la tua password.

## Utilizzare le connessioni salvate sul cloud
Il contenuto del tuo cloud appare nel widget {{< mdi "cloud-key" >}} dopo l'accesso. Per impostazione predefinita, vedi la tua cartella Private (con accesso in scrittura).

Salvare una connessione sul cloud:
* Menu contestuale della connessione, scegli "Copy to cloud folder"
* Fai clic su {{<mdi "plus-thick" >}}, poi scegli "Add connection on cloud"

## Quale connessione è salvata sul cloud?
* Le tue connessioni cloud si trovano sempre nel widget {{< mdi "cloud-key" >}}
* Le tue connessioni salvate localmente si trovano nel widget {{< mdi "database" >}}

## Lavorare con le cartelle
Puoi creare ulteriori cartelle oltre alla tua cartella Private (è necessaria l'edizione Premium).

Sotto il pulsante {{<mdi "plus-thick" >}} sono disponibili i comandi:
* New shared folder - crea una nuova cartella condivisa. Per impostazione predefinita è accessibile solo a te, puoi invitare altri utenti
* Add existing shared folder - se hai un link di invito a una cartella condivisa (creata da un altro utente), questo è il posto giusto per utilizzarlo

Se vuoi condividere la tua cartella con altre persone, fai clic con il tasto destro sulla cartella e scegli "Copy invite link"

## Permessi delle cartelle condivise
* Admin - hai accesso completo alla cartella, puoi invitare altre persone e scrivere contenuti
* Write - puoi scrivere/eliminare contenuti, ma non puoi invitare altre persone
* Read - puoi solo leggere il contenuto della cartella. Tieni presente che questo permesso non si applica ai database disponibili all'interno di una connessione definita a livello di server

## Cartelle condivise nell'edizione Community
Nell'edizione Community puoi utilizzare le cartelle condivise create dagli utenti Premium, ma non puoi creare cartelle condivise personali. Questo consente ai team con edizione Premium di condividere connessioni, file SQL e diagrammi ER con altri membri del team che utilizzano l'edizione Community.

## Knowledge base pubblica
La knowledge base pubblica è una raccolta di script SQL e grafici utili per attività come l'ottimizzazione delle prestazioni SQL, l'analisi dei deadlock, l'utilizzo degli indici ecc... La knowledge base è disponibile in tutte le edizioni, ma i grafici sono disponibili solo nelle edizioni Premium.

Puoi vedere tutti gli elementi sotto l'icona {{< mdi "cloud-search" >}} nel pannello dei widget di sinistra.  
Gli script in grigio indicano gli script non compatibili con il database attualmente selezionato.

Se desideri arricchire la knowledge base con i tuoi script SQL, crea una pull request nel repository GIT [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base).

Gli script nella knowledge base sono annotati con la sintassi [SQL front matter](/it/dbgate/developer/sql-front-matter)

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)
