---
title: MCP Server for AI Agents
weight: 50
---

DbGate Central can expose your workspace to AI assistants such as [Claude](https://claude.ai) as a remote **MCP (Model Context Protocol)** connector - so an agent can explore and query your APIs the same way you do, with access that you stay in control of.

## Setting it up

1. Open the **Settings** tab and create an **MCP profile**. Copy its **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), **Client ID** and **Client Secret**.
2. In claude.ai (or another MCP-compatible client), add a custom connector using that URL and the OAuth credentials.
3. In each connection's editor, set its **MCP access** level - **No access**, **Read-only** or **Writable**. The default is no access, so nothing is shared until you allow it.
4. The assistant runs the OAuth handshake and you consent, binding the connector to that profile and workspace.

Each workspace can have multiple MCP profiles, each with its own URL, credentials and per-connection grants. Authentication uses OAuth 2.1 with mandatory PKCE, and client secrets are encrypted at rest.

## What the agent can do

Available for **oData**, **GraphQL** and **Shopify** connections (SQLite/DuckDB are browser-only and out of scope for MCP):

* **List connections** the profile is allowed to use.
* **List entities** - tables, views or catalog entities.
* **Inspect the schema** - column names and types.
* **Query rows** - filter, page and select data.
* **Update rows** - Shopify only, and only when you grant Writable access.

Because reads and writes reuse the same engine as the grid and the scheduler, an agent sees exactly the same data and capabilities you do - never more than the access you grant.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
