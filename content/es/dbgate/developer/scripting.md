---
sourceHash: 7f4d70f781d73ba668b164edc6d2ba96b55e82517290a913a90d21b02b03da18
language: es
title: Scripting
weight: 40
---

DbGate consta de varios [paquetes NPM](https://www.npmjs.com/search?q=keywords%3Adbgate), que se pueden utilizar en scripts de nodejs

Normalmente necesitarás estos paquetes:
* [dbgate-api](https://www.npmjs.com/package/dbgate-api) - implementa funciones de utilidad
* dbgate-plugin-`engine` - conjunto de plugins de conector, implementa la conexión a la base de datos y las operaciones específicas del motor de base de datos dado
* dbgate-plugin-`fileformat` - si utilizas la exportación a CSV o XML, estos proveedores de formato están implementados como plugins externos

[Documentación de la API](/es/dbgate/developer/apidoc)

## Generar un script desde DbGate
Muchas funciones de DbGate están implementadas internamente mediante la interfaz de scripting. Por eso, cuando utilizas alguna operación similar a una exportación, hay en algún lugar un botón "Generate Shell script", que genera un script de nodejs por ti.

Si quieres usar un script de nodejs para exportar, puedes seguir estos pasos:
* Haz clic derecho sobre la tabla y elige "Export/Export advanced"
* Configura tu exportación
* Elige "Generate script" en la barra de herramientas inferior. Ahora puedes editar el script JS y ejecutarlo dentro de DbGate
* Si eliges "Copy nodejs script" en la barra de herramientas inferior, puedes guardarlo en un archivo js y ejecutarlo con [nodejs](https://nodejs.org/) instalado en tu ordenador


## Ejemplo 1 - exportar una tabla a CSV
Este es un ejemplo sencillo, utilizamos [tableReader](https://dbgate.org/docs/apidoc.html#tableReader) del paquete `dbgateApi` y el writer de `dbgate-plugin-csv`. También se requiere `dbgate-plugin-mysql`, porque utilizamos el parámetro engine `mysql@dbgate-plugin-mysql`
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