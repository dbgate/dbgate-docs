---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: pt
title: Proxies de conexão
weight: 60
---

O DbGate Central pode acessar APIs oData e GraphQL que estão em uma rede privada, roteando o tráfego delas por meio de um pequeno agente de saída que você executa dentro dessa rede. Conexões Shopify e OpenAPI não podem ser roteadas por proxy.

## Configurando um proxy

1. Abra a aba **Settings** e crie um **proxy** em *Connection proxies*. Copie o token gerado.
2. Marque as conexões oData/GraphQL que o proxy pode atender. Cada alteração regenera o token, portanto reinicie o agente após alterar a seleção.
3. Execute o agente dentro da sua rede privada:
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   O agente faz apenas conexões de saída - nenhum acesso de entrada à sua rede é necessário.
4. Assim que o agente estiver em execução e conectado, as requisições para as conexões com proxy são roteadas por ele. Se o proxy não estiver conectado, o DbGate Central volta a buscar os dados diretamente.

O mesmo roteamento também se aplica ao [servidor MCP](../mcp-server): quando uma ferramenta MCP lê uma conexão com proxy, a requisição passa pelo mesmo proxy.
