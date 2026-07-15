---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: pt
title: Instalação
weight: 10
---

O DbGate está disponível para várias plataformas, o processo de instalação depende da plataforma.

## Windows
O Windows oferece suporte ao instalador msi e à instalação portátil em ZIP. O autoatualizador é suportado no instalador MSI.

## Linux
O Linux oferece suporte a pacotes snap e à distribuição AppImage. Ambos suportam autoatualização (o SNAP oferece suporte nativo).

## Mac
Para Mac, está disponível o instalador DMG. Há 3 pacotes disponíveis:
  - Apple (arm64) para os novos processadores Apple M1, M2, M3, M4
  - Intel (x86) - para processadores x86 antigos
  - Apple+Intel - ambos os pacotes em um único instalador


## Docker 
Para a edição Team Premium, siga as instruções em [Team Premium no Docker ](docker-tp)

Para a edição gratuita Community, siga as instruções no [docker hub](https://hub.docker.com/r/dbgate/dbgate)


## NPM
Você também pode instalar a versão web do DbGate a partir do NPM, siga as instruções no [npmjs](https://www.npmjs.com/package/dbgate-serve)

## Amazon (AWS)
Abra o [DbGate no Amazon marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy). Recomendamos o tipo de instância t2.medium para a melhor experiência do usuário, mas a t2.micro, disponível no nível gratuito, será suficiente para um pequeno número de usuários.

[Mais sobre AWS](aws)

## Azure
Abra o [DbGate no Azure marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview). Recomendamos máquinas virtuais com 2 GB de RAM.

[Mais sobre Azure](azure)
