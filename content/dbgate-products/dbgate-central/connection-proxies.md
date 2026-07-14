---
title: Connection Proxies
weight: 60
---

DbGate Central can reach oData and GraphQL APIs that live on a private network by routing their traffic through a small outbound agent that you run inside that network. Shopify and OpenAPI connections cannot be proxied.

## Setting up a proxy

1. Open the **Settings** tab and create a **proxy** under *Connection proxies*. Copy its generated token.
2. Tick the oData/GraphQL connections the proxy may serve. Each change regenerates the token, so restart the agent after changing the selection.
3. Run the agent inside your private network:
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   The agent only makes outbound connections - no inbound access to your network is required.
4. Once the agent is running and connected, requests to the proxied connections are routed through it. If the proxy is not connected, DbGate Central falls back to fetching directly.

The same routing also applies to the [MCP server](../mcp-server): when an MCP tool reads a proxied connection, the request goes through the same proxy.
