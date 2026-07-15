---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: pt
title: Servidor MCP para Agentes de IA
weight: 50
---

O DbGate Central pode expor seu workspace a assistentes de IA como o [Claude](https://claude.ai) na forma de um conector **MCP (Model Context Protocol)** remoto - assim, um agente pode explorar e consultar suas APIs da mesma maneira que você, com um acesso que permanece sob seu controle.

## Configuração

1. Abra a aba **Settings** e crie um **MCP profile**. Copie a **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), o **Client ID** e o **Client Secret**.
2. No claude.ai (ou em outro cliente compatível com MCP), adicione um conector personalizado usando essa URL e as credenciais OAuth.
3. No editor de cada conexão, defina o nível de **MCP access** - **No access**, **Read-only** ou **Writable**. O padrão é sem acesso, portanto nada é compartilhado até que você permita.
4. O assistente executa o handshake OAuth e você concede o consentimento, vinculando o conector àquele profile e workspace.

Cada workspace pode ter vários MCP profiles, cada um com sua própria URL, credenciais e permissões por conexão. A autenticação usa OAuth 2.1 com PKCE obrigatório, e os client secrets são criptografados em repouso.

## O que o agente pode fazer

Disponível para conexões **oData**, **GraphQL** e **Shopify** (SQLite/DuckDB funcionam somente no navegador e estão fora do escopo do MCP):

* **Listar conexões** que o profile tem permissão de usar.
* **Listar entidades** - tabelas, views ou entidades de catálogo.
* **Inspecionar o schema** - nomes e tipos das colunas.
* **Consultar linhas** - filtrar, paginar e selecionar dados.
* **Atualizar linhas** - somente Shopify, e apenas quando você concede acesso Writable.

Como as leituras e gravações reutilizam o mesmo mecanismo da grade e do agendador, um agente vê exatamente os mesmos dados e recursos que você - nunca mais do que o acesso que você concede.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
