---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: pt
title: Consultando APIs GraphQL
weight: 20
---

Aponte o DbGate Central para qualquer API GraphQL e ele descobre o que está disponível para você - sem precisar vasculhar documentações separadas.

## Explore o schema

O DbGate Central faz a introspecção do schema GraphQL assim que você se conecta. Navegue pelos tipos e campos disponíveis na árvore e abra uma aba de consulta para começar a trabalhar.

## Execute consultas

* Escreva consultas com o editor GraphQL e execute-as na API ao vivo.
* Forneça variáveis de consulta junto com a consulta, seja em um formulário ou como JSON puro.
* Os resultados voltam na mesma grade rápida, ordenável e filtrável usada em todo o DbGate, de modo que uma resposta GraphQL parece uma tabela de banco de dados.
* Objetos e listas aninhados são retornados como JSON estruturado que você pode expandir e inspecionar ali mesmo.

As visualizações consultadas são armazenadas em cache por conexão, então reabri-las é instantâneo enquanto você continua trabalhando.

> As conexões GraphQL no DbGate Central são uma implementação separada, baseada em navegador, do [recurso GraphQL da versão desktop](/pt/dbgate/developer/api-connections/#graphql) - consulte essa página se você estiver usando o aplicativo desktop.

![DbGate Central - consultar uma API GraphQL](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
