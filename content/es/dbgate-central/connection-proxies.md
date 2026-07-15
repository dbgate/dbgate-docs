---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: es
title: Proxies de conexión
weight: 60
---

DbGate Central puede acceder a APIs de oData y GraphQL que se encuentran en una red privada enrutando su tráfico a través de un pequeño agente saliente que se ejecuta dentro de esa red. Las conexiones de Shopify y OpenAPI no se pueden enrutar mediante proxy.

## Configuración de un proxy

1. Abra la pestaña **Settings** y cree un **proxy** en *Connection proxies*. Copie el token generado.
2. Marque las conexiones oData/GraphQL que el proxy puede atender. Cada cambio regenera el token, por lo que debe reiniciar el agente después de modificar la selección.
3. Ejecute el agente dentro de su red privada:
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   El agente solo establece conexiones salientes: no se requiere ningún acceso entrante a su red.
4. Una vez que el agente está en ejecución y conectado, las solicitudes a las conexiones con proxy se enrutan a través de él. Si el proxy no está conectado, DbGate Central recurre a la obtención directa de los datos.

El mismo enrutamiento se aplica también al [servidor MCP](../mcp-server): cuando una herramienta MCP lee una conexión con proxy, la solicitud pasa por el mismo proxy.
