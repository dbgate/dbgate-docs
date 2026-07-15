---
sourceHash: 80df2a73525118cee579014e200ff5f67715aa6f35468656abb3f8b70c254566
language: pt
title: Arquivos de dados
weight: 1
---

Arquivos (archives) são pastas com dados no formato JSONL (NDJSON). O DbGate permite trabalhar com eles de forma muito eficiente: você pode importá-los para o banco de dados, exportá-los para outros formatos ou editar os dados diretamente no arquivo. Um arquivo se comporta como um banco de dados muito rápido e leve armazenado em arquivos locais.

## Formato JSONL
O DbGate usa o formato JSONL internamente em todos os lugares. JSONL é um arquivo de texto no qual cada linha contém uma linha de dados serializada em JSON. O DbGate assume que a primeira linha pode conter um cabeçalho (também em JSON), com a estrutura da tabela. Quando você usa JSONL com estrutura dinâmica (sem a primeira linha fixa), esse formato é padronizado e pode ser carregado em muitas outras ferramentas.

## Pastas de arquivos
O arquivo é organizado em pastas, com arquivos JSONL. Ele tem uma estrutura semelhante à de um banco de dados. Você pode então exportar todo o banco de dados para um novo arquivo - cada tabela é exportada para um arquivo JSON e, graças à linha de cabeçalho, a estrutura da tabela também é preservada.

## Visualizar e editar arquivos de dados
Você pode abrir arquivos JSONL em diferentes modos:
- menu de contexto "Open" - abre a grade de dados, que permite ordenar, filtrar e editar seus dados JSONL
- menu de contexto "Open in text editor" - permite editar manualmente o arquivo JSONL

## Arquivos de dados e modelos de BD
As pastas de arquivos também são usadas como armazenamento para modelos de BD. Você pode exportar o modelo de BD no menu de contexto do banco de dados, "Export DB model". Você pode então editar esse modelo (arquivos YAML para a estrutura das tabelas, arquivos SQL para views e stored procedures), compará-lo com o banco de dados real e implantá-lo no banco de dados
