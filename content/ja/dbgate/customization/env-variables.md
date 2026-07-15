---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: ja
title: 環境変数
weight: 20
---

環境変数による設定は、docker コンテナで使用できるほか、npm パッケージを使用する場合にも利用できます。NPM パッケージは .env ファイルをサポートしています。
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - Community エディション用の NPM パッケージ
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - Premium エディション用の NPM パッケージ
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - Community エディション用の Docker イメージ
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - Premium エディション用の Docker イメージ

## Premium エディションと Team Community エディションの比較
Community（FOSS）エディションでは、以下に示す環境変数による設定のみを使用します。Team Premium エディションでは設定の保存にデータベースストレージを使用し、[管理 UI](/ja/features/administration) で設定します。環境変数で設定するのは、いくつかの基本的な設定のみです。

## Team Premium エディションの設定
これらの変数は Team Premium エディションでのみ利用できます。
  * STORAGE_SERVER - ストレージデータベース用のデータベースサーバー（ホスト名）
  * STORAGE_USER - データベースユーザー
  * STORAGE_PASSWORD - データベースパスワード
  * STORAGE_PORT - データベースポート（省略可。省略した場合は、選択したデータベースエンジンの既定のポートが使用されます）
  * STORAGE_DATABASE - ストレージデータベース名
  * STORAGE_SCHEMA - ストレージデータベースのスキーマ（省略可。例: PostgreSQL の場合は通常 public、MS SQL の場合は通常 dbo）
  * STORAGE_ENGINE - ストレージデータベースに使用するエンジン。現在は MySQL、PostgreSQL、SQL Server、Oracle に対応しています。次のいずれかの値を使用してください:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - 管理者用パスワード。管理画面は URL https://dbgate_url/admin.html で利用できます。パスワードが定義されておらず、STORAGE_DATABASE が定義されている場合、DbGate は最初に管理者パスワードの入力を求めます。
  * DBGATE_LICENSE - DbGate のライセンスキー。トライアルライセンスについては sales@dbgate.eu までお問い合わせください。定義されていない場合、DbGate Premium は最初にライセンスの入力を求めます。DbGate Community にはライセンスは不要です。
  
### ストレージの追加接続パラメーター
  * STORAGE_SOCKET_PATH - ストレージ接続用のソケットパス
  * STORAGE_DATABASE_URL - ストレージ接続用のデータベース URL
  * STORAGE_AUTH_TYPE - ストレージ接続の認証タイプ。値は AUTH_TYPE_xxx 変数と同じです
  * STORAGE_USE_SSL - SSL を使用する場合は 1 または true を設定します
  * STORAGE_KEY_FILE - キーファイルへのパス
  * STORAGE_KEY_FILE_PASSWORD - キーファイルのパスフレーズ
  * STORAGE_SSL_CA_FILE - CA 証明書ファイルへのパス
  * STORAGE_SSL_CERT_FILE - 証明書ファイルへのパス
  * STORAGE_SSL_CERT_FILE_PASSWORD - 証明書キーファイルのパスワード
  * STORAGE_SSL_KEY_FILE - キーファイルへのパス
  * STORAGE_SSL_KEY_FILE_PASSWORD - キーファイルのパスフレーズ
  * STORAGE_SSL_REJECT_UNAUTHORIZED - 未承認の接続を拒否する場合は 1 または true を設定します
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - MSSQL の trustServerCertificate オプションを設定する場合は 1 または true を設定します

以下の変数は Community エディションと Premium エディションの両方で利用できます。ただし Premium エディションでは、ストレージデータベースを使用し、管理 UI で設定を行う方法が推奨されます。

## Web と権限の設定
* WEB_ROOT - DbGate を仮想サブディレクトリで実行する必要がある場合に使用します（例: 値が /dbadmin の場合、dbgate は localhost:3000/dbadmin でアクセスできます）
* LOGIN , PASSWORD - Web アプリにアクセスするための認証情報
* PERMISSIONS - カンマ区切りの権限のリスト。下記の権限一覧も参照してください
* SHELL_CONNECTION - true または 1 の場合、シェルスクリプト内で接続を定義できます。それ以外の場合は、事前設定された接続のみが許可されます。既定では、セキュリティ上の理由から許可されていません。許可した場合、暗号化されたパスワードがフロントエンドに送信される点にご注意ください。
* SHELL_SCRIPTING - true または 1 の場合、カスタムの JavaScript シェルスクリプトが許可されます。既定では、セキュリティ上の理由から許可されていません。
* LOGIN_PASSWORD_[login] - 指定したログインのパスワード
* LOGIN_PERMISSIONS_[login] - 指定したログインに対するカンマ区切りの権限のリスト。下記の権限一覧も参照してください
* TOKEN_LIFETIME - アクセストークンの有効期間。この時間が経過すると、ログイン済みユーザーはログインページにリダイレクトされます。既定値は 1d（1 日を意味します）です。3h（3 時間）、10m（10 分）、2d（2 日）のような値を指定できます
* SINGLE_CONNECTION - 接続 ID。定義した場合、この接続のみが利用可能になります（SINGLE_DATABASE と一緒に使用する必要があります）
* SINGLE_DATABASE - データベース名。このデータベースのみが利用可能になります（SINGLE_CONNECTION と一緒に使用する必要があります）
* BASIC_AUTH - true または 1 の場合、Web と API の両方でベーシック認証が使用されます。それ以外の場合は、ログインフォームと JWT トークンベースの API 認証が使用されます。ベーシック認証は OAuth 認証には使用できません。
* SKIP_ALL_AUTH - true または 1 の場合、すべての認証がスキップされます
* ALLOW_DBGATE_PRIVATE_CLOUD - 既定では、DbGate Cloud は Web 版では無効になっています。この変数を使用して有効にできます
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - Web 版で、新しいウィンドウを開く代わりに DbGate Cloud のログインへリダイレクトします
* LANGUAGE - UI の言語。例: en、cs、de、fr など。下記の言語設定表を参照してください。ブラウザーの言語を使用するには "auto" を設定します

## 言語設定
| 言語 | 値 |
|----------|-------|
| 英語 | en |
| ドイツ語 | de |
| スペイン語 | es |
| フランス語 | fr |
| イタリア語 | it |
| ポルトガル語（ブラジル） | pt |
| 日本語 | ja |
| 中国語 - 簡体字 | zh |
| チェコ語 | cs |
| スロバキア語 | sk |


## ログの設定
* LOG_LEVEL - このログレベル以上のすべてのメッセージがログに記録されます。trace、debug、info、warn、error、fatal のいずれかの値です。既定値は info です
* FILE_LOG_LEVEL - ログファイルへの記録に使用するログレベル。ファイルへのログ記録では、これが LOG_LEVEL よりも優先されます
* CONSOLE_LOG_LEVEL - ログファイルへの記録に使用するログレベル。コンソールへのログ記録では、これが LOG_LEVEL よりも優先されます

## OAuth の設定（Web 版のみ）
* OAUTH_AUTH - OAuth プロトコルの認証エンドポイント
* OAUTH_TOKEN - OAuth プロトコルのトークンエンドポイント
* OAUTH_LOGOUT - OAuth プロバイダーのログアウト URL。ユーザーがログアウトを要求すると、この URL にリダイレクトされます
* OAUTH_CLIENT_ID - クライアント ID
* OAUTH_CLIENT_SECRET - クライアントシークレット
* OAUTH_LOGIN_FIELD - ログイン名を保持するペイロード内のフィールド名。利用可能なフィールドは dbgate のログで確認できます。OAuth プロバイダーから送信されたペイロードはコンソールに記録されます。このログイン名は、たとえば権限の設定に使用されます。OAuth で入力されたログインである必要はありません。指定しない場合、OAuth プロバイダーのすべてのユーザーが同じログイン名を持つことになります。
* OAUTH_ALLOWED_LOGINS - ログインを許可するログイン名（カンマ区切り）。指定しない場合、すべてのログインが DbGate アプリを使用できます。
* OAUTH_SCOPE - OAuth の authorize エンドポイントおよび token エンドポイントに送信されるスコープ
* OAUTH_GROUP_FIELD - OAuth からのペイロード内でグループを示すフィールド
* OAUTH_ALLOWED_GROUPS - カンマ区切りの許可されたグループ名

## Active Directory/LDAP の設定（Web 版のみ）
* AD_URL - LDAP プロバイダーの URL（例: ldap://domain.com）
* AD_BASEDN - 例: dc=domain,dc=com
* AD_USERNAME - Active Directory のユーザー名
* AD_PASSWORD - Active Directory のパスワード
* AD_ALLOWED_LOGINS - ログインを許可するログイン名（カンマ区切り）。指定しない場合、すべてのログインが DbGate アプリを使用できます。

## Oracle クライアントの設定  
* ORACLE_INSTANT_CLIENT - [Oracle instant client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html) へのパス

## 接続の設定
環境変数で接続リストを設定できます。その場合、「接続の追加」と「接続の編集」コマンドは利用できなくなります。

* CONNECTIONS - 事前設定された接続名のリスト（カンマ区切り）。以降のオプションでは、[connection id] はこのリストの ID を指します
* LABEL_[connection id] - 接続のラベル（表示名）。
* SERVER_[connection id] - 接続のサーバー（ホスト名）。
* USER_[connection id] - DB 接続のユーザー名。
* PASSWORD_[connection id] - DB 接続のパスワード。
* PASSWORD_MODE_[connection id] - パスワードとユーザー名を保存するか、ユーザーが入力する必要があるかを決定します。次のいずれかの値です:
  * askPassword - 接続時に DbGate がパスワードを尋ねます
  * askUser - DbGate がユーザー名とパスワードを尋ねます
* PORT_[connection id] - DB 接続のポート。
* FILE_[connection id] - データベースファイルのパス（SQLite 用）。
* URL_[connection id] - データベース URL（MongoDB、PostgreSQL、CockroachDb、Redshift、Oracle で機能します）。
* SERVICE_NAME_[connection id] - Oracle のサービス名。
* DATABASE_[connection id] - 既定のデータベース名。
* READONLY_[connection id] - 読み取り専用モードで接続します
* ENGINE_[connection id] - 接続のエンジン（**必須**、プラグイン付きのエンジン名）。次のいずれかです:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - SSH トンネルを使用する場合は 1 または true を設定します
* SSH_HOST_[connection id] - SSH のホスト名
* SSH_PORT_[connection id] - SSH のポート番号
* SSH_MODE_[connection id] - 次のいずれかの値です
  * userPassword - ユーザーとパスワードで認証します
  * agent - SSH エージェントで認証します
  * keyFile - キーファイルで認証します
* SSH_LOGIN_[connection id] - SSH のログイン
* SSH_PASSWORD_[connection id] - SSH のパスワード
* SSH_KEY_FILE_[connection id] - キーファイルへのフルパス
* SSH_KEY_FILE_PASSWORD_[connection id] - キーファイルのパスフレーズ
* USE_SSL_[connection id] - SSL を使用する場合は 1 または true を設定します
* SSL_CA_FILE_[connection id] - CA 証明書ファイルへのパス
* SSL_CERT_FILE_[connection id] - 証明書ファイルへのパス
* SSL_CERT_FILE_PASSWORD_[connection id] - 証明書キーファイルのパスワード
* SSL_KEY_FILE_[connection id] - キーファイルへのパス
* SSL_REJECT_UNAUTHORIZED_[connection id] - 未承認の接続を拒否する場合は 1 または true を設定します
* SSL_TRUST_CERTIFICATE_[connection id] - MSSQL の trustServerCertificate オプションを設定する場合は 1 または true を設定します
* SETTINGS_[settings key] - 設定値を事前構成します。設定キーはソースコード https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/ から確認できます
* SOCKET_PATH_[connection id] - ソケット経由で接続する場合の、ソケットファイルへのパス
* AUTH_TYPE_[connection id] - 認証タイプ
  * hostPort（既定）
  * socket - SOCKET_PATH を設定すると暗黙的に設定される値です
  * tedious - tedious ドライバーを使用する、MS SQL 用の既定のポータブル認証
  * sspi - ネイティブ MSSQL ドライバーを使用する Windows 統合認証（Windows のみ、MS SQL）
  * sql - ネイティブ MSSQL ドライバーを使用する SQL 認証（Windows のみ、MS SQL）
* ALLOWED_DATABASES_[connection id] - 指定した接続で許可するデータベース名（パイプ（"|"）区切り）
* ALLOWED_DATABASES_REGEX_[connection id] - 指定した接続で許可するデータベース名の正規表現
* USE_SEPARATE_SCHEMAS_[connection id] - スキーマを個別に読み込む場合は 1 または true を設定します。大きなスキーマがある場合に使用してください。
* LOCAL_DATA_CENTER_[connection id] - ローカルデータセンター（Apache Cassandra 用）
* CONNECTION_[connection id]_parameterName - エンジン固有のパラメーター名を設定します

SettingsModal.svelte で、文字列 "name=" を検索してください。"true" を定義する必要がある場合は、値 "1" を使用してください。"false" が必要な場合は、空の文字列を使用してください（"0" は機能しません）

## ロールの設定
この設定は、設定にストレージデータベースを使用する Team Premium エディションでのみ使用できます。環境変数からのロールは、docker コンテナの起動時にストレージデータベースにインポートされます。
特定の権限を持つロールを定義し、そのロールに接続を割り当てることができます。ユーザーへのロールの割り当ては管理 UI で行います。
* `ROLE_[role_name]_PERMISSIONS` - 指定したロールの権限のカンマ区切りリスト。下記の権限一覧を参照してください
* `ROLE_[role_name]_CONNECTIONS` - 指定したロールに割り当てる接続 ID のカンマ区切りリスト
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - 指定した ID のデータベース権限に対する接続 ID
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - 指定した ID のデータベース権限に対するデータベース名のパイプ（"|"）区切りリスト
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - 指定した ID のデータベース権限に対するデータベース名の正規表現
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - 次のいずれか: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - 指定した ID のテーブル権限に対する接続 ID
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - 指定した ID のデータベース権限に対するデータベース名のパイプ（"|"）区切りリスト
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - 指定した ID のデータベース権限に対するデータベース名の正規表現
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - 指定した ID のテーブル権限に対するスキーマ名のパイプ（"|"）区切りリスト
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - 指定した ID のテーブル権限に対するスキーマ名の正規表現
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - 指定した ID のデータベース権限に対するテーブル名のパイプ（"|"）区切りリスト
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - 指定した ID のデータベース権限に対するテーブル名の正規表現
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - 次のいずれか: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - 次のいずれか: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## 権限
既定では、すべての権限が利用可能です。\~ プレフィックスを使用すると、権限が取り消されます。

### 例
* ~*, widgets/database - すべての権限が取り消され、データベースウィジェットのみが表示されます
* ~widgets/*, widgets/database - すべてのウィジェット権限が取り消され、データベースウィジェットのみが表示されます
* ~connections/*, connections/con1 - con1 以外のすべての接続が非表示かつ無効になります

### 権限の一覧
* settings/change - 設定の変更を許可します
* plugins/install - プラグインのインストールを許可します
* widgets/[widget_name] - 付与されていない場合、ウィジェットは非表示になります。ウィジェットは左側のストリップです。利用可能なウィジェット:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - 指定したフォルダーからファイルを読み取ります
* files/[folder]/write - 指定したフォルダーにファイルを書き込みます
* apps/write - アプリのコンテンツへの保存
* archive/write - アーカイブのコンテンツへの保存
* connections/[connection_id] - 定義された接続の表示と使用を許可します
* internal-storage = 内部ストレージへのアクセス（Premium）
* admin/auth - 管理 - 認証タブ（Premium）
* admin/connections - 管理 - 接続タブ（Premium）
* admin/users - 管理 - ユーザータブ（Premium）
* admin/roles - 管理 - ロールタブ（Premium）
* dbops/sql-template/* - SQL テンプレート（例: SQL: CREATE TABLE、SQL: SELECT）
* dbops/sql-generator - SQL ジェネレーター
* dbops/sql-dump/import - SQL ダンプのインポート
* dbops/sql-dump/export - SQL ダンプのエクスポート
* dbops/query - SQL クエリの実行
* dbops/import - データのインポート
* dbops/export - データのエクスポート
* dbops/charts - チャートの表示
* dbops/profiler - データベースプロファイラー
* dbops/createdb - データベースの作成
* dbops/dropdb - データベースの削除
* dbops/model/view - データベースモデルの表示（ダイアグラム、JSON）
* dbops/model/edit - データベースモデルの編集（テーブル、ビューなどの作成/変更）
* dbops/model/compare - データベースモデルの比較
* dbops/table/rename - テーブル名の変更
* dbops/table/truncate - テーブルの切り詰め
* dbops/table/backup - テーブルバックアップの作成

