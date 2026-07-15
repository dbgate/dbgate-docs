---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: it
title: Distribuzione su Azure
weight: 20
---

DbGate Azure edition è una piattaforma web collaborativa e multiutente progettata specificamente per la gestione dei database all'interno di Azure. Sfruttando l'infrastruttura di Azure, semplifica il lavoro di squadra per le organizzazioni che operano in ambienti cloud. La sua interfaccia condivisa basata su browser semplifica la collaborazione, l'accesso ai dati e la supervisione dei database, integrandosi perfettamente con Azure.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate su Azure{{< /button >}}


## Funzionalità principali di DbGate Azure
DbGate Azure supporta le stesse funzionalità di DbGate Team Premium, ma è ottimizzato per Azure

* Supporta l'identità gestita di Azure
* Amministrazione di utenti, connessioni e ruoli
* Esplorazione, filtraggio e modifica dei dati
* Importazione ed esportazione dei dati
* Generatore visuale di query

## Processo di installazione
L'installazione su Azure è molto semplice, è quasi un processo con un solo clic.

Consigliamo macchine virtuali con 2 GB di RAM.

Dopo l'installazione, è necessario impostare la password dell'amministratore, dopodiché sarà possibile amministrare connessioni, utenti, ruoli e concedere autorizzazioni.

## Sottoscrizione e licenze
DbGate Azure può essere sottoscritto tramite l'Azure Marketplace, con prezzi basati sul numero di processori della macchina virtuale scelta.

Una prova gratuita di 30 giorni consente di accedere a tutte le funzionalità di DbGate. Al termine del periodo di prova, la fatturazione segue il piano tariffario di Azure in base alla dimensione dell'istanza selezionata. Non è richiesta alcuna licenza aggiuntiva, poiché tutti i pagamenti vengono gestiti tramite la sottoscrizione dell'[Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview).

## Aggiornamenti di DbGate Azure
DbGate Azure ha una build speciale e viene eseguito direttamente sul server virtuale (non è presente alcun livello di virtualizzazione aggiuntivo come docker). È disponibile una funzionalità di aggiornamento automatico: dopo l'avvio, il container richiede la build più recente e, se la trova, sostituisce la versione precedente. Non è necessario eseguire l'aggiornamento manualmente.

Se create manualmente una nuova macchina virtuale con una nuova versione, questa avrà il proprio database (il database MySQL interno fa parte della macchina virtuale), quindi non esiste un modo semplice per spostare connessioni e utenti sulla nuova macchina virtuale.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate su Azure{{< /button >}}
</content>
</invoke>
