---
sourceHash: f40d2449d850b2f3fb0bbefb91685fbbc63c23ad73bd0cf5febb08e0f4a7eefa
language: es
title: Exportar e importar
weight: 20
---

DbGate tiene un sistema de exportación/importación flexible que permite tanto exportaciones sencillas con un solo clic como configuraciones personalizadas complejas.

## Exportación sencilla con un solo clic

Si no necesitas ninguna configuración y solo quieres exportar datos a un archivo, puedes usar la exportación sencilla. Hay varias formas de invocar la exportación sencilla:
- Menú contextual de tabla/vista/colección, Export
- Datos de la tabla, menú contextual "Export" o botón {{<mdi "export" >}}. Los filtros también se aplican a los datos exportados
- Resultado de la consulta, menú contextual "Export" o botón {{<mdi "export" >}}

En la aplicación de escritorio, puedes guardar directamente el archivo exportado.

En la aplicación web, el archivo exportado se ofrece para su descarga.

## Exportación/importación avanzada
Si necesitas configurar más detalles o exportar varias tablas de una sola vez, debes usar la "Exportación avanzada".  
La misma herramienta de configuración se usa para importar, solo que con la configuración de origen y destino intercambiada.

La exportación/importación avanzada se puede invocar desde:
- los mismos lugares que la exportación sencilla, solo que en lugar del formato de archivo elige "Export advanced..."
- el menú contextual de la base de datos, elige "Export" o "Import"


![screenshot](https://media.dbgate.io/img/configure-export-csv-light.png)

### {{<mdi "import" >}} Configuración del origen
* Storage type - elige el origen de los datos
  * Database - entonces configuras la "Exportación"
    * Selecciona varias tablas de origen
  * File (JSON, CSV, DBF...) - entonces configuras la "Importación"
    * Abre o arrastra y suelta el archivo de origen
  * Query - en la mayoría de los casos no lo necesitarás, pero puedes escribir la consulta directamente aquí. Esta opción se usa internamente cuando exportas, por ejemplo, datos filtrados de una tabla.
  * Archive - importa/exporta datos desde un [archivo de datos](advanced-data-tools/archives)

### {{<mdi "export" >}} Configuración del destino
* Storage type - igual que en la configuración del origen, pero con el significado opuesto
  * Database - configuras la "Importación"
  * File (JSON, CSV, DBF...) - configuras la "Exportación"

### {{< mdi "table-multiple" >}} Mapear tablas/archivos de origen
Puedes mapear cómo se transforman los archivos/tablas de entrada en la salida

### Botones de acción
  * {{< mdi "play" >}} Run - ejecuta la tarea de importación/exportación definida
  * {{< mdi "flash" >}} Generate script - crea código JavaScript que ejecuta la tarea definida. Puedes ejecutarlo en la consola shell de DbGate, o puedes exportarlo a un archivo y ejecutarlo desde la línea de comandos con nodejs
  * {{< mdi "content-save" >}} Save - guarda la tarea para más tarde

## Scripts de importación/exportación
Todas las tareas de importación/exportación en DbGate se transpilan primero a scripts. A continuación, un ejemplo de exportación de una tabla SQLite a CSV.

```js
// @require dbgate-plugin-sqlite
// @require dbgate-plugin-csv

const var1 = await dbgateApi.tableReader({
    "connection":{"engine":"sqlite@dbgate-plugin-sqlite","databaseFile":"/home/jena/test/chinook/Chinook.db"}
});
const var2 = await dbgatePluginCsv.shellApi.writer({"fileName":"Album.csv"});
await dbgateApi.copyStream(var1, var2);
```

También puedes ejecutar este script sin DbGate. Usa el menú contextual del editor de scripts "Copy nodejs script". Copiará el siguiente script:

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

Después de instalar las dependencias utilizadas en la carpeta con el script (todos los paquetes usados en la función require()):

```sh
yarn add dbgate-api
yarn add dbgate-plugin-sqlite
yarn add dbgate-plugin-csv
```

Puedes ejecutar este script con el comando:

```sh
node myExportScript.js
```
