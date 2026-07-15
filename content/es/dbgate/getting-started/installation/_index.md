---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: es
title: Instalación
weight: 10
---

DbGate está disponible para varias plataformas, el proceso de instalación depende de la plataforma.

## Windows
Windows admite el instalador msi y la instalación portable en ZIP. El autoactualizador es compatible con el instalador MSI.

## Linux
Linux admite paquetes snap y la distribución AppImage. Ambos admiten la actualización automática (SNAP la admite de forma nativa)

## Mac
Para Mac está disponible el instalador DMG. Hay 3 paquetes disponibles:
  - Apple (arm64) para los nuevos procesadores Apple M1, M2, M3, M4
  - Intel (x86) - para procesadores x86 antiguos
  - Apple+Intel - ambos paquetes en un solo instalador


## Docker 
Para la edición Team Premium, siga las instrucciones en [Team Premium en Docker ](docker-tp)

Para la edición gratuita Community, siga las instrucciones en [docker hub](https://hub.docker.com/r/dbgate/dbgate)


## NPM
También puede instalar la versión web de DbGate desde NPM, siga las instrucciones en [npmjs](https://www.npmjs.com/package/dbgate-serve)

## Amazon (AWS)
Abra [DbGate en Amazon marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy). Recomendamos el tipo de instancia t2.medium para obtener la mejor experiencia de usuario, pero t2.micro, disponible en la capa gratuita, será suficiente para un número reducido de usuarios.

[Más sobre AWS](aws)

## Azure
Abra [DbGate en Azure marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview). Recomendamos máquinas virtuales con 2 GB de RAM.

[Más sobre Azure](azure)
