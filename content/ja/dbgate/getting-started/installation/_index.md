---
sourceHash: 0cb335ca40af87498f8b4953eddcbb27c0ed2f4ba8c5cacbd108504ae8cd9cc4
language: ja
title: インストール
weight: 10
---

DbGate はさまざまなプラットフォームで利用でき、インストール手順はプラットフォームによって異なります。

## Windows
Windows では msi インストーラーとポータブル ZIP でのインストールがサポートされています。自動アップデーターは MSI インストーラーでサポートされています。

## Linux
Linux では snap パッケージと AppImage 形式での配布がサポートされています。どちらも自動アップデートに対応しています（SNAP はネイティブに対応しています）。

## Mac
Mac 向けには DMG インストーラーが利用できます。3 種類のパッケージが用意されています。
  - Apple (arm64) - 新しい Apple M1、M2、M3、M4 プロセッサー向け
  - Intel (x86) - 旧来の x86 プロセッサー向け
  - Apple+Intel - 両方のパッケージを 1 つにまとめたインストーラー


## Docker 
Team Premium エディションについては、[Docker 上の Team Premium](docker-tp) の手順に従ってください。

無料の Community エディションについては、[docker hub](https://hub.docker.com/r/dbgate/dbgate) の手順に従ってください。


## NPM
DbGate の Web 版を NPM からインストールすることもできます。[npmjs](https://www.npmjs.com/package/dbgate-serve) の手順に従ってください。

## Amazon (AWS)
[Amazon マーケットプレイスの DbGate](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy) を開いてください。最適な使用感を得るには t2.medium インスタンスタイプを推奨しますが、無料利用枠で使える t2.micro でも少人数のユーザーであれば十分です。

[AWS の詳細](aws)

## Azure
[Azure マーケットプレイスの DbGate](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview) を開いてください。2 GB RAM の仮想マシンを推奨します。

[Azure の詳細](azure)
