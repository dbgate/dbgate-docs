---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: ja
title: ロール
weight: 40
---

## ロールタブ
ロール、ロールの権限、およびロールと接続のマッピングを設定します。カスタムロールを作成してユーザーを割り当てることができ、このロールに割り当てられたすべてのユーザー間で権限とリンクされた接続が共有されます。

いくつかの定義済みロールがあります:
- superadmin - 管理ページ https://your_dbgate_instance/admin.html で使用されるロール
- logged-user - ログインしたすべてのユーザーに使用されるロール。特定のユーザーに対して権限を上書きできます
- anonymous-user - 「Anonymous」認証方式でログインしたユーザーに使用されるロール

![Role administration - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### ロール詳細タブ
* Info
  * ロールの権限を設定します
  * このロールに割り当てられたユーザーを設定します
* Team files - [チームファイル](team-files)へのアクセスを設定します
* Connections - このロールに割り当てられた接続を設定します
* Databases - このロールの[データベース権限](permissions#database-permissions)を設定します
* Tables/views/objects - このロールの[テーブル権限](permissions#table-permissions)を設定します
* Disk files - ディスク/docker ボリューム上のファイルへのアクセスを設定します
