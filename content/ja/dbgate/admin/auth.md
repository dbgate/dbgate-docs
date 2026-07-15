---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: ja
title: 認証
weight: 10
---

## 「Authentication」タブ
認証方法にはいくつかの種類があります。ユーザーはログインページで認証方法を選択します。有効な認証方法が 1 つだけで、その認証方法がログインページを必要としない場合、ログインページはスキップされます。

![Authentication administration - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Local 認証方法 - ストレージデータベース内のユーザー一覧（「Users」タブで設定）からユーザーを選択します
- Anonymous - 資格情報は不要で、ユーザーは「anonymous-user」ロールの権限を持ちます
- Use database login - 資格情報はデータベースサーバーにリダイレクトされます。ユーザーは「Connections」タブから接続を選択します
- OAuth 2.0 - 汎用の OAuth プロバイダーです。少しの手間と適切な知識があれば、Google、Facebook、Keycloak など最近のほとんどの ID プロバイダーで設定できます
- Active Directory - LDAP プロトコル経由の AD アクセス
- Microsoft Entra - 旧 Azure Active Directory - Azure データベースへのシングルサインオンアクセス

### オプション「Allow only defined logins」
外部 ID プロバイダーの場合、ユーザーが DbGate のストレージデータベースに存在する必要はありません。このチェックボックスをオンにすると、ストレージデータベースに見つからないユーザーはログインできなくなります。

### Keycloak

Keycloak は、汎用の OAuth 2.0 プロバイダーを使用して DbGate と統合できます。Keycloak 認証を設定するには、次の作業が必要です:

1. Keycloak レルムに新しいクライアントを作成する
2. クライアント設定を構成する
3. DbGate で OAuth 2.0 プロバイダーを次のパラメーターで設定する

**必要な設定:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: Keycloak のクライアント ID
- **OAuth login field**: ユーザーのログイン識別子を含む Keycloak のクレーム（通常は `preferred_username`。Keycloak の構成によっては `given_name`、`email`、その他の適切なクレームを使用することもできます）

**Keycloak クライアントの設定:**
- Valid Redirect URIs: `https://dbgate.company.com/`

DbGate が OAuth プロバイダーに期待する必要なクレーム（email、name、username）が提供されるよう、Keycloak のユーザー属性が正しくマッピングされていることを確認してください。


