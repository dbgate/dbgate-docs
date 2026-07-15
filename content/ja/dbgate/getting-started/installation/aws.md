---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: ja
title: AWS へのデプロイ
subtitle: Amazon EC2 クラスターへのシングルクリックデプロイ
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

DbGate AWS エディションは、Amazon Web Services (AWS) 内でのデータベース管理に特化して設計された、共同作業向けのマルチユーザー Web プラットフォームです。AWS インフラストラクチャを活用することで、クラウド環境で運用する組織のチームワークを効率化します。ブラウザベースの共有インターフェースにより、AWS とシームレスに統合しながら、コラボレーション、データアクセス、データベース監視をシンプルにします。

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate on AWS{{< /button >}}

## DbGate AWS の主な機能
DbGate AWS は DbGate Team Premium と同じ機能をサポートしていますが、AWS 向けに最適化されています

* AWS IAM のサポート
* ユーザー、接続、ロールの管理
* データの参照、フィルタリング、編集
* データのインポートとエクスポート
* ビジュアルクエリビルダー

## インストール手順
AWS へのインストールは非常に簡単で、ほぼシングルクリックで完了します。

最適なユーザー体験のためには t2.medium インスタンスタイプを推奨しますが、無料利用枠で利用できる t2.micro でも少人数のユーザーであれば十分です。

インストール後、管理者パスワードを設定する必要があります。その後、接続、ユーザー、ロールを管理し、権限を付与できます。

## サブスクリプションとライセンス
DbGate AWS は AWS Marketplace を通じてサブスクリプションでき、料金は選択したインスタンスのサイズに基づきます。大きなインスタンスほど、より多くの同時ユーザーをサポートします。

30 日間の無料トライアルで、DbGate のすべての機能を利用できます。トライアル終了後は、選択したインスタンスサイズに応じた AWS の料金プランに従って課金されます。すべての支払いは [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy) のサブスクリプションを通じて処理されるため、追加のライセンスは必要ありません。

## DbGate AWS のアップデート
DbGate AWS は専用のビルドを持ち、EC2 の仮想サーバー上で直接実行されます (Docker のような追加の仮想化レイヤーはありません)。自動アップグレード機能があり、起動後にコンテナが最新ビルドをリクエストし、見つかった場合は古いバージョンを置き換えます。手動でアップグレードする必要はありません。

新しいバージョンの EC2 コンテナを手動で作成した場合、そのコンテナは新しいデータベースを持つことになるため (内部の MySQL データベースはコンテナの一部です)、接続やユーザーを新しい EC2 コンテナに移行する簡単な方法はありません。

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate on AWS{{< /button >}}
