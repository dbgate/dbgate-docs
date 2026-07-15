---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: pt
title: Administração
weight: 60
---

A interface de administração permite que uma equipe execute o DbGate como uma aplicação web compartilhada e multiusuário: você gerencia conexões de forma centralizada, define quem pode entrar e como, e concede acesso refinado a bancos de dados e objetos por meio de usuários, funções e permissões. Ela também hospeda arquivos compartilhados da equipe. Tudo o que é configurado aqui é armazenado no banco de dados de armazenamento, e não em arquivos locais.

A ferramenta de administração está disponível somente na edição Team Premium. Na edição Community, configure o DbGate usando [variáveis de ambiente](/pt/dbgate/customization/env-variables).

Toda a configuração da administração é salva no banco de dados de armazenamento - use as [variáveis de ambiente STORAGE_xxx](/pt/dbgate/customization/env-variables/#team-premium-edition-configuration) para configurá-lo.

Nesta seção:

* [Autenticação](auth) - configure métodos de login e provedores de identidade
* [Conexões](connection) - gerencie as conexões disponíveis para sua equipe
* [Arquivos da Equipe](team-files) - compartilhe scripts SQL, diagramas ER e gráficos
* [Usuários](users) - gerencie contas de usuário
* [Funções](roles) - agrupe permissões em funções
* [Permissões](permissions) - conceda acesso a conexões, bancos de dados e tabelas

## Acesso de administrador

A página de administração está disponível na URL https://your_dbgate_instance/admin.html . 

O administrador root deve ter uma senha definida. Você pode definir a variável de ambiente ADMIN_PASSWORD. Se essa variável não estiver definida, o DbGate solicitará a senha de administrador na primeira vez.

Você pode então adicionar a permissão de administração a outro usuário com um método de autenticação diferente, mas primeiro você precisa abrir esta página de administração.

