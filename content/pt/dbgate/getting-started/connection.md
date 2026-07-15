---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: pt
title: Conexão
weight: 20
---

Conectar-se ao seu banco de dados a partir do DbGate é fácil. Você pode se conectar a um banco de dados de algumas maneiras diferentes:

* Menu Arquivo/Adicionar conexão ou ícone {{< mdi "plus-thick" >}} no widget CONEXÕES
* Menu Arquivo/Novo banco de dados SQLite - cria um novo banco de dados SQLite
* Menu Arquivo/Abrir - você pode abrir um banco de dados SQLite existente

## Tela de conexão
![Tela de conexão](https://media.dbgate.io/img/new-connection-light.png)

Os campos da tela de conexão dependem muito do tipo de conexão.

Vários campos comuns:

* Server - nome do host do servidor de banco de dados
* Port - porta; no caso da porta padrão do banco de dados, você pode deixá-la em branco
* User, Password - autenticação
* Password mode
    * Save and encrypt - a senha é salva de forma criptografada, você não poderá vê-la na próxima vez
    * Save RAW - a senha é salva como está (sem criptografia), você pode consultá-la mais tarde
    * Don't save, ask for password - a senha não é salva, você precisa digitá-la ao conectar
    * Don't save, ask for login and password - nem a senha nem o login são salvos, você precisa digitar ambos ao conectar
* Is read only - a conexão será somente leitura (para mecanismos sem suporte a sessões somente leitura, você não poderá executar consultas SQL nesse caso)
* Default database - qual banco de dados estará ativo após a conexão
* Use only database *&lt;default database&gt;* - se marcado, apenas o banco de dados padrão aparece na árvore de conexões (os outros bancos de dados do servidor ficam ocultos)
* Display name - nome sob o qual a conexão aparecerá no aplicativo

## Túnel SSH
Aqui você pode configurar a conexão através de um túnel SSH. 

Campos comuns:
* Use SSH tunnel - marque para usar o túnel SSH
* Host - nome do host do servidor SSH

![DbGate - configuração de túnel SSH](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
Configure a conexão SSL.

Campos comuns:
* Use SSL - marque para usar SSL. Na maioria dos casos, isso é tudo o que você precisa configurar para usar SSL

![DbGate - configuração de conexão SSL](https://media.dbgate.io/img/connection-ssl-window-light.png)
