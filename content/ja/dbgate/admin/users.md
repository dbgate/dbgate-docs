---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: ja
title: ユーザー
weight: 30
---

## ユーザータブ
ユーザー、パスワード、ユーザー権限、およびユーザーと接続のマッピングを設定します。
パスワードは「Local」認証方式でのみ使用されます。ただし、外部 ID プロバイダーを使用するすべての方式でもユーザー検索が行われるため、外部認証されたユーザーであっても、そのユーザーの権限や利用可能な接続を設定できます。

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### ユーザー詳細タブ
* Info
  * ユーザー権限を設定します
  * このユーザーに割り当てられたロールを設定します
* Team files - [チームファイル](team-files)へのアクセスを設定します
* Connections - このユーザーに割り当てられた接続を設定します
* Databases - このユーザーの[データベース権限](permissions#database-permissions)を設定します
* Tables/views/objects - このユーザーの[テーブル権限](permissions#table-permissions)を設定します
* Disk files - ディスク／Docker ボリューム上のファイルへのアクセスを設定します
