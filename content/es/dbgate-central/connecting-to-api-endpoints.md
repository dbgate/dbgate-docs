---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: es
title: Conexión a endpoints de API
weight: 10
---

DbGate Central se conecta a tres familias de endpoints de API, utilizando el mismo diálogo Nueva conexión para todas ellas.

## Tipos de endpoints admitidos

* **GraphQL** - inspecciona el esquema, explora los tipos y ejecuta consultas contra cualquier API de GraphQL.
* **oData** - trabaja con servicios oData V4 como si fueran tablas normales.
* **Shopify** - conéctate a tu tienda a través de la Shopify Admin API y explora productos, pedidos, clientes, metafields y mucho más.

## Crear una conexión

Abre el diálogo **Nueva conexión**, elige el tipo de conexión, introduce la URL del servicio y selecciona el método de autenticación:

* **Ninguna** - para endpoints abiertos y públicos.
* **Basic** - nombre de usuario y contraseña.
* **Bearer token** - pega un token de acceso.
* **API key** - envía una clave en una cabecera o en un parámetro de consulta.

Las conexiones se guardan en tu espacio de trabajo, de modo que estarán ahí la próxima vez que inicies sesión, en cualquier dispositivo, sin necesidad de configurar nada localmente.

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
