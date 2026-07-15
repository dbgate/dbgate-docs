---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: ja
title: 管理
weight: 60
---

管理インターフェースを使用すると、チームは DbGate を共有のマルチユーザー Web アプリケーションとして運用できます。接続を一元管理し、誰がどのようにサインインできるかを定義し、ユーザー、ロール、権限を通じてデータベースやオブジェクトへのきめ細かなアクセスを付与できます。また、チームの共有ファイルもホストします。ここで設定されたすべての内容は、ローカルファイルではなくストレージデータベースに保存されます。

管理ツールは Team Premium エディションでのみ利用できます。Community エディションでは、代わりに[環境変数](/ja/dbgate/customization/env-variables)を使用して DbGate を設定してください。

管理画面のすべての設定はストレージデータベースに保存されます。設定するには [STORAGE_xxx 環境変数](/ja/dbgate/customization/env-variables/#team-premium-edition-configuration)を使用してください。

このセクションの内容:

* [認証](auth) - サインイン方法と ID プロバイダーを設定する
* [接続](connection) - チームで利用できる接続を管理する
* [チームファイル](team-files) - SQL スクリプト、ER 図、チャートを共有する
* [ユーザー](users) - ユーザーアカウントを管理する
* [ロール](roles) - 権限をロールにまとめる
* [権限](permissions) - 接続、データベース、テーブルへのアクセスを付与する

## 管理者アクセス

管理ページは URL https://your_dbgate_instance/admin.html で利用できます。 

ルート管理者にはパスワードを定義する必要があります。環境変数 ADMIN_PASSWORD を設定できます。この変数が定義されていない場合、DbGate は最初に管理者パスワードの入力を求めます。

その後、別の認証方法を使用する別のユーザーに管理権限を追加できますが、まずはこの管理ページを開く必要があります。

