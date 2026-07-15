---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: pt
title: Permissões
weight: 50
---

As permissões do DbGate usam **duas dimensões**:

1. **Origem das permissões (quem as define)**
   As permissões se propagam do geral para o específico. Configurações mais específicas prevalecem sobre as mais gerais:
   * Conjuntos de permissões predefinidos
   * Funções predefinidas (*superadmin*, *usuário logado*, *anônimo*)
   * Funções personalizadas
   * Usuário individual

2. **Escopo dos objetos**
   As permissões podem ser aplicadas a **bancos de dados** e **tabelas/objetos** específicos. Consulte **[Permissões de banco de dados](#database-permissions)** e **[Permissões de tabela](#table-permissions)**.

---

## Permissões básicas

Configure as permissões globais/básicas na **árvore de permissões** no **Detalhe do usuário** ou no **Detalhe da função**.

* Uma caixa de seleção **esmaecida** significa que a permissão é **herdada** (por exemplo, de uma função ou de um conjunto de permissões predefinido), e não definida diretamente nesse usuário/função.

![Administração de funções - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## Permissões de banco de dados

Defina as permissões em nível de banco de dados na aba **Databases** (tanto no Detalhe da função quanto no Detalhe do usuário).

> **Importante:** as regras de banco de dados são aplicadas **somente se** a permissão **“All databases”** estiver desmarcada nas permissões básicas.

* Cada linha da tabela de regras concede ou nega acesso aos bancos de dados que **correspondem** aos filtros da linha.
* **A ordem das regras importa**: as regras situadas **mais abaixo** na lista **prevalecem** sobre as anteriores.

![Permissões de banco de dados - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**Colunas**

* **Connection** – a qual conexão a regra se aplica.
* **Database names** – bancos de dados a serem correspondidos (lista de nomes ou uma expressão regular).
* **Role (nível de acesso)**
  * **View** – pode ver o banco de dados, mas não suas tabelas/views/etc.
  * **Read content** – acesso somente leitura ao conteúdo do banco de dados.
  * **Write data** – pode modificar os dados das tabelas.
  * **Run script** – pode executar qualquer script SQL; pode criar/remover/alterar objetos.
  * **Deny** – bloqueia o acesso ao banco de dados.

---

## Permissões de tabela

Defina as permissões em nível de tabela/objeto na aba **Tables / Views / Objects** (no Detalhe da função e no Detalhe do usuário).

> **Importante:** as regras de tabelas/objetos são aplicadas **somente se** a permissão **“All tables/views/objects”** estiver desmarcada nas permissões básicas.

* Cada linha define o acesso às tabelas/objetos que **correspondem** aos filtros.
* **A ordem das regras importa**: as regras situadas **mais abaixo** na lista **prevalecem** sobre as anteriores.
* Por padrão, as permissões de tabela são **herdadas da permissão do banco de dados**.

**Colunas**

* **Connection** – a qual conexão a regra se aplica.
* **Database names** – bancos de dados a serem correspondidos (lista ou expressão regular).
* **Schema names** – esquemas a serem correspondidos (lista ou expressão regular).
* **Table names** – nomes de objetos a serem correspondidos (tabela/view/procedure/trigger) como lista ou expressão regular.
* **Scope** – quais tipos de objetos a regra abrange (tabelas, views, procedures, triggers, …).
* **Role (nível de acesso)**
  * **Read** – pode ler os dados da tabela.
  * **Update only** – pode atualizar linhas; **inserir** e **excluir** não são permitidos.
  * **Create, update, delete** - pode editar linhas sem restrições
  * **Run script** – pode executar um script que afete este objeto.
    > Observação: se você **não** tiver **“Run script”** no nível de **banco de dados**, não poderá usá-lo no nível de tabela.
  * **Deny** – bloqueia o acesso ao objeto.
