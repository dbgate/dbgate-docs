---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: pt
title: Conectando-se a Endpoints de API
weight: 10
---

O DbGate Central se conecta a três famílias de endpoints de API, usando a mesma caixa de diálogo Nova Conexão para todas elas.

## Tipos de endpoint suportados

* **GraphQL** - faça a introspecção do schema, navegue pelos tipos e execute consultas em qualquer API GraphQL.
* **oData** - trabalhe com serviços oData V4 como se fossem tabelas comuns.
* **Shopify** - conecte-se à sua loja por meio da API Shopify Admin e explore produtos, pedidos, clientes, metafields e muito mais.

## Criando uma conexão

Abra a caixa de diálogo **Nova Conexão**, escolha o tipo de conexão, informe a URL do serviço e selecione como autenticar:

* **Nenhuma** - para endpoints abertos e públicos.
* **Basic** - nome de usuário e senha.
* **Bearer token** - cole um token de acesso.
* **Chave de API** - envie uma chave em um cabeçalho ou parâmetro de consulta.

As conexões são salvas no seu workspace, portanto estarão lá na próxima vez que você entrar, em qualquer dispositivo, sem nada para configurar localmente.

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
