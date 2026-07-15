---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: pt
title: Editor SQL
weight: 10
---

O editor SQL é onde você escreve e executa scripts SQL na sua conexão. Abra-o pelo botão {{< mdi "flash" >}} "Nova consulta" na barra de ferramentas ou pelo menu de contexto de uma conexão ou banco de dados.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## Executando SQL

* **Executar script** - execute o script inteiro com o botão {{< mdi "play" >}} Executar (ou F5).
* **Executar instrução atual** - execute apenas a instrução sob o cursor.
* **Executar seleção** - se você selecionar parte do script, apenas o texto selecionado é executado.
* Os resultados aparecem na grade de resultados abaixo do editor. Múltiplos conjuntos de resultados são exibidos em abas separadas.
* Mensagens, contagens de linhas e erros são exibidos na aba **Mensagens**.

## Auxiliares de edição

* **Formatador de código SQL** - reformata o script atual para uma indentação e capitalização consistentes.
* **Autocompletar código** - sugestões de tabelas, colunas e palavras-chave com base no esquema do banco de dados conectado.
* **Auxiliar de join** - o utilitário "Adicionar join SQL" gera uma cláusula `LEFT`/`INNER`/`RIGHT JOIN` a partir de chaves estrangeiras, para que você não precise digitar as condições de join manualmente.

## Trabalhando com resultados

A grade de resultados usa o mesmo mecanismo que o [navegador de dados](/pt/dbgate/working-with-data/data-browser/), portanto você pode [filtrar e ordenar](/pt/dbgate/working-with-data/data-filtering/), copiar células em vários formatos e [exportar](/pt/dbgate/working-with-data/export-import/) o resultado.

### Editar resultados de consultas e views *(Premium)*

Os resultados de consultas são editáveis quando o DbGate consegue mapear o resultado de volta para uma única tabela ou para uma view atualizável. Edite as células diretamente na grade de resultados, revise o script de alterações gerado e salve-o de volta no banco de dados - o mesmo fluxo de trabalho de alterações preparadas do [navegador de dados](/pt/dbgate/working-with-data/data-browser/). A edição de views também é suportada.

> Resultados de consultas editáveis e views editáveis foram introduzidos no DbGate 7.2.

## Controle de transações

Você pode controlar as transações a partir do editor - execute dentro de uma transação explícita e confirme (commit) ou reverta (rollback) as alterações, o que é útil ao testar scripts que modificam dados.

## Outros editores

* **Editor JavaScript do Mongo** - para conexões MongoDB, escreva e execute scripts do Mongo usando a sintaxe do NodeJS.
* **Redis** - navegue pela árvore de chaves do Redis, gere um script a partir das chaves selecionadas e execute scripts do Redis.
