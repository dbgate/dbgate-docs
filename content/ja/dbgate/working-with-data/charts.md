---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: ja
title: チャート
weight: 30
---

DbGate では、SQL クエリを可視化するためにチャートを使用できます。クエリを実行するだけで、チャートが自動検出されると「Chart 1」タブが表示されます。クエリ結果が複数ある場合は、チャートも複数になることがあります。

チャートが自動検出されないものの、クエリ結果からチャートを作成したい場合は、クエリ結果のデータを右クリックして「Open chart」を選択してください。

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## チャートの設定
チャート設定を呼び出すには {{< mdi "pencil" >}} Customize ボタンを使用します。チャートのデータソースとスタイルを設定できます。
* チャートの種類
  * Bar
  * Line
  * Timeline - X 軸に時間を取る折れ線チャートの特別なケースです
  * Pie
  * Polar area
* X 軸フィールド - X 軸のデータです。日付/時刻の値に対しては、グループ化とタイムライン関数が利用できます
* グループ化フィールド - このフィールドの値によって複数のチャートを定義します
* X 軸変換 - X 軸のタイムラインのグループ化を定義できます (例: 年ごと、月ごと)
* Y 軸フィールド N - Y 軸には複数のフィールドを持たせることができます
  * 各データセットには特別なフィールド「Count」が用意されており、行数をカウントします
* 集計関数 - Sum、Minimum、Maximum、Average、First Value、Last Value

チャート設定のオプションを変更すると、その内容は SQL スクリプトの先頭に front-matter として保存されます。

## チャート定義の手動編集
一部のオプションはエディターでは利用できませんが、SQL コード内で編集できます。詳細については [SQL front matter](/ja/dbgate/developer/sql-front-matter) をお読みください
