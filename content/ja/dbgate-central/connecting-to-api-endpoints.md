---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: ja
title: API エンドポイントへの接続
weight: 10
---

DbGate Central は 3 種類の API エンドポイントに接続でき、いずれの場合も同じ新規接続ダイアログを使用します。

## サポートされているエンドポイントの種類

* **GraphQL** - スキーマをイントロスペクションし、型を参照して、任意の GraphQL API に対してクエリを実行します。
* **oData** - oData V4 サービスを通常のテーブルのように扱えます。
* **Shopify** - Shopify Admin API を通じてストアに接続し、商品、注文、顧客、メタフィールドなどを探索できます。

## 接続の作成

**New Connection** ダイアログを開き、接続の種類を選択し、サービスの URL を入力して、認証方法を選びます。

* **None** - 公開されているオープンなエンドポイント向け。
* **Basic** - ユーザー名とパスワード。
* **Bearer token** - アクセストークンを貼り付けます。
* **API key** - ヘッダーまたはクエリパラメーターでキーを送信します。

接続はワークスペースに保存されるため、次回サインインしたときにも、どのデバイスからでも、ローカルでの設定なしにそのまま利用できます。

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
