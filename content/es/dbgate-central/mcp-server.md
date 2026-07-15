---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: es
title: Servidor MCP para agentes de IA
weight: 50
---

DbGate Central puede exponer tu espacio de trabajo a asistentes de IA como [Claude](https://claude.ai) mediante un conector remoto **MCP (Model Context Protocol)**, de modo que un agente pueda explorar y consultar tus API igual que lo haces tú, con un acceso que sigues controlando.

## Configuración

1. Abre la pestaña **Settings** y crea un **perfil MCP**. Copia su **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), el **Client ID** y el **Client Secret**.
2. En claude.ai (u otro cliente compatible con MCP), añade un conector personalizado usando esa URL y las credenciales de OAuth.
3. En el editor de cada conexión, establece su nivel de **MCP access**: **No access**, **Read-only** o **Writable**. El valor predeterminado es sin acceso, por lo que no se comparte nada hasta que lo permitas.
4. El asistente ejecuta el intercambio OAuth y tú das tu consentimiento, vinculando el conector a ese perfil y espacio de trabajo.

Cada espacio de trabajo puede tener varios perfiles MCP, cada uno con su propia URL, credenciales y permisos por conexión. La autenticación utiliza OAuth 2.1 con PKCE obligatorio, y los client secrets se almacenan cifrados.

## Qué puede hacer el agente

Disponible para conexiones **oData**, **GraphQL** y **Shopify** (SQLite/DuckDB funcionan solo en el navegador y quedan fuera del alcance de MCP):

* **Listar conexiones** que el perfil tiene permitido usar.
* **Listar entidades**: tablas, vistas o entidades de catálogo.
* **Inspeccionar el esquema**: nombres y tipos de columnas.
* **Consultar filas**: filtrar, paginar y seleccionar datos.
* **Actualizar filas**: solo en Shopify, y únicamente cuando concedes acceso Writable.

Como las lecturas y escrituras reutilizan el mismo motor que la cuadrícula y el planificador, un agente ve exactamente los mismos datos y capacidades que tú, nunca más allá del acceso que le concedes.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
