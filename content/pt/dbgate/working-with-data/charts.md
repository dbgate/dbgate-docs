---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: pt
title: Gráficos
weight: 30
---

Com o DbGate, você pode usar gráficos para visualizar suas consultas SQL. Basta executar a consulta; se um gráfico for detectado automaticamente, a aba "Chart 1" aparecerá. Se você tiver mais resultados de consulta, poderá haver mais gráficos.

Se nenhum gráfico for detectado automaticamente, mas você quiser criar algum gráfico a partir dos resultados da consulta, clique com o botão direito nos dados do resultado da consulta e escolha "Open chart".

![Captura de tela do gráfico](https://media.dbgate.io/img/query-result-chart-light.png)

## Configurações do gráfico
Use o botão {{< mdi "pencil" >}} Customize para abrir as configurações do gráfico. Você pode configurar a fonte de dados e o estilo do gráfico:
* Tipo de gráfico
  * Barras
  * Linhas
  * Linha do tempo - é um caso especial do gráfico de linhas, com tempo no eixo X
  * Pizza
  * Área polar
* Campo do eixo X - dados no eixo X. Para valores de data/hora, estão disponíveis funções de agrupamento e de linha do tempo
* Campo de agrupamento - define mais gráficos especificados pelo valor deste campo
* Transformação do eixo X - permite definir o agrupamento para a linha do tempo do eixo X (ex. por ano ou por mês)
* Campo N do eixo Y - você pode ter mais campos no eixo Y
  * Há um campo especial disponível para cada conjunto de dados, "Count", que conta as linhas
* Função de agregação - Sum, Minimum, Maximum, Average, First Value, Last Value

Quando você altera qualquer opção nas configurações do gráfico, ela é salva no início do script SQL como front-matter.

## Editando manualmente a definição do gráfico
Algumas opções não estão disponíveis no editor, mas podem ser editadas no código SQL. Leia [SQL front matter](/pt/dbgate/developer/sql-front-matter) para mais informações
