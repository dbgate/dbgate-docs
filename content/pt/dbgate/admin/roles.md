---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: pt
title: Funções
weight: 40
---

## Aba Roles
Configure funções, permissões de funções e o mapeamento entre funções e conexões. Você pode criar funções personalizadas e atribuir usuários a elas, de modo que as permissões e as conexões vinculadas sejam compartilhadas entre todos os usuários atribuídos a essa função.

Existem algumas funções predefinidas:
- superadmin - função usada para a página de administração, https://your_dbgate_instance/admin.html
- logged-user - função usada para todos os usuários logados. Você pode substituir a permissão para usuários específicos
- anonymous-user - função usada para usuários logados com o método de autenticação "Anonymous"

![Administração de funções - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Abas de detalhe da função
* Info
  * Configure as permissões da função
  * Configure os usuários atribuídos a essa função
* Team files - configure o acesso aos [arquivos de equipe](team-files)
* Connections - configure as conexões atribuídas a essa função
* Databases - configure as [permissões de banco de dados](permissions#database-permissions) para essa função
* Tables/views/objects - configure as [permissões de tabela](permissions#table-permissions) para essa função
* Disk files - configure o acesso a arquivos no disco/volume do docker
