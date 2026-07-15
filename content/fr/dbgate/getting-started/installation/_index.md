---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: fr
title: Installation
weight: 10
---

DbGate est disponible pour diverses plateformes, le processus d'installation dépend de la plateforme.

## Windows
Windows prend en charge l'installateur msi et l'installation portable au format ZIP. La mise à jour automatique est prise en charge pour l'installateur MSI.

## Linux
Linux prend en charge les paquets snap et la distribution AppImage. Les deux prennent en charge la mise à jour automatique (SNAP la gère nativement)

## Mac
Pour Mac, un installateur DMG est disponible. Trois paquets sont proposés :
  - Apple (arm64) pour les nouveaux processeurs Apple M1, M2, M3, M4
  - Intel (x86) - pour les anciens processeurs x86
  - Apple+Intel - les deux paquets dans un seul installateur


## Docker 
Pour l'édition Team Premium, veuillez suivre les instructions sur [Team Premium sur Docker ](docker-tp)

Pour l'édition gratuite Community, suivez les instructions sur [docker hub](https://hub.docker.com/r/dbgate/dbgate)


## NPM
Vous pouvez également installer la version web de DbGate depuis NPM, veuillez suivre les instructions sur [npmjs](https://www.npmjs.com/package/dbgate-serve)

## Amazon (AWS)
Ouvrez [DbGate sur la marketplace Amazon](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy). Nous recommandons le type d'instance t2.medium pour une expérience utilisateur optimale, mais l'instance t2.micro disponible dans l'offre gratuite sera suffisante pour un petit nombre d'utilisateurs.

[En savoir plus sur AWS](aws)

## Azure
Ouvrez [DbGate sur la marketplace Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview). Nous recommandons des machines virtuelles avec 2 Go de RAM.

[En savoir plus sur Azure](azure)
