---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: ja
title: AI エージェント向け MCP サーバー
weight: 50
---

DbGate Central は、[Claude](https://claude.ai) などの AI アシスタントに対して、ワークスペースをリモートの **MCP (Model Context Protocol)** コネクタとして公開できます。これにより、エージェントはあなたと同じ方法で API を探索してクエリでき、そのアクセス範囲は常にあなたの管理下に置かれます。

## セットアップ

1. **Settings** タブを開き、**MCP プロファイル**を作成します。その **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`)、**Client ID**、**Client Secret** をコピーします。
2. claude.ai (または他の MCP 対応クライアント) で、その URL と OAuth 認証情報を使ってカスタムコネクタを追加します。
3. 各接続のエディタで、**MCP access** レベルを **No access**、**Read-only**、**Writable** のいずれかに設定します。デフォルトはアクセスなしなので、許可するまで何も共有されません。
4. アシスタントが OAuth ハンドシェイクを実行し、あなたが同意すると、コネクタがそのプロファイルとワークスペースに紐付けられます。

各ワークスペースは複数の MCP プロファイルを持つことができ、それぞれが独自の URL、認証情報、接続ごとの権限を持ちます。認証には PKCE 必須の OAuth 2.1 を使用し、クライアントシークレットは保存時に暗号化されます。

## エージェントができること

**oData**、**GraphQL**、**Shopify** の接続で利用できます (SQLite/DuckDB はブラウザ専用のため MCP の対象外です)。

* プロファイルが使用を許可されている**接続の一覧表示**。
* **エンティティの一覧表示** - テーブル、ビュー、カタログエンティティ。
* **スキーマの調査** - 列名と型。
* **行のクエリ** - データのフィルタリング、ページング、選択。
* **行の更新** - Shopify のみ、かつ Writable アクセスを許可した場合のみ。

読み取りと書き込みはグリッドやスケジューラと同じエンジンを再利用しているため、エージェントが見るデータと機能はあなたが見るものとまったく同じであり、許可したアクセス範囲を超えることはありません。

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
