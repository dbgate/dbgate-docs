---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: ja
title: クエリデザイナー
weight: 20
---

クエリデザイナー *(Premium)* を使うと、SQL を手書きすることなく、視覚的に SQL クエリを組み立てられます。キャンバスにテーブルを追加し、列を選択して条件を定義すれば、DbGate が SQL を生成します。

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## クエリの作成

* **テーブルの追加** - デザインキャンバスにテーブルをドロップします。DbGate は外部キーからリレーションを自動的に描画します。
* **列の選択** - 結果に表示する列を選び、並べ替えやグループ化を定義します。
* **JOIN の種類** - 標準の SQL 結合 (`INNER`、`LEFT`、`RIGHT`) に加えて、疑似結合も使用できます。最も便利なのは `WHERE NOT EXISTS` です。
* **強力なフィルター** - [データブラウザー](/ja/dbgate/working-with-data/data-browser/) と同じエンジンでフィルタリングでき、複合条件や値のセットによるフィルタリングにも対応しています。

## 結果

デザイナーは通常の SQL クエリを生成するため、手書きの SQL と同じパフォーマンスで実行されます。いつでも生成された SQL に切り替えて、[SQL エディター](sql-editor) で編集を続けられます。

## パースペクティブ - 万能デザイナー

入れ子になった階層的なビューや、SQL テーブルと MongoDB コレクションのデータをクライアント側で結合する場合は、[パースペクティブ](/ja/dbgate/working-with-data/perspectives/) を使用してください。ソースデータベースが結合できる範囲に制限されません。
