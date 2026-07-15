---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: es
title: Variables de entorno
weight: 20
---

La configuración mediante variables de entorno se puede utilizar en contenedores docker, así como al usar el paquete npm. El paquete NPM admite archivos .env.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - paquete NPM para la edición Community
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - paquete NPM para la edición Premium
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - imagen Docker para la edición Community
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - imagen Docker para la edición Premium

## Edición Premium frente a Team Community
La edición Community (FOSS) utiliza únicamente la configuración de las variables de entorno que se enumeran a continuación. La edición Team Premium utiliza almacenamiento en base de datos para la configuración con la [interfaz de administración](/es/features/administration); solo unos pocos ajustes básicos se configuran con variables de entorno.

## Configuración de la edición Team Premium
Estas variables están disponibles únicamente en la edición Team Premium.
  * STORAGE_SERVER - servidor de base de datos (nombre de host) para la base de datos de almacenamiento
  * STORAGE_USER - usuario de la base de datos
  * STORAGE_PASSWORD - contraseña de la base de datos
  * STORAGE_PORT - puerto de la base de datos (opcional. Si se omite, se utiliza el puerto predeterminado del motor de base de datos seleccionado)
  * STORAGE_DATABASE - nombre de la base de datos de almacenamiento
  * STORAGE_SCHEMA - esquema de la base de datos de almacenamiento (opcional, p. ej. para PostgreSQL (normalmente public) o MS SQL (normalmente dbo))
  * STORAGE_ENGINE - motor utilizado para la base de datos de almacenamiento. Actualmente, MySQL, PostgreSQL, SQL Server y Oracle. Utilice uno de los siguientes valores:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - contraseña del administrador. La administración está disponible en la URL https://dbgate_url/admin.html. Si la contraseña no está definida y STORAGE_DATABASE sí lo está, DbGate solicitará la contraseña de administrador al principio.
  * DBGATE_LICENSE - clave de licencia para DbGate. Póngase en contacto con sales@dbgate.eu para obtener una licencia de prueba. Si no está definida, DbGate Premium solicitará la licencia al principio. DbGate Community no requiere ninguna licencia.
  
### Parámetros adicionales de conexión del almacenamiento
  * STORAGE_SOCKET_PATH - ruta del socket para la conexión de almacenamiento
  * STORAGE_DATABASE_URL - URL de base de datos para la conexión de almacenamiento
  * STORAGE_AUTH_TYPE - tipo de autenticación para la conexión de almacenamiento. Los valores son los mismos que para la variable AUTH_TYPE_xxx
  * STORAGE_USE_SSL - establezca el valor 1 o true cuando se deba utilizar SSL
  * STORAGE_KEY_FILE - ruta al archivo de clave
  * STORAGE_KEY_FILE_PASSWORD - frase de contraseña del archivo de clave
  * STORAGE_SSL_CA_FILE - ruta al archivo de certificado CA
  * STORAGE_SSL_CERT_FILE - ruta al archivo de certificado
  * STORAGE_SSL_CERT_FILE_PASSWORD - contraseña del archivo de clave del certificado
  * STORAGE_SSL_KEY_FILE - ruta al archivo de clave
  * STORAGE_SSL_KEY_FILE_PASSWORD - frase de contraseña del archivo de clave
  * STORAGE_SSL_REJECT_UNAUTHORIZED - establezca el valor 1 o true si se deben rechazar las conexiones no autorizadas
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - establezca el valor 1 o true para configurar la opción trustServerCertificate de MSSQL

Las siguientes variables están disponibles tanto en la edición Community como en la Premium. Sin embargo, en la edición Premium, la forma preferida es utilizar la base de datos de almacenamiento y la interfaz de administración para la configuración.

## Configuración web y de permisos
* WEB_ROOT - si necesita ejecutar DbGate en un subdirectorio virtual (p. ej. para el valor /dbadmin , dbgate será accesible en localhost:3000/dbadmin )
* LOGIN , PASSWORD - credenciales para acceder a la aplicación web
* PERMISSIONS - lista de permisos separados por comas. Consulte también la lista de permisos más abajo
* SHELL_CONNECTION - si es true o 1, las conexiones se pueden definir en scripts de shell. De lo contrario, solo se permiten conexiones preconfiguradas. De forma predeterminada, esto no está permitido por razones de seguridad. Tenga en cuenta que, cuando se permite, las contraseñas cifradas se envían al frontend.
* SHELL_SCRIPTING - si es true o 1, se permiten scripts de shell personalizados en JavaScript. De forma predeterminada, esto no está permitido por razones de seguridad.
* LOGIN_PASSWORD_[login] - contraseña para el login especificado
* LOGIN_PERMISSIONS_[login] - lista de permisos separados por comas para el login indicado. Consulte también la lista de permisos más abajo
* TOKEN_LIFETIME - tiempo de vida del token de acceso. Transcurrido este tiempo, el usuario conectado será redirigido a la página de inicio de sesión. El valor predeterminado es 1d (significa 1 día). Son posibles valores como 3h (3 horas), 10m (10 minutos), 2d (2 días)
* SINGLE_CONNECTION - ID de conexión. Si se define, solo esta conexión estará disponible (debe utilizarse con SINGLE_DATABASE)
* SINGLE_DATABASE - nombre de base de datos, solo esta base de datos estará disponible. (debe utilizarse con SINGLE_CONNECTION)
* BASIC_AUTH - si es true o 1 , se utiliza autenticación básica tanto para la web como para la API. De lo contrario, se utiliza el formulario de inicio de sesión y la autenticación de la API basada en tokens JWT. La autenticación básica no se puede utilizar con la autenticación OAuth.
* SKIP_ALL_AUTH - si es true o 1, se omite toda la autenticación
* ALLOW_DBGATE_PRIVATE_CLOUD - de forma predeterminada, DbGate Cloud está deshabilitado en la versión web. Con esta variable puede habilitarlo
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - en la versión web, redirige al inicio de sesión de DbGate Cloud en lugar de abrir una nueva ventana
* LANGUAGE - idioma de la interfaz, p. ej. en, cs, de, fr, etc. Consulte la tabla de configuración de idiomas más abajo. Establezca "auto" para usar el idioma del navegador

## Configuración de idioma
| Idioma | Valor |
|----------|-------|
| Inglés | en |
| Alemán | de |
| Español | es |
| Francés | fr |
| Italiano | it |
| Portugués (Brasil) | pt |
| Japonés | ja |
| Chino - simplificado | zh |
| Checo | cs |
| Eslovaco | sk |


## Configuración del registro (logging)
* LOG_LEVEL - se registrarán todos los mensajes con este nivel de registro o superior. Uno de los valores trace, debug, info, warn, error, fatal. El valor predeterminado es info
* FILE_LOG_LEVEL - nivel de registro para el registro en archivo. Para el registro en archivo, tiene mayor prioridad que LOG_LEVEL
* CONSOLE_LOG_LEVEL - nivel de registro para el registro en archivo. Para el registro en consola, tiene mayor prioridad que LOG_LEVEL

## Configuración de OAuth (solo versión web)
* OAUTH_AUTH - endpoint de autenticación del protocolo OAuth
* OAUTH_TOKEN - endpoint de token del protocolo OAuth
* OAUTH_LOGOUT - URL de cierre de sesión del proveedor OAuth. El usuario será redirigido a esta URL cuando solicite cerrar la sesión
* OAUTH_CLIENT_ID - ID de cliente
* OAUTH_CLIENT_SECRET - secreto de cliente
* OAUTH_LOGIN_FIELD - nombre del campo del payload que contiene el nombre de inicio de sesión. Para conocer los campos disponibles, puede inspeccionar el registro de dbgate; el payload enviado por el proveedor OAuth se registra en la consola. Este nombre de inicio de sesión se utiliza, p. ej., para configurar permisos. No es necesariamente el login introducido en OAuth. Si no se especifica, todos los usuarios del proveedor OAuth tendrán el mismo nombre de inicio de sesión.
* OAUTH_ALLOWED_LOGINS - nombres de inicio de sesión separados por comas a los que se permitirá iniciar sesión. Si no se especifica, todos los logins podrán utilizar la aplicación DbGate.
* OAUTH_SCOPE - scope que se envía a los endpoints de autorización y de token de OAuth
* OAUTH_GROUP_FIELD - campo del payload de OAuth que indica el grupo
* OAUTH_ALLOWED_GROUPS - nombres de grupos permitidos separados por comas

## Configuración de Active Directory/LDAP (solo versión web)
* AD_URL - URL del proveedor LDAP (p. ej. ldap://domain.com)
* AD_BASEDN - p. ej. dc=domain,dc=com
* AD_USERNAME - nombre de usuario de Active Directory
* AD_PASSWORD - contraseña de Active Directory
* AD_ALLOWED_LOGINS - nombres de inicio de sesión separados por comas a los que se permitirá iniciar sesión. Si no se especifica, todos los logins podrán utilizar la aplicación DbGate.

## Configuración del cliente de Oracle  
* ORACLE_INSTANT_CLIENT - ruta al [Oracle instant client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html)

## Configuración de conexiones
Puede configurar la lista de conexiones con variables de entorno; en tal caso, los comandos "Add connection" y "Edit connection" no estarán disponibles.

* CONNECTIONS - lista de nombres de conexiones preconfiguradas, separados por comas. En las siguientes opciones, [connection id] es el ID de esta lista
* LABEL_[connection id] - etiqueta (nombre visible) de la conexión. 
* SERVER_[connection id] - servidor (nombre de host) de la conexión.
* USER_[connection id] - nombre de usuario para la conexión a la BD.
* PASSWORD_[connection id] - contraseña para la conexión a la BD.
* PASSWORD_MODE_[connection id] - determina si la contraseña y el nombre de usuario se almacenan o deben ser introducidos por el usuario. Uno de los siguientes valores:
  * askPassword - DbGate solicita la contraseña al conectar
  * askUser - DbGate solicita el nombre de usuario y la contraseña
* PORT_[connection id] - puerto para la conexión a la BD.
* FILE_[connection id] - ruta del archivo de base de datos (para SQLite).
* URL_[connection id] - URL de la base de datos (funciona para MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle).
* SERVICE_NAME_[connection id] - nombre de servicio de Oracle.
* DATABASE_[connection id] - nombre de la base de datos predeterminada.
* READONLY_[connection id] - conectar en modo de solo lectura
* ENGINE_[connection id] - motor de la conexión (**obligatorio**, nombre del motor con el plugin), uno de:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - establezca el valor 1 o true cuando se deba utilizar un túnel SSH
* SSH_HOST_[connection id] - nombre de host SSH
* SSH_PORT_[connection id] - número de puerto SSH
* SSH_MODE_[connection id] - uno de los siguientes valores
  * userPassword - autenticar con usuario y contraseña
  * agent - autenticar con agente SSH
  * keyFile - autenticar con archivo de clave
* SSH_LOGIN_[connection id] - login SSH
* SSH_PASSWORD_[connection id] - contraseña SSH
* SSH_KEY_FILE_[connection id] - ruta completa al archivo de clave
* SSH_KEY_FILE_PASSWORD_[connection id] - frase de contraseña del archivo de clave
* USE_SSL_[connection id] - establezca el valor 1 o true cuando se deba utilizar SSL
* SSL_CA_FILE_[connection id] - ruta al archivo de certificado CA
* SSL_CERT_FILE_[connection id] - ruta al archivo de certificado
* SSL_CERT_FILE_PASSWORD_[connection id] - contraseña del archivo de clave del certificado
* SSL_KEY_FILE_[connection id] - ruta al archivo de clave
* SSL_REJECT_UNAUTHORIZED_[connection id] - establezca el valor 1 o true si se deben rechazar las conexiones no autorizadas
* SSL_TRUST_CERTIFICATE_[connection id] - establezca el valor 1 o true para configurar la opción trustServerCertificate de MSSQL
* SETTINGS_[settings key] - preconfigurar un valor de ajuste. La clave del ajuste se puede consultar en el código fuente, https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - ruta al archivo de socket, si se conecta mediante socket
* AUTH_TYPE_[connection id] - tipo de autenticación
  * hostPort (predeterminado)
  * socket - el valor se establece implícitamente al configurar SOCKET_PATH
  * tedious - autenticación portable predeterminada para MS SQL, usando el driver tedious
  * sspi - autenticación integrada de Windows (solo Windows, MS SQL), usando el driver nativo de MSSQL
  * sql - autenticación SQL (solo Windows, MS SQL), usando el driver nativo de MSSQL
* ALLOWED_DATABASES_[connection id] - nombres de bases de datos permitidos para la conexión especificada, separados por barra vertical ("|")
* ALLOWED_DATABASES_REGEX_[connection id] - expresión regular para los nombres de bases de datos permitidos para la conexión especificada
* USE_SEPARATE_SCHEMAS_[connection id] - establezca el valor 1 o true para cargar los esquemas por separado. Utilice esto si tiene esquemas grandes.
* LOCAL_DATA_CENTER_[connection id] - centro de datos local (para Apache Cassandra)
* CONNECTION_[connection id]_parameterName - establecer un nombre de parámetro específico del motor

SettingsModal.svelte , busque la cadena "name="/ Si necesita definir "true", utilice el valor "1". Si necesita "false", utilice una cadena vacía ("0" no funcionará)

## Configuración de roles
Esta configuración solo se puede utilizar en la edición Team Premium, cuando se usa una base de datos de almacenamiento para los ajustes. Los roles de las variables de entorno se importan a la base de datos de almacenamiento al iniciar el contenedor docker.
Puede definir roles con permisos específicos y asignar conexiones al rol. La asignación de roles a usuarios se realiza en la interfaz de administración.
* `ROLE_[role_name]_PERMISSIONS` - lista de permisos separados por comas para el rol indicado. Consulte la lista de permisos más abajo
* `ROLE_[role_name]_CONNECTIONS` - lista de IDs de conexión separados por comas asignados al rol indicado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - ID de conexión para el permiso de base de datos con el ID indicado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - lista de nombres de bases de datos separados por barra vertical ("|") para el permiso de base de datos con el ID indicado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - expresión regular para los nombres de bases de datos del permiso de base de datos con el ID indicado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - uno de: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - ID de conexión para el permiso de tabla con el ID indicado
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - lista de nombres de bases de datos separados por barra vertical ("|") para el permiso de base de datos con el ID indicado
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - expresión regular para los nombres de bases de datos del permiso de base de datos con el ID indicado
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - lista de nombres de esquemas separados por barra vertical ("|") para el permiso de tabla con el ID indicado
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - expresión regular para los nombres de esquemas del permiso de tabla con el ID indicado
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - lista de nombres de tablas separados por barra vertical ("|") para el permiso de base de datos con el ID indicado
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - expresión regular para los nombres de tablas del permiso de base de datos con el ID indicado
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - uno de: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - uno de: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## Permisos
De forma predeterminada, todos los permisos están disponibles. Si utiliza el prefijo \~, el permiso se revoca.

### Ejemplos
* ~*, widgets/database - se revocan todos los permisos, solo es visible el widget de base de datos
* ~widgets/*, widgets/database - se revocan todos los permisos de widgets, solo es visible el widget de base de datos
* ~connections/*, connections/con1 - todas las conexiones excepto con1 quedan ocultas y deshabilitadas

### Lista de permisos
* settings/change - permite cambiar la configuración
* plugins/install - permite instalar plugins
* widgets/[widget_name] - si no se concede, el widget queda oculto. El widget es la franja del lado izquierdo. Widgets disponibles:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - leer archivos de la carpeta indicada
* files/[folder]/write - escribir archivos en la carpeta indicada
* apps/write - guardar en el contenido de apps
* archive/write - guardar en el contenido del archivo (archive)
* connections/[connection_id] - permitir ver y utilizar la conexión definida
* internal-storage = acceso al almacenamiento interno (Premium)
* admin/auth - Administración - pestaña Autenticación (Premium)
* admin/connections - Administración - pestaña Conexiones (Premium)
* admin/users - Administración - pestaña Usuarios (Premium)
* admin/roles - Administración - pestaña Roles (Premium)
* dbops/sql-template/* - plantillas SQL (p. ej. SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - generador de SQL
* dbops/sql-dump/import - importar volcado SQL
* dbops/sql-dump/export - exportar volcado SQL
* dbops/query - ejecutar consulta SQL
* dbops/import - importar datos
* dbops/export - exportar datos
* dbops/charts - ver gráficos
* dbops/profiler - profiler de base de datos
* dbops/createdb - crear base de datos
* dbops/dropdb - eliminar base de datos
* dbops/model/view - ver el modelo de base de datos (diagramas, JSON)
* dbops/model/edit - editar el modelo de base de datos (crear/modificar tablas, vistas, etc.)
* dbops/model/compare - comparar modelos de bases de datos
* dbops/table/rename - renombrar tabla
* dbops/table/truncate - vaciar tabla (truncate)
* dbops/table/backup - crear copia de seguridad de tabla

