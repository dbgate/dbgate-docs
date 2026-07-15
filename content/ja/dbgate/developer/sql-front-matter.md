---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: ja
title: SQL フロントマター
weight: 50
---

SQL フロントマターとは、SQL ファイルの先頭に YAML 形式で記述されたメタデータです。この概念は、マークダウンファイル向けにフロントマターを導入した gohugo と Jekyll から着想を得ています。([Hugo のフロントマター](https://gohugo.io/content-management/front-matter/))

SQL フロントマターは、SQL ファイルの先頭にあるファイル開始マーク `-- >>>` から始まり、`-- <<<` のみを含む行で終わります。YAML コンテンツの各行には `-- ` という接頭辞が付くため、ファイル全体は有効な SQL のままとなります。

このメタデータは、特にチャート（チャート設定の保存）や公開ナレッジベースの属性（スクリプトのタイトルや説明など）に使用されます。ただし、DbGate のあらゆる SQL スクリプトで利用できる属性もあります。

## 汎用属性
- autoExecute: `true` または `false`。スクリプトを開いたときに自動的に実行するかどうか
- splitterInitialValue: パーセンテージ（20% など）または絶対サイズ（220px など） - 上部の SQL 領域のサイズを定義するために使用します。残りの領域はクエリ結果に使用されます

## 公開ナレッジベースの属性
- title: スクリプトのタイトル（デフォルト - 拡張子なしのファイル名）
- description: スクリプトの説明（デフォルト - 空）
- icon: スクリプトのアイコン（[Material design icons](https://pictogrammers.com/library/mdi/) から、`mdi mdi-chart-pie` の形式で指定）

## チャート属性
- selected-chart: 自動選択するチャートの番号（1 から）
- chart-N: N 番目のチャートの定義
    - title: チャートのタイトル
    - pieRatioLimit - 円グラフの制限値。値がこれを下回る場合、「その他」にグループ化されます（デフォルト: 0.05）
    - pieCountLimit - 円グラフのスライス数の制限値。スライス数がこれを超える場合、「その他」にグループ化されます（デフォルト 10）
    - dataLabelFormatter - データラベルのフォーマッター。'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb' のいずれか

最新の完全なフィールド一覧については、[TypeScript の定義](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts)の `ChartDefinition` インターフェイスを参照してください

## 例

```sql
-- >>>
-- selected-chart: 1
-- chart-1:
--   chartType: bar
--   xdef:
--     field: InvoiceDate
--     transformFunction: date:month
--   ydefs:
--     - field: Total
--       aggregateFunction: sum
-- <<<
SELECT
  `InvoiceId`,
  `CustomerId`,
  `InvoiceDate`,
  `BillingAddress`,
  `BillingCity`,
  `BillingState`,
  `BillingCountry`,
  `BillingPostalCode`,
  `Total`
FROM
  `Invoice`
```