---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: es
title: Conexiones API
weight: 10
---

DbGate admite conexiones a APIs REST, servicios GraphQL y endpoints OData. Estas conexiones API utilizan los mismos patrones de interfaz que las conexiones a bases de datos, lo que le permite trabajar con APIs y bases de datos en un entorno unificado.

La compatibilidad con conexiones API está disponible en DbGate Premium.

> ¿Busca navegar por APIs sin la aplicación de escritorio? [DbGate Central](/es/dbgate-central/connecting-to-api-endpoints/) es una implementación independiente y alojada de conexiones GraphQL/oData/Shopify, reimplementada desde cero para el navegador.

## GraphQL

Las conexiones GraphQL le permiten interactuar con APIs GraphQL. DbGate proporciona capacidades de introspección de esquemas y ejecución de consultas.

### Crear una conexión GraphQL

Para crear una conexión GraphQL, use el diálogo New Connection y seleccione GraphQL como tipo de conexión. Introduzca la URL del endpoint de GraphQL y configure la autenticación si es necesario.

### Introspección del esquema

DbGate detecta automáticamente el esquema de GraphQL, incluidos los tipos, consultas y mutaciones disponibles, junto con sus argumentos. El explorador de esquemas muestra el sistema de tipos y le permite explorar la estructura de la API.

### Editor de consultas

El editor de consultas GraphQL le permite escribir consultas y mutaciones. Puede usar el explorador de GraphQL para construir consultas seleccionando campos y argumentos del esquema.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Variables

Las consultas GraphQL admiten variables. Defina las variables en el panel de variables y haga referencia a ellas en sus consultas usando la sintaxis estándar de variables de GraphQL. Las variables se pueden editar en un formulario o como JSON sin formato.

### Visor de respuestas

Los resultados de las consultas se muestran en un visor JSON formateado con una estructura de árbol expandible. Si se detectan arrays en la respuesta, se muestra automáticamente la vista tabular. Puede volver a la vista JSON sin formato si lo necesita.

## OpenAPI (Swagger)

Las conexiones OpenAPI admiten APIs REST que proporcionan especificaciones OpenAPI (versiones 2.0 y 3.0).

### Crear una conexión OpenAPI

Cree una nueva conexión y seleccione OpenAPI como tipo de conexión. Proporcione la URL del archivo de especificación OpenAPI (normalmente swagger.json u openapi.json). DbGate analizará la especificación y pondrá a disposición todos los endpoints documentados.

### Explorador de documentación de la API

El explorador de OpenAPI muestra todos los endpoints disponibles, organizados por etiquetas y rutas. Para cada endpoint, puede ver:
- Método HTTP (GET, POST, PUT, DELETE, PATCH)
- Parámetros (ruta, consulta, cabecera, cuerpo)
- Esquemas del cuerpo de la petición
- Descripciones de la documentación

### Ejecución de peticiones

Seleccione un endpoint para abrir el constructor de peticiones. Rellene los parámetros, cabeceras y el cuerpo de la petición requeridos. Ejecute la petición para enviarla al servidor de la API.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Inspección de la respuesta

Vea el código de estado, las cabeceras y el cuerpo de la respuesta. Las respuestas JSON se formatean y se pueden mostrar tanto en vista de árbol como de tabla. Las respuestas que no son JSON se muestran como texto.

## OData

Las conexiones OData permiten consultar servicios OData usando la sintaxis estándar de consultas OData.

### Crear una conexión OData

Cree una nueva conexión con OData como tipo de conexión. Introduzca la URL raíz del servicio OData. DbGate recuperará el documento de metadatos del servicio.

### Exploración de metadatos

El explorador de metadatos muestra los conjuntos de entidades, tipos de entidad, propiedades y relaciones definidos en los metadatos del servicio.

### Ejecución de consultas

Las consultas OData admiten las opciones de consulta estándar de OData:
- `$filter` - filtra entidades por valores de propiedades
- `$select` - especifica qué propiedades devolver
- `$expand` - incluye entidades relacionadas
- `$orderby` - ordena los resultados
- `$top` y `$skip` - paginación
- `$count` - incluye el número de resultados

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

Los resultados se muestran en formato tabular, de forma similar a los resultados de consultas a bases de datos.

## Autenticación

Todos los tipos de conexión API admiten varios métodos de autenticación:

- **API Key** - especifique el nombre y el valor de la clave, enviada como cabecera o parámetro de consulta
- **Bearer Token** - tokens OAuth o JWT enviados en la cabecera Authorization
- **Basic Authentication** - nombre de usuario y contraseña usando HTTP Basic Auth
- **Sin autenticación** - para APIs públicas

Configure la autenticación en las propiedades de la conexión.

## Exportación de datos

Los datos de las respuestas de la API se pueden exportar a varios formatos usando la funcionalidad de exportación estándar de DbGate:
- JSON
- CSV
- Excel
- Sentencias SQL INSERT
- XML

Use la opción "Export" del menú contextual estándar en el explorador de datos tabulares.

## Trabajar con varias APIs

Puede crear conexiones a varias APIs y bases de datos. Abra varias pestañas de peticiones para trabajar con distintos endpoints simultáneamente.

El estado de las pestañas se conserva después de cerrar y reabrir la aplicación; puede reabrir una petición desde el historial de pestañas cerradas.
