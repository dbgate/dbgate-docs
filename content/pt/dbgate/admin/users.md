---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: pt
title: Usuários
weight: 30
---

## Aba Users
Configure usuários, senhas, permissões de usuários e o mapeamento entre usuários e conexões.
As senhas são usadas apenas para métodos de autenticação "Local". Mas todos os métodos com provedores de identidade externos usam a busca de usuários, portanto você pode configurar as permissões e as conexões disponíveis para o usuário, mesmo para usuários autenticados externamente.

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### Abas de detalhe do usuário
* Info
  * Configure as permissões do usuário
  * Configure as funções atribuídas a este usuário
* Team files - configure o acesso aos [arquivos de equipe](team-files)
* Connections - configure as conexões atribuídas a este usuário
* Databases - configure as [permissões de banco de dados](permissions#database-permissions) para este usuário
* Tables/views/objects - configure as [permissões de tabela](permissions#table-permissions) para este usuário
* Disk files - configure o acesso a arquivos em disco/volume do docker
