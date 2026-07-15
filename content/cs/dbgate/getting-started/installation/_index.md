---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: cs
title: Instalace
weight: 10
---

DbGate je dostupný pro různé platformy, proces instalace závisí na platformě.

## Windows
Windows podporuje instalátor msi a přenosnou instalaci ze ZIP archivu. Automatická aktualizace je podporována u MSI instalátoru.

## Linux
Linux podporuje snap balíčky a distribuci AppImage. Obojí podporuje automatickou aktualizaci (SNAP ji podporuje nativně)

## Mac
Pro Mac je k dispozici DMG instalátor. K dispozici jsou 3 balíčky:
  - Apple (arm64) pro nové procesory Apple M1, M2, M3, M4
  - Intel (x86) - pro staré procesory x86
  - Apple+Intel - oba balíčky v jednom instalátoru


## Docker 
Pro edici Team Premium postupujte podle instrukcí na stránce [Team Premium na Dockeru ](docker-tp)

Pro bezplatnou edici Community postupujte podle instrukcí na [docker hub](https://hub.docker.com/r/dbgate/dbgate)


## NPM
Webovou verzi DbGate můžete také nainstalovat z NPM, postupujte podle instrukcí na [npmjs](https://www.npmjs.com/package/dbgate-serve)

## Amazon (AWS)
Otevřete [DbGate na Amazon marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy). Pro nejlepší uživatelský zážitek doporučujeme typ instance t2.medium, ale t2.micro dostupná ve free tier bude pro malý počet uživatelů dostačující.

[Více o AWS](aws)

## Azure
Otevřete [DbGate na Azure marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview). Doporučujeme virtuální stroje s 2 GB RAM.

[Více o Azure](azure)
