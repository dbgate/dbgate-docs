---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: pt
title: Scripts
weight: 40
---

O DbGate é composto por diversos [pacotes NPM](https://www.npmjs.com/search?q=keywords%3Adbgate), que podem ser usados em scripts nodejs

Normalmente você precisará destes pacotes:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - implementa funções utilitárias
* dbgate-plugin-`engine` - conjunto de plugins de conector, implementa a conexão com o banco de dados e as operações específicas de um determinado mecanismo de banco de dados
* dbgate-plugin-`fileformat` - se você usar exportação para CSV ou XML, esses provedores de formato são implementados como plugins externos

[Documentação da API](/pt/dbgate/developer/apidoc)

## Gerando script a partir do DbGate
Muitos recursos do DbGate são implementados internamente com a interface de scripts. Assim, quando você usa alguma operação do tipo exportação, há em algum lugar um botão "Generate Shell script", que gera um script nodejs para você.

Se você quiser usar um script nodejs para exportar, poderá seguir estes passos:
* Clique com o botão direito na tabela e escolha "Export/Export advanced"
* Configure sua exportação
* Escolha "Generate script" na barra de ferramentas inferior. Agora você pode editar o script JS e executá-lo dentro do DbGate
* Se você escolher "Copy nodejs script" na barra de ferramentas inferior, poderá salvá-lo em um arquivo js e executá-lo com o [nodejs](https://nodejs.org/) instalado no seu computador


## Exemplo 1 - exportar tabela para CSV
Este é um exemplo simples, estamos usando o [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) do pacote `dbgateApi` e o writer do `dbgate-plugin-csv`. Também é necessário o `dbgate-plugin-mysql`, porque estamos usando o parâmetro engine `mysql@dbgate-plugin-mysql`
```js
const dbgateApi = require('dbgate-api');
const dbgatePluginMysql = require("dbgate-plugin-mysql");
const dbgatePluginCsv = require("dbgate-plugin-csv");

dbgateApi.registerPlugins(dbgatePluginMysql);

async function run() {
  const reader = await dbgateApi.tableReader({
    connection: { server: 'localhost', engine: 'mysql@dbgate-plugin-mysql', user: 'root', password: 'xxxx', database: 'Chinook' },
    pureName: 'Customer',
  });
  const writer = await dbgatePluginCsv.shellApi.writer({ fileName: 'Customer.csv' });
  await dbgateApi.copyStream(reader, writer);

  console.log('Finished job script');
}
dbgateApi.runScript(run);
```
