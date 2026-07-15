---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: pt
title: Recursos de IA
weight: 55
---

O DbGate inclui vários recursos baseados em IA *(Premium e Team Premium)*. Eles estão disponíveis para todos os usuários Premium sem chaves de API ou configuração - o DbGate usa seu próprio gateway de IA, que encaminha as requisições para o provedor de LLM.

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## Chat com o banco de dados

O chat com o banco de dados é um chatbot de IA que entende tanto o esquema do seu banco de dados quanto seus dados.

* **Conversa natural** - faça perguntas em qualquer linguagem natural e receba respostas ou SQL pronto para executar.
* **Ciente do contexto** - o modelo conhece o seu esquema e (com permissão) os dados reais, então ele sugere joins, filtros e agregações corretos.
* **Iterativo** - refine com comandos como "adicione um filtro de data" ou "agrupe por cliente" e a consulta é atualizada instantaneamente.
* **Gráficos** - peça um gráfico de barras, de pizza ou de linhas construído a partir dos resultados.
* **Modo consultor** - ele pode analisar stored procedures e views, então você pode perguntar coisas como "Explique a procedure X" ou "Quais tabelas são afetadas pela procedure Y". O DbGate mostra quais objetos foram analisados.

### Executando SQL - segurança em primeiro lugar

O chat com o banco de dados pode executar SQL para responder às perguntas. Você escolhe como:

* **Perguntar antes de executar SQL (padrão)** - o DbGate pergunta antes de executar cada consulta.
* **Executar SQL automaticamente** - consultas que não sejam `SELECT` ainda exigem confirmação.
* **Nunca executar, apenas sugerir SQL** - o chat apenas mostra as consultas; nenhum dado do seu banco de dados é enviado ao LLM.

Se uma consulta sugerida falhar, o DbGate envia o erro de volta ao modelo, que normalmente corrige a consulta automaticamente.

## Assistente de IA para SQL

Use o chat como um assistente de SQL - "Escreva uma consulta SQL para os 10 principais clientes por vendas" - e abra o resultado em uma aba do [editor SQL](/pt/dbgate/sql-and-queries/sql-editor/).

## Explicar erro de SQL

Clique em **Explain** ao lado de uma mensagem de erro para obter uma explicação de IA sobre o que deu errado e como corrigir.

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## Assistente de IA para temas

A IA também pode gerar temas de cores personalizados - veja [Temas personalizados](/pt/dbgate/customization/custom-themes/).

## Desativando os recursos de IA

Os recursos de IA podem ser desativados por completo (por exemplo, em ambientes restritos) através das configurações do DbGate.
