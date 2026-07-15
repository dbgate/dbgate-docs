---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: es
title: Despliegue de base de datos
weight: 10
---

*La funcionalidad de despliegue cambiará significativamente en la próxima versión, esta documentación está relacionada con la última versión BETA*

DbGate ofrece un mecanismo para el despliegue automático de bases de datos. Mientras que la forma tradicional de lograr esto utiliza scripts SQL de migración, DbGate usa por defecto una forma diferente (los scripts de migración también están soportados).
Defines el modelo de BD con archivos YAML que describen la estructura de las tablas y los datos de listas, y archivos SQL que describen vistas, procedimientos almacenados y funciones. Este modelo se despliega en la base de datos, comparando la estructura actual con la estructura del modelo, creando las columnas y tablas que faltan y actualizando las definiciones de vistas y procedimientos. **No se realizan acciones destructivas** (que podrían provocar pérdida de datos), por lo que cuando eliminas una columna o tabla del modelo, esta permanece en la base de datos. Si renombras una columna en el modelo, se crea una nueva columna con el nuevo nombre y la columna antigua permanece en la base de datos.

El despliegue se puede invocar desde la línea de comandos (usando scripts de node), o desde la interfaz gráfica de DbGate. También puedes usar la función de comparación de BD para comparar visualmente las diferencias entre el modelo y la base de datos real.

## Formato yaml de tabla

```yaml
name: Album # table name 
columns:
  - name: AlbumId # column name 
    type: int # data type. is used directly in target SQL engine  
    autoIncrement: true # column is autoincrement 
    notNull: true # column is not nullable (default: is nullable) 
  - name: Title
    type: nvarchar(150)
    notNull: true
  - name: ArtistId
    type: int
    references: Artist # name of table. Is used for creating foreign key 
  - name: isDeleted
    type: bit
    notNull: true
    default: 0 # default value 
  - name: created
    type: timestamp
    default: current_timestamp
primaryKey:
  - AlbumId # list of primary key column names 
indexes:
  - name: UQ_AlbumTitleArtistId # index name 
    unique: true # whether index is unique. default=false 
    columns: # list of index columns 
      - Title
      - ArtistId
data: # static data (only for list tables) 
  - AlbumId: -1 # values for all columns, which should be filled 
    Title: Predefined static album
```

- Los nombres se definen sin el nombre del esquema, un modelo describe un esquema
- Los valores por defecto se definen como expresiones SQL, así que si quieres definir una cadena de texto, debes usar 'comillas simples'
- Puedes definir datos estáticos para una tabla

### Uso de scripts de migración
Puedes combinar scripts de migración más tradicionales con la gestión de despliegue específica de DbGate, algunos objetos más específicos se pueden crear con scripts de migración.
Los tipos de script se determinan por la extensión del archivo, la disposición de los directorios es elección del usuario, DbGate no se ve afectado por esto.

Se admiten las siguientes extensiones de script:
- `*.predeploy.sql` - los scripts se ejecutan antes de cada proceso de despliegue
- `*.install.sql` - los scripts se ejecutan solo si son diferentes del despliegue anterior
- `*.uninstall.sql` - este script está emparejado con el archivo `.install.sql`, se ejecuta antes de que se ejecute la nueva versión del archivo `*.install.sql`
- `*.once.sql` - los scripts se ejecutan solo una vez
- `*.postdeploy.sql` - los scripts se ejecutan antes de cada proceso de despliegue

DbGate utiliza la tabla `dbgate_deploy_journal` para el seguimiento de los scripts de despliegue desplegados en la base de datos. Esta tabla se crea automáticamente cuando despliegas cualquier proyecto con al menos un script de migración.


### Uso en la interfaz gráfica de DbGate

- En conexiones, en el menú contextual de la base de datos, elige "Export DB model" (solo Premium). El modelo de BD se guarda en un directorio o en un archivo. Si planeas usar la funcionalidad de despliegue, elige los destinos Data archive o Folder (YAML + SQL).
- Abre el widget de archivos, deberías ver el modelo descargado
- En el menú contextual del modelo, puedes realizar algunas operaciones con el modelo:
    - Generate deploy DB SQL - compara la base de datos actual (puedes verla en la barra de estado) y genera un script SQL, que despliega los cambios del modelo en la base de datos actual
    - Shell: Deploy DB - genera un shell de JavaScript, que se puede usar para desplegar la BD
    - Compare with {current database} - compara gráficamente la base de datos actual con el modelo (solo Premium)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### Uso desde la línea de comandos
Copia el siguiente script en el archivo deploy.js y actualiza la configuración de la base de datos. También deberías cambiar modelFolder, según la ubicación de la carpeta de tu modelo.
Ejecutar este script requiere tener [NodeJs](https://nodejs.org/) instalado en tu ordenador.

```js
const path = require('path');
const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginPostgres = require('dbgate-plugin-postgres');
dbgateApi.registerPlugins(dbgatePluginPostgres);

async function run() {
	await dbgateApi.deployDb({
		connection: {
			server: process.env.DB_SERVER || 'localhost',
			engine: 'postgres@dbgate-plugin-postgres',
			password: process.env.DB_PASSWORD || 'test',
			user: process.env.DB_USER || 'postgres',
			port: process.env.DB_PORT || 5432,
			database: process.env.DB_NAME || 'my_database',
		},
		modelFolder: path.join(__dirname, 'database'),
	});
	await dbgateApi.finalizer.run();
	console.log('Finished job script');
}
dbgateApi.runScript(run);
```

Luego, instala los módulos requeridos, ejecutando los comandos en el directorio con deploy.js:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

Ejecuta el despliegue de la base de datos con el comando:
```sh
node deploy.js
```

Este script es para PostgreSQL, otros motores de bases de datos requieren cambios en el driver.

Este script también se puede generar automáticamente desde la interfaz gráfica de DbGate, usa el menú contextual "Shell: Deploy DB" desde la carpeta de archivos, luego "Copy nodejs script" en el script generado copiará un script válido. Todos los paquetes que se usan en el comando require deben instalarse con npm install.
