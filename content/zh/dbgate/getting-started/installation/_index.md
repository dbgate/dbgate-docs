---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: zh
title: 安装
weight: 10
---

DbGate 支持多种平台，安装过程取决于具体平台。

## Windows
Windows 支持 msi 安装程序和便携版 ZIP 安装。MSI 安装程序支持自动更新。

## Linux
Linux 支持 snap 软件包和 AppImage 分发方式。两者都支持自动更新（SNAP 原生支持）。

## Mac
对于 Mac，提供 DMG 安装程序。共有 3 个可用的安装包：
  - Apple (arm64) — 适用于新款 Apple M1、M2、M3、M4 处理器
  - Intel (x86) — 适用于旧款 x86 处理器
  - Apple+Intel — 将两个包合并在一个安装程序中


## Docker 
对于 Team Premium 版本，请按照 [Docker 上的 Team Premium](docker-tp) 中的说明操作

对于免费的 Community 版本，请按照 [docker hub](https://hub.docker.com/r/dbgate/dbgate) 上的说明操作


## NPM
你也可以从 NPM 安装 DbGate 的 Web 版本，请按照 [npmjs](https://www.npmjs.com/package/dbgate-serve) 上的说明操作

## Amazon (AWS)
打开 [Amazon marketplace 上的 DbGate](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy)。为获得最佳使用体验，我们推荐 t2.medium 实例类型，但免费套餐中提供的 t2.micro 对于少量用户来说已经足够。

[关于 AWS 的更多信息](aws)

## Azure
打开 [Azure marketplace 上的 DbGate](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview)。我们推荐使用具有 2 GB 内存的虚拟机。

[关于 Azure 的更多信息](azure)
