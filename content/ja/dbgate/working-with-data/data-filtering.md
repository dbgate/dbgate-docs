---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: ja
title: データフィルタリング
weight: 10
---

DbGate は強力なデータフィルタリングエンジンを備えており、非常に簡単なデータフィルタリングから複雑な条件まで対応できます。

データフィルターは DbGate のさまざまな場所で使用できますが、最も一般的なのはデータグリッドのフィルタリングです。

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

フィルターには背景色が付きます。
* 緑の背景 - フィルターが正しく、適用されています
* 赤の背景 - フィルター式にエラーがあり、フィルターは無視されます

フィルターを作成する方法はいくつかあります。
* {{< mdi "filter" >}} - 定義済みのフィルターとダイアログのメニューを表示します
* {{< mdi "dots-vertical" >}} - フィルターする値を選択できます
* フィルターを直接記述できます - [filter-expressions](#filter-expressions) で説明されている非常に簡単な構文を使用します
* または、ビジュアルな方法でフィルターを作成し、手動で編集することもできます

その他のコマンド:
* {{< mdi "filter-off" >}} - すべてのフィルターをクリアします

## Filter expressions
フィルター式は直感的に使えるように設計されており、ほとんどの場合、検索したい内容をそのまま記述するだけです。ただし、構文は非常に強力で、複数の条件を組み合わせたり、さまざまな演算子を使用したりできます。
式の構文は列のデータ型によって異なります。

### Examples

| 列の型 | フィルター式 |  説明 |
|----------|-------------|------|
| string | canada | 列の値にテキスト "canada" が含まれる |
| string | canada, usa | 列の値にテキスト "canada" または "usa" が含まれる |
| string | canada lake | 列の値にテキスト "canada" と "lake" が含まれる |
| string | NOT EMPTY NOT NULL | 文字列が空でない値を持つ |
| number | >10 | 列の値が 10 より大きい |
| number | >=5 <=10 | 列の値が 5 以上 10 以下 |
| number | 1,2,3 | 列の値が 1 または 2 または 3 |
| datetime | 2020-05-26 | 日付の値が 2020-05-26 のもの（24 時間の範囲）  |

### Common filters (for all data types)
- NULL - 列の値が null である
- NOT NULL - 列の値が null でない
- {$$ is null} - SQL 条件、{} 括弧内に記述します。$$ はフィルター対象の列のプレースホルダーです

### Text filters
テキストの比較は大文字小文字を区別しません。
- text - 列の値に _text_ が含まれる。'シングルクォート' または "ダブルクォート" で囲むこともできます
- +text - 列の値に _text_ が含まれる（上の行と同じ）
- ^text - 列の値が _text_ で始まる
- $text - 列の値が _text_ で終わる
- !+text - 列の値に _text_ が含まれない（上の行と同じ）
- !^text - 列の値が _text_ で始まらない
- !$text - 列の値が _text_ で終わらない
- EMPTY - 列の値に空白以外の文字が含まれない
- NOT EMPTY - 列の値に空白以外の文字が含まれる

### Number filters
- number - 列の値が number と等しい
- =number - 列の値が number と等しい
- !=number - 列の値が number と等しくない
- <>number - 列の値が number と等しくない
- <number - 列の値が number より小さい
- \>number - 列の値が number より大きい
- <=number - 列の値が number 以下である
- \>=number - 列の値が number 以上である

### Datetime filters
- 2021 - 列の値の年
- 2021-02 - 列の値の年、月
- 2021-02-15 - 列の値の年、月、日
- 2021-02-15 23:15 - 列の値の年、月、日、時、分
- 2021-02-15 23:15:51 - 列の値の年、月、日、時、分、秒
- 現在の日付を基準とした相対フィルター
  - YESTERDAY
  - TODAY
  - TOMORROW
  - LAST WEEK
  - THIS WEEK
  - NEXT WEEK
  - LAST MONTH
  - THIS MONTH
  - NEXT MONTH
  - LAST YEAR
  - THIS YEAR
  - NEXT YEAR

### Logical (boolean) filters
- TRUE, true, 1 - 列の値が true/1 である
- FALSE, false, 0 - 列の値が false/0 である

### Combinations of filters
フィルターは組み合わせることができます。スペースは AND 演算子、カンマは OR 演算子として解釈されます。AND は OR よりも優先順位が高くなります。
