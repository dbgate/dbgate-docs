---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: ja
title: GraphQL API のクエリ
weight: 20
---

DbGate Central を任意の GraphQL API に向けるだけで、利用可能な内容が自動的に検出されます。個別のドキュメントを調べる必要はありません。

## スキーマを探索する

DbGate Central は接続すると同時に GraphQL スキーマをイントロスペクションします。利用可能な型とフィールドをツリーで参照し、クエリタブを開いて作業を始められます。

## クエリを実行する

* GraphQL エディタでクエリを記述し、稼働中の API に対して実行できます。
* クエリ変数はクエリと一緒に、フォームまたは生の JSON として指定できます。
* 結果は DbGate 全体で使われているのと同じ高速でソート・フィルタリング可能なグリッドに返されるため、GraphQL のレスポンスがデータベースのテーブルのように扱えます。
* ネストされたオブジェクトやリストは構造化された JSON として返され、その場で展開して確認できます。

クエリしたビューは接続ごとにキャッシュされるため、作業を続けながら再度開いても即座に表示されます。

> DbGate Central の GraphQL 接続は、[デスクトップの GraphQL 機能](/ja/dbgate/developer/api-connections/#graphql)とは別の、ブラウザベースの実装です。デスクトップアプリを使用している場合は、そちらのページを参照してください。

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
