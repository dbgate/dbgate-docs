---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: ja
title: Azure へのデプロイ
weight: 20
---

DbGate Azure エディションは、Azure 内でのデータベース管理向けに特別に設計された、共同作業が可能なマルチユーザー Web プラットフォームです。Azure インフラストラクチャを活用することで、クラウド環境で運用する組織のチームワークを効率化します。ブラウザベースの共有インターフェイスにより、Azure とシームレスに統合しながら、コラボレーション、データアクセス、データベース監視をシンプルにします。

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate on Azure{{< /button >}}


## DbGate Azure の主な機能
DbGate Azure は DbGate Team Premium と同じ機能をサポートしていますが、Azure 向けに最適化されています。

* Azure マネージド ID のサポート
* ユーザー、接続、ロールの管理
* データの参照、フィルタリング、編集
* データのインポートとエクスポート
* ビジュアルクエリビルダー

## インストールの手順
Azure へのインストールは非常に簡単で、ほぼワンクリックで完了します。

2 GB RAM の仮想マシンを推奨します。

インストール後、管理者パスワードを設定する必要があります。その後、接続、ユーザー、ロールを管理し、権限を付与できます。

## サブスクリプションとライセンス
DbGate Azure は Azure Marketplace からサブスクライブでき、料金は選択した仮想マシンのプロセッサ数に基づきます。

30 日間の無料トライアルにより、DbGate のすべての機能をご利用いただけます。トライアル終了後は、選択したインスタンスサイズに応じた Azure の料金プランに従って課金されます。支払いはすべて [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview) のサブスクリプションを通じて処理されるため、追加のライセンスは必要ありません。

## DbGate Azure のアップデート
DbGate Azure は専用のビルドを持ち、仮想サーバー上で直接実行されます（Docker のような追加の仮想化レイヤーはありません）。自動アップグレード機能があり、起動後にコンテナが最新ビルドを要求し、見つかった場合は古いバージョンを置き換えます。手動でアップグレードする必要はありません。

新しいバージョンの仮想マシンを手動で作成した場合、その仮想マシンには新しいデータベースが作成されるため（内部の MySQL データベースは仮想マシンの一部です）、接続やユーザーを新しい仮想マシンへ移行する簡単な方法はありません。

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate on Azure{{< /button >}}
