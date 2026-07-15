---
sourceHash: 9faead63589d3a58402650e29cd85afd2223ffa5317dbd506eb962c893c3c04e
language: pt
title: Comparar e implantar modelos
weight: 15
---

O DbGate pode comparar a estrutura do banco de dados e implantar alterações *(Premium)*. Isso é útil para manter os ambientes sincronizados e para versionar o seu esquema.

![Compare database](https://media.dbgate.io/img/compare-database-settings-light.png)

## Comparar bancos de dados

* **Comparar dois bancos de dados** - encontre diferenças em colunas, definições de views e outros objetos SQL.
* **Sincronizar estrutura** - gere e execute as ações necessárias para que um banco de dados fique igual a outro.
* **Comparar com um modelo YAML** - compare um banco de dados real com um modelo armazenado em YAML e implante as diferenças.
* **Configurações** - controle a comparação, por exemplo, ignorando chaves estrangeiras, excluindo objetos específicos ou escolhendo quais ações de sincronização executar.

## Exportar um modelo de banco de dados

* **Scaffold para uma pasta** - salve o modelo de um banco de dados existente em uma pasta ou em um único arquivo JSON.
* **Arquivos YAML de tabelas** - as tabelas são armazenadas como arquivos YAML simples que você pode manter em um repositório Git.
* **Arquivos de definição SQL** - views, procedures e funções são armazenadas como arquivos SQL.

## Implantar

Implante o modelo visualmente com a ferramenta Compare ou pela linha de comando como parte de um pipeline de CI/CD. Para o formato do arquivo de modelo e o fluxo de trabalho da CLI, consulte [Implantação de banco de dados](dbdeploy).

## Páginas relacionadas

* [Editor de tabelas e esquemas](schema-editor) - edite a estrutura das tabelas pela interface gráfica
* [Implantação de banco de dados](dbdeploy) - formato do arquivo de modelo e implantação por linha de comando
