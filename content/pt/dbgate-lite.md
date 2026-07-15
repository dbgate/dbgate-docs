---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: pt
title: DbGate Lite
weight: 30
---

O [DbGate Lite](https://lite.dbgate.io/) é uma ferramenta gratuita, executada no navegador, para trabalhar com dados - sem instalação e sem login. Ele é construído sobre a mesma grade, filtragem e mecanismo de consultas do [DbGate Central](../dbgate-central/), então navegar, filtrar e editar funcionam da mesma forma em ambos.

## Aprenda e ensine SQL

O DbGate Lite executa **SQLite e DuckDB** inteiramente no seu navegador, usando WebAssembly:

* Escreva e execute consultas SQL em um banco de dados de exemplo na conhecida grade do DbGate.
* Visualize como as tabelas se relacionam com diagramas ER.
* Sem instalação, sem login - abra o site e comece a trabalhar.

## Trabalho pontual com arquivos de dados

Abra um arquivo no DbGate Lite e trate-o como um banco de dados:

* **Importe** arquivos CSV, JSON e Excel e consulte-os ou edite-os com SQL.
* Limpe e reorganize os dados e depois **exporte** o resultado de volta para CSV, JSON ou Excel.

## Compartilhando um banco de dados ou consulta com um link

Abrir o DbGate Lite com determinados parâmetros de hash na URL inicializa automaticamente um banco de dados temporário:

* `initdbtype` - tipo de banco de dados, `sqlite` ou `duckdb`
* `initdbscript` - script SQL usado para criar e preencher o banco de dados temporário
* `initquery` (opcional) - consulta SQL aberta em uma nova aba de Query

Qualquer pessoa que abrir o link obtém o mesmo banco de dados de exemplo e a mesma consulta com um clique - útil para tutoriais, relatórios de bugs e ensino.

## Publicando uma visualização somente leitura

Além de compartilhar um link editável, você pode **publicar** uma visualização somente leitura de um arquivo CSV/JSON ou de um relatório de BI usando o botão Publish na barra de ferramentas. Isso abre uma página independente - apenas os dados e um alternador claro/escuro, sem barra lateral nem editor - que qualquer pessoa com o link pode visualizar sem uma conta.

## Escolhendo entre Lite, Central, Premium e Team Premium

O DbGate Lite é ideal para aprender e para tarefas pontuais. Para trabalho contínuo e profissional, um produto dedicado é mais adequado:

* **DbGate Lite** - gratuito, no navegador. Ideal para aprender SQL e para arquivos de dados pontuais.
* **[DbGate Central](../dbgate-central/)** - produto hospedado para trabalhar com APIs: conecte-se a endpoints GraphQL, oData e Shopify ao vivo, mantenha conexões e relatórios em um workspace e compartilhe-os com sua equipe.
* **[DbGate Premium](/pt/dbgate/getting-started/installation/)** - uma edição do [DbGate](/pt/dbgate/): o aplicativo desktop completo para trabalhar com bancos de dados, conecte-se a servidores SQL e NoSQL com o conjunto completo de ferramentas profissionais.
* **[DbGate Team Premium](/pt/dbgate/getting-started/installation/docker-tp/)** - outra edição do [DbGate](/pt/dbgate/), para equipes: uma interface web compartilhada que roda on-premise, para que toda a sua equipe trabalhe com bancos de dados a partir do navegador na sua própria infraestrutura.
