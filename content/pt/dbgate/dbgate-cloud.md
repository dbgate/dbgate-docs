---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: pt
title: DbGate Cloud
weight: 80
---

O DbGate Cloud é um armazenamento online para suas conexões, scripts SQL e outros objetos. Ele também oferece uma base de conhecimento pública com scripts SQL úteis.

> O DbGate Cloud é um complemento de armazenamento para o aplicativo **desktop** do DbGate (conexões, scripts SQL, pastas compartilhadas). Procurando um aplicativo hospedado, exclusivamente no navegador? Veja [DbGate Central](/pt/dbgate-central/).

## Entrar
Para usar o DbGate Cloud, é necessário entrar. Use o ícone {{< mdi "account-remove-outline" >}} no painel esquerdo.

Seu armazenamento na nuvem está sempre associado ao seu endereço de e-mail.  
Você pode escolher um dos seguintes provedores de autenticação:
* GMail
* GitHub
* E-mail - um link mágico de acesso único será enviado para o seu e-mail

Os servidores do DbGate não armazenam sua senha.

## Usar conexões armazenadas na nuvem
Seu conteúdo na nuvem aparece no widget {{< mdi "cloud-key" >}} após entrar. Por padrão, você vê sua pasta Private (com acesso de escrita).

Salvar conexão na nuvem:
* No menu de contexto da conexão, escolha "Copy to cloud folder"
* Clique em {{<mdi "plus-thick" >}} e escolha "Add connection on cloud"

## Qual conexão está armazenada na nuvem?
* Suas conexões na nuvem estão sempre no widget {{< mdi "cloud-key" >}}
* Suas conexões armazenadas localmente estão no widget {{< mdi "database" >}}

## Trabalhando com pastas
Você pode criar outras pastas além da sua pasta Private (é necessária a edição Premium).

No botão {{<mdi "plus-thick" >}}, estão disponíveis os comandos:
* New shared folder - cria uma nova pasta compartilhada. Por padrão, ela é acessível somente por você, e você pode convidar outros usuários
* Add existing shared folder - se você tem um link de convite para alguma pasta compartilhada (criada por outro usuário), este é o lugar certo para usá-lo

Se quiser compartilhar sua pasta com outras pessoas, clique com o botão direito na pasta e escolha "Copy invite link"

## Permissões de pastas compartilhadas
* Admin - você tem acesso total à pasta, pode convidar outras pessoas e gravar conteúdo
* Write - você pode gravar/excluir conteúdo, mas não pode convidar outras pessoas
* Read - somente leitura do conteúdo da pasta. Tenha em mente que esta permissão não se aplica aos bancos de dados disponíveis dentro de uma conexão definida no servidor

## Pastas compartilhadas na edição Community
Na edição Community, você pode usar pastas compartilhadas criadas por usuários Premium, mas não pode criar suas próprias pastas compartilhadas. Isso permite que equipes com a edição Premium compartilhem conexões, arquivos SQL e diagramas ER com outros membros da equipe que usam a edição Community.

## Base de conhecimento pública
A base de conhecimento pública é uma coleção de scripts SQL e gráficos úteis para tarefas como ajuste de desempenho SQL, análise de deadlocks, uso de índices etc... A base de conhecimento está disponível em todas as edições, mas os gráficos estão disponíveis apenas nas edições Premium.

Você pode ver todos os itens no ícone {{< mdi "cloud-search" >}} no painel de widgets à esquerda.  
Scripts em cinza indicam scripts que não são compatíveis com o banco de dados atualmente selecionado.

Se você quiser aprimorar a base de conhecimento com seus scripts SQL, crie um pull request no repositório GIT [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base).

Os scripts na base de conhecimento são anotados com a sintaxe [SQL front matter](/pt/dbgate/developer/sql-front-matter)

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)

