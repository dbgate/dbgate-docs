---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: ja
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) は、データを扱うための無料のブラウザ内ツールです。インストールもログインも不要です。[DbGate Central](../dbgate-central/) と同じグリッド、フィルタリング、クエリエンジンの上に構築されているため、参照、フィルタリング、編集の操作感はどちらでも同じです。

## SQL を学び、教える

DbGate Lite は **SQLite と DuckDB** を WebAssembly によってブラウザ内で完全に実行します。

* 使い慣れた DbGate のグリッドで、サンプルデータベースに対して SQL クエリを記述して実行できます。
* ER 図でテーブル同士の関連を可視化できます。
* インストール不要、ログイン不要 - サイトを開けばすぐに作業を始められます。

## データファイルのアドホックな処理

DbGate Lite でファイルを開いて、データベースのように扱えます。

* CSV、JSON、Excel ファイルを **インポート** し、SQL でクエリまたは編集できます。
* データをクリーニングして整形し、結果を CSV、JSON、Excel に **エクスポート** して戻せます。

## リンクによるデータベースやクエリの共有

URL に特定のハッシュパラメーターを付けて DbGate Lite を開くと、一時データベースが自動的に初期化されます。

* `initdbtype` - データベースの種類、`sqlite` または `duckdb`
* `initdbscript` - 一時データベースを作成してデータを投入するために使用する SQL スクリプト
* `initquery` (省略可能) - 新しいクエリタブで開かれる SQL クエリ

リンクを開いた人は誰でも、同じサンプルデータベースとクエリをワンクリックで利用できます。チュートリアル、バグレポート、教育に便利です。

## 読み取り専用ビューの公開

編集可能なリンクの共有とは別に、ツールバーの Publish ボタンを使って CSV/JSON ファイルや BI レポートの読み取り専用ビューを **公開** できます。これにより、データとライト/ダークの切り替えだけを備え、サイドバーやエディターのない独立したページが開きます。リンクを知っている人なら誰でもアカウントなしで閲覧できます。

## Lite、Central、Premium、Team Premium の選び方

DbGate Lite は学習や単発の作業に最適です。継続的でプロフェッショナルな作業には、専用の製品の方が適しています。

* **DbGate Lite** - 無料、ブラウザ内で動作。SQL の学習やアドホックなデータファイルに最適です。
* **[DbGate Central](../dbgate-central/)** - API を扱うためのホスティング製品。ライブの GraphQL、oData、Shopify エンドポイントに接続し、接続情報やレポートをワークスペースに保存して、チームと共有できます。
* **[DbGate Premium](/ja/dbgate/getting-started/installation/)** - [DbGate](/ja/dbgate/) のエディションの一つ。データベースを扱うためのフル機能のデスクトップアプリケーションで、プロフェッショナルなツール一式を備えて SQL および NoSQL サーバーに接続できます。
* **[DbGate Team Premium](/ja/dbgate/getting-started/installation/docker-tp/)** - チーム向けの [DbGate](/ja/dbgate/) のもう一つのエディション。オンプレミスで動作する共有 Web インターフェースにより、チーム全体が自社のインフラ上でブラウザからデータベースを扱えます。
