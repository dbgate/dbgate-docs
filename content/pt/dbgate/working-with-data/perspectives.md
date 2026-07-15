---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: pt
title: Perspectivas
weight: 50
---

A perspectiva é uma visualização somente leitura de dados aninhados complexos. Ela se assemelha a relatórios, mas as perspectivas são criadas simplesmente adicionando dados à visualização. Você pode usar o designer de perspectivas, que permite unir dados seguindo outras relações além das chaves estrangeiras.

As perspectivas podem unir dados facilmente e exibir grupos.

<!-- ![screenshot](/screenshots/perspective1.png) -->

## Criar perspectiva
As perspectivas podem ser criadas a partir de tabelas e views SQL (coleções do MongoDB ainda não são suportadas, mas esse suporte está planejado).
Use o menu de contexto da tabela/view, "Open perspective".

![screenshot](/img/perspective-create.png)

O DbGate abre uma perspectiva simples, com apenas uma coluna exibida. Essa coluna é escolhida por um algoritmo heurístico, para ser a melhor representação da linha inteira.
## Personalizar perspectiva
Você pode definir quais colunas estão disponíveis na visualização. Também pode adicionar dados referenciados à visualização. Use o botão de expandir para navegar pela árvore de referências.

## Filtrar dados
Use o menu de contexto na tabela ou na lista de colunas do lado esquerdo, "Add to filter". Você pode usar as mesmas expressões de filtro que em outros lugares do DbGate. Ou pode usar o comando "Filter this value" do menu de contexto em uma célula da tabela.

## Filtrar linhas pai
Considere a perspectiva a seguir. Temos uma relação mestre/detalhe, Genre, com as tracks relacionadas. Queremos filtrar por Track (tentei pesquisar o texto "mix").

![screenshot](/img/parentrows1.png)

Como você pode ver, há muitas linhas de Genre sem nenhuma track correspondente aos critérios de pesquisa. Se quiser filtrar também as linhas de Genre, use o comando "Filter parent rows" no menu de contexto do cabeçalho da tabela. Você também pode usar o botão de alternância na linha de filtro.

![screenshot](/img/parentrows2.png)

## Definir junções personalizadas
As perspectivas funcionam muito bem com chaves estrangeiras. Mas mesmo quando você tem um banco de dados sem chaves estrangeiras, pode usar esse recurso. É possível definir uma junção personalizada com qualquer condição. Você pode até definir uma junção personalizada com outro banco de dados (que pode estar em um servidor de banco de dados diferente, inclusive com um mecanismo de banco de dados subjacente diferente).

![screenshot](/img/customjoin.png)

Você também pode arrastar &amp; soltar colunas para criar uma relação de junção.

![screenshot](/img/customjoin2.png)
