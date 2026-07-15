---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: es
title: Desarrollo de plugins
weight: 30
---

DbGate permite crear plugins. Gracias al asistente de plugins, es realmente sencillo crear un plugin básico. Los plugins de DbGate son paquetes NPM (JavaScript), pueden tener dependencias. (pero no dependencias nativas)

Actualmente hay 3 tipos de plugins:
- Plugin de tema
- Plugin de formato de archivo
- Plugin de controlador de base de datos

## Instalar los prerrequisitos
Necesitas tener instalado [node.js](https://nodejs.org).

También necesitarás [Yeoman](https://yeoman.io/) y el [generador de plugins de DbGate](https://www.npmjs.com/package/generator-dbgate) para Yeoman:

```sh
npm install -g yo
npm install -g generator-dbgate
```

## Crear un plugin
Ejecuta el siguiente comando en la consola:

```sh
yo dbgate
```

Tienes que responder 3 preguntas:
- Nombre del plugin, debe empezar por dbgate-plugin-, p. ej. dbgate-plugin-myplugin
- Tipo de plugin, elige p. ej. "Database driver"
- Gestor de paquetes, elige npm o yarn, el que prefieras. DbGate usa yarn.

## Editar y probar el plugin
Abre algún editor, la opción recomendada es [Visual Studio Code](https://code.visualstudio.com/)  .
El plugin de tema contiene un único archivo fuente, src/index.js. Puedes modificar los colores del tema como quieras. El atributo themeName es el nombre que se muestra en el selector de temas de DbGate.

Cuando quieras ver tu nuevo tema, ejecuta esto desde la consola (desde el directorio del plugin):
```sh
yarn plugin
```
o si usas npm, entonces
```sh
npm run plugin
```
Este comando instala tu plugin en la instancia de DbGate instalada localmente (o lo actualiza cuando haces cambios). Tras reiniciar DbGate, deberías ver el nuevo tema.  
No es necesario reiniciar, basta con recargar la aplicación (menú View/Reload) para usar la nueva versión del plugin después de ejecutar "yarn plugin"

## Eliminar un plugin
Puedes desinstalar el plugin desde el widget de plugins de DbGate. O usando el siguiente comando:
```sh
yarn plugout
```

## Publicar un plugin
El plugin es un paquete NPM normal, puedes publicarlo en el repositorio NPM. Después de publicarlo, estará disponible para todos los usuarios de DbGate en el widget "Plugins".

## Icono del plugin
Cada plugin se representa con un icono en la lista de extensiones. NPM no admite iconos para los paquetes NPM, así que el icono puede ir en el campo description del archivo package.json con la siguiente sintaxis:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Si usas el generador de Yeoman, te ayudará un poco con esto.

## Crear un plugin de controlador de base de datos
Crear un plugin de controlador es muy similar, solo que seleccionas "Database driver plugin". Después de `yarn plugin` deberías poder definir una conexión usando tu nuevo controlador y ver una lista ficticia de bases de datos y de tablas.

Puedes crear un controlador sencillo con funcionalidad básica muy rápidamente, las funciones más complejas se pueden implementar más tarde.

La creación de un controlador puede constar de los siguientes pasos:
* encontrar el paquete de nodejs (controlador) apropiado. Elige un paquete de JavaScript puro si es posible. Los paquetes nativos son una gran complicación, ese paquete nativo debe añadirse a la distribución de DbGate y además puedes esperar problemas con la compilación en distintas plataformas. Por otro lado, los paquetes de JavaScript puro funcionan normalmente sin problemas en todas las plataformas, sin necesidad de cambiar DbGate.
* definir los campos de la conexión en frontend/driver.js, función showConnectionField
* implementar la función connect en backend/driver.js
* implementar la función getVersion en backend/driver.js (opcional, pero una vez hecho, ya puedes probar la conexión con el botón "Test" en la pestaña de conexión)
* implementar el método _rynAnalysis en la clase backend/Analyser.js. Este método debe devolver la estructura de la base de datos.
* implementar el método query en backend/driver.js. Después de esto, deberías poder ver la lista de tablas y explorar los datos de las tablas
* implementar los demás métodos. Usa otros plugins de controladores como inspiración, el plugin más típico es probablemente el plugin de PostgreSQL, https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
