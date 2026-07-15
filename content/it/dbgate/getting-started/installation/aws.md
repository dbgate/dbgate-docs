---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: it
title: Deploy su AWS
subtitle: Deploy con un solo clic su un cluster Amazon EC2
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

DbGate AWS edition è una piattaforma web collaborativa e multiutente progettata specificamente per la gestione dei database all'interno di Amazon Web Services (AWS). Sfruttando l'infrastruttura AWS, semplifica il lavoro di squadra per le organizzazioni che operano in ambienti cloud. La sua interfaccia condivisa, basata su browser, semplifica la collaborazione, l'accesso ai dati e la supervisione dei database, integrandosi perfettamente con AWS.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate su AWS{{< /button >}}

## Funzionalità principali di DbGate AWS
DbGate AWS supporta le stesse funzionalità di DbGate Team Premium, ma è ottimizzato per AWS

* Supporto per AWS IAM
* Amministrazione di utenti, connessioni e ruoli
* Esplorazione, filtraggio e modifica dei dati
* Importazione ed esportazione dei dati
* Query builder visuale

## Processo di installazione
L'installazione su AWS è molto semplice, è quasi un processo con un solo clic.

Consigliamo il tipo di istanza t2.medium per la migliore esperienza utente, ma t2.micro, disponibile nel piano gratuito, sarà sufficiente per un numero ridotto di utenti.

Dopo l'installazione, devi impostare la password di amministratore, quindi potrai amministrare connessioni, utenti, ruoli e assegnare i permessi.

## Sottoscrizione e licenze
DbGate AWS può essere sottoscritto tramite l'AWS Marketplace, con prezzi basati sulla dimensione dell'istanza scelta. Le istanze più grandi supportano un maggior numero di utenti simultanei.

Una prova gratuita di 30 giorni ti dà accesso a tutte le funzionalità di DbGate. Al termine della prova, la fatturazione segue il piano tariffario di AWS in base alla dimensione dell'istanza selezionata. Non è richiesta alcuna licenza aggiuntiva, poiché tutti i pagamenti vengono gestiti tramite la sottoscrizione su [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy).

## Aggiornamenti di DbGate AWS
DbGate AWS ha una sua build speciale e viene eseguito direttamente su un server virtuale in EC2 (non c'è alcun livello di virtualizzazione aggiuntivo come docker). È disponibile una funzionalità di aggiornamento automatico: dopo l'avvio, il container richiede la build più recente e, se la trova, sostituisce la versione precedente. Non devi eseguire l'aggiornamento manualmente.

Se crei manualmente un nuovo container EC2 con una nuova versione, questo avrà il proprio nuovo database (il database MySQL interno fa parte del container), quindi non esiste un modo semplice per spostare connessioni e utenti nel nuovo container EC2.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate su AWS{{< /button >}}
