---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: sk
title: Inštalácia
weight: 10
---

DbGate je dostupný pre rôzne platformy, proces inštalácie závisí od platformy.

## Windows
Windows podporuje inštalátor msi a prenosnú (portable) ZIP inštaláciu. Automatická aktualizácia je podporovaná pre inštalátor MSI.

## Linux
Linux podporuje balíčky snap a distribúciu AppImage. Obe podporujú automatickú aktualizáciu (SNAP ju podporuje natívne)

## Mac
Pre Mac je dostupný inštalátor DMG. K dispozícii sú 3 balíčky:
  - Apple (arm64) pre nové procesory Apple M1, M2, M3, M4
  - Intel (x86) - pre staré procesory x86
  - Apple+Intel - oba balíčky v jednom inštalátore


## Docker 
Pre edíciu Team Premium postupujte podľa pokynov na stránke [Team Premium na Dockeri ](docker-tp)

Pre bezplatnú edíciu Community postupujte podľa pokynov na [docker hub](https://hub.docker.com/r/dbgate/dbgate)


## NPM
Webovú verziu DbGate môžete nainštalovať aj z NPM, postupujte podľa pokynov na [npmjs](https://www.npmjs.com/package/dbgate-serve)

## Amazon (AWS)
Otvorte [DbGate na Amazon marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy). Pre najlepší používateľský zážitok odporúčame typ inštancie t2.medium, ale t2.micro dostupná v rámci free tier bude postačovať pre malý počet používateľov.

[Viac o AWS](aws)

## Azure
Otvorte [DbGate na Azure marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview). Odporúčame virtuálne stroje s 2 GB RAM.

[Viac o Azure](azure)
