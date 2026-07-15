---
title: SQL editor
weight: 10
---

The SQL editor is where you write and run SQL scripts against your connection. Open it from the {{< mdi "flash" >}} "New query" button in the toolbar, or from the context menu of a connection or database.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## Running SQL

* **Execute script** - run the whole script with the {{< mdi "play" >}} Execute button (or F5).
* **Execute current statement** - run only the statement under the cursor.
* **Run selection** - if you select part of the script, only the selected text is executed.
* Results appear in the result grid below the editor. Multiple result sets are shown in separate tabs.
* Messages, row counts and errors are shown in the **Messages** tab.

## Editing helpers

* **SQL code formatter** - reformat the current script for consistent indentation and casing.
* **Code completion** - table, column and keyword suggestions based on the connected database schema.
* **Join helper** - the "Add SQL join" utility generates a `LEFT`/`INNER`/`RIGHT JOIN` clause from foreign keys, so you don't have to type join conditions by hand.

## Working with results

The result grid uses the same engine as the [data browser](/dbgate/working-with-data/data-browser/), so you can [filter and sort](/dbgate/working-with-data/data-filtering/), copy cells in various formats and [export](/dbgate/working-with-data/export-import/) the result.

### Edit query results & views *(Premium)*

Query results are editable when DbGate can map the result back to a single table or an updatable view. Edit cells directly in the result grid, review the generated change script and save it back to the database - the same staged-changes workflow as in the [data browser](/dbgate/working-with-data/data-browser/). Editing views is supported as well.

> Editable query results and editable views were introduced in DbGate 7.2.

## Transaction control

You can control transactions from the editor - execute inside an explicit transaction and commit or roll back the changes, which is useful when testing data-modifying scripts.

## Other editors

* **Mongo JavaScript editor** - for MongoDB connections, write and execute Mongo scripts using NodeJS syntax.
* **Redis** - browse the Redis key tree, generate a script from selected keys and run Redis scripts.
