---
sourceHash: a1e2c8e626b7d397e242c5a182c920ca58971109a164a8c90e909a521a92e5db
language: pt
title: Mapas
weight: 40
---

O DbGate oferece suporte à exibição de dados geográficos em mapas.

## Fontes de mapas suportadas
- MySQL: todas as colunas espaciais
- MSSQL: colunas GEOGRAPHY
- PostGIS: colunas GEOGRAPHY
- Todas as fontes de dados: coordenadas armazenadas em colunas de latitude/longitude

## Abrindo a visualização de mapa
A visualização de mapa é aberta a partir da grade de dados. Primeiro, selecione as células com os dados geográficos desejados. A maneira mais simples é selecionar uma célula GEOGRAPHY ou GEOMETRY. Você também pode selecionar várias linhas. Em seguida, clique no widget Dados da célula. O mapa deve aparecer no widget de dados da célula.

![screenshot](/img/map1.png)

Quando você tiver colunas de latitude e longitude armazenadas, selecione todos os dados que deseja exibir no mapa. As colunas diferentes de latitude ou longitude serão exibidas nos popups dos marcadores.

![screenshot](/img/map2.png)

Como alternativa, você pode usar o menu de contexto "Abrir seleção no mapa" na grade de dados sobre as células selecionadas; então uma nova aba com o mapa será aberta.

No menu de contexto do mapa, também existe a possibilidade de exportar o mapa para um arquivo HTML independente, que pode ser exibido em qualquer lugar, mesmo onde o DbGate não esteja instalado.
