---
title: DbGate Lite
weight: 20
---

[DbGate Lite](https://lite.dbgate.io/) is a free, in-browser tool for working with data - no installation and no login required. It is built on the same grid, filtering and query engine as [DbGate Central](../dbgate-central/), so browsing, filtering and editing feel the same in both.

## Learn and teach SQL

DbGate Lite runs **SQLite and DuckDB** entirely in your browser, using WebAssembly:

* Write and run SQL queries against a sample database in the familiar DbGate grid.
* Visualize how tables relate with ER diagrams.
* No install, no login - open the site and start working.

## Ad-hoc work with data files

Open a file in DbGate Lite and treat it like a database:

* **Import** CSV, JSON and Excel files and query or edit them with SQL.
* Clean and reshape data, then **export** the result back to CSV, JSON or Excel.

## Sharing a database or query with a link

Opening DbGate Lite with certain hash parameters in the URL automatically initializes a temporary database:

* `initdbtype` - database type, `sqlite` or `duckdb`
* `initdbscript` - SQL script used to create and fill the temporary database
* `initquery` (optional) - SQL query opened in a new Query tab

Anyone who opens the link gets the same sample database and query in one click - useful for tutorials, bug reports and teaching.

## Publishing a read-only view

Separately from sharing an editable link, you can **publish** a read-only view of a CSV/JSON file or a BI report using the Publish button in the toolbar. This opens a standalone page - just the data and a light/dark toggle, no sidebar or editor - that anyone with the link can view without an account.

## Choosing between Lite, Central, Premium and Team Premium

DbGate Lite is best for learning and one-off tasks. For ongoing, professional work, a dedicated product is a better fit:

* **DbGate Lite** - free, in-browser. Best for learning SQL and ad-hoc data files.
* **[DbGate Central](../dbgate-central/)** - hosted product for working with APIs: connect to live GraphQL, oData and Shopify endpoints, keep connections and reports in a workspace, and share them with your team.
* **[DbGate Premium](/getting-started/installation/)** - the full desktop application for working with databases: connect to SQL and NoSQL servers with the complete set of professional tools.
* **[DbGate Team Premium](/getting-started/installation/docker-tp/)** - for teams: a shared web interface that runs on-premise, so your whole team works with databases from the browser on your own infrastructure.
