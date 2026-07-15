---
sourceHash: 0f10d627c0492363d84834c24da993d0686916c833728726a2d34648885161b1
language: pt
title: Editor de tabelas e esquemas
weight: 5
---

O DbGate pode criar e modificar a estrutura do banco de dados por meio de uma interface gráfica, sem escrever DDL manualmente. Abra o editor de estrutura de uma tabela pelo seu menu de contexto ("Edit table") ou crie uma nova tabela pelo menu de contexto do banco de dados.

![Table structure editor](https://media.dbgate.io/img/table-structure-editor-light.png)

## Editando tabelas

* **Colunas e tipos de dados** - defina colunas, tipos de dados, permissão de valores nulos e valores padrão para tabelas novas ou existentes.
* **Chaves e índices** - gerencie chaves primárias, chaves estrangeiras e índices.
* **Propriedades específicas do mecanismo** - defina opções específicas do banco de dados, como o mecanismo (engine) de tabela do MySQL.

## Prévia do SQL e alterações seguras

* **Prévia do SQL** - antes que qualquer coisa seja salva, o DbGate mostra o SQL gerado para que você possa revisá-lo.
* **Aviso de recriação de tabela** - quando uma alteração exige a recriação da tabela (uma limitação de alguns bancos de dados), o DbGate avisa você e permite inspecionar o script gerado primeiro.

## Outros objetos do banco de dados

Você também pode criar, remover e modificar outros objetos - views, procedures e funções - e navegar por tabelas, views, procedures, funções e coleções do MongoDB a partir da árvore de objetos.

## Páginas relacionadas

* [Comparar e implantar modelos](model-compare-deploy) - compare a estrutura entre bancos de dados e implante alterações *(Premium)*
* [Implantação de banco de dados](dbdeploy) - arquivos de modelo YAML/SQL e implantação via CLI
