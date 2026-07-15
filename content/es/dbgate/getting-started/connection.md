---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: es
title: Conexión
weight: 20
---

Conectarse a la base de datos desde DbGate es sencillo. Puede conectarse a una base de datos de varias formas:

* Menú Archivo/Añadir conexión o el icono {{< mdi "plus-thick" >}} en el widget CONEXIONES
* Menú Archivo/Nueva base de datos SQLite: crea una nueva base de datos SQLite
* Menú Archivo/Abrir: puede abrir una base de datos SQLite existente

## Pantalla de conexión
![Pantalla de conexión](https://media.dbgate.io/img/new-connection-light.png)

Los campos de la pantalla de conexión dependen en gran medida del tipo de conexión.

Algunos campos comunes:

* Servidor: nombre de host del servidor de base de datos
* Puerto: puerto; en caso del puerto predeterminado de la base de datos, puede dejarlo vacío
* Usuario, Contraseña: autenticación
* Modo de contraseña
    * Guardar y cifrar: la contraseña se guarda cifrada, no podrá verla la próxima vez
    * Guardar sin cifrar: la contraseña se guarda tal cual (sin cifrar), podrá consultarla más adelante
    * No guardar, preguntar la contraseña: la contraseña no se guarda, tiene que introducirla al conectarse
    * No guardar, preguntar el usuario y la contraseña: no se guardan ni la contraseña ni el usuario, tiene que introducir ambos al conectarse
* Es de solo lectura: la conexión será de solo lectura (en motores sin soporte para sesiones de solo lectura, en este caso no podrá ejecutar consultas SQL)
* Base de datos predeterminada: qué base de datos estará activa tras la conexión
* Usar solo la base de datos *&lt;base de datos predeterminada&gt;*: si está marcado, solo aparece la base de datos predeterminada en el árbol de conexiones (las demás bases de datos del servidor quedan ocultas)
* Nombre para mostrar: nombre con el que aparecerá la conexión en la aplicación

## Túnel SSH
Aquí puede configurar la conexión a través de un túnel SSH.

Campos comunes:
* Usar túnel SSH: márquelo para usar un túnel SSH
* Host: nombre de host del servidor SSH

![DbGate - configuración del túnel SSH](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
Configure la conexión SSL.

Campos comunes:
* Usar SSL: márquelo para usar SSL. En la mayoría de los casos, esto es lo único que tiene que configurar para usar SSL

![DbGate - configuración de la conexión SSL](https://media.dbgate.io/img/connection-ssl-window-light.png)
