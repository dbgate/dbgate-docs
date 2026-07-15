---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: pt
title: Exportação e importação
weight: 20
---

O DbGate possui um sistema flexível de exportação/importação, permitindo tanto exportações simples com um clique quanto configurações personalizadas complexas.

## Exportação simples com um clique

Se você não precisa de nenhuma configuração e só quer exportar dados para um arquivo, pode usar a exportação simples. Há várias maneiras de acionar a exportação simples:
- Menu de contexto de tabela/visão/coleção, Export
- Dados da tabela, menu de contexto "Export" ou botão {{<mdi "export" >}}. Os filtros também são aplicados aos dados exportados
- Resultado da consulta, menu de contexto "Export" ou botão {{<mdi "export" >}}

No aplicativo desktop, você pode salvar o arquivo exportado diretamente.

No aplicativo web, o arquivo exportado é oferecido para download.

## Exportação/importação avançada
Se você precisa configurar mais detalhes ou exportar várias tabelas de uma só vez, é necessário usar a "Exportação avançada".  
A mesma ferramenta de configuração é usada para importação, apenas com a configuração de origem e destino invertida.

A exportação/importação avançada pode ser acionada a partir de:
- os mesmos lugares que a exportação simples, apenas escolhendo "Export advanced..." em vez do formato de arquivo
- menu de contexto do banco de dados, escolha "Export" ou "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} Configuração da origem
* Tipo de armazenamento - escolha a origem dos dados
  * Database - então você configura a "Exportação"
    * Selecione várias tabelas de origem
  * File (JSON, CSV, DBF...) - então você configura a "Importação"
    * Abra ou arraste e solte o arquivo de origem
  * Query - na maioria dos casos você não precisará disso, mas pode digitar a consulta diretamente aqui. Essa opção é usada internamente quando você está exportando, por exemplo, dados filtrados de uma tabela.
  * Archive - importe/exporte dados de um [arquivo de dados](advanced-data-tools/archives)

### {{<mdi "export" >}} Configuração do destino
* Tipo de armazenamento - o mesmo que na configuração da origem, mas com significado oposto
  * Database - você configura a "Importação"
  * File (JSON, CSV, DBF...) - você configura a "Exportação"

### {{< mdi "table-multiple" >}} Mapear tabelas/arquivos de origem
Você pode mapear como os arquivos/tabelas de entrada são transformados na saída

### Botões de ação
  * {{< mdi "play" >}} Run - executa o job de importação/exportação definido
  * {{< mdi "flash" >}} Generate script - cria um código JavaScript que executa o job definido. Você pode executá-lo no console shell do DbGate ou exportá-lo para um arquivo e executá-lo na linha de comando com o nodejs
  * {{< mdi "content-save" >}} Save - salva o job para uso posterior

## Scripts de importação / exportação
Todos os jobs de importação/exportação no DbGate são primeiro transpilados em scripts. Segue um exemplo de exportação de uma tabela SQLite para CSV.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

Você também pode executar esse script sem o DbGate. Use o menu de contexto no editor de scripts, "Copy nodejs script". Isso copiará o seguinte script:

```js

const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginSqlite = require('dbgate-plugin-sqlite');
const dbgatePluginCsv = require('dbgate-plugin-csv');
dbgateApi.registerPlugins(dbgatePluginSqlite,dbgatePluginCsv);

require=null;
async function run() {

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);


await dbgateApi.finalizer.run();
console.log('Finished job script');
}
dbgateApi.runScript(run);
```

Depois de instalar as dependências usadas na pasta do script (todos os pacotes usados na função require()):

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

Você pode executar esse script com o comando:

```sh
node myExportScript.js
```
