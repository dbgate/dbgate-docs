---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: ja
title: 接続
weight: 20
---

DbGate からデータベースに接続するのは簡単です。データベースへの接続方法はいくつかあります:

* メニューの File/Add Connection、または CONNECTIONS ウィジェットの {{< mdi "plus-thick" >}} アイコン
* メニューの File/New SQLite database - 新しい SQLite データベースを作成します
* メニューの File/Open - 既存の SQLite データベースを開くことができます

## 接続画面
![Connection screen](https://media.dbgate.io/img/new-connection-light.png)

接続画面のフィールドは、接続の種類によって大きく異なります。

共通のフィールドをいくつか紹介します:

* Server - データベースサーバーのホスト名
* Port - ポート。データベースの既定のポートを使用する場合は、空のままにできます
* User、Password - 認証情報
* Password mode
    * Save and encrypt - パスワードは暗号化して保存されます。次回以降、パスワードを確認することはできません
    * Save RAW - パスワードはそのまま（暗号化されずに）保存されます。後から確認できます
    * Don't save, ask for password - パスワードは保存されず、接続時に入力する必要があります
    * Don't save, ask for login and password - パスワードもログインも保存されず、接続時に両方を入力する必要があります
* Is read only - 接続が読み取り専用になります（読み取り専用セッションをサポートしないエンジンでは、この場合 SQL クエリを実行できません）
* Default database - 接続後にアクティブになるデータベース
* Use only database *&lt;既定のデータベース&gt;* - チェックすると、接続ツリーには既定のデータベースのみが表示されます（サーバー上の他のデータベースは非表示になります）
* Display name - アプリケーション上で接続が表示される際の名前

## SSH トンネル
ここでは、SSH トンネル経由の接続を設定できます。

共通のフィールド:
* Use SSH tunnel - SSH トンネルを使用する場合にチェックします
* Host - SSH サーバーのホスト名

![DbGate - SSH tunnel configuration](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
SSL 接続を設定します。

共通のフィールド:
* Use SSL - SSL を使用する場合にチェックします。ほとんどの場合、SSL を使用するために設定が必要なのはこれだけです

![DbGate - SSL connection configuration](https://media.dbgate.io/img/connection-ssl-window-light.png)
