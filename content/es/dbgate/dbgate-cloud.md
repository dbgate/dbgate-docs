---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: es
title: DbGate Cloud
weight: 80
---

DbGate Cloud es un almacenamiento en línea para sus conexiones, scripts SQL y otros objetos. Además, ofrece una base de conocimiento pública de scripts SQL útiles.

> DbGate Cloud es un complemento de almacenamiento para la aplicación DbGate de **escritorio** (conexiones, scripts SQL, carpetas compartidas). ¿Busca en su lugar una aplicación alojada, solo para navegador? Consulte [DbGate Central](/es/dbgate-central/).

## Iniciar sesión
Para usar DbGate Cloud, es necesario iniciar sesión. Utilice el icono {{< mdi "account-remove-outline" >}} en el panel izquierdo.

Su almacenamiento en la nube siempre está asociado a su dirección de correo electrónico.  
Puede elegir uno de los siguientes proveedores de autenticación:
* GMail
* GitHub
* Correo electrónico: se enviará a su correo un enlace mágico de inicio de sesión de un solo uso

Los servidores de DbGate no almacenan su contraseña.

## Usar conexiones almacenadas en la nube
Su contenido en la nube aparece bajo el widget {{< mdi "cloud-key" >}} después de iniciar sesión. De forma predeterminada, ve su carpeta Private (con acceso de escritura).

Guardar una conexión en la nube:
* En el menú contextual de la conexión, elija "Copy to cloud folder"
* Haga clic en {{<mdi "plus-thick" >}} y luego elija "Add connection on cloud"

## ¿Qué conexión está almacenada en la nube?
* Sus conexiones en la nube están siempre bajo el widget {{< mdi "cloud-key" >}}
* Sus conexiones almacenadas localmente están bajo el widget {{< mdi "database" >}}

## Trabajar con carpetas
Puede crear más carpetas además de su carpeta Private (se necesita la edición Premium).

Bajo el botón {{<mdi "plus-thick" >}} están disponibles los comandos:
* New shared folder: crea una nueva carpeta compartida. De forma predeterminada, solo usted tiene acceso a ella; puede invitar a más usuarios
* Add existing shared folder: si tiene un enlace de invitación a alguna carpeta compartida (creada por otro usuario), este es el lugar adecuado para usarlo

Si desea compartir su carpeta con otras personas, haga clic con el botón derecho en la carpeta y elija "Copy invite link"

## Permisos de carpetas compartidas
* Admin: tiene acceso completo a la carpeta, puede invitar a otras personas y escribir contenido
* Write: puede escribir/eliminar contenido, pero no puede invitar a otras personas
* Read: solo lectura del contenido de la carpeta. Tenga en cuenta que este permiso no se aplica a las bases de datos disponibles dentro de una conexión definida a nivel de servidor

## Carpetas compartidas en la edición Community
En la edición Community, puede usar carpetas compartidas creadas por usuarios Premium, pero no puede crear sus propias carpetas compartidas. Esto está pensado para permitir que los equipos con la edición Premium compartan conexiones, archivos SQL y diagramas ER con otros miembros del equipo que usan la edición Community.

## Base de conocimiento pública
La base de conocimiento pública es una colección de scripts SQL y gráficos útiles para tareas como el ajuste de rendimiento de SQL, el análisis de deadlocks, el uso de índices, etc. La base de conocimiento está disponible en todas las ediciones, pero los gráficos solo están disponibles en las ediciones Premium.

Puede ver todos los elementos bajo el icono {{< mdi "cloud-search" >}} en el panel de widgets izquierdo.  
Los scripts atenuados en gris indican scripts que no son compatibles con la base de datos seleccionada actualmente.

Si desea ampliar la base de conocimiento con sus scripts SQL, cree una pull request en el repositorio GIT [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base).

Los scripts de la base de conocimiento están anotados con la sintaxis [SQL front matter](/es/dbgate/developer/sql-front-matter)

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)

