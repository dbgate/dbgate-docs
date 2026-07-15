---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: de
title: Installation
weight: 10
---

DbGate ist für verschiedene Plattformen verfügbar, der Installationsvorgang hängt von der Plattform ab.

## Windows
Windows unterstützt den MSI-Installer und die portable ZIP-Installation. Der Autoupdater wird für den MSI-Installer unterstützt.

## Linux
Linux unterstützt Snap-Pakete und die AppImage-Distribution. Beide unterstützen Autoupdate (SNAP unterstützt es nativ)

## Mac
Für Mac ist ein DMG-Installer verfügbar. Es sind 3 Pakete verfügbar:
  - Apple (arm64) für neue Apple M1-, M2-, M3-, M4-Prozessoren
  - Intel (x86) - für alte x86-Prozessoren
  - Apple+Intel - beide Pakete in einem Installer


## Docker 
Für die Team Premium Edition folgen Sie bitte den Anweisungen unter [Team Premium auf Docker ](docker-tp)

Für die kostenlose Community Edition folgen Sie den Anweisungen auf [Docker Hub](https://hub.docker.com/r/dbgate/dbgate)


## NPM
Sie können die Web-Version von DbGate auch über NPM installieren, folgen Sie bitte den Anweisungen auf [npmjs](https://www.npmjs.com/package/dbgate-serve)

## Amazon (AWS)
Öffnen Sie [DbGate auf dem Amazon Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy). Wir empfehlen den Instanztyp t2.medium für das beste Benutzererlebnis, aber t2.micro, das im kostenlosen Kontingent verfügbar ist, reicht für eine kleine Anzahl von Benutzern aus.

[Mehr über AWS](aws)

## Azure
Öffnen Sie [DbGate auf dem Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview). Wir empfehlen virtuelle Maschinen mit 2 GB RAM.

[Mehr über Azure](azure)
