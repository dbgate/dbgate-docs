---
title: Charts
weight: 85
---

With DbGate, you could use chart for visualization of your SQL queries. Simply execute query, in chart is auto-detected, the tab "Chart 1"  will appear. If you have more query results, there could be more charts.

If no chart is autodetected, but you would like to create some chart from your query results, right click on your query result data and choose "Open chart".

![Chart screenshot](https://media.dbgate.io/img/query-result-chart-light.png)

## Chart settings
Use {{< mdi "pencil" >}} Customize button for invoking chart settings. You could configure chart data source and style:
* Chart type - Line, Bar, Pie
* X axis field - data on X axis. For date/time calues, grouping and timeline functions are available
* X axis transform - allows to define grouping for X - axis timeline (eg. by year or by month)
* Y axis field N - you could have more fields on Y axis

When you change any option in chart settings, it is saved at the beginning of the SQL script as front-matter.

## Manually editing chart definition
Some options are not available in editor, but they could be edited in SQL code. Please read [SQL front matter](/sql-front-matter) for more info