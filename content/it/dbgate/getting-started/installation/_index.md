---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: it
title: Installazione
weight: 10
---

DbGate è disponibile per diverse piattaforme, il processo di installazione dipende dalla piattaforma.

## Windows
Windows supporta l'installer msi e l'installazione portable tramite ZIP. L'aggiornamento automatico è supportato per l'installer MSI.

## Linux
Linux supporta i pacchetti snap e la distribuzione AppImage. Entrambi supportano l'aggiornamento automatico (SNAP lo supporta nativamente)

## Mac
Per Mac è disponibile l'installer DMG. Sono disponibili 3 pacchetti:
  - Apple (arm64) per i nuovi processori Apple M1, M2, M3, M4
  - Intel (x86) - per i vecchi processori x86
  - Apple+Intel - entrambi i pacchetti in un unico installer


## Docker 
Per l'edizione Team Premium, segui le istruzioni su [Team Premium su Docker ](docker-tp)

Per l'edizione gratuita Community, segui le istruzioni su [docker hub](https://hub.docker.com/r/dbgate/dbgate)


## NPM
Puoi anche installare la versione web di DbGate da NPM, segui le istruzioni su [npmjs](https://www.npmjs.com/package/dbgate-serve)

## Amazon (AWS)
Apri [DbGate sull'Amazon marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy). Consigliamo il tipo di istanza t2.medium per la migliore esperienza utente, ma t2.micro disponibile nel piano gratuito sarà sufficiente per un numero ridotto di utenti.

[Maggiori informazioni su AWS](aws)

## Azure
Apri [DbGate sull'Azure marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview). Consigliamo macchine virtuali con 2 GB di RAM.

[Maggiori informazioni su Azure](azure)
