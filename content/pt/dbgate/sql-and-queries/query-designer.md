---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: pt
title: Designer de consultas
weight: 20
---

O designer de consultas *(Premium)* permite criar consultas SQL visualmente, sem escrever SQL manualmente. Adicione tabelas à área de trabalho, escolha colunas e defina condições - o DbGate gera o SQL para você.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## Criando uma consulta

* **Adicionar tabelas** - arraste tabelas para a área de design; o DbGate desenha as relações a partir das chaves estrangeiras automaticamente.
* **Escolher colunas** - escolha quais colunas aparecem no resultado, defina ordenação e agrupamento.
* **Tipos de JOIN** - além dos joins SQL padrão (`INNER`, `LEFT`, `RIGHT`), você pode usar pseudo-joins - sendo o mais útil o `WHERE NOT EXISTS`.
* **Filtros poderosos** - filtre usando o mesmo mecanismo do [navegador de dados](/pt/dbgate/working-with-data/data-browser/), incluindo condições compostas e filtragem por um conjunto de valores.

## Resultado

O designer produz uma consulta SQL comum, portanto ela é executada com o mesmo desempenho de um SQL escrito à mão. Você pode alternar para o SQL gerado a qualquer momento e continuar editando-o no [editor SQL](sql-editor).

## Perspectivas - o designer universal

Para visualizações aninhadas e hierárquicas - e para juntar dados entre tabelas SQL e coleções MongoDB no lado do cliente - use as [Perspectivas](/pt/dbgate/working-with-data/perspectives/), que não são limitadas pelo que o banco de dados de origem consegue juntar.
