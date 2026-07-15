---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: pt
title: Conexões de API
weight: 10
---

O DbGate oferece suporte a conexões com APIs REST, serviços GraphQL e endpoints OData. Essas conexões de API usam os mesmos padrões de interface das conexões de banco de dados, permitindo que você trabalhe com APIs e bancos de dados em um ambiente unificado.

O suporte a conexões de API está disponível no DbGate Premium.

> Procurando navegar por APIs sem o aplicativo desktop? O [DbGate Central](/pt/dbgate-central/connecting-to-api-endpoints/) é uma implementação separada e hospedada de conexões GraphQL/oData/Shopify, reimplementada desde o início para o navegador.

## GraphQL

As conexões GraphQL permitem que você interaja com APIs GraphQL. O DbGate fornece recursos de introspecção de esquema e execução de consultas.

### Criando uma conexão GraphQL

Para criar uma conexão GraphQL, use a caixa de diálogo New Connection e selecione GraphQL como o tipo de conexão. Informe a URL do endpoint GraphQL e configure a autenticação, se necessário.

### Introspecção de esquema

O DbGate descobre automaticamente o esquema GraphQL, incluindo os tipos, consultas e mutações disponíveis, além de seus argumentos. O navegador de esquema exibe o sistema de tipos e permite que você explore a estrutura da API.

### Editor de consultas

O editor de consultas GraphQL permite que você escreva consultas e mutações. Você pode usar o explorador GraphQL para construir consultas selecionando campos e argumentos do esquema.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Variáveis

As consultas GraphQL oferecem suporte a variáveis. Defina as variáveis no painel de variáveis e faça referência a elas em suas consultas usando a sintaxe padrão de variáveis do GraphQL. As variáveis podem ser editadas em um formulário ou como JSON bruto.

### Visualizador de respostas

Os resultados das consultas são exibidos em um visualizador JSON formatado, com uma estrutura em árvore expansível. Se forem detectados arrays na resposta, a visualização tabular é exibida automaticamente. Você pode voltar para a visualização JSON bruta, se necessário.

## OpenAPI (Swagger)

As conexões OpenAPI oferecem suporte a APIs REST que fornecem especificações OpenAPI (versões 2.0 e 3.0).

### Criando uma conexão OpenAPI

Crie uma nova conexão e selecione OpenAPI como o tipo de conexão. Informe a URL do arquivo de especificação OpenAPI (normalmente swagger.json ou openapi.json). O DbGate irá analisar a especificação e disponibilizar todos os endpoints documentados.

### Navegador de documentação da API

O navegador OpenAPI exibe todos os endpoints disponíveis, organizados por tags e caminhos. Para cada endpoint, você pode visualizar:
- Método HTTP (GET, POST, PUT, DELETE, PATCH)
- Parâmetros (path, query, header, body)
- Esquemas do corpo da requisição
- Descrições da documentação

### Execução de requisições

Selecione um endpoint para abrir o construtor de requisições. Preencha os parâmetros, cabeçalhos e o corpo da requisição obrigatórios. Execute a requisição para enviá-la ao servidor da API.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Inspeção de respostas

Visualize o código de status, os cabeçalhos e o corpo da resposta. As respostas JSON são formatadas e podem ser exibidas tanto na visualização em árvore quanto na tabular. Respostas que não são JSON são exibidas como texto.

## OData

As conexões OData oferecem suporte à consulta de serviços OData usando a sintaxe de consulta padrão do OData.

### Criando uma conexão OData

Crie uma nova conexão com OData como o tipo de conexão. Informe a URL raiz do serviço OData. O DbGate irá recuperar o documento de metadados do serviço.

### Exploração de metadados

O navegador de metadados mostra os conjuntos de entidades, tipos de entidade, propriedades e relacionamentos disponíveis definidos nos metadados do serviço.

### Execução de consultas

As consultas OData oferecem suporte às opções de consulta padrão do OData:
- `$filter` - filtra entidades por valores de propriedades
- `$select` - especifica quais propriedades retornar
- `$expand` - inclui entidades relacionadas
- `$orderby` - ordena os resultados
- `$top` e `$skip` - paginação
- `$count` - inclui a contagem de resultados

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

Os resultados são exibidos em formato tabular, de forma semelhante aos resultados de consultas de banco de dados.

## Autenticação

Todos os tipos de conexão de API oferecem suporte a vários métodos de autenticação:

- **API Key** - especifique o nome e o valor da chave, enviada como cabeçalho ou parâmetro de consulta
- **Bearer Token** - tokens OAuth ou JWT enviados no cabeçalho Authorization
- **Basic Authentication** - nome de usuário e senha usando HTTP Basic Auth
- **No Authentication** - para APIs públicas

Configure a autenticação nas propriedades da conexão.

## Exportação de dados

Os dados de resposta da API podem ser exportados para vários formatos usando a funcionalidade padrão de exportação do DbGate:
- JSON
- CSV
- Excel
- Comandos SQL INSERT
- XML

Use a opção "Export" do menu de contexto padrão no navegador de dados tabulares.

## Trabalhando com várias APIs

Você pode criar conexões com várias APIs e bancos de dados. Abra várias abas de requisição para trabalhar com diferentes endpoints simultaneamente.

O estado das abas é preservado após fechar e reabrir o aplicativo; você pode reabrir uma requisição a partir do histórico de abas fechadas.
