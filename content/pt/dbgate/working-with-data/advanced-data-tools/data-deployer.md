---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: pt
title: Implantador de dados
weight: 2
---

Com o implantador de dados, você pode comparar e sincronizar visualmente seus dados em **pastas de arquivo** com o **banco de dados real**
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Executar o implantador de dados
Você pode executar o implantador de dados a partir do menu de contexto do banco de dados ou do menu de contexto da pasta de arquivo. Ao executá-lo a partir do banco de dados, será solicitado que você escolha o arquivo. Ao executá-lo a partir do arquivo, o implantador de dados será iniciado com o banco de dados atual.

## Configurações
- Servidor de banco de dados, banco de dados - escolha o banco de dados com o qual trabalhar
- Arquivo de dados - escolha a pasta com os dados que serão usados para comparação e sincronização
### Relacionadas à tabela
- Chave (colunas de correspondência) - escolha as colunas que serão usadas para corresponder as linhas entre o banco de dados e o arquivo
### Configurações do replicador
As configurações abaixo ("tabela" - implantação e configurações globais de implantação de dados) são específicas do replicador e estão descritas no tópico [Replicador de dados](data-replicator)

## Copiar diferenças de dados
O implantador de dados mostra as diferenças entre os dados no arquivo e no banco de dados. Se você selecionar algumas células com diferença, poderá gravar essas diferenças no arquivo ou no banco de dados. Quando essas células estão selecionadas, aparecem no canto inferior direito botões que permitem a sincronização:
- Gravar x linhas, y colunas no arquivo - copia as células selecionadas do banco de dados para o arquivo.
- Gravar x linhas, y colunas no banco de dados - copia as células selecionadas do arquivo para o banco de dados. Primeiro é exibida uma caixa de diálogo de confirmação com o SQL de alteração.

## Ações do replicador de dados
- Implantar no BD - esta ação implanta as alterações no banco de dados com as configurações definidas
- Gerar shell - esta ação cria um arquivo JavaScript que executará a implantação. Esse arquivo pode ser executado a partir da linha de comando
- Gerar SQL - cria o SQL que implanta as alterações do arquivo no banco de dados

Mais sobre essas ações no tópico [Replicador de dados](data-replicator)
